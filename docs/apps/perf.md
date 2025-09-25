---
tags:
  - Free
catalog:
  name: perf
  description: Command line tool for performance analysis
  description_fi: Komentorivityökalu suorituskyvyn analysointiin
  license_type: Free
  disciplines:
    - Miscellaneous
  available_on:
    - LUMI
    - Puhti
    - Mahti
---

# perf { #perf }

[`perf`](https://perfwiki.github.io/main/) on suorituskyvyn seurantatyökalu Linux-järjestelmille.
Se tarjoaa pääsyn Performance Monitor Unitin (PMU) laitelaskureihin ja mahdollistaa kevyen suorituskykyprofiiloinnin.
Tyypillisiä käyttötapauksia ovat laitteistotapahtumien, kuten välimuistin ohilyöntien tai haaraennustevirheiden, seuranta sekä tietyn tyyppisten käskyjen laskeminen.

## Saatavuus { #available }

`perf` on saatavilla kaikilla CSC:n supertietokoneilla.

## Lisenssi { #license }

Käyttö on mahdollista sekä akateemisiin että kaupallisiin tarkoituksiin.

## Käyttö { #usage }

Profiilointi työkalulla `perf` tehdään käynnistämällä ja ajamalla sovelluksesi `perf`:n kautta haluamillasi valinnoilla.
Yleisimmät käyttötapaukset hyödyntävät komentoja `perf stat` suorituslaskureiden tilastojen keräämiseen
sekä `perf record`, joka tallentaa ohjelmastasi yksityiskohtaisen suorituskykyprofiilin, jota voidaan myöhemmin tarkastella komennolla `perf report`.
Kaikki käytettävissä olevat `perf`-komennot saa listattua komennolla `perf help`.

Esimerkiksi komento `perf stat -d ./my_application` kerää ja tulostaa ohjelman `my_application` yleisiä suoritinstatistiikoita.
Oletusarvoisesti `perf stat` seuraa muun muassa käskyjen ja kellosyklien määriä, ja valitsimella `-d` saadaan lisäksi
laskurit välimuistin latauksille ja ohilyönneille.

**Huomioithan, että suorituskykymittaukset työkalulla `perf` tulee tehdä laskentasolmuilla**, käyttäen Slurm-työjonojärjestelmää.
Kirjautumissolmuilla kerätty `perf`-data ei yleensä ole **luotettavaa**. Alla esimerkki yhdestä komennosta, jolla yllä oleva `perf stat` -komento
ajetaan Mahti-laskentasolmulla:
```bash
srun --account=<project_name> --partition=small --nodes=1 --ntasks-per-node=1 --cpus-per-task=1 --time=0:10:00 perf stat -d ./my_application
```
Vastaavasti seuraava käyttää `perf record` -komentoa tallentaakseen suorituskykyprofiilin tiedostoon nimeltä `perf.data`:
```bash
srun --account=<project_name> --partition=small --nodes=1 --ntasks-per-node=1 --cpus-per-task=1 --time=0:10:00 perf record -o perf.data ./my_application
```
Tuloksia voi tarkastella komennolla `perf report -i perf.data`. Parhaita tuloksia varten varmista, että ohjelmasi on käännetty valitsimella `-g`.

### Tiettyjen tapahtumien seuranta { #monitoring-specific-events }

Lisälaitteisto- tai ohjelmistotapahtumien laskenta voidaan ottaa käyttöön `-e`-valitsimella komennoissa `perf stat` tai `perf record`.
Käytettävissä olevat tapahtumat saa listattua komennolla `perf list`. Huomaa, että tapahtumakoodit vaihtelevat yleensä järjestelmittäin.
Esimerkiksi Mahtissa ja LUMIssa liukulukulaskutoimitusten määrän (FLOPs) laskemiseen käytettävä tapahtumakoodi on `fp_ret_sse_avx_ops.all`,
ja sitä voi käyttää esimerkiksi näin:
```bash
srun --account=<project_name> --partition=small --nodes=1 --ntasks-per-node=1 --cpus-per-task=1 --time=0:10:00 perf stat -e fp_ret_sse_avx_ops.all ./my_application
```
Puhtissa vastaavat tapahtumakoodit ovat `fp_arith_inst_retired.scalar_double` kaksoistarkkuuden FLOP-laskuille ja `fp_arith_inst_retired.scalar_single` yksittäistarkkuuden FLOP-laskuille.

### Rajoitukset CSC:n supertietokoneilla { #restrictions-on-csc-supercomputers }

Huomaa, että osia `perf`:n toiminnallisuudesta on poistettu käytöstä CSC:n supertietokoneilla turvallisuussyistä.
Tarkemmin, `perf_event_paranoid`-asetus on arvossa 2, mikä estää järjestelmänlaajuisen ja ytimen tason profiloinnin muilta kuin ylläpitäjiltä.
Käytännössä tämä tarkoittaa, että ei ole mahdollista käyttää `perf`-valitsimia kuten `-a` (kaikkien suorittimien valvonta) eikä seurata ytimen tracepointteja.

Lisätietoa `perf`:n tietoturvatasoista löytyy [Linux-ytimen dokumentaatiosta](https://www.kernel.org/doc/html/latest/admin-guide/perf-security.html).

## Lisätietoja { #further-information }

- [`perf` wiki](https://perfwiki.github.io/main/)
- [`perf`-esimerkkejä (Brendan Gregg)](https://www.brendangregg.com/perf.html)