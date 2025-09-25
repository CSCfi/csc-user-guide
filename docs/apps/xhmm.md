---
tags:
  - Free
catalog:
  name: XHMM (eXome-Hidden Markov Model)
  description: Copy number variation calling from targeted sequencing data
  description_fi: Kopiolukumuutosten tunnistus kohdennetun sekvensoinnin aineistosta
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Puhti
---

# XHMM (eXome-Hidden Markov Model) { #xhmm-exome-hidden-markov-model }



XHMM:n C++-ohjelmistopaketti on kehitetty kopiolukumuutosten (CNV) tunnistamiseen sellaisten seuraavan sukupolven sekvensointiprojektien aineistosta, joissa on käytetty eksomien rikastusta (tai yleisemmin kohdennettua sekvensointia).

XHMM hyödyntää pääkomponenttianalyysiin (PCA) perustuvaa normalointia ja piilotettua Markovin mallia (HMM) havaitakseen ja genotyypittääkseen kopiolukumuutoksia (CNV) kohdennetun sekvensoinnin kokeista saadusta normaloidusta lukusyvyysaineistosta.

XHMM on nimenomaisesti suunniteltu käytettäväksi kohdennetun eksomisekvensoinnin kanssa korkealla peitolla (vähintään 60x - 100x), käyttäen Illumina HiSeqin (tai vastaavan) sekvensointia vähintään ~50 näytteestä. Kuitenkaan mikään XHMM:n osa ei nimenomaisesti vaadi juuri näitä koeolosuhteita; olennaista on genomialueiden korkea peitto monissa näytteissä.

[TOC]

## Lisenssi { #license }

Ohjelmisto on vapaasti käytettävissä ja avointa lähdekoodia, mutta lisenssiä ei ole määritelty.

## Saatavilla { #available }

* Puhti: 0.0.0.2016_01_04.cc14e52 

## Käyttö { #usage }

XHMM:n käyttöä varten lataa moduuli:

```bash
module load xhmm
```

Tämän jälkeen XHMM käynnistyy komennolla:

```bash
xhmm
```

## Lisätietoja { #more-information }

* [XHMM:n kotisivu](https://statgen.bitbucket.io/xhmm/index.html)