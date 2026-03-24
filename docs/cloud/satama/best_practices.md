# Best Practices

Following these best practices will help you manage container images in Satama efficiently and securely.

### Organize Repositories Clearly

If you are a project admin, create repositories in a way that makes sense to your team For example, repositories can be grouped by:

* application
* microservice
* environment (development, staging, production)

A clear structure helps others quickly locate and reuse images.

### Assign Appropriate User Permissions

Project administrators should assign permissions carefully.

Only users who need to push images should receive **Developer** access. Users who only need to pull images should remain **Guests**. Limiting push permissions helps prevent accidental overwrites or unauthorized image modifications.

### Use Robot Accounts for Automation

Try to use project-scoped robot accounts rather than using personal login. 
Robot accounts provide several advantages:

* Controlled access permissions
* Easier credential rotation
* Reduced risk of exposing personal accounts

This approach improves security and simplifies automation workflows.

### Use CLI Secrets for Authentication

If you authenticate using a myCSC account, always use the CLI secret instead of the Web UI password when logging in through Docker or other command-line tools.

Using CLI secrets ensures secure authentication and prevents issues caused by expired UI sessions.

### Avoid Using the latest Tag

Avoid relying on the latest tag for production images. The latest tag can be overwritten and may not always refer to the expected version of an image.

Instead, use meaningful and consistent tags such as:

* version numbers (v1.2.0)
* release identifiers (release-2024-01)
* commit hashes (git-sha)

Using explicit version tags improves traceability and ensures reproducible deployments.

### Regularly Review Vulnerability Reports

Periodically review vulnerability scan reports for images stored in Satama.

If vulnerabilities are detected:

* update the base image
* update affected packages
* rebuild the container image

High-severity vulnerabilities should be addressed before deploying images to production environments.

### Remove Unused Images

Over time, repositories may accumulate outdated images and unused tags. Removing these unused artifacts helps keep the registry organized.

Cleaning up old images provides several benefits:

* reduces storage usage
* prevents confusion between image versions
* improves overall repository management

Administrators can also configure tag retention policies to automatically remove outdated tags while preserving the most recent or important versions.