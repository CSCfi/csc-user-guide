# Miksi eräajoni epäonnistuu? {#why-does-my-batch-job-fail}

Alla on yleisiä virheilmoituksia, joita saatat kohdata eräajon epäonnistuessa, sekä neuvoja niiden korjaamiseksi.

## Virheellinen tili tai tili/osa-yhdistelmä määritelty {#invalid-account-or-account-partition-combination-specified}

Täydellinen virheilmoitus on seuraava:

```text
sbatch: error: Batch job submission failed: Invalid account or account/partition combination specified
```

Tämä virheilmoitus viittaa Slurm-valintoihin `--account=<project>` ja `--partition`. Yleisimmät syyt ovat:

* Projektia ei ole olemassa.
* Projekti on olemassa, mutta et ole sen jäsen. Katso, kuinka
  [lisätä jäsen projektiin](../../accounts/how-to-add-members-to-project.md)
* Olet projektin jäsen, mutta projektia ei ole otettu käyttöön Puhti-alustalla. Katso kuinka
  [lisätä palvelun käyttöoikeus projektille](../../accounts/how-to-add-service-access-for-project.md).
* Osa ei ole olemassa.
* Osa on olemassa, mutta projektisi ei ole sallittu siinä.

## Työ rikkoo laskutuksen/QOS-käytäntöä {#job-violates-accounting-qos-policy}

Täydellinen virheilmoitus on seuraava:

```text
sbatch: error: AssocMaxSubmitJobLimit
sbatch: error: Batch job submission failed: Job violates accounting/QOS policy (job submit limit, user's size and/or time limits)
```

Yleisimmät syyt ovat:

* Työskriptistä puuttuu `--account`-parametri.
* Projektilasi sisältää liikaa töitä järjestelmässä, joko suoritettavana tai jonossa.
  Huomaa, että sisäisesti Slurm laskee jokaisen työn eräajotyössä erilliseksi
  työksi.
* Työ suoritettiin suoraan `./script_name.sh` tai `bash script_name.sh` komennolla,
  kun se tulisi lähettää `sbatch script_name.sh` komennolla.
* Projektisi on käyttänyt loppuun laskutusyksikkönsä. Katso
  [Kuinka hakea lisää laskutusyksiköitä](../../accounts/how-to-apply-for-billing-units.md).

## Pyydetty solmukonfiguraatio ei ole saatavilla {#requested-node-configuration-is-not-available}

Täydellinen virheilmoitus on seuraava:

```text
sbatch: error: Batch job submission failed: Requested node configuration is not available
```

Yleisimmät syyt ovat:

* Pyydetään esimerkiksi GPU:ta tai NVMe:ä osassa, jossa niitä ei ole.
* Pyydetään esimerkiksi enemmän muistia tai aikaa kuin valittu osuus voi tarjota. Erityisesti
  käytettäessä `--mem-per-cpu`-lippua muistin määrittämiseksi, huomaa, että tämä kerrotaan
  pyydettyjen suoritun määrä (1 tehtävää kohden) ja tuloksen on oltava valitun osuus
  rajojen sisällä.

Katso [eräajojen osat](../../computing/running/batch-job-partitions.md) saadaksesi lisätietoa resurssien saatavuudesta kussakin jonossa.