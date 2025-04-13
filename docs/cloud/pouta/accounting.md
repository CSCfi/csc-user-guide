# Kirjanpitoperiaatteet ja kiintiöt {#accounting-principles-and-quotas}

Tämä asiakirja kuvaa, kuinka Pouta-palveluiden resurssien käyttö lasketaan laskentayksiköinä (BU).

Akatemiallisen tutkimuksen asiakkaat voivat saada resurssikäyttönsä maksettua Opetus- ja kulttuuriministeriön toimesta. Kaupallisille asiakkaille ja akateemisille asiakkaille, jotka tarvitsevat ministeriön maksamaa siirtoa enemmän, CSC:llä on myynnissä laskentayksikköpaketteja.

Lisätietoja siitä, mihin kategoriaan projektisi kuuluu, löydät kohdasta
[Tilien ja projektien hallinta](https://research.csc.fi/accounts-and-projects){ target="_blank" }.

[TOC]

## Resurssien laskenta {#accounting-for-resources}

Tällä hetkellä laskemme virtuaalikoneet, tallennusvolyymit, objektitallennuksen ja kelluvat IP-osoitteet.

| Resurssi | Kustannus |
|-----------------|---------------------|
| Virtuaalikoneet | Katso [Tyypit](vm-flavors-and-billing.md) |
| Tallennusvolyymit | 3,5 BU / TiB tunti |
| Kelluvat IP:t | 0,2 BU / tunti |

Huomaa, että virtuaalikoneet kuluttavat laskentayksiköitä riippumatta siitä, käytätkö niitä vai et. Tämä tarkoittaa, että sammutettuna tai keskeytettynä oleva virtuaalikone kuluttaa edelleen laskentayksiköitä. Lisätietoa virtuaalikoneiden eri tiloista ja niiden laskentayksiköiden kulutuksesta löydät kohdasta
[Virtuaalikoneen elinkaari](vm-lifecycle.md). Virtuaalikoneen vähimmäislaskenta-aika on yksi tunti. Toinen resurssikäytön arviointilähde on
[Resurssilaskuri](https://research.csc.fi/billing-units/#buc).

Tallennusvolyymit kuluttavat laskentayksiköitä koon perusteella. Mittayksikkö on [TebiTavua](https://en.wikipedia.org/wiki/Tebibyte) tunteja. Tallennusvolyymit kuluttavat laskentayksiköitä myös silloin, kun ne eivät ole kiinnitettyinä virtuaalikoneisiin.

Objektitallennus kuluttaa laskentayksiköitä tallennetun datamäärän perusteella. Laskentayksiköitä kuluu siihen asti, kunnes data poistetaan.

Kelluvat IP-osoitteet laskutetaan, jos ne on allokoitu projektille tai liitetty virtuaalikoneeseen. Kaikki ylimääräiset reitittimet, jotka luot ja yhdistät ulkoiseen verkkoon, laskutetaan myös yhdestä kelluvasta IP:stä. Projektin oletusreititin ei kuluta laskentayksiköitä.

## Muut kustannukset {#other-costs}

Jos sinulla on sopimus CSC:n kanssa, sinut laskutetaan aina sopimuksen mukaan, vaikka se poikkeaisi näistä käytännöistä. Kaupallisia asiakkaita laskutetaan yleensä myös maksulla projektin jokaisesta jäsenestä.

## Kiintiöt {#quotas}

Jokaisella cPouta- ja ePouta-projektilla on pilvilaskennan kiintiö, joka rajoittaa samanaikaisten pilviresurssien käyttöä. On olemassa oletus cPouta-projektin kiintiö, joka on varsin pieni, mutta käyttäjät voivat hakea laajennuksia lähettämällä sähköpostia [CSC Service Desk](../../support/contact.md).

**cPouta-projektin oletuskiintiön koko.**

| Resurssityyppi | oletus |
|-----------------|:-------:|
| Instanssit | 8 |
| Ytimet | 8 |
| Muisti | 32 GB |
| Kelluvat IP:t | 2 |
| Tallennus | 1 TB |

Oletusresurssien avulla cPouta-käyttäjä voi käynnistää kahdeksan *standard.tiny*-instanssia tai kaksi *standard.large*-instanssia tai yhden *hpc-gen1.8core*-instanssin. Kiintiön tarkoituksena on estää yksittäisiä käyttäjiä varaamasta koko klusteria ja siten estämästä muita käyttäjiä pääsemästä siihen käsiksi.

Myös tallennusta rajoittaa kiintiö. Uusien projektien oletuskiintiö on 1 TB. Lisäallokointeja voi pyytää lähettämällä sähköpostia [CSC Service Desk](../../support/contact.md).

ePouta-projektien alkuperäiset kiintiöt sovitaan uuden projektin alussa.

Huomaa, että vapaa kiintiö ei takaa, että tietyt resurssit ovat saatavilla.

Tietyt virtuaalikonetyypit voivat olla täysiä, joten et voi provisioida niitä, vaikka sinulla olisi niiden kiintiö käytettävissäsi. Pyrimme aina siihen, että joitakin tyyppejä on saatavilla vapaana. Suunnittelemme parantavamme saatavilla olevien tyyppien näkyvyyttä tulevaisuudessa.

Pyrimme aina siihen, että varastointiresurssit ja kelluvat IP-resurssit ovat vapaita, jos niille on allokoitu kiintiö.