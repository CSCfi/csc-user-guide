# Sähköpostin lähettäminen työn alkaessa/loppuessa ei toimi {#sending-email-when-a-job-starts/finishes-is-not-working}

* Tarkista, että vaihtoehto on oikein asetettu eräajossasi. Esimerkiksi, jos haluat saada sähköpostia, kun työ alkaa, sen tulisi olla `#SBATCH --mail-type=BEGIN`.
* Useat argumentit erotetaan pilkulla, esim. `#SBATCH --mail-type=BEGIN,END`.
* Sähköposti lähetetään oletusarvoisesti CSC-tiliisi liitettyyn sähköpostiosoitteeseen.
* Jos käytät asetusta `#SBATCH --mail-user=<your email address>` ohittaaksesi oletussähköpostiosoitteen, varmista, että asetettu sähköpostiosoite on kelvollinen.