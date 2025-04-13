
# Minkä hakemiston minun tulisi käyttää analysoidessani useita pieniä tiedostoja? {#which-directory-should-i-use-to-analyze-many-small-files}

[Vuorovaikutteinen erätöiden ajo](../../computing/running/interactive-usage.md) Puhti-palvelussa sallii sinun aloittaa shell-istunnon laskentasolmulla enintään:

* 8 ydintä
* 76 GB muistia
* 7 päivää ajoaikaa
* 720 GB *nopeaa paikallista työsarakkoa*

Käynnistäksesi vuorovaikutteisen istunnon Puhti-palvelussa, suorita komento:

```bash
sinteractive -i
```

Yksi hyödyllisistä ominaisuuksista vuorovaikutteisissa erätöissä Puhti-palvelussa on NVMe-pohjainen [nopea paikallinen työsarja](../../computing/disk.md#temporary-local-disk-areas) (`$LOCAL_SCRATCH`), jota voit pyytää. "Normaalit" Lustre-pohjaiset, projektikohtaiset hakemistot *scratch* ja *projappl* voivat tallentaa suuria datamääriä ja ovat kaikkien Puhti-solmujen käytettävissä. Kuitenkin nämä hakemistot ovat [tehottomia hallitessaan tuhansia tiedostoja](../../computing/running/throughput.md#inputoutput-efficiency).

Yleensä sinun tulisi välttää työnkulkuja, jotka edellyttävät suuren määrän pienten tiedostojen luomista. Jos sinun kuitenkin täytyy työskennellä tuhansien tiedostojen parissa, sinun tulisi harkita NVMe-pohjaisten väliaikaisten paikallisten levyalueiden käyttöä, joko normaalien tai vuorovaikutteisten erätöiden kautta. Paikallinen työsara on solmukohtainen ja näkyy vain työtehtävälle, joka sitä pyytää. Kun työ päättyy, paikallinen työsara tyhjennetään. Tämän vuoksi sinun on aina ensin tuotava tietoaineistosi paikalliselle levylle, ja kun olet valmis, kopioitava tiedot, jotka haluat säilyttää, jonnekin pysyvämpään tallennustilaan, kuten scratch tai Allas.

Demonstroidaksesi paikallisen työsaran tehokkuutta, tutkitaan esimerkkihakemistoa nimeltä `big_data`. Hakemisto sisältää noin 100 GB dataa 120 000 tiedostossa. Aluksi data on pakattu yhdeksi tar-arkistoksi projektihakemiston työsarkaan 2001234 (`/scratch/project_2001234/big_data.tar`).

Ensimmäiseksi käynnistämme vuorovaikutteisen erätyön, jossa on 2 ydintä, 4000 MB muistia ja 250 GB nopeaa paikallista väliaikaista levytilaa.

```bash
sinteractive --cores 2 --mem 4000 --tmp 250
```

Analyysi tapahtuu sitten kolmessa vaiheessa:

1. Siirry paikalliseen työsaraan käyttäen ympäristömuuttujaa `$LOCAL_SCRATCH` ja pura tar-paketti:
   ```bash
   cd $LOCAL_SCRATCH
   tar xf /scratch/project_2001234/big_data.tar
   ```

2. Suorita analyysi. Tällä kertaa suoritamme `for`-silmukan, joka käyttää komentoa `transeq` kääntääkseen kaikki `big_data`-hakemistosta löytyvät fasta-tiedostot uusiksi proteiinisekvenssitiedostoiksi:
   ```bash
   for ffile in $(find ./ | grep fasta)
   do
       transeq ${ffile} ${ffile}.pep
   done 
   ```
   Tässä esimerkissä löydettiin noin 52 000 fasta-tiedostoa. Siten käsittelyn jälkeen `big_data`-hakemisto sisältää nyt 52 000 lisää pieniä tiedostoja. Varsinainen käännös on laskennallisesti kevyt tehtävä, joten suurin osa ajasta kuluu vain tiedostojen avaamiseen ja sulkemiseen (I/O).

3. Kun käsittely on päättynyt, tallennamme tulokset takaisin työsarakkaan uutena tar-tiedostona:
   ```bash
   tar cf /scratch/project_2001234/big_data.pep.tar ./
   ```
   Nyt tulokset ovat turvallisesti yhdessä tiedostossa työsarakassa, ja voimme poistua vuorovaikutteisesta istunnosta.

Sama analyysimenetelmä voitaisiin suorittaa myös työsarkahakemistossa. Se on kuitenkin hidasta ja saattaa heikentää jaetun tiedostojärjestelmän suorituskykyä kaikille käyttäjille. Näyttääksemme eron, alapuolella on suoritusaikavertailu yllä olevien kolmen vaiheen suorittamiseksi `$LOCAL_SCRATCH`- ja tavallisessa Lustre-pohjaisessa työsarkahakemistossa. `$LOCAL_SCRATCH`:n vasteajat ovat melko vakaita, mutta työsarkahakemistossa suoritusajat vaihtelevat paljon nykyisen Lustre-tiedostojärjestelmän kokonaiskuormituksen perusteella.

| Vaihe                   | `$LOCAL_SCRATCH` | `/scratch` |
|-------------------------|-----------------:|-----------:|
|1. Tar-tiedoston avaus   | 2m 8s            | 4m 12s     |
|2. Käsittely             | 9m 42s           | 21m 58s    |
|3. Uuden tar-tiedoston luonti | 2m 25s    | 42m 21s    |
|Yhteensä                 | 14m 15s          | 1h 8m 31s  |

[Lue lisää väliaikaisista paikallisista levyalueista](../../computing/disk.md#temporary-local-disk-areas).
