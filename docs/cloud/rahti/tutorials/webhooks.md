!!! success "Basic level"
    You need to familiarize yourself with the Rahti [web interface](../usage/getting_started.md)

    You need knowledge of Git and GitHub. Also, a GitHub account is required

# Webhooks

Webhooks are URLs that allow triggering actions in a system. Rahti supports webhooks to trigger rebuilds. This means that each BuildConfig is listening to a particular URL that includes a secret (more about that later), and that when this URL is called, a build will be triggered for a default branch.

There are few types of formats supported: Generic, GitHub, GitLab and Bitbucket. This means that if the source code of the application is in Gitlab, the Gitlab URL type must be selected.

![Triggers](../../img/trigger.drawio.svg)

In this example we will use the GitHub type.

## Creating a secret

After loggin in at Rahti, in the left hand side menu, click on `Workloads` dropdown list, go to the **Secrets** page. Make sure that you are in the right project and then click in **Create -> Webhook secret**. Write any sensible name. And click on **Generate**. Write down the generated secret. And **Save**.

![CreateWebhookSecret](../../img/CreateWebhookSecret.png)

## Getting the URL

You need an already created `BuildConfig` object, or create a new one. In order to create a new BuildConfig, check out the [Creating an image](../images/creating.md) article.

Now you need to edit the build config (**Actions -> Edit BuildConfig**), and add a trigger. To do this, click on "Trigger", in the bottom of the edit page, in the "Advanced options" section. Then, click in "Add trigger". The new trigger must have a type, in our case it will be "GitHub". It also needs a secret, select the secret you created in the previous step.

![Edit BuildConfig](../../img/editBuildConfig.png)

When the `BuildConfig` is configured, you can get the URL via the webinterface. Using the left menu, go to the **Builds** dropdown list, and select the `BuildConfigs`. In the `Webhooks` section, you will see "Copy URL with Secret". Click on it, and the URL will be in your clipboard.

![Copy URL with Secret](../../img/webhooks.png)

!!! Warning "Default branch names do not match"

    You need to make sure that the branch names match between Rahti and GitHub. In Rahti, the default branch name is `master`, but in GitHub, the default branch name is `main`. This means that&mdash;by default&mdash;any change in a GitHub branch named `main` will be ignored by Rahti.

    If you want changes in `main` to be picked up by Rahti, you need to:

    1. Edit the **BuildConfigs**
    2. Expand **Show advanced Git options** under **Source**
    3. Add the correct branch name (in this case `master`) under **Git reference**.

## GitHub

Once you got the URL and the secret, go to <https://github.com>. There you should go to the repository where the code is, and in **Settings -> Webhooks**, click in "Add webhook".

![GitHub Webhooks](../../img/GitHubWebhook.png)

You just need to fill up the "Payload URL" and the "Secret", and change the content type to `Application/json`.

![Add webhook](../../img/Addwebhook.png)
