# Condan parhaat käytännöt CSC:n supertietokoneilla { #conda-best-practices-for-csc-supercomputers }

!!! warning "Älä asenna Conda-ympäristöjä suoraan CSC:n supertietokoneiden rinnakkaistiedostojärjestelmiin!"
    [CSC on poistanut käytöstä Conda-ympäristöt](../../computing/usage-policy.md#conda-installations),
    jotka on asennettu _suoraan_ CSC:n supertietokoneiden rinnakkaistiedostojärjestelmään
    (esim. `/scratch`, `/projappl`, `$HOME`). Tämä johtuu jaetuilla tiedostojärjestelmillä
    toimivien Conda-pohjaisten ympäristöjen suorituskykyongelmista, jotka aiheuttavat pitkiä
    käynnistysviiveitä ja järjestelmänlaajuisia hidastumisia Python-skriptejä ajettaessa.

Conda-ympäristöt sisältävät tyypillisesti kymmeniä tai jopa satoja tuhansia tiedostoja,
ja Conda-sovelluksen käynnistäminen edellyttää suuren määrän näistä tiedostoista lukemista.
Valitettavasti kaikki rinnakkaistiedostojärjestelmät, jotka on optimoitu suurelle määrälle
asiakkaita, tarjoavat heikon suorituskyvyn yksittäiselle asiakkaalle. Huomaat tämän pidempinä
alkukäynnistysaikoina Conda-sovelluksille sekä lisäkuormana Lustre-metatietopalvelimelle.

**Condaa voidaan silti käyttää epäsuorasti**. Vaihtoehtona suoralle Condan käytölle suosittelemme:

1. **Käytä CSC:n moduulijärjestelmän kautta saatavilla olevia esiasennettuja ympäristöjä**

    Tarkista, sopisiko jokin
    [CSC:n esiasennetuista ympäristöistä](../../apps/python.md#pre-installed-python-environments)
    projektiisi. Jos olemassa olevasta ympäristöstä puuttuu muutama kriittinen paketti, voit usein
    asentaa puuttuvat paketit itse.

    [Pythonin käyttöoppassaamme](python-usage-guide.md#installing-python-packages-to-existing-modules)
    ja [R-sovellussivulla](../../apps/r-env.md#r-package-installations) on lisätietoja siitä,
    kuinka voit asentaa omia pakettejasi moduuliemme päälle. Voit myös
    [ottaa yhteyttä CSC Service Deskiin](../contact.md) puuttuvia paketteja koskevissa pyynnöissä.

2. **Luo kontitettu Conda- tai pip-ympäristö CSC:n Tykky-työkalulla**

    CSC on kehittänyt
    [työkalun Conda- tai pip-asennusten paketoimiseksi](../../computing/containers/tykky.md)
    pienemmäksi tiedostojoukoksi Apptainer- ja SquashFS-teknologioita hyödyntäen. Työkalu on
    saatavilla esiasennettuna moduulina, ja CSC käyttää sitä myös omissa asennuksissaan.

3. **Käytä omia mukautettuja kontteja**

    Tämä on erinomainen vaihtoehto, kun kehität ohjelmistoa paikallisesti työasemalla ja otat sen
    sitten käyttöön toisella työasemalla, klusterissa tai pilvialustoilla. CSC:n supertietokoneet
    tukevat Apptainer-kontteja, jotka ovat Lustren kannalta vain yksittäisiä suuria tiedostoja,
    mikä välttää suuren osan ongelmista. Monet ohjelmistoprojektit tarjoavat Docker-kontteja,
    jotka voidaan usein helposti muuntaa Apptainer-muotoon. Kontin sisällä voit luonnollisesti
    käyttää esimerkiksi Condaa pakettien hallintaan aiheuttamatta tiedostojärjestelmäongelmia.

    Käytä [Tykkya](../../computing/containers/tykky.md) olemassa olevan Docker-kontin muuntamiseen
    Apptaineriksi tai lue dokumentaatiostamme,
    [kuinka luot oman Apptainer-kontin](../../computing/containers/overview.md#building-container-images).