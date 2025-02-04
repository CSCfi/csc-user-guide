---
tags:
  - Other
system:
  - www-puhti
  - www-mahti
---

# CryoSPARC

CryoSPARC(Cryo-EM Single Particle Ab-Initio Reconstruction and Classification) is a state of the art scientific software platform for processing cryo-electron microscopy (cryo-EM) used in research and drug discovery activities by solving structures of membrane proteins, viruses, complexes, flexible molecules, small particles, phase plate data and negative stain data.


## Available

 The software can be installed on Puhti and Mahti. CSC recommends using Mahti for CryoSPARC usage due to limited availale scratch are on Puhti  Follow installation instructions for Master at [CryoSPARC](https://cryosparc.com/docs/reference/install/). Users can reques port ranges from CSC by sending email to servicedesk@csc.fi.


## License

CryoSPARC has non-profit and commercial licensing options. The software is free of charge for non-profit academic use but the user has to request [a licence key](https://cryosparc.com/download/) from Structura from their website. Please consult structure Bio (e-mail:sales@structura.bio) for commercial usage


## Usage

Note that every user needs to install their own instance of cryoSPARC, shared installations are not recommended. Request a port for you to use for your cryoSPARC installation by sending an email to servicedesk@csc.fi. The port number and login node you receive will be reserved to you on both Puhti and Mahti. The cryosparc_master.tar.gz file required in the installation contains over 160 000 files, while the default limit in projappl is 100 000. You will therefore need to apply for an extension to the default quota when installing cryoSPARC.  CSC maintains a centralised installation of cryoSPARC worker. If you follow these instructions and use the correct lane templates, you do not need to install worker at all. It is helpful to setup passwordless login for cryoSPARC use. Check the documentation on CSC webpages on how to do this: https://docs.csc.fi/computing/connecting/ (Setting up SSH keys)


!!! Web interfaces may not be used for using CryoSPARC as login nodes are randomly assigned. Please note that each user is assigned on a specific login node with specific port range. 


## References

Please consult all publications including the one mentioned below:

> cryoSPARC: algorithms for rapid unsupervised cryo-EM structure determination
Punjani, Ali ; Rubinstein, John L ; Fleet, David J ; Brubaker, Marcus A
Nature Methods, 2017-03, Vol.14 (3), p.290-296, Article 290


## More information

- [CryoSPARC home page](https://cryosparc.com/)
- [CryoSPARC official installation instructions](https://guide.cryosparc.com/setup-configuration-and-management/how-to-download-install-and-configure)
- [CryoSPARC documentation](https://guide.cryosparc.com/)  
