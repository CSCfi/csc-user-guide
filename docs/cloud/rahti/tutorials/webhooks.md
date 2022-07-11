<style>
.admonition-title { background-color: rgba(255, 145, 0, 0.1) !important; }
.admonition { background-color: white !important; }
</style>
!!! Attention "⚠️ Rahti 3 is deprecated"

    This page is about a deprecated version of Rahti, please consult the [updated documentation article](../../../rahti4/tutorials/webhooks/)

# Webhooks

Webhooks are URLs that allow triggering actions in a system. Rahti supports webhooks to trigger rebuilds. This means that each BuildConfig is listening to a particular URL that includes a secret (more about that later), and that when this URL is called, a build will be triggered. There few types of formats supported: Generic, GitHub, GitLab and Bitbucket. This means that if the source code of the application is in Gitlab, the Gitlab URL type is the one that should be filled in in Gitlab's side.

![Triggers](/cloud/rahti4/img/trigger.drawio.svg)

First, it is necessary to find the secret, in the BuildConfig (in this case called `serveimg-generate`) look for the name of the secret reference:

```bash
oc get bc/serveimg-generate -o yaml
```


```yaml
spec:
  triggers:
  - type: GitHub
    github:
      SecretReference:
        name: webhooksecret
```

Now the secret `webhooksecret` should have the `WebHookSecretKey` field:

```bash
oc get Secret webhooksecret -o yaml
```

which output something like:

```yaml
apiVersion: v1
kind: Secret
data:
  WebHookSecretKey: dGhpc19pc19hX2JhZF90b2tlbgo=
metadata:
  name: webhooksecret
  namespace: mynamespace     # set this to your project namespace
```

The `WebHookSecretKey` is encoded in base64, to decode it:

```bash
echo 'dGhpc19pc19hX2JhZF90b2tlbgo=' | base64 -d
```

When the BuildConfig is configured to be triggered by the webhook, and the
corresponding secret exists, the webhook URL can be found by using the command `oc describe`:

```bash
$ oc describe bc/serveimg-generate
Name:                serveimg-generate
.
.
.
Webhook GitHub:
        URL:        https://rahti.csc.fi:8443/apis/build.openshift.io/v1/.../<secret>/github
.
.
.
```

Finally, go to <GitHub.com>, go to the repository where the code is, and in Settings > Webhooks, click in "Add webhook".

![GitHub Webhooks](/cloud/rahti/tutorials/img/GitHubWebhook.png) 

The GitHub WebHook payload URL is the URL above with `<secret>` replaced with the base64 decoded string of the value of `data.WebHookSecretKey` above, and the content type is `application/json`. Leave the filed `Secret` empty.

![Add webhook](/cloud/rahti/tutorials/img/Addwebhook.png)
