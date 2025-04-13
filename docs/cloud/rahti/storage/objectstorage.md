
# Allas-tallennus Rahtissa

Lisätietoja [Allaksesta](../../../data/Allas/index.md)

## Varmuuskopiointi Allakseen {#backup-to-allas}

On olemassa erilaisia tapoja varmuuskopioida Allakseen Rahtista. Näytämme teille kaksi esimerkkiä:
  - Ensimmäinen tapa on käyttää toista podia kopioimaan pysyvän volyymin sisältö Allakseen.
  - Toinen esimerkki on bash-skripti, joka sinun on suoritettava paikalliselta koneeltasi.

Tässä ensimmäisessä esimerkissä lisäämme `nginx`-jakelun, joka toimii `PersistentVolumeClaim`-hakulausekkeella. Tarjoamme tiedostot testitarkoituksia varten.

### NGINX-jakelun valmistelu {#preparing-a-nginx-deployment}

Ensiksi, tutoriaaliamme varten rakennamme ja julkaisemme NGINX-palvelimen.

Rakennamme [nginx-kuvamme](../images/creating.md) tällä Dockerfile-tiedostolla: (koska ei ole mahdollista käyttää tavallista `nginx`-kuvaa OpenShiftissa)

```Dockerfile
FROM nginx:stable

ENV LISTEN_PORT=8080

# tukee käyttöoikeutta juuriryhmään kuuluvana satunnaiskäyttäjänä
RUN chmod g+rwx /var/cache/nginx /var/run /var/log/nginx

# käyttäjien ei ole sallittua kuunnella etuoikeutetuilla porteilla
RUN sed -i.bak "s/listen\(.*\)80;/listen ${LISTEN_PORT};/" /etc/nginx/conf.d/default.conf

# kommentoi käyttäjädirektiivi, koska master-prosessi toimii käyttäjänä OpenShiftissa
RUN sed -i.bak 's/^user/#user/' /etc/nginx/nginx.conf

EXPOSE 8080
```

Jos rakennat kuvasi paikallisesti, älä unohda [puskemista](../../rahti/images/Using_Rahti_integrated_registry.md) projektiisi.
Voit julkaista tämän `nginx`-palvelimen tällä Jakelulla:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx
  labels:
    name: nginx
spec:
  replicas: 1
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: <our_custom_nginx_image>
        resources:
          limits:
            memory: "128Mi"
            cpu: "500m"
        ports:
          - containerPort: 8080
        volumeMounts:
        - name: myvol
          mountPath: /mnt
      volumes:
      - name: myvol
        persistentVolumeClaim:
          claimName: nginx-pvc

---
apiVersion: v1
kind: Service
metadata:
  name: nginx-svc
spec:
  selector:
    app: nginx
  ports:
  - port: 8080

---
apiVersion: route.openshift.io/v1
kind: Route
metadata:
  name: nginx-route
spec:
  host: ""
  path: /
  to:
    kind: Service
    name: nginx-svc
  tls:
    insecureEdgeTerminationPolicy: Redirect
    termination: edge

---
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: nginx-pvc
spec:
  resources:
    requests:
      storage: 1Gi
  accessModes:
    - ReadWriteOnce
  storageClassName: standard-csi
```

Tallenna tiedosto ja käytä tätä komentoa: `oc apply -f {name_of_yaml_file}`
Jakelussa käytetään esimerkissä `PersistentVolumeClaimia`.

Nyt kun meillä on toimiva `nginx`-pod, haluamme kopioida PVC:n sisällön Allakseen. Käytämme uutta jakelua `rclone` Docker-kuvan kanssa.

### Ensimmäinen esimerkki: toisen podin käyttö {#first-example-using-another-pod}

Luo `rclone.conf` omalla `access_key_id` ja `secret_access_key`.

Jos sinulla ei ole `access_key_id` ja `secret_access_key`, sinun täytyy käyttää Pouta-projektiasi ja sitten käyttää tätä komentoa luodaksesi tunnistetiedot:

```sh
openstack ec2 credentials create
```

Kun olet luonut, luo `rclone.conf` tiedosto:

```ini
[default]
type = s3
provider = Other
env_auth = false
access_key_id = {ACCESS_KEY_ID}
secret_access_key = {SECRET_ACCESS_KEY}
endpoint = a3s.fi
acl = private
```

_Vaihda `{ACCESS_KEY_ID}` ja `{SECRET_ACCESS_KEY}` omiin tietoihisi._

Luo `rclone.sh` skripti:

```sh
#!/bin/sh -e

