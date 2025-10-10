# VM:n elinkaari ja Cloud BU:iden säästäminen { #vm-lifecycle-saving-cloud-bus }

Tässä artikkelissa selitetään virtuaalikoneinstanssien eri tilat
ja niiden vaikutus resurssien käyttöön.

Kuten muillakin pilvitarjoajilla, myös Poutan virtuaalikoneilla on elinkaari. 
Eri virtuaalikoneiden tiloilla on erilaiset
vaatimukset taustalla olevalle laitteistolle, ja siksi
laskutus on erilaista. Poutan eri tilojen tunteminen
auttaa sinua tekemään parempia päätöksiä infrastruktuurisi ylläpidosta.
Tämä auttaa myös säästämään Cloud-laskutusyksiköitä. 

## Tilat { #states }

Poutan virtuaalikoneiden päätilat:

### Aktiivinen { #active }
Virtuaalikone on aktiivinen, kun se
on *power on* -tilassa. Se pysyy aktiivisena
riippumatta siitä, käytätkö sitä vai et. Aktiivisessa tilassa olevat
virtuaalikoneet käyttävät laskentaresursseja yhdellä laskentasolmuistamme
ja ne laskutetaan normaalisti kuten kohdassa [Pouta flavors and billing](vm-flavors-and-billing.md) on selitetty.

### Sammutettu { #shut-off }
Virtuaalikone ei ole käynnissä ja se on *powered
off*. Kuitenkin *shut off* -tilassa oleva virtuaalikone kuluttaa edelleen
laskutusyksiköitä samalla tavalla kuin **aktiivinen**. Tämä johtuu siitä, että
aktiiviset/sammutetut virtuaalikoneet käyttävät samoja laskentaresursseja
yhdellä laskentasolmuistamme kuten kohdassa [Pouta flavors and billing](vm-flavors-and-billing.md) on selitetty.

!!! warning

    *Shut off* -tilassa oleva virtuaalikone kuluttaa edelleen Cloud-laskutusyksiköitä. 
    Kulutuksen lopettamiseksi valitse *shelved*-tila.

### Keskeytetty (pause) { #pause }
Virtuaalikoneen keskeyttäminen (pause) pysäyttää kaikki virtuaalikoneessa
ajossa olevat prosessit ja tallentaa koko koneen tilan
(muistin, sovellusten tilan jne.) isäntälaskentasolmulle. Et
voi käyttää virtuaalikonetta tai siellä olevia sovelluksia, kun
virtuaalikone on *paused*-tilassa. Jotkin sovellukset voivat
kärsiä sivuvaikutuksista keskeytyksen aikana, joten tätä tilaa ei
suositella tuotantokäyttöön. Jotkin vanhat laskentatyöt
voivat hyötyä pause-tilasta, mutta moderneissa työnkuluissa sitä
ei yleensä käytetä. Pause-tilassa olevaa virtuaalikonetta laskutetaan samalla tavalla
kuin **aktiivista** virtuaalikonetta.

!!! warning

    "Paused"-tilassa oleva virtuaalikone voidaan sammuttaa huoltotoimenpiteiden aikana.

### Keskeytetty (suspend) { #suspend }
Virtuaalikoneen suspendointi tallentaa sen nykyisen tilan
virtuaalikoneen isäntälaskentasolmulle. Virtuaalikone voidaan
palauttaa samaan tilaan kuin ennen keskeytystä, mutta
laskentaresurssit (ytimet, laskentasolmut jne.) voivat olla eri
kuin ennen keskeytystä. Et voi käyttää virtuaalikonetta, kun se on
*suspended*-tilassa. Suspendoituja virtuaalikoneita laskutetaan samalla tavalla
kuin **aktiivisia** virtuaalikoneita. Suspendia ei yleisesti käytetä
moderneissa työnkuluissa.

!!! warning

    "Suspended"-tilassa oleva virtuaalikone voidaan sammuttaa huoltotoimenpiteiden aikana.

### Hyllytetty (shelved) { #shelved }
Hyllyttäminen tarkoittaa virtuaalikoneen sammuttamista ja sen poistamista isäntälaskentasolmulta. 
Tämä vapauttaa virtuaalikoneelle varatut laskentaresurssit. 
Kaikkien muiden siihen liittyvien resurssien tila, esimerkiksi tiedostojärjestelmä,
kelluvat IP-osoitteet, verkko­konfiguraatio jne., tallennetaan kuitenkin keskitettyyn tallennuspalveluumme. 
Huomaa, että virtuaalikoneen hyllyttäminen **ei** vähennä projektin käyttämien
resurssien määrää, vaan ainoastaan kyseisen virtuaalikoneen laskutus lakkaa.

