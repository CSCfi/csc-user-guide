# Muuta tietokanta-instanssin tilavuuden kokoa {#resize-database-instance-volume}

Kun luot tietokanta-instanssin, määrität sen käytössä olevan tilavuuden koon. Jos myöhemmin huomaat, että koko ei riitä, voit muuttaa tilavuuden kokoa joko verkkokäyttöliittymästä tai CLI:stä. Huomaa, että voit vain kasvattaa tilavuuden kokoa, etkä pienentää sitä.

## Varotoimet {#precautions}

Tilavuuden koon muuttamisen ei pitäisi vaikuttaa tietoihisi, mutta voit tehdä varmuuskopion instanssistasi manuaalisesti ennen koon muuttamista tietojen katoamisen estämiseksi.

Katso ohjeet `manuaalisten varmuuskopioiden` tekemiseen [Varmuuskopiot](backups.md).

## Muuta tilavuuden kokoa verkkokäyttöliittymässä {#resize-volume-from-the-web-interface}

1. Vasemmassa reunassa olevasta sarakkeesta voit siirtyä kohtaan `Tietokanta` -> `Instanssit` ja etsiä instanssin, jonka tilavuuden kokoa haluat muuttaa.

2. Valitun rivin oikeassa reunassa, luo varmuuskopio -painikkeen vieressä, paina `nuolikuvaketta` avataksesi pudotusvalikon ja valitse `Muuta tilavuuden kokoa`.

   ![Valitse 'Muuta tilavuuden kokoa'](../img/cloud_dbaas_resize_volume_1.png "Muuta tilavuuden kokoa")

3. Siellä voit määrittää tietokanta-instanssin `uuden koon` GB:na.  
Huomaa, että uuden arvon on oltava suurempi kuin nykyinen tilavuuden koko.

4. Vahvista muutos painikkeella `Muuta tietokannan tilavuutta`.

   ![Valitse 'Muuta tilavuuden kokoa'](../img/cloud_dbaas_resize_volume_2.png "Muuta tilavuuden kokoa")

5. Muutoksen pitäisi kestää 1-2 minuuttia. Jos verkkokäyttöliittymä ei automaattisesti päivitä tilaa `Muutetaan` tilaan `Aktiivinen`, yritä ladata sivu uudelleen.

   Jos tila on `Muutetaan` yli 5 minuuttia, tarkista alla oleva kohta `Minulla on ongelmia tilavuuden koon muuttamisessa`.

## Muuta tilavuuden kokoa CLI:stä {#resize-volume-from-the-cli}

1. Etsi instanssista `instanssin ID`, jonka tilavuuden kokoa haluat muuttaa:

    ```sh
    openstack database instance list
    ```

2. `Muuta instanssin tilavuuden kokoa`:

    ```sh
    openstack database instance resize volume $INSTANCE_ID $NEW_VOLUME_SIZE
    ```

    Esimerkiksi:  
    openstack database instance resize volume `f37a8ea6-5ed7-4982-8a71-9131756f04ae` `5`

3. 1-2 minuutin kuluttua instanssin `tila` pitäisi olla `AKTIIVINEN`:  

    ```sh
    openstack database instance show $INSTANCE_ID
    ```

    Jos tila on `Muutetaan` yli 5 minuuttia, tarkista alla oleva kohta `Minulla on ongelmia tilavuuden koon muuttamisessa`.

## Minulla on ongelmia tilavuuden koon muuttamisessa {#im-having-problems-with-resizing-the-volume}

### Tila juuttunut MUUTETAAN-tilaan {#status-stuck-on-resizing}

Varmista, että olet yrittänyt `ladata verkkokäyttöliittymäsivu uudelleen` tai suorittanut `openstack database instance show $INSTANCE_ID` komennon 5 minuutin kuluttua tilavuuden koon muuttamisesta. Jos instanssin tila on `MUUTETAAN` 5 minuutin kuluttua, ole hyvä ja [ota meihin yhteyttä](../../support/contact.md).