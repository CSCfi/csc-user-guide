
Rahti supports Generic, GitHub, GitLab and Bitbucket webhooks. They are
particularly useful in triggering builds. The BuildConfig syntax:

```yaml
spec:
  triggers:
  - type: GitHub
    github:
      SecretReference:
        name: webhooksecret
```

Now the secret `webhooksecret` should have:

```yaml
apiVersion: v1
kind: Secret
data:
  WebHookSecretKey: dGhpc19pc19hX2JhZF90b2tlbgo=    # "this_is_a_bad_token" in
metadata:                                           #  base64 encoding
  name: webhooksecret
  namespace: mynamespace     # set this to your project namespace
```

When the BuildConfig is configured to trigger by the webhook and the
corresponding secret exists, the webhook URL can be found by using the command `oc describe` (assuming we
included the webhook in `serveimg-generate`):

```
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

Finally, the GitHub WebHook payload URL is the URL above with `<secret>`
replaced with the base64 decoded string of the value of `data.WebHookSecretKey`
above, and the content type is `application/json`.

