# Running CWL workflows on Puhti with `toil-cwl-runner`

[Common Workflow Language](https://www.commonwl.org/) is a popular set of open standards implemented by several workflow runners and platforms.
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

(and nodejs)

## Defining CWL workflows

Learning resources
- [Novice CWL tutorial](https://carpentries-incubator.github.io/cwl-novice-tutorial/), includes detailed setup instructions for local editing and running on Microsoft Windows, macOS, and Linux
- <https://www.commonwl.org/user_guide/>

## Running CWL workflows with `toil-cwl-runner`

(use sbatch to submit toil-cwl-runner job to submit further jobs)

## Monitoring a running workflow
