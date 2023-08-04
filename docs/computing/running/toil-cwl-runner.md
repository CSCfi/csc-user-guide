# Running CWL workflows on Puhti with `toil-cwl-runner`

![CWL Logo](https://raw.githubusercontent.com/common-workflow-language/cwl-website/main/content/assets/img/CWL-Logo-HD-cropped2.png){ width=50% }

The [Common Workflow Language](https://www.commonwl.org/) is a popular set of open standards implemented by several workflow runners and platforms.
The CWL standards are targeted at creating portable workflows made of command line programs. The steps can be written in any compiled or interpreted language.
Sub-workflows, optional steps, scatter-gather, and implicit parallelism are just some of the features.

The [Toil workflow system](https://toil.ucsc-cgl.org/) supports running CWL on a variety of schedulers and systems.

This page describes how run CWL worklflows on Puhti using `toil-cwl-runner`, including the usage of `apptainer` to execute any provided Docker-format containers.

## Strengths of the Common Workflow Language standards

- Open standard (free to read, free to contribute to) governed by a [not-for-profit charity which is legally obligated to work in the public interest](https://sfconservancy.org/news/2018/apr/11/cwl-new-member-project/).
- [Multiple implementations](https://www.commonwl.org/implementations/) of the CWL standards
- Used in many [different fields of research](https://www.commonwl.org/gallery/)
- YAML based syntax with [special support in many IDEs](https://www.commonwl.org/tools/#editors)
- Support, but does not require, software containers. Can also work with conda packages, `module load` environments, and locally available software.
- CWL's model works hard to keep site-specific deatuls out of the workflow definition. Enabling portability between laptops, clusters, and cloud systems.

## Strengths of `toil-cwl-runner`
- Supports sending jobs to Slurm, translating CWL resource requirements to Slurm resources specifications.
- Even when using Slurm, (sub-)tasks do not have to have identical resource requirements.
- Can also run on other batch systems: Grid Engine, Torque, LSF, HTCondor.
- Launches and monitors Slurm jobs for you. Also constructs the `apptainer` commands (or some other software container engine as appropriate: `docker`, `podman`, `singularity`, `udocker`).
- No database needs to be setup.

## Disadvantages for using `toil-cwl-runner`
- Just a workflow runner. Won't manage your data, or keep track of previous workflow runs.

## Installing `toil-cwl-runner` using Tykky

Create a containerized installation of `toil` with `CWL` plugin, along with `nodejs` to provide helpful tools for debugging `toil` internals.

The Conda environment to be containerized is defined in the file `environment.yml`.
```yaml
channels:
  - conda-forge
dependencies:
  - python=3.10
  - pip
  - pip:
    - toil[cwl]
  - nodejs

```

Use the [Tykky](../containers/tykky.md) command `conda-containerize` to create an installation into the [project application directory](../disk.md#projappl-directory).

```bash
module purge
module load tykky

install_dir=/projappl/<project_xxxxxxx>/<install dir name>
mkdir $install_dir

conda-containerize new --prefix $install_dir environment.yml
```

Add the `bin` directory to the PATH to call the executables as with a virtual environment.

```bash
export PATH="$install_dir/bin:$PATH"

toil-cwl-runner --version
```

## Defining CWL workflows

Learning resources

- [Novice CWL tutorial](https://carpentries-incubator.github.io/cwl-novice-tutorial/), includes detailed setup instructions for local editing and running on Microsoft Windows, macOS, and Linux
- <https://www.commonwl.org/user_guide/>

## Running CWL workflows with `toil-cwl-runner`

!!! Note
    Singularity containers can't be run in the **login node** or in an **interactive session** due to network constraints.

When you have defined a workflow with `CWL`, you can send it to the cluster using `sbatch`, and then `toil` will start new jobs for each item in the workflow description.

### Preliminary Steps
Create a working directory for `toil` inside the [scratch directory](../disk.md#scratch-directory).
```bash
mkdir /scratch/<project_xxxxxxx>/<work dir name>
```

### Creating the sbatch file
The `sbatch` file `workflow.sh` will reference the `CWL` file `workflow.cwl` where you have described your workflow steps.

!!! Note
    See [batch documentation](./creating-job-scripts-puhti.md) on how to fill out the `#SBATCH` values.

`workflow.sh`
```bash
#!/bin/sh
#SBATCH --job-name=<job name here>
#SBATCH --account=<project_number here>
#SBATCH --time=01:00:00
#SBATCH --mem-per-cpu=1G
#SBATCH --nodes=1
#SBATCH --cpus-per-task=2
#SBATCH --partition=small

work_dir=/scratch/<project_xxxxxxx>/<work dir name>

export TOIL_SLURM_ARGS="--account=project_nnnnnnn --partition=small"
export CWL_SINGULARITY_CACHE=$work_dir/singularity
unset XDG_RUNTIME_DIR

toil-cwl-runner \
    --jobStore $work_dir/<job store name> \
    --workDir $work_dir \
    --tmpdir-prefix $work_dir/<tmp name> \
    --batchSystem slurm \
    ~/workflow.cwl \
    --message "message for job"
```

Send your workflow to the cluster.
```
sbatch workflow.sh
```

## Monitoring a running workflow

Check the output logs from the main Toil job or
run `toil status /scratch/<project_xxxxxxx>/<work dir name>/<job store name>`.
