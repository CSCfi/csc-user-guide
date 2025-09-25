---
tags:
  - Free
catalog:
  name: BLAST
  description: Sequence similarity search tool for nucleotides and proteins
  description_fi: Sekvenssien samankaltaisuushakutyökalu nukleotideille ja proteiineille
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Puhti
---

# BLAST { #blast }

BLAST (Basic Local Alignment Search Tool) on yleisimmin käytetty sekvenssien homologiahakuohjelma. Kun annat kyselysekvenssin (nukleotidi tai proteiini), BLAST vertaa sitä sekvenssitietokantaan ja poimii esiin sekvenssit, joilla on merkittävä samankaltaisuus kyselyyn nähden. BLAST käyttää heuristista hakuprotokollaa, minkä ansiosta haku on hyvin nopea verrattuna ei-heuristisiin menetelmiin. Heuristiikat voivat kuitenkin johtaa siihen, ettei BLAST löydä kaikkia merkittäviä osumia.

NCBI-BLASTin komentoriviversio mahdollistaa kaikkien parametrien säätämisen, erikoismenetelmien kuten PSI-BLAST ja PHI-BLAST käytön sekä suurten aineistojen analysoinnin.

Puhtissa voit käyttää suurille kyselysekvenssijoukoille komentoa `pb` (Parallel Blast). `pb` jakaa suuren hakutehtävän useisiin samanaikaisesti ajettaviin alitöihin (lisää alla).

Yleisimmät BLAST-komennot ovat:

* `blastn` hakee osumia nukleotidisekvenssille nukleotiditietokannasta
* `blastp` hakee osumia proteiinisekvenssille proteiinitietokannasta
* `blastx` hakee osumia nukleotidisekvenssille proteiinitietokannasta
* `psiblast` tekee iteratiivisen haun proteiinisekvenssille proteiinitietokannasta
* `rpsblast` hakee osumia proteiinisekvenssille proteiiniprofiilitietokannasta
* `rpstblastn` hakee osumia nukleotidisekvenssille proteiiniprofiilitietokannasta
* `tblastn` hakee osumia proteiinisekvenssille nukleotiditietokannasta
* `tblastx` hakee osumia nukleotidisekvenssille nukleotiditietokannasta käyttäen sekä kysely- että tietokantasekvenssien proteiinikäännöksiä.

Muut BLAST-komennot

* `blastdbcmd` noutaa yhden sekvenssin tai sekvenssijoukon BLAST-tietokannoista
* `makeblastdb` luo uuden BLAST-tietokannan
* `blast_formatter` muotoilee uudelleen BLAST-arkistomuotoisen BLAST-tulostiedoston.

[TOC]

## License { #license }

