
# CSC käyttäjätilin elinkaari {#csc-user-account-lifecycle}

!!! note
    CSC lähettää ilmoituksia ja ohjeita sähköpostitse hyvissä ajoin ennen kuin
    käyttäjätilit tai salasanat vanhenevat. Pidä sähköpostiyhteystietosi ajan
    tasalla. Jos sinulla on ongelmia tilien tai kirjautumisten kanssa, ota yhteyttä
    [CSC Service Desk](../support/contact.md).

CSC käyttäjätilisi salasana on voimassa yhden vuoden. Saat CSC:ltä ilmoituksia,
kun salasanasi on vanhenemassa. Vanhentunut salasana ei estä sinua käyttämästä
CSC käyttäjätiliäsi, jos käytät jotain seuraavista kolmesta kirjautumismenetelmästä:
Haka, Virtu tai SSH-avainpari. Nämä kolme kirjautumismenetelmää ohittavat
käytännössä CSC käyttäjätilin salasanan tarpeen. **Suosittelemme kuitenkin
vahvasti vaihtamaan salasanasi ajoissa**.

Jos CSC käyttäjätilisi salasana vanhenee etkä voi kirjautua Hakan, Virtun tai SSH-avaimien kautta, 
ota yhteyttä [CSC Service Desk](../support/contact.md).

[MyCSC](https://my.csc.fi) on asiakasportaalimme, jossa asiakkaamme voivat
tarkastella projektiensa tilannetta ja käyttäjätiliensä tietoja. MyCSC:ssä voit
myös [vaihtaa CSC käyttäjätilisi salasanan](how-to-change-password.md).
MyCSC ja muut CSC:n palvelut tarjoavat yhden tai useamman alla mainitun
kirjautumismenetelmän.

## CSC käyttäjätili {#csc-user-account}

Tässä kirjautumismenetelmässä käytät CSC:n luomaa käyttäjätiliä ja
asettamaasi salasanaa. Kaikilla käyttäjillä, joilla on pääsy CSC:n palveluihin,
on CSC käyttäjätili, vaikka he käyttäisivät vain jotain alla mainituista
kirjautumismenetelmistä.

## Haka {#haka}

Tämä kirjautumismenetelmä on saatavilla suomalaisille yliopistoille,
ammattikorkeakouluille ja tutkimuslaitoksille. Tässä menetelmässä käytät
kotiorganisaatiosi käyttäjätiliä ja salasanaa CSC:n tarjoaman tilin sijaan.
Tämä toimii, koska ainutlaatuinen käyttäjätunnus kotiorganisaatiostasi on
liitetty CSC käyttäjätiliisi.

Jos käytät tätä kirjautumismenetelmää, sinun täytyy kirjautua CSC:n palveluihin
Hakan kautta vähintään kerran puoleen vuoteen, jotta CSC käyttäjätilisi pysyy
aktiivisena.

## Virtu {#virtu}

Tämä kirjautumismenetelmä on saatavilla valtion virastoille. Samankaltaisesti
kuin Haka, tässä menetelmässä käytät kotiorganisaatiosi käyttäjätiliä ja
salasanaa CSC:n tarjoaman tilin sijaan. Tämä toimii, koska ainutlaatuinen
käyttäjätunnus kotiorganisaatiostasi on liitetty CSC käyttäjätiliisi.

Jos käytät tätä kirjautumismenetelmää, sinun täytyy kirjautua CSC:n palveluihin
Virtun kautta vähintään kerran puoleen vuoteen, jotta CSC käyttäjätilisi pysyy
aktiivisena.

## LS Login {#ls-login}

LS Login on Euroopan biotieteiden tutkimusinfrastruktuurien
(LS RI) autentikointipalvelu, joka on EOSC-Life-hankkeen kautta
perustettu yhteisöalusta ja jota ylläpitää Masarykin yliopisto, Brno, CZ.
Myös tässä menetelmässä ainutlaatuinen LS Login -käyttäjätunnus on liitetty
CSC käyttäjätiliisi, mikä mahdollistaa autentikoinnin CSC:n palveluissa.

## SSH-avaimet {#ssh-keys}

SSH-avaimet ovat toiminnallisesti samankaltaisia käyttäjätunnusten ja salasanojen
kanssa ja tarjoavat keinon käyttää CSC:n järjestelmiä turvallisesti, mutta ilman
tarvetta kirjoittaa käyttäjätunnusta ja salasanaa manuaalisesti joka kerta. Vain
tietty alajoukko CSC:n palveluista tukee SSH-avaimia. Esimerkiksi ne eivät ole
tuettuja yhdessäkään selaimen perustuvassa kirjautumismenetelmässä.

SSH-avaimet on liitetty CSC käyttäjätiliisi ja ne toimivat vertaamalla
julkista avainta, jonka olet ladannut tiettyyn CSC-järjestelmään, siihen
yksityiseen avaimeen, jonka säilytät turvallisesti paikallisella tietokoneellasi.

[Katso ohjeet SSH-avainten asettamiseksi](../computing/connecting/ssh-keys.md).

## Käyttäjätilien vanheneminen {#expiration-of-user-accounts}

Jos sinulle on myönnetty tili määräajaksi, tili vanhentuu ajanjakson päättyessä.
Haka- tai Virtu kirjautumismenetelmillä luodut tilit validoidaan säännöllisesti.
Seuraavia menetelmiä voidaan itsenäisesti käyttää kirjautumiseen palveluista
riippuen: Haka, Virtu, salasana tai SSH-avaimet.

Käyttäjätilit voidaan sulkea, jos niiden omistajaan ei saada yhteyttä, esimerkiksi
kun sähköpostit palaavat takaisin.

!!! note
    Jos haluat lopettaa tilisi, ota yhteyttä [CSC Service Desk](../support/contact.md).
