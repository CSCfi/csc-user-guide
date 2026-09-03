---
tags:
  - Academic
catalog:
  name: Maestro
  description: Versatile drug discovery and materials modeling suite
  license_type: Academic
  disciplines:
    - Chemistry
    - Biosciences
  available_on:
    - Roihu
    - LUMI
---

# Maestro

!!! info "Online Schrödinger certification courses offered by CSC"
    Users in scope of [CSC's Schrödinger license](#license) are eligible to
    apply for free-of-charge access to participate in online certification
    courses organized by Schrödinger. The offered _introductory_ and
    _intermediate_ online courses focus on a range of topics related to drug
    discovery and materials science.

    [Read more and apply here :material-open-in-new:](https://csc.fi/en/training-calendar/online-schrodinger-certification-courses-offered-by-csc-3/)

Schrödinger Maestro is a versatile molecular modeling environment. It has
modules for _drug design_ and _materials science_. It can be used to build,
edit, run and analyze chemical model systems.

Schrödinger Maestro provides access to the, which runs **very well** on GPUs.

See also the [bottom of this page](#more-information) for links to further
self-learning materials.

[TOC]

## Available

* Roihu-CPU: 2025.1, 2025.2, 2025.3, 2025.4, 2026.1, 2026.2, 2026.3
* LUMI: 2026.1, 2026.2, 2026.3

A two-year cleaning cycle is applied on the Maestro modules on CSC
supercomputers. Specifically, this means that module versions older than two
years will be removed. This policy is enforced to free up disk space and
encourage use of the latest versions which tend to be more performant and have
less bugs.

!!! warning "Desmond MD simulations cannot be run on Roihu!"
    Schrödinger currently only ships x86 builds of their software suite. This
    means that **any Schrödinger modules that require GPUs, most notably
    Desmond, cannot be run on Roihu**.

    CSC provides Maestro modules only on Roihu-CPU for purely CPU-based
    workloads such as virtual screening (Glide).

## License

Maestro is available for all academic users in Finland: staff and students, for
academic purposes. Please consult the [EULA](https://www.schrodinger.com/eula)
for the exact definition. Using Maestro means that you accept the EULA linked
to above. The Maestro license consists of floating licenses and tokens. If
licenses run out, contact us via [ServiceDesk](../support/contact.md).

## Usage

It is recommended to download and install Maestro on your own computer, see
[below](#local-installation).

### Local installation

Maestro can be installed on a Linux, Mac or Windows computer. Download the
appropriate files from [the Schrödinger website](https://www.schrodinger.com/).
You don't need a license to _download_ the software, although you do need to
register at the Schrödinger website first. Note that getting access may take up
to 24 hours, so please be patient.

After you've downloaded and installed Maestro, you'll need to configure
licensing to be able to _run_ the software.
[See these instructions on how to configure licensing](https://wiki.eduuni.fi/pages/viewpage.action?pageId=130528861)
(logging in to Eduuni requires Haka authentication). Accessing the license
requires that your computer is in the FUNET network, i.e. you're at the
university or connected to it via VPN from home.

### Standalone usage on Roihu and LUMI

!!! warning "Roihu vs. LUMI"
    Note that Roihu is not suitable for running Desmond MD simulations on GPUs.
    Please use LUMI-D if you need to run Desmond simulations. If you need
    support, [contact us](../support/contact.md).

It is possible to run heavier computations on Roihu and LUMI. Here, a brief
overview is given. Additional details and some diagnostics tips are explained
in our [Maestro power usage tutorial](../support/tutorials/power-maestro.md).

First, you need to
[get a CSC account](../accounts/how-to-create-new-user-account.md) and
[create](../accounts/how-to-create-new-project.md) or be
[added](../accounts/how-to-add-members-to-project.md) to a project that has
[access](../accounts/how-to-add-service-access-for-project.md) to Roihu or
LUMI.

For actual simulations we recommend using Roihu-CPU or LUMI as follows:

1. Set up your simulations on your local computer.
2. Write the GUI-generated input files to disk:

    1. Instead of selecting _Run_, open the nearby drop-down menu marked with a
       cogwheel.
    2. Select _Write_ to write the input files to disk.

3. Copy the input files to the supercomputer with e.g.
   [`scp`](../data/moving/scp.md) or using the
   [web interfaces](../computing/webinterface/index.md).
4. **Important!** The `<job-name>.sh` file contains the command to launch your
   simulation. To make it work on CSC supercomputers, ensure that:

    1. `-HOST localhost` is set.
    2. `-WAIT` is appended at the end of the command.
    3. **Windows users** should replace the forward-slashes `\` with
       back-slashes `/` in the path to the Schrödinger binary (right after
       `${SCHRODINGER}` in the command).

    Additionally, the `<job-name>.sh` file should be edited into a proper
    Slurm batch script. Examples for different platforms:

    === "Roihu-CPU"
        ```bash
        #!/bin/bash
        #SBATCH --account=project_2001234
        #SBATCH --partition=small
        #SBATCH --time=00:30:00
        #SBATCH --nodes=1
        #SBATCH --ntasks=1
        #SBATCH --cpus-per-task=16
        #SBATCH --mem-per-cpu=2000M

        module load maestro/2026.2

        # Start a local job server
        ${SCHRODINGER}/jsc local-server-start

        # Run a Glide job distributed over 16 cores (16 subjobs running concurrently)
        "${SCHRODINGER}/glide" cdk2_dock.in -OVERWRITE -NJOBS ${SLURM_CPUS_PER_TASK} -new -JOBNAME cdk2_dock -HOST localhost:${SLURM_CPUS_PER_TASK} -WAIT
        
        # Stop the local job server
        ${SCHRODINGER}/jsc local-server-stop
        ```
    === "LUMI-C"
        ```bash
        #!/bin/bash
        #SBATCH --account=project_462000123
        #SBATCH --partition=small
        #SBATCH --time=00:30:00
        #SBATCH --nodes=1
        #SBATCH --ntasks=1
        #SBATCH --cpus-per-task=16
        #SBATCH --mem-per-cpu=2000M

        module use /appl/local/csc/modulefiles
        module load maestro/2026.2

        # Start a local job server
        ${SCHRODINGER}/jsc local-server-start

        # Run a Glide job distributed over 16 cores (16 subjobs running concurrently)
        "${SCHRODINGER}/glide" cdk2_dock.in -OVERWRITE -NJOBS ${SLURM_CPUS_PER_TASK} -new -JOBNAME cdk2_dock -HOST localhost:${SLURM_CPUS_PER_TASK} -WAIT
        
        # Stop the local job server
        ${SCHRODINGER}/jsc local-server-stop
        ```
    === "LUMI-D"
        ```bash
        #!/bin/bash
        #SBATCH --account=project_462000123
        #SBATCH --partition=lumid
        #SBATCH --time=00:30:00
        #SBATCH --nodes=1
        #SBATCH --ntasks=1
        #SBATCH --gpus=1
        #SBATCH --mem-per-cpu=2000M

        module use /appl/local/csc/modulefiles
        module load maestro/2026.2

        # Start a local job server
        ${SCHRODINGER}/jsc local-server-start

        # Run a Desmond MD simulation using a single GPU
        "${SCHRODINGER}/utilities/multisim" -JOBNAME desmond_job -HOST localhost -maxjob 1 -cpu 1 -m desmond_job.msj -c desmond_job.cfg -description 'Molecular Dynamics' desmond_job.cms -mode umbrella -o desmond_job-out.cms -lic DESMOND_GPGPU:16 -WAIT
        
        # Stop the local job server
        ${SCHRODINGER}/jsc local-server-stop
        ```

5. Submit the job to the queue with `sbatch <job-name>.sh`.
6. Copy the results back to your local workstation for analysis.

!!! info "Important notes"
    * Please observe that the `${SCHRODINGER}/jsc local-server-start` and
      `${SCHRODINGER}/jsc local-server-stop` commands are mandatory.
      Schrödinger has deprecated the old Job Control system and
      `schrodinger.hosts` files that were used on Puhti and Mahti. The new
      _Job Server_ system must be used on Roihu and LUMI.
    * No long/heavy tasks should be done on the login nodes! Please consult
      the [Usage policy](../computing/usage-policy.md) page for more details.

### Monitoring running jobs

Running Slurm jobs can be monitored as usual using the `squeue` command.
Additionally, running Schrödinger jobs and the log files they produce can be
monitored using tools provided by the Job Server command-line utility `jsc`:

=== "Roihu"
    ```bash
    # Replace <node> with the id of the node your job is running on, e.g. rc4136.
    # Note that the Schrödinger job id is different from the Slurm job id.

    ssh <node> "${SCHRODINGER}/jsc list" # List jobs and their status
    ssh <node> "${SCHRODINGER}/jsc tail-file <schrodinger-jobid>" # Tail log file for a running job
    ```

=== "LUMI"
    ```bash
    # Note that the Schrödinger job id is different from the Slurm job id.

    srun -n 1 --overlap --pty --jobid=<slurm-jobid> ${SCHRODINGER}/jsc list
    srun -n 1 --overlap --pty --jobid=<slurm-jobid> ${SCHRODINGER}/jsc tail-file <schrodinger-jobid>
    ```

## References

Please cite the Maestro modules in all published work as described
in the Module manuals.

## More information

* [Tutorial and tips for power usage](../support/tutorials/power-maestro.md)
* Schrödinger training materials overview
   * [Life science](https://www.schrodinger.com/life-science/learn/education/)
    * [Materials science](https://www.schrodinger.com/materials-science/learn/education/)
    * [Apply for free-of-charge online course seats](https://csc.fi/en/training-calendar/online-schrodinger-certification-courses-offered-by-csc-3/)
* Free learning resources at Schrödinger
    * [Life science](https://www.schrodinger.com/life-science/learn/education/free-learning-resources/)
    * [Materials science](https://www.schrodinger.com/materials-science/learn/education/free-learning-resources/)
* The [Schrödinger knowledge base](https://support.schrodinger.com/s/) has an
  extensive collection of articles, for example:
    * [How to restart a single Desmond simulation](https://www.schrodinger.com/kb/1883)
    * [How to restart a Desmond multisim workflow](https://www.schrodinger.com/kb/1896)
    * [Structure file formats compatible with Maestro](https://www.schrodinger.com/kb/1278)
* Video materials:
    * [Getting Going with Maestro](https://learn.schrodinger.com/private/edu/release/current/Getting-Going-With-Video-Series/Maestro/Get-Going-Maestro-VS/Content/maestro/Page-Topics-m/01-Course-Intro-Get-Going.htm)
    * [Getting Going with Materials Science Maestro](https://learn.schrodinger.com/private/edu/release/current/Getting-Going-With-Video-Series/MS_Maestro/Get-Going-MS-VS/Content/maestro-ms/Page-Topics-ms/01-Course-Intro-Get-Going-ms.htm)
    * [Schrödinger YouTube channel](https://www.youtube.com/@SchrodingerTV)
* Issues on how to run Maestro in CSC environment: [contact CSC Service Desk](../support/contact.md)
* Scientific questions related to Maestro modules: [contact Schrödinger Support](https://support.schrodinger.com/s/contactsupport)
