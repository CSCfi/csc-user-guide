# Ensimmäisen työn suorittaminen Puhtilla

## Kirjautuminen {#logging-in}

Jotta voit valmistella ja suorittaa työsi, sinun on ensin kirjauduttava Puhtille. Voit käyttää joko komentorivisovellusta tai erikoistunutta päätelohjelmaa. Komentorivisovellukset ovat vakiovaruste useimmissa käyttöjärjestelmissä. Päätelohjelmat voivat vaatia erillisen asennuksen, mutta ne tarjoavat yleensä enemmän vaihtoehtoja esimerkiksi kirjasinkoon, kopioinnin ja liittämisen suhteen.

Avaa Linux- tai macOS-järjestelmässä päätelaite. Windows 10:ssä avaa Powershell. Anna komento:

```text
ssh yourcscusername@puhti.csc.fi
```
Missä **yourcscusername** on CSC:ltä saatu käyttäjänimi.

Voit löytää tarkemmat ohjeet käyttäjäohjeestamme: [Yhdistäminen CSC:n supertietokoneisiin](../../computing/connecting/index.md).

## Mikä Puhti on? {#what-is-puhti}

Puhti on, kuten useimmat modernit HPC-järjestelmät (High Performance Computing), klusteritietokone. Tämä tarkoittaa sitä, että sillä on pieni määrä kirjautumissolmuja ja suuri määrä laskentasolmuja.

Kun kirjaudut sisään, päädyt johonkin kahdesta kirjautumissolmusta. Kirjautumissolmut on tarkoitettu esimerkiksi datan siirtämiseen, eräajotyöiden hallintaan ja asetusten tekemiseen. Sinun ei pitäisi suorittaa varsiniaisia töitä kirjautumissolmuissa. Niitä on vain kaksi, ja ne ovat jaettu kaikkien käyttäjien kesken. Suurten töiden suorittaminen niissä voi tehdä järjestelmästä hitaan ja epävakaan kaikkien käyttäjien kannalta (Lisätietoa [käyttöpolitiikastamme](../../computing/usage-policy.md)).

