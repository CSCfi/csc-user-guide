
# Graafiset tiedostonsiirtotyökalut {#graphical-file-transfer-tools}

On olemassa runsaasti graafisia tiedostonsiirtotyökaluja, joita voit asentaa
paikalliselle tietokoneellesi siirtääksesi dataa CSC:n palvelimille tai sieltä pois.
Tässä esittelemme lyhyesti kaksi niistä: **FileZilla**, joka on saatavilla Windowsille,
macOS:lle ja Linuxille, sekä **WinSCP**, joka on saatavilla Windowsille. **Cyberduck**,
josta keskustellaan [Allas-käyttöohjeessa](../Allas/using_allas/cyberduck.md), voi myös
käyttää tähän tarkoitukseen.

## FileZilla – yleinen tiedostonsiirtotyökalu {#filezilla-a-general-file-transfer-tool}

FileZilla on tiedostonsiirtotyökalu, jonka voit asentaa kaikille yleisille käyttöjärjestelmille
(Windows, macOS, Linux). Voit ladata FileZilla-asiakkaan FileZilla-kotisivulta
(palvelinta ei tarvita):

- [FileZilla ladattavat](https://filezilla-project.org/download.php?show_all=1)

Kun käynnistät FileZillan, graafinen tiedostonsiirtonäkymä avautuu näytöllesi.
Yhteyden avaaminen CSC:hen tapahtuu avaamalla _Sivun hallinta_ -paneeli
(napsauta kuvaketta tai valitse _Tiedosto_ > _Sivun hallinta_).

Esimerkiksi, käytä seuraavia asetuksia yhdistääksesi Puhtiin:

- Protokolla: SFTP - SSH tiedostonsiirtoprotokolla
- Isäntä: `puhti.csc.fi`
- Portti: `22`
- Kirjautumistyyppi: Avaintiedosto
- Käyttäjä: CSC-käyttäjätunnuksesi
- Avaintiedosto: Polku
  [SSH-yksityisavaimeesi](../../computing/connecting/ssh-keys.md) paikallisella
  koneellasi

![FileZilla käyttöliittymä](../../img/filezilla.png 'FileZilla käyttöliittymä')

Klikkaa _Yhdistä_. Jos yhdistät ensimmäistä kertaa, FileZilla kysyy luotatko isäntään,
ja sen jälkeen kysyy SSH-avaimen salasanaa.

Kun yhteys on avattu, FileZilla näyttää kaksi interaktiivista tiedostolistausta
vierekkäin. Vasemmalla puolella on paikallinen tiedostojärjestelmäsi ja oikealla puolella
etätiedostojärjestelmä (esim. tiedostot Puhtissa). Voit vaihtaa sijaintia interaktiivisella
selaamisella tai kirjoittamalla hakemistopolun _Paikallinen sijainti_ tai _Etäsijainti_
kenttään.

Kun olet saanut oikeat hakemistot auki sekä paikallisella että etäsijainnilla, voit kopioida
tiedostoja tai hakemistoja paikkojen välillä valitsemalla tiedoston tai kansion hiirellä ja
vetämällä sen toiseen sijaintiin. Muiden toimintojen osalta kokeile napsauttaa hiiren
oikeaa painiketta tiedoston tai kansion päällä.

## WinSCP - tiedostonsiirto ja paljon muuta Windowsissa {#winscp-file-transfer-and-more-on-windows}

WinSCP on ilmainen avoimen lähdekoodin ohjelma Windowsille. Se tarjoaa turvallisen
tiedostonsiirron paikallisen ja etäkoneen välillä. WinSCP tukee SFTP-, FTP- ja SCP-siirtoprotokollia.
Siirtojen lisäksi WinSCP:ssä on monia ominaisuuksia, jotka tekevät tiedostojen
käsittelystä yksinkertaista. WinSCP:n asennusdokumentaatio on saatavilla
[viralliselta sivustolta](https://winscp.net/eng/docs/installation).

WinSCP:ssä on kaksi graafista käyttöliittymää: _Explorer_ ja _Commander_.
Voit valita oletuskäyttöliittymän WinSCP:n asennuksen yhteydessä, mutta voit
myöhemmin muuttaa sen asetuskeskustelussa. Explorer-käyttöliittymä näyttää ja
toimii kuin Windowsin Resurssienhallinta. Jos olet tottunut Windowsin
Resurssienhallintaan, saatat pitää WinSCP Explorer -käyttöliittymää helpompana käyttää.

Aloita WinSCP ja anna kirjautumistietosi, esimerkiksi:

- Tiedostoprotokolla: SFTP
- Isäntänimi: `puhti.csc.fi`
- Porttinumero: 22
- Käyttäjänimi: CSC-käyttäjätunnuksesi
- Salasana: jätä tyhjäksi, sillä käytät
  [SSH-avainta](../../computing/connecting/ssh-keys.md)

![WinSCP-sivun asetukset ilman salasanaa mutta ssh-yksityisavain käytössä](https://a3s.fi/docs-files/winscp-ssh-key-add-1.png 'Ei salasanaa WinSCP:lle')

Klikkaa _Advanced_ (Lisäasetukset) -painiketta ja avaa _SSH_ > _Authentication_
(Todennus)-välilehti. Kirjoita polku SSH-yksityisavaimeesi _Private key file_
(Yksityisen avaimen tiedosto) -kenttään ja klikkaa _OK_.

![WinSCP lisäasetukset ssh-yksityisavaimen lisäämiseksi](https://a3s.fi/docs-files/winscp-ssh-key-add.png 'Lisää SSH-avain WinSCP:hen')

Klikkaa _Login_ (Kirjaudu) yhdistääksesi. Jos yhdistät ensimmäistä kertaa, WinSCP
kysyy luotatko isäntään, ja sen jälkeen kysyy SSH-avaimen salasanaa.

### Tiedostojen lataaminen CSC-ympäristöön {#uploading-files-to-csc-environment}

Voit käyttää monia WinSCP:n työkaluja ladataksesi tiedostoja CSC:n laskenta-
ympäristöön. Helpompia menetelmiä ovat hiirellä raahaaminen, kopioiminen ja
liittäminen tai Windows Explorerin _Lähetä kohteeseen_-toiminto.

Kun käytät vetämistä ja pudottamista, valitse paikalliset tiedostot, jotka
haluat ladata esim. Windows Exploreriin. Vedä sitten valitut tiedostot hiirelläsi
ja pudota ne WinSCP:n käyttöliittymän etäpaneeliin.

Kopioimalla ja liittämällä, valitse paikalliset tiedostot, jotka
haluat ladata esim. Windows Explorerissa ja kopioi ne leikepöydälle.
Siirry sitten WinSCP:n käyttöliittymään ja valitse _File|Paste_ (Tiedosto|Liitä)
valikosta (tai _Ctrl+V_). Huomaa: jos leikepöydän sisältö on pelkkä tekstimerkki,
_File|Paste_-operaatio toimii eri tavalla. Tässä tapauksessa se avaa
leikepöydällä tallennetun polun, eikä liitä tiedostoja.

Voit käyttää Windows Explorerin _"Lähetä kohteeseen"_ -toimintoa ladataksesi
tiedostoja palvelimelle. Ottaaksesi tämän ominaisuuden käyttöön, käytä asennusohjelmaa
tai valitse ominaisuus asetuksissa ("lisää latauksen oikotie Exploreriin 'lähetä
kohteeseen' kontekstivalikkoon").

### Tiedostojen lataaminen CSC-ympäristöstä {#downloading-files-from-csc-environment}

Helpoimmat tavat ladata tiedostoja ovat hiirellä raahaaminen ja URL-osoitteiden
käyttäminen. Kun käytät vetämistä ja pudottamista, valitse ensin etätiedostot,
jotka haluat ladata WinSCP:n käyttöliittymän etäpaneelista. Vedä sitten
valitut tiedostot hiirelläsi ja pudota ne paikalliseen hakemistoon esim.
Windows Explorerissa.

Voit rekisteröidä WinSCP:n käsittelemään SFTP- ja SCP-protokollan URL-osoitteita.
Rekisteröidäksesi tämän ominaisuuden, käytä asennusohjelmaa tai valitse ominaisuus
asetuksista ("Rekisteröidy käsittelemään sftp:// ja scp:// osoitteita"). Nyt voit
kirjoittaa URL-osoitteen verkkoselaimeesi ja WinSCP antaa sinun ladata tiedoston.

![WinSCP käyttöliittymä](/img/Winscp2.jpg 'WinSCP käyttöliittymä')

### Muita WinSCP:n toimintoja {#other-winscp-operations}

WinSCP tarjoaa monia lisätiedosto- ja hakemistotoimintoja siirtojen
lisäksi. Näihin pääse käsiksi napsauttamalla mitä tahansa objektia hiiren
oikealla painikkeella käyttöliittymässä ja valitsemalla toimenpide
ponnahdusvalikosta. On myös mahdollista napsauttaa hiiren oikeaa painiketta
tiedoston tai hakemiston päällä, ja esim. vetää se toiseen sijaintiin.

### Lisädokumentaatio {#further-documentation}

- [Laaja WinSCP dokumentaatio](https://winscp.net/eng/docs/start)

