
# PostgreSQL-versiot

Tällä hetkellä Pukki tukee kahta suurta PostgreSQL-versiota, 14 ja 17. Suosittelemme aina käyttämään uusinta saatavilla olevaa versiota, kun luodaan uusia tietokantaesiintymiä, ja olemassa olevia voidaan päivittää käyttämään uudempia vähäisiä tai suuria versioita. Lisätietoja kaikista PostgreSQL-versioiden eroista saat [PostgreSQL-dokumentaatiosta](https://www.postgresql.org/docs/release/).

## Vähäiset versioiden päivitykset {#minor-version-upgrades}

Vähäisillä versiopäivityksillä PostgreSQL:ssä (esim. 14.12:sta 14.13:een) ei pitäisi olla rikkoontuvia muutoksia. Itse päivitysprosessi tapahtuu automaattisesti taustalla, kun aloitettu, ja sen pitäisi kestää vain muutama minuutti. Se sisältää olemassa olevan palvelimen sulkemisen, uuden version asentamisen ja palvelimen käynnistämisen uudelleen muuttamatta tietoja millään tavalla.

## Suuret versioiden päivitykset {#major-version-upgrades}

Suuret versiepäivitykset eivät saisi olla Pukki-käyttäjälle näkyvästi erilaisia kuin vähäiset versiopäivitykset, mutta kulissien takana tapahtuu paljon enemmän, ja prosessissa on lisääntynyt riski, että jokin menee pieleen. On olemassa todellinen tietojen menetyksen riski, ja käyttäjän tulisi olla valmis luomaan uusi tietokantaesiintymä varmuuskopiosta tällaisessa tapauksessa.

Ennen kuin päivität tietokantasi uuteen suureen versioon, suosittelemme vahvasti käyttämään varmuuskopiota uuden tietokantaesiintymän luomiseen vain päivityksen testaamista varten. Suurten versioiden välinen päivitys vaatii huomattavasti enemmän levytilaa kuin vähäiset versiopäivitykset, ja jos levytilaa ei ole tarpeeksi, päivitys epäonnistuu. Näissä tapauksissa on välttämätöntä lisätä tilavuuden kokoa ennen suurten versioiden päivitystä.

Edelliseen suureen versioon palauttaminen ei ole mahdollista Pukissa. Ainoa tapa palata vanhempaan suureen versioon on palauttaa vanha varmuuskopio ennen päivitystä.

## Muutokset PostgreSQL 14:n ja 17:n välillä {#changes-between-postgresql-14-and-17}

Suurin osa muutoksista PostgreSQL:ssä versioiden 14 ja 17 välillä ei ole käyttäjälle näkyvissä. Monet niistä keskittyvät palvelinpuolen suorituskykyyn, lokitukseen ja kehittyneempiin ja erityisiin SQL-ominaisuuksiin. PostgreSQL 15 toi kuitenkin erittäin erityisen muutoksen oletuslupiin, mikä vaikuttaa siihen, kuinka Pukki hallitsee käyttäjiä ja heidän käyttöoikeuksiaan.

Pidä mielessä, kun päivität tietokannan PostgreSQL 14:stä 17:ään, että olemassa olevat käyttöoikeudet säilyvät ennallaan. Tämä tarkoittaa, että uusi PostgreSQL 17 -esiintymä eroaa joissakin asioissa verrattuna sellaiseen, joka on päivitetty PostgreSQL 14:stä. Voit lukea lisää tästä [käyttöoikeussivulta](postgres-permissions.md).

## Joitakin hyödyllisiä komentoja {#some-useful-commands}

### Näytä nykyinen tietokantaversio {#show-the-current-database-version}

```sql
SELECT 1;
```

### Tuo tietokantadump

Jos sinulla on tietokantadump, voit tuoda sen Pukki-tietokantaasi seuraavalla komennolla. Huomioi, että tämä saattaa korvata jo tietokannassa olevan sisällön:

```bash
psql -h $FLOATING_IP -d $DATABASE -U USERNAME -f file.sql
```
