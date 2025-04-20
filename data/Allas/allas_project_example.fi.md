# Allaksen käyttö tutkimusprojektin aineiston tallennukseen {#using-allas-to-host-a-data-set-for-a-research-project} #

Esimerkkitilanne Allaksen käyttötapauksesta.

### Rooleissa {#roles-of-the-play} ###

**Saara**:   Professori, joka koordinoi inspiroivaa tutkimusprojektia.

**Pekka**:   Tutkija, joka huolehtii projektin aineistonhallinnasta.

**Mats**:    Tekninen asiantuntija Analyysipalvelukeskuksessa.

**Xi ja Laura**:   Tutkijoita, jotka työskentelevät tutkimusprojektissa.
 

## Näytös 1. Professori Saara avaa CSC-projektit {#act-1-professor-saara-opens-csc-projects} ##

Professori Saara vetää suurta tutkimusprojektia nimeltään _HiaNo_ suomalaisessa yliopistossa.
Projekti on juuri toimittanut näytesarjan analysoitavaksi Analyysipalvelukeskukseen.
Analyysissä kestää joitakin viikkoja ja se tuottaa 80 TB dataa, jota tutkimusryhmä käyttää varsinaiseen tutkimukseen.

Saara ja Pekka, joka huolehtii aineistonhallinnasta, tutustuvat [CSC:n tarjoamiin tallennusvaihtoehtoihin](https://research.csc.fi/data-management). He päättävät käyttää Allasta datan tallentamiseen ja jakamiseen tutkimusprojektin aikana. Data ei ole arkaluontoista henkilötietoa, joten Allas soveltuu tähän tarkoitukseen.

Ensimmäisenä vaiheena Saara ja Pekka kirjautuvat [MyCSC-portaaliin](https://my.csc.fi) ja [rekisteröityvät CSC:n käyttäjiksi](../../accounts/how-to-create-new-user-account.md).

Sen jälkeen Saara [luo kaksi tutkimusprojektia](../../accounts/how-to-create-new-project.md) CSC:hen: ensimmäinen on nimeltään _HiaNo-projektin aineistonhallinta_ (projektitunnus: project_2000444) ja toinen _HiaNo-tutkimusprojekti_ (projektitunnus: project_2000333).

Kun CSC-projektit on perustettu, Saara [aktivoi Allas-, Puhti- ja cPouta-palvelut](../../accounts/how-to-add-service-access-for-project.md) molemmille projekteille. Koska Saara tietää, ettei Allaksen oletustallennustila (10 TB) riitä saapuvalle aineistolle, hän lähettää pyynnön 90 TB Allas-kiintiöstä projektille _HiaNo-projektin aineistonhallinta_ osoitteeseen servicedesk@csc.fi.

Lopuksi Saara [lisää Pekan molempiin CSC-projekteihin](../../accounts/how-to-add-members-to-project.md) ja pyytää häntä huolehtimaan saapuvan datan yksityiskohdista.

## Näytös 2. Jaetun bucketin luominen {#act-2-creating-a-shared-bucket} ##

Mats Analyysipalvelukeskuksesta ottaa yhteyttä Pekkaan ja kertoo, että tulokset ovat valmiina, ja kysyy, kuinka datat tulisi toimittaa. Matsilla on tili CSC:llä (_msundber_ projektissa _project_2000111_) Allaksen käyttöoikeudella, joten Pekka ehdottaa, että data ladataan Allakseen. Tätä varten Pekka luo bucketin Allakseen ja antaa Matsille käyttöoikeuden siihen.

Pekka kirjautuu Puhtiin
```text
ssh puhti.csc.fi
```
ja avaa yhteyden aineistonhallinnan projektiin Allaksessa:
```text
module load allas
allas-conf project_2000444
```
Sen jälkeen hän luo uuden bucketin Allakseen. Tapoja on monia, tällä kertaa Pekka tekee sen tuomalla uuden tiedoston Allakseen _a-put_-komennolla:
```text
echo “This bucket is used to host the original data of HiaNo project sample1” > README.txt
a-put -b hiano-project-sample001 README.txt
a-list hiano-project-sample001 
```
Pekka sisällytti projektin nimen bucketin nimeen (_hiano-project-sample001_) varmistaakseen, että nimi on yksilöllinen koko Allas-palvelussa. _a-list_-komento näyttää, että bucket on onnistuneesti luotu.

Seuraavaksi Pekka käyttää _a-access_-komentoa [muuttaakseen uuden bucketin käyttöoikeuksia](./using_allas/swift_client.md#giving-another-project-read-and-write-access-to-a-bucket) siten, että Mats (käyttäjä _msundber_ Allaksessa projektissaan _project_2000111_) voi käyttää sitä.
```text
a-access +rw project_2000111 hiano-project-sample001
```
Pekan on vielä lähetettävä jaetun bucketin nimi Matsille, koska normaalit Allas-listauskomennot eivät näytä Matsille bucketin nimeä, jos hän ei ole sen omistavan projektin jäsen.

## Näytös 3. Datan lataaminen {#act-3-uploading-data} ##

Matsilla on [Allas-työkalut](https://github.com/CSCfi/allas-cli-utils) asennettuna mittalaitteen palvelimen etupäähän Analyysipalvelukeskuksessa. Näin hän voi ladata datan suoraan etupalvelimelta Allaksen _hiano-project-sample1_-bucketiin:
```text
rclone copy sample1/cannel43/aa_3278830.dat  allas:hiano-project-sample001/sample1/cannel43/aa_3278830.dat
```
Koska siirrettävää dataa on paljon, lataus kestää muutamia päiviä ja pitää tehdä useassa erässä. Kun Mats ilmoittaa olevansa valmis datan latauksen kanssa, Pekka sulkee jaetun bucketin:
```text
a-access -rw project_2000111 hiano-project-sample001
```

## Näytös 4. Datan hyödyntäminen tutkimuksessa {#act-4-using-the-data-in-research} ##

Kun data on saatavilla, varsinainen analyysityö alkaa. Useat käyttäjät hyödyntävät datasettiä tutkimusprojektin aikana. Pekka tietää, että jos kaikilla käyttäjillä on täydet oikeudet (luku ja kirjoitus), on mahdollista, että joku voi vahingossa poistaa tai ylikirjoittaa aineistoa. Sovitaan siis, että kun data on aineistonhallinnan projektin (project_2000444) hallussa, tutkijat käyttävät sitä _HiaNo-tutkimusprojektin_ (project_2000333) kautta.

Pekka antaa lukuoikeuden _hiano-project-sample001_-bucketiin projektille _project_2000333_, ei kuitenkaan kirjoitusoikeutta.
```text
module load allas
allas-conf project_2000444
a-access +r project_2000333 hiano-project-sample001
```
Xi ja Laura voivat nyt aloittaa työskentelyn datan parissa. He rekisteröityvät MyCSC-portaalissa, jonka jälkeen Saara, joka on vastuullinen johtaja (Principal Investigator), lisää heidät CSC:n projektiin _HiaNo-tutkimusprojekti_ (project_2000333).

Xi ja Lauran pitää käydä MyCSC:ssa hyväksymässä projektin palvelut. Sen jälkeen he voivat ladata tutkimusdataa mihin tahansa ympäristöön, joka pystyy yhdistämään Allakseen: Puhti, virtuaalikone cPoutassa, tai oma kannettava. Kun uusia tutkijoita liittyy projektiin, Saara lisää heidät projektiin project_2000333, jotta he saavat pääsyn aineistoon.

Koska Allaksessa datan säilytys kuluttaa laskentayksiköitä, Saaran pitää tarkistaa saldo MyCSC:ssa aika ajoin, ja tarvittaessa [hakea lisää laskentayksiköitä](../../accounts/how-to-apply-for-billing-units.md) (80 TB vie 700 800 Bu vuodessa). Onneksi HiaNo on akateeminen tutkimusprojekti, joten Saaran ei tarvitse maksaa laskentayksiköistä.

Allaksen tallennus on tarkoitettu vain tutkimusprojektin ajaksi, mutta Saara ajattelee, että olisi hyödyllistä avata esiaineisto julkisesti löydettäväksi. Tätä tukevat [Fairdata-palvelut](https://www.fairdata.fi/en/), joita CSC tuottaa.

Pekka luo uuden bucketin julkisella näkyvyydellä ja lataa sinne datan. Komento _a-publish_ luo bucketin ja lataa valitut tiedostot siihen. Parametrilla `-b` määritetään bucketin nimi, tässä tapauksessa `hiano-project-public001`.
```text
a-publish -b hiano-project-public001 zz_364872.dat zz_242165.dat
```
Seuraavaksi Pekka tekee datasta perustason kuvauksen [Fairdata Qvain -työkalulla](https://www.fairdata.fi/en/qvain/) ja liittää kaksi URL-osoitetta (yksi jokaista Allas-tiedostoa varten) Qvainin etäresurssiksi. Tämän jälkeen aineisto voidaan julkaista datasetiksi, jolla on oma laskeutumissivu ja pysyvä tunniste. Näin esiaineistoa voidaan jakaa kollegoille pysyvän tunnisteen avulla. Datasettiä voi myös tarkastella [Fairdata Etsin -palvelussa](https://www.fairdata.fi/en/etsin/), jossa tiedoista näkee rakenteisen kuvauksen ja tiedostot voi ladata Allaksesta suoraan.

## Näytös 5. Loppu {#act-5-the-end} ##

Neljä vuoden intensiivisen tutkimuksen jälkeen, joka on laajentunut useisiin instituutioihin Suomessa ja ulkomailla, HiaNo-projekti on tuottanut joitain opinnäytetöitä ja lukuisia korkealaatuisia julkaisuja (kaikissa maininta CSC:n resurssien käytöstä).

Data ei ole enää aktiivisessa käytössä tällä hetkellä. Osa Allakseen tuodusta datasta on julkaistu kansainvälisissä tutkimustietokannoissa. Joitakin datasettiä on siirretty [IDAan](https://ida.fairdata.fi), jotta niihin voidaan liittää DOI-tunniste ja metadata mahdollistaen aineiston uudelleenkäytön muille tutkijoille. Näitä datasettiä voi tarkastella myös [Fairdata Etsinissä](https://www.fairdata.fi/en/etsin/). Osa datasta voidaan nyt poistaa ja osa siirtää uuden _HiaNo2_-projektin bucketiin.

Tässä vaiheessa Pekka poistaa jäljelle jääneet dataobjektit Allaksesta, minkä jälkeen Saara ilmoittaa CSC:lle, että projekti voidaan päättää.