---
hide:
  - toc
---

# Sensitive Data (SD) -palveluiden käyttöopas – Sisällysluettelo { #sensitive-data-sd-services-user-guide-table-of-contents }

!!! Note
    Valitse oikea käyttöopas aloittamalla sen tunnistamisesta, minkä tyyppistä dataa käsittelet:
    
    1. Tutkimusdata (esim. tutkimustarkoituksiin kerätty, suostumuksella hankittu data): noudata ohjeita tutkimusdatan tallentamiseen ja analysointiin tai julkaisemiseen ja uudelleenkäyttöön.
    
    2. Sosiaali- ja terveysdatan toissijainen käyttö, rekisteridata, jonka toimittaa Findata tai jokin julkinen rekisterinpitäjä: noudata rekisteridatan analysointiin tarkoitettua ohjetta ja Suomen lainsäädännön vaatimuksia. 
    
    Etkö ole varma, mikä opas sopii tilanteeseesi? Lähetä meille sähköpostia osoitteeseen servicedesk@csc.fi aiherivillä "SD Services"

## 1. Tutkimusdata { #1-research-data }

### 1.1 Tallenna ja analysoi tutkimusdataa { #1-1-store-and-analyse-research-data }

* [Aloita tästä: CSC-projektin luominen (akateeminen tyyppi)](sd-access.md)
    * [Käyttö projektipäällikkönä](sd-use-case-new-user-project-manager.md)
    * [Käyttö projektin jäsenenä](sd-use-case-new-user-project-member.md)

#### 1.1.1 Tallenna ja jaa SD Connectilla { #1-1-1-store-and-share-with-sd-connect }

* [Tallenna ja jaa SD Connectilla](sd_connect.md)
    * [Kirjaudu SD Connectiin](sd-connect-login.md)
    * [Lähetä](sd-connect-upload.md)
    * [Jaa](sd-connect-share.md)
        * [Siirrä dataa toiseen projektiin](sd-connect-share-tranfer-data.md)
        * [Käytä kansiota jaettuna työtilana](sd-connect-share-workspace.md)
        * [Anna pääsy kansion sisältöön vain SD Desktopissa](sd-connect-share-read-to-sd-desktop.md)
    * [Lataa](sd-connect-download.md)
    * [Poista](sd-connect-delete.md)
    * [Komentorivikäyttöliittymä](sd-connect-command-line-interface.md)
    * [Vianmääritys](sd-connect-troubleshooting.md)

#### 1.1.2 Analysoi ja suorita laskentaa SD Desktopissa { #1-1-2-analyze-and-compute-with-sd-desktop }

* [Analysoi ja suorita laskentaa Sensitive Data Desktopissa](sd_desktop.md)
    * [Kirjaudu SD Desktopiin](sd-desktop-login.md)
    * [Luo virtuaalityöpöytä](sd-desktop-create.md)
    * [Hallitse virtuaalityöpöytää](sd-desktop-manage.md)
    * [Käytä virtuaalityöpöytää](sd-desktop-access-vm.md)
    * [Työskentely virtuaalityöpöydälläsi](sd-desktop-working.md)
    * [Mukauttaminen – ohjelmistot ja työkalut](sd-desktop-software.md)
    * [Tuo dataa](sd-desktop-access.md)  
    * [Vie dataa käyttöliittymän kautta](sd-desktop-export.md)  
    * [Vie dataa ohjelmallisesti](sd-desktop-export-commandline.md)
    * [Vianmääritys](sd-desktop-troubleshooting.md)

### 1.2 Julkaise ja uudelleenkäytä tutkimusdataa { #1-2-publish-and-reuse-research-data }

#### 1.2.1 Julkaise Fedarated EGA:ssa { #1-2-1-publish-with-fedarated-ega }

* [Julkaise Fedarated EGA:ssa](federatedega.md)
    * [Julkaise dataa](fega-submission.md)

#### 1.2.2 Uudelleenkäytä SD Applyn avulla { #1-2-2-reuse-with-sd-apply }

* [Uudelleenkäytä SD Applyn avulla](sd-apply.md)
    * [Hae pääsyä FEGA-dataan](sd-apply-access.md)
    * [Hyväksy pääsy FEGA-dataan](sd-apply-approval.md)
    * [Mahdollista FEGA-datan uudelleenkäyttö](sd-apply-dac.md)

## 2 Sosiaali- ja terveysdatan toissijainen käyttö (rekisteridata) { #2-secondary-use-of-health-and-social-data-register-data }

### 2.1 Aloita tästä: Pääsy sosiaali- tai terveysdatan toissijaisen käytön aineistoihin Sensitive Data -palveluiden ja CSC-projektin Findata-tyypin kautta { #2-1-start-here-accessing-secondary-use-health-or-social-data-via-sensitive-data-services-and-a-csc-project-findata-type }

* [Aloita tästä: Pääsy sosiaali- tai terveysdatan toissijaisen käytön aineistoihin Sensitive Data -palveluiden kautta](secondarydata-access.md)
    * [Pääsy Findatan luvalla](findata-permit.md)
    * [Pääsy rekisteriluvalla](single-register-permit.md)

### 2.2 Analysoi SD Desktopilla toissijaista käyttöä varten { #2-2-analyze-with-sd-desktop-for-secondary-use }

* [Analysoi SD Desktopilla toissijaista käyttöä varten ](sd-desktop-audited.md)
    * [Kirjaudu SD Desktopiin](sd-desktop-secondary-login.md)
    * [Luo virtuaalityöpöytä](sd-desktop-secondary-create.md)
    * [Hallitse virtuaalityöpöytää](sd-desktop-secondary-manage.md)
    * [Käytä virtuaalityöpöytää](sd-desktop-secondary-access-vm.md)
    * [Työskentele työpöydälläsi ja ohjelmistojen kanssa](sd-desktop-secondary-working.md)
    * [Tuo dataa](sd-desktop-secondary-access.md)  
    * [Vie dataa](sd-desktop-secondary-export.md)  
    * [Vianmääritys](sd-desktop-secondary-troubleshooting.md)

## 3. Ohjeet { #3-tutorials }

Huomaa: osa näistä ohjeista vaatii ennakkotuntemusta SD-palveluista tai edistyneitä koodaustaitoja.

* [Puuttuvien Python-kirjastojen lisääminen Pythioniin SD Desktopissa](./tutorials/sd-pythonlibs.md)
* [RStudion ja R-kirjastojen lisääminen SD Desktopiin](./tutorials/rstudio.md)
* [Auto-apptainer](./tutorials/auto-apptainer.md)
* [Varmuuskopiointi SD Desktopille](./tutorials/backup_sd_desktop.md)
* [Kaikkien tiedostojen salauksen purkaminen hakemistossa](./tutorials/decrypt-directory.md)
* [SD Desktopin ohjelmistoympäristön laajentaminen omilla Apptainer-kontteillasi](./creating_containers.md)
* [Asenna VS Code SD Desktopiin](./tutorials/vscode.md)
* [Asenna Whisper SD Desktopiin](./tutorials/whisper.md)
* [Podman SD Desktopissa](./tutorials/podman-in-sd-desktop.md)
* [Väliaikaisen PostgreSQL-tietokannan ajaminen SD Desktopissa](./tutorials/postgresql.md)
* [Allas-tallennuspalvelun käyttäminen arkaluonteisen tutkimusdatan vastaanottamiseen](./sequencing_center_tutorial.md)

## 4. Sekalaista { #4-misc }
* [Hyödyllistä terminologiaa: palvelut ja tekniset näkökohdat](sd-terminology.md)