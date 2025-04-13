
# Tiedostoselain ja tallennuspalveluiden käyttäminen verkkoliittymistä {#file-browser-and-accessing-storage-services-from-the-web-interfaces}

Tiedostoselain voidaan avata _Tiedostot_-osiosta ylävalikossa (tämä näyttää luettelon kaikista projektin levyaluesista) tai käyttämällä kotikansion pikakuvaketta aloitussivun (koontinäytön) _Kiinnitetyt sovellukset_ -näkymässä. Tiedostoselaimessa voit ladata/siirtää tiedostoja, luoda uusia tiedostoja ja kansioita tai avata komentokehotteen nykyisessä kansiossa. Sitä voidaan käyttää myös datan siirtämiseen Allas-palveluiden, LUMI-O:n, IDA:n ja supertietokoneen välillä.

!!! warning "Tärkeää"
    Pidä tiedostoselainta auki, kunnes tiedostonsiirto on valmis, jotta varmistetaan, että se onnistuu. Huomaa myös, että ladatut tiedostot korvaavat olemassa olevat samannimiset tiedostot _ilman erillistä kyselyä_! Tällä hetkellä yksittäisten tiedostojen maksimikoko on **10 GB**.

Tiedostoon napsauttamalla sitä avataan vain katselutilassa. Lisää vaihtoehtoja, kuten muokkaaminen, nimetäminen ja poistaminen, saa painikkeella, jossa on kolme pistettä tiedostonimen vieressä.

Tiedostoselaimeen kuuluu yksinkertainen tekstieditori. Muutamia tärkeitä huomioita editorista:

- Jos muutoksia ei ole tehty, _tallenna_-painike on harmaana.
- _Tallenna nimellä_ -toimintoa ei ole.
- Käyttäjää ei varoiteta, jos lukuoikeudellinen tiedosto avataan editorissa. Täten muutokset eivät tule voimaan tiedostossa.

## Allas ja LUMI-O pääsy {#accessing-allas-and-lumi-o}

Verkkoliittymien tiedostoselaimesta pääsee myös käyttämään **[Allas-objektitallennuspalvelua](../../computing/allas.md)**.

Autentikoinnin määrittäminen Alttaa varten:

1. Avaa _Pilvitallennuskonfiguraatio_-sovellus joko _Kiinnitetyt sovellukset_-osiossa tai työkalut-pudotusvalikossa.
2. Kun avaat sovelluksen, sinulta kysytään CSC-salasana sivun alareunassa.
3. Kun olet tunnistautunut salasanallasi, voit luoda sekä S3- että Swift-yhteyksiä, joita kutsutaan myös remotes, Allakseen. Jokainen remote on voimassa vain yhden projektin ajan, mutta voit luoda useita remotes, jotka kattavat eri projektit.
4. Luodut remotes ovat näkyvissä _Tiedostot_-pudotusvalikossa sekä tiedostoselaimessa (esim. `s3allas-project_2001234`).

!!! info "Huomaa"
    Swift- ja S3-protokollat eivät ole täysin yhteensopivia keskenään, erityisesti yli 5 GB kokoisissa tiedostoissa. Lisätietoja protokollien eroista löytyy [Allas-protokollat](../../data/Allas/introduction.md#protocols).

**[LUMI-O](https://docs.lumi-supercomputer.eu/storage/lumio/)** on myös käytettävissä tiedostoselaimen kautta.

LUMI-O:n autentikoinnin määrittäminen:

1. Avaa _Pilvitallennuskonfiguraatio_-sovellus joko _Kiinnitetyt sovellukset_-osiossa tai _Työkalut_-pudotusvalikossa.
2. Valitse _Configure new remotes_-osiossa LUMI-O-välilehti.
3. Valitse projekti, johon autentikointi luodaan, sekä haluatko s3cmd-konfiguraatiota ja julkista remotea.

!!! warning "Julkiset LUMI-O-remotet"
    Julkisesti LUMI-O-remotelle ladatut tiedostot (esim. `lumi-462001234-public`) voivat olla kenen tahansa saatavilla URL-osoitteella `https://<project-number>.lumidata.eu/<bucket_name>`. Ole varovainen, ettet lataa yksityisiä tietoja sinne.

Kun olet määrittänyt yhteyden Alttaan/LUMI-O-on verkkoliittymässä, voit käyttää tiedostoselainta päästäksesi Alttaan/LUMI-O-on samalla tavalla kuin pääsy jaettuun tiedostojärjestelmään supertietokoneissa.

Huomaa, että määritetyt remotet, jotka eivät ole saavutettavissa esimerkiksi vanhentuneen autentikoinnin tai verkkoyhteysongelmien vuoksi, eivät näy _Tiedostot_-pudotusvalikossa.

!!! warning "Suuria tiedostoja"
    Suurten tiedostojen lataaminen paikalliselta tietokoneeltasi Alttaan verkkoliittymien kautta ei ole tällä hetkellä suositeltavaa teknisten rajoitusten vuoksi.

Jos et enää tarvitse määritettyä remotea, voit perua sen pääsytunnuksen remoteluettelosta tai poistaa remoten konfiguraatiosta. Remotet, joita ei ole konfiguroitu Pilvitallennuskonfiguraatio-sovelluksen kautta, ovat myös näkyvissä ja ne voidaan poistaa, mutta niiden pääsytunnuksia ei voi peruuttaa.
![Pilvitallennuskonfiguraatio-ohjelman remote-lista](../../img/ood_cloud_storage_conf_table.png)

## IDA:n käyttäminen {#accessing-ida}

[IDA-tallennuspalvelua](../../data/ida/using_ida.md) voidaan myös käyttää verkkoliittymistä. Kuitenkin, jotkut keskeiset ominaisuudet, kuten datan siirtäminen valmistelualueelta lukitusalueelle, ovat mahdollisia vain [IDA:n verkkoliittymän](https://ida.fairdata.fi) kautta.

IDA:n käyttö Puhti/Mahti-verkkoliittymistä edellyttää, että se konfiguroidaan käytettäväksi Rclonella kirjautumisnodessa seuraavasti:

```
module load allas
rclone config
```

Rclone-konfiguraatioiden käyttöliittymässä, luo uusi remote seuraavilla asetuksilla:

1. Tallennus: WebDAV (#45)
2. URL: <https://ida.fairdata.fi/remote.php/webdav/>
3. Toimittaja: Nextcloud (#1)
4. Käyttäjätunnus: CSC-käyttäjätunnuksesi
5. Salasana:
     1. Kirjaudu sisään [IDA:n verkkoliittymään](https://ida.fairdata.fi).
     2. Siirry oikeassa yläkulmassa asetuksiin.
     3. Siirry _Tietoturva_-välilehteen ja luo uusi sovellussalasana.
     4. Kopioi salasana ja liitä se Rclone-konfiguraation käyttöliittymään.
6. Pääsytunnus: Jätä tyhjäksi
7. Laajennettu konfiguraatio: Ei

Kun Rclone-konfiguraatio on valmis, käynnistä Puhti/Mahti-verkkoliittymä uudelleen valitsemalla _Käynnistä verkkopalvelin uudelleen_ apuvalikosta ylävalikon oikealla puolella. IDA:n tiedostoselaimeen voi nyt päästä, jossa voit ladata/siirtää, siirtää ja muokata tiedostoja valmistelualueella, sekä katsoa ja ladata tiedostoja jäädytetyltä alueelta.
