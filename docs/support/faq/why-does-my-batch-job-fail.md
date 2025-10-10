# Miksi eräajoni epäonnistuu? { #why-does-my-batch-job-fail }

Alla on yleisiä virheilmoituksia, joita voit saada työn epäonnistuessa, sekä ohjeita niiden korjaamiseksi.

## Virheellinen tili tai tili/partitio-yhdistelmä määritetty { #invalid-account-or-account-partition-combination-specified }

Täydellinen virheilmoitus on seuraava:

```text
sbatch: error: Batch job submission failed: Invalid account or account/partition combination specified
```

Tämä virheilmoitus viittaa Slurm-asetuksiin `--account=<project>` ja
`--partition`. Yleisimmät syyt ovat:

* Projektia ei ole olemassa.
* Projekti on olemassa, mutta et ole sen jäsen. Katso, miten
  [lisäät jäsenen projektiin](../../accounts/how-to-add-members-to-project.md)
* Olet projektin jäsen, mutta projektia ei ole otettu käyttöön Puhtissa. Katso,
  miten
  [lisäät projektille palveluoikeuden](../../accounts/how-to-add-service-access-for-project.md).
* Partitiota ei ole olemassa.
* Partitio on olemassa, mutta projektiasi ei ole siinä aktivoitu.

## Työ rikkoo accounting/QOS-käytäntöä { #job-violates-accounting-qos-policy }

Täydellinen virheilmoitus on seuraava:

```text
sbatch: error: AssocMaxSubmitJobLimit
sbatch: error: Batch job submission failed: Job violates accounting/QOS policy (job submit limit, user's size and/or time limits)
```

Yleisimmät syyt ovat:

* Työskriptistä puuttuu `--account`-parametri.
* Projektillasi on liikaa töitä järjestelmässä, joko käynnissä tai jonossa.
  Huomaa, että Slurm laskee array-työssä jokaisen yksittäisen työn erilliseksi
  työksi.
* Työ ajettiin suoraan `./script_name.sh` tai `bash script_name.sh`,
  vaikka se pitäisi lähettää jonoon komennolla `sbatch script_name.sh`.
* Projektisi Billing Unitit ovat loppuneet. Katso
  [kuinka hakea lisää Billing Unitteja](../../accounts/how-to-apply-for-billing-units.md).

## Pyydetty solmukokoonpano ei ole saatavilla { #requested-node-configuration-is-not-available }

Täydellinen virheilmoitus on seuraava:

```text
sbatch: error: Batch job submission failed: Requested node configuration is not available
```

Yleisimmät syyt ovat:

* Pyydät esimerkiksi GPU:ta tai NVMe:tä partiosta, jossa niitä ei ole.
* Pyydät esimerkiksi enemmän muistia tai aikaa kuin valittu partitio tarjoaa. Erityisesti, jos
  käytät `--mem-per-cpu`-lippua muistin määrittämiseen, huomaa, että tämä kerrotaan
  pyydettyjen suoritinytimien määrällä (oletuksena 1 per tehtävä) ja lopputuloksen on oltava
  valitun partition rajoissa.

Katso [eräajon partitioista](../../computing/running/batch-job-partitions.md) lisätietoja
kussakin jonossa saatavilla olevista resursseista.