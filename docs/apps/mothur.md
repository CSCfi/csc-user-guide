
---
tags:
  - Free
---

# Mothur

Mothur on bioinformatiikkatyökalu mikrobiekologiaan liittyvän data-analyysin tarpeisiin.

[TOC]

## Lisenssi {#license}

Vapaa käyttää ja avoimen lähdekoodin GNU GPLv3 -lisenssin alla [GNU GPLv3](https://www.gnu.org/licenses/gpl-3.0.html).

## Saatavilla {#available}

- Puhti: 1.39.5, 1.44.0, 1.48.0, 1.48.2
- [Chipster](https://chipster.csc.fi) graafinen käyttöliittymä

## Käyttö {#usage}

Mothurin oletusversion alustaminen Puhtilla:

```bash
module load mothur
```

Kaikkien saatavilla olevien versioiden näkeminen:

```bash
module spider mothur
```

Tietyn version lataaminen:

```bash
module load mothur/1.48.0
```

Mothurin ajaminen interaktiivisessa tilassa, käytä [sinteractive](../computing/running/interactive-usage.md).

```bash
sinteractive --account=project_1234567 -m 8000
module load mothur
mothur
```

Jos analyysisi vie paljon aikaa tai haluat käyttää useampia ytimiä, sinun tulisi ajaa Mothur erätehtävänä.

Aloita keräämällä Mothur-komennot komennotiedostoon käyttääksesi Mothuria [erätilassa](http://www.mothur.org/wiki/Batch_mode).

Kun sinulla on toimiva Mothur-komennotiedosto, voit tarvittaessa käynnistää Mothur-töitä, joiden suoritus kestää useita päiviä.

Alla on esimerkki Mothur-erätehtävätiedostosta. Tässä esimerkissä oletamme, että Mothur-komennot ovat tiedostossa `my_mothur_task.txt`.

```bash
#!/bin/bash
#SBATCH --account=project_1234567
#SBATCH --job-name=mothur
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=32G
#SBATCH --time=48:00:00
#SBATCH --partition=small

module load mothur
mothur my_mothur_task.txt
```

Jos haluat käyttää useampia ytimiä, säädä parametriä `--cpus_per_task`. Sinun on myös säädettävä `processors`-parametria jokaisessa Mothur-komennotiedoston komennossa vastaavasti. Huomaa, että vain osa [Mothur-komennoista](https://mothur.org/wiki/tags/#commands) voi käyttää useampia ytimiä. Tarkista dokumentaatiosta, sisältääkö komento `processors`-asetuksen.

Mothur-töiden on määrä ajaa yhdellä solmulla, joten Puhtin maksimiydinmäärä on 40. Tarkista skaalautuvuus ennen suurten töiden lähettämistä. Monet Mothur-tehtävät eivät skaalaudu kovin hyvin muutamaa ydintä pidemmälle. Liian monen ytimen käyttäminen voi jopa hidastaa työsi suoritusta.

Yllä kuvattu erätehtäväskenaario (tässä tapauksessa nimettynä `mothur_batch_job.sh`) voidaan lähettää erätehtäväjärjestelmään komennolla:

```bash
sbatch mothur_batch_job.sh
```

Katso lisätietoja erätehtävien ajamisesta [Puhti-käyttäjän oppaasta](../computing/running/getting-started.md).

## Tuki {#support}

[CSC Service Desk](../support/contact.md)

## Lisätietoja {#more-information}

- [Mothur-etusivu](https://www.mothur.org/)

