# Getting started

Step-by-step instructions on using the CSC Notebooks environment. 

## How to login to CSC Notebooks?

CSC Notebooks can be accessed by anyone that has _Haka_, _Virtu_ or _CSC_ account.

Check if your institution belongs to _Haka_ or _Virtu_ here :

* [Haka institutions](https://wiki.eduuni.fi/pages/viewpage.action?pageId=27297776){target="_blank"}
* [Virtu institutions](https://wiki.eduuni.fi/display/CSCVIRTU/Organisaatiot){target="_blank"}

## Joining a course

If you are a student in a course that uses the CSC Notebooks environment, you will be provided a _join code_ by the course organizer.
Once you have the code, you can visit [the Notebooks application](https://notebooks-beta.rahtiapp.fi), login with any of the [supported login methods](getting_started.md/#how-to-login-to-csc-notebooks) , then find the `Join workspace` button on the top right corner of the Notebooks home page. Enter the join code in the popup and click the `+` button. If that succeeded, it will guide you to your courses workspace, from where you can find your courses application from the list. If it did not succeed, ṕlease verify that your copied the join code correctly and there are no trailing whiltespaces. 

You can then start the application by using the power control button on the right of the application. A new tab will open with your application.


## Self-learning

1. After logging in, you will be presented with a list of publicly accessible *applications*. The applications that 
   have self-learning material included are marked with `self-learning` label.
2. Start a session of any application by using the power control button on the right. A new tab is opened for
   your session. If your browser blocks this pop-up, you can click on the power control again to enter the session.
3. When you are finished, delete the application session using the power control button.
4. The running application session will be deleted automatically if the session exceeds its lifetime. Lifetime is 
   shown next to the power control button. The remaining time is visible in the power control button itself.

!!!Note

    Public applications do not support saving your session or data. If you want to keep your content, please download it
    locally before your session ends.

## How to host a course

CSC Notebooks is built for hosting online courses. We support currently Jupyter and RStudio based content, with more
options to come in the future. The intended workflow is that you create one workspace per course, and arrange your 
exercises in one or more applications in that workspace.

Here is a step-by-step guide for hosting a course on CSC Notebooks.

### Becoming a workspace owner and creating a workspace

1. Login to CSC Notebooks using your CSC account. Make note of your user account on the bottom of the left navigation
   bar. If you don't have a CSC account yet, 
   [see the instructions on how to create new user account](../../../accounts/how-to-create-new-user-account/).
2. Send email to <notebooks@csc.fi> to request workspace owner rights. Please include your CSC user account in the mail. 
   We will add the capability to create your own workspaces to your account.
3. Once the access is given, a new entry *Manage workspaces* in the left navigation bar will appear. Use *Create
   workspace* button to create a workspace.

### Creating an application in the workspace

Open *Manage workspaces* in the left navigation and select the workspace you want to work on. Create a new application 
through *Application creation wizard* or *Use simple editor* -buttons.

**Application template** Template provides the base features for your application. Most of the templates are based on
container images maintained by Notebooks team. Take a look at the 
[image sources in notebook-images repository.](https://github.com/CSCfi/notebook-images/tree/master/builds){target="_blank"}

**Application name** Give a valid meaningful name.

**Application description** Fill a detailed description to helps users to understand more about the application.

**Container image** For advanced use cases. You can customize the container image the application uses by building 
your own image, uploading it to a public image registry (such as docker-registry in Rahti, DockerHub or Quay.io)
and pointing *Container image* to it. See [instructions for creating custom images](./custom_image.md).

**Labels** Select the default labels or create custom labels. Labels are useful in searching applications. The icon for
the application is also selected based on assigned labels.

**Interface** JupyterLab or old Jupyter notebooks. Applicable only for Jupyter based applications.

**Download Method** The location to download the course contents from. Choose *git clone* if you wish to clone a git
repository. Choose *Download from url* if you have contents hosted in Allas or other HTTP accessible location and 
provide the url.

!!!Note

    The external location should be publicly accessible. For example git repositories should be public.

As an alternative, the course material can be provided through `shared` folder. Workspace owner can prepare the
shared folder in advance. The folder is visible but read-only for normal workspace members.
[See data persistence document for more information](data_persistence.md).

**Work folder per user** Whether `my-work` folder is available for users in this application. 
This is enabled by default.

### Invite users

Once the content is ready, you can invite users by sharing a workspace specific join code. The code can be found in
*Manage workspaces* view, in workspace list or on the Info tab of each workspace.
The users can enter the code by clicking *Join workspace* button located in the top bar. They can then see all published 
applications on top of the application list on the *Applications* page, and under *My workspaces* page as well.

### Promote users

As workspace owner or co-owner, you can promote members of the workspace to be co-owners or demote co-owners to members.
Co-owners can do everything the owner can, except demoting the owner or deleting the workspace. 

## Using CSC Notebooks for collaboration

A simple setup for collaboration can be achieved by following the 'How to host a course' instructions above and 
promoting the collaborators as co-owners. The process is:

1. Obtain workspace owner rights.
2. Create a workspace.
3. Invite the collaborators using the join code.
4. Make collaborators co-owners, so they can also write to the shared folder in the workspace.

## Security guidelines for Workspace owners

- CSC Notebooks is not intended for sensitive data. Do not store sensitive data or data sets.
- Share join code only with users you wish to join your workspace.
- If you are creating custom images for your course, do not store any keys or sensitive data in the image.
- Delete the workspace as soon as the course is over.
