# Graafiset tiedostonsiirtotyökalut {#graphical-file-transfer-tools}

Paikalliselle tietokoneellesi on saatavilla useita graafisia tiedostonsiirtotyökaluja, joiden avulla voit siirtää dataa CSC:n palvelimille ja takaisin. Tässä esittelemme lyhyesti kaksi niistä: **FileZilla**, joka on saatavilla Windows-, macOS- ja Linux-laitteille, sekä **WinSCP**, joka on saatavilla Windowsille. **Cyberduck** -ohjelmaa käsitellään [Allas-käyttäjän oppaassa](../Allas/using_allas/cyberduck.md), ja sitä voi myös käyttää tähän tarkoitukseen.

## FileZilla – yleinen tiedostonsiirtotyökalu {#filezilla--a-general-file-transfer-tool}

FileZilla on tiedostonsiirtotyökalu, jonka voi asentaa kaikille yleisimmille käyttöjärjestelmille (Windows, macOS, Linux). FileZilla-asiakasohjelman voi ladata FileZillan kotisivulta (palvelinta ei tarvita):

- [FileZilla downloads](https://filezilla-project.org/download.php?show_all=1)

Kun käynnistät FileZillan, näytölle avautuu graafinen tiedostonsiirtoikkuna. Yhteyden avaamiseksi CSC:lle aukaise _Site Manager_ -paneeli (klikkaa kuvaketta tai valitse _File_ > _Site Manager_).

Voit esimerkiksi muodostaa yhteyden Puhtiin seuraavilla asetuksilla:

- Protocol: SFTP - SSH File Transfer Protocol
- Host: `puhti.csc.fi`
- Port: `22`
- Logon type: Key file
- User: CSC-käyttäjätunnuksesi
- Key file: Polku paikallisella koneellasi olevaan [SSH-yksityiseen avaimeseen](../../computing/connecting/ssh-keys.md)

![FileZilla interface](../../img/filezilla.png 'FileZilla interface')

Klikkaa _Connect_. Jos yhdistät ensimmäistä kertaa, FileZilla kysyy luotatko isäntään ja pyytää SSH-avaimen salasanaa.

Kun yhteys on avattu, FileZilla näyttää kaksi interaktiivista tiedostoluetteloa rinnakkain. Vasemmalla on paikallinen tiedostojärjestelmäsi ja oikealla puolella etäkoneen tiedostojärjestelmä (esim. Puhdin tiedostot). Voit vaihtaa sijaintia selaamalla kansioita interaktiivisesti tai kirjoittamalla hakemiston polun _Local site_- tai _Remote site_ -kenttiin.

Kun oikeat hakemistot ovat auki sekä paikallisella että etäkoneella, voit siirtää tiedostoja tai kansioita niiden välillä valitsemalla tiedoston tai kansion ja vetämällä sen hiirellä toiseen puoleen. Muita toimintoja varten yritä napsauttaa tiedostoa tai kansiota hiiren oikealla painikkeella.

## WinSCP - tiedostonsiirtoa ja enemmän Windowsilla {#winscp---file-transfer-and-more-on-windows}

WinSCP on ilmainen avoimen lähdekoodin ohjelma Windowsille. Se mahdollistaa turvallisen tiedostonsiirron paikallisen ja etäkoneen välillä. WinSCP tukee SFTP-, FTP- ja SCP-siirtoprotokollia. Siirtojen lisäksi WinSCP:llä on monia ominaisuuksia, jotka tekevät tiedostojen käsittelystä helppoa. WinSCP:n asennusohjeet löytyvät [viralliselta sivulta](https://winscp.net/eng/docs/installation).

WinSCP:ssä on kaksi graafista käyttöliittymää: _Explorer_ ja _Commander_. Valitset oletuskäyttöliittymän ohjelman asennuksen yhteydessä, mutta voit vaihtaa sitä myöhemmin asetuksista. Explorer-käyttöliittymä näyttää ja toimii samankaltaisesti kuin Windowsin Resurssienhallinta. Jos olet tottunut Windowsin Resurssienhallintaan, Explorer-näkymä on luonteva vaihtoehto.

Käynnistä WinSCP ja syötä kirjautumistietosi esimerkiksi näin:

- File protocol: SFTP
- Host name: `puhti.csc.fi`
- Port number: 22
- User name: CSC-käyttäjätunnuksesi
- Password: jätä tyhjäksi, koska käytät [SSH-avainta](../../computing/connecting/ssh-keys.md)

![WinSCP site settings without password but use ssh private key](https://a3s.fi/docs-files/winscp-ssh-key-add-1.png 'No password to WinSCP')

Klikkaa _Advanced_-painiketta ja avaa _SSH_ > _Authentication_ -välilehti. Anna polku SSH-yksityiseen avaimeen _Private key file_ -kenttään ja valitse _OK_.

![WinSCP advanced site settings to add ssh private key](https://a3s.fi/docs-files/winscp-ssh-key-add.png 'Add SSH key to WinSCP')

Klikkaa _Login_ muodostaaksesi yhteyden. Jos yhdistät ensimmäistä kertaa, WinSCP kysyy luotatko isäntään ja pyytää SSH-avaimen salasanaa.

### Tiedostojen lataaminen CSC:n ympäristöön {#uploading-files-to-csc-environment}

Voit käyttää WinSCP:n eri toimintoja ladataksesi tiedostoja CSC:n laskentaympäristöön. Helpoimmat tavat ovat vetäminen ja pudotus hiirellä, kopioiminen ja liittäminen tai Windowsin Resurssienhallinnan _Send To_ -toiminto.

Kun käytät vetämistä ja pudotusta, valitse paikallisella koneella haluamasi tiedostot esimerkiksi Windowsin Resurssienhallinnassa. Raahaa valitut tiedostot hiirellä ja pudota ne etäpaneeliin WinSCP-käyttöliittymässä.

Kun käytät kopiointia ja liittämistä, valitse paikalliselta koneeltasi ladattavat tiedostot esimerkiksi Windowsin Resurssienhallinnassa, ja kopioi ne leikepöydälle. Siirry sen jälkeen WinSCP-ikkunaan ja valitse valikosta _File|Paste_ (tai _Ctrl+V_). Huom: jos leikepöydän sisältö on pelkkä teksti, _File|Paste_ -toiminto toimii eri tavalla avaamalla polun, joka on leikepöydällä, eikä liitä tiedostoja.

Voit käyttää Windowsin _"Send To"_ -toimintoa tiedostojen lataamiseen palvelimelle. Ota tämä ominaisuus käyttöön asennusohjelmalla tai valitse se asetuksista ("add upload short cut to Explorer's 'send to' context menu").

### Tiedostojen lataaminen CSC:n ympäristöstä {#downloading-files-from-csc-environment}

Helpoin tapa ladata tiedostoja on vetää ja pudottaa hiirellä tai käyttää URL-osoitteita. Kun käytät vetämistä ja pudotusta, valitse ensin haluamasi tiedostot WinSCP:n etäpaneelissa ja vedä ne hiirellä paikalliseen kansioon, esimerkiksi Windowsin Resurssienhallinnassa.

Voit rekisteröidä WinSCP:n käsittelemään SFTP- ja SCP-protokollan URL-osoitteita. Ota tämä ominaisuus käyttöön asennusohjelmalla tai valitse se asetuksista ("Register to handle sftp:// and scp:// addresses"). Nyt voit syöttää URL-osoitteen selaimeesi, ja WinSCP sallii tiedoston lataamisen.

![WinSCP interface](/img/Winscp2.jpg 'WinSCP interface')

### Muita WinSCP:n toimintoja {#other-winscp-operations}

WinSCP tarjoaa useita lisätoimintoja tiedostojen ja kansioiden käsittelyyn siirtojen lisäksi. Pääset niihin käsiksi napsauttamalla oikealla hiiren painikkeella mitä tahansa kohdetta käyttöliittymässä ja valitsemalla haluamasi toiminnon avautuvasta valikosta. Voit myös esimerkiksi vetää tiedoston tai kansion toiseen sijaintiin.

### Lisädokumentaatio {#further-documentation}

- [Extensive WinSCP documentation](https://winscp.net/eng/docs/start)