Hyllytys toimii parhaiten standardeilla flavor-vaihtoehdoilla, jotka ovat jo valmiiksi keskitetyn 
tallennuspalvelumme tukemia. Hyllytys voi olla hidasta flavor-vaihtoehdoilla, jotka käyttävät paikallista tallennusta,
varsinkin isommilla fl avoreilla, koska data täytyy kopioida paikallisen ja keskitetyn
tallennuksen välillä. Harvinaisissa tapauksissa, jos kaikki laskentaresurssimme ovat käytössä,
emme välttämättä pysty poistamaan virtuaalikonettasi hyllyltä (unshelve) ennen kuin toinen käyttäjä vapauttaa
laskentaresursseja. Huomaa myös, että kelluvia IP-osoitteita, volum eja jne. ei voi irrottaa
virtuaalikoneesta ennen kuin se on otettu pois hyllyltä. Jos sinulla on kelluvien IP-osoitteiden kiintiö
kaksi ja toinen niistä on liitetty hyllytettyyn virtuaalikoneeseen, sinulla on käytettävissä vain yksi. 
**Huom.** IO- tai TB-flavorien efemeeristä tallennusta ei **hyllytetä**.

### Lopetus { #terminate }
Lopetus (tai poisto) poistaa virtuaalikoneen
projektistasi ja vapauttaa käytössä olleet laskentaresurssit.
Niitä ei voi palauttaa, ja kaikki virtuaalikoneelle tallennettu data
poistetaan, lukuun ottamatta mahdollisesti liitettyjä volumeja. Kun
virtuaalikone on poistettu, sitä ei enää laskuteta.

## Säästä Cloud-laskutusyksiköitä { #save-your-cloud-billing-units }

Alla oleva kuva havainnollistaa tilojen välisiä siirtymiä.

![Virtuaalikoneen elinkaari](../../img/instance-lifecycle-1.png)

