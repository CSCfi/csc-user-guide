# Tiedostoselain ja tallennuspalveluihin pääsy verkkokäyttöliittymistä { #file-browser-and-accessing-storage-services-from-the-web-interfaces }

Tiedostoselaimen voi avata yläreunan navigointipalkin _Files_-osiosta (tässä näkyy luettelo kaikista projektien levyalueista) tai käyttämällä kotihakemistoosi johtavaa pikakuvaketta aloitussivun (dashboard) _Pinned Apps_ -näkymässä. Tiedostoselaimessa voit lähettää/noutaa tiedostoja, luoda uusia tiedostoja ja hakemistoja tai avata komentokuoren nykyisessä hakemistossa. Sitä voi käyttää myös datan siirtämiseen Allaksen, LUMI-O:n, IDA:n ja superkoneen välillä.

!!! warning "Tärkeää"
    Pidä tiedostoselaimen välilehti auki tiedonsiirron aikana, jotta siirto valmistuu onnistuneesti. Huomaa myös, että lähetetyt tiedostot korvaavat samannimiset olemassa olevat tiedostot _ilman varmistuskyselyä_! Tällä hetkellä yksittäisen tiedoston lähetyksen enimmäiskoko on **10 GB**.

Tiedostoa napsauttamalla se avautuu vain luku -tilaan. Lisätoimintoja, kuten muokkaus, uudelleennimeäminen ja poistaminen, saat esiin tiedostonimen vieressä olevasta kolmen pisteen painikkeesta. 

Tiedostoselaimessa on mukana yksinkertainen tekstieditori. Tärkeitä huomioita editorista:

- Jos muutoksia ei ole tehty, _save_-painike on harmaana.
- _save-as_-toimintoa ei ole.
- Käyttäjää ei ilmoiteta, jos editorilla avataan kirjoitussuojattu (read-only) tiedosto. Tällöin muutoksia ei tallenneta tiedostoon.

## Pääsy Allakseen ja LUMI-O:hon { #accessing-allas-and-lumi-o }

**[Allas-objektivarastopalveluun](../../data/Allas/index.md)** pääsee myös verkkokäyttöliittymistä tiedostoselaimen kautta.

Allaksen todennuksen määrittäminen: 

1. Avaa _Cloud storage configuration_ -sovellus joko _Pinned Apps_ -näkymästä tai yläreunan _Tools_-pudotusvalikosta.
2. Kun avaat sovelluksen, sinua pyydetään syöttämään CSC-salasanasi sivun alaosassa.
3. Kun olet tunnistautunut salasanallasi, voit luoda sekä S3- että Swift-yhteyksiä (remotes) Allakseen. Kukin remote on voimassa vain yhdessä projektissa, mutta voit luoda useita remoteja eri projekteja varten.
4. Luodut remotet näkyvät yläreunan _Files_-pudotusvalikossa sekä tiedostoselaimessa (esim. `s3allas-project_2001234`).

!!! info "Huomautus"
    Swift- ja S3-protokollat eivät ole täysin yhteensopivia keskenään, erityisesti yli 5 Gt:n tiedostojen osalta. Lisätietoja protokollien eroista: [Allaksen protokollat](../../data/Allas/introduction.md#protocols).

**[LUMI-O:ta](https://docs.lumi-supercomputer.eu/storage/lumio/)** voi myös käyttää tiedostoselaimen kautta.

LUMI-O:n todennuksen määrittäminen:

1. Avaa _Cloud storage configuration_ -sovellus joko _Pinned Apps_ -näkymästä tai yläreunan _Tools_-pudotusvalikosta.
2. Valitse LUMI-O-välilehti _Configure new remotes_ -osiossa.
3. Valitse projekti, jolle todennus luodaan, sekä haluatko s3cmd-määrityksen ja julkisen remoten.

!!! warning "Julkiset LUMI-O-remotet"
    Julkisiin LUMI-O-remoteihin (esim. `lumi-462001234-public`) ladattuihin tiedostoihin pääsee kuka tahansa URL-osoitteella
    `https://<project-number>.lumidata.eu/<bucket_name>`. Varo, ettet lataa sinne yksityistä dataa.

Kun olet määrittänyt yhteyden Allakseen/LUMI-O:hon verkkokäyttöliittymästä, voit käyttää tiedostoselainta päästäksesi Allakseen/LUMI-O:hon samaan tapaan kuin superkoneiden jaettuun tiedostojärjestelmään.

Huomaa, että remotet, joihin ei päästä esimerkiksi vanhentuneen todennuksen tai verkkoyhteysongelmien vuoksi, eivät näy _Files_-pudotusvalikossa.

!!! warning "Suuret tiedostot"
    Suurten tiedostojen lähettäminen paikalliselta koneelta Allakseen verkkokäyttöliittymien kautta ei toistaiseksi ole suositeltavaa teknisten rajoitteiden vuoksi.

Jos et enää tarvitse määritettyä remotea, voit peruuttaa sen käyttöoikeustunnuksen remotelistassa tai poistaa remoten kokoonpanosta. Myös remotet, joita ei ole määritetty _Cloud storage configuration_ -sovelluksella, näkyvät ja ne voidaan poistaa, mutta niiden käyttöoikeustunnuksia ei voi peruuttaa.
![Cloud storage configuration -työkalun remote-luettelo](../../img/ood_cloud_storage_conf_table.png)

## Pääsy IDA:an { #accessing-ida }

[IDA-tallennuspalvelua](../../data/ida/using_ida.md) voidaan käyttää myös verkkokäyttöliittymistä. Joitakin keskeisiä toimintoja, kuten datan siirtäminen staging-alueelta frozen-alueelle, on kuitenkin mahdollista tehdä vain [IDA:n verkkokäyttöliittymässä](https://ida.fairdata.fi).

Jotta IDA:ta voi käyttää Puhti/Mahti-verkkokäyttöliittymistä, se on ensin määritettävä Rclonen käyttöön kirjautumissolmun komentokuoressa seuraavasti:

```
module load allas
rclone config
```

Luo Rclonen määritysikkunassa uusi remote seuraavilla asetuksilla:

1. Storage: WebDAV (#45)
2. URL: <https://ida.fairdata.fi/remote.php/webdav/>
3. Vendor: Nextcloud (#1)
4. Username: CSC-käyttäjätunnuksesi
5. Password:
      1. Kirjaudu [IDA:n verkkokäyttöliittymään](https://ida.fairdata.fi).
      2. Siirry oikean yläkulman asetuksiin.
      3. Avaa _Security_-välilehti ja luo uusi sovellussalasana.
      4. Kopioi salasana ja liitä se Rclonen määritysikkunaan.
6. Bearer token: Jätä tyhjäksi
7. Advanced config: No

Kun Rclone-määritys on valmis, käynnistä Puhti/Mahti-verkkokäyttöliittymä uudelleen valitsemalla _Help_-valikosta yläoikealta _Restart web server_. IDA on nyt käytettävissä tiedostoselaimessa, jossa voit lähettää, ladata, siirtää ja muokata tiedostoja staging-alueella sekä katsella ja ladata tiedostoja frozen-alueelta.