---
tags:
  - Academic
description: Schrodinger Maestro usage instructions on CSC supercomputer Puhti
---
# Maestro

Schrödinger Maestro is a versatile molecular modelling environment. It has modules
for *drug design* and *materials science*. It can be used to build, edit, run and analyze chemical
model systems.

[TOC]

## Available

* Puhti: 2020.4, 2021.3, 2021.4, 2022.1, 2022.2, 2022.3, 2022.4
* Mahti: 2021.4, 2022.1, 2022.2

!!! info "Incompatibility issue with latest versions on Mahti"

    Versions 2022.3 and later are incompatible with Mahti. If you intend to run
    jobs on Mahti, don't upgrade your local installation beyond 2022.2! We're
    looking for a workaround.
    
    Note that Mahti is mostly suitable for running Desmond MD simulations on GPUs.
    Most other jobs do not scale to full nodes, so please use Puhti instead for these.

## License

Maestro is available for all academic users in Finland: staff and students,
for academic purposes. Please consult the [EULA](https://www.schrodinger.com/maestro-academic-eula)
for the exact definition.
Using Maestro means that you accept the EULA linked to above.
The Maestro license consists of floating licenses and tokens.
If licenses run out, contact us via [ServiceDesk](/support/contact/)

## Usage

!!! info "Please update your `schrodinger.hosts` file"

    The login nodes of Puhti were renamed following the RHEL8 upgrade in October 2022.
    Consequently, old `schrodinger.hosts` files referencing `puhti-login1` will not work
    anymore! Please update your hosts file either manually by replacing all occurrences of
    `login1` with `login11`, or by deleting your old `schrodinger.hosts` file and setting a
    new one by running the `/appl/soft/chem/schrodinger/set-hosts-file.bash` script.

It is recommended to download and install Maestro on your
own computer, see below.

### Local Installation

Maestro can be installed on a Linux, Mac or Windows computer. Download the appropriate files
from [the Schrödinger website](https://www.schrodinger.com/). You don't need a license to
*download* the software, although you need to register to the Schrödinger website, but you'll
need to configure licensing before you can *run* it. [See these instructions on how to configure
licensing](https://wiki.eduuni.fi/pages/viewpage.action?pageId=130528861) (requires Haka
authentication). Access to the license requires that your computer is in FUNET network, e.g.
you're on the university or connected to it via VPN from home.

### Standalone usage on Puhti

!!! Note
     We mainly recommend using Puhti to run your Maestro jobs. If running on
     Mahti, you must ensure that your jobs are able to utilize full nodes
     (128 CPU cores). Preferably, run only Desmond MD simulations on GPUs
     because most other jobs do not scale. If in doubt, [contact us](/support/contact/).

It is possible to run the heavy computations on Puhti. To do that you need to
[get a CSC account](../accounts/how-to-create-new-user-account.md) and
apply for [access to Puhti](../accounts/how-to-add-service-access-for-project.md). Before you
start the actual workflow below, you need to set up your Maestro environment on Puhti.

These first four steps you only need to do once

1. ssh to Puhti
     * `ssh <your username>@puhti.csc.fi`
2. `module load maestro`
     * Make sure you use the same version as on your local computer
3. An error may appear on your screen. If it asks you to run a script to generate the hosts file,
   run it (copy paste it to the command line)
     * Now you have your own `schrodinger.hosts` file in your `$HOME` directory
4. Copy the HOST descriptions from the `schrodinger.hosts` file on Puhti to your local hosts
   file on your computer
     * Copy everything starting from `name: test` and paste it at the end of your local
       `schrodinger.hosts` file
     * This step may need administrator privileges

For actual simulations we recommend using Puhti as follows:

1. Set up your simulations on your local computer
2. Write the GUI generated input files on disk
3. Copy them to Puhti
4. Edit the script (`your-jobname.sh`) if needed
5. Run the script on the Puhti command line to submit the jobs to the queuing system
6. Copy the results back for analysis

The overall process is shown in the video below, and additional details and some diagnostics tips
are explained in our [Maestro power usage tutorial](../support/tutorials/power-maestro.md)

!!! note
    Maestro jobs are not run via batch scripts like most other applications at CSC, but
    via Schrödinger binaries using options.

For example, a Desmond workflow could be run with:

```bash
"${SCHRODINGER}/utilities/multisim" -JOBNAME 2hhb_test -HOST gputest  \
-maxjob 1 -cpu 1 -m 2hhb_test.msj -c 2hhb_test.cfg -description "Molecular Dynamics" \
2hhb_test.cms -mode umbrella -set stage[1].set_family.md.jlaunch_opt=["-gpu"] \
-o 2hhb_test-out.cms -lic "DESMOND_GPGPU:16 -set "stage[1].set_family.md.jlaunch_opt=["\-LOCAL\"]" \
-LOCAL"
```

This is a bit complicated and it's best to write it out from the Maestro GUI as
explained above. Please also have a look at the [additional flags we recommend
to use](../support/tutorials/power-maestro.md).

To run such a script in Puhti you first need to initialize Maestro (possibly edit
it a bit) and run the script:

```bash
module load maestro
bash your_script_name.sh
```

The following video tutorial walks you through it:  

[![Maestro Standalone](http://img.youtube.com/vi/Aj205UDcWFE/0.jpg)](http://www.youtube.com/watch?v=Aj205UDcWFE "Maestro Standalone")

!!! note
    We do *not* recommend running the Maestro GUI remotely on Puhti. It *can* be done via
    [the Puhti web interface remote desktop](../computing/webinterface/desktop.md), but
    the performance may be somewhat slow due to lack of accelerated graphics, and submitted
    jobs may end up fizzled. Also,
    **no long/heavy tasks** should be done on the login nodes. Please consult the
    [Usage policy](../../computing/usage-policy) page under Computing.

!!! note
    **Windows** users, may need to edit the script created by GUI a little.
    Replace the backslashes "\" with "/" in the path to the Maestro binary
    (right after `$SCHRODINGER` in the script).

Desmond molecular dynamics runs **very well** on GPUs. We recommend watching
the video above on how to accomplish this easily.

Maestro gives a warning for using a `schrodinger.hosts` file from your home directory. This is
**not an issue**: that file cannot be made available in the installation directory, so please
ignore that warning, but consider any others you may see.

## References

Please cite the Maestro modules in all published work as described
in the Module manuals. Jaguar, for example, should be acknowledged with:

Jaguar, version 7.6, Schrödinger, LLC, New York, NY, 2009.

## More information

* [Tutorial and tips for power usage on Puhti](../support/tutorials/power-maestro.md)
* Manual including tutorials come with the Maestro GUI.
* The [Schrödinger website](http://www.schrodinger.com/support) has an extensive collection of
  videos, tutorials, online courses, etc.
   * [A 3 min overview video](https://www.youtube.com/watch?v=NkM8jjHr7f4)
   * [Learn Maestro in 40 minutes](https://www.schrodinger.com/seminars/archives/1338/6th-life-science-bootcamp)
     Requires registration, which may take a while to complete.
   * [Short videos on 11 features](https://www.schrodinger.com/training/videos/maestro/all)
   * [Downloadable tutorials section](https://www.schrodinger.com/training/tutorials)
* Search the [Schrödinger KnowledgeBase](https://www.schrodinger.com/kb) for solutions 
* Issues on how to run Maestro on CSC environment: [contact ServiceDesk](/support/contact/)
* Scientific questions related to Maestro modules: [help@schrodinger.com](mailto:help@schrodinger.com)
