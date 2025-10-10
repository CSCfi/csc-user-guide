# Tietojen hallinta Puhtin ja Mahtin scratch-levyillä { #managing-data-on-puhti-and-mahti-scratch-disks }

Tärkeä tehtävä kaikille Puhtin ja Mahtin käyttäjille on hallita, mitä dataa on projektikansioissa `scratch`-alueella. Nämä on tarkoitettu vain väliaikaiseksi tallennustilaksi aktiivisesti käytössä olevalle datalle. Kaikki muu data tulisi poistaa tai siirtää muihin paremmin soveltuviin tallennusjärjestelmiin. Käyttäjien ei odoteta käyttävän koko kiintiötään; enimmäiskiintiö on tarkoitettu vain lyhytaikaisiin piikkeihin.

Huomaa myös, että:

* Lustre-rinnakkaistiedostojärjestelmän suorituskyky heikkenee, kun yli noin 70 % levytilasta on käytössä, ja mitä täydemmäksi levyt tulevat, sitä hitaammaksi suorituskyky muuttuu. CSC on myöntänyt enemmän kiintiötä kuin fyysistä tilaa on käytettävissä, joten kaikilla käyttäjillä ei ole edes mahdollista käyttää `scratch`-kansioitaan pidempiaikaiseen säilytykseen.
* `scratch`-levyalueesta ei ole **varmuuskopioita**. Älä luota siihen kaiken tutkimusdatan säilyttämisessä.
* Tiedostojen poistaminen voi pienentää projektisi Storage BU -kulutusta, koska sinua [laskutetaan](../../computing/hpc-billing.md#scratch-disk-billing) yli 1 TiB:n levytilan käytöstä.

Pyydämme kaikkia käyttäjiä auttamaan levytilan käytön pitämisessä hallittavana ja suorituskyvyn kohtuullisena. Tee seuraavat toimet:

* **Poista tiedostot**, joita projektisi `scratch`-kansiossa ei enää tarvita. Huomaa, että emme voi palauttaa vahingossa poistettuja tiedostoja, joten toimi varoen!
* **Pakkaa tiedostot**, jos se pienentää tiedostokokoa. ASCII-tekstitiedostot pakkaantuvat yleensä hyvin. Kokeile ensin yhdellä tiedostolla. Jos koko pienenee 50 %, jatka ja pakkaa kaikki vastaavat tiedostot. [Katso täältä saatavilla olevat pakkaustyökalut](env-guide/packing-and-compression-tools.md).
* **Siirrä tiedostot**, jotka eivät ole aktiivisessa käytössä nyt, mutta joiden pitää olla saatavilla myöhemmin projektin aikana. Tyypillinen malli on siirtää tiedostot [Allakseen](../../data/Allas/index.md). Suosittelemme käyttämään [a-tools](../../data/Allas/using_allas/a_commands.md) -työkaluja pienten ja keskisuurten datasiirtojen tekemiseen, erityisesti silloin, kun sinulla on suuri määrä pieniä tiedostoja. Nämä työkalut tekevät Allaksen käytöstä turvallisempaa ja voivat helpottaa datan hallintaa. Hyvin suuriin datasiirtoihin suosittelemme [rclonea](../../data/Allas/using_allas/rclone.md). Datan siirtämisen opas löytyy täältä: [Allas HPC -opastus](../../data/Allas/allas-hpc.md).
* **Arkistoi tiedostot**, joiden tulee olla saatavilla pidempään kuin laskentaprojektien elinkaari. Vaihtoehtoja ovat esimerkiksi organisaatiosi omat tallennusjärjestelmät tai [IDA turvallinen tutkimusdatan säilytys](https://www.fairdata.fi/en/).

## Tietojen sijainnin tunnistaminen { #identifying-where-you-have-data }

Jos sinulla on suuri määrä tiedostoja, analysointi siitä, kuinka paljon dataa eri kansioissa on, voi olla aikaa vievää ja myös raskasta tiedostojärjestelmälle. Suosituksemme työkaluista, joilla voit tarkastella kansioiden datamääriä:

* **Vältä** käyttämästä `find`-optiota kuten `-size` tai vastaavia
* **Vältä** `du`-komentoa
* **Käytä** `lue` tai `lfs find --lazy`

CSC on kehittänyt likimääräisen työkalun nimeltä LUE (Lustre usage explorer) kansioiden datamäärien raportointiin. [Lue LUE:n dokumentaatio](../../support/tutorials/lue.md) ennen käyttöä. `lfs find --lazy` sisältää joitakin reunatapauksia, joissa se voi olla yhtä huono kuin `du` tai epäonnistua hiljaisesti antamaan oikeat kokotiedot. Aja `man lfs-find` saadaksesi lisäohjeita ja tietoa sen rajoituksista.

!!! Note
    Riippumatta siitä, mitä työkalua käytät, sinun ei tulisi koskaan yrittää listata tai käsitellä kaikki projektisi tai `scratch`-kansiosi tiedostot yhdellä komennolla. Suorita sen sijaan komentoja rajatuissa alihakemistoissa, joissa on rajoitettu määrä tiedostoja ja dataa. Käytetyn tilan kokonaismäärä on saatavilla komennolla `csc-workspaces`.

## Automaattinen tiedostojen poisto { #automatic-removal-of-files }

`scratch`-alueelta (ei `projappl`) poistetaan [käytännön](../../computing/usage-policy.md#disk-cleaning) mukaisesti tiedostoja, jotka ovat vanhempia kuin **180 päivää** (`scratch`-kiintiö alle 5 TiB) tai **90 päivää** (`scratch`-kiintiö 5 TiB tai enemmän), jotta levyllä säilyisi vain aktiivisesti käytössä olevaa dataa (toteutettu tällä hetkellä vain Puhtissa).

Seuraavassa siivouksessa poistettavat tiedostot on listattu niin sanotuissa "purgelistojen" tiedostoissa. Ne on jaettu projekteittain ja löytyvät Lustrielta jommasta kummasta alla olevista sijainneista. Vain projektiryhmien jäsenet pääsevät projektihakemistoihin. Jos projektisi on vasta luotu, sillä ei välttämättä vielä ole omaa alihakemistoa `purge_lists`-hakemistossa, jolloin se ei osallistu automaattiseen siivoukseen.

* `/scratch/purge_lists/<PROJECT NAME>/path_summary.txt`
* `/fmi/scratch/purge_lists/<PROJECT NAME>/path_summary.txt` (vain Puhtissa, FMI-projekteille)

Jos `path_summary.txt`-tiedostoa ei ole, projektissasi ei ollut siivouskriteereihin sopivia tiedostoja, eikä siitä poisteta mitään. Ilmoittaaksemme, että tiedosto puuttuu tarkoituksella, CSC sijoittaa projektisi purge_lists-alihakemistoon tiedoston nimeltä `nothing-to-remove-for-your-project`, joten tarkista myös tämän tiedoston olemassaolo.

Osana automaattista siivousprosessia tiedostojen nimiä muutetaan. Ennen siivouksen alkamista jokaisella mukaan kuuluvalla projektilla on tiedosto nimeltä `path_summary.txt`. Erityistapauksissa, joissa projekti on vapautettu tulevasta siivouksesta tai tarvitsee lisää aikaa tiedostojen siirtämiseen, ylläpitäjät nimeävät tiedoston uudelleen, yleensä muotoon `path_summary.txt-later-delete`. Kun projekti on käsitelty automaattisessa siivouksessa, tiedoston nimeksi muutetaan `path_summary.txt-stashed`. Nämä tiedostot ovat edelleen projektien luettavissa, jotta listaan voidaan viitata myös siivouksen jälkeen. Edellisen kierroksen tiedostot arkistoidaan, kun seuraava siivouskierros on alkamassa. Voit tarkistaa, onko projektisi purgelistaa päivitetty hiljattain, katsomalla tiedoston viimeisen muokkauspäivän. Alla olevassa esimerkissä tiedosto on muutaman kuukauden ikäinen, joten se on selvästi edelliseltä siivouskierrokselta:

```bash
$ stat -c %y /scratch/purge_lists/project_2001659/path_summary.txt-stashed
2023-05-23 00:35:28.000000000 +0300
$ date +%F
2023-08-04
```

Toinen tiedosto, joka lisätään jokaiseen projektin `purge_lists`-hakemistoon, on `total_size.txt`. Tämä tiedosto sisältää valmiiksi lasketun kokoarvion perustuen `path_summary.txt`-tiedostojen lukuihin. Tiedosto on olemassa jokaisessa projektissa ja luodaan automaattisesti purgelistojen muodostamisen yhteydessä. Tiedosto voi näyttää tältä:

```bash
$ cat /scratch/purge_lists/project_2001659/total_size.txt
Total size: 798343125192 bytes = 743.515 GiB = 0.726 TiB
```

Näiden tietojen avulla voit arvioida, kuinka paljon aikaa datan varmuuskopioiminen muualle saattaa vaatia, jos haluat säilyttää kaiken purgelistalla olevan datan Puhtin `scratch`-tiedostojärjestelmän ulkopuolella. Tiedostojärjestelmätyökalut, joita CSC käyttää poistettavien tiedostojen listan tuottamiseen, tuottavat melko laajoja ja vaikealukuisia tiedostoja. Käyttämällä seuraavassa luvussa kuvattua LCleaner-työkalua käyttäjät voivat saada oleellisen tiedon käyttäjäystävällisemmässä muodossa.

## LCleanerin käyttäminen automaattisesti poistettavien tiedostojen tarkistamiseen { #using-lcleaner-to-check-which-files-will-be-automatically-removed }

LCleaner on CSC:n kehittämä työkalu, jonka tarkoitus on auttaa sinua löytämään, mitä tiedostoja projektissasi on automaattisen poiston kohteena.

Aja `lcleaner --help` kirjautumissolmuilla nähdäksesi, mitä valintoja LCleaner tukee.

### LCleaner-esimerkkejä { #lcleaner-examples }

#### Tarkista, onko projektillasi path_summary.txt -tiedosto { #check-if-your-project-has-a-path_summary.txt-file }

Ensimmäiseksi kannattaa tarkistaa, onko projektillasi ylipäätään `path_summary.txt`-tiedostoa. Kaikilla projekteilla ei ole sellaista automaattisesti, vain niillä, joilla on jotain siivottavaa.

```bash
# Check if your project has a path_summary.txt file
my_project="project_2001659" # Replace with your own project name
ls "/scratch/purge_lists/${my_project:?}/"
# Or if you are in an FMI project on Puhti:
ls "/fmi/scratch/purge_lists/${my_project:?}/"
```

Jos näet hakemistossa `path_summary.txt`-tiedoston, jatka lukemista selvittääksesi, mitkä tiedostot ovat listalla. Jos taas löydät tiedoston `nothing-to-remove-for-your-project`, projektiisi ei sisälly automaattisesti poistettavia tiedostoja.

Jos haluat nopean, kopioi–liitä-tyyppisen ratkaisun, käytä alla olevaa pientä skriptiä:

```bash
# Check all of the projects you belong to in one go:

for g in $(/usr/bin/groups) ; do
  if [ -d "/scratch/$g" -a ! -L "/scratch/$g" ]; then
    dir="/scratch/purge_lists/$g" ;
  elif [ -d "/fmi/scratch/$g" ]; then
    dir="/fmi/scratch/purge_lists/$g";
  else
    continue;
  fi ;
  echo -n "- Project '$g': ";
  if [ ! -d "${dir:?}" ]; then
    echo "doesn't have a purge_lists subdirectory. No files will be removed.";
    continue;
  fi ;
  if [ -f "${dir:?}/path_summary.txt" ]; then
    echo "has files that will be removed." ;
  elif [ -f "${dir:?}/nothing-to-remove-for-your-project" ]; then
    echo "is not included in the automatic cleaning.";
  else
    echo "is unclear, based on this script. Check with Service desk what to do.";
  fi ;
done
```

#### Listaa tiedostosi { #list-your-files }

Saadaksesi yksinkertaisen listan kaikista poluista purgelistallasi, anna vain `path_summary.txt`-tiedoston polku argumenttina:

```bash
# List all files in your purge list:
lcleaner "/scratch/purge_lists/${my_project:?}/path_summary.txt"
```

Jos `path_summary.txt` on suuri (yli 100 MB), työkalun suorittaminen voi viedä aikaa. Voit säästää aikaa ja resursseja tallentamalla tuloksen ulostulotiedostoon:

```bash
# List all files in your purge list into an output file in your home folder:
lcleaner --out-file ~/purge_list "/scratch/purge_lists/${my_project:?}/path_summary.txt"

# Alternatively, you can redirect the standard output with the bash shell:
lcleaner "/scratch/purge_lists/${my_project:?}/path_summary.txt" > ~/purge_list

# Check the output with less, or your preferred text editor
less ~/purge_list
```

Jos haluat etsiä tiettyä tiedostoa tai hakemistoa, voit käyttää siihen `grep`-komentoa. Voit joko etsiä suoraan `path_summary.txt`-tiedostosta tai, jos tallensit `lcleaner`-tulosteen johonkin, kuten yllä, voit käyttää sitä tiedostoa.

```bash
# Search for directories to check if they are included in the purge list
my_project="project_2001659" # Replace with your own project name!
grep "/scratch/${my_project:?}/important-dir" "/scratch/purge_lists/${my_project:?}/path_summary.txt"
# Or search the purge_list if you saved it:
grep "/scratch/${my_project:?}/important-dir" ~/purge_list

# If there are no matches, grep will not print anything.
```

#### Löydä listan suurimmat tiedostot { #find-the-biggest-files-on-the-list }

LCleanerissa on valinta tiedostojen lajittelemiseksi koon mukaan. Valinta on `--sort-by-size`, ja se lajittelee aina laskevaan järjestykseen (eli suurimmat tiedostot ensin). Jos haluat nähdä tiedostojen koot niiden tulostuessa, käytä `--csv`-valintaa. Oletuksena tulostetaan vain tiedostopolut. Voit myös rajoittaa tulosteen sisältämään annetun määrän tiedostoja parametrilla `--limit N`, jossa `N` on haluamasi rivimäärä.

```bash
# Print the file paths to be purged in size order:
lcleaner --sort-by-size "/scratch/purge_lists/${my_project:?}/path_summary.txt"

# Print the 10 biggest files:
lcleaner --sort-by-size --limit 10 "/scratch/purge_lists/${my_project:?}/path_summary.txt"

# Print the 10 biggest files, and their sizes in bytes:
lcleaner --sort-by-size --limit 10 --csv "/scratch/purge_lists/${my_project:?}/path_summary.txt"
```

#### Poista puhdistuslistan tiedostot { #delete-your-purge-list-files }

Kannustamme poistamaan tarpeettomat tiedostot itse sen sijaan, että odottaisit automaattisen siivouksen tapahtuvan. Jos haluat poistaa kaikki `path_summary.txt`-tiedostossa listatut tiedostot, voit ajaa seuraavan komennon:

!!! warning-label
    **Tämän osion komennot poistavat tiedostojasi!** Varmista, että olet tarkistanut poistettavien tiedostojen listan huolellisesti! Varmista myös, että olet varmuuskopioinut haluamasi tiedostot (klusterin ulkopuolelle) ennen komentojen ajamista. Toiminto on peruuttamaton.

!!! Note
    Poistoprosessi voi kestää huomattavan kauan (useita tunteja riippuen tiedostomäärästä), joten on parasta käynnistää se `screen`- tai `tmux`-istunnossa, jotta voit katkaista SSH-yhteyden poistamisen jatkuessa taustalla.

```bash
# Start a screen session
screen
# Delete all of the files on your purge list:
# Replace the "/path/to/my/path_summary.txt" with the path to your project's path_summary.txt
lcleaner -0 /path/to/my/path_summary.txt | xargs -0 -n 50 rm -vf --
# Then you can press "Ctrl + a" and then "d" to disconnect from the screen and keep
# the deletion running in the background.
# Run "screen -r" to reattach your screen.
# Close the screen session by typing "exit" in the shell.
```

Jos haluat poistaa vain osan tiedostoista, esimerkiksi tietyn hakemiston sisältä, voit käyttää esimerkiksi tällaista komentoa:

```bash
# Delete only files on the list which are inside /scratch/$my_project/delete-this-dir/
screen lcleaner -0 /path/to/my/path_summary.txt | grep -zZ "/scratch/${my_project:?}/delete-this-dir/" | xargs -0 -n 50 rm -vf --
# Ctrl + a, d to detach from the screen.
```

#### LCleanerin tulostusmuodot { #lcleaner-output-formats }

Jos haluat nähdä poistettavien tiedostojen koot, voit käyttää joko JSON- tai CSV-muotoja. Huomaa, että jos haluat suorittaa useita tulostusmuotoja samanaikaisesti, sinun on myös määritettävä ulostulotiedoston polku. Parametrien `-0` tai `--nullbyte` käyttäminen tuottaa tiedostopolut null-merkillä eroteltuna, mikä voi olla hyödyllistä välttämään ongelmia tiedostonimien välilyöntien kanssa.

```bash
# Print your purge list as CSV output with file paths and sizes.
# Note that the CSV format also prints a header row.
lcleaner --csv "/scratch/purge_lists/${my_project:?}/path_summary.txt"

# Print your purge list as JSON output with file paths and sizes:
lcleaner --json "/scratch/purge_lists/${my_project:?}/path_summary.txt"
# TIP: You can pipe the output into the jq program to prettify the output.
# The dot at the end is a mandatory argument to jq.
lcleaner --json "/scratch/purge_lists/${my_project:?}/path_summary.txt" | jq .

# Output both JSON and CSV into purge_list.json and purge_list.csv:
lcleaner --json --csv --out-file purge_list "/scratch/purge_lists/${my_project:?}/path_summary.txt"

# Output file paths separated by null bytes:
lcleaner -0 "/scratch/purge_lists/${my_project:?}/path_summary.txt"
# Usually you will want to pipe null-byte-separated output into "xargs -0" and do some
# further processing with it. For example like this:
lcleaner -0 --limit 3 "/scratch/purge_lists/${my_project:?}/path_summary.txt" \
  | xargs -0 -Ifilepath echo "I should run: rm -vf 'filepath'"
```

Tulostusesimerkkejä:

```
# Plain text:
[westersu@puhti-login11 ~]$ lcleaner path_summary.txt | head -3
/scratch/westersu/my-old-files/file1
/scratch/westersu/my-old-files/file2
/scratch/westersu/my-old-files/file3

# CSV:
[westersu@puhti-login11 ~]$ lcleaner --csv path_summary.txt | head -4
"path","size"
"/scratch/westersu/my-old-files/file1","1704"
"/scratch/westersu/my-old-files/file2","452"
"/scratch/westersu/my-old-files/file3","4951"

# JSON, piped into jq:
[westersu@puhti-login11 ~]$ lcleaner --json path_summary.txt | jq .
{
  "lustre_files": [
    {
      "size": 1704,
      "path": "/scratch/westersu/my-old-files/file1"
    },
    ...
  ]
}

# Null byte xargs:
[westersu@puhti-login11 ~]$ lcleaner -0 --limit 3 path_summary.txt \
>   | xargs -0 -Ifilepath echo "I should run: rm -vf 'filepath'"
I should run: rm -vf '/scratch/westersu/my-old-files/file1'
I should run: rm -vf '/scratch/westersu/my-old-files/file2'
I should run: rm -vf '/scratch/westersu/my-old-files/file3'
```

### Huomioita LCleanerin käytöstä { #notes-on-lcleaner-usage }

Tässä osiossa kerrotaan asioista, jotka voivat olla hyvä tietää LCleanerin toiminnasta tai miksi yllä olevat komentoesimerkit on suunniteltu sellaisiksi kuin ne ovat.

- Joskus `lcleaner` tulostaa virheitä riveistä, joita se ei pystynyt jäsentämään. Jos virheitä on, lopussa tulostuu varoitus, joka kertoo, että havaittiin ainakin yksi virhe. Varoitukset ovat tyyliin: "We detected N errors during the execution. Please check the logs, for more information!" Virheilmoitukset kertovat, millä rivinumerolla ongelmallinen teksti oli, jotta voit tarkistaa sen käsin.
    - Vinkki: Tulostaaksesi vain tietyn rivin, esim. rivin 123 tiedostosta `path_summary.txt`, voit käyttää komentoa: `sed -n 123p /path/to/path_summary.txt`
- LCleanerin lokituksen talteen saamiseksi voit ohjata virhevirran (stderr) tiedostoon. Tämä voi olla hyödyllistä, jos kohtaat ongelmia ja haluat apua tilanteen vianmääritykseen.
    - `lcleaner --log-level debug path_summary.txt 2> ~/lcleaner-debug-$(date +%s).log`
- `-0`-valinnan käyttö sekä `lcleaner`- että `xargs`-komennon kanssa on suositeltavaa välttääksesi ongelmia tiedostonimien välilyöntien kanssa.
- LCleanerissa on myös joitakin ylläpitotoimintoja, joita ei ole tarkoitettu ja joissakin tapauksissa eivät toimikaan tavallisille käyttäjille. Kaikki, mikä mainitsee `--admin-mode`-lipun, voidaan turvallisesti sivuuttaa.

### LCleanerin vianmääritys { #troubleshooting-lcleaner }

Jos huomaat bugeja, ilmoita niistä [CSC Service Deskille](../contact.md).