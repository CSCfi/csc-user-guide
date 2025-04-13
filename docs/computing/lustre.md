# Lustre-tiedostojärjestelmä

CSC:n supertietokoneet käyttävät [Lustre](https://www.lustre.org/)-järjestelmää rinnakkaisena hajautettuna tiedostojärjestelmänä. Tämä artikkeli tarjoaa lyhyen teknisen kuvauksen Lustresta.

## Lustren arkkitehtuuri {#lustre-architecture}

Lustre erottaa tiedostodatat ja metadatat eri palveluiksi. **Data** on tiedoston varsinaista sisältöä, kun taas **metadata** sisältää tietoa kuten tiedoston koko, käyttöoikeudet, viimeisin käyttöpäivä jne.

Lustre-tiedostojärjestelmä koostuu joukosta I/O-palvelimia, joita kutsutaan objektivarastopalvelimiksi (Object Storage Servers, OSSs) ja levyistä, joita kutsutaan objektivarastokohteiksi (Object Storage Targets, OSTs), jotka tallentavat varsinaisen tiedon. Tiedoston metadataa ohjaavat metadatapalvelimet (Metadata Servers, MDSs) ja ne tallennetaan metadatakohteisiin (Metadata Targets, MDTs). Käytännössä palvelimet käsittelevät pyyntöjä tiedostosisältöjen ja metadatan saatavuudesta; sovellukset eivät pääse levyihin suoraan. Lustre-järjestelmissä käytetään tavallisesti useita OSS- ja MDS-palvelimia yhdistettynä useisiin OST- ja MDT-kohteisiin rinnakkaisen I/O-kyvykkyyden tarjoamiseksi.

* *Objektivarastopalvelimet* (OSSs): Ne käsittelevät asiakkaiden pyyntöjä tiedonsiirtoa varten. Lisäksi ne hallinnoivat joukkoa OST-kohteita; jokainen OSS voi käsitellä useampaa kuin yhtä OST-kohdetta parantaakseen I/O-rinnakkaisuutta.
* *Objektivarastokohteet* (OSTs): Yleensä OST koostuu joukosta tallennuslaitteita RAID-konfiguraatiossa. Tieto tallennetaan yhteen tai useampaan objektiin, ja jokainen objekti tallennetaan erilliseen OST-kohteeseen.
* *Metadatapalvelin* (MDS): Palvelin, joka seuraa kaikkien tietojen sijainteja, jotta se voi päättää, mitä OSS- ja OST-kohteita käytetään. Esimerkiksi tiedoston avaamisen jälkeen MDS ei enää osallistu prosessiin.
* *Metadatakohde* (MDT): Tallennus sisältää tiedostojen ja hakemistojen tietoja, kuten tiedostojen koon, käyttöoikeudet ja viimeisimmät käyttöpäivät. Jokaiselle tiedostolle MDT sisältää tietoa datan sijoittelusta OST-kohteissa, kuten OST-numeroista ja objekti-identifioijista.

!["Laskentasolmujen kaaviokuva, jotka pääsevät OST- ja MDT-kohteisiin OSS- ja DST-palvelimien kautta verkon välityksellä. Lyhenteet ja suhteet selitetään myös tekstissä."](../img/lustre.png 'Lustre-tiedostojärjestelmän näkymä')

*Lustre-tiedostojärjestelmän näkymä*

Lustre on suunniteltu tehokkaaseen rinnakkaiseen I/O-käyttöön suurille tiedostoille. Kuitenkin, kun käsitellään pieniä tiedostoja ja intensiivisiä metadatatoimintoja, MDS/MDT voi muodostua pullonkaulaksi. Esimerkiksi käyttäjän avattessa/sulkiessa tiedoston monta kertaa silmukassa, MDT:n työmäärä kasvaa. Jos useat käyttäjät tekevät samanlaisia operaatioita, metadatatoiminnot voivat hidastaa koko järjestelmää ja vaikuttaa moniin käyttäjiin. Koska kirjautumis- ja laskentasolmut jakavat tiedostojärjestelmän, tämä voi ilmetä jopa hitautena tiedostojen muokkauksessa kirjautumissolmua käyttäen. Myös, jos rinnakkaissovelluksessa eri prosessit suorittavat paljon operaatioita samoille pienille tiedostoille, metadatatoiminnot voivat hidastua. Viattoman näköiset Linux-komennot voivat myös kasvattaa metadatan työkuormaa: esimerkiksi `ls -l` tulostaa tiedostojen metadataa, ja komennon antaminen hakemistossa, jossa on paljon tiedostoja, aiheuttaa monia pyyntöjä MDS:lle.

## Tiedostojen jakaminen ja optimointi {#file-striping-and-alignment}

Jotta Lustren rinnakkaisesta I/O:sta hyötyisi, tiedot pitäisi jakaa monille OST-kohteille. Tietojen jakaminen monille OST-kohteille tunnetaan nimellä **file striping**. Loogisesti tiedosto on lineaarinen bittijonon jakso. Tiedostojen jakaminen tarkoittaa, että tiedosto jaetaan bittilohkoihin, jotka sijaitsevat eri OST-kohteissa, jolloin luku- ja kirjoitusoperaatiot voidaan suorittaa rinnakkain.

Jakaminen voi lisätä käytettävissä olevaa kaistanleveyttä tiedostojen käyttöön, mutta siinä on myös ylimääräistä viivettä, joka johtuu verkko-operaatioiden lisääntymisestä ja mahdollisesta palvelinkilpailusta. Näin ollen jakaminen on yleensä hyödyksi vain suurille tiedostoille.

Koska supertietokoneet sisältävät paljon enemmän solmuja kuin OSS-/OST-kohteet, I/O-suorituskyky voi vaihdella paljon koko supertietokoneen I/O-työkuorman mukaan.

Rinnakkaisohjelmassa suorituskyky paranee, kun jokainen rinnakkainen prosessi käyttää eri jonoa tiedostosta rinnakkaisen I/O:n aikana. Lisäksi verkkojen kilpailun välttämiseksi kunkin prosessin pitäisi käyttää mahdollisimman harvoja OST-/OSS-kohteita. Tämä voidaan saavuttaa kaistan tasauksella. Paras suorituskyky saavutetaan, kun tiedot jakautuvat tasaisesti OST-kohteisiin ja rinnakkaisprosessit käyttävät tiedostoa alueilla, jotka vastaavat jono-rajapintoja.

!["Kaavio, joka näyttää tiedoston jaettuna lohkoihin, joista kukin on tallennettu eri OST-kohteeseen."](../img/file_striping.png 'Lustre-tiedostojen jakaminen ja tasapainotus')

*Lustre-tiedostojen jakaminen ja tasapainotus*

Jos edellisessä esimerkissä meillä olisi ollut 5 MB:n kokoinen tiedosto, niin OST 0:lla olisi ollut ylimääräinen 1 MB tietoa. Jos data jaettaisiin tasaisesti neljän prosessin kesken, jokaisella prosessilla olisi 1.5 MB ja käyttö ei olisi kaistan tasaukseen määrittynyt: ensimmäinen prosessi tarvitsee käyttää OST 0 ja 1, seuraava prosessi OST 1 ja 2, *jne.* prosessit eivät ole tasattuja. Tämä voisi nyt aiheuttaa verkon kilpailuongelmia.

### Kaistan hallinta {#controlling-striping}

CSC:n Lustren oletuskaistankoko on 1 MB ja kaistaluku on 1, eli oletuksena tiedostoja ei ole jaettu kaistaksi. Käyttäjä voi kuitenkin vaihtaa kaista-asetuksia, mikä voi parhaimmillaan parantaa I/O-suorituskykyä huomattavasti.

Kaista-asetukset tiedostolle tai hakemistolle voidaan kysellä `lfs getstripe` -komennolla

```
lfs getstripe my_file
```
joka tulostaa:
```
my_file
lmm_stripe_count:  2
lmm_stripe_size:   1048576
lmm_pattern:       raid0
lmm_layout_gen:    0
lmm_stripe_offset: 11
    obdidx         objid        objid         group
        11      29921659    0x1c8917b             0
        20      29922615    0x1c89537             0

```
Tuloste osoittaa, että tiedosto on jaettu kahdelle OST-kohteelle (kaistaluku 2), tuloste myös osoittaa, että kyseiset OST-kohteet ovat 11 ja 20.

Hakemiston kohdalla tuloste näyttää asetukset, joita käytetään kaikille hakemistossa luotaville tiedostoille.

Kaistakonfiguraation voi asettaa `lfs setstripe` -komennolla. Useimmissa tapauksissa riittää asettaa kaistaluku `-c`-valinnalla, mutta myös muita vaihtoehtoja voidaan asettaa, katso esim. `man lfs-setstripe` tai [Lustre wiki](https://wiki.lustre.org/Configuring_Lustre_File_Striping).

```
mkdir experiments
lfs setstripe -c 4 experiments
touch experiments/new_file
```
Suorittamalla nyt `lfs getstripe experiments/new_file` tulostuu:
```
experiments/new_file
lmm_stripe_count:  4
lmm_stripe_size:   1048576
lmm_pattern:       raid0
lmm_layout_gen:    0
lmm_stripe_offset: 6
    obdidx         objid        objid         group
         6      29925064    0x1c89ec8             0
         1      29925258    0x1c89f8a             0
        19      29926834    0x1c8a5b2             0
        15      29921764    0x1c891e4             0

```

!!!! Huomio Jos tiedosto on jo luotu tietyllä kaistalla, sitä ei voi 
muuttaa. Myös jos siirrät tiedoston, sen kaista-asetukset eivät muutu. Kaistan muuttamiseksi tiedosto 
tarvitsee kopioida:

* käyttämällä `setstripe`, luo uusi, tyhjä tiedosto halutuilla kaista-asetuksilla ja kopioi sitten vanha tiedosto uuteen tiedostoon, tai
* aseta hakemisto halutuilla konfiguraatioilla ja kopioi (ei siirrä) tiedosto hakemistoon.

## Erot Puhti ja Mahti tuoleilla {#differences-between-puhti-and-mahti}

Puhti ja Mahti sisältävät samanlaisia tallennusalueita [kotihakemisto](disk.md#home-directory), [projektihakemisto](disk.md#projappl-directory) ja [työhakemisto](disk.md#scratch-directory), mutta niiden Lustre-konfiguraatio ei ole sama.

|  Nimi         | Puhti  |        | Mahti  |        |
|---------------|--------|--------|--------|--------|
|**Levyn alue** | **# OSTs** | **# MDTs** | **# OSTs** | **# MDTs** |
| koti         |  24    |   4    |    8    |   1    |
| projappl     |  24    |   4    |    8    |   1    |
| työhakemisto |  24    |   4    |   24    |   2    |

Yksi merkittävä ero on se, että Mahtilla on erilliset MDT:t välissä `työhakemisto`, `koti`, ja `projekti`, tällöin metadatasuorituskyky ei häiritse eri tiedostojärjestelmien välillä. Lisäksi Mahtin `työhakemisto` voi tarjota parempaa suorituskykyä kuin muut tallennusalueet, jos sovelluksesi ja datan koko on tarpeeksi suuri johtuen enemmän OST:sta ja MDT:ista. Puhdilla, kaikki OST:t ja MDT:t ovat jaetut tallennusalueiden kesken, jolloin suorituskyvyn pitäisi olla samanlainen niiden kesken.

Mahtin huippu I/O-suorituskyky on noin 100 GB/s kirjoitusta ja 115 GB/s lukemista varten. Tämä suorituskyky saavutettiin dedikoidulla järjestelmällä, jossa on 64 laskentasolmua, mikä tarkoittaa noin 1.5 GB/s kutakin laskentasolmua kohden. Mikäli enemmän solmuja käytetään tai monet työt tekevät merkittävää I/O:ta, niin et saavuta 1.5 GB/s, sisältäen myös sen, että ehkä sovelluksen I/O-kaava ei ole tehokas. Vastaava suorituskyky Puhdilla on puolet Mahtin suorituskyvystä.

## Parhaat käytännöt {#best-practices}

* Vältä `ls -l` käyttöä, mikäli mahdollista, koska omistajuus ja käyttöoikeusmetadata on tallennettu MDT:lle, tiedoston kokometadata on saatavilla OST:istä. Käytä `ls`-komentoa, jos et tarvitse ylimääräistä tietoa.

* Vältä suuren tiedostomäärän tallentamista yhteen hakemistoon, on parempi jakaa ne useampiin hakemistoihin.

* Vältä mahdollisuuksien mukaan suuren määrän pienten tiedostojen käyttöä Lustrella.

* Varmista, että pienten tiedostojen kaistaluku on 1.

* Jos sovellus avaa tiedoston lukemista varten, avaa tiedosto pelkästään lukumoodissa.

* Nosta kaistalukua rinnakkaiskäyttäytymiselle, erityisesti suurille tiedostoille:
    * Kaistatekijän tulisi olla rinnakkaisen I/O:n suorittavien prosessien lukumäärän tekijä
    * Nyrkkisääntönä on käyttää kaistana tiedoston koon neliöjuurta GB:ssa. Jos tiedosto on 90 GB, neliöjuuri on 9.5, joten käytä vähintään 9 OST:ta.
    * Jos käytät, esimerkiksi, 16 MPI-prosessia rinnakkaiseen I/O:hon, käytettävien OST:jen lukumäärän tulisi olla enintään 16.

Lisätietoja saat tarkastelemalla [Lustre-suorituskyvyn optimointia käsittelevää opetusmateriaaliamme](../support/tutorials/lustre_performance.md).