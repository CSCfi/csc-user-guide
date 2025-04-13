# GPU-pohjainen muotoseulonta molekyyleille

Tässä opetusohjelmassa näytetään, kuinka käyttää [Schrödinger Maestro Shape](https://www.schrodinger.com/Shape-Screening/) -ohjelmaa
16 miljoonan rakenteen (160 miljoonan konformaation) seulontaan 
[Molport molecular database](https://molport.com/shop/screeening-compound-database) -tietokannassa GPU:lla Puhti-palvelimella.

Molport-tietokannan _valmistelu_ GPU-seulontaa varten kestää kaksi viikkoa, mutta koska valmisteltu _muototiedosto_ on jo saatavilla Puhtissa, varsinaiseen molekyylin seulontaan GPU:lla kuluu vain 5-20 minuuttia.


## OHJEET {#how-to}

* Asenna Maestro paikalliselle tietokoneellesi. Yksityiskohtaiset ohjeet löytyvät [Maestro-sivultamme](../../apps/maestro.md).
* Piirrä / tuo molekyyli, jolle haluat löytää samankaltaisia molekyylejä
* Aja [Maestro LigPrep](https://www.schrodinger.com/LigPrep/) -työkalu sille
* Vie valmisteltu molekyyli Maestro-alkuperäisessä formaatissa (mae), esim. nimellä `target.mae`
* Kopioi tiedosto Puhtiin omaan scratch-kansioosi ([Vinkkejä tiedostojen kopiointiin](../../data/moving/index.md))
* Kopioi (ja muokkaa tarvittaessa) seuraava _skripti_ nimellä `gpushape.bash` samaan kansioon (älä kopioi 139GB muototiedostoa)
  * Tämä skripti pyytää 60 minuuttia aikaa yhdelle GPU:lle, käyttää _muototiedostoa_ sijainnista `/appl/data/bio/molport-shape/MP_SHAPE.bin`, käyttää `target.mae` hakumolekyylinä ja sijoittaa tulokset `shape_test-out.maegz`-tiedostoon
```
$SCHRODINGER/shape_screen_gpu run -shape_data_treatment remote \
      -shape target.mae -HOST quick-gpu -JOBNAME shape_test \
      -screen /appl/data/bio/molport-shape/MP_SHAPE.bin
```
* Alusta oletus Maestro-asennus komennolla
```
module load maestro
```
* ...ja lähetä tehtävä ajettavaksi (huom, ei `sbatch`-komentoa!)
```
bash gpushape.bash
```
* Kopioi tulokset paikalliselle tietokoneellesi analysointia varten