Edellä käsiteltiin Poutan virtuaalikoneiden päätilat.
Teoriassa on olemassa myös muita tiloja.
Täydellinen luettelo tiloista ja niiden toiminnasta: [OpenStack documentation](https://developer.openstack.org/api-guide/compute/server_concepts.html).

Tilojen välillä siirtymiseksi sinulla on kaksi päävaihtoehtoa: käytä [Command line client tools](command-line-tools.md) -työkaluja tai käytä verkkokäyttöliittymää.
Verkkokäyttöliittymästä voit siirtää VM:ääsi kaikkiin näihin tiloihin. Poutan verkkokäyttöliittymän etusivulla avaa **Instances**-näkymä. Sarakkeessa **Actions** näet pudotusvalikon, jossa ovat kaikki mahdolliset toiminnot.

![Säästä Cloud-laskutusyksiköitä](../../img/Save-Your-billing-units.png)

On monia muitakin käytäntöjä, jotka auttavat säästämään Cloud-laskutusyksiköitä:

### Automaattinen provisiointi { #automated-provisioning }
Virtuaalikoneidesi automaattinen provisiointi ja konfigurointi
auttaa säästämään Cloud-laskutusyksiköitä. Esimerkiksi
voit purkaa (teardown) käyttämättömät virtuaalikoneesi automaattisen
provisioinnin ja konfiguroinnin avulla, kun et enää tarvitse niitä. Myöhemmin, kun
tarvitset niitä taas, voit ottaa uudet virtuaalikoneet käyttöön
alusta alkaen. Datan tulisi aina sijaita volumella, ja virtuaali­
koneet tulisi käynnistää vain, kun tarvitset laskentaa. 

Esimerkki työnkulun automatisoinnista Heatilla, Ansiblella ja Dockerilla Etherpadin
käyttöönottoon klusteroidulla tietokannalla ja kuormantasauksella: <https://github.com/CSCfi/etherpad-deployment-demo>

### Käynnistä levykuvasta { #boot-from-image }
Hyödyllinen toiminto
Poutassa on oman virtuaalikoneen luominen *Boot from image
(creates new  volume)* -vaihtoehdolla. Tällöin, vaikka poistaisit
virtuaalikoneesi, koko tiedostojärjestelmän tila tallennetaan
pysyvälle volumelle keskitettyyn tallennuspalveluumme. Voit käynnistää uuden
virtuaalikoneen tästä volumesta. Siinä on sama tiedostojärjestelmän
tila kuin aiemmin poistetussa virtuaalikoneessa. Voit myös liittää tämän
volumen mihin tahansa toiseen virtuaalikoneeseen ja käyttää poistetun
virtuaalikoneen tiedostojärjestelmää. Sitä laskutetaan normaalina volumena
Cloud-laskutusyksiköissä, mikä on edullisempaa kuin käynnissä oleva virtuaali­
kone. Virtuaalikoneiden luominen tällä tavalla ja niiden poistaminen,
kun et tarvitse niitä, auttaa säästämään Cloud-laskutusyksikkö­
allokaatiotasi. Suuri etu on, että voit helposti poistaa
virtuaalikoneen ja käynnistää uuden samalla volumella
ja uudella flavorilla. Tämä mahdollistaa helpon skaalauksen
pienemmästä virtuaalikoneen flavorista suurimpiin
flavoreihin.

!!! info

    Tällainen skaalaus ei ole suositeltavaa IO-, GPU- tai TB-flavoreille,
    koska efemeerinen tallennusdata menetetään tässä
    prosessissa.

### Valitse virtuaalikoneellesi sopiva tila { #select-a-suitable-state-of-your-virtual-machine }
Projektisi vaatimuksista riippuen voit vaihtaa virtuaalikoneidesi
tilaa:

-   Jos olet lähdössä pitkälle lomalle ja haluat säästää 
    Cloud-laskutusyksiköitä, voit hyllyttää virtuaalikoneesi.
-   Jos et enää tarvitse virtuaalikonetta, voit poistaa sen
    kopioituasi ensin kaiken oleellisen datan volumelle.

Voit siirtyä eri tilojen välillä Pouta-hallintapaneelissa,
komentorivityökaluilla tai REST API:eilla projektisi asetuksista riippuen. 
Yleisimmät tilat virtuaalikoneille ovat aktiivinen, sammutettu,
hyllytetty ja poistettu. Saattaa esiintyä tilanteita, joissa virtuaalikoneesi
siirtyy _error_-tilaan. Virhetilassa olevista virtuaalikoneista laskutetaan edelleen.
Jos virtuaalikoneesi menee virhetilaan etkä
pysty palauttamaan sitä, ota yhteyttä osoitteeseen cloud-support@csc.fi.

### Muuta virtuaalikoneesi kokoa { #resize-your-virtual-machine }
Virtuaalikoneen koon muuttaminen on
hyödyllinen toiminto Poutassa ja auttaa säästämään
Cloud-laskutusyksiköitä. Projektisi vaatimuksista riippuen voit skaalata virtuaalikonettasi ylös tai
alas muihin fl avoreihin. Skaalaaminen alaspäin, kun laskentakuorma on pieni, vapauttaa
laskentaresursseja ja säästää Cloud-laskutusyksiköitä. Myöhemmin
laskentakuorman kasvaessa voit skaalata virtuaalikoneita ylöspäin. Huomaa, että voit muuttaa kokoa toiseen flavoriin toisesta *family*:sta, mutta tätä **ei suositella lainkaan!**.
Saatat menettää dataa tämän prosessin aikana, eikä CSC vastaa siitä. Suosittelemme muuttamaan kokoa vain saman
*family*n flavoreihin. Jos käytät esimerkiksi standardi-
familyn flavorea, voit muuttaa sen vain toiseen standardi-familyn
flavoriin. Kun koon muutos valmistuu, virtuaalikoneen tila näyttää ensin
_verify resize_. Tässä vaiheessa sinun täytyy vahvistaa, että
virtuaalikone on muuttunut odotetulla tavalla. Koon muuttaminen aiheuttaa
katkon virtuaalikoneelle, kunnes koko prosessi on
valmis. Huomaa, että koon muuttaminen ei ole yhtä jouhevaa kuin yllä kuvattu _boot
from volume_ -vaihtoehto. Jos tiedät etukäteen, että haluat joskus muuttaa
virtuaalikoneiden kokoa, käynnistäminen volumelta
virtuaalikonetta luotaessa antaa enemmän
joustavuutta.  
Lisätietoja instanssin koon muuttamisesta [täältä](../../support/faq/how-to-resize-in-pouta.md)

  [Pouta flavors and billing]: vm-flavors-and-billing.md