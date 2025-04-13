
# Kiihtyvytetty visualisointi
Kiihtyvytetty visualisointi -sovellus mahdollistaa visualisointisovellusten käytön GPU-kiihdytyksellä Puhti-laskentayksikössä.

## Saatavilla olevat sovellukset {#available-applications}
* [Abaqus CAE](../../apps/abaqus.md)
* [Ansys Workbench](../../apps/ansys.md)
* [Blender](../../apps/blender.md)
* [CloudCompare](../../apps/cloudcompare.md)
* [COMSOL](../../apps/comsol.md)
* [ParaView](../../apps/paraview.md)
* [VisIt](../../apps/visit.md)
* [VMD](../../apps/vmd.md)

## Käynnistäminen {#launching}
1. Avaa `Kiihtyvytetty visualisointi` -sivu sovelluksissa.
2. Määritä tarvittavat resurssit. Yksi GPU varataan.
3. Käynnistä sovellus.
4. Yhdistä työpöydälle.
5. Käynnistä visualisointisovellus sovellusvalikosta, joka löytyy joko vasemmasta yläkulmasta tai napsauttamalla hiiren kakkospainikkeella työpöytää.

!!! Huomio

    Huomioita GPU-osuuksista:

    * `gputest`:illä on 15 minuutin aikaraja, mutta sen pitäisi yleensä olla saatavilla heti tai hyvin pian.
    * `gpu` mahdollistaa sovelluksen pidemmän käytön, mutta jonotusaika voi olla pidempi.
    * GPU-laskenta-aika on ~60x kalliimpaa laskutusyksiköissä, joten pidä kiihtyvytetty visualisointi -sovellus auki vain, kun todella käytät sitä. Käytä `Poista`-painiketta `Omat interaktiiviset istunnot` -sivulla lopettaaksesi työskentelyn.

## Yhdistäminen {#connecting}
Kiihtyvytetty visualisointi -sovellukseen voi yhdistää kahdella tavalla:

1. **Verkkoselaimella**.
noVNC-yhteys-välilehteä voidaan käyttää sovellukseen yhdistämiseen verkkoselaimella valitsemalla haluttu pakkaus ja laatu ja sitten napsauttamalla `Käynnistä työpöytä`.
Suosittelemme selaimen käyttöä useimmille käyttäjille.
![](../../img/ood-vnc-connect.png)
2. **VNC-asiakasohjelmalla**.
Parempaa suorituskykyä varten voit käyttää natiivin VNC-asiakasohjelmaa, kuten RealVNC tai TigerVNC.
Ohjeet natiivien VNC-asiakasohjelmien käyttöön löytyvät Käyttöohjeet-välilehdeltä.
Tämä edellyttää VNC-asiakasohjelman asentamista paikalliselle koneellesi.

## Sovelluksen käyttäminen {#using-the-app}

Kiihtyvytettyä visualisointi -sovellusta käytetään samalla tavalla kuin [Työpöytä-sovellusta](desktop.md). Kuitenkaan kiihtyvätettyjen sovellusten pikavalintoja ei automaattisesti luoda työpöydälle. Luodaksesi pikavalintoja voit vetää halutun sovelluksen sovellusvalikosta työpöydälle.

Huomaa, että jos käytät sovelluksia, jotka eivät hyödy GPU-kiihdytyksestä, sinun pitäisi käyttää [Työpöytä-sovellusta](desktop.md). Vain sovellukset, joiden päädyssä on `(Kiihtyvytetty)`, hyötyvät GPU:sta.

Lisätietoja omien sovellustesi ajamisesta Kiihtyvyttä visualisointi -sovelluksessa löydät [konttien luomisen sivulta](../containers/creating.md#using-gpu-from-containers-in-interactive-sessions-in-puhti).
