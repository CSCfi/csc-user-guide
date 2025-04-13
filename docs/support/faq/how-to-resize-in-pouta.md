
# Kuinka muuttaa instanssin tai levyn kokoa Poutassa
## Muuta instanssin kokoa {#resize-an-instance}
### Käyttämällä tilannevedosta {#using-a-snapshot}
Kohtaatko suorituskykyongelmia alkuperäisellä instanssillasi ja haluaisit ajaa instanssisi suuremmalla maulla?  
On mahdollista edetä ottamalla tilannevedos instanssistasi ja sitten käynnistämällä uusi instanssi uudella maulla tilannevedosta käyttäen.  
Voit löytää enemmän tietoa tilannevedoksista [täältä](../../cloud/pouta/snapshots.md) ja miten edetä.

### Käyttämällä koonmuutos-toimintoa {#using-the-resize-functionality}
!!! Warning
    [I/O maut](../../cloud/pouta/vm-flavors-and-billing.md#io-flavors_2) ja [GPU maut](../../cloud/pouta/vm-flavors-and-billing.md#gpu-flavors_2) eivät voi vaihtaa eri makuperheeseen. Suosittelemme käyttämään [tilannevedoksia](../../cloud/pouta/snapshots.md#launching-an-instance-from-a-volume-snapshot).

!!! Warning  
    On mahdollista muuttaa kokoa `standard` makuperheestä `hpc` makuperheeseen. Mikään ei estä sinua tekemästä tätä, mutta se on **erittäin epäsuositeltavaa!**  
    Voit menettää tietoja prosessin aikana ja CSC ei ole vastuussa. Suosittelemme muuttamaan kokoa vain saman makuperheen makuihin (paitsi I/O maut, katso yllä).

Instanssisi **Toimintovalikossa** valitse **Muuta kokoa** aloittaaksesi prosessin:

![muuta-kokoa-nappi](img/resize_button.png)

Ikkuna avautuu. Valitse uusi maku:

![muuta-kokoa-ikkuna](img/resize_window.png)

Klikkaa **Muuta kokoa**

Odota muutama minuutti ja prosessin aikana sinua pyydetään vahvistamaan koonmuutos:

![vahvista-koko](img/confirm_resize.png)

Kun instanssisi on tilassa `Vahvista koonmuutos/Siirrä`, voit yhdistää instanssiisi tarkistaaksesi, että kaikki toimii hienosti, koska se on jo muunnettu uuteen makuun.  
Jos huomaat jotain vialla, voit palauttaa edelliseen tilaan `Palauta koonmuutos/Siirrä` -napilla pudotusvalikosta.

!!! error-label  
    Huomaa, että automaattinen vahvistusprosessi käynnistetään kolmen päivän kuluttua tilasta `Vahvista tai palauta koonmuutos/Siirrä`.

Kun prosessi on päättynyt, sinun pitäisi olla instanssisi uuden maun kanssa.

## Muuta levyn kokoa {#resize-a-volume}
!!! Notes  
    Voit ainoastaan laajentaa levyä. Tällä hetkellä levyn kutistamista ei tueta Openstackissa.

Pouta antaa sinun luoda [ulkoisia levyjä](../../cloud/pouta/storage.md). Jos alkuperäinen levysi on liian pieni, voit muuttaa sen kokoa.

!!! Note
    Jos levysi on kytketty instanssiisi, sinun täytyy irrottaa se voidaksesi muuttaa kokoa

Levyt-sivulta, **Toimintavalikossa** klikkaa **Laajenna levyä**:

![muuta-levyn-kokoa](img/resize_volume.png)

Ikkuna avautuu. Syötä uusi levysi määrä:

![muuta-levyn-kokoa-ikkuna](img/resize_volume_window.png)

Klikkaa **Laajenna levyä**

Sinun pitäisi nähdä levysi uusi koko.

Voit nyt liittää uuden levyn takaisin instanssiisi.

## Mukauta levyn kokoa luotaessa instanssia {#customize-disk-size-when-creating-the-instance}

Mukauttaaksesi juurilevyn kokoa instanssin luomisen aikana (tilannevedoksen sijaan), noudata näitä vaiheita:

1. Mene kohtaan **Projekti > Laskenta > Instanssit** ja klikkaa **Käynnistä Instanssi**.
2. **Yksityiskohdat**-osiossa:
   - **Instanssin nimi**: Syötä nimi instanssillesi.
   - **Maku**: Valitse sopiva maku, kuten `standard.tiny` (oletus 80 GB levytilalla).
   - **Instanssin käynnistyslähde**: Valitse **Käynnistä kuvasta (luo uusi volyymi)**.
   - **Kuvan nimi**: Valitse kuva, jota haluat käyttää (esim. AlmaLinux-8).
   - **Laitteen koko**: Säädä juuriosion kokoa haluamaasi kokoon, kuten kuvassa (esim. 200 GB oletus 80 GB:n sijaan).
   
   - Tämä kenttä antaa sinulle mahdollisuuden mukauttaa juuriosion kokoa makun oletuslevykokoa suuremmaksi, kuten alla olevassa kuvassa.

3. Kun olet konfiguroinut loput asetusvaihtoehdot (turvallisuus, verkotus jne.), klikkaa **Käynnistä**.

![cloud_pouta_koosta_muokattu_levy](img/cloud_pouta_resize_custome_disk.png)

Jos haluat mieluummin laajentaa levyä tilannevedosta käyttäen, vieraile [Levyn tilannevedokset](../../cloud/pouta/snapshots.md#volume-snapshots) saadaksesi tarkempia ohjeita.
