# Allaksen käyttäminen tutkimusprojektin aineiston isännöintiin { #using-allas-to-host-a-data-set-for-a-research-project } #

Esimerkkiskenaario Allaksen käyttötapauksesta.

### Roolit näytelmässä { #roles-of-the-play } ###

**Saara**:   Professori, joka koordinoi inspiroivaa tutkimusprojektia.

**Pekka**:  Tutkija, joka huolehtii projektin datanhallinnasta.

**Mats**:    Teknikko, joka työskentelee Analysis Service Centerissä.

**Xi ja Laura**:   Tutkimusprojektiin osallistuvat tutkijat. 
 

## Näytös 1. Professori Saara avaa CSC-projektit { #act-1-professor-saara-opens-csc-projects } ##

Professori Saara johtaa suomalaiseen yliopistoon sijoittuvaa laajaa tutkimusprojektia nimeltä _HiaNo_. 
Projekti on juuri lähettänyt joukon näytteitä Analysis Service Centeriin prosessoitavaksi ja analysoitavaksi. 
Analyysi kestää muutamia viikkoja ja tuottaa 80 TB dataa, jota tutkimusryhmä käyttää varsinaisessa tutkimuksessa.

Saara ja datanhallinnasta vastaava Pekka tutustuvat [CSC:n tarjoamiin tallennusvaihtoehtoihin](https://research.csc.fi/data-management). He päättävät käyttää Allas-palvelua datan tallentamiseen ja jakamiseen tutkimusprojektin aikana. Data ei ole arkaluonteista henkilötietoa, joten Allas soveltuu hyvin.

Ensimmäisenä askeleena Saara ja Pekka kirjautuvat [MyCSC-portaaliin](https://my.csc.fi) ja [rekisteröityvät CSC-käyttäjiksi](../../accounts/how-to-create-new-user-account.md).

Sitten Saara [luo CSC:lle kaksi tutkimusprojektia](../../accounts/how-to-create-new-project.md): toisen nimellä _Data management of the HiaNo project_ (projektitunnus: project_2000444) ja toisen nimellä _HiaNo research project_ (projektitunnus: project_2000333).

Kun CSC-projektit on perustettu, Saara [aktivoi Allas-, Puhti- ja cPouta-palvelut](../../accounts/how-to-add-service-access-for-project.md) molemmille projekteille. Koska Saara tietää, että Allaksen oletustallennustila (10 TB) ei riitä saapuvalle aineistolle, hän lähettää pyynnön 90 TB:n Allas-kiintiöstä projektille _Data management of the HiaNo project_ osoitteeseen servicedesk@csc.fi.

Lopuksi Saara [lisää Pekan molempiin CSC-projekteihin](../../accounts/how-to-add-members-to-project.md) ja pyytää häntä huolehtimaan saapuvan datan käytännön yksityiskohdista.  

## Näytös 2. Jaetun bucketin luominen { #act-2-creating-a-shared-bucket } ##

Analysis Service Centerin Mats ottaa yhteyttä Pekkaan ja kertoo, että tulokset ovat valmiit, ja kysyy, miten data tulisi toimittaa. Matsilla on CSC-tunnus (_msundber_ projektissa _project_2000111_) ja Allas käytössä, joten Pekka ehdottaa, että data ladataan Allakseen. Tätä varten Pekka luo Allakseen bucketin ja antaa Matsille oikeudet käyttää sitä.

Pekka kirjautuu Puhtiin
```text
ssh puhti.csc.fi   
```
ja avaa yhteyden Allaksessa datanhallintaprojektiin:
```text
module load allas
allas-conf project_2000444
```
Sitten hän luo Allakseen uuden bucketin. Tapoja on monia, mutta tällä kertaa Pekka tekee sen tuomalla uuden tiedoston Allakseen komennolla _a-put_:
```text
echo “This bucket is used to host the original data of HiaNo project sample1” > README.txt
a-put -b hiano-project-sample001 README.txt
a-list hiano-project-sample001 
```
Pekka sisällytti projektin nimen bucketiin (_hiano-project-sample001_) varmistaakseen, että bucketin nimi on uniikki koko Allas-palvelussa. Komento _a-list_ näyttää, että bucket luotiin onnistuneesti.

Seuraavaksi Pekka käyttää komentoa _a-access_ [muuttaakseen uuden bucketin käyttöoikeuksia](./using_allas/swift_client.md#giving-another-project-read-and-write-access-to-a-bucket) niin, että Mats (käyttäjä _msundber_ Allas-projektista _project_2000111_) voi käyttää sitä.
```text
a-access +rw project_2000111 hiano-project-sample001
```
Pekan täytyy vielä lähettää jaetun bucketin nimi Matsille, sillä tavalliset Allaksen listauskomennot eivät näytä bucketiä Matsille, joka ei ole bucketin omistavan projektin jäsen.

## Näytös 3. Datan lataaminen { #act-3-uploading-data }

Matsilla on [Allas-työkalut](https://github.com/CSCfi/allas-cli-utils) asennettuna mittalaitteen etupalvelimelle Analysis Service Centerissä. Näin hän voi ladata datan suoraan etupalvelimelta Allaksen _hiano-project-sample1_-bucketiin:
```text
rclone copy sample1/cannel43/aa_3278830.dat  allas:hiano-project-sample001/sample1/cannel43/aa_3278830.dat
```
Koska siirrettävää dataa on paljon, lataus kestää muutamia päiviä ja se täytyy tehdä useassa erässä. Kun Mats ilmoittaa, että kaikki datalataukset on tehty, Pekka sulkee jaetun bucketin:
```text
a-access -rw project_2000111 hiano-project-sample001
```

## Näytös 4. Datan käyttö tutkimuksessa { #act-4-using-the-data-in-research } ##

Kun data on saatavilla, varsinainen analyysityö alkaa. Tutkimusprojektin aikana useat käyttäjät hyödyntävät aineistoa. Pekka tietää, että jos kaikilla käyttäjillä on täydet käyttöoikeudet (luku ja kirjoitus), on vaarana, että joku vahingossa poistaa tai ylikirjoittaa osan datasta. Siksi sovitaan, että vaikka dataa isännöidään datanhallintaprojektissa (project_2000444), tutkijat käyttävät dataa _HiaNo research project_ -projektin (project_2000333) kautta.

Pekka antaa _hiano-project-sample001_-bucketille lukuoikeuden projektille _project_2000333_, mutta ei kirjoitusoikeutta.
```text
module load allas
allas-conf project_2000444
a-access +r project_2000333 hiano-project-sample001
```
Xi ja Laura voivat nyt aloittaa työn datan parissa. He rekisteröityvät MyCSC-portaalissa, minkä jälkeen Saara, joka on päätutkija, lisää heidät CSC-projektiin _HiaNo research project_ (project_2000333).

Xi ja Laura käyvät uudelleen MyCSC:ssä ja hyväksyvät tutkimusprojektin palvelut. Tämän jälkeen he voivat ladata tarvitsemansa tutkimusdatan mihin tahansa ympäristöön, joka osaa muodostaa yhteyden Allakseen: Puhtiin, cPoudan virtuaalikoneeseen tai omaan kannettavaan. Kun projektiin liittyy uusia tutkijoita, Saara lisää heidät projektiin project_2000333, jotta he pääsevät dataan käsiksi.

Koska datan tallentaminen Allakseen kuluttaa Storage Billing Unit -yksiköitä, Saran on syytä tarkistaa MyCSC:stä saldo aika ajoin ja tarvittaessa [hakea lisää laskutusyksiköitä](../../accounts/how-to-apply-for-billing-units.md) (80 TB kuluttaa 700 800 Storage BU:ta vuodessa). Onneksi HiaNo on akateeminen tutkimusprojekti, joten Saran ei tarvitse maksaa laskutusyksiköistä.

Allas-tallennus on tarkoitettu vain tutkimusprojektin ajaksi, mutta Saara ajattelee, että alustavan datan julkaiseminen julkisesti ja helpommin löydettäväksi olisi hyödyllistä. Tätä tukevat CSC:n tuottamat [Fairdata-palvelut](https://www.fairdata.fi/en/).

Pekka luo uuden julkisen bucketin ja lataa datan sinne. Komento _a-publish_ luo bucketin ja lataa valitut tiedostot siihen. Parametrilla `-b` määritetään bucketin nimi, tässä tapauksessa `hiano-project-public001`.
```text
a-publish -b hiano-project-public001 zz_364872.dat zz_242165.dat
```
Seuraavaksi Pekka laatii aineistosta perustason kuvauksen [Fairdata Qvain -työkalulla](https://www.fairdata.fi/en/qvain/) ja lisää kaksi URL-osoitetta (yhden kutakin Allaksessa olevaa tiedostoa kohti) Qvainissa Remote Resource -tietoihin. Tämän jälkeen data voidaan julkaista datasetinä, jolla on laskeutumissivu ja pysyvä tunniste. Näin alustavaa dataa voidaan jakaa kollegoille pysyvän tunnisteen avulla. Aineistoa voi myös selata [Fairdata Etsin -palvelussa](https://www.fairdata.fi/en/etsin/), jossa on jäsenneltyä tietoa ja suora pääsy Allaksessa olevien tiedostojen lataamiseen.


## Näytös 5. Loppu { #act-5-the-end } ##

Neljä vuotta kestäneen intensiivisen tutkimuksen jälkeen, joka on laajentunut useisiin tutkimuslaitoksiin Suomessa ja ulkomailla, HiaNo-projekti on tuottanut joitakin opinnäytteitä ja paljon korkeatasoisia julkaisuja (kaikissa mainitaan CSC:n resurssien käyttö).  

Data ei ole enää aktiivisessa käytössä. Osa Allakseen tuodusta datasta on julkaistu kansainvälisissä tutkimustietokannoissa. Jotkin aineistot on siirretty [IDAan](https://ida.fairdata.fi), jotta dataan voidaan liittää DOI-tunniste ja metadata, mikä tekee sen uudelleenkäytöstä muille tutkijoille mahdollista. Näitä aineistoja voi myös selata [Fairdata Etsinissä](https://www.fairdata.fi/en/etsin/). Osan datasta voi nyt poistaa, ja osa voidaan siirtää uuden _HiaNo2_-projektin bucketeihin.

Tässä vaiheessa Pekka siivoaa loput dataobjektit Allaksesta, minkä jälkeen Saara ilmoittaa CSC:lle, että projekti voidaan sulkea.