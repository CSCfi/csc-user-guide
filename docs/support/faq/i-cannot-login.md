# En voi kirjautua sisään. Mitä tehdä? {#i-cannot-login-what-to-do}

Ensimmäinen asia, kun kohtaat kirjautumisongelmia, on selvittää, mihin palveluihin voit kirjautua ja mihin et.

## Voin kirjautua MyCSC:hen mutta en siihen järjestelmään, jota haluan käyttää {#i-can-login-to-mycsc-but-not-the-system-i-want-to-use}

Jos voit kirjautua [MyCSC:hen](https://my.csc.fi), on kolme yleistä syytä, miksi kirjautumisongelmat vaikuttavat muihin palveluihin, kuten Puhtiin:

1. Yrität kirjautua Puhtiin, Mahtiin tai LUMI:iin SSH-asiakkaalla, mutta et ole määrittänyt SSH-avaimia ja/tai ladannut julkista avaintasi MyCSC:hen. Tämä on vaatimus alkaen 14. huhtikuuta 2025. Ole hyvä ja lue [ohjeet, kuinka luodaan SSH-avainpari ja lisätään julkinen avain MyCSC:hen](../../computing/connecting/ssh-keys.md). Jos ongelmat jatkuvat, [katso tämä FAQ](ssh-keys-not-working.md).
2. Palvelu, johon yrität kirjautua, on alas tai siinä on ongelmia. Katso ilmoituksia postilaatikossasi tai osoitteessa [research.csc.fi](https://research.csc.fi). Odota, kunnes huolto on suoritettu tai ongelma ratkaistu.
3. Sinulla ei ole projekteja käytössä palvelussa, johon yrität kirjautua. Tarkista MyCSC:ssä projektiesi linkitetyt palvelut. [Lisää palvelun käyttöoikeus projektiisi](../../accounts/how-to-add-service-access-for-project.md) jos sinulla on sopiva projekti, tai [luo uusi projekti](../../accounts/how-to-create-new-project.md) ja sille lisää palvelun käyttölupa.
4. Olet juuri vaihtanut salasanasi, eikä sitä ole vielä päivitetty järjestelmään, johon yrität päästä. Ole hyvä ja odota jopa tunnin ja yritä uudelleen. Liian monet epäonnistuneet yritykset estävät (tilapäisesti) IP-osoitteesi tai tilisi.

## En voi kirjautua MyCSC:hen {#i-cannot-login-to-mycsc}

Jos et voi kirjautua MyCSC:hen, on yksi ongelma, joka on yleisempi kuin muut:

1. Tilisi on lukittu. Yleisimmät syyt ovat:

* Et ole vaihtanut salasanaa vuoteen.
* Olemme lähettäneet sinulle sähköpostia, mutta se palautuu.
* Tilisi sekä oikeudet myönnettiin määräajaksi ja aika on loppunut.

Sinun täytyy [ottaa yhteyttä CSC Service Deskiin](../contact.md) saadaksesi tilisi avatuksi.

## Miksi SSH-asiakasohjelmani sanoo "Corrupted MAC on input"? {#why-is-my-ssh-client-saying-corrupted-mac-on-input}

**Windows OpenSSH -asiakasohjelmissa** on tunnettu ongelma, joissa käytetään LibreSSL-kirjastoa salaukseen. Virhe ilmenee, kun käytetään yhdistelmää, jossa on salaus `aes128-ctr` ja joko `umac-128-etm@openssh.com` tai `umac-128@openssh.com` MAC-algoritmia. Asiakasohjelma näyttää virheen `Corrupted MAC on input`.

Tässä on joitakin linkkejä asiaankuuluviin virheraportteihin:

* [https://github.com/libressl/portable/issues/603](https://github.com/libressl/portable/issues/603)
* [https://github.com/PowerShell/Win32-OpenSSH/issues/1359](https://github.com/PowerShell/Win32-OpenSSH/issues/1359)
* [https://github.com/PowerShell/Win32-OpenSSH/issues/2078](https://github.com/PowerShell/Win32-OpenSSH/issues/2078)

Jos kohtaat tämän ongelman yrittäessäsi kirjautua sisään SSH:n kautta, voit yrittää lisätä MAC-algoritmin valinnan SSH-asiakasohjelmaasi, sen sijaan että käytät automaattisesti valittuja algoritmeja. Tämä saavutetaan `-m <MAC-algoritmi>` -vaihtoehdolla. Selvittääksesi, mitä MAC-algoritmeja asiakasohjelmasi teknisesti tukee, voit suorittaa `ssh -Q mac` -komennon.

Kirjoitushetkellä "hmac-sha2-512" on sopiva vaihtoehto esimerkiksi. Tämä voi muuttua tulevaisuudessa, joten voi olla hyvä idea olla ottamatta itsestäänselvyytenä, että tämä kiertotapa toimii ikuisesti.

`-o MACS=-<algoritmit>` -vaihtoehto toimii myös. Tämä syntaksi estää annettujen algoritmien käytön. Tämä on suositeltavampi kuin `-m <MAC-algoritmi>`, koska se luottaa järjestelmän oletuksiin valitakseen sinulle sopivimman algoritmin myös tulevaisuudessa.

```bash
# (Suositeltu tapa:) Kerro SSH:lle, ettei se käytä viallisia algoritmeja:
ssh -o MACS="-umac-128-etm@openssh.com,umac-128@openssh.com" yourcscusername@mahti.csc.fi

# Tai ohita oletus MAC-algoritmi:
ssh -m hmac-sha2-512 yourcscusername@puhti.csc.fi
# Näytä, mitä MAC-algoritmeja SSH-asiakasohjelmasi tukee:
ssh -Q mac
```

Huomaa, että kaikki `*-etm` versiot on tällä kertaa kielletty CSC:n supertietokoneiden SSH-palvelimilla, koska niistä löytyi uusi tietoturvaheikkous joulukuussa 2023, nimeltään "Terrapin". Jos käytät tuettua algoritmia, palvelin ilmoittaa sinulle:

```text
Unable to negotiate with <palvelimen IP>:n portti 22: no matching MAC found.
```

Jos kohtaat tämän ongelman ja löydät toimivan ratkaisun toisen MAC-algoritmin avulla, saatat haluta lisätä rivin `ssh_config` -tiedostoosi, joka mahdollistaisi kiertotavan automaattisesti. Esimerkiksi, jos haluat kertoa SSH:lle, että `umac-128` -algoritmi tulisi hylätä, käytä alla olevan kaltaista asetusta:

```text
# Aseta tämä kotihakemistosi ssh\config-tiedostoon:

Host *
    MACs -umac-128-etm@openssh.com,umac-128@openssh.com

# Huomioi miinus merkkinä listattujen algoritmien edessä, mikä tarkoittaa,
# että nämä algoritmit tulisi poistaa hyväksyttyjen joukosta.
```

## SSH-palvelin sanoo "Unable to negotiate ... no matching MAC found" {#the-ssh-server-says-unable-to-negotiate-no-matching-mac-found}

Katso [kohta ylempänä](#why-is-my-ssh-client-saying-corrupted-mac-on-input) liittyen eri MAC-algoritmin valintaan asiakasohjelmallesi.