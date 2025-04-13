
---
search:
  boost: 0.1
---

# CSC Pikaviite {#csc-quick-reference}

Yhteyshenkilöt: @attesillanpaa @JMuff22 @joonas-somero

Tämä kansio sisältää nykyisen version "CSC Pikaviite" -dokumentista sekä vanhoja kopioita. Mukana on Word-dokumenttitiedosto sekä LaTeX-tiedosto dokumentin tuottamista varten. Vanhoja kopioita säilytetään, mutta tämä saattaa muuttua tulevaisuudessa.

## Lähdetiedosto repositoriossa {#source-file-in-repository}

LaTeX-lähdetiedosto löytyy repositoriosta, polusta _[docs/img/csc-quick-reference/](https://github.com/CSCfi/csc-user-guide/tree/master/docs/img/csc-quick-reference)_.

## LaTeX-tiedoston rakentaminen {#building-latex-file}

Yksinkertaisesti `latexmk -pdf --shell-escape "csc-quick-reference.tex"`. Latexmk toimitetaan useimpien TeX-jakelujen (TeXLive ja MiKTeX) mukana, ja se on Perl-komentosarja, joka suorittaa `pdflatex`-ohjelman tai muunkin LaTeX-jakelun oikean määrän kertoja. Tämä tekee muotoilusta paljon helpompaa. Sitä ylläpidetään tällä hetkellä osoitteessa: https://personal.psu.edu/~jcc8/software/latexmk/.

## Word-dokumentti {#word-doc}

Avaa Word-dokumentti (`.docx`) Microsoft Wordissa, muokkaa ja tallenna pdf-muodossa.
