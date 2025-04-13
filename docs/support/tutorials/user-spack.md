
# Käyttäjäkohtaisen Spack-moduulin käyttö ohjelmistojen asennuksessa {#using-user-spack-module-for-software-installations}

Spack on pakettienhallintaohjelma supertietokoneille, Linuxille ja macOS:lle. Sitä voidaan käyttää tieteellisten ohjelmistopakettien helppoon asentamiseen. CSC asentaa kehityspaketin, joka sisältää kääntäjät, MPI-kirjastot sekä monia muita kirjastoja ja sovelluksia Spackin avulla. CSC tarjoaa myös käyttäjämoduulin asiakkaille, joka mahdollistaa projektikohtaiset ohjelmistoasennukset Spackin avulla.

!!! warning "Huomautus"
    Spack on edistynyt työkalu ja vaatii ohjelmien kääntämisen ja linkittämisen ymmärtämistä.

!!! info "Saatavilla olevat versiot"
    Tämä opastus olettaa, että olet Puhtilla, jossa on asennettuna `spack/v0.18-user`. Mahtilla on käyttäjille saatavilla kaksi Spackin versiota, `spack/v0.17-user` ja `spack/v0.20-user`. Moduuliversioita lukuun ottamatta toimintatapa on identtinen molemmissa järjestelmissä.

## Spack-instanssin luominen {#creating-a-spack-instance}

Ennen kuin suoritat Spack-moduulin ensimmäistä kertaa, sinun on valmisteltava asennuspaikka, joka voi sijaita joko `/projappl` tai `/scratch` levyalueilla. Sinun on myös asetettava ympäristömuuttuja, joka osoittaa Spack-instanssin sijainnin.

Esimerkiksi, jos haluat luoda Spack-instanssin `/projappl` hakemistoon, voit alustaa ympäristön seuraavasti:

```bash
[maijam@puhti-login11 ~]$ module purge
Seuraavat moduulit eivät purkautuneet:
  (Käytä "module --force purge" purkaaksesi kaikki):

  1) csc-tools
[maijam@puhti-login11 ~]$ export USER_SPACK_ROOT=/projappl/project_2001234/spack-instance-1
[maijam@puhti-login11 ~]$ mkdir -p ${USER_SPACK_ROOT}
[maijam@puhti-login11 ~]$ module load spack/v0.18-user
Suorita user-spack-init alustaksesi käyttäjän asennus kohteessa /projappl/project_2001234/spack-instance-1
[maijam@puhti-login11 ~]$ user-spack-init
[INFO] USER_SPACK_GROUP ei ole asetettu, käytetään oletuksena project_2001234 kohdehakemiston perusteella
```

!!! info "Puhdistaminen ennen latausta"
    Ennen Spackin lataamista sinun on suoritettava `module purge` puhdistaaksesi kaikki oletusarvoiset ympäristön kääntäjät ja kirjastomoduulit, koska ne voivat häiritä Spackin rakennusprosessia.

!!! info "Useita Spack-instansseja"
    Voit käyttää useita Spack-instanseja samassa projektissa. Käytettävä instanssi määritetään ympäristömuuttujalla `$USER_SPACK_ROOT`, joka osoittaa instanssin juurihakemistoon.

!!! info "Alustaminen"
    Ennen kuin käytät Spack-instanssia ensimmäistä kertaa, sinun on alustettava se suorittamalla `user-spack-init` komento.

## Spack-instanssin käyttäminen {#using-the-spack-instance}

Alustettu instanssi voidaan aktivoida purkamalla moduuliympäristö, asettamalla instanssin juuripolku ja lataamalla Spack-moduuli:

```bash
[maijam@puhti-login11 ~]$ module purge
Seuraavat moduulit eivät purkautuneet:
  (Käytä "module --force purge" purkaaksesi kaikki):

  1) csc-tools
[maijam@puhti-login11 ~]$ export USER_SPACK_ROOT=/projappl/project_2001234/spack-instance-1
[maijam@puhti-login11 ~]$ module load spack/v0.18-user
Löydetty olemassa oleva käyttäjän spack-asennus kohteesta /projappl/project_2001234/spack-instance-1
```

### Esimerkki rakennuksesta {#example-build}

