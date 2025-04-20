# Etäkiekkojen liittäminen {#remote-disk-mounts}

Etäkiekkojen liittämisen avulla voit käyttää CSC:n hakemistoja tavalla, joka muistuttaa ulkoisen levyn tai USB-muistitikun käyttöä. Tämä tapa vaatii yleensä ylimääräisen ohjelmiston asentamisen paikalliselle tietokoneellesi, mutta näin käyttökokemus on sujuva, eikä esimerkiksi `scp`:tä tai muita tiedostonsiirto-ohjelmia tarvita tiedostojen siirtämiseksi oman koneesi ja CSC:n välillä.

macOS- ja Linux-koneilla voidaan käyttää `sshfs`-ohjelmaa CSC:n tiettyjen levyalueiden liittämiseen käyttäjän omalle koneelle. Tämän työkalun avulla CSC:n palvelimien etälevyalueita voi käyttää aivan kuten paikallisia hakemistoja. `sshfs`:n käyttöön tarvitset, että Linux-koneellesi on asennettu [FUSE](https://github.com/libfuse/libfuse) ja [`sshfs`](https://github.com/libfuse/sshfs). macOS:llä tarvittavat paketit ovat [macFUSE ja SSHFS](https://osxfuse.github.io/).

Huomaa, että sinun tulee olla ottanut SSH-avaimet käyttöön ja ladannut julkinen avaimesi MyCSC:hen, jotta voit käyttää etäkiekkojen liittämistä – aivan kuten tavallisessa SSH-yhteydessä.
[Lue ohjeet SSH-avaimien käyttöönottoon täältä](../../computing/connecting/ssh-keys.md).

## Sshfs:n käyttö Linuxissa {#using-sshfs-in-linux}

Kun `sshfs` on asennettu Linux-koneellesi, voit liittää etäkiekon seuraavalla komentorakenteella:

```bash
sshfs username@hostname:/path/to/dir /path/to/mountpoint
```

Jos esimerkiksi käyttäjän _kayttaja_ kotihakemisto Puhti-palvelimella halutaan näkyviin paikalliselle Linux-koneelle, suoritetaan seuraavat komennot paikallisella koneella:

```bash
mkdir csc_home
sshfs kayttaja@puhti.csc.fi:/users/kayttaja csc_home
```

!!! Huomio
    macOS:llä voit joutua lisäämään `-o defer_permissions` -valitsimen
    `sshfs`-komentoon, jos saat `Permission denied` -ilmoituksia liittämisen jälkeen.

Ensimmäinen komento luo tyhjän hakemiston, jota käytetään liitoskohtana toisessa komennossa. Kun etäliitos on muodostettu, hakemistoa voi käyttää kuin mitä tahansa hakemistoa Linux-järjestelmässäsi. Esimerkiksi, jos haluaa listata _kayttaja_-käyttäjän CSC-kotikansion sisällön, riittää komento:

```bash
ls csc_home
```

Jos polkua ei erikseen määritellä, oletuksena liitetään käyttäjän kotihakemisto.

Tiedostojärjestelmän irrottamiseksi annetaan komento:

```bash
fusermount -u mountpoint
```

Esimerkissämme komento olisi:

```bash
fusermount -u csc_home
```

macOS:ssä `fusermount -u`-komennon tilalla käytä komentoa `umount`.