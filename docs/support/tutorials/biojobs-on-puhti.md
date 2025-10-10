# Ensimmäisen työn ajaminen Puhtissa { #running-your-first-job-on-puhti }

## Kirjautuminen { #logging-in }

Ennen kuin valmistelet ja ajat työsi, sinun on ensin kirjauduttava Puhtiin. Voit käyttää joko komentorivisovellusta tai erillistä pääteohjelmaa. Komentorivisovellukset sisältyvät vakiona useimpiin käyttöjärjestelmiin. Pääteohjelmat saattavat vaatia erillisen asennuksen, mutta ne tarjoavat tyypillisesti enemmän vaihtoehtoja esimerkiksi fonttikoon, kopioi–liitä-toimintojen jne. suhteen.

Avaa Linuxissa tai macOS:ssä pääte. Windows 10:ssä avaa PowerShell. Anna komento:

```text
ssh yourcscusername@puhti.csc.fi
```
Missä **yourcscusername** on CSC:ltä saamasi käyttäjätunnus.

Löydät tarkemmat ohjeet käyttäjäoppaastamme: [Connecting
to CSC supercomputers](../../computing/connecting/index.md).


## Mikä on Puhti? { #what-is-puhti }

Puhti on, kuten useimmat modernit HPC-järjestelmät (High Performance Computing), klusteritietokone. Tämä tarkoittaa, että siinä on pieni määrä kirjautumissolmuja ja suuri määrä laskentasolmuja.

Kirjautuessasi päädyt johonkin kahdesta kirjautumissolmusta. Kirjautumissolmut on tarkoitettu esimerkiksi datan siirtämiseen sekä eräajojen valmisteluun ja hallintaan. Et saa ajaa varsinaisia töitä kirjautumissolmuissa. Kirjautumissolmuja on vain kaksi ja ne ovat kaikkien yhteiskäytössä. Raskaiden töiden ajaminen niissä voi hidastaa ja tehdä järjestelmästä epävastaavan kaikille (lisätietoja [käyttöpolitiikassamme](../../computing/usage-policy.md)).

