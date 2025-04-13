
# Tiedon tallennus koneoppimiseen {#data-storage-for-machine-learning}

Tämä opas selittää, kuinka tallentaa tietosi tehokkaasti koneoppimissovelluksia varten CSC:n supertietokoneilla. Se on osa meidän [Koneoppimisopasta](ml-guide.md).

## Minne tallentaa dataa? {#where-to-store-data}

CSC:n supertietokoneilta löytyy kolme erilaista jaettua levyaluetta: **home**, **projappl** ja **scratch**. Voit [lukea lisää levyalueista täältä](../../computing/disk.md). [LUMI-tietokoneelle löydät tietojen tallennusosion täältä](https://docs.lumi-supercomputer.eu/storage/).
Yleisesti, pidä koodi ja ohjelmistot **projappl**-alueella ja datat, lokit ja laskentatulokset **scratch**-alueella. **Home**-hakemistoa ei ole tarkoitettu tietojen analysointiin ja laskentaan, ja siellä pitäisi säilyttää vain pieniä henkilökohtaisia tiedostoja.

Lisäksi [LUMI:lla on jaettu **flash**-tallennusalue](https://docs.lumi-supercomputer.eu/storage/), joka on nopeampi päästä käsiksi kuin scratch. Flash on tarkoitettu vain väliaikaiseen tietojen tallentamiseen käsittelyä varten, ja [flash-alueella on korkeampi kustannus kuin normaalilla scratch-tallennuksella](https://docs.lumi-supercomputer.eu/runjobs/lumi_env/billing/#flash-storage-lumi-f-billing).

On suositeltavaa tallentaa suuria datakokonaisuuksia [Allas-objektivarastoon](../../data/Allas/index.md) ja ladata ne projektiisi scratch-hakemistoon ennen laskennan aloittamista. Esimerkiksi:

```bash
module load allas
allas-conf
cd /scratch/<your-project>
swift download <bucket-name> your-dataset.tar
```

Kaikki, mikä on säilytettävä pidemmän aikaa (projektin eliniän ajan), pitäisi kopioida takaisin Allas-palveluun. [Scratch-levyalue puhdistetaan säännöllisesti vanhoista tiedostoista](clean-up-data.md), eikä sitä pitäisi käyttää pitkäaikaisesti tärkeiden asioiden säilyttämiseen.

Jotkin CPU-solmut ja kaikki GPU-solmut Puhti- ja Mahti-supertietokoneilla (mutta *ei* LUMI:lla) sisältävät myös nopeat paikalliset NVMe-asemat, joiden kapasiteetti on vähintään 3,6 TB. Tämä tila on käytössä vain Slurm-jobin suorituksen aikana ja puhdistuu sen jälkeen. Tiedonintensiivisille töille on usein kannattavaa kopioida tiedot NVMe-asemalle työn alussa ja tallentaa lopulliset tulokset scratch-asemalle työn lopussa.
[Lue alta lisää, kuinka käyttää nopeaa paikallista NVMe-asemaa](#fast-local-drive-puhti-and-mahti-only).

## Jaetun tiedostojärjestelmän tehokas käyttö {#using-the-shared-file-system-efficiently}

Koneoppimismallien opetusdata koostuu usein valtavasta määrästä tiedostoja. Tyypillinen esimerkki on neuroverkon opettaminen kymmenillä tuhansilla suhteellisen pienillä JPEG-kuvatiedostoilla. Valitettavasti Lustre-tiedostojärjestelmä, jota käytetään `/scratch`-, `/projappl`- ja käyttäjien kotihakemistoissa, ei suoriudu hyvin satunnaispääsystä moniin tiedostoihin tai monien pienten lukujen suorittamisessa. Tämän lisäksi se voi hidastaa laskentaa ja äärimmäisissä tapauksissa **aiheuttaa huomattavia hidastuksia kaikille supertietokoneen käyttäjille, tehden koko supertietokoneen käyttökelvottomaksi tuntikausiksi**.

!!! huomio
    Ole hyvä ja **älä lue valtavasti tiedostoja jaetusta tiedostojärjestelmästä**. Käytä nopeita paikallisia asemia tai pakkaa datasi suuremmiksi tiedostoiksi sarjallista pääsyä varten sen sijaan!

Lisätietoa saat CSC:n
[Lustre-tiedostojärjestelmän teknisestä kuvauksesta](../../computing/lustre.md) ja yleisestä tutoriaalistamme
[miten saavutetaan parempi I/O-suorituskyky Lustre-ympäristössä](lustre_performance.md).

### Tehokkaampi tiedostoformaatti {#more-efficient-data-format}

Monet koneoppimisympäristöt tukevat formaatteja, jotka tekevät datan pakkaamisesta tehokkaampaa. Yleisiä formaatteja ovat [TensorFlow'n TFRecord][TFRecord] ja [WebDataset] PyTorchille. Muita esimerkkejä ovat [HDF5]- tai [LMDB]-formaatit, tai jopa yksinkertaiset ZIP-tiedostot, esimerkiksi Pythonin [zipfile]-kirjastoa käyttäen.

[LUMI AI opas][LUMI-AI-data] sisältää mukavan vertailun eri formaateista käytettäväksi PyTorchin kanssa. Katso myös [esimerkki TFRecord-tiedostojen luomisesta kuvatietokannasta][tfrecord-example].

Kaikkien näiden formaattien pääasiallinen tarkoitus on, että useiden tuhansien pienten tiedostojen sijaan sinulla on yksi tai muutamia isompia tiedostoja, jotka ovat paljon tehokkaampia käyttää ja lukea sarjallisesti. Älä epäröi [ottaa yhteyttä palvelupisteeseemme](../contact.md), jos tarvitset neuvoja tehokkaampaan datan pääsyyn.

[TFRecord]: https://www.tensorflow.org/tutorials/load_data/tfrecord
[WebDataset]: https://github.com/webdataset/webdataset
[HDF5]: https://docs.h5py.org/en/stable/
[LMDB]: https://en.wikipedia.org/wiki/Lightning_Memory-Mapped_Database
[zipfile]: https://docs.python.org/3/library/zipfile.html
[LUMI-AI-data]: https://github.com/Lumi-supercomputer/LUMI-AI-Guide/tree/main/3-file-formats#readme
[tfrecord-example]: https://github.com/CSCfi/machine-learning-scripts/blob/master/notebooks/tf2-pets-create-tfrecords.ipynb

### Nopea paikallinen asema (vain Puhti ja Mahti) {#fast-local-drive-puhti-and-mahti-only}

Jos todella tarvitset päästä käsiksi yksittäisiin pieniin tiedostoihin, voit hyödyntää nopeaa NVMe-paikallisasemaa, joka on käytössä GPU-solmuissa Puhdilla ja Mahtilla. Yksinkertaisesti lisää `nvme:<gigatavujen määrä>` `--gres`-lippuun lähetystiedostossasi, jonka jälkeen nopea paikallinen tallennus on käytettävissä sijainnissa, jonka ympäristömuuttuja `$LOCAL_SCRATCH` määrittää. Tässä on esimerkki ajosta, joka varaa 100 GB nopeaa paikallisasemaa ja purkaa datasetin tar-paketin tuolle asemalle ennen laskennan aloitusta:

```bash
#!/bin/bash
#SBATCH --account=<project>
#SBATCH --partition=gpu
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=10
#SBATCH --mem=64G
#SBATCH --time=1:00:00
#SBATCH --gres=gpu:v100:1,nvme:100

tar xf /scratch/<your-project>/your-dataset.tar -C $LOCAL_SCRATCH

srun python3 myprog.py --input_data=$LOCAL_SCRATCH <options>
```

Huomaa, että sinun täytyy välittää ohjelmallesi tieto siitä, mistä löytää datasetti, esimerkiksi komentoriviparametrilla. Katso myös meidän [yleiset ohjeet, kuinka hyödyntää nopeaa paikallista varastoa](../../computing/running/creating-job-scripts-puhti.md#local-storage).

Jos ajat [monen solmun työtä](ml-multi.md), sinun täytyy muuttaa `tar`-riviä niin, että se suoritetaan jokaisella solmulla erikseen:

```bash
srun --ntasks=$SLURM_NNODES --ntasks-per-node=1 \
    tar xf /scratch/<your-project>/your-dataset.tar -C $LOCAL_SCRATCH
```
```

