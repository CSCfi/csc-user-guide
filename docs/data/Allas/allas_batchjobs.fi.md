# Allaksen käyttö ajotehtävissä {#using-allas-in-batch-jobs}

Allas-initialisointikomento `allas-conf` avaa Allas-yhteyden, joka on voimassa kahdeksan tuntia. 
Interaktiivisessa käytössä tämä kahdeksan tunnin rajoitus ei yleensä ole ongelmallinen, sillä _allas-conf_-komennon voi suorittaa uudelleen yhteyden voimassaoloajan pidentämiseksi.

Ajotehtävissä tilanne on eri, sillä ajotehtävä voi kestää useita päiviä, ja joissain tapauksissa saattaa kestää yli kahdeksan tuntia ennen kuin tehtävä edes käynnistyy. Näissä tapauksissa Allas-yhteys kannattaa avata komennolla:
```text
allas-conf -k 
```
Yllä oleva komento tulisi suorittaa siinä komentorivisessiossa, jota aiot käyttää ajotehtävän käynnistämiseen.
Komentorivissä `-k`-valitsin tarkoittaa, että _allas-conf_-ohjelmaan syötetty salasana tallennetaan ympäristömuuttujaan `$OS_PASSWORD`. Kun tämä muuttuja on asetettu, sinun ei tarvitse enää syöttää salasanaa uudelleen, kun suoritat _allas-conf_-komennon -k-valitsimella ja Allas-projektin nimellä. Projektin nimen voi antaa joko erikseen:
```text  
allas-conf -k project_2012345
```
Tai käyttää $OS_PROJECT_NAME -muuttujaa, joka määriteltiin yhteyttä ensimmäistä kertaa avattaessa:
```text
allas-conf -k $OS_PROJECT_NAME
```
Yllä olevilla kahdella komennolla avataan Allas-yhteys kahdeksaksi tunniksi ilman käyttäjän syötettä.

Huomaa, että jos kirjoitat salasanasi väärin käyttäessäsi _-k_-valitsinta, sinun täytyy suorittaa `unset`-komento *OS_PASSWORD*-muuttujan nollaamiseksi ennen kuin voit kokeilla uudelleen:
```text
unset OS_PASSWORD
```
Jotta voit käyttää automatisoitua yhteyden luontia ajotehtävissä, sinun tulee lisätä komennon perään valitsin `-f`, jolla ohitetaan eräät sisäiset tarkistukset, joita ajotehtävissä ei tarvita.
Lisäksi _allas-conf_ on vain alias _source_-komennolle, joka lukee Allaksen määritysskriptin `allas_conf`. Tämä alias ei ole käytettävissä ajotehtävissä, joten _allas-conf_-komennon sijaan sinun pitää käyttää komentoa:

Puhti:
```text
source /appl/opt/csc-cli-utils/allas-cli-utils/allas_conf -f -k $OS_PROJECT_NAME
```
Mahti:
```text
source /appl/opt/csc-tools/allas-cli-utils/allas_conf -f -k $OS_PROJECT_NAME
```

Kun Allas-yhteys on avattu komennoilla
```text
module load allas
allas-conf -k
```
voit lisätä yllä mainitut source-komennot ajotehtäväskriptiisi varmistaaksesi, että Allas-yhteys on voimassa tarvittaessa.

*a-komentoja* (_a-put_, _a-get_, _a-list_, _a-delete_) käytettäessä tämä ominaisuus on sisäänrakennettu, joten määrityskomentoja ei tarvitse lisätä ajotehtäväskriptiin, mutta muista silti ajaa `allas-conf -k` ennen työn lähettämistä jonoon:
```text
module load allas
allas-conf -k
sbatch my_long_job.sh
```
Missä _my_long_job.sh_ voisi näyttää tältä:

```text
#!/bin/bash
#SBATCH --job-name=my_allas_job
#SBATCH --account=project_2012345
#SBATCH --time=48:00:00
#SBATCH --mem-per-cpu=1G
#SBATCH --partition=small
#SBATCH --output=allas_output_%j.txt
#SBATCH --error=allas_errors_%j.txt

#ladataan data
a-get 178-data-bucket/dataset34/data2.txt.zst

#suoritetaan analyysi
my_analysis_command -in dataset34/data2.txt   -outdir results34

#tulosten siirto Allakseen
a-put -b 178-data-bucket results34
```

Jos käytät _rclone_- tai _swift_-työkaluja a-komentojen sijaan, sinun tulee lisätä _source_-komennot skriptiin. Tässä tapauksessa Puhtin ajotehtäväskripti voisi näyttää tältä:
```text
#!/bin/bash
#SBATCH --job-name=my_allas_job
#SBATCH --account=project_2012345
#SBATCH --time=48:00:00
#SBATCH --mem-per-cpu=1G
#SBATCH --partition=small
#SBATCH --output=allas_output_%j.txt
#SBATCH --error=allas_errors_%j.txt

#varmistetaan yhteys Allakseen
source /appl/opt/csc-cli-utils/allas-cli-utils/allas_conf -f -k $OS_PROJECT_NAME

#ladataan syötedata
rclone copy allas:178-data-bucket/dataset34/data2.txt ./

#suoritetaan varsinainen analyysi
my_analysis_command -in dataset34/data2.txt   -outdir results34

#varmistetaan yhteys Allakseen
source /appl/opt/csc-cli-utils/allas-cli-utils/allas_conf -f -k $OS_PROJECT_NAME

#tulosten siirto Allakseen
rclone copyto results34 allas:178-data-bucket/
```
Mahtilla muista käyttää `source /appl/opt/csc-tools/allas-cli-utils/allas_conf` kaikkialla, missä yhteyden avaus Allakseen tulee varmistaa, `source /appl/opt/csc-cli-utils/allas-cli-utils/allas_conf` sijaan.