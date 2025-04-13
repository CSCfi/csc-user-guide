
# Miksi yksityinen SSH-avaimeni ei toimi Rahtissa? {#why-my-private-ssh-key-does-not-work-in-rahti}

Saatat tarvita SSH-avainparia, jos rakennat yksityisestä GitHub-repositoriosta.  
Tämä artikkeli voi auttaa sinua selvittämään, miksi avaimet eivät toimi.

Kattavan oppaan koko prosessista käyttää SSH-avaimia yksityisen repositorion kloonaamiseen Rahtissa löydät täältä: [Repository SSH Keys](https://cloud.redhat.com/blog/private-git-repositories-part-2a-repository-ssh-keys) opas.

## Yhteensopimattomat avaimet {#mismatched-keys}

On muutamia syitä, miksi SSH-avain ei toimi, yksinkertaisin on silloin, kun **yksityinen avain** ei vastaa **julkista avainta**. Tarkistaaksesi tämän, voit luoda julkisen avaimen uudestaan yksityisestä seuraavasti:

```bash
ssh-keygen -y -f private_key_file
```

Tarkista, että luotu julkinen avain vastaa käytettyä. Jotkut palvelimet myös luovat avaimen sormenjäljen, voit luoda tämän sormenjäljen joko julkisista tai yksityisistä avaimista, sormenjäljen on täsmättävä. Komento, jota käytetään, on:

```bash
$ ssh-keygen -l -f repo-openshift-builder
2048 SHA256:ijP8/1P3ZSOBrJDD2PoCWmJceKd5JwDAmzmEqsH1itk openshift-source-builder/repo (RSA)

$ ssh-keygen -l -f repo-openshift-builder.pub
2048 SHA256:ijP8/1P3ZSOBrJDD2PoCWmJceKd5JwDAmzmEqsH1itk openshift-source-builder/repo (RSA)
```

## Salasanalla suojattu avain {#passphrase-protected-key}

Toinen yleinen syy epäonnistumiseen on, kun yksityinen avain on suojattu salasanalla. Vaikka yleensä suositellaan suojaamaan yksityinen avain salasanalla, kun se tallennetaan työasemaan, Rahtilla ei ole mahdollisuutta tallentaa salasanaa ja se ei silloin pysty käyttämään avainta. Tarkistaaksesi, onko yksityinen avain suojattu salasanalla, voit käyttää yllä olevaa komentoa julkisen avaimen luomiseen. Jos avain on suojattu, komento kysyy salasanaa.

## Erinäisiä formaattivirheitä {#miscellaneous-format-errors}

SSH-avaimen formaatti on tiukka. Yksityinen SSH-avain voidaan katsoa virheelliseksi seuraavissa tapauksissa:

* Avain on koodattu DOS-formaatin rivinvaihdoilla. DOS/Windows-koneilla luodut tekstitiedostot sisältävät eri rivinvaihdot kuin Unix/Linux-käyttöjärjestelmissä luodut tiedostot. DOS käyttää rivin lopetuksena CR ja LF merkkiparia (`\r\n`), kun Unix käyttää vain rivinvaihtoa (`\n`). **Ratkaisu** on käyttää työkalua kuten `dos2unix` tai luoda avain uudelleen Linuxilla.
* Avaimen otsikko (`-----BEGIN OPENSSH PRIVATE KEY-----`) tai lopputeksti (`-----END OPENSSH PRIVATE KEY-----`) ei ole kopioitu oikein. Molemmissa päissä sekä otsikossa että lopputekstissä on oltava 5 `-` merkkiä, ja lopputekstin jälkeen on oltava rivinvaihto(end of line), eli tiedoston viimeinen merkki ei ole '-' vaan uusi rivi ('\n'). Tämä ongelma syntyy normaalisti kopiointivirheistä, kun avaimen tiedoston alku tai loppu ei ole kopioitu oikein, ja se on yleisin "formaattivirheiden" lähde.

Yleisenä ohjeena käytä `ssh-keygen -l -f <file>` tarkistaaksesi, että avaimen formaatti on oikea.
