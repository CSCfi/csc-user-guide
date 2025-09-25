---
tags:
  - Free
catalog:
  name: Mothur
  description: Package for microbial community analysis of amplicon sequencing data
  description_fi: Paketti amplikonsekvensointiaineiston mikrobiyhteisöanalyysiin
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Puhti
---

# Mothur { #mothur }

Mothur on bioinformatiikan työkalupakki mikrobiekologiaan liittyvän aineistoanalyysin tarpeisiin.

[TOC]

## License { #license }

Vapaasti käytettävissä ja avoimen lähdekoodin ohjelmisto, lisensoitu [GNU GPLv3](https://www.gnu.org/licenses/gpl-3.0.html) -lisenssillä.

## Available { #available }

- Puhti: 1.39.5, 1.44.0, 1.48.0, 1.48.2
- [Chipster](https://chipster.csc.fi) graafinen käyttöliittymä

## Usage { #usage }

Lataa Mothurin oletusversio Puhtissa komennolla:

```bash
module load mothur
```

Näytä kaikki saatavilla olevat versiot:

```bash
module spider mothur
```

Lataa tietty versio:

```bash
module load mothur/1.48.0
```

Aja Mothur interaktiivisessa tilassa käyttämällä [sinteractive](../computing/running/interactive-usage.md)-komentoa.

```bash
sinteractive --account=project_1234567 -m 8000
module load mothur
mothur
```

Jos analyysit kestävät kauan tai haluat käyttää useita ytimiä, Mothur kannattaa ajaa eräajona.

Aloita kokoamalla Mothur-komennot komentotiedostoon, jotta voit käyttää Mothuria [erätilassa](http://www.mothur.org/wiki/Batch_mode).

Kun sinulla on toimiva Mothur-komentotiedosto, voit tarvittaessa käynnistää Mothur-ajoja, jotka kestävät useita päiviä.

Alla on esimerkki Mothur-eräajotiedostosta. Tässä esimerkissä oletamme, että Mothur-komennot ovat tiedostossa `my_mothur_task.txt`.

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

Jos haluat käyttää useita ytimiä, säädä parametriä `--cpus_per_task`. Sinun on myös säädettävä Mothur-komentotiedoston kunkin komennon `processors`-parametria vastaavasti. Huomaa, että vain osa [Mothur-komennoista](https://mothur.org/wiki/tags/#commands) osaa käyttää useita ytimiä. Tarkista dokumentaatiosta, sisältyykö komennon valintoihin `processors`.

Mothur-ajojen on ajettava yhdellä solmulla, joten Puhtissa käytettävissä olevien ytimien enimmäismäärä on 40. Skaalautuvuus on syytä tarkistaa ennen suurten ajojen lähettämistä. Monet Mothur-tehtävät eivät skaalaudu hyvin muutamaa ydintä pidemmälle. Liian monen ytimen käyttö voi jopa hidastaa ajoa.

Yllä kuvattu eräajon skripti (tässä nimellä `mothur_batch_job.sh`) voidaan lähettää eräajojärjestelmään komennolla:

```bash
sbatch mothur_batch_job.sh
```

Katso lisätietoja eräajojen ajamisesta [Puhti-käyttöoppaasta](../computing/running/getting-started.md).

## Support { #support }

[CSC Service Desk](../support/contact.md)

## More information { #more-information }

- [Mothurin kotisivu](https://www.mothur.org/)