Työt tulisi suorittaa laskentasolmuissa. Tämä tapahtuu erätyöjärjestelmää käyttäen, jota kutsutaan myös *ajastimeksi* tai *kuormanhallitsijaksi*. Puhtilla käytettävä järjestelmä on nimeltään [Slurm](https://slurm.schedmd.com/overview.html).

Suorittaaksesi työsi erätyöjärjestelmän kautta käytät komentoa **srun** tai kirjoitat erätyöskriptin ja käytät komentoa **sbatch**. Keskustelemme tästä myöhemmin yksityiskohtaisemmin.

Katsoaksesi, millaisista laskentasolmuista Puhti koostuu, katso käyttäjän opas: [Puhtin tekniset tiedot](../../computing/systems-puhti.md).

## Ohjelmistoympäristö {#software-environment}

Puhti tarjoaa valikoiman yleisesti käytettyjä biotieteiden ohjelmistoja. Voit tarkistaa listauksen [Sovellukset](../../apps/by_discipline.md#biosciences).

Sovelluslista ei välttämättä ole täysin ajan tasalla, joten on hyvä idea käyttää **module spider** -komentoa tarkistaaksesi, onko ohjelmisto (ja mikä versio) saatavilla, *esim.*:

```text
module spider bowtie2
```

Konfliktien välttämiseksi eri sovellusten ja versioiden välillä suurin osa Puhtin ohjelmistoista on asennettu *moduleina*. Sovelluksen käyttämiseksi sinun on ladattava moduuli, *esim.*:

```text
module load bowtie2
```
Voit myös määrittää tietyn version, *esim.*:
```text
module load bowtie2/2.3.5.1
```
Jos et määritä versiota, ladataan oletusversio (yleensä uusin vakaa julkaisu).

Tarjoamme myös moduulin, joka lataa monia yleisesti käytettyjä biotieteiden sovelluksia kerralla:
```text
module load biokit
```
Helpointa tarkastaa biokit-moduulin sisältö on ladata se ja tarkistaa listaus.
```text
module list
```

Katsoaksesi, mitkä moduulit on ladattava, katso käyttöohje jokaiselle ohjelmistolle.

Lisätietoja moduulijärjestelmästä löytyy käyttäjäoppaan osiosta: [Moduulijärjestelmä](../../computing/modules.md).

## Työn suunnittelu {#planning-your-job}

Työn suorittamiseen erätyöjärjestelmän kautta sinun täytyy varata resursseja, *ts.* ytimien, muistin ja ajan, jotka sopivat työhön. Voidaksesi päättää tarvittavista resursseista, sinun täytyy vastata joihinkin kysymyksiin:

### Kuinka monta ydintä sovellukseni voi käyttää? {#how-many-cores-can-my-application-use}

Ensiksi lyhyesti terminologiasta: Puhuttaessa kotitietokoneista käytetään yleensä termejä "prosessor" ja "ydin". Esimerkiksi useimmissa moderneissa kotitietokoneissa on yksi prosessori, jossa on kaksi tai useampia ytimiä. Puhuttaessa HPC-koneista vastaavat termit ovat "kanta" ja "CPU". Esimerkiksi Puhtin laskentasolmuissa on kaksi kantaa, joissa kummassakin on 20 CPU:ta. Tässä ohjeessa käytetään termejä "prosessorit/ytimet", koska ne ovat todennäköisesti tutumpia ihmisille, joilla ei ole HPC-taustaa.

Sovellukset voidaan jakaa kategorioihin niiden käytettävissä olevien ytimien määrän mukaan:

- **Sarjaohjelmistot**
    - Voi käyttää vain yhtä ydintä
    - Monet biotieteiden ohjelmistot kuuluvat tähän kategoriaan
    - Jos sovellusohjeessa ei mainita käytettävien ytimien tai säikeiden määrää, sovellus on todennäköisesti sarjallinen
    - Useampien ytimien varaaminen ei tee näistä sovelluksista nopeampia, koska ne voivat käyttää vain yhtä ydintä
- **Jaetun muistin/säikeistetyty/OpenMP-sovellukset**
    - Voi käyttää useampaa kuin yhtä ydintä, mutta kaikkien ytimien on oltava samassa solmussa (joten Puhtilla enintään 40 ydintä)
    - Useimmat biotieteiden sovellukset, jotka voivat käyttää useampaa kuin yhtä ydintä, kuuluvat tähän kategoriaan
    - Muista myös ilmoittaa sovellukselle käytettävien ytimien määrä
    - Tarkista sovelluksen dokumentaatiosta oikeat komentorivivaihtoehdot
    - Yleensä on parasta vastata ytimiä säikeiden määrään, mutta tarkista sovelluksen dokumentaatio
- **MPI-parallelisoidut sovellukset**
    - Voi käyttää useampaa kuin yhtä ydintä, ytimet eivät tarvitse olla samassa solmussa
    - Vain hyvin harvat biotieteiden sovellukset kuuluvat tähän kategoriaan
- **Hybridi-parallelisoidut sovellukset**
    - Työ, jossa jokaiselle MPI-tehtävälle varataan useita ytimiä. Jokainen tehtävä käyttää sitten jotain muuta rinnakkaistamista kuin MPI työtä tehdäkseen. Yleisin strategia on se, että jokainen MPI-tehtävä käynnistää useita säikeitä käyttämällä OpenMP:tä.
    - Melko harvinainen biotieteen sovelluksissa

Selvittääksesi, mihin kategoriaan sovelluksesi kuuluu, lue dokumentaatio.

On myös huomattava, että useammat ytimet eivät automaattisesti tarkoita nopeampaa suoritusaikaa. Liian monen ytimen varaaminen voi itse asiassa hidastaa ohjelmiston toimintaa. Optimaalinen ytimien määrä riippuu sovelluksesta, datasta ja suoritetusta analyysista. Sinun pitäisi tarkistaa sovelluksen dokumentaatiosta, antaa kehittäjät ohjeita. On myös hyvä idea tehdä joitakin testejä eri ytimien lukumäärillä nähdäkseen, kuinka hyvin sovellus skaalautuu.

### Kuinka paljon muistia sovellukseni tarvitsee? {#how-much-memory-does-my-application-need}

Vaaditun muistin arvioiminen voi olla melko vaikeaa. Monissa tapauksissa se riippuu valitusta datasta ja sovelluksen asetuksista. Myös säikeiden määrä voi usein vaikuttaa muistivaatimuksiin.

Sinun pitäisi lukea sovelluksen dokumentaatio nähdäksesi, antavatko kehittäjät jotakin arviota. Usein on myös hyödyllistä tarkistaa käyttäjäfoorumeilta, jos ohjelmistolla on sellainen.

Usein, erityisesti kun sovellusta ajetaan ensimmäistä kertaa, täytyy vain tehdä arvaus. Jos saat virheilmoituksen muistin loppumisesta, lisää muistivarausta ja yritä uudelleen. Jos tehtävä valmistuu, voit tarkistaa todellisen muistinkäytön ja käyttää sitä varausten tekemiseen tulevaisuudessa.

Enemmän tietoa löytyy tästä UKK-kohdasta: [Miten arvioida kuinka paljon muistia erätehtäväni tarvitsee?](../faq/how-much-memory-my-job-needs.md)

### Kuinka paljon aikaa minun pitäisi varata? {#how-much-time-should-i-reserve}

Suoritusaikaan tutustuminen etukäteen voi olla vaikeaa, jos et tunne sovellusta.

Sinun pitäisi varmistaa, että varaat tarpeeksi, sillä työ keskeytetään, kun aikavaraus loppuu, olipa se valmistunut vai ei.

Toisaalta liian suuren aikavälin varaaminen ei ole niin suuri ongelma. Työ valmistuu, kun työn viimeinen tehtävä valmistuu. Työsi kuluttaa laskentayksikköjä ainoastaan todellisen kuluneen ajan, ei varauksen mukaan.

On ihan ok varata maksimiaika osiossa, jossa käytät sovellusta ensimmäistä kertaa. Kun työ on valmis, voit tarkistaa kuluneen ajan ja tehdä paremmin tietoisen varauksen seuraavalla kerralla.

## Työn suorittaminen {#running-your-job}

### Interaktiiviset työt {#interactive-jobs}

Interaktiiviset työt ovat hyviä esimerkiksi testaamiseen, pienien tehtävien suorittamiseen ja ohjelmistoihin, joilla on graafinen käyttöliittymä.

Kuten mainittua, et pitäisi suorittaa töitä kirjautumissolmussa. Sen sijaan voit käyttää **sinteractive**-komentoa avataksesi interaktiivisen komentokehotteen:

```text
sinteractive -i
```
Katso tarkemmat ohjeet Käyttäjän oppaasta: [Interaktiivinen käyttö](../../computing/running/interactive-usage.md)

Pidemmät töitä, jotka vievät enemmän resursseja, on parasta suorittaa erätöinä.

### Erätyöt {#batch-jobs}

Erätyön suorittaminen koostuu tyypillisesti kolmesta vaiheesta:
1. Varmista, että sinulla on kaikki tarvittavat syötetiedostot
    1. Ohjeet kuinka siirtää tietoa omalta tietokoneeltasi Puhtille, katso osio [Data/Tiedon siirtäminen](../../data/moving/index.md) Käyttäjän oppaassa
2. Kirjoita erätyöskripti
    1. Käytä tekstieditoria kuten nano, vim tai emacs kirjoittaaksesi skriptin
    2. Jos kirjoitat skriptin omalla tietokoneellasi ja siirrät sen Puhtille, ole varovainen. Varmista, että se on tallennettu tekstinä eikä esimerkiksi Word-dokumenttina. Ole myös tietoinen, että Windows käsittelee rivinvaihtoja eri tavalla kuin Linux, ja tämä voi aiheuttaa ongelmia.
3. Lähetä työ

Tässä on esimerkki erätyöskriptistä. Se on tallennettu nimellä *myjobscript*
```text
#!/bin/bash
#SBATCH --job-name=bowtie2
#SBATCH --account=project_123456
#SBATCH --ntasks=1
#SBATCH --nodes=1  
#SBATCH --cpus-per-task=16
#SBATCH --mem=16g
#SBATCH --time=04:00:00
#SBATCH --partition=small

module load biokit
bowtie2 -p $SLURM_CPUS_PER_TASK -x genome -1 reads_1.fq -2 reads_2.fq > output.sam
```

Kaikki rivit, jotka alkavat **#SBATCH**-merkkijonolla, välitetään erätyöjärjestelmälle. Käytämme niitä vaatiaksemme tarvittavat resurssit.

Työn nimi (--job-name) käytetään pääasiassa työn tunnistamiseksi *esim.* kun listaat työt **squeue**-komennolla tai tarkistat menneitä töitä **sacct**-komennolla.

On välttämätöntä ilmoittaa järjestelmälle, mikä projektin pitäisi laskuttaa. Tämä tehdään **--account**-vaihtoehdolla. Voit tarkistaa projektit, joihin kuulut, [MyCSC](https://my.csc.fi/myProjects)-palvelusta tai `csc-projects`-komennolla komentorivillä.

Bowtie2 on jaetun muistin sovellus. Kuten aiemmin mainittiin, tämä tarkoittaa, että se voi käyttää useampaa kuin yhtä ydintä, mutta kaikki ytimet on oltava samassa solmussa. Määrittelemme, että haluamme ajaa yhden tehtävän (--ntask=1) yhdessä solmussa (--nodes=1) käyttäen 16 ydintä (--cpus-per-task):

```text
#SBATCH --ntasks=1
#SBATCH --nodes=1  
#SBATCH --cpus-per-task=16
```

Koska se on jaetun muistin sovellus, voimme käyttää `--mem`-vaihtoehtoa määrittämään tehtävälle pyydetyn kokonaismuistin. MPI-työlle meidän täytyisi pyytää muisti per ydin `--mem-per-cpu`-vaihtoehdolla.

```text
#SBATCH --mem=16G
```

Aikavaraus annetaan muodossa tunnit:minuutit:sekunnit *eli* `hh:mm:ss`. Tässä tapauksessa varataan neljä tuntia:

```text
#SBATCH --time=04:00:00
```

Meidän täytyy myös määrittää, mitä osiota (myös kutsutaan jonoksi) haluamme työn suorittamiseen. Tämä määritetään `--partition`-vaihtoehdolla. Useimmille biotieteiden töille "small" on oikea valinta. Se on töille, jotka suoritetaan yhden solmun sisällä.

```text
#SBATCH --partition=small
```

Voit tarkistaa käytettävissä olevat osiot Käyttäjän oppaasta: [Saatavilla olevat erätehtäväosiot](../../computing/running/batch-job-partitions.md)

Oletuksena erilaiset tulosteet ja virheilmoitukset, jotka tulostettaisiin näytölle, jos sovellus ajettaisiin interaktiivisesti, tallennetaan tiedostoon nimeltä *slurm-&lt;jobid&gt;.out*. Joskus on selvempää erottaa tulosteet ja virheet. Tämä voidaan tehdä lisäämällä `--output` ja `--error`-vaihtoehdot. `%j` korvataan työn jobid-tunnuksella tiedoston nimessä.

```text
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
```

Saatavilla on myös muita vaihtoehtoja. Yksityiskohtaisempaan selitykseen, katso Käyttäjän opas: [Erätehtäväskriptin luominen Puhtille](../../computing/running/creating-job-scripts-puhti.md)

Kun olet kirjoittanut erätyöskriptin, voit lähettää työn jonoon:
```text
sbatch myjobscript
```
Jos työ lähetettiin onnistuneesti, sinun pitäisi nähdä viesti:
```text
Submitted batch job <jobid>
```

On mahdollista käynnistää työ suoraan komennolla **srun** antamalla `#SBATCH`- rivien vaihtoehdot suoraan komentorivi-vaihtoehtoina, mutta erätyöskriptin kirjoittaminen on yleensä suositeltavaa selkeyden ja uudelleenkäytön helpottamiseksi *esim.* jos haluat lähettää samanlaisen työn eri datalla tai muokatuilla parametreilla.

### Taulukkoajot {#array-jobs}

Jos haluat suorittaa useita saman komennon instansseja eri syötetiedostoilla tai eri parametreillä, kannattaa harkita niiden ajamista taulukkoajona. Taulukkoajot tarjoavat helpon tavan käynnistää ja hallita ryhmää samanlaisia töitä.

Taulukkoajojen suorittaminen kuvataan yksityiskohtaisesti Käyttäjän oppaassa: [Array-jotokset](../../computing/running/array-jobs.md)

## Tehtävien hallinta {#managing-jobs}

Voit tarkistaa nykyiset tehtäväsi, sekä suoritettavat että jonossa olevat:
```text
squeue -u <username>
```
Tai saada hieman yksityiskohtaisempia listatietoja käyttäen:
```text
squeue -l -u <username>
```
Voit tarkistaa työsi tilan ST- tai STATUS-sarakkeesta riippuen, käytetäänkö vaihtoehdon -l vai ei. R tai RUNNING tarkoittaa, että työ on tällä hetkellä käynnissä. P tai PENDING tarkoittaa, että se on vielä jonossa.

Jos työ on odottava, voit nähdä syyn NODELIST(REASON)-sarakkeesta.

Syyt:
```text
(Resources)
```
tai
```text
 (Nodes required for job are DOWN, DRAINED or reserved for jobs in higher priority partitions)
```
tarkoittavat, että tällä hetkellä ei ole saatavilla olevia resursseja työn suorittamiseen. Työ käynnistyy, kun resurssit vapautuvat.

Syyt:
```text
(Priority)
```
tarkoittavat, että työsi pidätetään erätyöjärjestelmän fair share -toiminnallisuuden vuoksi: Kun käyttäjä suorittaa paljon töitä lyhyessä ajassa, hänen työnsä saa alhaisemman prioriteetin. Nämä työt odottavat jonossa hieman kauemmin, mutta ne suoritetaan lopulta.

Jonotusaika riippuu yleisestä kuormituksesta järjestelmässä (*eli* kuinka monta työtä on jonossa ennen sinun) ja töiden resurssivaatimuksista.

Jos tuntuu, että työsi jonottuvat pitkään, kannattaa tarkistaa tämä UKK-kohta: [Miksi erätehtäväni jonottaa niin pitkään?](../faq/why-is-my-job-queueing-so-long.md)

On myös muita vähemmän yleisiä syitä, mutta ne ovat harvinaisempia. Tarvittaessa ota yhteyttä **servicedesk@csc.fi**.

Voit peruuttaa lähetetyn erätyön seuraavasti:
```text
scancel <jobid>
```

## Resurssien käytön seuranta {#monitoring-resource-usage}

Kun työ on valmis, voit käyttää komentoja **seff** ja **sacct** tarkistaaksesi työn todelliset resurssienkulutukset.
```text
seff <jobid>
```

Tärkeimmät asiat tarkistaa ovat CPU:n tehokkuus ja muistin käyttö.

Monet asiat voivat aiheuttaa huonoa CPU:n tehokkuutta. Se voisi esimerkiksi tarkoittaa, että ohjelma odottaa levytoimintojen saavuttavan tehtävänsä. Näissä tapauksissa on syytä harkita solmun käyttöä, jossa on nopea paikallinen levy. Yksityiskohdat löytyvät Käyttäjän oppaasta: [Erätöiden luominen Puhtille](../../computing/running/creating-job-scripts-puhti.md)

Alhainen tehokkuus voi myös johtua yli yhden ytimen varaamisesta ja ohjelmiston huonosta skaalaamisesta. Tarkista erityisesti, vastaako prosenttiluku varattujen ytimien määrää, *esim.* 25% neljällä ytimellä tai 12,5% kahdeksalla ytimellä *etc*. Tämä johtuu yleensä siitä, että sovellus käyttää vain yhtä ydintä. Tarkista, voiko sovellus todella käyttää enemmän kuin yhtä ydintä, tai oletko asettanut vastaavan sovellusparametrin oikein.

```text
CPU Efficiency: 12.48% of 06:56:08 core-walltime
```

Tarkista myös todellinen hyödynnetty muisti ja aseta muistivaraus seuraavaa suoritus kertaa varten vastaavasti, mutta jätä jonkin verran turvamarginaalia, esim. muutama GB. Esimerkiksi seuraavassa työssä, muistipyyntö on ollut aivan liian suuri (92GB pyydetty vs. 6GB käytetty).

```text
Memory Utilized: 5.98 GB
Memory Efficiency: 6.25% of 92.59 GB
```

Toinen komento tarkistaa menneiden töiden tila ja resurssien käyttö on **sacct**. Se on kätevä, kun haluat nähdä monien töiden tilan (*esim.* kaikki osatyöt taulukkoajossa). Komento **seff** näyttää vain yhden työn kerrallaan.

```text
sacct
```
Oletuksena näytettävä tieto sisältää töiden tilan (PENDING/RUNNING/COMPLETED/FAILED) ja työn id:n.

Voit myös määrittää, mitkä kentät näytetään -o-vaihtoehdolla:
```text
sacct -o jobid,jobname,ntasks,ReqNodes,allocnodes,reqcpus,alloccpus,reqmem,maxrss,timelimit,elapsed,state -j <jobid>
```
Oletuksena **sacct** näyttää vain nykyisen päivän töitä. Voit valita aloituspäivämäärän -S-vaihtoehdolla.
```text
sacct -S <YYYY-MM-DD>
```
Huomaa, että `sacct`-komento on raskas jonotusjärjestelmän suhteen, joten älä rakenna skriptejä, jotka suorittavat sen toistuvasti.

## Vianmääritys {#troubleshooting}

### Tutustuminen uuteen ohjelmaan {#getting-familiar-with-a-new-program}

Tässä on joitakin hyödyllisiä vaiheita tutustuessasi uuteen ohjelmaan.

- Lue ohje
- Voi olla hyödyllistä yrittää ensin ajaa ohjelma interaktiivisesti löytääksesi oikeat komentorivivaihtoehdot
    - Tämä mahdollistaa `top`-komennon käytön saadakseen karkean arvion muistinkäytöstä jne.
- Jos kehittäjät tarjoavat joitain testaus- tai esimerkkidataa, aja ne ensin
    - Varmista, että tulokset ovat odotetut
- Voit käyttää testiosuutta tarkistaaksesi erätyöskriptin
    - Rajat: 15 min, 2 solmua
    - Työn vaihtuvuus yleensä hyvin nopeaa
    - Voi olla hyödyllinen tarkistaa kirjoitusvirheitä, puuttuvia tiedostoja jne. ennen suuren työn lähettämistä
- Ennen hyvin suuria suorituslenkkejä on hyvä tehdä pienempi koeajo
    - Tarkista, että tulokset ovat odotetut
    - Tarkista resurssien käyttö koeajon jälkeen ja säädä sitä vastaavasti
    - Kokeile eri ytimien määriä ja katso, kuinka ohjelmisto skaalautuu

### Vianmäärityksen tarkistuslista {#troubleshooting-checklist}

Aloita näistä, jos työsi epäonnistuu:

1. Loppuiko tehtävältä aika?
2. Loppuiko tehtävältä muisti?
3. Käyttikö tehtävä todella määrittämiäsi resursseja?
    - Ongelmia erätyöskriptissä voi aiheuttaa parametrien huomiotta jättämisen ja oletusarvojen käytön
4. Epäonnistuko se heti vai ajoiko se jonkin aikaa?
    - Välittömästi epäonnistuvat työt johtuvat usein jostain yksinkertaisesta kuten 
      kirjoitusvirheistä komentorivillä, puuttuvista syötteistä, vääristä parametreista jne.
5. Tarkista erätyöskriptin tallentama virhetiedosto
6. Tarkista kaikki muut virhetiedostot ja lokit, jotka ohjelma on saattanut luoda
7. Virheilmoitukset voivat toisinaan olla pitkiä, kryptisiä ja hieman pelottavia, 
   mutta yritä silti silmäillä niitä ja katso, voitko löytää jotain 
   ”ihmisen luettavissa” sen sijaan, että olisi ”nörtille luettavissa”
    - Usein voit huomata todellisen ongelman helposti käymällä koko 
      viestin läpi. Jotain kuten ”vaadittu syötetiedosto on ja on puuttuva” 
      tai ”parametri X vääränlainen” jne.

Jos et pysty selvittämään sitä, älä epäröi ottaa yhteyttä osoitteeseen 
**servicedesk@csc.fi**. Muista liittää mukaan olennaiset tiedot, kuten mitä 
ohjelmaa yritit suorittaa ja millä palvelimella jne.