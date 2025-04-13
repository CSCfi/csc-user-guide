# Puhti ja Mahti scratch-levyjen datan hallinta {#managing-data-on-puhti-and-mahti-scratch-disks}

Tärkeä tehtävä kaikille Puhti ja Mahti -käyttäjille on hallinnoida, mitä dataa säilytetään projektikansioissa `scratch`:ssä. Nämä ovat tarkoitettu vain väliaikaiseksi säilytystilaksi aktiiviselle datalle. Kaikki muu data tulisi poistaa tai siirtää muihin sopivampiin tallennusjärjestelmiin. Käyttäjien ei odoteta käyttävän koko kiintiötään, maksimikiintiö on tarkoitettu vain lyhytaikaisiin tarpeisiin.

Huomioi myös, että:

* Lustre-rinnakkaistiedostojärjestelmän suorituskyky alkaa laskea, kun yli noin 70 % levystilasta on käytössä, ja levyjen täyttyessä enemmän suorituskyky laskee. CSC on varannut enemmän kiintiöitä kuin tilaa on, joten kaikilla käyttäjillä ei ole edes mahdollista käyttää `scratch`-kansioitaan pidemmän aikavälin tallennukseen.
* `scratch`-levyalueella **ei ole varmuuskopioita**. Älä luota siihen, että se tallentaisi kaikki tutkimusdatanne.
* Tiedostojen poistaminen saattaa vähentää projektinne BU-kulutusta, sillä ylimääräisestä yli 1 TiB:n levykäytöstä laskutetaan.

Pyydämme kaikkia käyttäjiä auttamaan pitämään levyn käyttö hallittavissa ja suorituskyky kohtuullisena. Ole hyvä ja suorita seuraavat tehtävät:

