# Webhooks

Webhooks are URLs that allow triggering actions in a system. Rahti supports webhooks to trigger rebuilds. This means that each BuildConfig is listening to a particular URL that includes a secret (more about that later), and that when this URL is called, a build will be triggered. There few types of formats supported: Generic, GitHub, GitLab and Bitbucket. This means that if the source code of the application is in Gitlab, the Gitlab URL type is the one that should be filled in in Gitlab's side.

![Triggers](/cloud/rahti4/img/trigger.drawio.svg)

In this example we will use GitHub.

## Getting the URL

First you need a `BuildConfig` object. In order to create a BuildConfig, check out the [Creating an image](../../images/creating/) article. When the BuildConfig is configured, you can get the URL via the webinterface.

Using the `Developer` menu, go to the **Builds** page, and select the BuildConfig you want to trigger. In the `Webhooks` section, you will see "
copy URL with Secret". Click on it, and the URL will be in your clipboard.



You can also obtain the URL via the command line by first describing the Build config object:

```bash
$ oc describe bc/serveimg-generate | grep URL
  URL:  https://api.rahti4-qa.csc.fi:6443/apis/build.openshift.io/v1/namespaces/agonzale-test/buildconfigs/serveimg-generate/webhooks/<secret>/github 
```

Then you can get the secret by:

```bash
$ oc get bc/serveimg-generate -o yaml | yq .spec.triggers -y
- type: ConfigChange
- github:
    secret: secret101
  type: GitHub
```

**NOTE:** `yq` is a command line tool for the manipulation of YAML documents. The same information can be obtained without `yq` by running `oc get bc/serveimg-generate -o yaml`

In this example, you must use `secre101` as `<secret>`.

**NOTE2:** You can change the secret by editting the build config.

## GitHub

Once you got the URL, go to <https://github.com>. There you should go to the repository where the code is, and in **Settings -> Webhooks**, click in "Add webhook".

  ![GitHub Webhooks](../../tutorials/img/GitHubWebhook.png)

The GitHub WebHook payload URL is the URL above with `<secret>` replaced with the base64 decoded string of the value of `data.WebHookSecretKey` above, and the content type is `application/json`. Leave the filed `Secret` empty.

![Add webhook](../../tutorials/img/Addwebhook.png)
