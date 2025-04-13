
# VM:n elinkaari & BU:iden säästäminen {#vm-lifecycle-saving-bus}

Tämä artikkeli selittää, mitä eri tiloja virtuaalikone-instansseilla voi olla ja miten ne vaikuttavat resurssien käyttöön.

[TOC]

Samoin kuin muut pilvipalveluntarjoajat, myös Poutan virtuaalikoneilla on elinkaari. Virtuaalikoneiden eri tiloilla on erilaiset resurssivaatimukset taustalla olevalle laitteistolle, ja sen vuoksi niistä laskutetaan eri tavalla. Tietämällä nämä eri tilat Poutassa voit tehdä parempia päätöksiä infrastruktuurisi ylläpitämiseksi. Tämä auttaa sinua myös säästämään laskentayksikköjä.

## Tilat {#states}

Poutassa virtuaalikoneiden pääasialliset tilat ovat:

### Aktiivinen {#active}
Virtuaalikone on aktiivinen, kun se on *virta päällä* -tilassa. Se pysyy tässä tilassa, olipa se käytössä tai ei. Aktiivinen tila kuluttaa laskentaresursseja yhdeltä laskentasolmuistamme, ja siten siitä laskutetaan normaalisti, kuten on selitetty kohdassa [Pouta-maut ja laskutus](vm-flavors-and-billing.md).

### Sammutettu {#shut-off}
Virtuaalikone ei ole käynnissä ja on *virta pois* -tilassa. Sammutettu virtuaalikone kuluttaa kuitenkin laskentayksiköitä samoin kuin **aktiivinen** tila. Tämä johtuu siitä, että aktiiviset/sammutetut virtuaalikoneet kuluttavat samat laskentaresurssit yhdeltä laskentasolmuistamme, kuten on selitetty kohdassa [Pouta-maut ja laskutus](vm-flavors-and-billing.md).

!!! warning

    *Sammutettu* virtuaalikone kuluttaa edelleen laskentayksiköitä. Jos et halua kuluttaa lisää, valitse *hyllytetty* tila.

### Tauko {#pause}
Virtuaalikoneen tauottaminen pysäyttää kaikki virtuaalikoneessa käynnissä olevat prosessit ja tallentaa koko koneen tilan (muisti, sovellustila jne.) isäntälaskentasolmulle. Et voi käyttää virtuaalikonettasi tai isännöityjä sovelluksia, kun virtuaalikone on *tauko* -tilassa. Jotkut sovellukset saattavat kärsiä haittavaikutuksista tauon aikana, joten tätä tilaa ei suositella tuotantosovelluksille. Jotkin vanhat laskennalliset tehtävät saattavat hyötyä taukotilasta, mutta modernit työnkulut eivät yleensä käytä tätä tilaa. Virtuaalikoneen tauottamisesta laskutetaan samalla tavalla kuin **aktiivisena** olevaa virtuaalikonetta.

### Keskeytä {#suspend}
Virtuaalikoneen keskeyttäminen tallentaa sen nykyisen tilan virtuaalikoneen isäntälaskentasolmulle. Virtuaalikone voidaan käynnistää uudelleen samassa tilassa kuin ennen keskeyttämistä, mutta laskentaresurssit (todelliset ytimet, laskentasolmut jne.) voivat olla erilaiset kuin ennen keskeytystä. Et voi käyttää konettasi, kun se on *keskeytetty* -tilassa. Keskeytetyssä tilassa olevista virtuaalikoneista laskutetaan kuten **aktiivisista** virtuaalikoneista. Keskeyttäminen ei yleensä ole käytössä moderneissa työnkuluissa.

### Hyllytetty {#shelved}
Hyllyttäminen tarkoittaa virtuaalikoneen sammuttamista ja sen poistamista isäntälaskentasolmulta. Tämä vapauttaa virtuaalikoneelle varatut laskentaresurssit. Kaikkien muiden liitettyjen resurssien tila, kuten tiedostojärjestelmä, kelluvat IP-osoitteet, verkkokonfiguraatio jne., tallennetaan keskitettyyn tallennustilaan. Huomaa, että virtuaalikoneen hyllyttäminen **ei** vähennä hankkeen käyttämien resurssien määrää, ainoastaan virtuaalikoneen laskutus pysähtyy.

