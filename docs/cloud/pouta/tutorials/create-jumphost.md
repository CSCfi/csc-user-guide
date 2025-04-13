
# Hyppypalvelin cPoutassa {#jumphost-in-cpouta}

## Johdanto {#introduction}
Hyppypalvelimen tarkoitus infrastruktuurissa on mahdollistaa pääsy ulkoiselta verkolta useille koneille antamatta niille julkista IP-osoitetta (kelluva IP).  
Voit konfiguroida yhden koneen julkisella IP-osoitteella ja käyttää muita koneita hyppypalvelimen kautta. Tämä ainutlaatuinen julkisen IP:n omaava kone toimii porttina sisäverkkoon.  

Tässä on kaavio:  
![hyppypalvelimen-kaavio](../../img/jumphost_schema.png)

## Kuinka luoda hyppypalvelin? {#how-to-create-a-jumphost}
Voit löytää mallin GitHub-repostamme: [jumphost CSC](https://github.com/CSCfi/openshift-jumphost-example). Lue huolellisesti repossa annetut ohjeet.  
Muista, että tarjoamme perusmallin. Voit kloonata ja muokata sen tarpeidesi mukaan.

## Selitykset {#explanations}
Kaksi lisäkansiota täytyy luoda: `files` ja `keys`.  

`files`-kansiossa sinun tulee kopioida julkinen avain, jota käytät yhteyden muodostamiseksi instansseihin. Se voi olla julkinen avain, jota käytät aina cPoutassa, tai se voi olla uusi avain. Älä unohda ladata sitä cPouta-projektiisi.  

`keys`-kansiossa sinun tulee kopioida kaikkien niiden käyttäjien julkiset avaimet, joille haluat antaa oikeuden muodostaa yhteyden eri instansseihin. Ansible etsii `keys`-kansiosta.  

Tässä on osa koodista:  
```yaml
- name: Set authorized key taken from files
  authorized_key:
    user: "ubuntu"
    state: present
    key: "{{ lookup('file', item) }}"
  with_fileglob: "keys/*"
  tags:
    - keys
```

Tämä tarkoittaa `Ubuntu`-kuvien käyttöönottoa. Jos haluat käyttää sitä `CentOS`-koneiden kanssa, älä unohda muokata tiedostoa `all.yaml` sekä `os_image` ja `user` arvoja.  

Ajaaksesi playbookin, kirjoita tämä komento:  
```sh
ansible-playbook main.yaml
```
Se kehottaa sinua syöttämään käytettävän verkon nimen.  

Katso lisätietoja GitHub-repon `README.md`-tiedostosta.