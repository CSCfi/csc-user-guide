# Laskutus { #billing }

## Mahti-laskennan laskutus { #mahti-compute-billing }

Mahtin CPU-osioissa ajot kuluttavat CPU BU -yksiköitä joko varattujen solmujen määrän (solmupohjainen allokaatio) tai varattujen ytimien määrän (ydinpohjainen allokaatio) perusteella. Muistista ei veloiteta erikseen, mutta paikallisen levytilan käytöstä veloitetaan erikseen. Tarkemmin:

* Solmupohjaisissa osioissa jokainen varattu CPU-solmu kuluttaa **100** CPU BU -yksikköä tunnissa.
* Ydinpohjaisissa osioissa jokainen ydin kuluttaa **1** CPU BU -yksikön tunnissa, ja jokainen varattu NVMe-levyn GiB kuluttaa **0.01** CPU BU -yksikköä tunnissa.

Mahtin GPU-osioissa ajot kuluttavat GPU BU -yksiköitä varattujen GPU:iden lukumäärän perusteella. Muistista ei veloiteta erikseen, mutta paikallisen levytilan käytöstä veloitetaan erikseen. Tarkemmin:

* Jokainen varattu A100-GPU kuluttaa **100** GPU BU -yksikköä tunnissa, eli yhteensä **400** GPU BU -yksikköä tunnissa täydellä GPU-solmulla.
* A100-GPU:n seitsemäsosa (a100_1g.5gb) kuluttaa **15** GPU BU -yksikköä tunnissa.
* Jokainen varattu NVMe-levyn GiB kuluttaa **0.01** GPU BU -yksikköä tunnissa.

## Puhti-laskennan laskutus { #puhti-compute-billing }

Puhti on heterogeeninen järjestelmä, jossa on CPU-, GPU- ja IO-solmuja sekä solmuja vaihtelevilla muistimäärillä. Lisäksi on mahdollista käyttää vain osaa solmusta ja sen erilaisista resursseista. Laskutusmalli veloittaa laskutusyksiköitä (BU) oikeudenmukaisesti varattujen solmuresurssien määrän perusteella. 

Puhtin [CPU-osioissa](running/batch-job-partitions.md#puhti-cpu-partitions) ajot kuluttavat CPU BU -yksiköitä. Laskentatyön CPU BU -kulutusnopeus riippuu lineaarisesti pyydettyjen ytimien lukumäärästä, pyydetyn paikallisen tallennustilan määrästä sekä pyydetyn muistin määrästä. Tarkemmin:

* Jokainen varattu ydin kuluttaa **1** CPU BU -yksikön tunnissa.
* Jokainen varattu GiB muistia kuluttaa **0.1** CPU BU -yksikköä tunnissa.
* Jokainen varattu NVMe-levyn GiB (jos saatavilla) kuluttaa **0.006** CPU BU -yksikköä tunnissa.

```
Total CPU BU = ( NCores * 1 + MemGiBs * 0.1 + NVMeGiBs * 0.006 ) * Walltime hours
```

Puhtin [GPU-osioissa](running/batch-job-partitions.md#puhti-gpu-partitions) ajot kuluttavat GPU BU -yksiköitä. Laskentatyön GPU BU -kulutusnopeus riippuu lineaarisesti pyydettyjen GPU:iden ja ytimien lukumäärästä, pyydetyn paikallisen tallennustilan määrästä sekä pyydetyn muistin määrästä. Tarkemmin:

* Jokainen varattu GPU kuluttaa **60** GPU BU -yksikköä tunnissa.
* Jokainen varattu ydin kuluttaa **1** GPU BU -yksikön tunnissa.
* Jokainen varattu GiB muistia kuluttaa **0.1** GPU BU -yksikköä tunnissa.
* Jokainen varattu NVMe-levyn GiB (jos saatavilla) kuluttaa **0.006** GPU BU -yksikköä tunnissa.

```
Total GPU BU = ( NCores * 1 + MemGiBs * 0.1 + NVMeGiBs * 0.006 + NGPUs * 60 ) * Walltime hours
```

## Scratch-levytilan laskutus { #scratch-disk-billing }

Puhtissa ja Mahtissa scratch-tallennuksen laskutus on sama. Käyttö 1 TiB:iin asti on maksutonta. 

* Ylimenevä käyttö yli 1 TiB:n laskutetaan: 1 TiB kuluttaa **5** Storage BU -yksikköä tunnissa.

## ProjAppl-levytilan laskutus { #projappl-disk-billing }

Puhtissa ja Mahtissa ProjAppl-tallennuksen laskutus on sama. Käyttö 50 GiB:iin asti on maksutonta. 

* Ylimenevä käyttö yli 50 GiB:n laskutetaan: 1 TiB kuluttaa **5** Storage BU -yksikköä tunnissa.