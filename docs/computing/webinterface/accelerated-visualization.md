# Kiihdytetty visualisointi { #accelerated-visualization }
Kiihdytetty visualisointi -sovellus mahdollistaa visualisointisovellusten käytön GPU-kiihdytyksellä Puhti-laskentasolmulla.

## Saatavilla olevat sovellukset { #available-applications }
* [Abaqus CAE](../../apps/abaqus.md)
* [Ansys Workbench](../../apps/ansys.md)
* [Blender](../../apps/blender.md)
* [CloudCompare](../../apps/cloudcompare.md)
* [COMSOL](../../apps/comsol.md)
* [ParaView](../../apps/paraview.md)
* [VisIt](../../apps/visit.md)
* [VMD](../../apps/vmd.md)

## Käynnistäminen { #launching }
1. Avaa `Accelerated visualization` -sivu kohdasta Apps.
2. Määritä tarvittavat resurssit. Yksi GPU varataan.
3. Käynnistä sovellus.
4. Yhdistä työpöytään.
4. Käynnistä visualisointisovellus sovellusvalikosta, joka löytyy joko vasemmasta yläkulmasta tai napsauttamalla työpöytää hiiren oikealla painikkeella.

!!! Note

    Huomioita GPU-osioista:
    
    * `gputest`-osion aikaraja on 15 minuuttia, mutta sen pitäisi yleensä olla heti tai hyvin pian käytettävissä.
    * `gpu` mahdollistaa pidemmän sovelluksen käytön, mutta jonotusaika voi olla myös pidempi.
    * Laskutusyksiköissä GPU-laskenta-aika on noin 60 kertaa kalliimpaa kuin CPU-aika (ks. [Billing](../hpc-billing.md)). Pidä siis kiihdytetty visualisointi -sovellus auki vain, kun käytät sitä aktiivisesti. Lopeta työ käyttämällä `Delete`-painiketta `My interactive Sessions` -sivulla.

## Yhdistäminen { #connecting }
On kaksi tapaa muodostaa yhteys Accelerated Visualization -sovellukseen:

1. Verkkoselaimella.
noVNC Connection -välilehteä voidaan käyttää sovellukseen yhdistämiseen verkkoselaimella valitsemalla haluttu pakkaus ja laatu ja napsauttamalla sitten `Launch Desktop`.
Selainyhteyttä suositellaan useimmille käyttäjille.
![](../../img/ood-vnc-connect.png)
2. VNC-asiakasohjelmalla.
Parempaa suorituskykyä varten voit käyttää natiivia VNC-asiakasohjelmaa, kuten RealVNC:tä tai TigerVNC:tä.
Ohjeet natiiveille VNC-asiakasohjelmille löytyvät välilehdeltä Native instructions.
Tämä edellyttää VNC-asiakasohjelman asentamista paikalliselle koneellesi.

## Sovelluksen käyttö { #using-the-app }
Accelerated Visualization -sovellusta käytetään samalla tavalla kuin [Työpöytäsovellusta](desktop.md). Kuitenkin kiihdytettyjen sovellusten pikakuvakkeita ei luoda työpöydälle automaattisesti. Voit luoda pikakuvakkeet vetämällä halutun sovelluksen sovellusvalikosta työpöydälle.

Huomaa, että jos ajat sovelluksia, jotka eivät hyödy GPU-kiihdytyksestä, sinun kannattaa käyttää sen sijaan [Työpöytäsovellusta](desktop.md). Vain sovellukset, joiden nimessä on loppuliite `(Accelerated)`, hyötyvät GPU:sta.

Lisätietoja omien sovellusten ajamisesta Accelerated Visualization -sovelluksessa löydät sivulta [creating containers page](../containers/examples.md#example-accelerated-visualization-application).