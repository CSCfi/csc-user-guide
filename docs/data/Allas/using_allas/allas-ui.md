# Allas-verkkokäyttöliittymä { #allas-web-ui }

Allas Web UI tarjoaa helppokäyttöisen verkkokäyttöliittymän CSC:n objektivarastopalvelulle, Allakselle.

## Aloitus { #getting-started }

1. Siirry osoitteeseen [https://allas.csc.fi](https://allas.csc.fi) ja kirjaudu sisään.
2. Valitse projektisi **Select Project** -pudotusvalikosta.

=== "Kirjautumissivu"
    ![Allas Web UI -kirjautuminen](img/Allas-UI-login.png){ width=80% }

=== "Pääsivu"
    ![Pääsivu](img/Allas-UI-main.png){ width=80% }

## Säiliön luominen { #creating-a-bucket }

Säiliö on objektiesi säilytyskontti. Luo säiliö seuraavasti:

1. Napsauta **Create bucket**.
2. Anna säiliön nimi (nimiä ei voi muuttaa myöhemmin. Katso [säiliön nimeämisen tarkistuslista](../introduction.md#naming-buckets-and-objects)).
3. (Valinnainen) Lisää tunnisteita (tags) parempaa organisointia ja hakua varten.
4. Napsauta **Save**.

![Säiliön luominen](img/Allas-UI-bucket.png){ width=80% }
<br>Uuden säiliön luominen

## Objektien lähettäminen { #uploading-objects }

Voit lähettää objekteja kahdella tavalla:

### Lähettäminen pääsivulta: { #uploading-from-the-main-page }

1. Napsauta koontinäytössä **Upload**-painiketta.
2. Anna säiliön nimi (nimiä ei voi muuttaa myöhemmin. Katso [säiliön nimeämisen tarkistuslista](../introduction.md#naming-buckets-and-objects)).
3. Valitse tai "Drag & Drop" -toiminnolla vedä ja pudota objektit ja napsauta **Upload**.
4. Luodaan uusi säiliö, joka sisältää objektit.

### Lähettäminen olemassa olevaan säiliöön: { #uploading-to-an-existing-bucket }

1. Napsauta olemassa olevaa säiliötä.
2. Paina **Upload**-painiketta.
3. Valitse tai "Drag & Drop" -toiminnolla vedä ja pudota objektit ja napsauta **Upload** tallentaaksesi ne valittuun säiliöön.

=== "Lähettäminen pääsivulta"
    ![Allas Web UI -kirjautuminen](img/Allas-UI-upload1.png){ width=80% }

=== "Lähettäminen olemassa olevaan säiliöön"
    ![Pääsivu](img/Allas-UI-upload2.png){ width=80% }

## Säiliöiden tarkasteleminen ja hallinta { #viewing-and-managing-buckets }

Kun olet luonut säiliöitä ja lähettänyt objekteja, niiden tarkastelu ja hallinta on helppoa.

1. Päänäkymä listaa kaikki säiliösi.
2. Napsauta säiliön nimeä nähdäksesi sen sisällön.
3. Käytä **[Download](#downloading-objects-and-buckets)**-, **[Share](#sharing-a-bucket)**- tai **Options**-valikon ( *[Copy](#copying-a-bucket)*, *Edit tags*, *[Delete](#removing-objects-and-buckets)* ) painikkeita toimintoihin objekteille ja säiliöille.

![Koontinäyttö](img/Allas-UI-dashboard.png){ width=80% }
<br>Säiliöiden hallinta Allaksessa

## Säiliön jakaminen { #sharing-a-bucket }

Jaa säiliö seuraavasti:

1. **Hanki Share ID**:
    - Jos jaat toiseen omaan projektiisi: Vaihda kyseiseen projektiin, paina **Copy Share ID** ja palaa sitten alkuperäiseen projektiisi.
    - Jos jaat toisen käyttäjän projektiin: Pyydä heitä kopioimaan oma Share ID ja lähettämään se sinulle.
2. Etsi jaettava säiliö, napsauta **Share** ja liitä kopioitu Share ID.
3. **Valitse käyttöoikeudet**:
    - **Transfer data**: sallii lataamisen ja kopioinnin.
    - **Collaborate**: sallii lähettämisen ja poistamisen.
    - **View**: lukuoikeus.
4. Viimeistele napsauttamalla **Share**.
5. Näet jakamasi säiliöt **Buckets you have shared** -välilehdellä.
6. Näet sinulle jaetut säiliöt **Buckets shared with you** -välilehdellä.

Huom: Voit aina poistaa säiliön jaon napsauttamalla **Share** ja painamalla **Delete**.

=== "Jako-oikeudet"
    ![Jako-oikeudet](img/Allas-UI-share.png){ width=80% }

=== "Jakamasi säiliöt"
    ![Jakamasi säiliöt](img/Allas-UI-shared.png){ width=80% }

## Säiliön kopioiminen { #copying-a-bucket }

**Käyttötapaus**: Jos haluat säilyttää säiliön datan samalla kun teet testejä tai muutoksia, voit kopioida säiliön ja työskennellä kaksoiskappaleen kanssa ilman, että alkuperäinen muuttuu.

Kopioi säiliö seuraavasti:

1. Napsauta säiliön vieressä olevaa **Options**-painiketta.
2. Valitse **Copy**.

## Objektien ja säiliöiden lataaminen { #downloading-objects-and-buckets }

!!! warning ""
    Yli **5 GiB** kokoisten säiliöiden tai kansioiden lataaminen ei toistaiseksi ole tuettu. Suurempia latauksia varten harkitse **[Command Line Tools](../accessing_allas.md#commandline-tools)** -työkalujen käyttöä.

1. Napsauta **Download**-painiketta säiliön/objektin vieressä.
2. Tiedosto tallennetaan paikalliselle järjestelmällesi.

## Objektien ja säiliöiden poistaminen { #removing-objects-and-buckets }

- **Buckets**: Napsauta säiliön vieressä **Options** > **Delete**.
- **Folders**: Napsauta kansion vieressä **Delete**.
- **Objects**: Napsauta objektin vieressä **Delete**.