Työt tulee ajaa laskentasolmuissa. Tämä tehdään käyttämällä *eräajojärjestelmää*, jota kutsutaan myös *ajastimeksi* tai *työkuorman hallintajärjestelmäksi*. Puhtissa käytössä oleva järjestelmä on [Slurm](https://slurm.schedmd.com/overview.html).

Ajaaksesi työn eräajojärjestelmän kautta käytät komentoa **srun** tai kirjoitat eräajoskriptin ja käytät komentoa **sbatch**. Palaamme tähän tarkemmin myöhemmin.

Puhtin käytettävissä olevat laskentasolmut löydät käyttäjäoppaasta: [Technical details about
Puhti](../../computing/systems-puhti.md).


## Ohjelmistoympäristö { #software-environment }

Puhtissa on saatavilla valikoima yleisesti käytettyjä bioalan ohjelmistoja. Voit tarkistaa listauksen kohdasta
[Applications](../../apps/by_discipline.md#biosciences).

Sovelluslista ei välttämättä ole täysin ajantasainen, joten on hyvä käyttää komentoa **module spider** nähdäksesi, onko ohjelmisto (ja mikä versio) saatavilla, *esim.*:

```text
module spider bowtie2
```

Välttääksesi ristiriidat eri sovellusten ja versioiden välillä, suurin osa ohjelmistoista Puhtissa on asennettu *moduleiksi*. Käyttääksesi sovellusta sinun tulee ladata moduuli, *esim.*:

```text
module load bowtie2
```
Voit myös valita tietyn version, *esim.*:
```text
module load bowtie2/2.3.5.1
```
Jos et määritä versiota, ladataan oletusversio (tyypillisesti uusin vakaa julkaisu).

Tarjoamme myös moduulin, joka lataa kerralla monia yleisesti käytettyjä bioalan sovelluksia:
```text
module load biokit
```
Helpoin tapa nähdä biokit-moduulin sisältö on ladata se ja tarkistaa listaus.
```text
module list
```

Nähdäksesi, mitkä moduulit pitää ladata, katso kunkin ohjelmiston ohjesivu.

Lisätietoja modulijärjestelmästä löydät käyttäjäoppaasta:
[The module system](../../computing/modules.md).


## Työn suunnittelu { #planning-your-job }

Ajaaksesi työn eräajojärjestelmän kautta sinun tulee varata resursseja, *eli* ytimiä, muistia ja aikaa, jotka sopivat työhön. Päättääksesi tarvittavista resursseista sinun pitää vastata muutamaan kysymykseen:

### Kuinka monta ydintä sovellukseni voi käyttää? { #how-many-cores-can-my-application-use }

Lyhyesti termistöstä: Kotikoneista puhuttaessa käytetään yleensä termejä ”prosessori” ja ”ydin”. Esimerkiksi useimmissa moderneissa kotikoneissa on yksi prosessori, jossa on kaksi tai useampia ytimiä. HPC-koneista puhuttaessa vastaavat termit ovat ”socket” ja ”CPU”. Esimerkiksi Puhtin laskentasolmuissa on kaksi socketia, joissa kussakin on 20 CPU:ta. Tässä ohjeessa käytetään termejä ”prosessori/ydin”, sillä ne ovat todennäköisesti tutumpia ilman HPC-taustaa.

Sovellukset voidaan jakaa kategorioihin sen mukaan, kuinka monta ydintä ne voivat käyttää:

- **Sarjaohjelmat**
    - Voivat käyttää vain yhtä ydintä
    - Monet bioalan sovellukset kuuluvat tähän kategoriaan
    - Jos sovelluksen ohjeessa ei mainita ytimien tai säikeiden määrää, sovellus on todennäköisesti sarjallinen
    - Lisäytimien varaaminen ei nopeuta näitä sovelluksia, koska ne voivat käyttää vain yhtä
- **Jaetun muistin/säikeistetyt/OpenMP-sovellukset**
    - Voivat käyttää useampaa ydintä, mutta kaikkien ytimien tulee olla samassa solmussa (Puhtissa enintään 40 ydintä)
    - Suurin osa bioalan sovelluksista, jotka voivat käyttää useampaa ydintä, kuuluu tähän kategoriaan
    - Muista kertoa sovellukselle käytettävien ytimien määrä
    - Tarkista oikeat komentorivivalinnat sovelluksen dokumentaatiosta
    - Yleensä on parasta sovittaa ytimien määrä säikeiden määrään, mutta tarkista sovelluskohtaiset ohjeet
- **MPI-rinnakkaissovellukset**
    - Voivat käyttää useampaa ydintä, eikä ytimien tarvitse olla samassa solmussa
    - Vain hyvin harvat bioalan sovellukset kuuluvat tähän kategoriaan
- **Hybridiparalleliset sovellukset**
    - Työ, jossa jokaiselle MPI-tehtävälle varataan useita ytimiä. Kukin tehtävä käyttää sitten jotakin muuta rinnakkaistusta kuin MPI:tä työn tekemiseen. Yleisin tapa on, että jokainen MPI-tehtävä käynnistää useita säikeitä OpenMP:llä.
    - Melko harvinaisia bioalan sovelluksissa

Selvittääksesi, mihin kategoriaan sovelluksesi kuuluu, lue dokumentaatio.

On myös syytä huomata, että enemmän ytimiä ei automaattisesti tarkoita lyhyempää ajoaikaa. Liian monen ytimen varaaminen voi itse asiassa hidastaa ohjelmaa. Optimaalinen ydinmäärä riippuu sovelluksesta, datasta ja tehtävästä analyysista. Tarkista, antaako sovelluksen dokumentaatio ohjeistusta. On myös hyvä ajaa testejä eri ydinmäärillä ja katsoa, miten sovellus skaalaa.


### Kuinka paljon muistia sovellukseni tarvitsee? { #how-much-memory-does-my-application-need }

Tarvittavan muistin arvioiminen voi olla melko vaikeaa. Usein siihen vaikuttavat käytettävä data ja valitut sovelluksen asetukset. Myös käytettyjen säikeiden määrä voi usein vaikuttaa muistitarpeeseen.

Lue sovelluksen dokumentaatiota nähdäksesi, antavatko kehittäjät mitään arviota. Usein on myös hyödyllistä tarkistaa käyttäjäfoorumit, jos sovelluksella on sellainen.

Usein, erityisesti ensimmäisellä ajokerralla, sinun on vain tehtävä valistunut arvaus. Jos saat virheilmoituksen muistin loppumisesta, kasvata muistivarausta ja yritä uudelleen. Jos työ valmistuu, voit tarkistaa toteutuneen muistinkäytön ja käyttää sitä tulevien varausten pohjana.

Lisätietoja löytyy tästä UKK-artikkelista: [How to estimate how
much memory my batch job
needs?](../faq/how-much-memory-my-job-needs.md)


### Kuinka paljon aikaa minun tulisi varata? { #how-much-time-should-i-reserve }

Ajoajan tunteminen etukäteen voi olla vaikeaa, jos et tunne sovellusta.

Varmista, että varaat riittävästi aikaa, koska työ pysäytetään, kun aikavaraus loppuu, oli se valmis tai ei.

Toisaalta liian suuren ajan varaaminen ei ole kovin suuri ongelma. Työ päättyy, kun työn viimeinen tehtävä valmistuu. Työ kuluttaa laskutusyksiköitä vain toteutuneen keston mukaan, ei varauksen mukaan.

On täysin ok varata osion sallima maksimiaika, kun ajat sovellusta ensimmäistä kertaa. Kun työ valmistuu, voit tarkistaa kuluneen ajan ja tehdä seuraavalla kerralla perustellumman varauksen.


## Työn ajaminen { #running-your-job }

### Interaktiiviset työt { #interactive-jobs }

Interaktiiviset työt sopivat hyvin esimerkiksi testaamiseen, pieniin tehtäviin ja ohjelmistoille, joilla on graafinen käyttöliittymä.

Kuten mainittu, töitä ei tule ajaa kirjautumissolmussa. Sen sijaan voit käyttää komentoa **sinteractive** avataksesi interaktiivisen shellin:

```text
sinteractive -i
```
Tarkemmat ohjeet löytyvät käyttäjäoppaasta: [Interactive usage](../../computing/running/interactive-usage.md)

Pidemmät ja enemmän resursseja vaativat työt kannattaa ajaa eräajoina.

### Eräajot { #batch-jobs }

Eräajon suorittaminen koostuu tyypillisesti kolmesta vaiheesta:
1. Varmista, että sinulla on kaikki tarvittavat syötteet
    1. Ohjeet datan siirtämiseksi omalta koneeltasi Puhtiin löydät käyttäjäoppaan osiosta [Data/Moving data](../../data/moving/index.md)
2. Kirjoita eräajoskripti
    1. Käytä tekstieditoria, kuten nano, vim tai emacs, skriptin kirjoittamiseen
    2. Jos kirjoitat skriptin omalla koneellasi ja siirrät sen Puhtiin, ole huolellinen. Varmista, että se on tallennettu tekstimuodossa, ei Word-dokumenttina tai vastaavana. Huomaa myös, että Windows käsittelee rivinvaihdot eri tavalla kuin Linux, mikä voi aiheuttaa ongelmia.
3. Lähetä työ jonoon

Tässä on esimerkkieräskripti. Se on tallennettu nimellä *myjobscript*
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

Kaikki rivit, jotka alkavat **#SBATCH**, välitetään eräajojärjestelmälle. Niillä pyydämme tarvittavat resurssit.

Työn nimi (--job-name) on lähinnä tunnistamista varten, *esim.* kun listaat töitä komennolla **squeue** tai tarkistat aiempia töitä komennolla **sacct**.

On välttämätöntä kertoa järjestelmälle, mille projektille laskutus kohdistetaan. Tämä tehdään valinnalla **--account**. Voit tarkistaa projektit, joihin kuulut, [MyCSC](https://my.csc.fi/myProjects)-palvelusta tai komennolla `csc-projects` komentoriviltä.

Bowtie2 on jaetun muistin sovellus. Kuten aiemmin todettiin, se voi käyttää useampaa ydintä, mutta kaikkien ytimien tulee olla samassa solmussa. Määrittelemme, että haluamme ajaa yhden tehtävän (--ntask=1) yhdessä solmussa
(--nodes=1) käyttäen 16 ydintä (--cpus-per-task):

```text
#SBATCH --ntasks=1
#SBATCH --nodes=1  
#SBATCH --cpus-per-task=16
```

Koska kyseessä on jaetun muistin sovellus, voimme käyttää `--mem`-valintaa pyytämään tehtävälle kokonaismuistin. MPI-työssä muistia pitäisi pyytää ydintä kohti valinnalla `--mem-per-cpu`.

```text
#SBATCH --mem=16G
```

Aikavaraus annetaan muodossa tunnit:minuutit:sekunnit, *eli* `hh:mm:ss`. Tässä varaamme neljä tuntia:

```text
#SBATCH --time=04:00:00
```

Meidän täytyy myös määrittää, missä osiossa (myös ”jono”) työ ajetaan. Tämä määritetään valinnalla `--partition`. Useimmille bioalan töille ”small” on oikea valinta. Se on töille, jotka ajavat yhden solmun sisällä.

```text
#SBATCH --partition=small
```

Käytettävissä olevat osiot löydät käyttäjäoppaasta: [Available
batch job partitions](../../computing/running/batch-job-partitions.md)

Oletuksena erilaiset tulosteet ja virheilmoitukset, jotka näkyisivät ruudulla, jos sovellus ajettaisiin interaktiivisesti, tallennetaan tiedostoon *slurm-&lt;jobid&gt;.out*. Joskus on selkeämpää erottaa tulosteet ja virheet. Tämä onnistuu lisäämällä valinnat `--output` ja
`--error`. `%j` korvataan tiedoston nimessä työn jobid:llä.

```text
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
```

Saatavilla on myös muita valintoja. Yksityiskohtaisemman selityksen löydät käyttäjäoppaasta: [Creating a batch job script
for Puhti](../../computing/running/creating-job-scripts-puhti.md)

Kun olet kirjoittanut eräskriptin, voit lähettää työn jonoon:
```text
sbatch myjobscript
```
Jos työn lähetys onnistui, näet viestin:
```text
Submitted batch job <jobid>
```

Työ on mahdollista käynnistää myös suoraan komennolla **srun** antamalla `#SBATCH`-riveillä annetut valinnat suoraan komentorivivalintoina, mutta eräskriptin kirjoittaminen on yleensä selkeämpää ja helpottaa uudelleenkäyttöä, jos esimerkiksi haluat ajaa vastaavan työn eri datalla tai muokatuilla parametreilla.

### Array-työt { #array-jobs }

Jos haluat ajaa saman komennon useita instansseja eri syötetiedostoilla tai eri parametrikokonaisuuksilla, kannattaa harkita niiden ajamista array-työnä. Array-työt tarjoavat helpon tavan käynnistää ja hallita joukkoa samankaltaisia töitä.

Array-töiden ajaminen on kuvattu yksityiskohtaisesti käyttäjäoppaassa:
[Array jobs](../../computing/running/array-jobs.md)

## Töiden hallinta { #managing-jobs }

Voit tarkistaa nykyiset työsi, sekä ajossa että jonossa:
```text
squeue -u <username>
```
Tai saada hieman yksityiskohtaisemman listauksen:
```text
squeue -l -u <username>
```
Voit tarkistaa työn tilan sarakkeesta ST tai STATUS (riippuen käytätkö -l -valintaa vai et). R tai RUNNING tarkoittaa, että työ on käynnissä. P tai PENDING tarkoittaa, että se odottaa edelleen jonossa.

Jos työ on jonossa (pending), näet syyn sarakkeessa NODELIST(REASON).

Syy:
```text
(Resources)
```
tai
```text
 (Nodes required for job are DOWN, DRAINED or reserved for jobs in higher priority partitions)
```
tarkoittaa, ettei tällä hetkellä ole vapaita resursseja työn ajamiseen. Työ käynnistyy heti, kun resursseja vapautuu.

Syy:
```text
(Priority)
```
tarkoittaa, että fairshare-toiminnallisuus pitää työtäsi odottamassa: Kun käyttäjä ajaa lyhyessä ajassa paljon töitä, hänen töidensä prioriteetti on matalampi. Tällaiset työt viettävät hieman pidempään jonossa, mutta ne ajetaan lopulta.

Jonotusaika riippuu järjestelmän kokonaiskuormasta (*eli* kuinka monta työtä on jonossa ennen omaasi) sekä töidesi resurssivaatimuksista.

Jos tuntuu, että työsi jonottavat pitkään, voit tarkistaa tämän UKK-kohdan:
[Why is my batch job queueing so long?](../faq/why-is-my-job-queueing-so-long.md)

On olemassa myös muita syitä, mutta ne ovat harvinaisempia. Ota tarvittaessa yhteyttä osoitteeseen **servicedesk@csc.fi**.

Voit perua lähetetyn erätyön komennolla:
```text
scancel <jobid>
```

## Resurssien käytön seuranta { #monitoring-resource-usage }

Kun työ on valmistunut, voit käyttää komentoja **seff** ja **sacct** tarkistaaksesi, mitä resursseja työ todellisuudessa käytti.
```text
seff <jobid>
```

Tärkeimmät tarkistettavat asiat ovat CPU-tehokkuus ja muistin käyttö.

Heikkoon CPU-tehokkuuteen voi olla monia syitä. Se voi esimerkiksi viitata siihen, että ohjelma odottaa levyn I/O:n pysyvän perässä. Tällaisissa tapauksissa kannattaa harkita solmua, jossa on nopea paikallinen levy. Lisätietoja käyttäjäoppaassa:
[Creating a batch job script for Puhti](../../computing/running/creating-job-scripts-puhti.md)

Heikko tehokkuus voi johtua myös siitä, että varasit useamman ytimen, mutta sovellus skaalaa huonosti. Tarkista erityisesti, vastaako prosenttiosuus varattujen ytimien määrää, *esim.* 25 % neljällä ytimellä tai 12,5 % kahdeksalla ytimellä *jne.* Tämä johtuu tyypillisesti siitä, että sovellus käyttää vain yhtä ydintä. Tarkista, voiko sovellus todella käyttää useampaa ydintä, tai oletko asettanut vastaavan sovellusparametrin oikein.

```text
CPU Efficiency: 12.48% of 06:56:08 core-walltime
```

Tarkista myös toteutunut muistinkäyttö ja säädä muistivarausta seuraavaa ajoa varten sen mukaan, mutta jätä turvamarginaalia, esim. muutama GB. Esimerkiksi seuraavassa työssä muistipyyntö on ollut selvästi liian suuri (pyydetty 92 GB vs. käytetty 6 GB).

```text
Memory Utilized: 5.98 GB
Memory Efficiency: 6.25% of 92.59 GB
```

Toinen komento aiempien töiden tilan ja resurssien käytön tarkasteluun on **sacct**. Se on kätevä, kun haluat nähdä monen työn tiedot (*esim.* array-työn kaikkien alitöiden). Komento **seff** näyttää vain yhden työn kerrallaan.

```text
sacct
```
Oletuksena näytettävät tiedot sisältävät töiden tilan (PENDING/RUNNING/COMPLETED/FAILED) ja jobid:n.

Voit myös valita näytettävät kentät -o -valinnalla:
```text
sacct -o jobid,jobname,ntasks,ReqNodes,allocnodes,reqcpus,alloccpus,reqmem,maxrss,timelimit,elapsed,state -j <jobid>
```
Oletuksena **sacct** näyttää vain kuluvan päivän aikana ajetut työt. Voit valita aloituspäivän valinnalla -S.
```text
sacct -S <YYYY-MM-DD>
```
Huomaa, että `sacct`-komento kuormittaa jonojärjestelmää, joten älä rakenna skriptejä, jotka ajavat sitä toistuvasti.

## Vianmääritys { #troubleshooting }

### Uuteen ohjelmaan tutustuminen { #getting-familiar-with-a-new-program }

Tässä muutamia hyödyllisiä askeleita uuteen ohjelmaan tutustumiseen.

- Lue ohje/dokumentaatio
- Voi olla hyödyllistä kokeilla ensin ohjelman ajamista interaktiivisesti löytääksesi oikeat komentorivivalinnat
    - Tällöin voit käyttää `top`-komentoa saadaksesi karkean arvion muistinkäytöstä jne.
- Jos kehittäjät tarjoavat testidata- tai esimerkkiaineistoa, aja se ensin
    - Varmista, että tulokset ovat odotetunlaisia
- Voit käyttää testiosiota eräskriptin tarkistamiseen
    - Rajat: 15 min, 2 nodes
    - Läpimeno yleensä hyvin nopea
    - Voi olla hyödyllinen havaitsemaan kirjoitusvirheet, puuttuvat tiedostot *jne.* ennen kuin lähetät työn, joka viettää pitkään jonossa
- Ennen hyvin suuria ajoja on hyvä tehdä pienempi koeajo
    - Tarkista, että tulokset ovat odotetut
    - Tarkista resurssien käyttö koeajon jälkeen ja säädä sen mukaan
    - Kokeile eri ydinmääriä ja katso, miten ohjelmisto skaalautuu

### Vianmäärityksen tarkistuslista { #troubleshooting-checklist }

Aloita näistä, jos työsi epäonnistuu:

1. Loppuiko työltä aika?
2. Loppuiko työltä muisti?
3. Käyttikö työ todella varaamiasi resursseja?
    - Ongelmat eräskriptissä voivat aiheuttaa sen, että parametreja ei huomioida ja käytetään oletusarvoja
4. Epäonnistuiko työ heti vai ajoiko se jonkin aikaa?
    - Heti epäonnistuvat työt johtuvat usein jostakin yksinkertaisesta, kuten
      komentorivin kirjoitusvirheistä, puuttuvista syötteistä, virheellisistä parametreista *jne.*
5. Tarkista eräskriptin kaappaama virhetiedosto
6. Tarkista muut ohjelman mahdollisesti tuottamat virhetiedostot ja lokit
7. Virheilmoitukset voivat joskus olla pitkiä, kryptisiä ja hieman pelottavia,
   mutta yritä silmäillä ne läpi ja katsoa, löydätkö jotain
   ”ihmisluettavaa” ”nörttiluettavan” sijaan
    - Usein varsinainen ongelma löytyy helposti, kun käyt koko viestin läpi. Esimerkiksi ”vaadittu syötteetiedosto sitä-ja-sitä puuttuu” tai ”parametri X sallitun alueen ulkopuolella” *jne.*

Jos et saa selville ongelmaa, älä epäröi ottaa yhteyttä meihin: **servicedesk@csc.fi**. Muista liittää mukaan olennaiset tiedot, kuten mitä ohjelmaa yritit ajaa ja millä palvelimella jne.