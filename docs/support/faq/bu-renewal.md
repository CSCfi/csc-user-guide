# Kysymyksiä ja vastauksia laskentayksikköuudistuksesta (2025) { #questions-and-answers-related-to-the-billing-unit-renewal-2025 }

## 1. Mitkä ovat uudet laskentayksiköt? { #1-what-are-the-new-billing-units }

Uudet laskentayksikkötyypit (BU) ovat **CPU**, **GPU**, **Cloud** ja
**Storage**. Toisin sanoen CSC:n tutkimuspalvelut kuluttavat eri
laskentayksiköitä sen mukaan, mitä palveluja käytetään. Yhteenveto siitä,
mitä palvelu käyttää mitäkin yksikköä, on alla:

* **CPU-laskentayksikkö**
    * Puhti-, Mahti- ja Roihu-ajot *ilman GPU:ta*
* **GPU-laskentayksikkö**
    * Puhti-, Mahti- ja Roihu-ajot *GPU:lla*
* **Cloud-laskentayksikkö**
    * cPouta, ePouta, Rahti, Pukki DBaaS, SD Desktop
* **Storage-laskentayksikkö**
    * Puhti-, Mahti- ja Roihu-Lustre-tallennus, Allas, Shared fileservice, SD
      Connect

!!! info "Huom."
    Tämä laskentayksikköuudistus ei **vaikuta** LUMIn laskutukseen. Samantyyppinen
    resurssileikkuri kuin [alla](#cutter) kuvattu otetaan kuitenkin käyttöön
    LUMIssa 1.10.2025 alkaen.

## 2. Milloin uudet laskentayksiköt otetaan käyttöön? { #2-when-are-the-new-billing-units-taken-into-use }

Uudet laskentayksiköt otetaan käyttöön alkaen **29.9.2025**. Tarkempi aikataulu:

* **Ma 29.9.** Laskentayksikköhakemukset MyCSC:ssä suljetaan tilapäisesti
* **Ke 1.10.** Vanhat hakemukset käsitellään ja projekteille myönnetään uudet
  laskentayksiköt
* **To 2.10.** Uudet laskentayksiköt otetaan käyttöön MyCSC:ssä ja palveluissa,
  resurssihakemukset uusille laskentayksiköille avataan

## 3. Pitääkö minun tehdä jotain? Mitä vanhoille laskentayksiköilleni tapahtuu? { #3-will-i-need-to-do-something-what-will-happen-to-my-old-billing-units }

Ei, sinun ei tarvitse tehdä mitään. Projekteille jo myönnetyt, käyttämättömät
laskentayksiköt siirretään uusiin yksiköihin, eli myönnetyt resurssit eivät
katoa. Vanhat BU:t kohdistetaan uusiin BU:ihin projektin aiemman käytön
perusteella. Toisin sanoen esimerkiksi Puhtissa vain GPU-ajoja suorittavat
projektit eivät saa Cloud-laskentayksiköitä, joille niillä ei ole käyttöä.

Voit tarkistaa nykyisen BU-budjettisi [MyCSC](https://my.csc.fi)-palvelusta sekä
Puhtissa ja Mahtissa komennolla `csc-projects`.

## 4. Miten BU-uudistus vaikuttaa CSC:n palveluihin? { #4-how-will-the-bu-renewal-affect-cscs-services }

Siirtymä uusiin laskentayksiköihin vaikuttaa palveluiden käyttöön vain vähän ja
palvelut ovat käytettävissä normaalisti. Resurssihakemukset eivät kuitenkaan ole
käytettävissä siirron aikana, kun vanhat laskentayksiköt muunnetaan uusiksi.

## 5. Miten uudet laskentayksiköt vaikuttavat resurssihakemuksiin? { #5-how-will-the-new-billing-units-affect-resource-applications }

Jatkossa resurssihakemukset tehdään neljässä uudessa laskentayksikössä. Tämä
tarkoittaa, että käyttäjien on pohdittava, millaisia resursseja ja palveluja he
tarvitsevat ennen hakemista.

Lisäksi eri resurssien hakurajoitukset erotellaan kunkin
laskentayksikkötyypin alla käytettävissä olevan kapasiteetin perusteella. Tähän
asti kaikki laskentayksikköhakemukset on käsitelty sen mukaan, ovatko ne S-, M-
vai L-kokoisia hakemuksia. Sen sijaan cPoudassa käytetty 1 miljoona BU:ta
kuormittaa palvelukapasiteettia huomattavasti enemmän kuin sama määrä BU:ta
Mahtin CPU-solmuilla. Siksi resurssihakemusten kokorajat perustuvat jatkossa
haettavan laskentayksikön tyyppiin.

## 6. Menetänkö laskentayksiköitä uudelle BU-leikkurille, vaikka projektini käyttävät laskentayksiköitä? { #6-will-i-lose-billing-units-to-the-new-bu-cutter-even-if-my-projects-use-billing-units } <a id="cutter"></a>

Uudistuksessa otetaan käyttöön “leikkuri”, joka poistaa käyttämättömiä BU:ita.
Laskentayksikköleikkuri koskee vain projekteja, jotka ovat käyttäneet
**alle 40 % laskentayksiköistään** kuuden kuukauden jaksolla, joka lasketaan
viimeisimmästä laskentayksikkömyönnöstä tai leikkaustarkistuksesta. Jos projekti
on käyttänyt enemmän, resursseja ei leikata. Leikkuri koskee vain akateemisia
projekteja; opiskelija- ja kurssiprojektit ovat tämän ulkopuolella.

## 7. Milloin ensimmäinen laskentayksikköleikkaus tehdään? { #7-when-will-the-first-billing-unit-depreciation-happen }

Laskentayksikköleikkuri otetaan käyttöön samaan aikaan uusien yksiköiden kanssa,
joten ensimmäiset leikkaukset tapahtuvat aikaisintaan **maaliskuussa 2026**.
Projektien laskentayksikköjen käyttö tarkistetaan kuuden kuukauden kuluttua
joko viimeisimmästä laskentayksikkömyönnöstä tai edellisestä
leikkaustarkistuksesta.

## Lisätietoja { #more-information }

* Dokumentaatio: [CSC:n palvelujen laskutus](../../accounts/billing.md)
* Blogi: [Laskentayksikköuudistuksen aikataulu ja muutokset](https://research.csc.fi/2025/06/02/billing-unit-renewal-schedule-and-changes/) (Research.csc.fi)