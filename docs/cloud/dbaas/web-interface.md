# Pääsy DBaaS:ään verkkoliittymästä {#getting-started-with-dbaas-from-the-web-interface}

Voit kirjautua DBaaS:ään menemällä osoitteeseen [pukki.dbaas.csc.fi](https://pukki.dbaas.csc.fi).

## Uuden tietokanta-instanssin luominen {#creating-a-new-database-instance}

Vasemmanpuoleisessa sarakkeessa voit siirtyä kohtaan `Database` -> `Instances` ja sitten painaa oikealla puolella olevaa `Launch Instance`. Nyt voit määrittää haluamasi asetukset tietokannallesi:

1. `Instance name` - Mikä tahansa, minkä haluat instanssille nimeksi.
2. `Volume size` - Kuinka paljon levytallennustilaa tietokantaa varten tarvitaan. Jos haluat vain testata DBaaS:ää, 1 GiB riittänee. Koon kasvattaminen myöhemmin vaatii käyttökatkon tietokannalle. Jos jo tiedät, kuinka paljon dataa käytät, on helppo arvioida, kuinka suuri tallennustila on tarpeen.
3. `Volume type` - Tämän voi jättää tyhjäksi.
4. `Datastore` - Minkä tyyppisen tietokannan haluat. Suositellaan käytettävän viimeisintä versiota suosikkitietokannastasi, ellei ole erityistä syytä käyttää vanhempaa versiota. Pukki tukee tällä hetkellä [PostgreSQL](postgresql.md) ja [MariaDB](mariadb.md).
5. `Flavor` - Kuinka suuria tietokanta-instansseja tarvitset. Pieniä käyttötilanteita varten `standard.small` on todennäköisesti riittävä. Jos myöhemmin huomaat, ettei se ole tarpeeksi suuri, voit aina muuttaa sitä. Flavorin muuttaminen vaatii käyttökatkon.
6. `Locality` - Ei tarvita. Tulevaisuudessa DBaaS tukee klusteroituja tietokantoja, jolloin anti-affiniteetti on useimmissa tapauksissa suositeltava vaihtoehto.

Seuraavalla sivulla `Database access`:

7. `Allowed CIDRs` - Tähän voit lisätä sallitut IP-osoitteesi muodossa `$IP/32`, jos haluat sallia useita IP-osoitteita. Ne täytyy erottaa pilkulla `,`. Oletuksena tietokannat luodaan ilman `Allowed CIDRs` -määrityksiä, mikä tarkoittaa, ettei tietokantaan voi yhdistää.

Kolmannella sivulla `Intialize Databases`:

8. Kentässä `Initial Databases` voit kirjoittaa, mitkä tietokannat tulisi alustaa. Voit lisätä lisää tietokantoja sen jälkeen, kun instanssi on käynnistynyt.
9. `Initial Admin User` lisää ensimmäisen käyttäjän, jota haluat käyttää tietokantaan yhdistämiseen. Voit lisätä lisää käyttäjätilejä sen jälkeen, kun tietokanta-instanssi on käynnistynyt.
10. `Password` ensimmäiselle käyttäjällesi. Varmista, ettei tätä salasanaa ole käytetty missään muualla.
11. `Allowed Host (optional)` , tätä ominaisuutta ei tällä hetkellä tueta, mutta tulevaisuudessa on mahdollista rajoittaa käyttäjien pääsyä IP-osoitteen perusteella.

Neljännellä sivulla `Advanced`:

12. Sinun ei tarvitse tehdä mitään, mutta on mahdollista käynnistää uusi tietokanta varmuuskopiosta. Jos valitset tietokannan käynnistämisen varmuuskopiosta, sinun ei tarvitse määrittää `Initial Admin User`, `Password` tai `Initial Databases`.
13. Nyt voit painaa `Launch`.
14. Kun tietokanta-instanssi on käynnistynyt, voit klikata tietokanta-instanssin nimeä ja hallita lisäominaisuuksia, kuten käyttäjiä, varmuuskopioita jne. Instanssin käynnistyminen ja toimintavalmius saattaa kestää muutaman minuutin.
15. Nyt voit siirtyä tietokantakohtaiseen dokumentaatioon löytääksesi lisäohjeita tietokannan käyttämiseen:

   * [PostgreSQL](postgresql.md)
   * [MariaDB](mariadb.md)

## Käyttäjätilien muokkaus tietokanta-instanssissa {#modify-user-accounts-in-the-database-instance}

Voit lisätä, poistaa ja muokata käyttäjiä tietokanta-instanssien käyttäjät-välilehdellä. Varmista, että käytät vahvoja salasanoja jokaiselle käyttäjälle.

## Tietokantojen lisääminen ja poistaminen {#add-and-remove-databases}

Voit lisätä ja poistaa tietokantoja tietokanta-instanssien `Database`-välilehdeltä.