rclone copy "/mnt/" "default:{BUCKET}"

echo "Valmis!"
```

_Vaihda `{BUCKET}` haluamaasi kohdeämpäriin, johon haluat varmuuskopioida tiedostosi._

Sitten, sinun on luotava oma mukautettu `rclone`-Docker-kuva:

```Dockerfile
FROM rclone/rclone

COPY rclone.conf /.rclone.conf
COPY rclone.sh /usr/local/bin/
RUN chmod 755 /.rclone.conf
RUN chmod +x /usr/local/bin/rclone.sh
```
Jos luot kuvasi paikallisesti, älä unohda [puskemista](../../rahti/images/Using_Rahti_integrated_registry.md) projektiisi.

Kun kaikki on tehty, voit julkaista `rclone`-podisi.
Voit käyttää tätä esimerkkiä:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: rclone
spec:
  containers:
  - name: copys3
    image: <your_rclone_image>
    command: ["/usr/local/bin/rclone.sh"]
    resources:
      limits:
        memory: "128Mi"
        cpu: "500m"
    volumeMounts:
    - name: vol-to-backup
      mountPath: /mnt/
  volumes:
  - name: vol-to-backup
    persistentVolumeClaim:
      claimName: nginx-pvc # Täytyy vastata sitä PVC-nimeä, jonka haluat varmuuskopioida
```

Tallenna tiedosto ja käytä tätä komentoa: `oc apply -f {name_of_yaml_file}`.

!!! Varoitus
    Jos `PersistentVolumeClaim` on `ReadWriteOnce`, sinun on vähennettävä `nginx`-jakelun skaalaa, jotta rclone voipodi voi kiinnittää volyymin.
    Käytä tätä komentoa: `oc scale --replicas=0 deploy/nginx`
    Jos `PersistentVolumeClaim` on `ReadWriteMany`, sinun ei tarvitse pienentää jakeluasi.
    Voit tarkistaa tämän komennolla: `oc get pvc`. Näet joko `RWO` tai `RWX`.

Pod ajaa ja varmuuskopioi PVC:n sisältöä Allakseen. Älä unohda skaalata alkuperäistä jakeluasi (`oc scale --replicas=1 deploy/nginx`) kopioinnin jälkeen.

Tässä ratkaisussa on FOR ja VASTA-argumentteja:  
Etuja:

  - Pod toimii Rahti-projektissasi

Haittoja:

  - PVC on `ReadWriteOnce`, joten käyttökatko on välttämätön.

### Toinen esimerkki: bash-skriptin käyttäminen {#second-example-using-bash-script}

Seuraavan skriptin toimimiseksi oletamme, että sinulla on asennettuna `rclone` komentoriviohjelma ja Allas-ämpäri on luotu. `rclone.conf` pitäisi olla määritetty paikallisessa järjestelmässäsi, kuten yllä kuvatussa esimerkissä. Esimerkiksi `rclone.conf`-reitti voisi olla `~/.config/rclone/rclone.conf`. Lisätietoja Allas-ämpärin luomisesta löytyy [täältä](../../../data/Allas/using_allas/rclone.md). Tämä skripti varmuuskopioi Rahtissa olevan sovelluksen. Sovelluksella on esimerkiksi nimi `/backup`, kuten `volumeMounts` `mountPath`.

