# Tietokantainstanssien uudelleenrakentaminen { #rebuilding-database-instances }

## Mitä uudelleenrakennus on? { #what-is-a-rebuild }
Tietokantainstanssin uudelleenrakentaminen Pukissa tarkoittaa käytännössä sen virtuaalikoneen luomista uudelleen, jolla tietokanta toimii, muuttamatta käyttäjän dataa. Tämä on toisinaan tarpeen sellaisten muutosten vuoksi, joita ei muuten voida ottaa käyttöön, esimerkiksi kun jokin komponentti lähestyy elinkaarensa loppua eikä sitä voida vaihtaa ilman käyttökatkoa.

Uudelleenrakennus aiheuttaa tavallisesti noin viiden minuutin käyttökatkon, mutta on silti hyvä varata toimenpiteelle hieman lisäaikaa.

## Huomioitavaa uudelleenrakennusta tehtäessä { #things-to-be-aware-of-when-performing-a-rebuild }
* Uudelleenrakennus on luultavasti monimutkaisin toimenpide, jonka käyttäjät saavat Pukissa tehdä. Tämän vuoksi on suositeltavaa tehdä se virka-aikana, jotta Pukin ylläpitäjät voivat auttaa odottamattomissa ongelmissa.
* Jos uudelleenrakennus kestää yli 15 minuuttia, voit avata tiketin osoitteeseen [servicedesk@csc.fi](mailto:servicedesk@csc.fi) ja liittää mukaan projektinumerosi sekä instanssin tunnisteen, jotta tiedämme, kehen olla yhteydessä ja mistä aloittaa selvitys, jos ilmenisi tarkempaa tutkintaa vaativia ongelmia.
* Tietokantainstanssin tila on `Building` uudelleenrakennuksen ollessa käynnissä.
* Vain ne instanssit, jotka on erikseen merkitty vaativan uudelleenrakennuksen, voidaan rakentaa uudelleen verkkokäyttöliittymästä. Muiden tietokantainstanssien uudelleenrakentamiseen on käytettävä komentorivityökaluja. Katso kohta [alla](#rebuilding-database-instances-using-the-openstack-command-line-client).

## Tietokantainstanssien uudelleenrakentaminen verkkokäyttöliittymän avulla { #rebuilding-database-instances-using-the-web-gui-interface }

1. Siirry [tietokantainstanssien listanäkymään](https://pukki.dbaas.csc.fi/project/).
2. Varmista, että olet valinnut oikean projektin vasemman yläkulman pudotusvalikosta, jos kuulut useaan projektiin.
3. Listanäkymässä kaikissa instansseissa, jotka vaativat uudelleenrakennuksen, oikean laidan sarakkeen painikkeen oletustoimintona on 'Rebuild Instance'. Jos oletustoiminto on jokin muu (yleensä 'Create Backup'), instanssi ei tarvitse uudelleenrakennusta.
4. Rakentaaksesi instanssin uudelleen, paina 'Rebuild Instance' -painiketta. Toimenpiteen odotettu käyttökatko on noin 5 minuuttia.
5. Onnistuneen uudelleenrakennuksen jälkeen oletustoiminto ei enää ole 'Rebuild Instance'.

## Tietokantainstanssien uudelleenrakentaminen OpenStackin komentoriviasiakkaalla { #rebuilding-database-instances-using-the-openstack-command-line-client }
!!! info "Huomio"
    Komentorivityökaluilla on mahdollista suorittaa uudelleenrakennus mille tahansa tietokantainstanssille, myös sellaisille, joita ei ole merkitty sitä vaativiksi.

1. Käytä `show`-komentoa `-c rebuild_required` -lipun kanssa selvittääksesi, tarvitseeko instanssi uudelleenrakennusta:

```txt
openstack database instance show -c rebuild_required $INSTANCE_ID
```

Tulosteen pitäisi näyttää suunnilleen tältä:

```txt
+------------------+-------+
| Field            | Value |
+------------------+-------+
| rebuild_required | True  |
+------------------+-------+
```

Arvo `True` tarkoittaa, että tietokantainstanssi tarvitsee uudelleenrakennuksen.

2. Käytä `rebuild`-komentoa instanssin uudelleenrakentamiseen:

```txt
openstack database instance rebuild $INSTANCE_ID latest
```

Tämän jälkeen uudelleenrakennuksen valmistuminen kestää noin 5 minuuttia, minkä jälkeen instanssin
`operating_status` on `HEALTHY` ja `status` on `ACTIVE`.

Tarkista arvot `show`-komennolla:

```txt
openstack database instance show $INSTANCE_ID
```

3. Kun instanssin `status` on `ACTIVE`, voit käyttää uudelleen `-c rebuild_required` -lippua `show`-komennon kanssa vahvistaaksesi, ettei instanssi enää vaadi uudelleenrakennusta:

```txt
openstack database instance show -c rebuild_required $INSTANCE_ID
+------------------+-------+
| Field            | Value |
+------------------+-------+
| rebuild_required | False |
+------------------+-------+
```

!!! info "Vinkki"
    Voit myös käyttää komentoa `openstack database instance list -vv` saadaksesi listauskomennolta tarkemman tulosteen ja etsiä tulosteesta merkkijonoa `"rebuild_required": true`.