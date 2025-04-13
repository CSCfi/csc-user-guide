
# Allaksen käyttö eräajoissa {#using-allas-in-batch-jobs}

Allas-yhteyden avaava `allas-conf`-komento tarjoaa kahdeksan tunnin voimassa olevan yhteyden. Interaktiivisessa käytössä tämä kahdeksan tunnin rajoitus ei ole ongelmallinen, koska _allas-conf_ voidaan suorittaa uudelleen yhteyden voimassaolon pidentämiseksi.

Eräajoissa tilanne on kuitenkin erilainen, sillä eräajon suorittaminen voi kestää useita päiviä, ja joissakin tapauksissa saattaa kestää yli kahdeksan tuntia ennen kuin työ edes alkaa. Näissä tapauksissa Allas-yhteys tulisi avata komennolla:
```text
allas-conf -k 
```
Yllä oleva komento tulisi suorittaa siinä shell-istunnossa, jota aiot käyttää eräajon käynnistämiseen. Komennossa valinta `-k` tarkoittaa, että _allas-conf_ varten syötetty salasana tallennetaan ympäristömuuttujaan `$OS_PASSWORD`. Tämän muuttujan ollessa määritettynä ei salasanaa tarvitse määritellä uudelleen suoritettaessa _allas-conf_ uudelleen _-k_ valinnalla ja Allakseen liittyvällä projektinimellä. Projektinimen voi määritellä joko eksplisiittisesti:
```text  
allas-conf -k project_2012345
```
Tai käyttää muuttujaa $OS_PROJECT_NAME, joka määritettiin, kun yhteys avattiin ensimmäisen kerran:
```text
allas-conf -k $OS_PROJECT_NAME
```
Yllä olevat kaksi komentoa luovat nyt Allas-yhteyden kahdeksaksi tunniksi ilman käyttäjän kehotepyyntöjä.

Huomaa, että jos kirjoitat salasanasi väärin käytettäessä _-k_ valintaa, sinun on käytettävä `unset` komentoa *OS_PASSWORD* muuttujan nollaamiseksi ennen kuin voit yrittää uudelleen:
```text
unset OS_PASSWORD
```
Jotta automatisoitu yhteyden muodostaminen eräajoissa onnistuisi, sinun on lisättävä `-f` valinta komentoon tiettyjen sisäisten tarkastusten ohittamiseksi, jotka eivät ole yhteensopivia eräajojen kanssa. Lisäksi _allas-conf_ on vain aliaksena olevalle _source_-komennolle, joka lukee Allas-konfiguraatioskriptiä `allas_conf`. Tämä aliaskomento ei ole käytettävissä eräajoissa, joten _allas-conf_:n sijasta sinun on käytettävä komentoa:

Puhti:
```text
source /appl/opt/csc-cli-utils/allas-cli-utils/allas_conf -f -k $OS_PROJECT_NAME
```
Mahti:
```text
source /appl/opt/csc-tools/allas-cli-utils/allas_conf -f -k $OS_PROJECT_NAME
```

Näin ollen, kun avaat Allas-yhteyden komennolla
```text
module load allas
allas-conf -k
```
Voit lisätä yllä mainitut source-komennot eräajosi skriptiin varmistaaksesi, että Allas-yhteys on voimassa tarvittaessa.

*A-komentoihin* (_a-put_, _a-get_, _a-list_, _a-delete_) tämä ominaisuus on sisällytetty, joten konfiguraatiokomentoja ei tarvitse lisätä eräsuoritusskriptiin, mutta on silti muistettava suorittaa `allas-conf -k` ennen työn lähettämistä:
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

#lataa data
a-get 178-data-bucket/dataset34/data2.txt.zst

#tee analyysi
my_analysis_command -in dataset34/data2.txt   -outdir results34

#lataa tulokset
a-put -b 178-data-bucket results34
```

Jos käytät _rclone_ tai _swift_ a-komentojen sijasta, sinun on lisättävä _source_-komennot skriptiisi. Tällöin eräajon skripti Puhtissa voisi näyttää tältä:
```text
#!/bin/bash
#SBATCH --job-name=my_allas_job
#SBATCH --account=project_2012345
#SBATCH --time=48:00:00
#SBATCH --mem-per-cpu=1G
#SBATCH --partition=small
#SBATCH --output=allas_output_%j.txt
#SBATCH --error=allas_errors_%j.txt

#varmista, että yhteys Allakseen on auki
source /appl/opt/csc-cli-utils/allas-cli-utils/allas_conf -f -k $OS_PROJECT_NAME

#lataa syötteet
rclone copy allas:178-data-bucket/dataset34/data2.txt ./

#tee varsinainen analyysi
my_analysis_command -in dataset34/data2.txt   -outdir results34

#varmista, että yhteys Allakseen on auki
source /appl/opt/csc-cli-utils/allas-cli-utils/allas_conf -f -k $OS_PROJECT_NAME

#palauta tulokset allakseen
rclone copyto results34 allas:178-data-bucket/
```
Mahdissa muista käyttää lähteenä `/appl/opt/csc-tools/allas-cli-utils/allas_conf` sen sijaan, että käyttäisit `/appl/opt/csc-cli-utils/allas-cli-utils/allas_conf` kaikissa paikoissa, joissa sinun on varmistettava yhteyden avautuminen.
