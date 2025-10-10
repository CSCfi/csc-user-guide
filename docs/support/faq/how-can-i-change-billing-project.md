# Miten voin vaihtaa, mille projektille käyttöni laskutetaan? { #how-can-i-change-which-project-is-billed-for-my-usage }

Tämä riippuu siitä, mitä CSC:n palvelua käytät. Jokaisessa palvelussa aloitat valitsemalla ensin projektin.

* Supertietokoneiden eräajoissa laskutusprojekti määritetään eräajon skriptissä. Puhtille ja Mahtille on erillinen dokumentaatio:
  [**Puhti**](../../computing/running/creating-job-scripts-puhti.md) ja
  [**Mahti**](../../computing/running/creating-job-scripts-mahti.md).
* **Allas**-palvelussa käytettävä projekti määritetään
  [`allas-conf`-komennolla](../../data/Allas/accessing_allas.md).
* **cPoutassa** tai **ePoutassa** projekti
  [valitaan OpenStack Horizon -käyttöliittymän pudotusvalikosta](../../cloud/pouta/launch-vm-from-web-gui.md#prerequisites).
* **Rahtissa**
  [OpenShift-projektit yhdistetään CSC:n projekteihin *Description*-kentän avulla](../../cloud/rahti/usage/projects_and_quota.md)
  OpenShift-projektissa.