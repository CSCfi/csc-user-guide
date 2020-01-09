# Maestro

Schrödinger Maestro is a versatile molecular modelling environment. It has modules
for drug design and Materials Science. It can be used to build, edit, run and analyse 
chemical model systems. Maestro is available for all academic users in 2020.

[TOC]

## Available

Puhti: 2019.3, 2019.4


## License

The Maestro license consists of floating licenses and tokens.
It is possible for one user to take up all licenses for a 
certain module. If licenses run out, contact Atte via Service Desk.
Using Maestro means that you accept the
[EULA](https://www.schrodinger.com/maestro-academic-eula).

## Usage

It is recommended to download and install Maestro on your 
own computer, see below.

**Local Installation**

Maestro can be installed on a Linux, Mac or Windows computer.
Download the appropriate files from [www.schrodinger.com](https://www.schrodinger.com/)
You don't need a license to _download_ the software, although you need to register
to the Schrödinger website, but you'll need
to configure licensing before you can _run_ it.
[These instructions to configure licensing](https://wiki.eduuni.fi/pages/viewpage.action?pageId=130528861)
require Haka authentication.

**Standalone usage on Puhti**

We recommend you to set up your simulations on your local
computer, generate and save the input files, copy them to Puhti and then 
run them from the command line on Puhti. Note, that Maestro jobs
are not run via batch scripts like most other applications at CSC, but
via Schrödinger binaries and a set of flags and options for them.
For example, a Desmond workflow could be run with:

```
"${SCHRODINGER}/utilities/multisim" -JOBNAME 2hhb_test -HOST gputest \
-maxjob 1 -cpu 1 -m 2hhb_test.msj -c 2hhb_test.cfg -description "Molecular Dynamics" \
2hhb_test.cms -mode umbrella -set stage[1].set_family.md.jlaunch_opt=["-gpu"] \
-o 2hhb_test-out.cms -lic "DESMOND_GPGPU:16"

```
This is a bit complicated and it's best to write it out from the Maestro GUI as explained above.

To run such a script in Puhti you first need to initialize Maestro with
 `module load maestro` and then run the script.

The following video tutorial walks you through it (Taito and Puhti work similarly):  

[![Maestro Standalone](http://img.youtube.com/vi/oQDLa6Bh-q4/0.jpg)](http://www.youtube.com/watch?v=oQDLa6Bh-q4 "Maestro Standalone")

!!! note
    We do not recommend running the Maestro GUI remotely on Puhti.
    It _can_ be done via [NoMachine](nomachine.md), but there are some known glitches
    and the performance is not very good. Also, no heavy tasks should be
    done on the login nodes. Please consult the
    [policy on the computing overview.](../computing/overview.md)

Desmond molecular dynamics runs **very well** on GPUs. We recommend watching 
the video above on how to accomplish this easily.

Maestro gives a warning for using a `schrodinger.hosts` file from your home directory. This is
not an issue: that file cannot be made available in the installation directory, so please
ignore that warning, but consider any others you may see.

## References

Please cite the Maestro modules in all published work as described 
in the Module manuals. Jaguar, for example, should be acknowledged with:

Jaguar, version 7.6, Schrödinger, LLC, New York, NY, 2009.

## More information

* Manual including tutorials come with the Maestro GUI.
* The [Schrödinger website](http://www.schrodinger.com/support) has an extensive collection of videos, tutorials, online courses, etc.
   * [A 3 min overview video](https://www.youtube.com/watch?v=NkM8jjHr7f4)
   * [Learn Maestro in 40 minutes](https://www.schrodinger.com/seminars/archives/1338/6th-life-science-bootcamp) Requires registration, which may take a while to complete.
   * [Short videos on 11 features](https://www.schrodinger.com/training/videos/maestro/all)
   * [Downloadable tutorials section](https://www.schrodinger.com/training/tutorials)
* Search the [Schrödinger KnowledgeBase](https://www.schrodinger.com/kb) for solutions 
* Issues on how to run Maestro on CSC environment: [servicedesk@csc.fi](mailto:servicedesk@csc.fi)
* Scientific questions related to Maestro modules: [help@schrodinger.com](mailto:help@schrodinger.com)
