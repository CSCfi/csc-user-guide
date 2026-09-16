{{- define "translation.translatorName" -}}
{{- printf "%s-translator" (include "docs-csc.name" .) | trunc 63 | trimSuffix "-" }}
{{- end -}}

{{- define "translation.translatorSecretName" -}}
{{- printf "%s-secret" (include "translation.translatorName" .) | trunc 63 | trimSuffix "-" }}
{{- end -}}

{{- define "translation.latestTranslatorImage" -}}
{{- printf "%s/%s/%s:latest" .Values.localRegistry
                             .Release.Namespace
                             (include "translation.translatorName" .) }}
{{- end -}}

{{/*
Volume for passing translation from translator to site builder container.
*/}}
{{- define "translation.ephemeralVolumeName" -}}
translations
{{- end -}}

{{- define "translation.translationsVolume" -}}
- name: {{ include "translation.ephemeralVolumeName" . }}
  emptyDir: {}
{{- end -}}

{{/*
Volume for serving the translated sites.
*/}}
{{- define "translation.buildsVolumeName" -}}
builds
{{- end -}}

{{- define "translation.buildsVolume" -}}
- name: {{ include "translation.buildsVolumeName" . }}
  persistentVolumeClaim:
    claimName: {{ include "docs-csc.altVolumeClaimName" . }}
{{- end -}}

{{- define "translation.volumes" -}}
{{ include "translation.translationsVolume" . }}
{{ include "translation.buildsVolume" . }}
{{- end -}}

{{- define "translation.translatorMounts" -}}
- name: {{ include "translation.ephemeralVolumeName" . }}
  mountPath: /translations
{{- end -}}

{{- define "translation.secretsFile" -}}
{{- .Values.components.translator.secretsFile
    | required "translator.secretsFile not provided!"
    | .Files.Get -}}
{{- end -}}

{{- define "translation.newTranslatorSecret" -}}
{{- $secretsfile := include "translation.secretsFile" . | fromYaml -}}
{{- $requiredkeys := list "openAiApiKey"
                          "resticPassword"
                          "osApplicationCredentialId"
                          "osApplicationCredentialSecret" -}}
kind: Secret
apiVersion: v1
metadata:
  name: {{ include "translation.translatorSecretName" $ }}
  labels:
{{ include "docs-csc.labels" $ | indent 4 }}
{{ include "translation.translatorName" $ | list $ | include "docs-csc.componentLabels" | indent 4 }}
type: Opaque
data:
{{- range $key := .Values.components.translator.restoreOnly
                  | ternary ("openAiApiKey" | without $requiredkeys)
                            $requiredkeys }}
  {{ $key | get $secretsfile
          | required (printf "%s not provided!" $key)
          | b64enc
          | printf "%s: %s" $key }}
{{- end -}}
{{- end -}}

{{- define "translation.translatorContainer" -}}
{{- $ := index . 0 -}}
{{- $args := index . 1 -}}
{{- $secretname := include "translation.translatorSecretName" $ -}}
- name: {{ $args.languageCode | printf "%s-%s" (include "translation.translatorName" $) }}
  image: {{ include "translation.latestTranslatorImage" $ | squote }}
  imagePullPolicy: Always
  env:
{{- if $args.configBranchOverride }}
    - name: CONFIG_BRANCH
      value: {{ $args.configBranchOverride | squote }}
{{- end }}
    - name: LANG_CODE
      value: {{ $args.languageCode | squote }}
    - name: LANG_NAME
      value: {{ $args.languageName | squote }}
    - name: RESTORE_ONLY
      value: {{ $args.restoreOnly | toString | squote }}
    - name: RESTIC_REPOSITORY
      value: {{ $args.resticRepository | squote }}
    - name: RESTIC_HOST
      value: {{ $args.resticHost | squote }}
    - name: RESTIC_PASSWORD
      valueFrom:
        secretKeyRef:
          name: {{ $secretname }}
          key: resticPassword
    - name: OS_AUTH_URL
      value: {{ $args.osAuthUrl | squote }}
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
{{- if $.Values.components.translator.restoreOnly | default false | not }}
    - name: OPENAI_API_KEY
      valueFrom:
        secretKeyRef:
          name: {{ $secretname }}
          key: openAiApiKey
{{- end }}
    - name: CACHE_CONTAINER
      value: {{ $args.cacheContainer | squote }}
    - name: CACHE_PREFIX
      value: {{ $args.cachePrefix | squote }}
  volumeMounts:
{{ include "translation.translatorMounts" $ | indent 4 }}
{{- end -}}

