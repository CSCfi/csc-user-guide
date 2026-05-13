{{- define "networking.redundantHost" -}}
{{- "2.rahtiapp.fi" | printf "%s.%s" (include "docs-csc.name" .) }}
{{- end -}}

{{- define "networking.productionRouteName" -}}
{{- .Values.site.host | replace "." "-" }}
{{- end -}}

{{/*
A single route.

Expects a list where
- [0] is the root context
- [1] is a dict of type {
    "name": <Name of the this Route object>,
    "host": <Hostname>,
    "path": <Subpath>,
    "service": <Name of a Service object>,
    (optional) "cert": {
      "content": <The certificate>,
      "key": <The private key>,
      "caCert": <The CA certificate>
    }
  }

*/}}
{{- define "networking.route" -}}
{{- $ := 0 | index . -}}
{{- $route := 1 | index . -}}
kind: Route
apiVersion: route.openshift.io/v1
metadata:
  name: {{ $route.name }}
  labels:
{{ $ | include "docs-csc.labels" | indent 4 }}
spec:
  host:  {{ $route.host }}
  path: {{ $route.path }}
  to:
    kind: Service
    name: {{ $route.service }}
    weight: 100
  port:
    targetPort: 8000-tcp
  tls:
    termination: edge
    insecureEdgeTerminationPolicy: Redirect
{{- if hasKey $route "cert" }}
{{- with $route.cert }}
    certificate: |-
{{ .content | indent 6 }}
    key: |-
{{ .key | indent 6 }}
    caCertificate: |-
{{ .caCert | indent 6 }}
{{- end -}}
{{- end -}}
{{- end -}}
