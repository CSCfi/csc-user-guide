{{/*
Expand the name of the chart.
*/}}
{{- define "docs-csc.name" -}}
{{- .Values.nameOverride | default .Chart.Name | trunc 63 | trimSuffix "-" }}
{{- end }}

{{- define "docs-csc.environment" -}}
{{ .Values.environment | default "preview" }}
{{- end }}

{{/*
Create names for resources.
*/}}
{{- define "docs-csc.baseName" -}}
{{- printf "%s-base" (include "docs-csc.name" .) | trunc 63 | trimSuffix "-" }}
{{- end }}
{{- define "docs-csc.origName" -}}
{{- printf "%s-original" (include "docs-csc.name" .) | trunc 63 | trimSuffix "-" }}
{{- end }}
{{- define "docs-csc.origServerName" -}}
{{- printf "%s-server" (include "docs-csc.origName" .) | trunc 63 | trimSuffix "-" }}
{{- end }}
{{- define "docs-csc.origBuilderName" -}}
{{- printf "%s-builder" (include "docs-csc.origName" .) | trunc 63 | trimSuffix "-" }}
{{- end }}
{{- define "docs-csc.altName" -}}
{{- printf "%s-alternate" (include "docs-csc.name" .) | trunc 63 | trimSuffix "-" }}
{{- end }}
{{- define "docs-csc.altConfigName" -}}
{{- printf "%s-nginx-location" (include "docs-csc.altName" .) | trunc 63 | trimSuffix "-" }}
{{- end }}
{{- define "docs-csc.altServerName" -}}
{{- printf "%s-server" (include "docs-csc.altName" .) | trunc 63 | trimSuffix "-" }}
{{- end }}
{{- define "docs-csc.altBuilderName" -}}
{{- printf "%s-builder" (include "docs-csc.altName" .) | trunc 63 | trimSuffix "-" }}
{{- end }}
{{- define "docs-csc.altVolumeClaimName" -}}
{{- printf "%s-builds" (include "docs-csc.altName" .) | trunc 63 | trimSuffix "-" }}
{{- end }}

{{/*
Create chart name and version as used by the chart label.
*/}}
{{- define "docs-csc.chart" -}}
{{- printf "%s-%s" .Chart.Name .Chart.Version | replace "+" "_" | trunc 63 | trimSuffix "-" }}
{{- end }}

{{/*
Common labels
*/}}
{{- define "docs-csc.labels" -}}
helm.sh/chart: {{ include "docs-csc.chart" . }}
{{ include "docs-csc.selectorLabels" . }}
{{- if .Chart.AppVersion }}
app.kubernetes.io/version: {{ .Chart.AppVersion | quote }}
{{- end }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
{{- end }}

{{/*
Component labels
*/}}
{{- define "docs-csc.componentLabels" -}}
{{- $ := index . 0 -}}
{{- $resourcename := index . 1 -}}
{{- $components := keys $.Values.components -}}
{{- $rootname := include "docs-csc.name" $ -}}
{{- $componentregex := printf "^%s-([^-]+)(?:$|-)" $rootname -}}
{{- $componentname := regexReplaceAll $componentregex $resourcename "$1" -}}
{{- $iscomponent := has $componentname $components -}}
{{- $fullname := $iscomponent | ternary (printf "%s-%s" $rootname $componentname)
                                $rootname -}}
app.kubernetes.io/name: {{ $fullname }}
{{- if $iscomponent }}
app.kubernetes.io/component: {{ $componentname }}
{{- end }}
{{- end }}

{{/*
Selector labels
*/}}
{{- define "docs-csc.selectorLabels" -}}
app.kubernetes.io/instance: {{ .Release.Name }}
app.kubernetes.io/part-of: {{ include "docs-csc.name" . }}
{{- end }}

{{- define "docs-csc.latestImageName" -}}
{{- $ := index . 0 -}}
{{- $resourcename := index . 1 -}}
{{- printf "%s:latest" $resourcename }}
{{- end -}}

{{- define "docs-csc.fullImageName" -}}
{{- $ := index . 0 -}}
{{- $resourcename := index . 1 -}}
{{- $resourcename | list $
                  | include "docs-csc.latestImageName"
                  | printf "%s/%s/%s" $.Values.localRegistry $.Release.Namespace }}
{{- end -}}

{{/*
GitBuildSource
*/}}
{{- define "docs-csc.gitSource" -}}
type: Git
git:
{{- range $key, $value := .Values.git }}
  {{ $value | squote | printf "%s: %s" $key }}
{{- end -}}
{{- end }}

{{/*
Allows for deploying forks and/or development branches.

Expects a dict of type {
  (optional) "host": <Git service hostname>
  (optional) "org": <Git organization>,
  (optional) "name": <Git repository name>,
  (optional) "branch": <Git repository branch>
}

*/}}
{{- define "docs-csc.repoOverride" -}}
{{- range $name, $value := . }}
- name: {{ printf "repo_%s" $name }}
  value: {{ $value | squote }}
{{- end -}}
{{- end }}

{{/*
Lookup resource(s) on the cluster, fail if not found.

Expects a dict of named arguments to pass to the 'lookup' function.

Outputs the resource(s) as YAML.
*/}}
{{- define "docs-csc.resourceLookup" -}}
{{- lookup .apiVersion .kind .namespace .name
    | default nil
    | required (printf "Lookup for '%s' '%s' '%s' '%s' failed!"
                       .apiVersion .kind .namespace .name)
    | toYaml }}
{{- end -}}

{{- define "docs-csc.deploymentTrigger" -}}
{{- $imagename := index . 0 -}}
{{- $containername := index . 1 -}}
{{- $fieldpath := printf `spec.template.spec.containers[?(@name=="%s")].image` $containername -}}
{{-
  dict "from" (dict "kind" "ImageStreamTag"
                           "name" $imagename)
       "fieldPath" $fieldpath
  | list
  | toJson
}}
{{- end -}}
