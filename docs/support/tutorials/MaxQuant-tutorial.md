
# MaxQuant-ohjelmiston käyttäminen Puhti-superkoneella {#running-maxquant-software-on-puhti-supercomputer}

[MaxQuant](https://maxquant.org/) on kvantitatiivinen proteomiikkasovelluspaketti, joka on suunniteltu suurten massaspektrometristen tietojoukkojen analysointiin. Suorituskykyinen laskentaympäristö, kuten Puhti, soveltuu laskentaintensiivisten tehtävien suorittamiseen MaxQuant-ohjelmiston avulla proteomiikan tutkimuksessa.

MaxQuant on ilmainen käyttää, mutta jokaisen käyttäjän on rekisteröidyttävä ja ladattava MaxQuant itse [kehittäjän sivustolta](https://maxquant.org/download_asset/maxquant/latest).

Tässä ohjeessa annetaan ohjeet MaxQuant-ohjelmiston suorittamiseen Puhtilla.

## Parametritiedoston konfigurointi {#configure-parameter-file}

Vaikka aiot suorittaa MaxQuant-putkiston Puhtilla, sinun on ensin konfiguroitava MaxQuant-työsi eri parametrit paikallisella Windows-koneellasi. Sen jälkeen lataa parametridata (eli `mqpar.xml`), raakatiedsätä (esim. .raw tiedostot) ja sekvenssitiedosto (eli .fasta tiedosto) Puhti-laskentaympäristöön.

## XML-konfigurointitiedoston muokkaaminen {#edit-xml-configuration-file}

Sinun on tehtävä joitain muutoksia parametridataasi (`mqpar.xml`), joka esimerkiksi luotiin paikallisella Windows-koneella, jotta se olisi yhteensopiva HPC-ympäristön kanssa.

Näihin muutoksiin kuuluu:

- Windows-polkujen muuttaminen linux-polkuiksi näytetiedostoille (vinkki: etsi `<filePaths>` XML-tiedostosta)
- Windows-polun muuttaminen linux-poluksi fasta-sekvenssitiedostolle (vinkki: etsi `<fastaFilePath>` XML-tiedostosta)
- Säikeiden lukumäärä näytteiden määrän mukaan (vinkki: etsi `<numThreads>` XML-tiedostosta)

## Lähettäminen erätyöksi Puhti-keskuksessa {#submit-as-a-batch-job-to-puhti-cluster}

- Kirjaudu ensin Puhti-koneeseen (katso ohjeet [täältä](../../computing/connecting/index.md))

- Vaihda projektihakemistoon Puhtilla ja kopioi syötetiedostosi sinne ([vinkkejä tiedostonsiirrosta](../../data/moving/index.md)).

  Tämä on projektihakemistosi (scratchissa), jossa .xml-tiedostosi, .fasta-tiedostosi ja raakatiedostosi sijaitsevat

- Opi ottamaan käyttöön MaxQuant-ympäristö

MaxQuant-ohjelmisto tarvitsee myös mono-ohjelmiston toimiakseen. Mono-ohjelmistolla voit valita MaxQuant-versiosi. CSC tarjoaa modulin mono:lle.

```text
module load mono/5.14
```

Lataa linux-yhteensopiva versiosi MaxQuantista (esim. v2.0.3.0) scratch-hakemistoosi Puhtilla ja suorita seuraava varmistaaksesi, että MaxQuant on asennettu oikein:

```text
mono MaxQuant\ 2.0.3.0/bin/MaxQuantCmd.exe --help
```

Huomaa, että hakemiston nimi sisältää välilyönnin, joten sinun on joko käytettävä kenoviivaa (\) tai ympäröitävä polku lainausmerkeillä. Helppouden vuoksi saatat haluta nimetä hakemiston niin, että siinä on esim. alaviiva välilyönnin sijasta.

!!! Huomio 
    Huomaa, että MaxQuant-versio, jota käytit .xml-parametrikonfiguraatiotiedoston luomiseen, on vastattava sitä versiota, jota käytät Linux-ympäristössä, jotta se sujuu kyseisessä klusteriympäristössä. Muut uusimmat versiot voivat toimia.

- Lähetä lopuksi skriptisi

Luo erätyöskripti [jaetun muistin töiden ohjeiden mukaisesti](../../computing/running/creating-job-scripts-puhti.md#serial-and-shared-memory-batch-jobs) ja varmista, että skripti päätyy samaan hakemistoon kuin missä `mqpar.xml`- ja muut tietotiedostosi sijaitsevat.

Helpottaaksesi erätyöskriptin kirjoittamista, voit käyttää seuraavaa vähimmäisesimerkkiskriptiä (kutsutaan esim. `maxquant.sh`), alustana:

```bash
#!/bin/bash
#SBATCH --job-name=maxquant
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
#SBATCH --account=project_xxx
#SBATCH --time=01:20:00
#SBATCH --ntasks=1
#SBATCH --partition=small
#SBATCH --cpus-per-task=6
#SBATCH --mem=16000

# lataa maxquant-ympäristö

module load mono/5.14

# säädä tiedostopolut täällä

mono /path_of_MaxQuant/bin/MaxQuantCmd.exe /path/MaxQuant/mqpar.xml

```

ja muuta sitten resurssivarauksia näytteiden määrän mukaan. Lähetä skriptisi alla:

```bash
sbatch maxquant.sh
```

Kun `maxquant`-tehtävä on valmis, tulostiedostosi ovat tässä samassa hakemistossa.

## Tutorista esimerkki {#tutorial-example}

Voit ladata esimerkkejä tutorista aineistosta MaxQuant-käyttöön alla:

```bash
wget https://a3s.fi/proteomics/MaxQuant_tutorial.tar.gz
```

ja pura sitten ladattu arkistotiedosto alla:

```bash
tar -xavf MaxQuant_tutorial.tar.gz
```

Opastus sisältää esimerkkiraakatiestoiminnan ja muut tarvittavat tiedostot MaxQuantin ajamiseen testattavaksi.

## Tarkista käytetyt resurssit, kun tehtäväsi on valmis {#look-at-the-used-resources-once-your-job-is-finished}

Kun `maxquant`-tehtävä on valmis, voit tarkistaa tietojenkäsittelyresurssien käytön, kuten [muistin](../faq/how-much-memory-my-job-needs.md) ja CPU:n käytön tehokkuuden. Tämä auttaa sinua hienosäätämään paremmin parametreja tehokasta tietojenkäsittelyresurssien käyttöä varten.

Voit käyttää seuraavia komentoja työnumeron avulla:

```
seff <jobid>
sacct –l –j <jobid>
sacct -o jobid,jobname,maxrss,maxvmsize,state,elapsed -j <jobid>
```
