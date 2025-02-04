---
tags:
  - Other
system:
  - www-puhti
  - www-mahti
---

# CryoSPARC

CryoSPARC (Cryo-EM Single Particle Ab-Initio Reconstruction and Classification) is a state-of-the-art scientific software platform for processing cryo-electron microscopy (cryo-EM) used in research and drug discovery activities by solving structures of membrane proteins, viruses, complexes, flexible molecules, small particles, phase plate data and negative stain data.


## Available

 The software can be installed on Puhti and Mahti. CSC recommends using Mahti for CryoSPARC usage due to its large requirement for scratch disk area. For master node installation, follow the installation instructions at [CryoSPARC](https://cryosparc.com/docs/reference/install/). Users can request port ranges from CSC by sending an e-mail to <servicedesk@csc.fi>.


## License

CryoSPARC has non-profit and commercial licensing options. The software is free-of-charge for non-profit academic use but user must request [a licence key](https://cryosparc.com/download/) from the CryoSPARC home page. Please consult Structura Biotechnology Inc.(<sales@structura.bio>) for commercial usage.


## Usage

Note that every user needs to install his or her instance of cryoSPARC and shared installations are not recommended. Request port numebrs for your CryoSPARC usage by sending an email to <servicedesk@csc.fi>. The port number and login node will be reserved to you on Puhti and/or Mahti. The CryoSPARC installation tar file contains over 160k files which exceeds the default file quota for /projappl disk space (100k). Users thus need to apply for an extension to the default quota when installing CryoSPARC. CSC maintains a centralised installation of cryoSPARC worker. If you follow CSC internal instructions and use the correct lane templates, you do not need to install worker at all. It is helpful to setup a passwordless login for CryoSPARC use. Consult  [CSC documentation](../computing/connecting.md)on setting up SSH keys.


!!! Web interfaces may not be recommended logging into Puhti/Mahti 
    for using CryoSPARC as login nodes are randomly assigned. Please note that each user is assigned to a specific login node with a specific port range. 


## References

Please consult all publications including the one mentioned below:

> cryoSPARC: algorithms for rapid unsupervised cryo-EM structure determination
Punjani, Ali ; Rubinstein, John L ; Fleet, David J ; Brubaker, Marcus A
Nature Methods, 2017-03, Vol.14 (3), p.290-296, Article 290


## More information

- [CryoSPARC home page](https://cryosparc.com/)
- [CryoSPARC official installation instructions](https://guide.cryosparc.com/setup-configuration-and-management/how-to-download-install-and-configure)
- [CryoSPARC documentation](https://guide.cryosparc.com/)  
