---
tags:
  - Academic
catalog:
  name: AMS-GUI
  description: AMS integrated GUI
  description_fi: AMS:n integroitu graafinen käyttöliittymä
  license_type: Academic
  disciplines:
    - Chemistry
  available_on:
    - Puhti
    - Mahti
---

# AMS-GUI { #ams-gui }

[AMS](../apps/ams.md) sisältää integroidun GUI:n (graafisen käyttöliittymän), joka helpottaa mallinnustehtävien määrittelyä, ajoa ja analysointia. Voit kokeilla GUI:ta Puhti-verkkokäyttöliittymän kautta, [www.puhti.csc.fi](../computing/webinterface/index.md), mutta laajempaa käyttöä varten suosittelemme asentamaan GUI:n omalle kannettavallesi tai työasemallesi.

## Lisenssi { #license }

Katso [AMS:n lisenssiosio](ams.md#license).

## Käyttö { #usage }

### Käyttö selaimen kautta { #use-via-your-browser }

Siirry selaimella osoitteeseen [puhti.csc.fi](https://puhti.csc.fi/) ja kirjaudu CSC-käyttäjätunnuksellasi.

1. Sieltä [käynnistä työpöytä](../computing/webinterface/desktop.md#launching). 
2. Avaa `Terminal` ja siirry sopivaan työhakemistoon.
3. Lataa AMS-moduuli `module load ams/2023.104`.
4. Käynnistä syötteen rakennustyökalu `amsinput` ja luo työsi.
5. Tallenna työ (`File-> Save As ...`).

Lyhyet työt voi käynnistää suoraan GUI:sta (`File-> Run`), mutta pidemmät työt pitäisi lähettää eräjonoon. Kaikki tallennetut työt, sekä lasketut että laskemattomat, löytyvät GUI:ssa kohdasta `SCM-> Jobs`. Ennen kuin lähetät työn eräjonoon, määritä mitä resursseja se tarvitsee (aika, muisti, ytimien määrä jne.)

1. Siirry kohtaan `SCM-> Jobs` ja valitse `Queue -> New -> SLURM`
2. `Queue Name: My_testqueue`. Voit tallentaa jonoja eri nimillä vastaamaan erilaisia resurssipyyntöjä  
3. `Remote host:`. Jätä tyhjäksi  
4. `Remote user:`. Jätä tyhjäksi  
5. `Remote job directory:`. Jätä tyhjäksi  
6. `Run command: sbatch --partition=test --nodes=1 --ntasks-per-node=40 --account=<yourproject> --time=00:10:00 "$job" `   
Korvaa `<yourproject>` oikealla projektinimellä. Voit käyttää samoja komentorivivalitsimia kuin tavallisessa eräajon skriptissä.
7. `Use Local Batch: yes`  
8. `Prolog command: source /appl/profile/zz-csc-env.sh; module load ams/2023.104; export SCM_TMPDIR=$PWD; export FORT_TMPDIR=$SCM_TMPDIR`
   Tämä alustaa AMS-ympäristön.

Valitse lähetettävä työ (`SCM-> Jobs`), valitse käytettävä jono (`Queue`) ja lähetä työ `Job-> Run`.  

### Asenna GUI omalle koneellesi { #install-your-own-gui }

CSC:n hankkima AMS-lisenssi sallii CSC:n akateemisten asiakkaiden asentaa AMS-GUI:n paikalliselle tietokoneelle. Näin käyttäjä voi kätevästi rakentaa ja määritellä laskentamallin. Kun malli on valmis, varsinainen laskenta lähetetään CSC:n palvelimille ja suoritetaan siellä. Tulokset voidaan sitten noutaa ja analysoida paikallisella koneella. Huomaa, että paikallisen asennuksen lisenssi kattaa vain AMS-GUI:n, ja se on voimassa vain akateemiseen käyttöön (ei valtion tai kaupalliseen tutkimukseen).

#### 1. Pyydä tunnukset { #1-request-credentials }

Pyydä AMS-GUI:n lataustunnukset [CSC Service Deskiltä](../support/contact.md). Lisää aihe-kenttään tunniste `AMS-GUI`. Huomaa, että lisenssi kattaa vain CSC:llä tehtävän akateemisen käytön (ei valtion tai kaupallista tutkimusta). Tunnukset nollataan 6 kuukauden välein.

#### 2. Lataa { #2-download }

Hae koneellesi sopiva binääri [SCM:n sivustolta](https://www.scm.com/support/downloads/)
käyttäen:

* **SCM User ID:** `<the User ID you got from servicedesk@csc.fi>`
* **Password:** `<the password you got from servicedesk@csc.fi>`   

Safari-selainta Macilla käyttävillä lataus alkaa ilman käyttäjätunnuksen ja salasanan syöttöä. 

#### 3. Asenna { #3-install }

*a. Windows:* aja exe-järjestelmänvalvojan oikeuksin ja hyväksy kaikki oletusasetukset.  
*b. Mac:* avaa dmg ja vedä kohde AMS2023.xxx Applications-hakemistoon.  
*c. Linux:* pura tgz ja suorita `amsbashrc.sh` source-komennolla AMS:n asennushakemistossa.

Yksityiskohtaisemmat ohjeet löytyvät [AMS:n asennusoppaasta](https://www.scm.com/doc/Installation/index.html).

#### 4. Aja { #4-run }

*a. Windows:* kaksoisnapsauta pikakuvaketta **AMSjobs**  
*b. Mac:* käynnistä sovellus **AMS2023.xxx**  
*c. Linux:* ota ympäristö käyttöön ja aja `$AMSBIN/adfjobs`

Kun käynnistät AMS:n ensimmäistä kertaa, sinulta kysytään käyttäjänimeä, salasanaa ja sähköpostiosoitetta. Lisenssi haetaan automaattisesti internetistä.

#### 5. Hallitse erätöitä { #5-control-batch-jobs }

Etätöiden hallintaa varten sinun on luotava SSH-avaimet työasemasi ja Puhtin (Mahti) välille, katso
[SSH-avainten luonti](../computing/connecting/ssh-keys.md).

Kaikki tallennetut työt, sekä lasketut että laskemattomat, löytyvät GUI:ssa kohdasta `SCM-> Jobs`.
Ennen kuin lähetät työn eräjonoon, määritä mitä resursseja se tarvitsee
(aika, muisti, ytimien määrä jne.)

1. Valitse `Queue -> New -> SLURM`
2. `Queue Name: My_testqueue`. Voit tallentaa jonoja eri nimillä vastaamaan erilaisia resurssipyyntöjä
3. `Remote host: puhti.csc.fi`. 
4. `Remote user: <your CSC username> `   
5. `Remote job directory: /scratch/<yourproject>`   
6. `Run command: sbatch --partition=test --nodes=1 --ntasks-per-node=40 --account=<yourproject> --time=00:10:00 "$job" `  
Korvaa `<yourproject>` oikealla projektinimellä. Voit käyttää samoja komentorivivalitsimia kuin tavallisessa eräajon skriptissä.  
7. `Use Local Batch: no`
8. `Prolog command: source /appl/profile/zz-csc-env.sh;source /appl/soft/chem/AMS/ams2022.103/ams_csc.bash;export SCM_TMPDIR=/scratch/<yourproject>; export FORT_TMPDIR=$SCM_TMPDIR`