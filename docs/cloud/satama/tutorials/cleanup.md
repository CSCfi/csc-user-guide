# Clean Up Old Image Tags

Over time, repositories may accumulate many image tags created during development, testing, or automated builds. Keeping unnecessary tags can make repositories harder to navigate and may increase storage usage. Cleaning up old tags helps keep projects organized and ensures that only relevant image versions remain available.

This tutorial explains how to remove old image tags using the Satama Web UI.

## Step 1: Open the Project

* Log in to the Satama Web UI.
* Navigate to Projects.
* Select the project that contains the repository you want to clean up.

Inside the project page, you will see a list of all repositories belonging to that project.

## Step 2: Open the Repository

* Click on the repository where the old image tags are stored.
* The repository page displays all artifacts and tags associated with that image.

Each tag represents a different version of the container image.

## Step 3: Identify Unused or Old Tags

Review the available tags and identify versions that are no longer needed. These might include:

* old development builds
* outdated release versions
* temporary testing images

You can use the following information to decide which tags to remove:

* tag name
* push time
* vulnerability scan results

## Step 4: Delete the Tag

To remove an image tag:

* Locate and check the box in front of the tag you want to remove.
* Click on **Remove Tag** button
* A pop-up window will appear. Click on **Delete**.

Once deleted, the tag will no longer appear in the repository.

Note that deleting a tag removes the reference to the image. The underlying data may be removed later during storage cleanup processes.

## Step 5: Verify the Repository

After deleting old tags:

* Refresh the repository page.
* Verify that only the required image versions remain.
* Ensure that active deployments are not using the deleted tags.

This helps prevent accidental removal of images that are still in use.

## Optional: Use Tag Retention Policies

Instead of manually deleting tags, projects can use [Tag Retention](../tag_retention.md) policies to automatically remove outdated tags.