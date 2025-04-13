
# Allas Web UI

Allas Web UI tarjoaa helppokäyttöisen verkkokäyttöliittymän CSC:n objektitallennuspalveluun, Allakseen.

## Aloittaminen {#getting-started}

1. Siirry osoitteeseen [https://allas.csc.fi](https://allas.csc.fi) ja kirjaudu sisään.
2. Valitse projektisi **Valitse projekti** -valikosta.


=== "Kirjautumissivu"
    ![Allas Web UI -kirjautuminen](img/Allas-UI-login.png){ width=80% }

=== "Pääsivu"
    ![Pääsivu](img/Allas-UI-main.png){ width=80% }

## Kaukalon luominen {#creating-a-bucket}

Kaukalo on objektiesi tallennussäiliö. Luodaksesi sellaisen noudata näitä ohjeita:

1. Klikkaa **Luo kaukalo**.
2. Syötä kaukalon nimi (nimiä ei voi muokata myöhemmin. Katso [kaukalon nimeämisohjeet](../introduction.md#naming-buckets)).
3. (Valinnainen) Lisää tageja paremman organisoinnin ja hakutoimintojen vuoksi.
4. Klikkaa **Tallenna**.

![Luo kaukalo](img/Allas-UI-bucket.png){ width=80% }
<br>Uuden kaukalon luominen

## Objektien lataaminen {#uploading-objects}

Voit ladata objekteja kahdella tavalla:

### Lataaminen pääsivulta: {#uploading-from-the-main-page}
1. Paina **Lataa**-painiketta hallintapaneelissa.
2. Syötä kaukalon nimi (nimiä ei voi muokata myöhemmin. Katso [kaukalon nimeämisohjeet](../introduction.md#naming-buckets)).
3. Valitse/”Raahaa ja pudota” objekteja ja klikkaa **Lataa**.
4. Uusi kaukalo, joka sisältää objektit, luodaan.


### Lataaminen olemassa olevaan kaukaloon: {#uploading-to-an-existing-bucket}
1. Klikkaa olemassa olevaa kaukaloa.
2. Paina **Lataa**-painiketta.
3. Valitse/”Raahaa ja pudota” objekteja ja klikkaa **Lataa** tallentaaksesi ne valittuun kaukaloon.

=== "Lataaminen pääsivulta"
    ![Allas Web UI -kirjautuminen](img/Allas-UI-upload1.png){ width=80% }

=== "Lataaminen olemassa olevaan kaukaloon"
    ![Pääsivu](img/Allas-UI-upload2.png){ width=80% }

## Kaukalojen tarkastelu ja hallinta {#viewing-and-managing-buckets}

Kaukalojen luomisen ja objektien lataamisen jälkeen voit tarkastella ja hallita niitä helposti.

1. Pääasiallinen hallintapaneeli listaa kaikki kaukalosi.
2. Klikkaa kaukalon nimeä nähdäksesi sen sisällön.
3. Käytä **[Lataa](#downloading-objects-and-buckets)**, **[Jaa](#sharing-a-bucket)** tai **Valinnat** -painikkeita (*[Kopioi](#copying-a-bucket)*, *Muokkaa tageja*, *[Poista](#removing-objects-and-buckets)*) objektien ja kaukaloiden toimenpiteille.

![Hallintapaneeli](img/Allas-UI-dashboard.png){ width=80% }
<br>Kaukalojen hallinta Allaksessa

## Kaukalon jakaminen {#sharing-a-bucket}

Kaukalon jakamiseksi noudata näitä ohjeita:

1. **Hanki Jako-ID**:
    - Jos jaat toiseen projektisi: Vaihda siihen projektiin, paina **Kopioi Jako-ID**, ja palaa alkuperäiseen projektiisi.
    - Jos jaat toisen käyttäjän projektiin: Pyydä häntä kopioimaan Jako-ID ja lähettämään se sinulle.
2. Etsi kaukalo, jonka haluat jakaa, klikkaa **Jaa** ja liitä kopioitu Jako-ID.
3. **Valitse oikeudet**:
    - **Siirrä dataa**: Mahdollistaa lataamisen ja kopioimisen.
    - **Tee yhteistyötä**: Mahdollistaa lataamisen ja poistamisen.
    - **Katso**: Vain lukuoikeudet.
4. Klikkaa **Jaa** viimeistelläksesi prosessin.
5. Näet jakamasi kaukalot **Jaetut kaukalot** -välilehdellä.
6. Näet sinulle jaetut kaukalot **Sinulle jaetut kaukalot** -välilehdellä.

**Huom:** Voit aina poistaa jaon kaukalosta klikkaamalla **Jaa** ja painamalla **Poista**.

=== "Jakamisoikeudet"
    ![Jakamisoikeudet](img/Allas-UI-share.png){ width=80% }

=== "Jaetut kaukalot"
    ![Jaetut kaukalot](img/Allas-UI-shared.png){ width=80% }

## Kaukalon kopiointi {#copying-a-bucket}

**Käyttötapaus**: Jos haluat säilyttää kaukalossa olevan datan samalla kun suoritat testejä tai muutoksia, voit kopioida sen ja työskennellä kopiolla vaikuttamatta alkuperäiseen.

Kaukalon kopioimiseksi:

1. Klikkaa **Valinnat**-painiketta kaukalon vieressä.
2. Valitse **Kopioi**.

## Objektien ja kaukaloiden lataaminen {#downloading-objects-and-buckets}

!!! warning ""
    Kaukaloiden tai kansioiden lataaminen, jotka ovat suurempia kuin **5 GiB**, ei tällä hetkellä ole tuettu. Suurempia latauksia varten käytä mieluummin **[Komentorivityökaluja](./rclone.md)**.


1. Klikkaa **Lataa**-painiketta kaukalon / objektin vieressä.
2. Tiedosto tallennetaan paikalliselle järjestelmällesi.

## Objektien ja kaukaloiden poistaminen {#removing-objects-and-buckets}

- **Kaukalot**: Tyhjennä ensin kaukalo, sitten klikkaa **Valinnat** > **Poista** kaukalon vieressä.
- **Objektit**: Klikkaa **Poista** objektin vieressä.
