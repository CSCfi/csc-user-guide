# Perustietoa kuvista {#basic-information-about-images}

[TOC]

CSC tarjoaa joukon standardikuvia, jotka sopivat hyvin pilvikäyttöön. Useimmissa tapauksissa voit käyttää näitä kuvia omien kuvien luomisen sijaan. Kuvat luodaan automaattisesti käyttäen _diskimage-builder_-työkalua. Jos olet kiinnostunut siitä, miten nämä kuvat luodaan, katso tämä [GitHub-sivu]. Kuvat päivitetään säännöllisesti, jotta ne sisältävät uusimmat tietoturvapäivitykset, kun virtuaalikoneet otetaan käyttöön.

On mahdollista, että joissakin käyttötapauksissa automaattisesti luodut kuvat eivät ole sopivia. Tässä tapauksessa on mahdollista luoda omia kuvia ja käyttää niitä sijasta. Kuitenkin omia kuvia luodessa on huomioitava eräitä seikkoja, joita ei tarvitse miettiä käytettäessä oletuskuvia. Lisätietoja saat osiosta [Edistyneet kuvat](adding-images.md).

## CSC:n tarjoamien kuvien pääominaisuudet {#the-main-features-of-the-images-provided-by-csc}

CSC:n tarjoamat kuvat ovat pääasiassa samanlaisia kuin alkuperäiset.

* Useimmat kuvat tulevat valmiiksi määritetyn käyttäjätunnuksen `cloud-user` kanssa, vaikka tästä säännöstä on joitakin poikkeuksia.
* Varmistamme, että kuvat päivitetään ennen julkaisua, jotta varmistumme niiden toimivuudesta.
* `-Cuda`-kuvat tulevat esiasennetuilla uusimmilla CUDA-ajureilla.
* Otamme automaattiset päivitykset käyttöön.
* Poistamme salasanakirjautumisen käytöstä.
* Lisäämme joskus muutamia hyödyllisiä paketteja, kuten _vim_ tai _ntp_. Yritämme pitää lisäpaketit minimissä.

## Kuvat {#images}

|Kuva|Käyttäjätunnus|Muokattu <br/>|
|--- |:---:|:---:|
|CentOS-9-Stream |**cloud-user** |ei  |
|AlmaLinux-8     |**almalinux**  |ei  |
|AlmaLinux-9     |**almalinux**  |ei  |
|Ubuntu-18.04    |**ubuntu**     |ei  |
|Ubuntu-20.04    |**ubuntu**     |ei  |
|Ubuntu-22.04    |**ubuntu**     |ei  |
|Ubuntu-24.04    |**ubuntu**     |ei  |

### CentOS-9-Stream {#centos-9-stream}

CentOS-yhteisö ylläpitää nyt aktiivisesti CentOS-9-Streamia, joka on RHEL:n ylävirran haara. Koska päivitykset ja muutokset testataan ensin CentOS:ssa ja vasta sitten otetaan käyttöön Red Hat Enterprise Linuxissa (RHEL), tuloksena oleva käyttöjärjestelmä on mahdollisesti vähemmän vakaa verrattuna aiempaan versioon, jolloin RHEL oli CentOS:n ylävirta. CentOS-yhteisö [korostaa](https://blog.centos.org/2020/12/future-is-centos-stream/), että Stream-versio on kuitenkin erittäin lähellä vakaudeltaan vastaavaa RHEL-versiota. Huomaa, että tämä on kuvan ylävirran versio, eli emme tee mitään muutoksia kuvaan ennen kuin se julkaistaan palveluissamme. Oletuskäyttäjänimi on `cloud-user`.

### AlmaLinux-8 ja AlmaLinux-9 {#almalinux-8-and-almalinux-9}

AlmaLinux on Linux-jakelu, joka luotiin vastauksena CentOS-8 projektin päättämiseen ja CentOS:in rakennusprosessin perustavanlaatuisen muutoksen vuoksi, mikä vaikutti CentOS:in perinteiseen vakauteen. AlmaLinux pyrkii olemaan täysin yhteensopiva Red Hat Enterprise Linuxin kanssa, ja näin ollen Linux-jakelu ottaa tehokkaasti sen roolin, mikä CentOS:lla oli ennen siirtymistä Stream-versioihin. Huomaa, että nämä ovat AlmaLinux-kuvien ylävirran versioita, ja niiden oletuskäyttäjänimi on `almalinux` `cloud-user` sijaan.

### Ubuntu-24.04, 22.04, 20.04 ja 18.04 LTS {#ubuntu-24-04-22-04-20-04-and-18-04-lts}

Jotkut pitävät suklaasta, toiset mansikasta. Tämä on valinta niille, jotka eivät halua käyttää CentOS:ia. Huomaa, että nämä ovat Ubuntun kuvien ylävirran versioita, ja niiden oletuskäyttäjänimi on `ubuntu` `cloud-user` sijaan.

## Huurrekukka-kuvat {#snowflake-images}

Näitä kuvia ei pitäisi käyttää ilman todella hyvää syytä. Saatat paremminkin hyötyä [oman kuvan luomisesta](adding-images.md).

Jos sinulla on mielessä kuvia, joita meidän tulisi lisätä, älä epäröi ottaa yhteyttä [Service Deskiin](mailto:servicedesk@csc.fi).

### cirros {#cirros}

Tämä on hyvin pieni kuva, jota voidaan käyttää käynnistämään instanssi erittäin nopeasti. Tämä voi olla hyödyllistä testauksessa Poudassa, kuten verkon toiminnan testaamisessa tai instanssin käynnistämisnopeuden tarkistamisessa. Tätä ei pitäisi käyttää pysyviin VM:iin, ja instanssi tulisi aina poistaa testauksen jälkeen. Tavallisten käyttäjien ei pitäisi juuri käyttää tätä kuvaa, ja jos olet epävarma, CentOS ja Ubuntu ovat parempia valintoja 99% ajasta.

[GitHub-sivu]: https://github.com/CSC-IT-Center-for-Science/diskimage-builder-csc-automation