{{- define "networking.redundantHost" -}}
{{- "2.rahtiapp.fi" | printf "%s.%s" (include "docs-csc.name" .) }}
{{- end -}}

{{- define "networking.productionRouteName" -}}
{{- .Values.site.host | replace "." "-" }}
{{- end -}}

{{/*
A single route. Attempts to lookup existing TLS certificate
if hostname does not end in ".rahtiapp.fi".

Expects a list where
- [0] is the root context
- [1] is a dict of type {
    "name": <Name of the this Route object>,
    "host": <Hostname>,
    "path": <Subpath>,
    "service": <Name of a Service object>
  }

*/}}
{{- define "networking.route" -}}
{{- $ := 0 | index . -}}
{{- $route := 1 | index . -}}
{{- $existingtls := $route.name | lookup "route.openshift.io/v1"
                                         "Route"
                                         $.Release.Namespace
                                | dig "spec" "tls" dict -}}
{{- $tlsfilename := $.Values.site.tlsFile | default "" -}}
{{- $filetls := (empty $tlsfilename | not)
                | ternary ($.Files.Get $tlsfilename | fromYaml | default dict)
                          dict
                | default dict -}}
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
{{ if $route.host | hasSuffix ".rahtiapp.fi" | not -}}
{{ range $key := list "certificate"
                      "key"
                      "caCertificate" -}}
{{ $key | printf "%s: |" | indent 4 }}
{{ $key
   | get $filetls
   | default ($key | get $existingtls)
   | required ($route.name | printf "%s is required for Route %s!" $key)
   | trim
   | indent 6 }}
{{ end -}}
{{- end -}}
{{- end -}}
