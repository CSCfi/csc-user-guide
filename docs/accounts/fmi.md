
# Täsmälliset ohjeet Puhti FMI -osioon {#specific-instructions-for-the-puhti-fmi-partition}

Puhti FMI -osio on saatavilla vain sellaisille FMI-käyttäjille, jotka kuuluvat projekteihin, joille on annettu pääsy. FMI-käyttäjät voivat myös käyttää yleistä Puhti-järjestelmää ja CSC:n muita palveluita tavallisten CSC-projektien kautta.

## Projektit: Puhti FMI vs. Puhti ja CSC:n muut palvelut {#projects-puhti-fmi-vs-puhti-and-cscs-other-services}

Projekti voi käyttää joko FMI-osioita tai yleistä osioita ja CSC:n muita palveluita, mutta ei molempia. Eli projekti voi sisältää **joko**

* Puhti FMI (ja mahdollisesti Allas)

**tai** (tämä on eksklusiivinen tai)

* esim. Puhtia ja cPoutaa (tai mitä tahansa muuta palvelua, joka on saatavilla kaikille tutkimuslaitosprojekteille) ja **ei** Puhti FMI:tä

osana käytettävissä olevia palveluita. Näin ollen, jos FMI-projektin johtaja haluaa käyttää sekä yleistä osiota/CSC:n muita palveluita että FMI-osiota, heidän on luotava erilliset projektit.

Kuitenkin kaikki data on saatavilla projektien välillä.

Yleisen osion ja CSC:n muiden palveluiden projektit luodaan [Creating new project](how-to-create-new-project.md) -sivun ohjeiden mukaisesti. Projektityypiksi valitaan _Academic_ ja lisätään Puhti sekä muut tarvittavat palvelut, kuten on kuvattu [Adding service access for project](how-to-add-service-access-for-project.md) -sivulla.

Puhti FMI -osion projektit luodaan samoin valitsemalla projektityypiksi _FMI_. FMI-projekteille ovat saatavilla palveluina vain Puhti FMI ja Allas.

## Puhti FMI -osio {#puhti-fmi-partition}

Puhti FMI -osio sisältää ylimääräiset 240 solmua, joissa on 192 GB muistia. Nämä ovat lisänä niihin, jotka on listattu [järjestelmän kuvauksessa](../computing/systems-puhti.md). Solmuilla on samat tekniset tiedot kuin Puhtin tavallisilla solmuilla. FMI-osiolla on kaksi jonoa: `fmi` ja `fmitest`. Jonon `fmi` maksimityön koko on 100 solmua ja maksimiajoaika on kuusi päivää. Jonon `fmitest` maksimityön koko on kaksi solmua ja maksimiajoaika on 30 minuuttia.

## Tallennusalueet {#storage-areas}

FMI-osion projektit voivat käyttää `/fmi/` -kansiota Puhtissa. Tällä kansiolla on 750 TiB:n globaalinen kiintiö. FMI-projektien projektikansiot sijaitsevat poluissa `/fmi/projappl/<projektinimi>` ja `/fmi/scratch/<projektinimi>`. Komento `csc-workspaces` listaa projektikansiot. Globaali kiintiö on jaettu __projappl__ ja __scratch__ välillä:
```text
/fmi/projappl   150 TiB
/fmi/scratch    600 TiB
```

!!! Huomio
    Kaikki FMI-projektit jakavat saman globaalin kiintiön ja siksi niiden tulisi pyrkiä käyttämään hyviä tietojen säilytyskäytäntöjä.
    Projektikohtainen käyttöä seurataan. Jos sinun tarvitsee säätää FMI-projektisi kiintiöitä, ota yhteys Lasse Jalavaan (CC Matti Keränen) FMI:ssä joko sähköpostitse tai FMI:n Slack-kanavalla 'fmi-computing'.

**Siivousskenaario ajetaan säännöllisesti `/fmi/scratch`-hakemistossa (FMI-projektit) samalla tavalla kuin `/scratch`-hakemistossa (akateemiset projektit). Siivous poistaa kaikki 180 päivää vanhat käyttämättömät tiedostot. Voit pyytää projektisi `/fmi/scratch`-hakemiston valkoinen listausta. Automaattinen siivous on kätevää, joten pyydä valkoinen listaus vain, jos se on todella tarpeen.**

## Käyttö {#usage}

FMI-asiakkaat voivat käyttää sekä tavanomaisia Puhti-kirjautumissolmuja `puhti.csc.fi`, että FMI-spesifisiä kirjautumissolmuja `puhti-login1.fmi.fi` ja `puhti-login2.fmi.fi`.

Puhti FMI toimii samalla tavalla kuin säännöllinen Puhti-järjestelmä, pääasiallinen ero on siinä että

1. FMI-projektit käyttävät `fmi` ja `fmitest`-jakoja säännöllisten jakojen (small, large jne.) sijasta,
2. FMI:n kirjautumissolmut on verkotettu FMI:n sisäisen verkon kautta, mikä tekee verkkoyhteydestä hieman erilaisen, ja
3. FMI:n laskentasolmuilla on samanaikainen monisäikeisyys (SMT/hyper threading) käytössä, joten useimmat työkalut, kuten `htop`,
   näyttävät 80 loogista suorittajaa 40 sijasta, `seff`-suorittimen tehokkuusraportti lasketaan 80 loogisella suorittajalla, jne. Konfiguraatio
   ja käyttö on samanlainen kuin Mahtissa, katso [Hybridi-tehtävät SMT:llä](../computing/running/creating-job-scripts-mahti.md#hybrid-batch-jobs-with-simultaneous-multithreading-smt).

Tavallisten CSC-käyttäjätuen lisäksi, [servicedesk@csc.fi](mailto:servicedesk@csc.fi), FMI-spesifistä tukea on saatavilla sisäisistä wikissä [FMI Puhti Guide](https://wiki.fmi.fi/display/VTUKI/FMI+Puhti+guide), ja hyvin aktiivisella FMI:n Slack-kanavalla 'fmi-computing'.
