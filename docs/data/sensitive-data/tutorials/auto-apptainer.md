
# Auto-apptainer {#auto-apptainer}

Auto-apptainer on apuväline, jota voidaan käyttää ohjelmistojen lisäämiseen SD Desktop -virtuaalikoneeseen. Se hyödyntää Apptainer-pohjaisia ohjelmistokontteja sisältävää kirjastoa, jonka CSC on esiladannut. Voit ehdottaa konttia lisättäväksi kirjastoon.

Auto-apptainer ei ole käytettävissä oletuksena, vaan sinun täytyy ensin asentaa se käyttämällä [SD-ohjelmiston asentajaa](../../sensitive-data/sd-desktop-software.md#customisation-via-sd-software-installer)

Tämän jälkeen voit käynnistää työkalun komennolla:

```text
auto-apptainer
```

Oletuksena tämä listaa kaikki auto-apptainerille saatavilla olevat Apptainer-paketit. Listalta voit valita asennettavan paketin.

Vaihtoehtoisesti voit lisätä suodatuskriteerin komentoon. Tässä tapauksessa listataan vain ne kontit, joiden nimi tai jokin konttien tarjoamista komennoista täsmää hakukriteerien kanssa.

Esimerkiksi komento:

```test
auto-apptainer bam
```

pyytää käyttäjää valitsemaan kahdesta kontista: _bamtools_ ja _bedtools_. Bedtools sisältyy, koska se tarjoaa komennot `bamToBed` ja `bamToFasta`, jotka täsmäävät hakukriteereihin tässä tapauksessa.

Kun kontti on valittu, yksi tai useampi Apptainer-käärinpohjainen komento luodaan hakemistoon: `/shared-directory/sd-tools/bin`.
Näitä komentoja voidaan yleensä käyttää kuin natiiveja asennettuja komentoja. Esimerkiksi Bamtools-kontin asentamisen jälkeen,
Bamtools voidaan käynnistää komennolla:

```text
bamtools
```

Alta löydät listan ohjelmistoista, jotka voidaan asentaa auto-apptainerilla. Lista voi olla vanhentunut. Voit saada ajan tasalla olevan listan suorittamalla komennon `auto-apptainer` SD Desktopissa.

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
