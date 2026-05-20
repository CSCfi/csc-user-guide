{{/*
Used for passing translation from translator to site builder container.
*/}}
{{- define "translation.translationsVolumeName" -}}
translations
{{- end -}}
{{- define "translation.translationsVolume" -}}
- name: {{ include "translation.translationsVolumeName" . }}
  emptyDir: {}
{{- end -}}

{{/*
Used for serving the translated sites.
*/}}
{{- define "translation.buildsVolumeName" -}}
builds
{{- end -}}
{{- define "translation.buildsVolume" -}}
- name: {{ include "translation.buildsVolumeName" . }}
  persistentVolumeClaim:
    claimName: {{ include "docs-csc.altClaimName" . }}
{{- end -}}

{{/*
Helper template for volumes.
*/}}
{{- define "translation.volumes" -}}
{{ include "translation.translationsVolume" . }}
{{ include "translation.buildsVolume" . }}
{{- end -}}

{{/*
Translator workload for single language. Translates source files and builds site.

Expects a list where
- [0] is the root context
- [1] is a dict of type {
  "code": <language code>,
  (optional) "matomoId": <Matomo site id>
}

TODO:
- Fix entrypoint.translator.bash so it doesn't require CONFIG_BRANCH to be set.

*/}}
{{- define "translation.jobSpec" -}}
{{- $ := index . 0 -}}
{{- $langcode := (1 | index .).code -}}
{{- $matomourl := $.Values.site.matomoUrl -}}
{{- $matomoid := (1 | index .).matomoId -}}
{{- $translatorname := $ | include "docs-csc.translatorName" -}}
{{- $buildername := $ | include "docs-csc.altBuilderName" -}}
{{- $secretname := $ | include "docs-csc.translatorSecretName" -}}
{{- $translator := $.Values.translator -}}
{{- $host := $.Values.site.host | default ($ | include "networking.redundantHost") -}}
metadata:
  labels:
{{ $ | include "docs-csc.labels" | indent 4 }}
  annotations:
{{ $ | include "docs-csc.annotations" | indent 4 }}
spec:
  restartPolicy: Never
  volumes:
{{ include "translation.volumes" $ | indent 4 }}
  initContainers:
    - name: {{ $langcode | printf "%s-%s" $translatorname }}
      image: {{ "latest" | printf "%s:%s" $translatorname | squote }}
      imagePullPolicy: Always
      volumeMounts:
        - name: {{ $ | include "translation.translationsVolumeName" }}
          mountPath: /translations
      env:
        - name: CONFIG_BRANCH
          value: {{ $translator.configBranchOverride | default $.Values.git.ref | squote }}
        - name: LANG_CODE
          value: {{ $langcode | squote }}
        - name: RESTORE_ONLY
          value: {{ $.Values.translator.restoreOnly | default false | squote }}
{{- with $translator.restic }}
        - name: RESTIC_REPOSITORY
          value: {{ .repository | squote }}
        - name: RESTIC_HOST
          value: {{ .host | squote }}
{{- end }}
        - name: RESTIC_PASSWORD
          valueFrom:
            secretKeyRef:
              name: {{ $secretname }}
              key: resticPassword
        - name: OS_AUTH_URL
          value: {{ $translator.os.authUrl | squote }}
        - name: OS_APPLICATION_CREDENTIAL_ID
          valueFrom:
            secretKeyRef:
              name: {{ $secretname }}
              key: osApplicationCredentialId
        - name: OS_APPLICATION_CREDENTIAL_SECRET
          valueFrom:
            secretKeyRef:
              name: {{ $secretname }}
              key: osApplicationCredentialSecret
        - name: OPENAI_API_KEY
          valueFrom:
            secretKeyRef:
              name: {{ $secretname }}
              key: openAiApiKey
{{- with $translator.cache }}
        - name: CACHE_CONTAINER
          value: {{ .container | squote }}
        - name: CACHE_PREFIX
          value: {{ .prefix | squote }}
{{- end }}
  containers:
    - name: {{ $langcode | printf "%s-%s" $buildername }}
      image: {{ "latest" | printf "%s:%s" $buildername | squote }}
      env:
{{- if $.Values.site.configBranchOverride }}
        - name: CONFIG_BRANCH
          value: {{ $.Values.site.configBranchOverride | squote }}
{{- end }}
        - name: PROPERDOCS_ENV
          value: {{ $ | include "docs-csc.environment" | squote }}
        - name: LANG_CODE
          value: {{ $langcode | squote }}
        - name: SITE_URL
          value: {{ dict "scheme" "https"
                         "host" $host
                         "path" $langcode
                    | urlJoin | squote }}
{{- if $matomoid | and $matomourl }}
        - name: MATOMO_URL
          value: {{ $matomourl | squote }}
        - name: MATOMO_SITE_ID
          value: {{ $matomoid | squote }}
{{- end }}
      volumeMounts:
        - name: {{ include "translation.translationsVolumeName" $ }}
          mountPath: /translations
        - name: {{ include "translation.buildsVolumeName" $ }}
          mountPath: {{ $langcode | printf "/site/%s" }}
          subPath: {{ $langcode }}
{{- end }}
