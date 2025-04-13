
# Allaksen käyttäminen tutkimushankkeen tietoaineiston isännöintiin #

Esimerkki Allaksen käyttöskenaariosta.

### Roolijako ###

**Saara**:   Inspiroivan tutkimushankkeen koordinaattori, professori.

**Pekka**:  Tutkimushankkeen tietohallinnosta vastaava tutkija.

**Mats**:    Analyysipalvelukeskuksessa työskentelevä teknikko.

**Xi ja Laura**:   Tutkimushankkeessa työskentelevät tutkijat.


## Näytös 1. Professori Saara avaa CSC-projektit {#act-1-professor-saara-opens-csc-projects} ##

Professori Saara johtaa suurta tutkimushanketta nimeltä _HiaNo_ eräässä suomalaisessa yliopistossa. Projekti on juuri lähettänyt joukon näytteitä analysoitavaksi Analyysipalvelukeskukseen, ja analyysin tuloksena syntyy 80 teratavua dataa, jota tutkimusryhmä käyttää varsinaiseen tutkimukseen.

Saara ja tietohallinnosta vastaava Pekka tutkivat [CSC:n tarjoamia tallennusvaihtoehtoja](https://research.csc.fi/data-management). He päättävät käyttää Allas-palvelua datan tallennukseen ja jakamiseen tutkimushankkeen aikana. Data ei ole arkaluonteista henkilötietoa, joten Allas on sopiva vaihtoehto.

Ensimmäiseksi Saara ja Pekka kirjautuvat [MyCSC-portaaliin](https://my.csc.fi) ja [rekisteröityvät CSC:n käyttäjiksi](../../accounts/how-to-create-new-user-account.md).

Saara [luo kaksi tutkimusprojektia](../../accounts/how-to-create-new-project.md) CSC:ssa: toinen nimeltään _HiaNo-projektin tietohallinta_ (projektitunnus: project_2000444) ja toinen nimeltään _HiaNo-tutkimusprojekti_ (projektitunnus: project_2000333).

CSC-projektien perustamisen jälkeen Saara [aktivoi Allas-, Puhti- ja cPouta-palvelut](../../accounts/how-to-add-service-access-for-project.md) molemmille projekteille. Koska Saara tietää, että Allaksen oletustallennustila (10 TB) ei riitä tulevalle tietoaineistolle, hän lähettää pyynnön 90 TB:n Allas-kiintiön saamiseksi projektille _HiaNo-projektin tietohallinta_ osoitteeseen servicedesk@csc.fi.

Lopuksi Saara [lisää Pekan molempiin CSC-projekteihin](../../accounts/how-to-add-members-to-project.md) ja pyytää häntä huolehtimaan saapuvan datan yksityiskohdista. 

## Näytös 2. Jaetun bucketin luominen {#act-2-creating-a-shared-bucket} ##

Analyysipalvelukeskuksen Mats ottaa yhteyttä Pekkaan ja kertoo, että tulokset ovat saatavilla, ja kysyy, miten hän voisi toimittaa datan. Matsilla on CSC:n tili (_msundber_ projektissa _project_2000111_), jossa on Allas käytössä, joten Pekka ehdottaa, että data ladataan Allakseen. Tätä varten Pekka luo Allakseen bucketin ja sallii Matsin käyttää sitä.

Pekka kirjautuu Puhdille
```text
ssh puhti.csc.fi   
```
ja avaa yhteyden tietohallintaprojektiin Allaksessa:
```text
module load allas
allas-conf project_2000444
```
Sitten hän luo uuden bucketin Allakseen. Tämä voidaan tehdä monella tavalla, mutta tällä kertaa Pekka tekee sen tuomalla uuden tiedoston Allakseen _a-put_-komennolla:
```text
echo “Tämä bucket isännöi HiaNo-projektin alkuperäistä tietoaineistoa sample1” > README.txt
a-put -b hiano-project-sample001 README.txt
a-list hiano-project-sample001 
```
Pekka sisällytti projektin nimen bucketin nimeen (_hiano-project-sample001_), jotta bucketin nimi on uniikki koko Allas-palvelussa. _a-list_-komento osoittaa, että bucket luotiin onnistuneesti.

Seuraavaksi Pekka käyttää _a-access_-komentoa [mukaillakseen uuden bucketin käyttöoikeuksia](./using_allas/swift_client.md#giving-another-project-read-and-write-access-to-a-bucket), jotta Mats (käyttäjä _msundber_ Allas-projektista _project_2000111_) voi sitä käyttää.
```text
a-access +rw project_2000111 hiano-project-sample001
```
Pekka joutuu vielä lähettämään jaetun bucketin nimen Matsille, sillä tavalliset Allas-listauskomennot eivät näytä nimeä Matsille, joka ei ole projektin jäsen, joka omistaa bucketin.

## Näytös 3. Datan lataaminen {#act-3-uploading-data} ##

Matilla on [Allas-työkalut](https://github.com/CSCfi/allas-cli-utils) asennettuna mittalaitteen käyttöliittymäpalvelimeen Analyysipalvelukeskuksessa. Näin hän voi ladata datan suoraan käyttöliittymäpalvelimelta _hiano-project-sample1_-bucketiin Allaksessa:
```text
rclone copy sample1/cannel43/aa_3278830.dat allas:hiano-project-sample001/sample1/cannel43/aa_3278830.dat
```
Koska siirrettävää dataa on paljon, lataus kestää useita päiviä ja se on tehtävä useissa erissä. Kun Mats kertoo Pekalle datan siirron olevan valmis, Pekka sulkee jaetun bucketin:
```text
a-access -rw project_2000111 hiano-project-sample001
```

## Näytös 4. Datan käyttö tutkimuksessa {#act-4-using-the-data-in-research} ##

Kun data on saatavilla, varsinainen analyysityö alkaa. Useat käyttäjät tulevat käyttämään tietoaineistoa tutkimushankkeen aikana. Pekka tietää, että jos kaikki käyttäjät käyttävät dataa täysillä käyttöoikeuksilla (luku ja kirjoitus), on vaarana, että joku poistaa tai korvaa vahingossa osan tiedoista. Siksi on sovittu, että kun dataa hallinnoi projektin tietohallinta (project_2000444), tutkijat pääsevät dataan _HiaNo-tutkimusprojektin_ (project_2000333) kautta.

Pekka antaa _hiano-project-sample001_-bucketille lukuoikeuden projektille _project_2000333_, mutta ei kirjoitusoikeutta.
```text
module load allas
allas-conf project_2000444
a-access +r project_2000333 hiano-project-sample001
```
Xi ja Laura voivat nyt aloittaa työn datan kanssa. He rekisteröityvät MyCSC-portaalin kautta, jonka jälkeen vastuututkija Saara lisää heidät CSC-projektiin _HiaNo-tutkimusprojekti_ (project_2000333).

Xi ja Laura käyvät uudelleen MyCSC:ssä ja hyväksyvät tutkimusprojektin palvelut. Tämän jälkeen he voivat ladata tarvitsemaansa tutkimusdataa mihin tahansa ympäristöön, joka voi muodostaa yhteyden Allakseen: Puhtiin, virtuaalikoneelle cPoutassa tai omaan kannettavaan tietokoneeseensa. Kun uusia tutkijoita liittyy projektiin, Saara lisää heidät projektiin_2000333, jotta heillä on pääsy dataan.

Koska datan tallentaminen Allakseen kuluttaa laskentayksiköitä, Saara joutuu tarkistamaan saldon MyCSC:stä säännöllisesti ja tarvittaessa [hakemaan lisää laskentayksiköitä](../../accounts/how-to-apply-for-billing-units.md) (80 TB kuluttaa 700 800 Bu vuodessa). Onneksi HiaNo on akateeminen tutkimushanke, joten Saaraan ei tarvitse maksaa laskentayksiköistä.

Allaksen tallennustila on vain tutkimusprojektin keston ajan, mutta Saara ajattelee, että olisi hyödyllistä, jos alustavaa dataa tehtäisiin julkisesti saatavilla ja helpommin löydettäväksi. Tähän on tukea CSC:n tuottamista [Fairdata-palveluista](https://www.fairdata.fi/en/).

Pekka luo uuden bucketin, jossa on julkinen pääsy ja lataa datan bucketille. Komento _a-publish_ luo bucketin ja lataa valitut tiedostot sinne. Parametria `-b` käytetään bucketin nimen määrittämiseen, tässä tapauksessa `hiano-project-public001`.
```text
a-publish -b hiano-project-public001 zz_364872.dat zz_242165.dat
```
Seuraavaksi Pekka luo perustiedot datasta [Fairdata Qvain -työkalun](https://www.fairdata.fi/en/qvain/) avulla ja antaa kaksi URL-osoitetta (yksi kullekin Allas-tiedostolle) etäresurssina Qvainissa. Tämän jälkeen data voidaan julkaista tietoaineistona avautumisivulla ja pysyvällä tunnisteella. Näin alustavaa dataa voidaan jakaa kollegoille pysyvän tunnisteen avulla. Tietoaineistoon voi myös tutustua [Fairdata Etsin -palvelussa](https://www.fairdata.fi/en/etsin/) jäsennetyn tiedon avulla ja ladata tiedostoja suoraan Allaksesta.

## Näytös 5. Loppu {#act-5-the-end} ##

Neljän vuoden intensiivisen tutkimuksen jälkeen, joka on laajentunut useisiin laitoksiin Suomessa ja ulkomailla, HiaNo-projekti on tuottanut muutaman opinnäytetyön ja monia korkealaatuisia julkaisuja (joissa kaikissa on tunnustettu CSC:n resurssien käyttö).

Tällä hetkellä dataa ei enää käytetä aktiivisesti. Osa Allakseen tuodusta datasta on julkaistu kansainvälisissä tutkimustietokannoissa. Jotkin datasetit on siirretty [IDA-palveluun](https://ida.fairdata.fi) (IDA), jotta dataan voidaan liittää DOI-tunniste ja metatieto, jotta muut tutkijat voivat käyttää sitä uudelleen. Näihin datasettiin voi myös tutustua [Fairdata Etsin -palvelun](https://www.fairdata.fi/en/etsin/) kautta. Osa datoista voidaan nyt poistaa ja osa jäljellä olevista osista siirtää uuteen _HiaNo2_-projektin bucketeihin.

Tässä vaiheessa Pekka puhdistaa jäljellä olevat dataobjektit Allaksesta, minkä jälkeen Saara ilmoittaa CSC:lle, että projekti voidaan sulkea.