Hyllyttäminen toimii parhaiten standardimaulle, jotka on jo varustettu keskitettyyn tallennuspalveluumme. Hyllyttäminen voi olla hidasta maulle, jotka käyttävät paikallista tallennusta, varsinkin suurempien makujen kohdalla, koska data täytyy kopioida paikallisen ja keskitetyn tallennuksen välillä. Harvoissa tapauksissa, jos kaikki laskentaresurssimme ovat käytössä, emme ehkä pysty purkamaan virtuaalikonettasi hyllyltä, ennen kuin toinen käyttäjä vapauttaa laskentaresursseja. Huomautus: kelluvia IP-osoitteita, levytilaa jne. ei voi poistaa virtuaalikoneesta ennen kuin se on purettu hyllyltä. Jos kelluvan IP-kiintiösi on kaksi ja yksi niistä on liitetty hyllytettyyn virtuaalikoneeseen, sinulla on vain yksi jäljellä. **Huomaa** että ohimenevä tallennus IO- tai TB-maussa **ei** ole hyllyllä.

### Poista {#terminate}
Poistaminen (tai deletointi) poistaa virtuaalikoneen hankkeestasi ja vapauttaa käytössä olevat laskentaresurssit. Niitä ei voi palauttaa, ja kaikki virtuaalikoneeseen tallennetut tiedot poistetaan, lukuun ottamatta liitettyjä levyjä. Kun virtuaalikone on poistettu, sitä ei enää laskuteta.

## Säästä laskentayksikköjäsi {#save-your-billing-units}

Alla oleva kuva havainnollistaa tilojen välistä siirtymistä.

![Virtuaalikoneen elinkaari](../../img/instance-lifecycle-1.png)

