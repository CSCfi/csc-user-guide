{{- define "networking.redundantHost" -}}
{{- printf "%s.rahtiapp.fi" (include "docs-csc.name" .) }}
{{- end -}}

{{- define "networking.siteHost" -}}
{{- .Values.site.host | default (include "networking.redundantHost" .) }}
{{- end -}}

{{- define "networking.redundantIngressName" -}}
{{- printf "%s-rahtiapp" (include "docs-csc.name" .) | trunc 63 | trimSuffix "-" }}
{{- end -}}

{{- define "networking.domainIngressName" -}}
{{- .Values.site.host | required "site.host not provided!"
                      | replace "." "-"
                      | trunc 63
                      | trimSuffix "-" }}
{{- end -}}

{{- define "networking.domainTlsSecretName" -}}
{{- printf "%s-tls" (include "networking.domainIngressName" .) | trunc 63 | trimSuffix "-" }}
{{- end -}}

{{- define "networking.webHookSecretName" -}}
{{- printf "%s-webhook" (include "docs-csc.origName" .) | trunc 63 | trimSuffix "-" }}
{{- end -}}

{{- define "networking.acmeIssuerName" -}}
{{- .Values.site.acme.issuerName | required "site.acme.issuerName not provided!" -}}
{{- end -}}

{{- define "networking.acmeEabSecretName" -}}
{{- printf "%s-eab-hmac" (include "networking.acmeIssuerName" . ) | trunc 63 | trimSuffix "-" -}}
{{- end -}}

{{- define "networking.acmeAccountKeySecretName" -}}
{{- printf "%s-account-key" (include "networking.acmeIssuerName" .) | trunc 63 | trimSuffix "-" -}}
{{- end -}}

{{- define "networking.acmeFile" -}}
{{- .Values.site.acme.acmeFile | required "site.acme.acmeFile not provided!"
                               | .Files.Get }}
{{- end -}}

{{- define "networking.acmeEabSecret" -}}
{{- $ := index . 0 -}}
{{- $data := index . 1 -}}
{{- $resourcename := include "networking.acmeEabSecretName" $ -}}
kind: Secret
apiVersion: v1
metadata:
  name: {{ $resourcename }}
  labels:
{{ include "docs-csc.labels" $ | indent 4 }}
{{ $resourcename | list $ | include "docs-csc.componentLabels" | indent 4 }}
data:
  kid: {{ $data.kid | required "eabKeyID not provided!" }}
  hmac: {{ $data.hmac | required "eabHmacKey not provided!" }}
type: Opaque
{{- end -}}

{{- define "networking.issuer" -}}
{{- $ := index . 0 -}}
{{- $acme := index . 1 -}}
{{- $resourcename := include "networking.acmeIssuerName" $ -}}
apiVersion: cert-manager.io/v1
kind: Issuer
metadata:
  name: {{ $resourcename }}
  labels:
{{ include "docs-csc.labels" $ | indent 4 }}
{{ $resourcename | list $ | include "docs-csc.componentLabels" | indent 4 }}
spec:
  acme:
    email: {{ $acme.email | required "email not provided!" }}
    server: {{ $acme.server | required "server not provided!" }}
    externalAccountBinding:
      keyID: {{ $acme.externalAccountBinding.keyID | required "eabKeyID not provided!" }}
      keySecretRef:
        name: {{ include "networking.acmeEabSecretName" $ }}
        key: hmac
    privateKeySecretRef:
      name: {{ include "networking.acmeAccountKeySecretName" $ }}
    solvers:
    - http01:
        ingress:
          ingressClassName: openshift-default
{{- end -}}

{{- define "networking.certificate" -}}
{{- $ := index . 0 -}}
{{- $spec := index . 1 -}}
{{- $hostname := $.Values.site.host -}}
{{- $resourcename := include "networking.domainIngressName" $ -}}
apiVersion: cert-manager.io/v1
kind: Certificate
metadata:
  name: {{ $resourcename }}
  labels:
{{ include "docs-csc.labels" $ | indent 4 }}
{{ $resourcename | list $ | include "docs-csc.componentLabels" | indent 4 }}
spec:
  secretName: {{ include "networking.domainTlsSecretName" $ }}
  duration: {{ $spec.duration | required "Certificate duration not provided!" }}
  renewBefore: {{ $spec.renewBefore | required "Certificate renewBefore not provided!" }}
  issuerRef:
    name: {{ include "networking.acmeIssuerName" $ }}
    kind: Issuer
  commonName: {{ $hostname }}
  dnsNames:
    - {{ $hostname }}
{{- end -}}

{{- define "networking.newAcmeEabSecret" -}}
{{- $acmefile := include "networking.acmeFile" . | fromYaml -}}
{{ dict "kid" ($acmefile.eabKeyID | b64enc)
        "hmac" ($acmefile.eabHmacKey | b64enc)
   | list $
   | include "networking.acmeEabSecret" }}
{{- end -}}

{{- define "networking.newIssuer" -}}
{{- $acmefile := include "networking.acmeFile" . | fromYaml -}}
{{ dict "email" $acmefile.email
        "server" $acmefile.server
        "externalAccountBinding" (dict "keyID" $acmefile.eabKeyID)
   | list $
   | include "networking.issuer" }}
{{- end -}}

{{- define "networking.newCertificate" -}}
{{- $acmefile := include "networking.acmeFile" . | fromYaml -}}
{{ dict "duration" $acmefile.certificateDuration
        "renewBefore" $acmefile.certificateRenewBefore
   | list $
   | include "networking.certificate" }}
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
