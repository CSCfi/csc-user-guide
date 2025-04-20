# Auto-apptainer {#auto-apptainer}

Auto-apptainer on apuväline, jota voidaan käyttää ohjelmistojen lisäämiseen SD Desktop -virtuaalikoneeseen. Se hyödyntää CSC:n valmiiksi lataamaa Apptainer-pohjaisten ohjelmistokonttien kirjastoa. Voit ehdottaa uuden kontin lisäämistä kirjastoon.

Auto-apptainer ei ole käytettävissä oletuksena, vaan se on ensin asennettava [SD-ohjelmistoasentajalla](../../sensitive-data/sd-desktop-software.md#customisation-via-sd-software-installer).

Tämän jälkeen työkalun voi käynnistää komennolla:

```text
auto-apptainer
```

Oletuksena tämä listaa kaikki auto-apptainerille saatavilla olevat Apptainer-paketit. Listalta voit valita asennettavan paketin.

Vaihtoehtoisesti voit lisätä komennolle suodatusehdon. Tällöin listataan vain ne kontit, joiden nimi tai jokin kontin tarjoamista komennoista vastaa hakuehtoa.

Esimerkiksi komento:

```test
auto-apptainer bam
```

pyytää käyttäjää valitsemaan kahdesta kontista: _bamtools_ ja _bedtools_. Bedtools sisältyy valintaan, koska se tarjoaa komennot `bamToBed` ja `bamToFasta`, jotka täsmäävät tässä tapauksessa hakuehtoon.

Kun kontti valitaan, luodaan yksi tai useampi Apptainer-wrapper-komento hakemistoon: `/shared-directory/sd-tools/bin`. Näitä komentoja voidaan pääosin käyttää kuten natiivisti asennettuja komentoja. Esimerkiksi Bamtools-kontin asentamisen jälkeen Bamtoolsin voi käynnistää komennolla:

```text
bamtools
```

Alta löydät listan ohjelmistoista, jotka voidaan asentaa auto-apptainerilla. Lista voi olla vanhentunut. Ajantasaisen listan saat suorittamalla komennon `auto-apptainer` SD Desktopilla.

*  bamtools_2.5.2--hd03093a_1
*  bcftools_1.20
*  bedtools_2.31.0
*  bwa_0.7.17
*  deepvariant_1.5.0
*  finnish-nertag
*  hisat2_2.2.1--h87f3376_5
*  python3-for-medimaging
*  regenie_3.0.1
*  samtools_1.17-2023-06
*  seqtk_v1.3-1-deb_cv1
*  stringtie_2.2.0--ha025227_1
*  taguette
*  vcftools_v0.1.16-1
*  vsearch_2.23.0--h6a68c12_0
*  weeder_2.0--h9f5acd7_7