
# Palomuurien käyttö Pukissa {#using-firewalls-in-pukki}

Kaikilla tietokantaesiintymillä on omat palomuurinsa. Käyttäjien vastuulla on varmistaa, että palomuurisäännöt ovat tiukat. Palomuurisääntöjen tulisi olla auki vain niille IP-osoitteille, joita tarvitaan. Löyhät palomuurisäännöt ovat todennäköisesti yksi suurimmista tietoturvariskeistä, ja ne tulee ottaa vakavasti. Vaikka tietokannassasi ei olisi mitään "salaista" tietoa, sitä ei silti saa jättää avoimeksi maailmalle. Jos haluat jakaa tietojasi, sinun tulisi tehdä se välityspalvelimen tai muiden palveluiden kautta, jotka voivat käyttää tietokantaa taustajärjestelmänä. Tietokantaportin jättäminen auki internetissä on varma tapa houkutella pahantahtoisia toimijoita kohdistamaan hyökkäyksiä tietokantaasi.

## Palomuurien hallinta {#how-to-manage-firewalls}

Voit muuttaa palomuureja [verkkokäyttöliittymässä](https://pukki.dbaas.csc.fi) olemassa olevissa
esiintymissä painamalla "Päivitä esiintymä".

[openstack CLI](cli.md) -työkalulla voit käyttää `opsenstack database instance update --help` -komentoa.
Huomaa, että komento korvaa olemassa olevat palomuurisäännöt, mikä tarkoittaa, että sinun on määritettävä
kaikki palomuurin avaukset joka kerta, kun päivität palomuurit esiintymälle `--allowed-cidr` -lipulla.

## Yksittäinen IP tai verkko-osa {#single-ip-or-subnet}

Lisäämällä "CIDR-ilmaisun" `/32` IP:n loppuun, kuten `192.168.0.1/32`, tarkoittaa, että sallitaan vain kyseinen IP.

On myös mahdollista sallia verkko-osa esimerkiksi `/24`, jos halutaan sallia koko verkko esim.
toimistoverkko. Pienin sallittu maski on `/22`, mikä on 1024 IP-osoitteelle.
Pukki ei salli `0.0.0.0/0`, koska olisi liian helppoa asettaa tämä arvo ja unohtaa, että tietokantaesiintymään pääsee käsiksi koko internetistä.

## Palomuurin avaukset muista CSC-palveluista {#firewall-openings-from-other-csc-services}

Jotta voit käyttää tietokantaasi muista CSC-palveluista, sinun on sallittava jonkin verran saapuvaa liikennettä.
Tämä tehdään sallimalla verkko-osa.

### cPouta {#cpouta}

* Jos palvelimellasi, josta haluat yhdistää tietokantaesiintymiin, on "kelluva IP"
(julkinen IP), sinun on sallittava se IP Pukissa.
* Jos palvelimellasi ei ole kelluvaa IP:tä, sinun on sallittava reitittimien "Ulkoiset kiinteät IP:t".
Voit löytää IP:n Pouta-verkkokäyttöliittymästä kohdasta Verkko -> Reitittimet -> Tietty reititin ->
"Ulkoiset kiinteät IP:t"

### ePouta {#epouta}

On tärkeää muistaa, että kaikki liikenne ePoudasta Pukkiin kulkee "internetin yli",
mikä saattaa olla ristiriidassa sen kanssa miksi valitsit ePoudan käyttääksesi alunperin.

1. Jos haluat silti sallia pääsyn Pukkiin, sinun on varmistettava, että organisaatiosi palomuurit
sallivat liikenteen tietokantaesiintymääsi Pukissa.
2. Jos käytät "julkista IP-aluetta" ePoudassa, voit yksinkertaisesti päivittää tietokantaesiintymäsi
uudella IP-osoitteella "CIDR-ilmaisun" (liite) `/32` kanssa.

### Rahti {#rahti}

Rahti käyttää `86.50.229.150/32` yhteisenä lähtevänä IP-osoitteena. Huomaa, että jos käytät
Rahtia yhteisellä lähtevällä IP-osoitteella, kaikki muut Rahti-asiakkaat voivat päästä käsiksi tietokantaasi,
mikä tekee entistä tärkeämmäksi käyttää vahvaa käyttäjätunnusta ja salasanaa tietokantaasi.

Lisätietoa löytyy [Rahtin turvallisuusoppaasta](../rahti/security-guide.md)

### Noppe {#noppe}
Jos sinun on päästävä käsiksi Pukkisi tietokantaesiintymään Noppesta, sinun on sallittava tämä IP
`193.167.189.137/32`. Huomaa, että myös kaikki muut Notebook-käyttäjät pääsevät tietokantaesiintymiin,
joten on tärkeää käyttää vahvoja salasanoja tietokantakäyttäjissäsi.

### Puhti {#puhti}

Päästäksesi Pukkisi tietokantaan kirjautumis- ja laskentasolmuisista voit sallia tämän:

```
86.50.164.176/28
```

<!--
Jos haluat vieläkin tiukempia sääntöjä, voit rajoittaa sen vain näihin
puhti-nat-[1,2].csc.fi ja puhti-login[11-15].csc.fi
-->

### Mahti {#mahti}

Päästäksesi Pukkisi tietokantaan Mahdilta kirjautumis- ja laskentasolmuisista voit sallia tämän:

```
86.50.165.192/27
```

<!--
Vaihtoehdoista:
86.50.165.192/27
86.50.165.200/30 + 86.50.165.208/28
86.50.165.200/30 + 86.50.165.208/29 + 86.50.165.216/32
86.50.165.200/30 + 86.50.165.211/32 + 86.50.165.212/30 + 86.50.165.216/32
-->

### LUMI {#lumi}

Päästäksesi Pukkisi tietokantaan LUMI:sta sinun on sallittava seuraava CIDR:

```
193.167.209.160/28
```
