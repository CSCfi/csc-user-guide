Maestro
-------

### Description

Maestro is a versatile molecular modelling environment especially for drug design. It can be used to build, edit, run and analyse molecules. Maestro is available for consortium members during 2017-2018. Please check below to see it you are allowed to use Maestro. Another, academic version of Maestro and Desmond with restricted Maestro functionality is available also for non-consortium members: see [Desmond](https://research.csc.fi/-/desmond).

* * *

### Available

##### Version on CSC's Servers

Taito, Taito-Shell, Taito-GPU: 2018.4, also older versions

* * *

##### Versions for Workstations

upto 2018.4

* * *

### Usage

The Maestro license consists of floating license tokens and separate license pools for selected modules. Different modules use a different amount of license tokens (0-8). The license allows for several (tens) of simultaneous jobs with each module. More information of the Maestro modules can be found at the Schrödinger www page: [www.schrodinger.com](http://www.schrodinger.com/)

It is possible for one user to take up all licenses for a certain module. If  licenses run out, contact Atte via Service Desk.

**Consortium**

The usage is limited to the Consortium members. The current members are the groups of Ari Koskinen (Aalto Univ.), Antti Poso (UEF), Mark Johnson (ÅA), Petri Pihko (JYU),  Olli Pentikäinen (JYU), Henri Xhaard (UH), Tero Aittokallio (UH/FIMM) and Jari Valkonen (UH). The licensing is IP-address or local username based. To install Maestro locally, the researchers within the consortium should contact servicedesk and send user information (details in the installation instructions in Scientist's User Interface, see below). The usage is restricted by the [EULA](http://www.schrodinger.com/salesagreements/20/7/).

**Usage**

It is recommended to download and install Maestro on your own computer (Linux, Mac or Windows). You can download it from [Scientist's Interface](https://sui.csc.fi) (requires a user account at CSC).

**Standalone usage on Taito**

You can save the input files needed to run the job from Maestro on your computer, copy them to Taito and then run them from the command line. [Instructions are here.](/-/maestro-standalone-jobs-on-taito "Submitting Maestro jobs from the commandline")

Alternatively, you can watch a video tutorial on how to do it:  

[![Maestro Standalone](http://img.youtube.com/vi/oQDLa6Bh-q4/0.jpg)](http://www.youtube.com/watch?v=oQDLa6Bh-q4 "Maestro Standalone")

**Interactive Remote usage on Taito**

If you want to run the Maestro GUI remotely, you can do it on Taito-shell. The best way to do that is to login to taito-shell via the NoMachine remote desktop. The remote graphics performance may be slow, but sometimes useful. Please don't run Maestro in the login nodes, but start Maestro on taito-shell:

```
module load maestro
maestro -NOSGL
```

Note, that to be able to run graphics remotely from a Windows machine, you need _e.g._ the NoMachine remote desktop. [Look here for installation and configuration.](/csc-guide-connecting-the-servers-of-csc#1.3.3 "Link title") NoMachine will also give better performance when working remotely from Linux/Macs. Yet another way to run the GUI remotely is to use [TurboVNC and the GPGPU nodes in Taito](https://research.csc.fi/taito-gpu-graphics).

**Desmond**

Although Desmond is available also in the suite provided by Schrödinger Inc. it is possible to use the Academic version obtained directly from D.E.Shaw research, which may have some additional features. That version can be used by all academics in Finland for academic research ([please consult the license agreement](http://www.deshawresearch.com/downloads/download_desmond.cgi/Desmond_2_License.txt)). Instructions for using [Desmond in Taito](/software-details?p_p_id=101&p_p_lifecycle=0&p_p_state=maximized&p_p_col_id=column-2&p_p_col_count=1&_101_struts_action=%2Fasset_publisher%2Fview_content&_101_assetEntryId=113505&_101_type=content&_101_urlTitle=running-desmond-jobs-in-taito&redirect=%2F-%2Fmaestro "Running Desmond jobs in Taito").

Desmond molecular dynamics runs **very well** on the **Taito GPUs** (3-4 times faster than a full CPU-only Haswell node, i.e. 24 cores). You can submit jobs to the GPGPUs from the GUI or command line from taito or taito-shell (no need to log in on taito-gpu) just select one of the gpu-named queues for your job. We recommed watching the video above on how to accomplish this easily.

**Installation**

Maestro can be installed on a Linux, Mac or Windows computer. Download the appropriate files from [the  Scientist's User Interface](https://sui.csc.fi) and follow instructions there. You need to have an account at CSC to download the software.

**Terms of Use and Privacy Policy**

It is possible to use the software at your own workstation or resources without a CSC user account. Also in this case, the user accepts the [Terms of use](https://research.csc.fi/general-terms-of-use) and the accompanying [The CSC Customer Register Privacy Policy](https://www.csc.fi/customer-register-privacy-policy).

* * *

### Discipline

Biosciences  
Chemistry  

* * *

### References

Please cite the Maestro modules in all published work as described in the Module manuals. Jaguar, for example, should be acknowledged with:

Jaguar, version 7.6, Schrödinger, LLC, New York, NY, 2009.

* * *

### Support

servicedesk@csc.fi

* * *

### Manual

Manual comes with the Maestro GUI.