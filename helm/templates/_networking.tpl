{{- define "networking.redundantHost" -}}
{{- printf "%s.rahtiapp.fi" (include "docs-csc.name" .) }}
{{- end -}}

{{- define "networking.siteHost" -}}
{{- .Values.site.host | default (include "networking.redundantHost" .) }}
{{- end -}}

{{- define "networking.redundantIngressName" -}}
{{- printf "%s-rahtiapp" (include "docs-csc.name" .) }}
{{- end -}}

{{- define "networking.domainIngressName" -}}
{{- .Values.site.host | default "" | replace "." "-" }}
{{- end -}}

{{- define "networking.domainTlsSecretName" -}}
{{- printf "%s-tls" (include "networking.domainIngressName" .) }}
{{- end -}}

{{- define "networking.webHookSecretName" -}}
{{- printf "%s-github-webhook" (include "docs-csc.name" .) | trunc 63 | trimSuffix "-" }}
{{- end -}}

{{- define "networking.acmeIssuerName" -}}
{{- .Values.site.acme.issuerName | required "site.acme.issuerName is required" -}}
{{- end -}}

{{- define "networking.acmeEabSecretName" -}}
{{- include "networking.acmeIssuerName" . | printf "%s-%s-eab-secret" (include "docs-csc.name" .) -}}
{{- end -}}

{{- define "networking.acmeAccountKeySecretName" -}}
{{- include "networking.acmeIssuerName" . | printf "%s-%s-account-key" (include "docs-csc.name" .) -}}
{{- end -}}

{{- define "networking.acmeFile" -}}
{{- .Values.site.acme.acmeFile | required "site.acme.acmeFile not provided!"
                               | .Files.Get }}
{{- end -}}

{{- define "networking.newAcmeEabSecret" -}}
{{- $acmefile := include "networking.acmeFile" . | fromYaml -}}
{{- $resourcename := include "networking.acmeEabSecretName" . -}}
kind: Secret
apiVersion: v1
metadata:
  name: {{ $resourcename }}
  labels:
{{ include "docs-csc.labels" .| indent 4 }}
{{ $resourcename | list $ | include "docs-csc.componentLabels" | indent 4 }}
data:
  kid: {{ $acmefile.eabKeyID | required "eabKeyID not provided!"
                             | b64enc }}
  hmac: {{ $acmefile.eabHmacKey | required "eabHmacKey not provided!"
                                | b64enc }}
type: Opaque
{{- end -}}

{{- define "networking.newAcmeAccountKeySecret" -}}
{{- $acmefile := include "networking.acmeFile" . | fromYaml -}}
{{- $resourcename := include "networking.acmeAccountKeySecretName" . -}}
kind: Secret
apiVersion: v1
metadata:
  name: {{ $resourcename }}
  labels:
{{ include "docs-csc.labels" .| indent 4 }}
{{ $resourcename | list $ | include "docs-csc.componentLabels" | indent 4 }}
data:
  tls.key: {{ $acmefile.accountKey | required "accountKey not provided!"
                                   | b64enc }}
type: Opaque
{{- end -}}

{{- define "networking.newIssuer" -}}
{{- $issuername := include "networking.acmeIssuerName" . -}}
{{- $acmefile := include "networking.acmeFile" . | fromYaml -}}
apiVersion: cert-manager.io/v1
kind: Issuer
metadata:
  name: {{ $issuername }}
  labels:
{{ include "docs-csc.labels" . | indent 4 }}
{{ include "docs-csc.name" . | list $ | include "docs-csc.componentLabels" | indent 4 }}
spec:
  acme:
    email: {{ $acmefile.email | required "email not provided!" }}
    server: {{ $acmefile.server | required "server not provided!" }}
    externalAccountBinding:
      keyID: {{ $acmefile.eabKeyID | required "eabKeyID not provided!" }}
      keySecretRef:
        name: {{ include "networking.acmeEabSecretName" . }}
        key: hmac
    disableAccountKeyGeneration: true
    privateKeySecretRef:
      name: {{ include "networking.acmeAccountKeySecretName" . }}
      key: tls.key
    solvers:
    - http01:
        ingress:
          ingressClassName: openshift-default
{{- end -}}

{{- define "networking.newCertificate" -}}
{{- $acmefile := include "networking.acmeFile" . | fromYaml -}}
{{- $resourcename := include "networking.domainIngressName" . -}}
apiVersion: cert-manager.io/v1
kind: Certificate
metadata:
  name: {{ include "networking.domainIngressName" . }}
  labels:
{{ include "docs-csc.labels" . | indent 4 }}
{{ $resourcename | list $ | include "docs-csc.componentLabels" | indent 4 }}
spec:
  secretName: {{ include "networking.domainTlsSecretName" . }}
  duration: {{ $acmefile.certificateDuration }}
  renewBefore: {{ $acmefile.certificateRenewBefore }}
  issuerRef:
    name: {{ include "networking.acmeIssuerName" . }}
    kind: Issuer
  commonName: {{ .Values.site.host }}
  dnsNames:
    - {{ .Values.site.host }}
{{- end -}}

{{- define "networking.ingressMetadata" -}}
{{- $allowfilename := .Values.site.ipAllowlistFile -}}
{{- $allowlist := $allowfilename | empty 
                                 | ternary list
                                           ((.Files.Get $allowfilename
                                             | fromYaml).ipAllowlist
                                             | required (printf "No ipAllowlist found in %s!" $allowfilename)) -}}
labels:
{{ include "docs-csc.labels" . | indent 2 }}
{{ include "docs-csc.name" . | list $ | include "docs-csc.componentLabels" | indent 2 }}
annotations:
  haproxy.router.openshift.io/redirect-to-https: 'true'
{{- if $allowlist }}
{{
  $allowlist | join " "
             | printf "%s: %q" "haproxy.router.openshift.io/ip_allowlist"
             | indent 2
}}
{{- end }}
{{- end }}

{{- define "networking.ingressRules" -}}
{{- $altservicename := .altServiceName -}}
- host: {{ .host }}
  http:
    paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: {{ .origServiceName }}
            port:
              number: 8000
{{- range .languages }}
      - path: {{ .code | printf "/%s" }}
        pathType: Prefix
        backend:
          service:
            name: {{ $altservicename }}
            port:
              number: 8000
{{- end }}
{{- end }}
