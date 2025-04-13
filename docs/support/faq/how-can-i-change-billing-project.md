
# Kuinka voin muuttaa, mikä projekti laskutetaan käytöstäni? {#how-can-i-change-which-project-is-billed-for-my-usage}

Tämä riippuu siitä, mitä CSC-palvelua käytät. Kussakin palvelussa aloitat valitsemalla projektin ensin.

* Supertietokoneen eräajossa määrittelet laskutusprojektin eräajon skriptissä. On erillinen dokumentaatio sekä [**Puhti**](../../computing/running/creating-job-scripts-puhti.md) että [**Mahti**](../../computing/running/creating-job-scripts-mahti.md) varten.
* **Allas**-palvelussa käytettävä projekti määritetään käyttämällä [`allas-conf`-komentoa](../../data/Allas/accessing_allas.md).
* **cPouta** tai **ePouta** -palveluissa [valitset projektin OpenStack Horizon -käyttöliittymän valikosta](../../cloud/pouta/launch-vm-from-web-gui.md#preparatory-steps).
* **Rahti**-palvelussa [OpenShift-projektit yhdistetään CSC-projekteihin *Description*-kentän](../../cloud/rahti/usage/projects_and_quota.md) avulla OpenShift-projektissa.

