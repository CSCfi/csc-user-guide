# Kuinka projektin ja väliaikaistiedostojen oikeudet toimivat? {#how-do-the-project-and-scratch-file-permissions-work}

CSC asettaa projektien ja väliaikaiskansioiden oikeudet siten, että
kaikilla projektin jäsenillä on pääsy kansioihin. Tarkemmin sanottuna,
kansiot omistaa järjestelmänvalvojan tili, mutta niihin liittyvällä
Unix-ryhmällä on luku- ja kirjoitusoikeudet. Lisäksi, GID-oikeus
asetetaan käytettäväksi, jolloin uudet tiedostot ja kansiot ovat
oletusarvoisesti projektiryhmän omistamia. Huomaa, että myös uusiin
kansioihin periytyy GID-oikeus.

Voit tarkistaa oikeudet komennolla `ls -l`. Oikeita oletusoikeuksia
alikansiolle ovat `drwxrws---`. Huomaa pieni `s`-kirjain ryhmän
oikeuksissa x:n sijaan. Jos näet ison `S`-kirjaimen, kansiolla ei ole
suoritusoikeuksia, jotka ovat tarpeen ryhmätason pääsyyn.

Jos alikansion GID-oikeus poistetaan tahallisesti tai vahingossa, kaikki
uudessa alikansiossa olevat tiedostot ja kansiot omistaa käyttäjän
oletushenkilökohtainen ryhmä, eikä muut ryhmän jäsenet voi käyttää niitä.
Jos pääsyä tarvitaan, näiden tiedostojen ja kansioiden omistajan tulee
muuttaa ryhmä ja korjata oikeudet. Huomaa, että monet työkalut ja asennusskriptit
muokkaa oletusoikeuksia.

Esimerkki puuttuvasta SGID-oikeudesta:

```bash
[maijam@puhti project_2009999]$ mkdir -m 00770 demofolder
[maijam@puhti project_2009999]$ ls -l
total 0
drwxrwx---. 2 maijam project_2009999       4096 Feb 15 14:52 demofolder
[maijam@puhti project_2009999]$ touch demofolder/my-file
[maijam@puhti project_2009999]$ ls -l demofolder/
total 0
-rw-rw----. 1 maijam maijam 0 Feb 15 14:52 my-file
[maijam@puhti project_2009999]$ chmod g+s demofolder/
[maijam@puhti project_2009999]$ ls -l
total 0
drwxrws---. 2 maijam project_2009999       4096 Feb 15 14:52 demofolder
[maijam@puhti project_2009999]$ touch demofolder/my-other-file
[maijam@puhti project_2009999]$ ls -l demofolder/
total 0
-rw-rw----. 1 maijam maijam          0 Feb 15 14:52 my-file
-rw-rw----. 1 maijam project_2009999 0 Feb 15 14:53 my-other-file
```

Esimerkki oikeuksien korjaamisesta:

```bash
[maijam@puhti project_2009999]$ chgrp -R project_2009999 demofolder/
[maijam@puhti project_2009999]$ lfs find demofolder -type d -0 | xargs -0 chmod 2770
[maijam@puhti project_2009999]$ lfs find demofolder -type f -0 | xargs -0 chmod g+rwX
```

Lisätietoja Linux-tiedosto-oikeuksista RedHatin dokumentaatiossa:
[Linux-oikeudet: SUID, SGID ja sticky bit](https://www.redhat.com/sysadmin/suid-sgid-sticky-bit).