{{- define "translation.buildContainer" -}}
{{- $ := index . 0 -}}
{{- $args := index . 1 -}}
{{- $buildsvolumename := include "translation.buildsVolumeName" $ -}}
- name: {{ $args.languageCode | printf "%s-%s" (include "docs-csc.altBuilderName" $) }}
  image: {{ include "docs-csc.altBuilderName" $ | list $ | include "docs-csc.latestImageName" | squote }}
  env:
{{- if $args.configBranchOverride }}
    - name: CONFIG_BRANCH
      value: {{ $args.configBranchOverride | squote }}
{{- end }}
    - name: PROPERDOCS_ENV
      value: {{ include "docs-csc.environment" $ | squote }}
    - name: LANG_CODE
      value: {{ $args.languageCode | squote }}
    - name: SITE_URL
      value: {{ dict "scheme" "https"
                      "host" (include "networking.siteHost" $)
                      "path" $args.languageCode
                | urlJoin
                | squote }}
{{- if $args.matomoSiteId | and $args.matomoUrl }}
    - name: MATOMO_URL
      value: {{ $args.matomoUrl | squote }}
    - name: MATOMO_SITE_ID
      value: {{ $args.matomoSiteId | squote }}
{{- end }}
  volumeMounts:
    - name: {{ $buildsvolumename }}
      mountPath: {{ $args.languageCode | printf "/site/%s" }}
      subPath: {{ $args.languageCode | printf "builds/%s" }}
    - name: {{ $buildsvolumename }}
      mountPath: /work/.cache
      subPath: cached_assets
{{ include "translation.translatorMounts" $ | indent 4 }}
{{- end -}}

{{- define "translation.jobTemplate" -}}
{{- $ := index . 0 -}}
{{- $args := index . 1 -}}
{{- $translatorrestic := $.Values.components.translator.restic | default dict -}}
{{- $translatorcache := $.Values.components.translator.cache | default dict -}}
metadata:
  labels:
{{ include "docs-csc.labels" $ | indent 4 }}
{{ include "translation.translatorName" $ | list $ | include "docs-csc.componentLabels" | indent 4 }}
spec:
  restartPolicy: Never
  volumes:
{{ include "translation.volumes" $ | indent 4 }}
  initContainers:
{{ dict "languageCode" $args.language.code
        "languageName" $args.language.name
        "restoreOnly" $args.restoreOnly
        "configBranchOverride" ($.Values.components.translator.configBranchOverride | default nil)
        "resticRepository" ($translatorrestic.repository | required "translator.restic.repository not provided!")
        "resticHost" ($translatorrestic.host | required "translator.restic.host not provided!")
        "osAuthUrl" ($.Values.components.translator.osAuthUrl | required "translator.osAuthUrl not provided!")
        "cacheContainer" ($translatorcache.container | required "translator.cache.container not provided!")
        "cachePrefix" ($translatorcache.prefix | required "translator.cache.prefix not provided!")
   | list $
   | include "translation.translatorContainer" | indent 4 }}
  containers:
{{ dict "languageCode" $args.language.code
        "configBranchOverride" ($.Values.components.alternate.configBranchOverride | default nil)
        "matomoUrl" ($.Values.site.matomoUrl | default nil)
        "matomoSiteId" ($args.language.matomoSiteId | default nil)
   | list $
   | include "translation.buildContainer" | indent 4 }}
{{- end -}}