Yllä olevassa osiossa käsittelimme Poutan virtuaalikoneiden päätiloja. Teoreettisesti on olemassa myös muita tiloja. Täydellinen luettelo tiloista ja niiden käyttäytymisestä: [OpenStack dokumentaatio](https://developer.openstack.org/api-guide/compute/server_concepts.html).

Jotta voit siirtyä tilojen välillä, sinulla on kaksi päävaihtoehtoa käyttää [komentoriviasiakastyökaluja](command-line-tools.md) tai käyttää verkkoliittymää. Poutan verkkoliittymän pääsivulla avaa **Instanssit** näkymä. **Toiminnot** sarakkeen alla näet avattavan valikon, jossa on kaikki mahdolliset vaihtoehdot.

![Säästä laskentayksikköjäsi](../../img/Save-Your-billing-units.png)

On monia muita käytäntöjä, jotka auttavat säästämään laskentayksiköitä:

### Automaattinen provisiointi {#automated-provisioning}
Automaattinen virtuaalikoneiden provisiointi ja konfigurointi auttaa säästämään laskentayksiköitä. Esimerkiksi voit poistaa käyttämättömät virtuaalikoneesi automaattisella provisioinnilla ja konfiguroinnilla, kun et enää tarvitse sitä. Myöhemmin, kun tarvitset niitä uudelleen, voit luoda uudet virtuaalikoneet alusta alkaen. Tietosi tulisi aina tallentaa levylle, ja virtuaalikoneet tulisi käynnistää, kun tarvitset laskentaa.

Esimerkki, kuinka automatisoida työvirta Heatillä, Ansiblellä ja Dockerilla käyttöönottaaksesi Etherpadin, joka sisältää sekä klusteroidun tietokannan että tasapainotuksen: <https://github.com/CSCfi/etherpad-deployment-demo>

### Käynnistä kuvasta {#boot-from-image}
Hyödyllinen työkalu Poutassa on oman virtuaalikoneen luominen käyttäen *käynnistä kuvasta (luo uusi levy)* -vaihtoehtoa. Tässä tapauksessa, vaikka poistaisit virtuaalikoneen, koko tiedostojärjestelmän tila tallennetaan pysyvään levyyn keskitettyyn tallennuspalveluumme. Voit käynnistää uuden virtuaalikoneen tältä levyltä. Se tulee olemaan sama tiedostojärjestelmätila kuin aiemmin poistetulla virtuaalikoneella. Voit liittää tämän levyn mihin tahansa muuhun virtuaalikoneeseen ja käyttää poistetun virtuaalikoneen tiedostojärjestelmää. Se laskutetaan kuten normaali levy laskentayksiköissä, mikä on halvempaa kuin käynnissä oleva virtuaalikone. Virtuaalikoneiden luominen tällä työkalulla ja niiden poistaminen, kun niitä ei tarvita, auttaa säästämään laskentayksikköjen allokointia. Yksi hieno vaihtoehto on, että voit helposti poistaa virtuaalikoneesi ja aloittaa uuden saman levyn ja uuden maun kanssa. Tämä tekee mahdolliseksi helposti skaalata pienemmästä virtuaalikoneen mausta suurimpaan virtuaalikoneen makuun.

!!! info

    Tällainen skaalaaminen ei ole suositeltavaa IO-, GPU- tai TB-maulle, sillä ohimenevät tallennustiedot menetetään tässä prosessissa.

### Valitse sopiva tila virtuaalikoneellesi {#select-a-suitable-state-of-your-virtual-machine}
Hankkeesi vaatimusten mukaan voit muuttaa virtuaalikoneidesi tilaa:

-   Jos olet menossa pitkälle lomalle ja haluat säästää laskentayksiköitä, voit hyllyttää virtuaalikoneesi.
-   Jos et enää tarvitse virtuaalikonettasi, voit poistaa sen kopioituasi kaikki olennaiset tiedot siitä levylle.

Voit siirtyä eri tilojen välillä Pouta-kojelautaa, komentorivityökaluja tai REST API:ja käyttäen riippuen projektisi kokoonpanosta. Yleisimmin käytettyjä tiloja virtuaalikoneille ovat aktiivinen, sammutettu, hyllytetty ja poistettu. Saattaa olla tapauksia, kun virtuaalikoneesi siirtyy _virhe_ -tilaan. Virhe tilassa olevista virtuaalikoneista laskutetaan edelleen. Jos virtuaalikoneesi siirtyy virhetilaan etkä pysty palauttamaan sitä, ota yhteyttä cloud-support@csc.fi.

### Muuta virtuaalikoneesi kokoa {#resize-your-virtual-machine}
Virtuaalikoneen koon muuttaminen on hyvä työkalu Poutassa, ja auttaa säästämään laskentayksiköitä. Projektisi vaatimusten perusteella voit skaalata virtuaalikonettasi ylös tai alas muihin makuihin. Virtuaalikoneen skaalaaminen alas, kun sillä on vähemmän laskennallista kuormitusta, vapauttaa laskentaresursseja ja säästää laskentayksiköitä. Myöhemmin, tietokantojasi muokattaessa voit skaalata virtuaalikoneitasi ylöspäin laskennallisista töistäsi riippuen. Huomaa, että voit muuttaa koon toiseen makuun toisesta *perheestä*, mutta tätä **ei suositella!**. Voit menettää tietoja tämän prosessin aikana, eikä CSC ole vastuussa. Suosittelemme koon muuttamista saman *perheen* makuihin. Esimerkiksi, jos käytät standardiperheen makua, voit muuttaa koon vain toiseen perheen makuun. Kun koon muutos on valmis, virtuaalikoneen tila näyttää aluksi _vahvista koon muutos_. Tässä kohdassa sinun täytyy uudelleen varmistaa, että virtuaalikoneesi koon muutos on toteutettu odotetulla tavalla. Ko

ko muutoksella on virtuaalikoneen käyttökatkos, kunnes koko prosessi on valmis. Huomaa, että koon muuttaminen ei ole niin sulava kuin _käynnistä levystä_ -vaihtoehdon käyttö. Jos tiedät etukäteen, että haluat joskus muuttaa virtuaalikoneiden kokoa, käytä levyltä käynnistämistä, kun virtuaalikonetta käynnistellä antaa enemmän joustavuutta.  
Lisätietoja instanssin koon muuttamisesta [täällä](../../support/faq/how-to-resize-in-pouta.md)

[Pouta-maut ja laskutus]: vm-flavors-and-billing.md
