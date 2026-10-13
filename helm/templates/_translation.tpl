{{- define "translation.translatorName" -}}
{{- printf "%s-translator" (include "docs-csc.name" .) | trunc 63 | trimSuffix "-" }}
{{- end -}}

{{- define "translation.translatorSecretName" -}}
{{- printf "%s-secret" (include "translation.translatorName" .) | trunc 63 | trimSuffix "-" }}
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

{{- define "translation.translatorContainer" -}}
{{- $ := index . 0 -}}
{{- $args := index . 1 -}}
{{- $translatorsecretname := include "translation.translatorSecretName" $ -}}
{{- $ossecretname := include "docs-csc.osAppCredSecretName" $ -}}
- name: {{ $args.languageCode | printf "%s-%s" (include "translation.translatorName" $) }}
  image: {{ include "translation.translatorName" $ | list $ | include "docs-csc.fullImageName" | squote }}
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
          name: {{ $translatorsecretname }}
          key: translator.restic.password
    - name: OS_AUTH_URL
      value: {{ $args.osAuthUrl | squote }}
    - name: OS_APPLICATION_CREDENTIAL_ID
      valueFrom:
        secretKeyRef:
          name: {{ $ossecretname }}
          key: os.applicationCredential.id
    - name: OS_APPLICATION_CREDENTIAL_SECRET
      valueFrom:
        secretKeyRef:
          name: {{ $ossecretname }}
          key: os.applicationCredential.secret
{{- if $.Values.components.translator.restoreOnly | default false | not }}
    - name: OPENAI_API_KEY
      valueFrom:
        secretKeyRef:
          name: {{ $translatorsecretname }}
          key: translator.openAi.apiKey
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
  image: {{ include "docs-csc.altBuilderName" $ | list $ | include "docs-csc.fullImageName" | squote }}
  imagePullPolicy: Always
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
      value: {{ list $ $args.languageCode | include "networking.sitePath" }}
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
        "osAuthUrl" ($.Values.os.authUrl | required "os.authUrl not provided!")
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
  affinity:
    podAffinity:
      requiredDuringSchedulingIgnoredDuringExecution:
        - topologyKey: kubernetes.io/hostname
          labelSelector:
            matchLabels:
{{ include "docs-csc.selectorLabels" $ | indent 14 }}
{{ include "docs-csc.altName" $ | list $ | include "docs-csc.componentLabels" | indent 14 }}
{{- end -}}
