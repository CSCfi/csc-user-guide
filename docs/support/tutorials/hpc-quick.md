# Superlaskennan käytön aloitus CSC:llä { #getting-started-with-supercomputing-at-csc }

Olet luonut [käyttäjätilin](../../accounts/how-to-create-new-user-account.md)
ja ensimmäisen [CSC-projektisi](../../accounts/how-to-create-new-project.md), joten olet valmis skaalaamaan laskentasi! Tällä sivulla annetaan ohjeita CSC:n HPC-resurssien käytön aloittamiseen.

Uusille käyttäjille suositellaan suorittamaan kurssi
*CSC Computing Environment*, joka tarjoaa perusteellisen johdatuksen CSC:n palveluihin. Seuraavan live-opetuskerran löydät
[CSC:n koulutuskalenterista](https://csc.fi/en/trainings/training-calendar/).
Myös
[itsepohjainen versio](https://csc.fi/en/training-calendar/csc-computing-environment-self-learning/)
on saatavilla.
[Kurssimateriaalit](https://csc-training.github.io/csc-env-eff/) ovat käytettävissä ilman ilmoittautumista ja ovat sellaisinaan erittäin hyödyllisiä.

Yleisempänä johdantona HPC:hen suosittelemme
verkko­kurssia [*Elements of Supercomputing*](https://edukamu.fi/elements-of-supercomputing/).

!!! note "Tarvitsetko tukea?"

    Älä epäröi [ottaa yhteyttä CSC Service Deskiin](../contact.md), jos sinulla on kysyttävää CSC:n palveluiden käytöstä. Autamme mielellämme!

## Mitä järjestelmää minun kannattaa käyttää? { #which-system-should-i-use }

### Puhti { #puhti }

Uusien käyttäjien suositellaan aloittavan työskentely
[Puhti-super­tieto­koneella](../../computing/available-systems.md#puhti).
Verrattuna Mahtiin sillä on huomattavasti enemmän
[esiasennettuja ohjelmistoja](../../apps/by_availability.md#puhti), enemmän GPU-solmuja ja
tyypillisesti enemmän muistia CPU-ydintä kohden. Lisäksi Puhtin GPU-solmuilla ja joillakin CPU-solmuilla on
[nopea paikallinen NVMe-tallennus](../../computing/disk.md#temporary-local-disk-areas).

### Mahti { #mahti }

Jos tiedät, että laskentasi on erittäin hyvin rinnakkaistettavissa, kannattaa harkita niiden ajamista
[Mahti-super­tieto­koneella](../../computing/available-systems.md#mahti).
Verrattuna Puhtiin Mahtissa on huomattavasti enemmän CPU-solmuja ja ytimiä per solmu. Mahti on
tarkoitettu laskentaan, joka pystyy tehokkaasti hyödyntämään vähintään kokonaisen CPU-solmun.

Lisäksi, vaikka Mahtissa on vähemmän GPU-solmuja kuin Puhtissa, Mahtin A100-GPU:t
ovat huomattavasti tehokkaampia kuin Puhtin V100-GPU:t, mikä tekee Mahtista
sopivan myös vaativiin [koneoppimisen](ml-guide.md) sovelluksiin.
Toisin kuin Puhtissa, Mahtissa nopea paikallinen NVMe-tallennus on käytettävissä
vain GPU-solmuissa.

### LUMI { #lumi }

[LUMI-super­tieto­kone](../../computing/available-systems.md#lumi)
on yksi maailman nopeimmista. Se on tarkoitettu ensisijaisesti
ajoihin, jotka hyötyvät sen LUMI-G-laitteisto-osion suuresta määrästä tehokkaita GPU:ita. Siinä missä Puhtin ja Mahtin GPU:t
valmistaa Nvidia, LUMIn GPU:t ovat AMD:n, joten varmista, että
GPU-sovelluksesi toimivat AMD:n GPU:illa. LUMIlla on
[omat dokumentaatiosivunsa](https://docs.lumi-supercomputer.eu/).

!!! note "Superlaskennasta"

    CSC:n supertietokoneet tarjoavat resursseja, jotka oikein käytettynä ylittävät selvästi sen, mihin kehittyneimmätkään kuluttajalaitteet pystyvät. Muista kuitenkin, että *et ole niiden ainoa käyttäjä*. Henkilökohtaisella työasemallasi pääset periaatteessa resursseihin heti käsiksi. Supertietokone on jaettu järjestelmä, jossa resursseihin täytyy yleensä jonottaa, koska kysyntä on usein suurempaa kuin tarjonta. Katso lisätietoja [käyttöpolitiikastamme](../../computing/usage-policy.md).

    On myös hyvä muistaa, että laskentojen ajaminen supertietokoneella parantaa suorituskykyä vain, jos hyödynnät sen vahvuuksia.
    Supertietokoneet ovat tehokkaita, koska ne mahdollistavat
    [rinnakkaislaskennan](https://en.wikipedia.org/wiki/Parallel_computing).
    Jos koodiasi ei ole kirjoitettu käyttämään useita CPU-ytimiä tai yhtä tai useampaa GPU:ta, siitä ei välttämättä ole hyötyä verrattuna oman työaseman käyttöön.
    Toisaalta suuret muisti- ja/tai tallennusvaatimukset sekä esiasennetut ohjelmistot ja lisenssit ovat tekijöitä, jotka voivat tehdä CSC:n supertietokoneiden käytöstä sinulle houkuttelevaa.

## Miten pääsen käyttämään CSC:n supertietokoneita? { #how-to-access-csc-supercomputers }

### Verkkokäyttöliittymä { #web-interface }

Puhtilla, Mahtilla ja LUMIlla on jokaisella
[oma verkkokäyttöliittymänsä](../../computing/webinterface/index.md), jonka kautta
voi käyttää supertietokonetta selaimella. Verkkokäyttöliittymä on hyvä valinta
vuorovaikutteiseen laskentaan, kuten datan analysointiin, tutkimiseen ja
visualisointiin. Tätä varten verkkokäyttöliittymässä on useita
vuorovaikutteisia sovelluksia, kuten
[Visual Studio Code](../../computing/webinterface/vscode.md),
[Jupyter](../../computing/webinterface/jupyter.md) ja
[RStudio](../../computing/webinterface/rstudio.md). Lisäksi se tarjoaa
[työpöytäympäristön](../../computing/webinterface/desktop.md), jossa on
graafisia käyttöliittymiä (GUI) käyttäviä ohjelmistoja, sekä
[kiihdytetyn visualisointisovelluksen](../../computing/webinterface/accelerated-visualization.md)
GPU-kiihdytettyä visualisointia ja renderöintiä varten. Vaativaan laskentaan,
kuten täysimittaisten simulaatioiden ajamiseen tai neuroverkkojen kouluttamiseen,
kannattaa käyttää komentorivikäyttöliittymää, koska sen avulla pääset käsiksi
suurempiin resursseihin ja voit ajastaa työsi.

- [Puhti web interface](https://www.puhti.csc.fi)
- [Mahti web interface](https://www.mahti.csc.fi)
- [LUMI web interface](https://www.lumi.csc.fi)

### Komentorivikäyttöliittymä { #command-line-interface }

Vaikka monet verkkokäyttöliittymän vuorovaikutteisista sovelluksista, kuten
Jupyter ja RStudio, ovat helppokäyttöisiä ja siten hyvä lähtökohta CSC:n
supertietokoneiden käyttöön, niiden laskentakapasiteetti on rajattu
melko pieniresurssiseen vuorovaikutteiseen käyttöön. Jos tarvitset enemmän
resursseja (esim. useita CPU-solmuja tai GPU:ita) tai jos työsi vaatii
vuorovaikutteisuuden sijaan tehokkuutta, kannattaa siirtyä käyttämään
tekstipohjaista komentorivikäyttöliittymää ja toimimaan suoraan supertietokoneen
[Linux-käyttöjärjestelmässä](./env-guide/index.md). Tapa voi vaikuttaa
vanhanaikaiselta, mutta siihen tottuessa se on erittäin tehokas.

CLI:n avulla voit
[lähettää laskentasi erätöinä](../../computing/running/getting-started.md)
SLURM-jonohallintaan, joka ajaa ne heti, kun pyydetyt resurssit
ovat saatavilla. Tärkeää on, että eräajojärjestelmä varmistaa töidesi ajon
*laskentasolmuissa* eikä *kirjautumissolmuissa*,
joita [**ei ole** tarkoitettu raskaaseen laskentaan](../../computing/usage-policy.md).
Eräajojen etuna on myös se, että laskentojen ajaminen ei sido sinua
työasemaasi. Vaikka tämän automatisoinnin käyttöönotto vaatii hieman
suunnittelua, pitkällä aikavälillä se tekee työstäsi sekä tehokkaampaa että
toistettavampaa niin itsellesi kuin muillekin, kuten arvioijille ja
yhteistyökumppaneille.

Pääset komentorivikäyttöliittymään joko
käyttämällä verkkokäyttöliittymien
[kuoriosovelluksia](../../computing/webinterface/shell.md) tai
[käyttämällä omalla työasemallasi SSH-asiakasta](../../computing/connecting/index.md#using-an-ssh-client).

!!! note "Yhteyden muodostaminen SSH:lla"
    Huomaa, että muodostettaessa yhteyttä CSC:n supertietokoneisiin
    komentoriviltä SSH-asiakkaalla sinun on ensin otettava käyttöön SSH-avaimet
    ja lisättävä julkinen avaimesi MyCSC-asiakasportaaliin. SSH-avainten ja
    MyCSC:n käyttäminen julkisen avaimesi lisäämiseen supertietokoneelle on
    huomattavasti turvallisempi todennustapa kuin perinteiset salasanat tai
    manuaalisesti hallitut SSH-avaimet.

    [Lue yksityiskohtaiset ohjeet SSH-avainten käyttöönotosta ja käytöstä](../../computing/connecting/ssh-keys.md).

## Kuinka työskennellä ohjelmistojen ja datan kanssa? { #how-to-work-with-software-and-data }

### Ohjelmistot { #software }

CSC:n supertietokoneilla on saatavilla monipuolinen valikoima
[scientific computing -ohjelmistoja](../../apps/index.md). Tässä suhteessa Puhti
erottuu edukseen: sillä on yli sata esiasennettua ohjelmaa. Sovellussivuillamme
on eräajoskriptiesimerkkejä ja ohjeita ohjelmistojen ajamiseen
tehokkaasti CSC:n supertietokoneilla. Suosittelemme lämpimästi käyttämään niitä
lähtökohtana!

CSC:n supertietokoneilla ohjelmisto­ympäristöjä hallitaan
[ympäristömoduuleilla](../../computing/modules.md). Moduulit kattavat kaiken
[kääntäjistä](../../computing/installing.md#compiling) ja
[ohjelmointikielistä](../../apps/by_discipline.md#mathematics-and-statistics)
työnkulkuvälineisiin, kuten
[Nextflow](../../apps/nextflow.md) ja [Snakemake](../../apps/snakemake.md).
Useimpien asennettujen ohjelmistojen tehokas ajaminen edellyttää
[komentorivikäyttöliittymän](#command-line-interface) käyttöä, joten on erittäin
hyödyllistä hallita
[Linux-käyttöjärjestelmän perusteet](./env-guide/index.md).

Vaikka esiasennetut ohjelmistot kattavat laajan kirjon käyttötapauksia, omien
sovellusten asentaminen CSC:n supertietokoneille on myös mahdollista. Prosessi
poikkeaa usein oman koneen asennuksista, joten tutustu
[asennusohjeisiimme](../../computing/installing.md). HPC-sovellusten kääntämistä
varten käytettävissä on erilaisia
[kääntäjiä](../../computing/installing.md#compiling),
[korkean suorituskyvyn kirjastoja](../../computing/hpc-libraries.md) ja muita
työkaluja tämän helpottamiseksi. Huomaa, että jotkin asennukset, kuten
monimutkaiset Python-ympäristöt, hyötyvät
[kontituksesta](../../computing/containers/overview.md).

Saatat haluta myös kehittää omia skriptejäsi ja ohjelmiasi valmiiden ohjelmistojen
sijaan. Tehokkainta on aloittaa koodin kirjoittaminen ja testaaminen omalla
laitteellasi, koska ajaminen jaetussa järjestelmässä (jollaisia supertietokoneet ovat)
tuo väistämättä jonkin verran ylimääräistä kuormaa. Siirry ajamaan skriptejäsi
supertietokoneella vasta, kun olet valmis testaamaan niitä suuremmassa mittakaavassa
tai käyttämään erityisresursseja, kuten GPU:ita.

!!! note "Saatavuuden tarkistaminen"

    Jos sinulla on mielessä jokin tieteellinen ohjelmisto, on varsin todennäköistä,
    että se on asennettuna Puhtiin. Docs CSC:n selaamisen lisäksi voit etsiä
    ohjelmistoja komentoriviltä komennolla
    `module spider <search-pattern>`. Usein ohjelmistomoduulin nimi on yksinkertaisesti
    ohjelmiston nimi, ja vaikka hakukuviosi ei täsmäisi moduulin nimeen täysin,
    haku ei ole kirjainkoosta riippuvainen ja tukee osittaisia osumia.

### Datan tallennus { #data-storage }

CSC:n supertietokoneilla on erilliset
[levyalueet](../../computing/disk.md) eri datan­tallennus­tarkoituksiin.
*Projektilähtöinen* jaettu tallennus löytyy polusta `/scratch/<project>`.
Tämä kansio on jaettu projektin *kaikkien käyttäjien* kesken ja sen
oletuskiintiö on 1 Tt.

Huomaa, että **scratch-levy ei ole tarkoitettu pitkäaikaiseen säilytykseen** ja Puhtissa
tiedostot, joita ei ole käytetty 180 päivään (kun scratch-kiintiö on alle 5 TiB)
tai 90 päivään (kun scratch-kiintiö on 5 TiB tai enemmän), poistetaan automaattisesti. Suosittelemme
[Allas-objektitallennuspalvelua](../../data/Allas/introduction.md) tutkimusdatan
säilyttämiseen silloin, kun sitä ei aktiivisesti käytetä supertietokoneilla. Katso
[lisäohjeet datan hallintaan Puhtin ja Mahtin scratch-levyillä](clean-up-data.md).
Huomaa myös, että arkaluonteista dataa ei saa käsitellä tai säilyttää CSC:n
supertietokoneilla. Tätä tarkoitusta varten meillä on erilliset
[arkaluonteisen datan palvelut](../../data/sensitive-data/index.md).

CSC:n supertietokoneilla on myös pysyvä projektilähtöinen tallennus, jonka
oletuskiintiö on 50 Gt. Se sijaitsee polussa  
`/projappl/<project>` ja sitä suositellaan esimerkiksi omien ohjelmistojen
asennuksiin. Lisäksi jokaisella käyttäjällä on käytettävissään enintään 10 Gt
dataa henkilökohtaisessa kotihakemistossaan (`$HOME`).

[Datan siirtäminen](../../data/moving/index.md) supertietokoneen ja paikallisen
työaseman välillä on helppoa käyttämällä
[verkkokäyttöliittymän tiedostoselainta](../../data/moving/web-interface.md) tai
komentorivin siirtotyökaluja, kuten [scp](../../data/moving/scp.md) ja
[rsync](../../data/moving/rsync.md). Voit myös käyttää
[Linuxin wget-apuohjelmaa](../../data/moving/wget.md) ladataksesi dataa
suoraan verkkosivulta tai FTP-palvelimelta supertietokoneelle.

!!! note "CSC ei varmuuskopioi dataasi!"
    Yhtäkään levyaluetta ei varmuuskopioida automaattisesti CSC:ssä. Tämä tarkoittaa,
    että käyttäjän vahingossa poistamaa dataa ei voida millään tavalla palauttaa.
    Vältä tahatonta datan menetystä varmuuskopioimalla säännöllisesti, esimerkiksi
    Allakseen tai oman organisaatiosi tallennusjärjestelmiin.

## Hyödyllisiä linkkejä { #useful-links }

Voit käyttää navigointisivupalkkia tai hakua löytääksesi lisää
tietoa CSC:n HPC-palveluiden käytöstä. Alla on linkkejä sivuille,
joista on erityisesti hyötyä superlaskennan aloittamisessa CSC:llä.

=== "Käyttäjätilit ja projektit"
    - [Uuden käyttäjätilin luominen](../../accounts/how-to-create-new-user-account.md)
    - [Uuden projektin luominen](../../accounts/how-to-create-new-project.md) ja
      [jäsenten lisääminen olemassa olevaan projektiin](../../accounts/how-to-add-members-to-project.md)
    - [Palveluoikeuksien lisääminen projektille](../../accounts/how-to-add-service-access-for-project.md)
    - [Laskutus](../../accounts/billing.md) ja
      [Laskentayksiköiden hakeminen](../../accounts/how-to-apply-for-billing-units.md)
    - [Salasanan vaihtaminen](../../accounts/how-to-change-password.md)
    - [MyCSC-asiakasportaali](https://my.csc.fi)

=== "Laskenta"
    - [Yleiskatsaus](../../computing/index.md)
    - [Käyttöpolitiikka](../../computing/usage-policy.md)
    - [Yhteyden muodostaminen supertietokoneisiin](../../computing/connecting/index.md)
    - [Eräajojen suorittaminen](../../computing/running/getting-started.md) ja
      [käytettävissä olevat eräajopartiot](../../computing/running/batch-job-partitions.md)
    - [Esiasennetut sovellukset](../../apps/index.md) ja
      [oman ohjelmiston asennusohjeet](../../computing/installing.md)
    - [LUMI:n käyttäjäopas](https://docs.lumi-supercomputer.eu/)

=== "Koulutusmateriaalit ja oppaat"
    - [*CSC Computing Environment* -kurssin materiaalit](https://csc-training.github.io/csc-env-eff/)
    - [Linuxin perusteet -opas](../tutorials/env-guide/index.md)
    - [Koneoppimisen opas](ml-guide.md)
    - [Pythonin käyttö CSC:n supertietokoneilla](python-usage-guide.md)
    - [Datan hallinta Puhti- ja Mahti-scratch-levyillä](clean-up-data.md)
    - Muut [oppaat](index.md) ja
      [koulutusmateriaalit](../training-material/index.md)

=== "Tuki"
    - [Usein kysytyt kysymykset](../faq/index.md)
    - [CSC Service Desk](../contact.md)