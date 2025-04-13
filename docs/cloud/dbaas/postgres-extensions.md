# PostgreSQL-laajennukset {#postgresql-extensions}

## Laajennusten ottaminen käyttöön {#enabling-extensions}

1. [Ota root-käyttäjä käyttöön](operations.md#enable-root).
2. [Kirjaudu tietokantaan root-käyttäjänä](postgres-accessing.md#command-line).
3. Käytä seuraavaa komentoa laajennusten ottamiseksi käyttöön:
   ```
   CREATE EXTENSION $EXTENSION_NAME ;
   ```
4. Poista root käytöstä, kun olet ottanut laajennukset käyttöön.

## Tällä hetkellä saatavilla olevat laajennukset {#currently-available-extensions}

Jos tästä puuttuu laajennuksia, joita haluaisit nähdä Pukissa käytettävissä, ota yhteyttä [CSC Service Deskiin](../../support/contact.md).
Huomioi, että laajennuslista perustuu uusimpaan PostgreSQL-versioon, ja saatavilla olevat laajennukset saattavat poiketa vanhemmissa versioissa.

<!-- Tämän laajennuslistan voi helposti luoda seuraavalla komennolla:
SELECT '| ' || name  AS name, comment || ' |' as comment FROM pg_available_extensions ORDER BY name;
--->
| Laajennuksen nimi  | Laajennuksen kuvaus |
|:--- |:--- |
| address_standardizer           | Käytetään osoitteen jäsentämiseen sen osatekijöihin. Yleisesti käytetty geokoodauksen osoitenormitointivaiheessa. |
| address_standardizer-3         | Käytetään osoitteen jäsentämiseen sen osatekijöihin. Yleisesti käytetty geokoodauksen osoitenormitointivaiheessa. |
| address_standardizer_data_us   | Address Standardizer US dataset example |
| address_standardizer_data_us-3 | Address Standardizer US dataset example |
| amcheck                        | funktiot suhteen eheyden tarkistamiseksi |
| autoinc                        | funktiot automaattisesti lisättävissä kentissä |
| bloom                          | bloom-hakumetodi - allekirjoitustiedostoon perustuva indeksi |
| btree_gin                      | Tuetaan yleisten tietotyyppien indeksointia GIN:ssä |
| btree_gist                     | Tuetaan yleisten tietotyyppien indeksointia GiST:ssä |
| citext                         | tietotyyppi kirjainkoolla erotukselle immuuneille merkkijonoille |
| cube                           | tietotyyppi moniulotteisille kuutioille |
| dblink                         | yhdistä muihin PostgreSQL-tietokantoihin tietokannan sisällä |
| dict_int                       | tekstinhakukirjaston sanakirjamalli kokonaisluvuille |
| dict_xsyn                      | tekstinhakukirjaston laajennettujen synonyymien prosessoinnin sanakirjamalli |
| earthdistance                  | suuren ympyrän välimatkojen laskeminen Maan pinnalla |
| file_fdw                       | vieraan tietoaineiston kansio tasotiedoston pääsyyn |
| fuzzystrmatch                  | määritä samankaltaisuus ja etäisyys merkkijonojen välillä |
| h3                             | H3-sidonnat PostgreSQL:lle |
| h3_postgis                     | H3 PostGIS-integraatio |
| hstore                         | tietotyyppi (avain, arvo) -parien tallentamiseen |
| insert_username                | funktioita muuttajaiden seuraamiseksi taulukossa |
| intagg                         | kokonaislukujen aggregaattori ja luetteloija (vanhentunut) |
| intarray                       | funktiot, operaattorit ja indeksituki kokonaislukutaulukoille |
| isn                            | tietotyypit kansainvälisille tuotenumerointisäännöille |
| lo                             | Suurten objektien ylläpito |
| ltree                          | tietotyyppi hierarkkisille puurakenteille |
| moddatetime                    | funktioita viimeisen muokkausajan seuraamiseen |
| pageinspect                    | tutki tietokantasivujen sisältöä alapinnalla |
| pg_buffercache                 | tutki jaettua välimuistia |
| pg_freespacemap                | tutki vapaata tilakarttaa (FSM) |
| pg_prewarm                     | esilämmittää suhdetiedot |
| pg_stat_statements             | seuraa kaikkien SQL-lausekkeiden suunnittelu- ja suoritustilastoja |
| pg_surgery                     | laajennus, jolla korjat mullistettua suhdetta |
| pg_trgm                        | tekstisamankaltaisuuden mittaus ja trigrammeihin perustuva hakemisto |
| pg_visibility                  | tutki näkyvyyskarttaa (VM) ja sivutason näkyvyystietoja |
| pg_walinspect                  | funktiot PostgreSQL:n Write-Ahead Log -sisältöjen tarkasteluun |
| pgcrypto                       | kryptografiset funktiot |
| pgrowlocks                     | näyttää rivitason lukitustiedot |
| pgstattuple                    | näyttää tuple-tason tilastoja |
| plpgsql                        | PL/pgSQL proseduurikieli |
| postgis                        | PostGIS-geometria- ja maantieteelliset tietotyypit ja funktiot |
| postgis-3                      | PostGIS-geometria- ja maantieteelliset tietotyypit ja funktiot |
| postgis_raster                 | PostGIS rasterityypit ja funktiot |
| postgis_raster-3               | PostGIS rasterityypit ja funktiot |
| postgis_sfcgal                 | PostGIS SFCGAL-funktiot |
| postgis_sfcgal-3               | PostGIS SFCGAL-funktiot |
| postgis_tiger_geocoder         | PostGIS tiger-paikannus- ja vastapaaikannustoiminnot |
| postgis_tiger_geocoder-3       | PostGIS tiger-paikannus- ja vastapaaikannustoiminnot |
| postgis_topology               | PostGIS topologiset tilarakenne- ja -funktiot |
| postgis_topology-3             | PostGIS topologiset tilarakenne- ja -funktiot |
| postgres_fdw                   | vieraan tietoaineiston kansio kauko-PostgreSQL-palvelimille |
| refint                         | funktiot viite-eheyden toteuttamiseen (vanhentunut) |
| seg                            | tietotyyppi viivasegmenttien tai liukulukualueiden esittämiseen |
| sslinfo                        | tietoja SSL-sertifikaateista |
| tablefunc                      | funktiot, jotka käsittelevät kokonaisia taulukoita, mukaan lukien crosstab |
| tcn                            | kytketyt muutosilmoitukset |
| tsm_system_rows                | TABLESAMPLE-menetelmä, joka hyväksyy rivien määrän rajaksi |
| tsm_system_time                | TABLESAMPLE-menetelmä, joka hyväksyy ajan millisekunteina rajaksi |
| unaccent                       | tekstinhakukirjasto, joka poistaa aksentit |
| uuid-ossp                      | luo universaalisti uniikit tunnisteet (UUID:t) |
| xml2                           | XPath-kyselyt ja XSLT |

## Parametrit, joita käyttäjät voivat muokata {#parameters-that-users-can-modify}

DBaS sallii käyttäjien muokata joitakin parametreja.
Jos on joitakin parametreja, joita mielestäsi pitäisi voida muokata, [ota yhteyttä](../../support/contact.md) ja katsomme, voimmeko tehdä sen mahdolliseksi.
Oletuksena oletamme, että oletusparametrit ovat järkeviä, eivätkä käyttäjät tavanomaisissa olosuhteissa saisi muokata mitään näistä parametreista.

| Parametrit           | Oletus | Vaatii uudelleenkäynnistyksen | Kommentit |
|:--- |:---:|:---|:---|
| maintenance_work_mem | 64MB  | Ei  | |
| max_connections      | 100   | Kyllä | Yleensä suositellaan käytettäviksi yhteyspuoleja tämän arvon muuttamisen sijaan |
| work_mem             | 4MB   | Ei  | |
| log_statement        | false | Ei  | Tämä on hyödyllinen, jos haluat selvittää lisää, miten tietokantaasi käytetään |
| log_statement_stats  | false | Ei  | Tämä kerää myös tilastoja tietokannastasi, tämän suositellaan pidettävän väärässä, koska se saattaa vaikuttaa suorituskykyyn |

## Joitain hyödyllisiä komentoja {#some-useful-commands}

**Saatavilla olevien laajennusten listaaminen**

```sql
SELECT name, default_version, comment FROM pg_available_extensions ORDER BY name;
```

**Käytössä olevien laajennusten listaaminen**

```sql
SELECT * from pg_extension ORDER BY extname;
```

**Laajennuksen luominen**

```sql
CREATE EXTENSION ${EXTENSION_NAME};
```

**Laajennuksen poistaminen käytöstä**
```sql
SELECT * FROM table1 LIMIT 1 \gx
