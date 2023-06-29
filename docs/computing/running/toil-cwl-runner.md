# Running CWL workflows on Puhti with `toil-cwl-runner`

<img src="https://github.com/common-workflow-language/cwl-website/blob/main/content/assets/img/CWL-Logo-HD-cropped2.png" width="50%" title="CWL Logo"/>

The [Common Workflow Language](https://www.commonwl.org/) is a popular set of open standards implemented by several workflow runners and platforms.
The CWL standards are targeted at creating portable workflows made of command line programs. The steps can be written in any compiled or interpreted language.
Sub-workflows, optional steps, scatter-gather, and implicit parallelism are just some of the features.

The [Toil workflow system](https://toil.ucsc-cgl.org/) supports running CWL on a variety of schedulers and systems.

This page describes how run CWL worklflows on Puhti using `toil-cwl-runner`, including the usage of `apptainer` to execute any provided Docker-format containers.

## Strengths of the Common Workflow Language standards

- Open standard (free to read, free to contribute to) governed by a [not-for-profit charity which is legally obligated to work in the public interest]([https://sfconservancy.org/](https://sfconservancy.org/news/2018/apr/11/cwl-new-member-project/)).
- [Multiple implementations](https://www.commonwl.org/implementations/) of the CWL standards
- Used in many [different fields of research](https://www.commonwl.org/gallery/)
- YAML based syntax with [special support in many IDEs](https://www.commonwl.org/tools/#editors)
- Support, but does not require, software containers. Can also work with conda packages, `module load` environments, and locally available software.
- CWL's model works hard to keep site-specific deatuls out of the workflow definition. Enabling portability between laptops, clusters, and cloud systems.

## Strengths of `toil-cwl-runner`
- Supports sending jobs to Slurm, translating CWL resource requirements to Slurm resources specifications.
- Can also run on other batch systems: Grid Engine, Torque, LSF, HTCondor.
- Launches and monitors Slurm jobs for you. Also constructs the apptainer commands.

## Disadvantages for using CWL

## Disadvantages for using `toil-cwl-runner`
- Just a workflow runner. Won't manage your data, or keep track of previous workflow runs.

## Installing `toil-cwl-runner`

Install `toil` with `CWL` plugin.
```
cd /projappl/<project_nnnnnnn>
python -m venv venv
source venv/bin/activate

pip install -U setuptools wheel
pip install toil[cwl]

toil-cwl-runner --version
```

Install `nodejs` which provides helpful tools for debugging `toil` internals.
```
cd /projappl/project_nnnnnnn
wget https://nodejs.org/dist/v18.16.1/node-v18.16.1-linux-x64.tar.xz
tar -xf node-v18.16.1-linux-x64.tar.xz
export PATH=$PATH:/projappl/project_nnnnnnn/node-v18.16.1-linux-x64/bin
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
Create working directories for `toil`.
```
mkdir /projappl/project_nnnnnnn/<job store name>
mkdir /projappl/project_nnnnnnn/<work dir name>
mkdir /projappl/project_nnnnnnn/<tmp name>
```

### Creating the sbatch file
The `sbatch` file `workflow.sh` will reference the `CWL` file `workflow.cwl` where you have described your workflow steps.

`workflow.sh`
```bash
#!/bin/sh
#SBATCH --job-name=<job name here>
#SBATCH --account=<project_number here>
#SBATCH --time=01:00:00
#SBATCH --mem-per-cpu=1G
#SBATCH --nodes=1
#SBATCH --cpus-per-task=2
#SBATCH --partition=<partition name>

source /projappl/<project_nnnnnnn>/venv/bin/activate

WORKDIR=/projappl/project_nnnnnnn
SCRATCH=/scratch/project_nnnnnnn
export TMPDIR=$WORKDIR/tmp
export TOIL_SLURM_ARGS="--account=project_nnnnnnn --partition=small"
export CWL_SINGULARITY_CACHE=$WORKDIR/singularity
unset XDG_RUNTIME_DIR

TOIL_SLURM_ARGS="--account=<project_nnnnnnn> --partition=<partition name>" toil-cwl-runner \
    --jobStore $WORKDIR/<job store name> \
    --workDir $SCRATCH/<work dir name> \
    --tmpdir-prefix $TMPDIR/<tmp name> \
    --batchSystem slurm \
    $WORKDIR/workflow.cwl \
    --message "message for job"
```

Send your workflow to the cluster.
```
sbatch workflow.sh
```

## Monitoring a running workflow
