
# Konttien ajaminen

Jos olet perehtynyt [Docker-kontteihin](https://en.wikipedia.org/wiki/Docker_(software)), [Apptainer-kontit](https://apptainer.org/) (aikaisemmin tunnettu nimellä Singularity) ovat käytännössä sama asia, mutta ne soveltuvat paremmin monen käyttäjän järjestelmiin, kuten CSC:n supertietokoneisiin. Kontit tarjoavat eristetyn ohjelmisto-ympäristön kullekin sovellukselle, mikä helpottaa monimutkaisten sovellusten asentamista. Jaetuissa tiedostojärjestelmissä, kuten CSC:n supertietokoneilla käytettävissä, käyttöajat voivat olla myös paljon lyhyempiä kuin vaihtoehtoilla, kuten conda.

Lisätietoja saat lukemalla [yleiskatsauksen kontteihin](overview.md) tai [Apptainer käyttäjän oppaan](https://apptainer.org/docs/user/main/).

## Apptainerin ajaminen {#running-apptainer}

CSC:n supertietokoneet Puhti ja Mahti tukevat molemmat Apptainer-konttien ajamista. Monissa käyttötapauksissa CSC:n henkilökunta on tarjonnut valmiiksi tehdyt kontit, joita voidaan käyttää yksinkertaisesti lataamalla vastaava moduuli. Tarkista [sovellussivut](../../apps/index.md), onko haluamallesi sovellukselle jo asennettu kontti saatavilla. Katso kyseisen sovelluksen sivulta tarkat käyttöohjeet.

Jos huomaat, että jokin kontti puuttuu, jonka uskot olevan yleisesti hyödyllinen, voit pyytää meitä asentamaan sen ottamalla yhteyttä [CSC:n palvelupisteeseen](../../support/contact.md). Vaihtoehtoisesti voit tutustua [oman konttikuvan rakentamiseen](creating.md).

### `apptainer_wrapper`-komennon käyttäminen {#using-apptainer-wrapper}

Ellei muuta ole sovelluksen dokumentaatiossa mainittu, kaikki CSC:n Apptainer-pohjaiset sovellukset voidaan helposti käyttää `apptainer_wrapper`-komennolla. Monissa tapauksissa myös muita yleisiä komentoja, kuten `python` tai `R`, on kääritty saumattoman käyttökokemuksen saavuttamiseksi. Katso [yksittäiset sovellusten dokumentaatiosivut](../../apps/index.md) saadaksesi lisätietoja.

Kun lataat konttiin perustuvan moduulin, se asettaa sopivat arvot `SING_IMAGE`- ja `SING_FLAGS`-ympäristömuuttujille, joita `apptainer_wrapper` käyttää asettaakseen kaikki sopivat vaihtoehdot automaattisesti Apptainerin ajamiseen.

Tyypillinen tapa ajaa jotain aktivoidulla kontilla on seuraava:

```bash
module load modulename
apptainer_wrapper exec command_to_run
```

Toinen hyödyllinen komento on `apptainer_wrapper shell`, joka aloittaa shell-istunnon kontin sisällä.

Kontin sisällä päähakemisto on yleensä vain luku -muodossa, eli et voi muuttaa itse kuvaa. Yleisiä polkuja kuten `/projappl`, `/scratch` ja käyttäjien kotihakemistot on "sidottu" todellisiin (isäntä)polkuihin ja niitä voidaan siten lukea ja niihin voidaan kirjoittaa normaalisti kontin sisältä.

Voit myös käyttää `apptainer_wrapper`-komentoa itse luomiesi konttien kanssa. Sinun tarvitsee vain asettaa `SING_IMAGE` osoittamaan oikeaan Apptainer-kuvatiedostoon. Esimerkiksi:

```bash
export SING_IMAGE=/path/to/apptainer_image.sif

apptainer_wrapper exec command_to_run
```

Voit myös asettaa lisäasetuksia Apptainerille `SING_FLAGS`-muuttujan kautta. Esimerkiksi GPU:iden käyttämiseksi:

```bash
export SING_FLAGS=--nv
```

### Apptainerin ajaminen suoraan {#running-apptainer-directly}

Voit myös ajaa Apptainerin suoraan, jos `apptainer_wrapper`-ohjelmointi ei jostain syystä sovi sinulle. Silloin sinun on itse annettava polku konttikuvaan ja sidottava kaikki polut, joita sinun tarvitsee päästä kuvan sisältä. Huomaa, että oletuksena jotkin polut, kuten `HOME` ja `CWD`, on [sidottu automaattisesti](https://apptainer.org/docs/user/main/bind_paths_and_mounts.html#system-defined-bind-paths).

Käyttöesimerkit:

```bash
apptainer exec -B /scratch:/scratch /path/to/apptainer_image.sif command_to_run
apptainer shell /path/to/apptainer_image.sif
```

Jos tarvitset GPU-tuenta, lisää `--nv`-lippu komentoosi.

### Datan asennus SquashFS:llä {#mounting-datasets-with-squashfs}

Yleinen ongelma supertietokoneissa on, että suurilla tiedostomäärillä olevan datan käyttö jaetussa tiedostojärjestelmässä on erittäin tehotonta. Lisätietoja lue [tekninen kuvaus Lustre-tiedostojärjestelmästä](../lustre.md). Apptaineria käyttäen yksi potentiaalinen ratkaisu tähän ongelmaan olisi [datan käyttö SquashFS-kuvalla](https://sylabs.io/guides/3.7/user-guide/bind_paths_and_mounts.html#squashfs-image-files).

Luo ensin SquashFS-kuva datastasi, vähentäen se yhdeksi suureksi tiedostoksi. Suosittelemme tekemään tämän [interaktiivisessa istunnossa](../running/interactive-usage.md) käyttäen nopeaa paikallista levyä tilapäiseen tallennukseen. Esimerkiksi, käynnistääksesi interaktiivisen istunnon, jossa on 100 GiB paikallista levytilaa (säädä kokoa tarpeen mukaan), voit ajaa:

```bash
sinteractive --time 1:00:00 --tmp 100 --cores 4
```

Sitten interaktiivisessa istunnossa:
```bash
# Poimi yksittäiset tiedostot paikalliselle levylle
cd $LOCAL_SCRATCH
tar xf /scratch/project/my_dataset.tar
# Luo squashfs-tiedosto
mksquashfs my_dataset my_dataset.sqfs -processors 4
# Siirrä syntyvä squashfs-tiedosto takaisin jaettuun levyyn
mv my_dataset.sqfs /scratch/project/
```

Ylläolevissa komennoissa oletetaan, että olet tallentanut datasetin tar-pakettiin ja se avautuu hakemistoon nimeltä `my_dataset`. Säädä komentoja omaan tilanteeseesi sopivaksi.

Seuraavaksi sinun tulisi asentaa tämä kuva Apptainerin suorittamiseen, jotta se näkyisi normaalina hakemistona kontin sisällä. Meidän tarvitsee vain lisätä bind-asetus Apptainerin komennolle: `-B /scratch/project/my_dataset.sqfs:/data:image-src=/`. Jos käytät `apptainer_wrapper`-ohjelmointia, voit tehdä tämän lisäämällä se `SING_FLAGS` ympäristömuuttujaan:

```
export SING_FLAGS="-B /scratch/project/my_dataset.sqfs:/data:image-src=/ $SING_FLAGS"
```

Tämän jälkeen datasetti on käytettävissä `/data`-polun alla kontin sisällä.
