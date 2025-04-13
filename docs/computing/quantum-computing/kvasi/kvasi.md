
# Kvasiin pääsy

Tarvitset ensin CSC-käyttäjätunnuksen Puhtille. Jos sinulla ei ole käyttäjätunnusta, tutustu 
[kuinka aloittaa uutena käyttäjänä CSC:llä?](../../../support/faq/how-to-get-started-at-CSC.md) usein kysyttyihin kysymyksiin.

Voidaksesi päästä Kvasiin, CSC-käyttäjätunnuksesi täytyy kuulua `kvasi-users` -ryhmään. Lähetä sähköpostia osoitteeseen servicedesk@csc.fi ja pyydä lisäystä **kvasi-users** -ryhmään.

Kun sinut on lisätty, voit käyttää SSH:ta kirjautuaksesi suoraan osoitteeseen kvasi.csc.fi.

## SSH-tunnelin perustaminen Jupyter-verkkokäyttöliittymälle {#setting-up-an-ssh-tunnel-for-the-jupyter-web-interface}

Jotta voit käyttää Jupyter-muistikirja-ympäristöä, sinun on asetettava SSH-tunneli, joka ohjaa muistikirjaympäristösi tulostusportin paikalliselle tietokoneellesi. Seuraa näitä ohjeita:

1. Kirjaudu Kvasiin SSH:lla:
    * `ssh <käyttäjätunnus>@kvasi.csc.fi`
2. Käynnistä Jupyter-palvelin: `./qlm_notebooks/launch_qlm_notebooks`. Tämä antaa sinulle kaksi arvoa:
    * Jupyter-portin numero. Se on `8888`, tai suurempi
    * Token verkkokäyttöliittymään pääsemiseksi (kirjain- ja numeromerkkijono)
    * Esimerkkiulostulo:

```
Jupyter port : 8888
Jupyter token: 123456abcdef

Jotta pääset Jupyter-muistikirjaasi paikalliselta tietokoneeltasi:

1. Luo SSH-tunneli: 
    ssh -L 8890:localhost:8888 yourcscusername@kvasi.csc.fi

2. Avaa selaimen linkki: http://127.0.0.1:8890/?token=123456abcdef
```

3. Aloita SSH-tunneli, siirtäen Jupyter-portin paikalliselle porttinumerolle.
   Voit valita esimerkiksi `8890` paikalliseksi portiksi
    * SSH-tunnelin avaamisen yksityiskohdat riippuvat SSH-asiakkaastasi.
    * Komentorivillä voit kirjautua uudelleen toisesta terminaalista,
      nyt määrittelemällä portin uudelleenohjaus käyttäen yllä annettua ssh-komentoa.

4. Avaa selaimesi ja mene osoitteeseen, joka on annettu ulostulona, esimerkiksi 
`http://127.0.0.1:8890/?token=123456abcdef` Tämä pitäisi avata Kvasin verkkokäyttöliittymä, jossa on kaksi päävaihtoehtoa tutkittavana:
    * **Käsikirja** (vasemmalla)
    * **Jupyter-muistikirja ympäristö esimerkeillä** (oikealla)

## myQLM {#myqlm}

myQLM on kevytversio QLM-ekosysteemistä, jota voidaan ajaa Kvasi QLM:n ulkopuolella. myQLM:n avulla voit suunnitella ja simuloida kvanttialgoritmeja paikallisesti, omalla tietokoneellasi. MyQLM soveltuu hyvin kvanttialgoritmien tutkimisen aloittamiseen. QLM:n kehittyneet ominaisuudet puuttuvat, mutta perusominaisuudet ovat samat.

myQLM on nyt avoin ja se voidaan ladata Linuxille ja Windowsille täältä:
[myQLM docs and installation instructions](https://myqlm.github.io/index.html)

Voit myös käyttää myQLM:ää suoraan [CSC Noppen ympäristöstä](https://noppe.csc.fi).
Kirjautumisen jälkeen käynnistä yksinkertaisesti uusi "myQLM Notebooks" -ympäristö ja avaa se selaimessasi.
Aiempiin kursseihin liittyvää koulutusmateriaalia löytyy kansiosta **CourseMaterial**.

## Linkit {#links}

* [Webinaari: Quantum Computing and Programming in Two Hours (2021)](https://youtu.be/whoTr3zM3jU)
* [Webinaari: Kvanttilaskentaa ja -ohjelmointia kahdessa tunnissa (2021)](https://youtu.be/EnDKcCAjRtg)
* [Webinaari: What is Quantum Computing? (2019)](https://youtu.be/44F0rYmLT4Y)
* [Verkkopohjainen: Introduction to Quantum Computing and Algorithms](https://ssl.eventilla.com/event/mZ9Pa)
* [The Quantum Learning Machine at atos.net](https://atos.net/en/solutions/quantum-learning-machine)
