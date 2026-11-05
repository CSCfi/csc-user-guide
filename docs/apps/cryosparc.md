---
tags:
  - Other
catalog:
  name: CryoSPARC
  description: Tool to analyse Cryo-EM data on Roihu
  license_type: Other
  disciplines:
    - Biosciences
  unchecked: true
---

# CryoSPARC

CryoSPARC (Cryo-EM Single Particle Ab-Initio Reconstruction and Classification)
is a state-of-the-art scientific software platform for processing cryo-electron
microscopy (cryo-EM) single particle analysis data used in research and drug
discovery activities by solving 3D structures of biological specimens, such as
soluble and membrane proteins and their complexes, viruses, nucleic acids, and
more. It can also process negative stain electron microscopy data.

## Available

The software can be installed on Roihu now. Please note that only the latest version, CryoSPARC v5.1.0, is compatible with the Roihu GPU environment due to its support for the ARM architecture. 

## License

CryoSPARC has non-profit and commercial licensing options. The software is
free-of-charge for non-profit academic use, but users must request
[a licence key](https://cryosparc.com/download/) from the CryoSPARC home page.
Please consult Structura Biotechnology Inc. (<mailto:sales@structura.bio>) for
commercial usage.

## Installation

Note that every user needs to install their own master instance of cryoSPARC. Shared installations are not recommended. Request port numbers for your CryoSPARC usage by sending an e-mail to [CSC Service Desk](../support/contact.md). The port number and login node will be reserved to you on Roihu.

The CryoSPARC installation tar file contains over 160k files, which exceeds the default file quota (150k) for `/projappl` disk space. Thus, users need to apply for an extension to the default quota when installing CryoSPARC.

CSC maintains a centralised installation of cryoSPARC worker. If you follow CSC
internal instructions and use the correct lane templates, you do not need to
install worker at all. The internal installation instructions on Roihu
are available at path:

```bash
/appl/soft/manual/bio/aarch64/cryosparc/lane_config/cryoSPARC_on_Roihu_runbook.pdf
```

Before you can log in to Roihu using SSH, you need to configure your SSH keys, register your public key in MyCSC, and create a short-lived SSH certificate.


Please consult our documentation on:

- [How to connect to CSC supercomputers](../computing/connecting/index.md)
- [How to set up SSH keys](../computing/connecting/ssh-keys.md)

!!! note "CryoSPARC cannot be used from HPC web interfaces"
    CryoSPARC users may not use web interfaces for logging in to Roihu as
    login nodes are randomly assigned. Please note that each user is assigned
    to a specific login node with a specific port range for CryoSPARC usage.

## References

Please consult all publications including the one mentioned below:

> Punjani, A., Rubinstein, J.L., Fleet, D.J. & Brubaker, M.A. cryoSPARC:
algorithms for rapid unsupervised cryo-EM structure determination. Nature
Methods 14, 290-296 (2017).

## More information

- [CryoSPARC home page](https://cryosparc.com/)
- [CryoSPARC official installation instructions](https://guide.cryosparc.com/setup-configuration-and-management/how-to-download-install-and-configure)
- [CryoSPARC documentation](https://guide.cryosparc.com/)  
