---
tags:
  - Academic
catalog:
  name: MATLAB
  description: High-level technical computing language
  description_fi: Korkean tason teknisen laskennan kieli
  license_type: Academic
  disciplines:
    - Mathematics and Statistics
  available_on:
    - web_interfaces:
        - LUMI
        - Puhti
    - LUMI
    - Puhti
---

# MATLAB { #matlab }
[MATLAB](https://mathworks.com/products/matlab.html) on korkean tason teknisen laskennan kieli ja interaktiivinen ympäristö algoritmien kehittämiseen, datan visualisointiin, data-analyysiin ja numeeriseen laskentaan.

[TOC]


## Lisenssi { #license }
MATLAB on proprietaarinen ohjelmisto.


## Saatavuus { #available }
### Puhti - Interaktiivinen MATLAB { #puhti-interactive-matlab }
Puhtissa on MATLAB-asennukset sekä interaktiivista käyttöä että eräajoja varten.
Interaktiivinen MATLAB on tarkoitettu tilapäiseen, kevyeen datan esi- ja jälkikäsittelyyn.
Saatavuus:

- Lisenssi: Akateeminen
- Versiot: R2023a:sta R2024b:hen
- Toolboxit: Parallel Computing Toolbox.
  Jokaista toolboxia on 2 lisenssiä.

### Puhti - MATLAB Parallel Server { #puhti-matlab-parallel-server }
MATLAB Parallel Server (MPS) mahdollistaa töiden lähettämisen eräajona paikallisesta MATLAB-asennuksesta Puhtiin.
Saatavuus:

- Lisenssi: Akateeminen
- Versiot: R2021a:sta R2025a:han
- Toolboxit: MATLAB Parallel Server.
  Lisenssi mahdollistaa enintään 500 laskentaydimen samanaikaisen käytön.
  Lisäksi paikallisessa MATLAB-lisenssissäsi olevia toolboxeja voidaan käyttää MATLAB Parallel Serverin kanssa.

Akateeminen lisenssi sallii käytön vain suomalaisten korkeakoulujen henkilökunnalle ja opiskelijoille.
Jos olet käyttäjä kaupallisesta yrityksestä tai suomalaisesta tutkimuslaitoksesta, ole hyvä ja [ota yhteyttä CSC Service Deskiin](../support/contact.md) jatko-ohjeita varten.

### LUMI - Interaktiivinen MATLAB { #lumi-interactive-matlab }
LUMIssa on MATLAB-asennus interaktiiviseen käyttöön.

- Lisenssi: Akateeminen
- Versiot: R2023b:stä R2024a:han
- Toolboxit: Simulink, Control System Toolbox, Curve Fitting Toolbox, Deep Learning Toolbox, Global Optimization Toolbox, Image Processing Toolbox, Optimization Toolbox, Parallel Computing Toolbox, Signal Processing Toolbox, Statistics and Machine Learning Toolbox, Wavelet Toolbox.
  Jokaista toolboxia on 25 lisenssiä.

Akateeminen lisenssi sallii käytön vain opetukseen ja akateemiseen tutkimukseen tutkinnon myöntävässä oppilaitoksessa.


## Interaktiivisen MATLABin käyttö Puhtissa ja LUMIssa { #using-interactive-matlab-on-puhti-and-lumi }
### Kommentorivikäyttöliittymä { #command-line-interface }
Voimme ajaa interaktiivisen MATLAB-istunnon komentoriviltä.
Ensin pitää tehdä varaus Slurmin avulla:

```bash
srun --account=project_id --partition=small --time=0:15:00 --cpus-per-task=1 --mem-per-cpu=4g --pty bash
```

Korvaa `project_id` oman projektisi tunnisteella, muuten komento epäonnistuu.

=== "Puhti"

    Tämän jälkeen ladataan MATLAB-moduuli:

    ```bash
    module load matlab
    ```

=== "LUMI"

    LUMIssa moduulitiedostot täytyy lisätä CSC:n paikallisesta hakemistosta moduulipolulle ennen moduulin lataamista.

    ```bash
    module use /appl/local/csc/modulefiles
    module load matlab
    ```

Nyt `matlab`-, `mbuild`-, `mex`- ja `mcc`-komennot ovat käytettävissä.
Esimerkiksi MATLABin komentorivikäyttöliittymän voi avata näin:

```bash
matlab -nodisplay
```

MATLAB-skriptejä voi ajaa myös eräajona seuraavasti:

```bash
matlab -batch <script>
```


### Web-käyttöliittymä { #web-interface }
Voimme käyttää myös [web-käyttöliittymää](../computing/webinterface/index.md) interaktiivisiin MATLAB-istuntoihin.
Kirjaudu ensin sisään osoitteeseen [www.puhti.csc.fi](https://www.puhti.csc.fi) tai [www.lumi.csc.fi](https://www.lumi.csc.fi).
Sen jälkeen on kaksi vaihtoehtoa:

1. Voimme käyttää **MATLAB web application** -palvelua, joka avaa MATLABin graafisen käyttöliittymän selainversion.

2. Voimme käyttää **Desktop application** -palvelua ja klikata MATLAB-kuvaketta avataksemme MATLABin graafisen käyttöliittymän työpöytäversion.

_LUMIn Desktop Applicationissa MATLAB löytyy vasemman alakulman valikkopainikkeen kautta. Hae “matlab” ja klikkaa kuvaketta / raahaa se työpöydälle löytääksesi sen jatkossa helposti._

MATLAB-sovellusta käynnistettäessä on varattava vähintään 4 Gt muistia.


## Rinnakkaislaskenta MATLABissa { #parallel-computing-on-matlab }
MATLABissa koodia voi rinnakkaistaa [Parallel Computing Toolbox](https://mathworks.com/help/parallel-computing/index.html) -toolboxin korkean tason rakenteilla.
Tarkastellaan seuraavaa sarjallista koodia tiedostossa `funcSerial.m`, joka pysäyttää suorituksen sekunniksi `n` kertaa ja mittaa suoritusajan:

```matlab
function t = funcSerial(n)
t0 = tic;
for idx = 1:n
    pause(1);
end
t = toc(t0);
end
```

Seuraavan sarja-ajon pitäisi kestää noin kaksi sekuntia:

```matlab
funcSerial(2)
```

Funktion voi rinnakkaistaa käyttämällä rinnakkaista for-silmukkaa, `parfor`, tiedostossa `funcParallel.m` seuraavasti:

```matlab
function t = funcParallel(n)
t0 = tic;
parfor idx = 1:n
    pause(1);
end
t = toc(t0);
end
```

Rinnakkaiskoodin ajamiseksi pitää luoda rinnakkaisallas prosesseilla tai säikeillä ja sen jälkeen ajaa rinnakkaiskoodi.
Voimme luoda rinnakkaisaltaan kahdella prosessilla ja ajaa rinnakkaiskoodin samalla parametrilla kuin sarjallinen versio, mutta sen pitäisi kestää noin sekunnin:

```matlab
pool = parpool('Processes', 2);
funcParallel(2)
delete(pool);
```

Sama säikeisiin perustuvalla poolilla:

```matlab
pool = parpool('Threads', 2);
funcParallel(2)
delete(pool);
```

MATLAB Parallel Serverin avulla voimme myös luoda rinnakkaisaltaita Puhtiin ja ajaa rinnakkaiskoodia siellä.

<!-- TODO: Constructs for using GPUs are also available. -->


## Työn lähettäminen paikallisesta MATLABista Puhtiin MATLAB Parallel Serverin avulla { #submitting-work-from-local-matlab-to-puhti-using-matlab-parallel-server }
### MPS:n määrittäminen paikallisessa MATLABissa { #configuring-mps-on-local-matlab }
Puhtin MATLAB Parallel Server (MPS) mahdollistaa erätöiden lähettämisen paikallisesta MATLAB-istunnosta Puhti-klusteriin.
Puhti MPS:n käyttö edellyttää paikallista MATLAB-asennusta, tuettua MATLAB-versiota ja Parallel Computing Toolboxia sekä pääsyä Puhti-klusteriin.
MPS voidaan määrittää paikalliselle koneelle seuraavasti.

1. Kirjaudu SSH-asiakkaalla Puhtiin ja ulos varmistaaksesi, että sinulle on luotu kotihakemisto.
2. Lataa Puhtia varten konfiguraatioskriptiarkisto [**mps_puhti.zip**](https://github.com/CSCfi/csc-env-matlab/raw/refs/heads/main/config/mps_puhti.zip).
3. Luo paikallinen MATLAB-asetushakemisto.
4. Pura asetukset asetushakemistoon.
5. Lisää purettujen asetustiedostojen hakemisto MATLABin polkuun MATLABissa funktioilla `addpath` ja `savepath`.
6. Määritä MATLAB lähettämään työt Puhtiin kutsumalla MATLABissa `configCluster` ja syötä käyttäjätunnuksesi kehotteeseen.


#### Linux ja macOS { #linux-and-macos }
Vaihe 1: Aja shellissä:

```bash
ssh <username>@puhti.csc.fi exit
```

Vaihe 2: Aja shellissä:

```bash
curl --location --output "$HOME/Downloads/mps_puhti.zip" https://github.com/CSCfi/csc-env-matlab/raw/refs/heads/main/config/mps_puhti.zip
```

Vaihe 3: Aja shellissä:

```bash
mkdir -p "$HOME/.matlab"
```

Vaihe 4: Aja shellissä:
```bash
unzip "$HOME/Downloads/mps_puhti.zip" -d "$HOME/.matlab/mps_puhti"
```

Vaihe 5: Aja MATLABissa:
```matlab
addpath(fullfile(getenv("HOME"), ".matlab", "mps_puhti"))
savepath
```

Vaihe 6: Aja MATLABissa:
```matlab
configCluster
```

#### Windows { #windows }
Vaihe 1: Aja Windows PowerShellissä:

```bash
ssh <username>@puhti.csc.fi exit
```

Vaihe 2: Aja Windows PowerShellissä:

```powershell
Invoke-Request -Uri "https://github.com/CSCfi/csc-env-matlab/raw/refs/heads/main/config/mps_puhti.zip" -OutFile "$env:USERPROFILE\Downloads\mps_puhti.zip"
```

Vaihe 3: Aja Windows PowerShellissä:

```powershell
New-Item -Path "$env:APPDATA\Mathworks\MATLAB" -ItemType Directory -Force 
```

Vaihe 4: Aja Windows PowerShellissä:
```powershell
Expand-Archive -Path "$env:USERPROFILE\Downloads\mps_puhti.zip" -DestinationPath "$env:APPDATA\Mathworks\MATLAB\mps_puhti"
```

Vaihe 5: Aja MATLABissa:
```matlab
addpath(fullfile(getenv("APPDATA"), "Mathworks", "MATLAB", "mps_puhti"))
savepath
```

Vaihe 6: Aja MATLABissa:
```matlab
configCluster
```


### Yksi- ja monisäikeisten töiden lähettäminen { #submitting-single-and-multithreaded-jobs }
Ennen erätyön lähettämistä resurssivaraus pitää määrittää `parcluster`-komennolla.
Koska `parcluster` on tilallinen, on turvallisinta nollata käyttämättömät ominaisuudet asettamalla ne tyhjäksi merkkijonoksi `''`.
Lisäksi `CPUsPerNode` asetetaan automaattisesti `batch`-komennolla, joten tyhjennämme sen.
Esimerkiksi yksinkertainen CPU-varaus näyttää tältä:

```matlab
c = parcluster;
% Replace 'project_id' to your project identifier, otherwise the script will fail.
c.AdditionalProperties.ComputingProject = 'project_id';
c.AdditionalProperties.Partition = 'small';
c.AdditionalProperties.WallTime = '00:15:00';
c.AdditionalProperties.CPUsPerNode = '';
c.AdditionalProperties.MemPerCPU = '4g';
c.AdditionalProperties.GpuCard = '';
c.AdditionalProperties.GPUsPerNode = '';
c.AdditionalProperties.EmailAddress = '';
% You can reserve multiple threads by increasing the NumThreads value.
c.NumThreads = 1;
```

Nyt voimme käyttää [`batch`](http://se.mathworks.com/help/distcomp/batch.html)-funktiota työn lähettämiseen Puhtiin.
Se palauttaa job-olion, jonka avulla voimme lukea lähetetyn työn tuottaman ulostulon.

Ensimmäisen lähetyksen yhteydessä MATLAB pyytää valitsemaan salasanalla tai SSH-avaimella tunnistautumisen.
Salasanatunnistautumista ei enää tueta Puhtissa, joten valitse SSH-avaintunnistautuminen.
Anna polku yksityiseen avaimeesi ja syötä mahdollinen salalause.
MATLAB tallentaa avaimen polun eikä kysy sitä uudestaan myöhemmissä istunnoissa.

Voimme lähettää yksinkertaisen testityön, joka palauttaa nykyisen työskentelyhakemiston, seuraavasti:

```matlab
j = batch(c, @pwd, 1, {}, 'CurrentFolder', '.', 'AutoAddClientPath', false)
```

Esimerkissä asetamme työskentelyhakemiston kotihakemistoon asettamalla `'CurrentFolder'` arvoon `'.'`.
Lisäksi kannattaa estää MATLABia lisäämästä paikallista MATLAB-hakupolkua etätyöntekijöille asettamalla `'AutoAddClientPath'` arvoon `false`.


### GPU-töiden lähettäminen { #submitting-gpu-jobs }
GPU-varaus luodaan asettamalla `Partition`-, `GpuCard`- ja `GPUsPerNode`-ominaisuudet sopiviksi.
Esimerkiksi yhden GPU:n varaus näyttää tältä:

```matlab
c = parcluster;
% Replace 'project_id' to your project identifier, otherwise the script will fail.
c.AdditionalProperties.ComputingProject = 'project_id';
c.AdditionalProperties.Partition = 'gpu';
c.AdditionalProperties.WallTime = '00:15:00';
c.AdditionalProperties.CPUsPerNode = 1;
c.AdditionalProperties.MemPerCPU = '4g';
c.AdditionalProperties.GpuCard = 'v100';
c.AdditionalProperties.GPUsPerNode = 1;
c.AdditionalProperties.EmailAddress = '';
% You can reserve multiple threads by increasing the NumThreads value.
c.NumThreads = 10;
```

Nyt voimme lähettää yksinkertaisen GPU-työn, joka kysyy käytettävissä olevan GPU-laitteen, seuraavasti:

```matlab
j = batch(c, @gpuDevice, 1, {}, 'CurrentFolder', '.', 'AutoAddClientPath', false)
```


### Rinnakkaisaltaan lähettäminen { #submitting-parallel-pool }
Luodaan varaus:

```matlab
c = parcluster;
% Replace 'project_id' to your project identifier, otherwise the script will fail.
c.AdditionalProperties.ComputingProject = 'project_id';
c.AdditionalProperties.Partition = 'small';
c.AdditionalProperties.WallTime = '00:15:00';
c.AdditionalProperties.CPUsPerNode = '';
c.AdditionalProperties.MemPerCPU = '4g';
c.AdditionalProperties.GpuCard = '';
c.AdditionalProperties.GPUsPerNode = '';
c.AdditionalProperties.EmailAddress = '';
% You can reserve multiple threads per worker by increasing the NumThreads value.
c.NumThreads = 1;
```

Nyt voimme käyttää batch-komentoa rinnakkaisaltaan luomiseen asettamalla `'Pool'`-argumenttiin varattavien ytimien määrän.
Esimerkiksi rinnakkaistyön voi lähettää kahdeksalle ytimelle näin:

```matlab
j = batch(c, @funcParallel, 1, {8}, 'Pool', 8, 'CurrentFolder', '.', 'AutoAddClientPath', false)
```

Huomaa, että rinnakkaisallas pyytää aina yhden lisä-CPU-ytimen erätyön ja allasytimien hallintaan.
Esimerkiksi kahdeksan ydintä tarvitseva työ kuluttaa yhdeksän CPU-ydintä.


### Töiden ja tulosteiden kysely { #querying-jobs-and-output }
Käynnissä olevien tai valmistuneiden töiden listan saa komennolla

```matlab
c = parcluster;
c.Jobs
```

Hae viite työhön, jonka järjestysnumero on 1

```matlab
j = c.Jobs(1);
```

Kun meillä on viite klusteriin, etsitään työ annettua ID:tä käyttäen `findJob`-metodilla; alla esimerkissä `ID = 11`.

```matlab
j = findJob(c, 'ID', 11);
```

Kun työ on valmistunut, funktion ulostulot voi hakea näin:

```matlab
fetchOutputs(j)
```

Klusterin tiedostoihin kirjoitettu data on noudettava suoraan tiedostojärjestelmästä.


<!--
Once we've identified the job we want, we can retrieve the results as we've done previously.
If the job has produced an error, we can call the `getDebugLog` method to view the error log file.
The error log can be lengthy and is not shown here.

As an example, we will retrieve the debug log of the serial job.

```matlab
getDebugLog(j.Parent, j.Tasks(1))
```

For debugging, retrieve the log file.

```matlab
getDebugLog(j.Parent ,j)
```
-->


<!--
### Checking license status
You can check the status of MPS licenses on Puhti after logging in with `scontrol` command.

```bash
scontrol show lic=mdcs
```

```text
LicenseName=mdcs
    Total=500 Used=320 Free=180 Remote=no
```
-->