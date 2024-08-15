# Data persistence

There are three types of storage in Noppe.

* **Workspace shared folder**: persisted for workspace lifetime
* **My-work folder**: persisted for workspace lifetime per user
* **Home directory**: persisted only for session lifetime, survives application restarts in error situations

!!!Note

    `home` or `$HOME` folder refers to `home/jovyan` for Jupyter based applications and `/home/rstudio` for RStudio based 
    applications.

!!!Note

    None of the persistent storage options are backed up. Always make sure you (and your users) make a copy outside 
    Noppe of any data you cannot afford to lose. 

## Workspace shared folder 

* A shared volume is created per workspace. This volume is mounted in `$HOME/shared` for each session.
* The default size of the volume is 20 GB.
* Workspace owner and managers/co-owners will have full access to this folder. Every other user in the workspace will
  have read-only access to this folder.
* Shared folder is directly linked to the lifetime of workspace. When the workspace is deleted, shared folder will be
  automatically deleted.
* The backing volume for shared folder lives on NFS, thus the storage is not as fast as home directory.

### Intended use

Workspace owner and co-owners can create, modify and save course contents in the shared folder and workspace members 
can directly read from them.

## My-work folder

* My-work folder is a workspace specific folder for each user, mounted to `$HOME/my-work`.
* Workspace owner can enable or disable `my-work` folder per application.
* If enabled, a volume will be automatically created for the user during the launch of the first session.
  Other users or workspace owners in the workspace will not have any access to the individual users volume.
* The default volume size is 1 GB.
* My-work folder is persisted until the workspace expires.
* The backing volume for my-work folder lives on NFS, thus the storage is not as fast as home directory.

### Intended use

Individual users can store and save their course data in this volume until the end of the workspace lifetime. Unlike
session volume, this is not deleted when the session expires. The contents from the previous session are available when
starting a new session. If the workspace has multiple applications, this folder will be mounted simultaneously to
parallel sessions and thus can be also used for data transfer between for example Jupyter and RStudio.

## Home directory

* Data is preserved over session container restarts, for example in out-of-memory situations. In practice, a volume is
  created and mounted on `$HOME` when the session is launched.
* Data is hosted on a local, fast disk. The disk does not have any redundancy for hardware failures.
* Data is deleted when the session is deleted by user or when the lifetime of session ends.
