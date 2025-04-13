# Gabeditin käyttäminen Gaussian-tehtäville Puhtilla {#using-gabedit-as-gui-for-gaussian-jobs-on-puhti}

[Gabedit](http://gabedit.sourceforge.net/) on ilmainen graafinen käyttöliittymä (GUI) moniin laskennallisiin kemian ohjelmistopaketteihin. Tässä esitellään, kuinka sitä voidaan käyttää valmistellessa ja analysoidessa [Gaussian](../../apps/gaussian.md) -tehtäviä Puhtilla. Esivaatimuksina on, että sinulla on voimassa oleva CSC-tili, joka kuuluu Gaussian-ryhmään, ja että olet jäsenenä CSC-projektissa, jolla on pääsy Puhtiin. Tätä opasta oletetaan, että sinulla on Gabedit asennettuna paikalliselle tietokoneellesi.

## Työnkulku {#the-workflow}

Lyhyesti, tärkeimmät vaiheet Gaussian-tehtävän rakentamisessa, suorittamisessa ja analysoimisessa Puhtilla Gabeditin avulla ovat:

1. Luo Gaussian-tulo tiedosto käyttämällä Gabeditia omalla tietokoneellasi.
2. Kopioi tulotiedostot paikalliselta tietokoneeltasi sopivaan työhakemistoon Puhtilla.
3. Käynnistä laskenta Puhtilla.
4. Kopioi tulokset Puhdilta omalle tietokoneellesi.
5. Käytä Gabeditia analysoidaksesi tulokset.

### 1. Luo Gaussian-tulo {#create-the-gaussian-input}

1. Rakenna tai lataa molekyylirakenteesi Gabeditissa.
2. Määritä menetelmä ja muut haluamasi yksityiskohdat.
   ![Gabedit input](../../img/gabedit_1.png)
3. Tallenna se Gaussian-tulo tiedostona erilliseen hakemistoon (tässä nimeltään `benzene`).
   ![Gabedit save](../../img/gabedit_2.png)

### 2. Kopioi tulotiedostot Puhtiin {#copy-the-input-files-to-puhti}

1. Kopioi koko tulo hakemisto (tässä nimeltään `benzene`) sopivaan väliaikaishakemistoon Puhtilla. Tässä käytetään `rsync`. Muiden menetelmien osalta katso [Tietojen siirtäminen CSC:n ja paikallisen työaseman välillä](../../data/moving/index.md).

      ```bash
      rsync -rP benzene username@puhti.csc.fi:/scratch/project_2001234/gabedit
      ```

### 3. Käynnistä laskenta Puhtilla {#start-the-calculation-on-puhti}

1. Kirjaudu Puhtiin ja siirry siihen hakemistoon:

      ```bash
      cd /scratch/project_2001234/gabedit/benzene
      ```

2. Lataa gaussian-moduuli komennolla `module load gaussian`.
3. Lähetä laskenta:

      ```bash
      subg16 00:10:00 benzene_opt_freq project_2001234
      ```

### 4. Kopioi tulokset takaisin tietokoneellesi {#copy-the-results-back-to-your-own-computer}

1. Kun gaussian-tehtävä on valmis, kopioi koko hakemisto Puhtilta takaisin omalle tietokoneellesi. Anna tämä komento omalla tietokoneellasi:

      ```bash
      rsync -rP username@puhti.csc.fi:/scratch/project_2001234/gabedit/benzene/ .
      ```

### 5. Käytä Gabeditia analysoidaksesi tulokset {#use-gabedit-to-analyze-the-results}

1. Gabeditissa käytä `File -> Open` navigoidaksesi siihen hakemistoon, jossa tulokset ovat.
2. Vaihda `Open file` ikkunan oikeassa alakulmassa `*.inp` muotoon `*.com`.
3. Valitse com-tiedosto, joka vastaa Gaussian-tehtävääsi ja avaa se. Tämä avaa Gabeditin pääikkunan.
4. Valitse välilehti, joka näyttää lokitiedoston.
   ![Gabedit analyze](../../img/gabedit_3.png)
5. Oikealla paneelilla näkyy erilaisia analysoitavia vaihtoehtoja.
6. Yllä olevassa esimerkissä laskettiin värähtelytaajuudet. Nämä tulokset voidaan tutkia valitsemalla `Dens. Orb`, joka avaa `Gabedit: Orbitals/Density/Vibration` ikkunan.
   1. Tee hiiren oikealla painikkeella klikkaus kankaalla.
   2. Valitse `Animation -> Vibration`.
   3. Valitsemalla tietyn tilan taulukosta, se voidaan animoida painamalla `Play`.
   4. Laskettu spektri näytetään valitsemalla `Vibration` -ikkunasta `Tools -> Draw IR spectrum`.