* **Poista tiedostoja**, jotka eivät ole enää tarpeellisia projektinne `scratch`-kansiossa. Huomaa, että emme voi palauttaa vahingossa poistamiasi tiedostoja, joten ole varovainen näitä toimintoja suorittaessasi!
* **Pakkaa tiedostoja**, jos se pienentää tiedostokokoa. Ascii-tekstiedostot pakkaantuvat yleensä hyvin. Testaa ensin yhdellä tiedostolla. Jos tiedostokoko pienenee 50 %, jatka kaikkien samankaltaisten tiedostojen pakkaamista. [Katso täältä saatavilla olevat pakkaustyökalut](env-guide/packing-and-compression-tools.md).
* **Siirrä tiedostoja**, joita ei käytetä aktiivisesti nyt, mutta joita tarvitaan myöhemmin projektin aikana. Tyypillinen malli on siirtää tiedostot [Allakseen](../../data/Allas/index.md). Suosittelemme käyttämään [a-tools](../../data/Allas/using_allas/a_commands.md) pienten ja keskikokoisten datasiirtojen tekemiseen, erityisesti kun sinulla on suuri määrä pieniä tiedostoja. Nämä työkalut tekevät Allaksen käytöstä turvallisempaa ja voivat helpottaa datanhallintaasi. Hyvin suurille datasiirroille suosittelemme käyttämään [rclone](../../data/Allas/using_allas/rclone.md). Datan siirtämiseen löytyy [allas-esimerkit](../../data/Allas/allas-examples.md) -tutoriaali.
* **Arkistoi tiedostot**, jotka pitäisi olla saatavilla pidempään kuin laskentaprojektien elinaika. Vaihtoehtoina voivat olla esimerkiksi organisaatiosi omat tallennusjärjestelmät tai [IDA-turvasäilytys tutkimusaineistoille](https://www.fairdata.fi/en/).

## Datan sijainnin tunnistaminen {#identifying-where-you-have-data}

Jos sinulla on suuri määrä tiedostoja, datan analysointi eri kansioissa voi olla aikaa vievää ja myös raskasta tiedostojärjestelmälle. Suosituksemme työkaluista, jotka voivat näyttää kuinka paljon dataa on kansioissa:

* Vältä käyttämästä `find`-valintoja kuten `-size` tai vastaavia
* Vältä käyttämästä `du`
* Käytä `lue` tai `lfs find --lazy`

CSC on kehittänyt karkean työkalun nimeltä LUE (Lustre usage explorer) kansioiden datamäärän raportointiin. [Lue dokumentaatio LUE:sta](../../support/tutorials/lue.md) ennen sen käyttöä. `lfs find --lazy` saattaa joissain tapauksissa käyttäytyä samalla tavalla kuin `du` tai epäonnistua hiljaisesti oikean koon saamisessa. Suorita `man lfs-find` saadaksesi lisäohjeita ja tietoa sen rajoituksista.

!!! Huomio
    Riippumatta siitä, mitä työkalua käytät, sinun ei tulisi koskaan yrittää listata tai käsitellä kaikkia tiedostoja projektisi tai `scratch`-kansiossasi yhdellä komennolla. Sen sijaan sinun tulisi suorittaa komennot tietyissä alikansioissa, joissa on rajattu määrä tiedostoja ja dataa. Käytetyn datan kokonaismäärä on saatavilla `csc-workspaces`-komennolla.

## Tiedostojen automaattinen poistaminen {#automatic-removal-of-files}

Vanhempien kuin 180 päivää vanhojen tiedostojen poistamisesta `scratch`-alueelta (ei `projappl`) on sääntö, jotta levyllä säilytetään vain aktiivisesti käytössä olevaa dataa (tällä hetkellä toteutettu vain Puhtissa).

Seuraavassa siivouksessa poistettavat tiedostot on listattu niin sanotuissa "purkulistoissa". Nämä on jaettu projekteittain ja ne löytyvät Lustresta alla olevista sijainneista. Vain projektiryhmien jäsenet voivat päästä projektihakemistoihin. Jos projektinne on vasta luotu, projektillanne ei ehkä ole vielä omaa alihakemistoa `purge_lists`-hakemistossa, jolloin se ei osallistu automaattiseen siivoukseen.

* `/scratch/purge_lists/<PROJEKTIN_NIMI>/path_summary.txt`
* `/fmi/scratch/purge_lists/<PROJEKTIN_NIMI>/path_summary.txt` (vain Puhti, FMI-projekteille)

Jos `path_summary.txt`-tiedostoa ei ole, projektillanne ei ollut siivouskriteerit täyttäviä tiedostoja, eikä mitään tulla poistamaan. Jos tiedosto puuttuu tarkoituksella, CSC asettaa projektille tiedoston nimeltä `nothing-to-remove-for-your-project` projektinne purge_lists-alihakemistoon, joten tarkista tämän tiedoston olemassaolo.

Ohjelmoidun siivousprosessin yhteydessä tiedostojen nimet muuttuvat. Ennen siivouksen alkamista jokaisella suursiivoukseen osallistuvalla projektilla on tiedosto nimeltä `path_summary.txt`. Erityistapauksissa, joissa projekti on vapautettu tulevasta siivouksesta tai tarvitsee enemmän aikaa tiedostojen siirtämiseen, järjestelmänvalvojat nimeävät tiedoston uudelleen, yleensä muotoon `path_summary.txt-later-delete`. Kun projekti on käsitelty automaattisessa siivouksessa, tiedosto nimetään muotoon `path_summary.txt-stashed`. Nämä tiedostot ovat edelleen luettavissa projekteille, jotta listaa voi käyttää referenssinä myös siivouksen jälkeen. Edellisen kierroksen tiedostot arkistoidaan, kun uusi siivouskierros on alkamassa. Voit tarkistaa, onko projektinne purkulista päivitetty hiljattain tarkistamalla sen viimeisen muokkauspäivämäärän. Alla olevassa esimerkissä tiedosto on muutaman kuukauden vanha, joten se on selvästi edellisen siivouskierroksen ajalta:

```bash
$ stat -c %y /scratch/purge_lists/project_2001659/path_summary.txt-stashed
2023-05-23 00:35:28.000000000 +0300
$ date +%F
2023-08-04
```

Toinen tiedosto, joka on lisätty jokaiseen projektin `purge_lists`-hakemistoon, on `total_size.txt`-tiedosto. Tämä tiedosto sisältää ennalta lasketun kokoarvion, joka perustuu `path_summary.txt`-tiedostojen sisältöön. Tämä tiedosto on olemassa jokaiselle projektille, ja se luodaan automaattisesti, kun purkulistat luodaan. Tiedosto voi näyttää tältä:

```bash
$ cat /scratch/purge_lists/project_2001659/total_size.txt
Total size: 798343125192 bytes = 743.515 GiB = 0.726 TiB
```

Tällä tiedolla voit arvioida, kuinka paljon aikaa voisi tarvita datan varmuuskopioimiseen muualle, jos haluat säilyttää kaiken puhtilistan ulkopuolella Puhti `scratch`-tiedostojärjestelmästä.
Tiedostojärjestelmätyökalut, joita CSC käyttää poistettavien tiedostojen listan luomiseksi, tuottavat melko yksityiskohtaisia ja vaikealukuisia tiedostoja. Käyttämällä seuraavassa osassa kuvattua LCleaner-työkalua, käyttäjät voivat saada asiaankuuluvaa tietoa helpommin luettavassa muodossa.

## LCleaner:in käyttö tiedostojen tarkistamiseen, jotka poistetaan automaattisesti {#using-lcleaner-to-check-which-files-will-be-automatically-removed}

LCleaner on CSC:n kehittämä työkalu, jonka tarkoitus on auttaa sinua selvittämään, mitkä projektisi tiedostot on tarkoitettu automaattisesti poistettaviksi.

Suorita `lcleaner --help` login-solmukoilla nähdäksesi, mitä vaihtoehtoja LCleaner tukee.

### LCleaner-esimerkkejä {#lcleaner-examples}

#### Tarkista, onko projektillasi path_summary.txt-tiedostoa {#check-if-your-project-has-a-path-summary-txt-file}

Ensimmäinen asia, joka kannattaa tarkistaa, on, onko projektillasi todella `path_summary.txt`-tiedosto. Kaikilla projekteilla ei ole automaattisesti sellaista, vain niillä, joilla on jotain siivottavaa.

```bash
# Tarkista, onko projektillasi path_summary.txt-tiedosto
my_project="project_2001659" # Korvaa omalla projektin nimelläsi
ls "/scratch/purge_lists/${my_project:?}/"
# Tai jos olet FMI-projektissa Puhtissa:
ls "/fmi/scratch/purge_lists/${my_project:?}/"
```

Jos näet `path_summary.txt`-tiedoston hakemistossa, lue eteenpäin selvittääksesi, mitkä tiedostot ovat listassa. Jos kuitenkin löydät tiedoston nimeltä `nothing-to-remove-for-your-project`, projektillasi ei ole mitään, mikä tulee automaattisesti poistettavaksi.

Jos haluat nopean, kopioitavan ratkaisun, käytä alla olevaa pientä skriptiä:

```bash
# Tarkista kaikki projektit, joihin kuulut, yhdellä kertaa:

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
    echo "ei ole purge_lists-alihakemistoa. Tiedostoja ei poisteta.";
    continue;
  fi ;
  if [ -f "${dir:?}/path_summary.txt" ]; then
    echo "on tiedostoja, jotka poistetaan." ;
  elif [ -f "${dir:?}/nothing-to-remove-for-your-project" ]; then
    echo "ei kuulu automaattiseen siivoukseen.";
  else
    echo "tilanne on epäselvä tämän skriptin perusteella. Tarkista Service deskin kanssa, mitä tehdä.";
  fi ;
done
```

#### Listaa tiedostosi {#list-your-files}

Jos haluat yksinkertaisen listan kaikista tiedostopolkuista purkulistassasi, anna yksinkertaisesti `path_summary.txt`-tiedoston polku LCleanerille argumentiksi:

```bash
# Listaa kaikki tiedostot purkulistassasi:
lcleaner "/scratch/purge_lists/${my_project:?}/path_summary.txt"
```

Jos `path_summary.txt`-tiedostosi on suuri (yli 100 MB kokoinen), työkalun suorittaminen saattaa kestää jonkin aikaa. Voit säästää aikaa ja resursseja tallentamalla tuloksen tiedostoon:

```bash
# Listaa kaikki tiedostot purkulistassasi tulostiedostoon kotihakemistoosi:
lcleaner --out-file ~/purge_list "/scratch/purge_lists/${my_project:?}/path_summary.txt"

# Vaihtoehtoisesti voit ohjata standardilähdön bash-komentotulkin avulla:
lcleaner "/scratch/purge_lists/${my_project:?}/path_summary.txt" > ~/purge_list

# Tarkista tulos less-ohjelmalla tai suosikkitekstieditorillasi
less ~/purge_list
```

Jos haluat etsiä tiettyä tiedostoa tai hakemistoa, voit käyttää `grep`-komentoa saavuttaaksesi tämän. Voit joko etsiä suoraan `path_summary.txt`-tiedostosta tai, jos tallensit LCleanerin tulostuksen jonnekin yllä olevien komentojen avulla, voit käyttää tuota tiedostoa.

```bash
# Etsi hakemistoja tarkistaaksesi, ovatko ne mukana listassa
my_project="project_2001659" # Korvaa omalla projektin nimelläsi!
grep "/scratch/${my_project:?}/important-dir" "/scratch/purge_lists/${my_project:?}/path_summary.txt"
# Tai etsi purge_list-tiedostosta, jos talletit sen:
grep "/scratch/${my_project:?}/important-dir" ~/purge_list

# Jos osumia ei löydy, grep ei tulosta mitään.
```

#### Löydä suurimmat tiedostot listassa {#find-the-biggest-files-on-the-list}

LCleanerilla on vaihtoehto lajitella tiedostot koon mukaan. Tähän vaihtoehtoon viitataan nimellä `--sort-by-size`, ja se lajitellaan aina laskevaan järjestykseen (eli suurimmat tiedostot ensin). Jos haluat nähdä tiedostojen koot, kun ne tulostetaan, käytä vaihtoehtoa `--csv`. Oletuksena tulostetaan vain tiedostopolut. Voit myös rajoittaa tulosteen tiettyyn tiedostojen lukumäärään `--limit N` -parametrilla, missä N on näytettävien rivien lukumäärä.

```bash
# Tulosta poistettavien tiedostojen polut kokojärjestyksessä:
lcleaner --sort-by-size "/scratch/purge_lists/${my_project:?}/path_summary.txt"

# Tulosta 10 suurinta tiedostoa:
lcleaner --sort-by-size --limit 10 "/scratch/purge_lists/${my_project:?}/path_summary.txt"

# Tulosta 10 suurinta tiedostoa, sekä niiden koot tavuina:
lcleaner --sort-by-size --limit 10 --csv "/scratch/purge_lists/${my_project:?}/path_summary.txt"
```

#### Poista purkulistasi tiedostot {#delete-your-purge-list-files}

Suosittelemme sinua poistamaan tarpeettomat tiedostot sen sijaan, että odottaisit automaattisen siivouksen tapahtumista. Jos olet tyytyväinen poistamaan kaikki `path_summary.txt`-tiedostossa listatut tiedostot, voit suorittaa seuraavan komennon:

!!! varoitus-label
    **Tämän osion komennot poistavat tiedostosi!** Varmista, että olet tarkistanut huolellisesti poistettavien tiedostojen listan! Varmista myös, että olet varmuuskopioinut säilytettävät tiedostot (klusterin ulkopuolella) ennen komentojen suorittamista. Tämä toimenpide on peruuttamaton.

!!! Huomio
    Poistamisprosessi voi kestää huomattavan kauan (useita tunteja riippuen tiedostojen määrästä), joten on parasta aloittaa se `screen`- tai `tmux`-istunnossa, jotta voit irrottautua SSH-istunnostasi, kun poistaminen jatkuu taustalla.

```bash
# Käynnistä screen-istunto
screen
# Poista kaikki tiedostosi purkulistalla:
# Korvaa "/path/to/my/path_summary.txt" oman projektisi path_summary.txt-tiedoston polulla
lcleaner -0 /path/to/my/path_summary.txt | xargs -0 -n 50 rm -vf --
# Tämän jälkeen voit painaa "Ctrl + a" ja sitten "d" irrottautuaksesi screen:stä ja pitääksesi
# poistamisen käynnissä taustalla.
# Suorita "screen -r" muodostaaksesi yhteyden takaisin screeniin.
# Sulje screen-istunto kirjoittamalla "exit" shellissä.
```

Jos haluat poistaa vain osan tiedostoista, esimerkiksi tietyn hakemiston sisällä olevat tiedostot, voit käyttää esimerkiksi seuraavaa komentoa:

```bash
# Poista vain purkulistalla olevat tiedostot, jotka ovat hakemistossa /scratch/$my_project/delete-this-dir/
screen lcleaner -0 /path/to/my/path_summary.txt | grep -zZ "/scratch/${my_project:?}/delete-this-dir/" | xargs -0 -n 50 rm -vf --
# Ctrl + a, d screenin irrottamiseen.
```

#### LCleaner-tulostusformaatit {#lcleaner-output-formats}

Jos haluat nähdä poistettavien tiedostojen koot, voit käyttää joko JSON- tai CSV-formaatteja. Huomaa, että jos haluat käyttää useita tulostusformaatteja samanaikaisesti, sinun on myös määritettävä tulostetiedostopolku.
Käyttämällä `-0` tai `--nullbyte` -parametreja, tiedostopolut erotellaan null-byte -merkilla, mikä voi olla hyödyllistä välittämään ongelmia tiedostopolkujen välilyönnin kanssa.

```bash
# Tulosta purkulistasi CSV-muodossa tiedostopolkujen ja kokojen kanssa.
# Huomaa, että CSV-formaatti tulostaa myös otsikkorivin.
lcleaner --csv "/scratch/purge_lists/${my_project:?}/path_summary.txt"

# Tulosta purkulistasi JSON-muodossa tiedostopolkujen ja kokojen kanssa:
lcleaner --json "/scratch/purge_lists/${my_project:?}/path_summary.txt"
# VINKKI: Voit välitellä tuloksen jq-ohjelmaan prettify-taakse valmisteluun.
# Piste lopputuloksen jälkeen on pakollinen argumentti jq:lle.
lcleaner --json "/scratch/purge_lists/${my_project:?}/path_summary.txt" | jq .

# Tulosta sekä JSON- että CSV-tiedostot purge_list.json ja purge_list.csv:
lcleaner --json --csv --out-file purge_list "/scratch/purge_lists/${my_project:?}/path_summary.txt"

# Tulosta tiedostopolut eritettyinä null-merkeillä:
lcleaner -0 "/scratch/purge_lists/${my_project:?}/path_summary.txt"
# Tavallisesti haluat putkittaa null-merkeillä-erotetun tuloksen "xargs -0"-komentoon ja tehdä jotain
# lisäkäsittelyä sillä. Esimerkiksi näin:
lcleaner -0 --limit 3 "/scratch/purge_lists/${my_project:?}/path_summary.txt" \
  | xargs -0 -Ifilepath echo "Minun pitäisi suorittaa: rm -vf 'filepath'"
```

Tulostus esimerkkejä:

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

# JSON, putkitetuna jq:lle:
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

# Null-bytets args:
[westersu@puhti-login11 ~]$ lcleaner -0 --limit 3 path_summary.txt \
>   | xargs -0 -Ifilepath echo "Minun pitäisi suorittaa: rm -vf 'filepath'"
Minun pitäisi suorittaa: rm -vf '/scratch/westersu/my-old-files/file1'
Minun pitäisi suorittaa: rm -vf '/scratch/westersu/my-old-files/file2'
Minun pitäisi suorittaa: rm -vf '/scratch/westersu/my-old-files/file3'
```

### Huomioita LCleaner-käytöstä {#notes-on-lcleaner-usage}

Tämä osio sisältää muutamia huomioita, jotka saattavat olla hyvä tietää siitä, miten LCleaner käyttäytyy, tai miksi yllä olevat komentoesimerkit on muokattu tavalla, jolla ne ovat.

- Joskus `lcleaner` tulostaa virheitä riveistä, joita se ei pystynyt jäsentämään.
  Jos virheitä on, varoitus tulostetaan lopussa, joka osoittaa, että oli ainakin yksi virhe. Varoitukset sanovat esimerkiksi näin: "Tunnistimme N virhettä komennon suorituksen aikana. Ole hyvä ja tarkista lokit lisätietoa varten!"
  Virheet osoittavat, mihin rivinumeroon ongelmallinen teksti liittyi, jotta voit tarkistaa sen manuaalisesti.
    - Vinkki: Tulosta vain tietty rivi, esimerkiksi rivi 123 `path_summary.txt`-tiedostossa, voit käyttää tätä komentoa: `sed -n 123p /path/to/path_summary.txt`
- Jotta `lcleaner`:in lokitus tallentuu, voit ohjata vakiovirran tiedostoon. Tämä saattaa olla hyödyllistä, jos kohtaat ongelmia ja haluat apua tilanteen ratkaisemiseksi.
    - `lcleaner --log-level debug path_summary.txt 2> ~/lcleaner-debug-$(date +%s).log`
- Esimerkkikomennoissa tällä sivulla `-0` sekä `lcleaner`:in että `xargs`:in käyttö on suositeltavaa, jotta vältetään ongelmia tiedostonimien kanssa, jotka sisältävät välilyöntejä.
- LCleanerilla on myös joitain hallinnollisia toimintoja, jotka eivät ole tarkoitettu ja joissain tapauksissa eivät toimi tavallisille käyttäjille. Mikäli ohjeissa viitataan `--admin-mode`-lippuun, se voidaan jättää huomiotta turvallisesti.

### LCleaner vianmääritys {#troubleshooting-lcleaner}

Jos huomaat virheitä, ilmoita niistä [CSC Service deskiin](../contact.md).