Vapaasti käytettävissä ja avoimen lähdekoodin ohjelmisto, lisensoitu [GNU LGPLv2.1](https://www.gnu.org/licenses/old-licenses/lgpl-2.1.html) -lisenssillä.

## Available { #available }

* Puhti: 2.15.0
* Chipsterin graafinen käyttöliittymä


## Usage { #usage }

CSC:llä BLAST-hakuja voi suorittaa usealla tavalla:

* Chipster-alustaa käyttäen
* tavallisilla BLAST-komennoilla interaktiivisissa eräajoissa (`sinteractive -i`)
* eräajoina `pb`-komennolla Puhtissa

## Interactive usage in Puhti { #interactive-usage-in-puhti }

Käyttääksesi Puhtissa uusinta BLAST-versiota, anna ensin komento:

```bash
module load biokit
```

Käynnistä sitten interaktiivinen eräajojonoistunto komennolla:

```bash
sinteractive -i
```

Varaa 8 GiB muistia interaktiiviselle istunnollesi.

Tämän jälkeen voit käyttää yllä lueteltuja BLAST-komentoja. Esimerkiksi seuraava komento etsii proteiinisekvenssille homologisia sekvenssejä UniProt-tietokannasta.

```bash
blastp -query proteinseq.fasta -db uniprot -out result.txt
```

Voit käyttää valitsinta `-help` nähdäksesi, mitä komentorivivalitsimia tietylle BLAST-komennolle on saatavilla. Esimerkiksi

```bash
blastp -help
```

Esimerkiksi komento:  

```bash
blastp -query proteinseq.fasta -evalue 0.001 -db uniprot -outfmt 7 -out result.table
```

suorittaa saman haun kuin yllä, mutta e-arvon kynnys asetetaan arvoon 0.001 (`-evalue 0.001`) ja tulos tulostetaan taulukkomuodossa (`-outfmt 7`).

## Usage of pb (Parallel BLAST) at CSC { #usage-of-pb-parallel-blast-at-csc }

Jos kyselysekvenssien joukossa on alle 20 sekvenssiä, interaktiivinen eräajo on todennäköisesti tehokkain tapa tehdä haku. Jos taas kyselyjoukko sisältää satoja tai tuhansia sekvenssejä, Puhtin rinnakkaislaskentakyvykkyyden hyödyntäminen on tehokkaampaa. Tällaisiin massiivisiin BLAST-hakuihin voit käyttää `pb`-komentoa.

`pb` (Parallel BLAST) on tarkoitettu tilanteisiin, joissa kyselytiedosto sisältää suuren määrän sekvenssejä. Se jakaa tehtävän useisiin alitöihin, joita voidaan ajaa samanaikaisesti palvelimen resursseja tehokkaasti hyödyntäen. Suurille kyselyjoukoille `pb` voi nopeuttaa hakua jopa 50-kertaiseksi. Kaksi esimerkkikomentoa Puhtiin:

```bash
module load biokit
pb blastn -db nt -query 100_ests.fasta -out results.out
pb psiblast -db swiss -query protseqs.fasta -num_iterations 3 -out results.out
```

`pb blast` -komentoja voi ajaa interaktiivisesti Puhtin kirjautumissolmuilta. Sinun ei tarvitse itse luoda eräajotiedostoa: `pb` luo ja lähettää eräajon automaattisesti. Kun BLAST-ajo on käynnistetty, `pb` käynnistää prosessin, joka seuraa työn etenemistä. Koska suuren BLAST-työn ajaminen voi kestää pitkään, seurantaprosessin voi olla tarpeen sulkea. Se onnistuu painamalla `Ctrl-c`. Tämän jälkeen voit aloittaa muita tehtäviä tai kirjautua ulos Puhtista. BLAST-työt jatkavat suorittamista eräajojärjestelmässä.

Yhdistääksesi uudelleen `pb blast` -työhösi siirry scratch-hakemistoosi ja suorita komento:

```bash
blast_clusterrun
```

Tämä listaa keskeneräisten `pb blast` -töidesi väliaikaishakemistot. Voit katsoa BLAST-työsi työnumeron hakemiston nimestä. Käytä tätä numeroa `-jobid`-valitsimen kanssa määrittääksesi `pb blast` -työn, johon haluat kytkeytyä uudelleen.

```bash
blast_clusterrun -jobid some-number
```

## Using own BLAST databases with pb { #using-own-blast-databases-with-pb }

`pb` mahdollistaa myös BLAST-hakujen ajamisen omia fasta-muotoisia sekvenssijoukkoja vastaan. Tämä tehdään korvaamalla valitsin `-db` valitsimella `-dbnuc` (nukleotideille) tai `-dbprot` (proteiineille). Esimerkki:

```bash
pb blastn -dbnuc my_seq_set.fasta -query querys.fasta -out results.out
```

Jos tietokanta on suuri, BLAST-indeksien rakentaminen voi vaatia yli 1 GB muistia (se on Puhtin kirjautumissolmujen työkohteille asetettu muistiraja). Tällöin voit lähettää työn interaktiivisesta eräajosta (esim. 8 GB muistilla).

## Using taxonomy to focus the search { #using-taxonomy-to-focus-the-search }

Yleisluonteiset NCBI BLAST -tietokannat kuten _NT_ tai _NE_ ovat kasvaneet hyvin suuriksi, mikä hidastaa hakuja Puhtissa. Jos voit rajata hakusi näiden tietokantojen osajoukkoon, haku nopeutuu ja epäolennaiset osumat karsiutuvat.

BLAST+ 2.15.0 -versiosta alkaen BLAST+:n komentorivisovellukset tukevat uutta ominaisuutta: ne hyväksyvät ei-lehtitason taxID:t (eli taksonit yli lajitason, kuten kädelliset). Esimerkiksi rajataksesi haun _NR_-tietokannan lintusekvensseihin (Taxonomy ID: 8782) voit käyttää komentoa

```bash
pb blastp -db nr - query test.fasta -taxids 8782 -out test.res
```

Jos tiedät käyttäväsi tiettyä _NR_- tai _NT_-tietokannan osajoukkoa useita kertoja, on tehokkaampaa suodattaa kyseiset sekvenssit kerran erilleen ja indeksoida oma tietokanta suodatetuista sekvensseistä. Voit käyttää komentoa `blastdbcmd` suodattaaksesi tietyn taksonomisen ryhmän _NR_- tai _NT_-tietokannoista.

Esimerkiksi kaikki lintusekvenssit voidaan noutaa _NR_-tietokannasta komennolla:

```bash
blastdbcmd -taxids 8782 -db nr -dbtype prot -out nrbirds.fasta -target_only
```

Syntynyt fasta-tiedosto voidaan indeksoida BLAST-hakuja varten komennolla `makeblastdb`.

```bash
makeblastdb -in nrbirds.fasta -dbtype prot
```

Käyttääksesi omaa tietokantaa sinun tulee asettaa ympäristömuuttuja `BLASTDB` osoittamaan hakemistoon, jossa indeksit sijaitsevat. Jos indeksit ovat esimerkiksi hakemistossa `my_blastdb` projektin `project_20012345` scratch-alueella, muuttuja asetetaan komennolla:

```bash
export BLASTDB=/scrartch/project_20012345/my_blastdb
```

Nyt voit käyttää omaa tietokantaasi BLAST-haussa:

```bash
pb blastp -db nrbirds.fasta - queryquery.fasta -out bird-only-hits.res
```

## Using genome data from Ensembl with pb { #using-genome-data-from-ensembl-with-pb }

`pb`-komento osaa myös noutaa automaattisesti lajikohtaisen aineiston Ensembl- tai Ensembl Genomes -palvelimilta ja käyttää sitä hakutietokantana. Tämä tehdään korvaamalla valitsin `-db` valitsimella `-ensembl_dna` (hakee genomin DNA:n), `-ensembl_cdna` (hakee cDNA-sekvenssit) tai `-ensembl_prot` (hakee proteiinisekvenssit). Lajin latinankielinen nimi tai taksonomiaindeksi annetaan Ensembl-valintojen argumentiksi. Lajin nimessä tulee käyttää alaviivaa (`_`) välilyönnin sijasta.

Esimerkiksi vertaillaksesi nukleotidisekvenssijoukon ihmisen genomia vastaan voit käyttää komentoa:

```bash
pb blastn -query dna_fargments.fasta -ensembl_dna homo_sapiens -out human_hits.txt
```

Vertaillaksesi samat DNA-fragmentit kanan genomista ennustettuja proteiinisekvenssejä vastaan voit käyttää komentoa:

```bash
pb tblastn -query dna_fargments.fasta -ensembl_prot gallus_gallus -out chicken_hits.txt
```

Näet Ensemblin ja Ensembl Genomes -tietokantojen saatavilla olevat lajilistaukset komennolla:

```bash
ensemblfetch.sh -names
```

Alla on luettelo BLAST-tietokannoista, joita CSC ylläpitää palvelimillaan.

| **Nimi          | Tietokanta                                             | Lähdetiedosto**                                               |
|-----------------|--------------------------------------------------------|---------------------------------------------------------------|
| **Nukleotidit** |                                                                                               |
| nt              | NCBI:n ei-redundanttinen nukleotiditietokanta          | ftp://ftp.ncbi.nih.gov/blast/db/FASTA/                        |
| refseq          | NCBI RefSeq RNA -tietokanta                            | ftp://ftp.ncbi.nih.gov/refseq/release/complete/               |
| refseq_con      | NCBI RefSeq -ihmisen kontigit                          | ftp://ftp.ncbi.nih.gov/refseq/H_sapiens/H_sapiens/            |
|                 |                                                        |                                                               |
| **Proteiinit**  |                                                        |                                                               |
| nr              | NCBI:n ei-redundanttinen proteiinitietokanta           | ftp://ftp.ncbi.nih.gov/blast/db/FASTA/                        |
| pdb_v5          | PDB:n proteiinirakennetietokanta                       | ftp://ftp.rcsb.org/pub/pdb/derived_data/                      |
| swiss           | UniProt/Swiss-tietokanta                               | ftp://ftp.ebi.ac.uk/pub/databases/uniprot/knowledgebase/      |
| trembl          | UniProt/TrEMBL-tietokanta                              | ftp://ftp.ebi.ac.uk/pub/databases/uniprot/knowledgebase/      |
| uniprot         | UniProt Swiss ja TrEMBL                                |   |
| uniref100       | UniRef100-tietokanta                                   | ftp://ftp.ebi.ac.uk/pub/databases/uniprot/uniref/uniref100/   |
| uniref90        | UniRef90-tietokanta                                    | ftp://ftp.ebi.ac.uk/pub/databases/uniprot/uniref/uniref90/    |
| uniref50        | UniRef50-tietokanta                                    | ftp://ftp.ebi.ac.uk/pub/databases/uniprot/uniref/uniref50/    |
| **Ensembl-genomit** | Valitse jokin laji `pb`-valinnoilla: `-ensembl_dna`, `-ensembl_cdna` tai `-ensembl_pep` | ftp://ftp.ensembl.org/   |

## Support { #support }

[Ota yhteyttä CSC Service Deskiin](../support/contact.md) saadaksesi teknistä tukea.

## More information { #more-information }

Lisätietoja BLASTista löytyy [NCBIn BLAST-sivulta](https://blast.ncbi.nlm.nih.gov/Blast.cgi).