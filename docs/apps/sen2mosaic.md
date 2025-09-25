---
tags:
  - Free
catalog:
  name: Sen2mosaic
  description: for download, preprocessing and mosaicing of Sentinel-2 products
  description_fi: Sentinel-2-tuotteiden latausta, esikäsittelyä ja mosaiikin muodostusta varten
  license_type: Free
  disciplines:
    - Geosciences
  available_on:
    - Puhti
---

# Sen2mosaic { #sen2mosaic }

[Sen2mosaic](https://sen2mosaic.readthedocs.io/en/latest/) on työkalu [Sentinel-2](https://sentinel.esa.int/web/sentinel/missions/sentinel-2) -aineistojen lataamiseen, esikäsittelyyn ja mosaiikin muodostamiseen.

## Saatavilla { #available }

__Sen2mosaic__ on saatavilla Puhtissa seuraavina versioina:

* 0.2

## Riippuvuudet { #dependencies }

__sen2mosaic__-moduuli riippuu [__geoconda/3.8.8__](./geoconda.md)- ja [__sen2cor/2.9__](./sen2cor.md) -moduuleista, jotka ladataan automaattisesti.

## Käyttö { #usage }

Sen2mosaic sisältyy __sen2mosaic__-moduuliin ja sen voi ladata komennolla

`module load sen2mosaic`

Puhtissa työkalut ajetaan komennoilla
```
s2m_download <arguments>
s2m_preprocess <arguments>
s2m_mosaic <arguments>
```

Lisätietoja kunkin työkalun käytettävissä olevista argumenteista saat komennolla

`s2m_mosaic --help`

tai [sen2mosaic-käyttöoppaasta](https://sen2mosaic.readthedocs.io/en/latest/command_line.html). (Huomaa alaviiva `_` Puhtin työkalujen nimissä!)

Työkaluissa `s2m_preprocess` ja `s2m_mosaic` voit käyttää argumenttia `--n_processes` asettaaksesi käytettävissä olevien CPU-ydinten määrän vastaamaan työsi laskentaydinten määrää.

### Edistynyt käyttö { #advanced-usage }

Lisäasetuksia `s2m_preprocess`-työkalulle voidaan tehdä `L2A_GIPP.xml`-tiedoston avulla (osa [Sen2cor](./sen2cor.md) -pakettia). 
Oletus-GIPP-tiedosto löytyy polusta `/appl/soft/geo/sen2cor/2.9/Sen2Cor-02.09.00-Linux64/lib/python2.7/site-packages/sen2cor/cfg/L2A_GIPP.xml`. 
Kopioi se `$HOME`-hakemistoosi, muokkaa tarpeidesi mukaan ja lisää se kutsuun: `s2m_preprocess --gipp $HOME/L2A_GIPP.xml <other arguments>`

## Lisenssi { #license }

Sen2mosaic julkaistaan [GNU,GPL v3](https://github.com/smfm-project/sen2mosaic/blob/master/LICENSE.md) -lisenssillä.


## Viittaus { #citation }

Sen2mosaic ei tarjoa suositeltua viittaustietoa.

```Samuel Bowers: Sen2mosaic v.0.2. https://github.com/smfm-project/sen2mosaic , last accessed on {date}.```


## Kiitokset { #acknowledgement }

Muistathan mainita CSC:n ja Geoportin julkaisuissasi; tämä on tärkeää hankkeen jatkumisen ja rahoitusraportoinnin kannalta.
Esimerkiksi: "Kirjoittajat kiittävät CSC:tä - Tieteen tietotekniikan keskus (urn:nbn:fi:research-infras-2016072531) sekä tutkimuksen avoimen paikkatiedon infrastruktuuria (Geoportti, urn:nbn:fi:research-infras-2016072513) laskentaresursseista ja tuesta."


## Asennus { #installation }

Lähes kaikki Sen2mosaicin riippuvuudet ovat saatavilla [sen2cor](./sen2cor.md)- ja [geoconda](./geoconda.md) -moduuleista, joten Sen2mosaic asennettiin niiden päälle komennolla `pip install --user opencv-python git+https://github.com/smfm-project/sen2mosaic.git`, kun molemmat moduulit oli ladattu (muista asettaa asennushakemisto ensin komennolla `export PYTHONUSERBASE=/path/to/sen2mosaic/install/directory`. Lyhyempiä komentorivikutsuja varten luotiin komennot `s2m_download`, `s2m_preprocess` ja `s2m_mosaic` lyhentämään alkuperäisiä `python3 /path/to/sen2mosaic/cli/download.py`-komentoja. Tämä viimeinen vaihe ei ole välttämätön käytettävyyden kannalta.  


## Viitteet { #references }

* [Sen2mosaic-käyttöopas](https://sen2mosaic.readthedocs.io/en/latest/)
* [Sen2mosaicin GitHub](https://github.com/smfm-project/sen2mosaic)