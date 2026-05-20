{{/*
Expand the name of the chart.
*/}}
{{- define "docs-csc.name" -}}
{{- .Values.nameOverride | default .Chart.Name | trunc 63 | trimSuffix "-" }}
{{- end }}

{{- define "docs-csc.environment" -}}
{{ .Values.site.environment | default "preview" }}
{{- end }}

{{/*
Create names for resources.
*/}}
{{- define "docs-csc.baseName" -}}
{{- "base" | printf "%s-%s" (include "docs-csc.name" .) | trunc 63 | trimSuffix "-" }}
{{- end }}
{{- define "docs-csc.origName" -}}
{{- "original" | printf "%s-%s" (include "docs-csc.name" .) | trunc 63 | trimSuffix "-" }}
{{- end }}
{{- define "docs-csc.origContainerName" -}}
{{- "server" | printf "%s-%s" (include "docs-csc.origName" .) | trunc 63 | trimSuffix "-" }}
{{- end }}
{{- define "docs-csc.origBuilderName" -}}
{{- "builder" | printf "%s-%s" (include "docs-csc.origName" .) | trunc 63 | trimSuffix "-" }}
{{- end }}
{{- define "docs-csc.origWebHookSecretName" -}}
{{- "github-webhook" | printf "%s-%s" (include "docs-csc.origName" .) | trunc 63 | trimSuffix "-" }}
{{- end }}
{{- define "docs-csc.altName" -}}
{{- "alternate" | printf "%s-%s" (include "docs-csc.name" .) | trunc 63 | trimSuffix "-" }}
{{- end }}
{{- define "docs-csc.altConfigName" -}}
{{- "nginx-location" | printf "%s-%s" (include "docs-csc.altName" .) | trunc 63 | trimSuffix "-" }}
{{- end }}
{{- define "docs-csc.altContainerName" -}}
{{- "server" | printf "%s-%s" (include "docs-csc.altName" .) | trunc 63 | trimSuffix "-" }}
{{- end }}
{{- define "docs-csc.altBuilderName" -}}
{{- "builder" | printf "%s-%s" (include "docs-csc.altName" .) | trunc 63 | trimSuffix "-" }}
{{- end }}
{{- define "docs-csc.altClaimName" -}}
{{- "builds" | printf "%s-%s" (include "docs-csc.altName" .) | trunc 63 | trimSuffix "-" }}
{{- end }}
{{- define "docs-csc.translatorName" -}}
{{- "translator" | printf "%s-%s" (include "docs-csc.name" .) | trunc 63 | trimSuffix "-" }}
{{- end }}
{{- define "docs-csc.translatorSecretName" -}}
{{- "secret" | printf "%s-%s" (include "docs-csc.translatorName" .) | trunc 63 | trimSuffix "-" }}
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
environment: {{ include "docs-csc.environment" . }}
{{- end }}

{{/*
Selector labels
*/}}
{{- define "docs-csc.selectorLabels" -}}
app.kubernetes.io/name: {{ include "docs-csc.name" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
{{- end }}

{{- define "docs-csc.annotations" -}}
meta.helm.sh/release-name: {{ .Release.Name }}
meta.helm.sh/release-namespace: {{ .Release.Namespace }}
{{- end }}

{{/*
Image names for build_args
*/}}
{{- define "docs-csc.latestBaseImage" -}}
{{- "latest" | printf "%s/%s/%s:%s" .Values.localRegistry .Release.Namespace (include "docs-csc.baseName" .) }}
{{- end }}
{{- define "docs-csc.latestBuilderImage" -}}
{{- "latest" | printf "%s/%s/%s:%s" .Values.localRegistry .Release.Namespace (include "docs-csc.origBuilderName" .) }}
{{- end }}
{{- define "docs-csc.latestAltBuilderImage" -}}
{{- "latest" | printf "%s/%s/%s:%s" .Values.localRegistry .Release.Namespace (include "docs-csc.altBuilderName" .) }}
{{- end }}
{{- define "docs-csc.latestTranslatorImage" -}}
{{- "latest" | printf "%s/%s/%s:%s" .Values.localRegistry .Release.Namespace (include "docs-csc.translatorName" .) }}
{{- end }}

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
  (optional) "org": <GitHub organization>,
  (optional) "name": <GitHub repository name>,
  (optional) "branch": <GitHub repository branch>
}

Outputs key-value pairs used in buildArgs.

*/}}
{{- define "docs-csc.repoOverride" -}}
{{- range $name, $value := . }}
- name: {{ $name | printf "repo_%s" }}
  value: {{ $value | squote }}
{{- end -}}
{{- end }}