
# Etälevyjen liittäminen {#remote-disk-mounts}

Etälevyjen liittämisellä voit käyttää CSC-hakemistojasi samalla tavalla kuin ulkoista levyä tai USB-muistitikkua. Tämä lähestymistapa vaatii yleensä ylimääräisen ohjelmiston asentamista paikalliselle tietokoneellesi, mutta se tekee käytöstä sujuvaa, sillä tiedostojen siirtämiseen paikallisen koneesi ja CSC:n välillä ei tarvita `scp`- tai muita tiedonsiirto-ohjelmia.

macOS- ja Linux-koneilla `sshfs`-ohjelmaa voidaan käyttää tiettyjen levyalueiden liittämiseen CSC:ltä käyttäjän omaan koneeseen. Tämän työkalun avulla CSC:n palvelimien etälevyalueita voidaan käyttää kuin paikallisia hakemistoja. Jotta voit käyttää `sshfs`-ohjelmaa, paikallisella Linux-koneellasi on oltava [FUSE](https://github.com/libfuse/libfuse) ja [`sshfs`](https://github.com/libfuse/sshfs) asennettuna. macOS:n tapauksessa tarvittavat paketit ovat [macFUSE ja SSHFS](https://osxfuse.github.io/).

Huomaa, että sinun on ensin asetettava SSH-avaimet ja ladattava julkinen avain MyCSC:hen voidaksesi työskennellä etälevyjen kanssa, aivan kuten yhdistettäessä tavallisella SSH:lla.
[Lue, miten SSH-avaimet asetetaan täällä](../../computing/connecting/ssh-keys.md).

## sshfs:n käyttö Linuxissa {#using-sshfs-in-linux}

Kun `sshfs` on asennettu Linux-koneellesi, voit luoda etälevyliitoksen komennon syntaksilla:

```bash
sshfs käyttäjänimi@isäntänimi:/polku/hakemistoon /polku/liitoskohtaan
```

Esimerkiksi saadaakseen käyttäjän _kayttaja_ kotihakemiston Puhtilla näkyviin paikalliselle Linux-koneelle, yksi toteuttaisi seuraavat komennot paikallisella koneella:

```bash
mkdir csc_home
sshfs kayttaja@puhti.csc.fi:/users/kayttaja csc_home
```

!!! Huomio
    macOS:llä saatat joutua lisäämään `-o defer_permissions` -valinnan `sshfs`-komentoon, jos saat `Permission denied` -virheitä liitoksen jälkeen.

Ensimmäinen komento luo tyhjän kansion, jota käytetään liitoskohtana toisessa komennossa. Kun etäliitos on muodostettu, voit käyttää hakemistoa kuin mitä tahansa hakemistoa Linux-järjestelmässäsi. Esimerkiksi, jos haluat listata CSC:n kotihakemiston sisällön käyttäjälle _kayttaja_, voi vain syöttää komennon:

```bash
ls csc_home
```

Jos polkua ei ole määritetty, oletusliitetty etähakemisto on käyttäjän kotihakemisto.

Tiedostojärjestelmän irrottamiseen annetaan komento:

```bash
fusermount -u liitoskohta
```

Esimerkissämme komento olisi:

```bash
fusermount -u csc_home
```

macOS:llä korvaa `fusermount -u` komennolla `umount`.
