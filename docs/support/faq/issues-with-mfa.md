# Kuinka ratkaista ongelmia monivaiheisen tunnistautumisen (MFA) kanssa { #how-to-solve-issues-with-multi-factor-authentication-mfa }

## Virhe: "Annettu koodi on väärä tai vanhentunut. Yritä uudelleen." { #error-the-provided-code-is-wrong-or-has-been-expired-please-try-again }

Ongelman ratkaisemiseksi:

1. Varmista, että laitteesi päivämäärä- ja aika-asetukset on asetettu tilaan "Automaattinen"
   tai synkronoitu verkon kanssa. Tarkista aika puhelimesi asetuksista:
    1. **Android**: *Asetukset* :material-arrow-right: *Järjestelmä*
       :material-arrow-right: *Päivämäärä ja aika* :material-arrow-right:
       *Aseta aika automaattisesti* täytyy olla *päällä*.
    2. **iPhone**: *Asetukset* :material-arrow-right: *Yleiset*
       :material-arrow-right: *Päivämäärä ja aika* :material-arrow-right:
       *Aseta aika automaattisesti* täytyy olla *päällä*.
2. Jos edellinen vaihe ei toimi, poista puhelimestasi CSC:n MFA-salainen avain
   ja aloita aivan alusta, mukaan lukien QR-koodin skannaus (eli nollaa MFA kokonaan).
    1. [Katso ohjeet](../../accounts/mfa.md#how-to-activate-csc-mfa).