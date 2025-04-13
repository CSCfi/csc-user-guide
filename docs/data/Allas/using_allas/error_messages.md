
# Yleiset virheilmoitukset

Olet saavuttanut Allas-kiintiösi rajan (oletus 10 TiB) tai kohdekohtaisten enintään 500 000 objektin rajan.
```bash
Too Large Object. 
```

### HTTP-tilakoodi 409 {#http-status-code-409}

Samanniminen ämpäri on jo olemassa:
```bash
Conflict
```

### HTTP-tilakoodi 404 {#http-status-code-404}

Ämpäriä ei ole olemassa:
```bash
NoSuchBucket
```

### HTTP-tilakoodi 403 {#http-status-code-403}

Tunnistetietosi eivät oikeuta ämpärin katseluun:
```bash
AccessDenied
```

### HTTP-tilakoodi 403 {#http-status-code-403-1}

Olet saavuttanut kiintiörajan. Ota yhteyttä osoitteeseen `servicedesk@csc.fi` ja pyydä kiintiön korotusta. Ilmoita pyynnössä projektin nimi, ämpärin nimi ja tiedoston koko.
```bash
QuotaExceeded
```

### HTTP-tilakoodi 400 {#http-status-code-400}

Tiedosto on liian suuri. Katso [Swift client – Tiedostot, jotka ovat suurempia kuin 5 GB](./swift_client.md#files-larger-than-5-gb).
```bash
EntityTooLarge
```
