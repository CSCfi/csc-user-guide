# Maestro

Schrödinger Maestro is a versatile molecular modelling environment. It has modules
for drug design and Materials Science. It can be used to build, edit, run and analyse 
chemical model systems. Maestro is available for consortium members during 
2019. 

[TOC]

## Available

Puhti: 2019.3


## License

The Maestro license consists of floating licenses and tokens.
Different modules 
use a different amount of tokens (0-8). The license 
allows for several simultaneous jobs with each module. 
More information of the Maestro modules can be found at the 
Schrödinger www page: [www.schrodinger.com]

It is possible for one user to take up all licenses for a 
certain module. If  licenses run out, contact Atte via Service Desk.

**Consortium**

Until end of 2019 Maestro usage is limited to the Consortium members. 
The current members 
are the groups of Ari Koskinen (Aalto Univ.), Antti Poso (UEF), 
Mark Johnson (ÅA), Petri Pihko (JYU),  Olli Pentikäinen (JYU), 
Henri Xhaard (UH), Tero Aittokallio (UH/FIMM) and Jari Valkonen (UH). 
The licensing is IP-address or local username based. To install 
Maestro locally, the researchers within the consortium should 
contact servicedesk and send user information (details in the 
installation instructions in Scientist's User Interface, see 
below). The usage is restricted by the 
[EULA](http://www.schrodinger.com/salesagreements/20/7/).

##Usage

It is recommended to download and install Maestro on your 
own computer (Linux, Mac or Windows). You can download it 
from [Scientist's Interface](https://sui.csc.fi) (requires 
a user account at CSC).

**Standalone usage on Puhti**

We recommend you to set up your simulations on your local
computer, generate and save the input files, copy them to Puhti and then 
run them from the command line on Puhti. Note, that Maestro jobs
are not run via batch scripts like most other applications at CSC, but
via Schrödinger binaries and a set of flags and options for them. The
best way is use scripts written by the Maestro GUI as explained above.

To run such a script in Puhti you first need to initialize Maestro with `module load maestro`
and then run the script.


Alternatively, you can watch a video tutorial on how to do it:  

[![Maestro Standalone](http://img.youtube.com/vi/oQDLa6Bh-q4/0.jpg)](http://www.youtube.com/watch?v=oQDLa6Bh-q4 "Maestro Standalone")

!!! note
    We do not recommend running the Maestro GUI remotely on Puhti.
    It _can_ be done via NoMachine, but there are some known glitches
    and the performance is not very good.

Desmond molecular dynamics runs **very well** on GPUs. We recommed watching 
the video above on how to accomplish this easily.

**Local Installation**

Maestro can be installed on a Linux, Mac or Windows computer. 
Download the appropriate files from [www.schrodinger.com] You
don't need a license to download the software, but you'll need
to configure licensing before you can run it.
Contact Atte via servicedesk@csc.fi for details.

## References

Please cite the Maestro modules in all published work as described 
in the Module manuals. Jaguar, for example, should be acknowledged with:

Jaguar, version 7.6, Schrödinger, LLC, New York, NY, 2009.

## More information

* Manual including tutorials come with the Maestro GUI.
* The [Schrödinger website support](http://www.schrodinger.com/support) has an extensive collection of videos, tutorials, online courses, etc.
* Search the [Schrödinger KnowledgeBase](https://www.schrodinger.com/kb) for solutions 
* Issues on how to run Maestro on CSC environment: mailto:servicedesk@csc.fi
* Scientific questions related to Maestro modules: mailto:info@schrodinger.com


![www.schrodinger.com](http://www.schrodinger.com/)