```bash
#!/bin/env bash

# Aseta podin nimi, lähdehakemisto ja kohdehakemisto
if [[ -z $1 ]];
then
    echo "Podin nimeä ei annettu parametrina."
    exit 22
else
     echo "POD_NAME = $1 on asetettu."
fi

POD_NAME=$1
SOURCE_DIR="/backup"
TIMESTAMP=$(date '+%Y%m%d%H%M%S') # Generoi aikaleima
DEST_DIR="/tmp/pvc_backup_$TIMESTAMP.tar.gz" # Sisällytä aikaleima tiedostonimeen
RCLONE_CONFIG_PATH="your/path/to/rclone.conf"
S3_BUCKET="pvc-test-allas" # Ämpärin nimi

# Kaiku funktio näyttämään tehtäväviestejä
echo_task() {
  echo "$(date '+%Y-%m-%d %H:%M:%S') - $1"
}

# Funktio virheiden käsittelyyn
handle_error() {
  echo_task "Virhe: $1"
  exit 1
}

# Tarkista, onko pod olemassa
oc get pod "$POD_NAME" &>/dev/null
if [ $? -ne 0 ]; then
  echo_task "Podia $POD_NAME ei löytynyt. Varmuuskopiointi keskeytetään."
  exit 1
fi

# Luo tar-arkisto podin sisällä
echo_task "Luodaan tar-arkisto podin sisällä..."
oc exec "$POD_NAME" -- /bin/sh -c "tar -czf /tmp/pvc_backup.tar.gz -C $SOURCE_DIR ."
if [ $? -ne 0 ]; then
  handle_error "Tar-arkiston luominen epäonnistui podissa. Varmuuskopiointi keskeytetään."
fi

# Kopioi tar-arkisto paikalliselle koneelle
echo_task "Kopioidaan tar-arkisto paikalliselle koneelle..."
oc cp "$POD_NAME:/tmp/pvc_backup.tar.gz" "$DEST_DIR"
if [ $? -ne 0 ]; then
  handle_error "Tar-arkiston kopioiminen paikalliselle koneelle epäonnistui. Varmuuskopiointi keskeytetään."
fi
echo_task "Varmuuskopiointi onnistui. Arkisto tallennettiin osoitteeseen $DEST_DIR."

# Käytä Rclone-ohjelmaa synkronoimaan tar-arkisto S3:een
echo_task "Synkronoidaan tar-arkisto S3:een..."
rclone --config "$RCLONE_CONFIG_PATH" sync "$DEST_DIR" default:"$S3_BUCKET"
if [ $? -ne 0 ]; then
  handle_error "Tar-arkiston lataaminen S3:een epäonnistui"
fi
echo_task "Varmuuskopiointi onnistui. Arkisto tallennettiin osoitteeseen $S3_BUCKET$DEST_DIR"

exit 0
```

Jos haluat poistaa tar-arkistotiedostot, voit lisätä seuraavan skriptin Allakseen tallentamisen jälkeen.

```bash
# Poista tar-arkisto podista
oc exec "$POD_NAME" -- /bin/sh -c "rm /tmp/pvc_backup.tar.gz"

# Poista väliaikaiset tiedostot
rm -rf /tmp/pvc_backup*
or
rm "$DEST_DIR"
```
Skriptiä voidaan käyttää seuraavasti, olettaen että skriptin nimi on `push_to_allas.sh` ja se on suoritettavissa:

```bash
./push_to_allas.sh "mypod-vol"
```

Tässä ratkaisussa on FOR ja VASTA-argumentteja:

Etuja:

  - Yksinkertaisuus: Juuri käsittele volyymia kuten mitä tahansa muuta hakemistoa. On suoraviivaista kopioida tiedot hakemistosta Allakseen.
  - Joustavuus: Voit valita erityisiä tiedostoja tai hakemistoja kiinnityksestä kopioitavaksi Allakseen ja se on ihanteellinen pienikokoisille tiedostoille.

Haittoja:

  - Suorituskyky: Tämä menetelmä voi olla hitaampi, erityisesti jos volyymilla on suuri määrä tiedostoja.

!!! Varoitus "Tallennustilan suorituskyky"
    On useita seikkoja, jotka on otettava huomioon Allaksen käytössä suorituskyvyn suhteen:

    - Pienet I/O-operaatiot heikentävät tallennustilan suorituskykyä. Samansuuruinen iso tiedosto on nopeampi kuin joukko pieniä tiedostoja. Ratkaisu saattaa olla kerätä pienet tiedostot yhteen arkistoon, kuten `tar`-tiedostoon.
    - Koska tallennusallas on jaettu, viive voi vaihdella. Jaettu laitteisto tarkoittaa, että suorituskyvyn jakavat eri käyttäjät.
    - Yksisäikeinen I/O on hidas, on suositeltavaa käyttää monisäikeistä I/O:ta kun mahdollista.

