# Tilit { #accounts }

## Yleiskatsaus { #overview }

CSC:n laskenta- ja tallennuspalveluiden käyttö perustuu _käyttäjätileihin_ ja _projekteihin_:

*   **Käyttäjätilejä** käytetään käyttäjien todennukseen ja hallintaan. Jokaisella käyttäjällä tulisi olla vain yksi käyttäjätili CSC:llä. Käyttäjätilit ovat aina henkilökohtaisia ja edellyttävät monivaiheista tunnistautumista. Tilin tunnistetietojen jakaminen muille tai tilin käytön salliminen muille on kiellettyä.

*   **CSC-projekteja** käytetään CSC:n palveluihin ja CSC:n tarjoamiin resursseihin pääsyn hallintaan. CSC:n palveluihin, kuten Puhti, Allas tai cPouta, myönnetään käyttöoikeus CSC-projekteille. Sama koskee Billing Units -yksiköitä, joita kulutetaan, kun näitä palveluja käytetään.
CSC-projekti voi sisältää yhden tai useita CSC-käyttäjätilejä, ja yksi käyttäjätili voi kuulua useisiin projekteihin. Jokaisella CSC-projektilla on oltava projektipäällikkö, joka luo projektin, hallinnoi projektiin kuuluvia käyttäjätilejä ja palveluja sekä vastaa resurssien käytöstä.
Projektipäällikkö on tyypillisesti tutkimusryhmän vetäjä tai muu kokeneempi tutkija. Katso tarkemmat [projektipäällikön edellytykset](https://research.csc.fi/en/prerequisites-for-a-project-manager){:target="_blank"}.

*   **Billing Units** (BU:t) -yksiköitä käytetään resurssien kohdentamiseen käyttäjien projekteille. Projekteilla voi olla neljää erilaista BU-tyyppiä: **CPU**, **GPU**, **Storage** ja **Cloud**, ja niitä kulutetaan, kun käytät palvelujamme tutkimuksessasi. Voit hakea Billing Units -yksiköitä [MyCSC](https://my.csc.fi) -portaalissa, ja CSC myöntää BU:t projekteille. [Käyttö kuluttaa Billing Units -yksiköitä](billing.md), mutta **varsinaista maksua** ei vaadita.

*   **LUMI-projekteja** käytetään LUMI-järjestelmään pääsyn ja sen tarjoamien resurssien hallintaan. LUMI-projektit ovat rajattuja vain LUMI-ympäristöön (LUMI-C, LUMI-G jne.). Suomalaisten LUMI-projektien kesto ja resurssit ovat kiinteitä, ja kokonaisresurssit on määriteltävä jo projektihakemuksessa. LUMI-projekteja käytetään myös [FiQCI-kvanttitietokoneille](../computing/quantum-computing/access.md). Lisätietoja löydät [näistä ohjeista](https://www.lumi-supercomputer.eu/get-started-2021/users-in-finland/){:target="_blank"}. 

*   **My.csc.fi-portaali** MyCSC on CSC:n itsepalveluasiakasportaali tutkimuksen ja koulutuksen asiakkaille ja loppukäyttäjille. MyCSC on käytettävissä myös muille CSC:n asiakkaille tai loppukäyttäjille, jos heillä on CSCID-käytäntöjen mukaiset CSC-käyttäjätilit.
MyCSC-portaali tarjoaa käyttäjille toiminnallisuudet CSC-käyttäjätilien rekisteröimiseen, laskenta- tai dataprojektien luomiseen, jäsenten lisäämiseen projekteihin ja resurssien hakemiseen projekteille. Käyttäjät voivat myös hallita projektejaan ja projektien elinkaarta MyCSC:ssä, ja he voivat nähdä siellä resurssien kulutuksen ja tallennettujen tietojen määrän.

*   **FMI-käyttäjätilit** Puhti-supertietokoneessa on erillinen osio Ilmatieteen laitokselle. FMI-käyttäjät voivat käyttää myös Puhtin yleisosaa normaaleihin projekteihin. [Katso FMI-käyttäjille suunnatut ohjeet](fmi.md).


CSC:n palvelut ovat maksuttomia akateemiseen tutkimukseen, opetukseen tai koulutukseen suomalaisten korkeakoulujen ja valtion tutkimuslaitosten jäsenille.

## Käyttöoikeuden hankkiminen { #getting-access }

Ohjeet käyttäjätilin ja projektin hankkimiseen CSC:n palveluihin pääsyä varten:

1. [Luo käyttäjätili](how-to-create-new-user-account.md)
1. [Luo projekti](how-to-create-new-project.md) tai
   [liity projektiin](how-to-add-members-to-project.md)
1. [Lisää projektiisi palveluoikeudet](how-to-add-service-access-for-project.md)
1. [Hae Billing Units -yksiköitä](how-to-apply-for-billing-units.md) tai
   [levykiintiötä](how-to-increase-disk-quotas.md), tarpeen mukaan
1. [Uudista salasanasi](how-to-change-password.md) vuosittain

Katso erilliset ohjeet [LUMI](https://docs.lumi-supercomputer.eu/firststeps/getstarted/) -supertietokoneelle.

Kaikki nämä tehtävät voi suorittaa
[itsepalveluportaalissa MyCSC](https://my.csc.fi).