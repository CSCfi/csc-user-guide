# Running CWL workflows on Puhti with `toil-cwl-runner`

[Common Workflow Language](https://www.commonwl.org/) is a popular set of open standards implemented by several workflow runners and platforms.
The CWL standards are targeted at creating portable workflows made of command line programs. The steps can be written in any compiled or interpreted language.
Sub-workflows, optional steps, scatter-gather, and implicit parallelism are just some of the features.

The [Toil workflow system](https://toil.ucsc-cgl.org/) supports running CWL on a variety of schedulers and systems.

This page describes how run CWL worklflows on Puhti using `toil-cwl-runner`, including the usage of `apptainer` to execute any provided Docker-format containers.

## Strengths of the Common Workflow Language standards

## Strengths of `toil-cwl-runner`

## Disadvantages for using CWL

## Disadvantages for using `toil-cwl-runner`

## Installing `toil-cwl-runner`

(and nodejs)

## Defining CWL workflows

(link to existing docs)

## Running CWL workflows with `toil-cwl-runner`

(use sbatch to submit toil-cwl-runner job to submit further jobs)

## Monitoring a running workflow
