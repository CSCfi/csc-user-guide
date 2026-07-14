# Roihu dataset projects

A **Roihu dataset project** provides a shared filesystem directory for
datasets that several computational projects need to use on Roihu.
A given dataset project is available directly on Roihu under:

```text
/dataset/<dataset-project-id>
```

A dataset project provides storage and access management, but no computing
resources. It does not include `scratch` or `projappl` directories and cannot
be used to submit jobs.

!!! note "Dataset project access begins in early August 2026"
        Applications for dataset projects are already open in MyCSC. The first
        approved dataset projects will be granted access in early August 2026.

A dataset project is useful when several computational projects need direct
access to the same actively used dataset.

Using a dataset project avoids storing separate copies of the same dataset in
multiple Scratch directories. It also provides a clear owner for maintaining
the dataset and a central place for managing read access across multiple projects on Roihu.

## Access model

Each dataset directory has one designated owning project with write access.
The owning project is responsible for maintaining the dataset and managing
its contents.

Read access can be granted to:

* Individual users
* One or more computational projects
* Users from selected organizations
* All Roihu users

Public dataset projects are readable by all Roihu users.
CSC publishes a list of public datasets.
Restricted dataset projects are readable only by the users, projects or organisations selected in MyCSC.

The dataset project ID used in the filesystem path identifies the dataset
project:

```text
/dataset/project_20XXXXX
```

## Using data from a dataset project

After you have been granted access, you can use the dataset directly from its
directory:

```bash
cd /dataset/<dataset-project-id>
ls
```

Users with read access can read the files but cannot modify them. If you need
to modify data for your own workflow, copy the required files to the Scratch
directory of your computational project:

```bash
cp -a /dataset/<dataset-project-id>/<data> \
    /scratch/<computational-project-id>/
```

Jobs must be submitted using a computational project:

```bash
#SBATCH --account=<computational-project-id>
```

**Do not** use the dataset project ID as the Slurm account. A dataset project does
not provide computing resources.

## Quota and billing

Dataset projects do not receive a default storage quota. The required quota
must be requested separately when applying for the project.

Dataset storage consumes Storage Billing Units. Request only the amount of
storage that the dataset currently requires.

Dataset projects are primarily intended for actively used datasets up to a
few terabytes in size. Contact
[CSC Service Desk](../support/contact.md) if your dataset is substantially
larger or your use case has unusual storage requirements.

Datasets consume the following amount of storage billing units, when compared to
other disk areas:

| Storage area     | Billing                       |
|:-----------------|:-----------------------------:|
| Scratch          | `6 BU * TiB * storage-hours`  |
| Home             | `10 BU * TiB * storage-hours` |
| Projappl         | `10 BU * TiB * storage-hours` |
| Dataset — public | `6 BU * TiB * storage-hours`  |
| Dataset — shared | `10 BU * TiB * storage-hours` |

See more details in the [HPC Billing documentation pages](hpc-billing.md).

## Applying for a dataset project

You can apply for a dataset project in MyCSC.

A dataset project is valid for one year at a time. An extension must be requested if
the dataset is still actively used after that period.

The project application must include an exit strategy explaining what will
happen to the data when the project ends. Depending on the use case, the data
should be:

- transferred to another storage service
- published or preserved in an appropriate repository
- transferred to the dataset owner
- deleted when it is no longer needed

For detailed application instructions, see
[Creating a new project: Dataset project](../accounts/how-to-create-new-project.md#dataset-project).

Dataset projects are not intended for long-term storage and they are not automatically backed up by CSC.
Only use dataset projects for actively used data. Maintain a separate copy of any important
or irreplaceable data.

For data that is not actively used on Roihu, consider
[Allas object storage](../data/Allas/index.md) or another storage service
provided by CSC or your organisation.

## Related documentation

- [Roihu disk areas](roihu-disk.md)
- [Creating a new dataset project](../accounts/how-to-create-new-project.md#dataset-project)
- [Storing data at CSC](../data/datasets/hosting-datasets-at-CSC.md)
- [Allas object storage](../data/Allas/index.md)