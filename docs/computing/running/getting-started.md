# Aloittaminen

CSC käyttää eräajojärjestelmää aikatauluttamaan ja suorittamaan laskentatehtäviä supertietokoneillamme.

Tyypillisesti eräajo aloittaa lataamalla ohjelmistoympäristön käyttäen [moduulijärjestelmää](../modules.md) ja suorittaa sitten ohjelman laskentatehtävän tekemiseksi. On tärkeää, että eräajossa määritellään myös ne resurssit (suoritusaika, muisti, ytimet jne.), joita tehtävän suorittamiseen tarvitaan.

Tässä osiossa käydään läpi perusasiat eräajojen luomisesta ja lähettämisestä käyttäen SLURM-eräajojärjestelmää CSC:ssä.

Huomaa, että myös [interaktiiviset tehtävät](interactive-usage.md) (muut kuin kääntäminen, tietojen siirto sekä kevyet esikäsittely- ja jälkikäsittelytehtävät) tulee suorittaa eräajojärjestelmän kautta. Katso tarkemmat tiedot [Käyttöpolitiikasta](../usage-policy.md).

!!! warning "Tärkeät käsitteet CSC:n eräajojärjestelmästä"
    1. **Työt eivät käynnisty välittömästi, vaan ne menevät jonoon.**
        - Työt suoritetaan, kun resursseja on vapaana. Käynnistysaika riippuu
          myös työn prioriteettipisteestäsi.
        - Työn prioriteettipisteet on olemassa varmistamaan
          oikeudenmukainen laskentatehojen jakaminen klusterin käyttäjien
          välillä. Paljon töiden suorittaminen alentaa työnne
          lähtöprioriteettipistettä. Prioriteettipisteet nousevat asteittain,
          kun työnne odottaa jonossa.
    1. **Työn tarkkaa käynnistysaikaa ei voida ennustaa.**
        - Se riippuu suurelta osin muiden käyttäjien töiden todellisista
          suoritusaikoista ja siitä, lähetetäänkö uusia töitä. Katso
          [FAQ](../../support/faq/when-will-my-job-run.md).
    1. **Laskentaresurssit (esim. suoritusaika, muisti, ytimien lukumäärä)
       pyydetään erikseen.**
        - Jos varattu aika tai muistirajat ylitetään, työ keskeytetään
          automaattisesti!

Aloittaaksesi sovelluksesi suorittamisen CSC:n supertietokoneilla:

1. [Eräajon käsikirjoituksen luominen Puhti:lle](creating-job-scripts-puhti.md)
2. [Eräajon käsikirjoituksen luominen Mahti:lle](creating-job-scripts-mahti.md)
3. [Eräajon lähettäminen](submitting-jobs.md)
4. [Saatavilla olevat eräajon osastot](batch-job-partitions.md)
5. [Suorituskyvyn tarkastuslista](performance-checklist.md)

Jos olet jo perehtynyt SLURM:iin, tarkista meidän
[esimerkkieräajon käsikirjoitukset Puhti:lle](example-job-scripts-puhti.md) tai
[esimerkkieräajon käsikirjoitukset Mahti:lle](example-job-scripts-mahti.md).

!!! info "LUMI:n aloittaminen"
    Katso [LUMI:n dokumentaatio](https://docs.lumi-supercomputer.eu/runjobs/scheduled-jobs/slurm-quickstart/) saadaksesi ohjeet töiden suorittamisesta LUMI-superkoneella. LUMI käyttää myös SLURM-eräajojärjestelmää, joten erot CSC:n superkoneiden ja LUMI:n välillä ovat vähäiset.