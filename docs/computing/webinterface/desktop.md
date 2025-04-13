# Työpöytä {#desktop}

Työpöytä mahdollistaa graafisten sovellusten käytön Puhti- tai Mahti-laskentasolmussa.

Puhtin verkkokäyttöliittymässä seuraavat sovellukset ovat saatavilla työpöydällä:

* [CloudCompare](../../apps/cloudcompare.md)
* [COMSOL](../../apps/comsol.md)
* [GRASS GIS](../../apps/grass.md)
* [Grace](../../apps/grace.md)
* [MATLAB](../../apps/matlab.md)
* [Maestro](../../apps/maestro.md)
* [QGIS](../../apps/qgis.md)
* [SAGA GIS](../../apps/saga-gis.md)
* [SNAP](../../apps/snap.md)
* [VMD](../../apps/vmd.md)

Mahtissa ovat saatavilla seuraavat sovellukset:

* [Maestro](../../apps/maestro.md)
* [VMD](../../apps/vmd.md)

Vain CPU-renderointi on tuettuna työpöydältä käynnistetyissä graafisissa sovelluksissa. Katso [täältä, miten GPU-kiihdytetty visualisointi otetaan käyttöön](accelerated-visualization.md) valituissa Puhti-sovelluksissa.

## Käynnistäminen {#launching}

1. Avaa `Työpöytä`-sivu Sovellukset-alavalikosta
2. Määritä tarvittavat resurssit. Työpöytä ajetaan [eräajona](../running/getting-started.md) kuten kaikki muutkin suurkoneilla, joten vaaditut resurssit tulee määritellä ennen työpöydän käynnistämistä. Suositeltava osio on [interaktiivinen](../running/interactive-usage.md), jotta työ voisi alkaa mahdollisimman pian, mutta jos tarvitaan enemmän resursseja, myös muita osioita on saatavilla.

## Yhdistäminen {#connecting}

Etätyöpöytään yhdistämiseen on kaksi vaihtoehtoa:

1. **Verkkoselaimella**. noVNC-yhteyspaneelia voidaan käyttää etätyöpöytään yhdistämiseen verkkoselaimella valitsemalla haluttu pakkaus ja laatu ja sitten klikkaamalla `Käynnistä työpöytä`. Selaimen käyttö yhdistämiseen on suositeltavaa useimmille käyttäjille.
![](../../img/ood-vnc-connect.png)
2. **VNC-asiakasohjelmalla**. Parempaa suorituskykyä varten voit käyttää natiivia VNC-asiakasohjelmaa, kuten RealVNC:ta tai TigerVNC:ta. Natiivi VNC-asiakasohjelma voi olla hyvä vaihtoehto, jos selainten leikepöytäintegraation kanssa esiintyy ongelmia etätyöpöydän ja paikallisen isännän välillä. Ohjeet natiiville VNC-asiakasohjelmille löytyvät Native instructions -välilehdeltä. Tämä vaatii VNC-asiakasohjelman asentamisen paikalliselle koneellesi.

## Työpöydän käyttäminen {#using-the-desktop}

Saatavilla olevat sovellukset löytyvät sovellusvalikosta, joka löytyy vasemmasta ylänurkasta, tai
hiiren oikealla näppäimellä työpöydän klikkaamalla. Sovellusten pikakuvakkeita suoraan työpöydälle voi myös luoda
tai palauttaa oletusasetuksiin valitsemalla *Resetoi työpöydän kuvakkeet* -vaihtoehdon Mahti-työpöytäsovelluksen avaamislomakkeessa. Lisätäksesi lisää työpöydän pikakuvakkeita, voit vetää halutut sovellukset sovellusvalikosta työpöydälle.

Muun ohjelmiston käynnistämiseksi, joka on saatavilla suurkoneilla:

1. Avaa terminaali
2. Käynnistä ohjelmisto kuten [Sovellukset-osiossa](../../apps/index.md) on kuvattu, yleensä komennolla `module load XX` ja `<start_command_for_XX>`.

(Työpöydän sovellusvalikko ei sisällä kaikkia Puhtin tai Mahtin tieteellisiä sovelluksia.)