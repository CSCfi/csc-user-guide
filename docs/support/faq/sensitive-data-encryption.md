# Salaus

## Miksi minun on salattava tietoni? {#why-do-i-need-to-encrypt-my-data}
GDPR:n mukaan rekisterinpitäjän ja henkilötietojen käsittelijän on toteutettava asianmukaiset tekniset ja organisatoriset toimenpiteet varmistaakseen riskin mukaisen tietoturvatason. Salaus on yksi vaadituista tietoturvatoimenpiteistä, jotka suojaavat arkaluonteisia tietoja. Katso: [Asiakaspuolen salauksen parhaat käytännöt](https://research.csc.fi/best-practices-for-client-side-encryption). SD Connect tarjoaa automaattisen datan salauksen ja purkamisen verkkokäyttöliittymän tai ohjelmallisen rajapinnan kautta.

## Pitääkö arkaluonteiset tiedot aina salata latauksen tai tiedonsiirron aikana (esim. SSH-yhteyttä käytettäessä)? {#do-sensitive-data-always-need-to-be-encrypted-during-upload-or-data-transfer-eg-using-an-ssh-connection}
Kyllä. CSC:n [Yleisten käyttöehtojen](https://research.csc.fi/general-terms-of-use) mukaan arkaluonteiset tiedot on salattava, kun ne tallennetaan CSC:n palveluihin tai siirretään CSC:lle. Tästä syystä tiedot on salattava, jos esimerkiksi käytät SSH-yhteyttä tietojen siirtoon.

## Mitä tiedostoformaatteja voi salata SD Connectilla? {#what-data-formats-can-be-encrypted-using-sd-connect}
Voit salata tietoja missä tahansa formaatissa (esim. video, kuvat, tekstitiedostot jne.).

## Mikä uusi tiedostopääte lisätään tiedostoihini SD Connectin avulla tehdyssä latauksessa? {#what-is-the-new-extension-added-to-my-files-after-upload-with-sd-connect}
Kun salaus SD Connectilla on onnistunut, tiedostopääte on .c4gh. Pääte poistetaan, kun tiedosto puretaan.

## Sallivatko CSC:n arkaluonteisten tietojen palvelut asiakkaiden omien salausavainten käytön? {#do-csc-sensitive-data-services-allow-the-use-of-customers-encryption-keys}
Kyllä. Voit salata tiedot useilla salausavaimilla. Otathan meihin yhteyttä osoitteeseen servicedesk@csc.fi (Aihe: Arkaluonteiset tiedot) saadaksesi tukea.