---
tags:
  - Academic
catalog:
  name: ABAQUS
  description: Dassault Systemes' SIMULIA academic research suite
  description_fi: Dassault Systemesin SIMULIAn akateeminen tutkimuspaketti
  license_type: Academic
  disciplines:
    - Computational Engineering
  available_on:
    - Puhti
---

# ABAQUS { #abaqus }

Dassault Systemesin SIMULIAn akateeminen ohjelmistoportfolio tarjoaa työkaluja realistiseen simulointiin, optimointiin, kestävyystarkasteluihin, monikappalesimulointiin, laskennalliseen virtausdynamiikkaan sekä sähkömagneettiseen simulointiin. [SIMULIA Academic Research Suite](https://www.3ds.com/products-services/simulia/academia/) -lisenssit ovat saatavilla CSC:n palvelimilla. 

## Lisenssi { #license }

SIMULIA Academic Research Suite -tuotteet ovat proprietaarista ohjelmistoa. Lisenssit ovat vain akateemiseen käyttöön. Käyttörajoituksista ks. verkkosivu [SIMULIA Academic Program](https://edu.3ds.com/en/software/simulia-academic), kohta **Eligibility for Academic Licensing of SIMULIA Products**.

## Saatavuus { #available }

Lisenssit ovat saatavilla CSC:n laskenta-alustalla [Puhti](../computing/available-systems.md) vain analyysiajoja varten. Uusimmat tuotteet ovat saatavilla palvelimilla, ja aiempien versioiden asennus on myös mahdollinen. Kaikkia asennettuja versioita ylläpidetään palvelimilla.

## Käyttö { #usage }

Kirjauduttuasi palvelimelle varmista, että olet siirtänyt kaikki analyysiajoa varten tarvittavat syötetiedostot paikalliselta koneeltasi palvelimelle. Sijoita tiedostot projektisi scratch-hakemistoon. Kotihakemistoa ei ole tarkoitettu laskentaan.

Asennettujen Abaqus-versioiden selvittämiseksi anna komento

```bash
module available
```

ja tarkista rivit `abaqus/<version number>`. Esimerkiksi Abaqus-version 2024 lataamiseksi anna komento

```bash
module load abaqus/2024
```

Puhti-palvelimella on saatavilla esimerkkieräajotiedosto:

```bash
/appl/soft/eng/simulia/example_batch_job_files/parjob_puhti_abaqus
```

Kopioi tiedosto ja muokkaa se omaan käyttöösi. Lisäohjeet löytyvät tiedostosta.

## Tuki { #support }

Ongelmatilanteissa ole hyvä ja [ota yhteyttä CSC Service Deskiin](../support/contact.md).

## Lisätietoja { #more-information }

* [SIMULIA Academic Research Suite](https://www.3ds.com/products-services/simulia/academia/)