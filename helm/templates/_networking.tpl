{{- define "networking.redundantHost" -}}
{{- printf "%s.rahtiapp.fi" (include "docs-csc.name" .) }}
{{- end -}}

{{- define "networking.siteHost" -}}
{{- .Values.site.host | default (include "networking.redundantHost" .) }}
{{- end -}}

{{- define "networking.sitePath" -}}
{{- $ := index . 0 -}}
{{- $path := index . 1 -}}
{{ dict "scheme" "https"
                 "host" (include "networking.siteHost" $)
                 "path" $path
   | urlJoin
   | squote }}
{{- end -}}

{{- define "networking.ingressName" -}}
{{- .Values.site.host | required "site.host not provided!"
                      | replace "." "-"
                      | trunc 63
                      | trimSuffix "-" }}
{{- end -}}

{{- define "networking.domainTlsSecretName" -}}
{{- printf "%s-tls" (include "networking.ingressName" .) | trunc 63 | trimSuffix "-" }}
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
{{- .Values.site.acme.secretsFile
    | required "site.acme.secretsFile not provided!"
    | .Files.Get -}}
{{- end -}}

{{- define "networking.ipAllowlistAnnotation" -}}
{{- $ := index . 0 -}}
{{- $apiversion := index . 1 -}}
{{- $kind := index . 2 -}}
{{- $resourcename := index . 3 -}}
{{- if or ($.Values.site.useAllowlistLookup | default false)
          ($.Values.site.ipAllowlist | empty | not) }}
{{- $allowlistkey := "haproxy.router.openshift.io/ip_allowlist" -}}
{{- if $.Values.site.useAllowlistLookup }}
{{ lookup $apiversion
          $kind
          $.Release.Namespace
          $resourcename
   | dig "metadata" "annotations" $allowlistkey ""
   | required "ipAllowlist lookup failed!"
   | quote
   | printf "%s: %s" $allowlistkey }}
{{- else }}
{{ $.Values.site.ipAllowlist
   | join " "
   | printf "%s: %q" $allowlistkey }}
{{- end }}
{{- end }}
{{- end -}}

{{- define "networking.ingressMetadata" -}}
{{- $ := index . 0 -}}
{{- $ingressname := index . 1 -}}
name: {{ $ingressname }}
labels:
{{ include "docs-csc.labels" $ | indent 2 }}
{{ include "docs-csc.name" $ | list $ | include "docs-csc.componentLabels" | indent 2 }}
annotations:
  haproxy.router.openshift.io/redirect-to-https: 'true'
{{- list $
         "networking.k8s.io/v1"
         "Ingress"
         $ingressname
    | include "networking.ipAllowlistAnnotation"
    | indent 2 }}
{{- end }}