```bash
[maijam@puhti-login11 ~]$ spack spec -I --reuse kakoune
Input spec
--------------------------------
 -   kakoune

Concretized
--------------------------------
 -   kakoune@2021.11.08%gcc@11.3.0 arch=linux-rhel8-cascadelake
[^]      ^ncurses@6.2%gcc@11.3.0~symlinks+termlib abi=none arch=linux-rhel8-cascadelake
[^]          ^pkgconf@1.8.0%gcc@11.3.0 arch=linux-rhel8-cascadelake
```

`spack spec` komento näyttää, mitä asennettaisiin tietyn syötteen perusteella. On hyvä tapa suorittaa se ennen asennusta varmistaaksesi, että rakennus on halutun kaltainen. `-I` lippu käytetään paketin ja sen riippuvuuksien nykyisen asennustilan näyttämiseen, kun taas `--reuse` lippu käytetään hyödyntämään jo asennettuja riippuvuuksia aina kun mahdollista. Varsinainen asennus suoritetaan `spack install` komennolla:

```bash
[maijam@puhti-login11 ~]$ spack install --reuse kakoune
[+] /appl/spack/v018/install-tree/gcc-11.3.0/pkgconf-1.8.0-2hkydh
[+] /appl/spack/v018/install-tree/gcc-11.3.0/ncurses-6.2-n4phtn
==> Installing kakoune-2021.11.08-yh4nmfid4st4l7gsmuzqv43o6qt6ckrm
==> No binary for kakoune-2021.11.08-yh4nmfid4st4l7gsmuzqv43o6qt6ckrm found: installing from source
==> Using cached archive: /local_scratch/maijam/spack-build-project_2002567/source-cache/_source-cache/archive/aa/aa30889d9da11331a243a8f40fe4f6a8619321b19217debac8f565e06eddb5f4.tar.bz2
==> No patches needed for kakoune
==> kakoune: Executing phase: 'edit'
==> kakoune: Executing phase: 'build'
==> kakoune: Executing phase: 'install'
==> kakoune: Successfully installed kakoune-2021.11.08-yh4nmfid4st4l7gsmuzqv43o6qt6ckrm
  Fetch: 0.00s.  Build: 34.31s.  Total: 34.31s.
[+] /projappl/project_2001234/spack-instance-1/install_tree/gcc-11.3.0/kakoune-2021.11.08-yh4nmf
```

!!! info "Spec-syntaksi"
    Merkkijono, joka määrittää mikä paketti tulisi asentaa (*spec*), voi olla vain paketin nimi, kuten yllä, mutta usein saatat haluta asentaa tietyn version, mahdollisesti tiettyä kääntäjää käyttäen ja joillakin valinnaisilla asennuslipuilla (esim. GPU-tuettu ohjelmistoversio). Spack käyttää erityistä syntaksia tämän tiedon määrittämiseen, kuten on selitetty virallisessa
    [dokumentaatiossa](https://spack.readthedocs.io/en/latest/basic_usage.html#specs-dependencies).

## Moduulien käyttäminen käyttäjän Spack-asennuksilla {#using-modules-with-user-spack-installations}

Oletuksena Spack luo moduulitiedostot polkuun `$USER_SPACK_ROOT/modules`
ja voit lisätä tämän polun `$MODULEPATH`:iin komennolla:

```bash
[maijam@puhti-login11 ~]$ module use ${USER_SPACK_ROOT}/modules
```

Uuden paketin asentamisen jälkeen saatat joutua regeneroimaan moduulitiedostot. Esimerkiksi:

```bash
[maijam@puhti-login11 ~]$ spack module tcl refresh kakoune
```

Nyt voit nähdä moduulit säännöllisillä `module avail` ja `module spider` komennoilla. Esimerkiksi `kakoune` editori, joka on rakennettu aiemmassa esimerkissä, voidaan etsiä ja ladata seuraavasti:

```bash
[maijam@puhti-login11 ~]$ module spider kakoune

--------------------------------
  kakoune: kakoune/2021.11.08-gcc-11.3.0-yh4n
--------------------------------

    Tämä moduuli voidaan ladata suoraan: module load kakoune/2021.11.08-gcc-11.3.0-yh4n

[maijam@puhti-login11 ~]$ module load kakoune/2021.11.08-gcc-11.3.0-yh4n
```

## Lisälukemista {#further-reading}

- [Virallinen Spack-dokumentaatio](https://spack.readthedocs.io/en/latest/index.html)
- [Spack-opetus](https://spack.readthedocs.io/en/latest/tutorial.html)
- [Spack GitHub-repositorio](https://github.com/spack/spack)

