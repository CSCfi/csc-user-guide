
---
tags:
  - Academic
system:
  - www-puhti
  - www-lumi
---

# MATLAB
[MATLAB](https://mathworks.com/products/matlab.html) on korkean tason tekninen laskentakieli ja interaktiivinen ympäristö algoritmien kehittämiseen, tiedon visualisointiin, tiedon analysointiin ja numeeriseen laskentaan.

[TOC]


## Lisenssi {#license}
MATLAB on suljettu ohjelmisto.


## Saatavilla {#available}
### Puhti - Interaktiivinen MATLAB {#puhti-interactive-matlab}
Puhtissa on MATLAB-asennuksia interaktiiviseen käyttöön ja eräajotöihin.
Interaktiivinen MATLAB on tarkoitettu väliaikaiseen, kevyeseen datan esikäsittelyyn ja jälkikäsittelyyn.
Se on saatavilla seuraavasti:

- Lisenssi: Akateeminen
- Versiot: R2023a:sta R2024b:hen
- Työkalupakit: Parallel Computing Toolbox.
  Käytössä on 2 lisenssiä jokaista työkalupakkia kohden.

### Puhti - MATLAB Parallel Server {#puhti-matlab-parallel-server}
MATLAB Parallel Server (MPS) mahdollistaa työn lähettämisen eräajotyönä paikallisesta MATLAB-asennuksesta Puhtiin.
Se on saatavilla seuraavasti:

- Lisenssi: Akateeminen
- Versiot: R2021a:sta R2024b:hen
- Työkalupakit: MATLAB Parallel Server.
  Käytössä on lisenssi enintään 500 laskentaytimen samanaikaiseen käyttöön.
  Lisäksi työkalupakkeja, joihin sinulla on lisenssi paikallisella MATLAB-lisenssilläsi, voidaan käyttää MATLAB Parallel Serverin kanssa.

Akateeminen lisenssi sallii käytön vain suomalaisten korkeakoulujen henkilökunnalle ja opiskelijoille.
Jos olet kaupallisen yrityksen tai suomalaisen tutkimuslaitoksen käyttäjä, pyydä [CSC:n asiakaspalvelua](../support/contact.md) ohjeiden saamiseksi.

### LUMI - Interaktiivinen MATLAB {#lumi-interactive-matlab}
LUMI:ssa on MATLAB-asennus interaktiiviseen käyttöön.

- Lisenssi: Akateeminen
- Versiot: R2023b:stä R2024a:han
- Työkalupakit: Simulink, Control System Toolbox, Curve Fitting Toolbox, Deep Learning Toolbox, Global Optimization Toolbox, Image Processing Toolbox, Optimization Toolbox, Parallel Computing Toolbox, Signal Processing Toolbox, Statistics and Machine Learning Toolbox, Wavelet Toolbox.
  Käytössä on 25 lisenssiä jokaista työkalupakkia kohden.

Akateeminen lisenssi sallii käytön vain opetus- ja tutkimuskäyttöön tutkintoa myöntävässä oppilaitoksessa.


## Interaktiivisen MATLABin käyttäminen Puhtilla ja LUMIlla {#using-interactive-matlab-on-puhti-and-lumi}
### Komentoriviliittymä {#command-line-interface}
Voimme suorittaa interaktiivisen MATLAB-istunnon komentoriviltä.
Aluksi meidän on tehtävä varaus käyttämällä Slurmia:

```bash
srun --account=project_id --partition=small --time=0:15:00 --cpus-per-task=1 --mem-per-cpu=4g --pty bash
```

Korvaa `project_id` projektitunnisteellasi, muuten skripti epäonnistuu.

=== "Puhti"

    Tämän jälkeen meidän on ladattava MATLAB-moduuli:

    ```bash
    module load matlab
    ```

=== "LUMI"

    LUMI:lla meidän on lisättävä moduulitiedostot CSC:n paikallisesta hakemistosta moduulipolulle ennen moduulin lataamista.

    ```bash
    module use /appl/local/csc/modulefiles
    module load matlab
    ```

Nyt `matlab`, `mbuild`, `mex` ja `mcc` komennot ovat käytettävissä.
Esimerkiksi, voimme avata MATLAB-komentoriviliittymän seuraavasti:

```bash
matlab -nodisplay
```

Voimme myös suorittaa MATLAB-skriptejä erätilassa seuraavasti:

```bash
matlab -batch <script>
```


### Web-käyttöliittymä {#web-interface}
Voimme myös käyttää [web-käyttöliittymää](../computing/webinterface/index.md) interaktiivisiin MATLAB-istuntoihin.
Ensinnäkin, meidän on kirjauduttava sisään [www.puhti.csc.fi](https://www.puhti.csc.fi) tai [www.lumi.csc.fi](https://www.lumi.csc.fi).
Tämän jälkeen meillä on kaksi vaihtoehtoa:

1. Voimme käyttää **MATLAB web -sovellusta**, joka avaa MATLAB-graafisen käyttöliittymän web-version.

2. Voimme käyttää **Työpöytäsovellusta** ja klikata MATLAB-ikonia avataksesi MATLAB-graafisen käyttöliittymän työpöytäversion.

_LUMI-työpöytäsovelluksessa Matlab löytyy vasemman alakulman valikkopainikkeen kautta. Etsi yksinkertaisesti matlab ja klikkaa kuvaketta / raahaa se työpöydälle löytääksesi sen helposti uudelleen._

Meidän on asetettava vähintään 4 GB muistia ennen MATLAB-sovelluksen käynnistämistä.


## Rinnakkaislaskenta MATLABissa {#parallel-computing-on-matlab}
MATLABissa voimme rinnakkaistaa koodia korkeatasoisilla [Parallel Computing Toolbox](https://mathworks.com/help/parallel-computing/index.html) -rakenteilla.
Harkitse seuraavaa sarjallista koodia, joka on kirjoitettu `funcSerial.m`-tiedostoon ja joka pysähtyy sekunniksi `n` kertaa ja mittaa suoritusajan:

```matlab
function t = funcSerial(n)
t0 = tic;
for idx = 1:n
    pause(1);
end
t = toc(t0);
end
```

Seuraavan sarjallisen suorituksen pitäisi kestää noin kaksi sekuntia:

```matlab
funcSerial(2)
```

Voimme rinnakkaista funktiota käyttämällä rinnakkaista for-silmukkarakennetta, `parfor`, joka on kirjoitettu `funcParallel.m`-tiedostoon seuraavasti:

```matlab
function t = funcParallel(n)
t0 = tic;
parfor idx = 1:n
    pause(1);
end
t = toc(t0);
end
```

Rinnakkaiskoodin suorittamiseksi meidän on luotava rinnakkaisallas prosesseista tai säikeistä ja sitten suoritettava rinnakkaiskoodi.
Voimme luoda rinnakkaisaltaan kahdella prosessilla ja suorittaa rinnakkaiskoodia samalla argumentilla kuin sarjallinen, mutta sen pitäisi kestää vain noin sekunti:

```matlab
pool = parpool('Processes', 2);
funcParallel(2)
delete(pool);
```

Sama säikeillä varustetulla rinnakkaisaltaalla:

```matlab
pool = parpool('Threads', 2);
funcParallel(2)
delete(pool);
```

MATLAB Parallel Serverilla voimme myös luoda rinnakkaisaltaita Puhtiin ja suorittaa rinnakkaiskoodia siellä.

<!-- TODO: Rakenteita myös GPU:iden käyttöön on saatavilla. -->


## Työn lähettäminen paikallisesta MATLABista Puhtiin MATLAB Parallel Serverin avulla {#submitting-work-from-local-matlab-to-puhti-using-matlab-parallel-server}
### MPS:n konfigurointi paikallisessa MATLABissa {#configuring-mps-on-local-matlab}
Puhtin MATLAB Parallel Server (MPS) mahdollistaa käyttäjille eräajotöiden lähettämisen paikallisesta MATLAB-istunnosta Puhti-klusteriin.
Puhtin MPS:n käyttö edellyttää paikallista MATLAB-asennusta tuetulla MATLAB-versiolla ja Parallel Computing Toolboxilla sekä pääsyä Puhti-klusteriin.
Voimme konfiguroida MPS:n paikallisessa tietokoneessa seuraavilla ohjeilla.

1. Kirjaudu ulos ja sisään Puhtiin SSH-asiakasohjelman kautta varmistaaksesi, että sinulla on kotihakemisto.
2. Lataa konfiguraatioskriptin arkisto [**mps_puhti.zip**](https://github.com/CSCfi/csc-env-matlab/raw/refs/heads/main/config/mps_puhti.zip) Puhtille.
3. Luo paikallinen MATLAB-konfiguraatiohakemisto.
4. Pura konfiguraatiot konfiguraatiohakemistoon.
5. Lisää hakemisto purettuihin konfiguraatiotiedostoihin MATLABin polkuun käyttämällä `addpath` ja `savepath` funktioita MATLABissa.
6. Määritä MATLABisi lähettämään töitä Puhtiin kutsumalla `configCluster` MATLABissa ja anna käyttäjätunnuksesi kehotteeseen.


#### Linux ja MacOS {#linux-and-macos}
Vaihe 1: Suorita komentorivillä:

```bash
ssh <username>@puhti.csc.fi exit
```

Vaihe 2: Suorita komentorivillä:

```bash
curl --location --output "$HOME/Downloads/mps_puhti.zip" https://github.com/CSCfi/csc-env-matlab/raw/refs/heads/main/config/mps_puhti.zip
```

Vaihe 3: Suorita komentorivillä:

```bash
mkdir -p "$HOME/.matlab"
```

Vaihe 4: Suorita komentorivillä:
```bash
unzip "$HOME/Downloads/mps_puhti.zip" -d "$HOME/.matlab/mps_puhti"
```

Vaihe 5: Suorita MATLABissa:
```matlab
addpath(fullfile(getenv("HOME"), ".matlab", "mps_puhti"))
savepath
```

Vaihe 6: Suorita MATLABissa:
```matlab
configCluster
```

#### Windows {#windows}
Vaihe 1: Suorita Windows Powershellissä:

```bash
ssh <username>@puhti.csc.fi exit
```

Vaihe 2: Suorita Windows Powershellissä:

```powershell
Invoke-WebRequest -Uri "https://github.com/CSCfi/csc-env-matlab/raw/refs/heads/main/config/mps_puhti.zip" -OutFile "$env:USERPROFILE\Downloads\mps_puhti.zip"
```

Vaihe 3: Suorita Windows Powershellissä:

```powershell
New-Item -Path "$env:APPDATA\Mathworks\MATLAB" -ItemType Directory -Force 
```

Vaihe 4: Suorita Windows Powershellissä:
```powershell
Expand-Archive -Path "$env:USERPROFILE\Downloads\mps_puhti.zip" -DestinationPath "$env:APPDATA\Mathworks\MATLAB\mps_puhti"
```

Vaihe 5: Suorita MATLABissa:
```matlab
addpath(fullfile(getenv("APPDATA"), "Mathworks", "MATLAB", "mps_puhti"))
savepath
```

Vaihe 6: Suorita MATLABissa:
```matlab
configCluster
```


### Sarjatöiden lähettäminen {#submitting-serial-jobs}
Ennen eräajotyön lähettämistä meidän on määritettävä resurssivaraus käyttämällä `parcluster`.
Koska `parcluster` on tilallinen, on turvallisinta tyhjentää eksplisiittisesti käyttämättömät ominaisuudet asettamalla ne tyhjäksi `'`.
Lisäksi `CPUsPerNode` asetetaan automaattisesti `batch`-komennolla, joten me tyhjennämme sen.
Esimerkiksi, yksinkertainen CPU-varaus näyttää seuraavalta:

```matlab
c = parcluster;
% Korvaa 'project_id' projektitunnisteellasi, muuten skripti epäonnistuu.
c.AdditionalProperties.ComputingProject = 'project_id';
c.AdditionalProperties.Partition = 'small';
c.AdditionalProperties.WallTime = '00:15:00';
c.AdditionalProperties.CPUsPerNode = '';
c.AdditionalProperties.MemPerCPU = '4g';
c.AdditionalProperties.GpuCard = '';
c.AdditionalProperties.GPUsPerNode = '';
c.AdditionalProperties.EmailAddress = '';
```

Nyt voimme käyttää [`batch`](http://se.mathworks.com/help/distcomp/batch.html) -funktiota lähettääksemme työn Puhtiin.
Se palauttaa työobjektin, jota voimme käyttää lähetetyn työn tulosten tarkasteluun.

Kun lähetät työn ensimmäisen kerran, MATLAB kehottaa sinua valitsemaan salasana- tai SSH-avainautentikoinnin välillä.
Salasanasautentikointia ei enää tueta Puhtissa, joten sinun on valittava SSH-avainautentikointi.
Anna polku yksityiseen avainavaimeesi ja syötä yksityiselle avaimelle oleva salasana, jos sellainen on.
MATLAB tallentaa avainavaimesi polun eikä pyydä sitä uudelleen tulevissa istunnoissa.

Voimme lähettää yksinkertaisen testityön, joka palauttaa nykyisen työhakemiston seuraavasti:

```matlab
j = batch(c, @pwd, 1, {}, 'CurrentFolder', '.', 'AutoAddClientPath', false)
```

Esimerkissä asetamme työhakemistoksi kotihakemiston asettamalla `'CurrentFolder'` arvoksi `'.'`.
Lisäksi meidän tulisi poistaa MATLABin paikallinen hakupolku käytöstä etätyöntekijöillä asettamalla `'AutoAddClientPath'` arvoksi `false`.


### Rinnakkaistöiden lähettäminen {#submitting-parallel-jobs}
Tehdään varaus:

```matlab
c = parcluster;
% Korvaa 'project_id' projektitunnisteellasi, muuten skripti epäonnistuu.
c.AdditionalProperties.ComputingProject = 'project_id';
c.AdditionalProperties.Partition = 'small';
c.AdditionalProperties.WallTime = '00:15:00';
c.AdditionalProperties.CPUsPerNode = '';
c.AdditionalProperties.MemPerCPU = '4g';
c.AdditionalProperties.GpuCard = '';
c.AdditionalProperties.GPUsPerNode = '';
c.AdditionalProperties.EmailAddress = '';
```

Nyt voimme käyttää batch-komentoa luodaksemme rinnakkaisaltaan työntekijöille asettamalla `'Pool'`-parametriksi varattavien ytimen määrä.
Esimerkiksi, voimme lähettää rinnakkaistyön kahdeksalle ytimelle seuraavasti:

```matlab
j = batch(c, @funcParallel, 1, {8}, 'Pool', 8, 'CurrentFolder', '.', 'AutoAddClientPath', false)
```

Huomaa, että rinnakkaisallas pyytää aina yhden lisä-CPU-ytimen hallitakseen eräajotyötä ja ydinpoolia.
Esimerkiksi, työ, joka tarvitsee kahdeksan ydintä, kuluttaa yhdeksän CPU-ydintä.


### Sarja-GPU-töiden lähettäminen {#submitting-serial-gpu-jobs}
Voimme luoda GPU-varauksen asettamalla sopivat arvot `Partition`, `GpuCard`, ja `GPUsPerNode` -ominaisuuksille.
Esimerkiksi, yhden GPU:n varaus näyttää seuraavalta:

```matlab
c = parcluster;
% Korvaa 'project_id' projektitunnisteellasi, muuten skripti epäonnistuu.
c.AdditionalProperties.ComputingProject = 'project_id';
c.AdditionalProperties.Partition = 'gpu';
c.AdditionalProperties.WallTime = '00:15:00';
c.AdditionalProperties.CPUsPerNode = 1;
c.AdditionalProperties.MemPerCPU = '4g';
c.AdditionalProperties.GpuCard = 'v100';
c.AdditionalProperties.GPUsPerNode = 1;
c.AdditionalProperties.EmailAddress = '';
```

Nyt voimme lähettää yksinkertaisen GPU-työn, joka kysyy saatavilla olevan GPU-laitteen seuraavasti:

```matlab
j = batch(c, @gpuDevice, 1, {}, 'CurrentFolder', '.', 'AutoAddClientPath', false)
```


### Töiden ja tulosten kysely {#querying-jobs-and-output}
Saadaksesi listan nykyisistä käynnissä olevista tai valmiista töistä, käytä

```matlab
c = parcluster;
c.Jobs
```

Hanki kahva työlle, jolla on sekvenssinumero 1

```matlab
j = c.Jobs(1);
```

Kun meillä on kahva klusterille, kutsumme `findJob`-metodia etsiäksemme työ ID:llä, esimerkissä alla `ID = 11`.

```matlab
j = findJob(c, 'ID', 11);
```

Kun työ on valmis, voimme hakea funktion tulokset seuraavasti:

```matlab
fetchOutputs(j)
```

Klusterin tiedostojärjestelmään kirjoitetut tiedot on haettava suoraan tiedostojärjestelmästä.


<!--
Kun olemme tunnistaneet työn, jonka haluamme nähdä, voimme noutaa tulokset aiemmin kuvatuilla tavoilla.
Jos työssä on ollut virhe, voimme kutsua `getDebugLog`-metodia nähdäksesi virhelokitiedoston.
Virheloki voi olla pitkä, joten sitä ei näytetä tässä.

Esimerkiksi, haemme sarjatyön virhelokin.

```matlab
getDebugLog(j.Parent, j.Tasks(1))
```

Vianmääritystä varten, haetaan lokitiedosto.

```matlab
getDebugLog(j.Parent ,j)
```
-->


<!--
### Lisenssitilanteen tarkistaminen
Voit tarkistaa MPS-lisenssien tilanteen Puhtilla kirjauduttuasi `scontrol`-komennolla.

```bash
scontrol show lic=mdcs
```

```text
LicenseName=mdcs
    Total=500 Used=320 Free=180 Remote=no
```
-->
```

