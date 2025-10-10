!!! warning "Keskitaso"
    Kubernetes-ympäristön ja websovelluspalvelimien toiminnan tuntemus vaaditaan. On myös hyödyllistä tietää, miten todennus toimii. Tämä opas käyttää OpenShiftin CLI-työkalua [oc](../usage/cli.md)

# Kuinka ottaa OAuth2 Proxy käyttöön Rahtissa { #how-to-deploy-oauth2-proxy-in-rahti }

Selitämme, miten [OAuth2 Proxy](https://oauth2-proxy.github.io/oauth2-proxy/) otetaan käyttöön ja miten sitä käytetään todennuksen hallintaan käyttäen tarjoajia kuten Google, GitHub ja muut.

Tässä oppaassa käytämme esimerkkinä GitHubia.

!!! warning
    Tämä on yksinkertainen konseptitodiste. Luonnollisesti sovelluksesi tulisi pystyä rajaamaan pääsyä esimerkiksi ryhmien, sähköpostin, käyttäjätunnuksen jne. perusteella.

## Ota web-sovelluksesi käyttöön { #deploy-your-web-application }

Ensin otamme käyttöön hyvin yksinkertaisen web-sovelluksen, tämän [Flask-demon](https://github.com/CSCfi/rahti-flask-hello). Seuraa ohjeita GitHub-repossa.

Älä luo Routea; sitä ei tarvita, koska käytämme `NGINX`:ää käänteisenä välityspalvelimena.

## Ota NGINX käyttöön { #deploy-nginx }

Voit käyttää meidän [NGINX-kuvaamme](https://github.com/CSCfi/nginx-okd) ajaaksesi NGINX:ää Rahtissa (OpenShift 4).

Rahtissa voit rakentaa kuvan suoraan. Lisätietoja [täällä](../images/creating.md#using-the-source-to-image-mechanism)

Aja tämä komento:

```sh
oc new-app https://github.com/CSCfi/nginx-okd
```

Kun build on valmis, suorita tämä komento Routea varten:

```sh
oc create route edge flask-demo --service=nginx-okd --hostname=demo-oauth2.2.rahtiapp.fi --insecure-policy='Redirect' --port=8081
```

!!! info
    Voit määrittää oman `--hostname`-arvosi. Tässä esimerkissä käytämme Rahtin oletusdomainia `2.rahtiapp.fi`.

    Voit käyttää myös omaa domainiasi, mutta siinä tapauksessa sinun täytyy luoda `Ingress`.
    Lisätietoja [täällä](https://kubernetes.io/docs/concepts/services-networking/ingress/)

Meidän täytyy luoda erityinen konfiguraatio, jotta NGINX toimii käänteisenä välityspalvelimena. Tätä varten käytämme [ConfigMapia](../concepts.md#configmap)

Luo uusi tiedosto `configmap.yaml`:

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: nginx-default
data:
  default.conf: |
    server {
      listen 8081; # NGINX service port
      server_name demo-oauth2.2.rahtiapp.fi; # The same as the --hostname created previously in the Route
    
    location /oauth2/ {
      proxy_pass       http://oauth2-proxy:4180;
      proxy_set_header Host                    $host;
      proxy_set_header X-Real-IP               $remote_addr;
      proxy_set_header X-Auth-Request-Redirect $request_uri;
      # or, if you are handling multiple domains:
      # proxy_set_header X-Auth-Request-Redirect $scheme://$host$request_uri;
    }
    
    location = /oauth2/auth {
      proxy_pass       http://oauth2-proxy:4180;
      proxy_set_header Host             $host;
      proxy_set_header X-Real-IP        $remote_addr;
      proxy_set_header X-Forwarded-Uri  $request_uri;
      # nginx auth_request includes headers but not body
      proxy_set_header Content-Length   "";
      proxy_pass_request_body           off;
    }
    
    location / {
      root   /usr/share/nginx/html;
      index  index.html index.htm;
      auth_request /oauth2/auth;
      error_page 401 =403 /oauth2/sign_in;
    
      # pass information via X-User and X-Email headers to backend,
      # requires running with --set-xauthrequest flag
      auth_request_set $user   $upstream_http_x_auth_request_user;
      auth_request_set $email  $upstream_http_x_auth_request_email;
      proxy_set_header X-User  $user;
      proxy_set_header X-Email $email;
      proxy_set_header Host $http_host;
    
      # if you enabled --pass-access-token, this will pass the token to the backend
      auth_request_set $token  $upstream_http_x_auth_request_access_token;
      proxy_set_header X-Access-Token $token;
    
      # if you enabled --cookie-refresh, this is needed for it to work with auth_request
      auth_request_set $auth_cookie $upstream_http_set_cookie;
      add_header Set-Cookie $auth_cookie;
    
      # When using the --set-authorization-header flag, some provider's cookies can exceed the 4kb
      # limit and so the OAuth2 Proxy splits these into multiple parts.
      # Nginx normally only copies the first `Set-Cookie` header from the auth_request to the response,
      # so if your cookies are larger than 4kb, you will need to extract additional cookies manually.
      auth_request_set $auth_cookie_name_upstream_1 $upstream_cookie_auth_cookie_name_1;
    
      # Extract the Cookie attributes from the first Set-Cookie header and append them
      # to the second part ($upstream_cookie_* variables only contain the raw cookie content)
      if ($auth_cookie ~* "(; .*)") {
          set $auth_cookie_name_0 $auth_cookie;
          set $auth_cookie_name_1 "auth_cookie_name_1=$auth_cookie_name_upstream_1$1";
      }
    
      # Send both Set-Cookie headers now if there was a second part
      if ($auth_cookie_name_upstream_1) {
          add_header Set-Cookie $auth_cookie_name_0;
          add_header Set-Cookie $auth_cookie_name_1;
      }
    
      proxy_pass http://course-flask-demo:8080/; # Set your backend, where you should be redirected. Here, our flask-demo webapp. It is the service name and its port.
    # or "root /path/to/site;" or "fastcgi_pass ..." etc
    }
    
      error_page   500 502 503 504  /50x.html;
      location = /50x.html {
        root   /usr/share/nginx/html;
      }
    }
```

Lisätietoja tästä konfiguraatiosta löytyy [OAuth2 Proxyn sivustolta](https://oauth2-proxy.github.io/oauth2-proxy/configuration/integration)

Tärkeimmät tässä ConfigMapissa muokattavat arvot ovat:

- `listen 8081`: Edustaa NGINX-palvelun porttia
- `server_name`: Sama kuin aiemmin Routessa luotu `--hostname`
- `proxy_pass`: Aseta taustapalvelu, johon käyttäjän tulisi ohjautua. Tässä tapauksessa Flask-demo-webappimme; kyseessä on palvelun nimi ja sen portti.

Ota ConfigMap-konfiguraatio käyttöön:

```sh
oc apply -f configmap.yaml
```

## Luo GitHub OAuth -sovelluksesi { #create-your-github-oauth-apps }

Siirry [GitHubiin](https://github.com/settings/developers) > OAuth Apps

Klikkaa New OAuth App

![Uusi GitHub OAuth -sovellus](../../img/GitHub-new-oauth-app.png)

Täytä kentät:

- Application Name: Anna nimi GitHub OAuth -sovelluksellesi
- Homepage URL: Web-sovelluksesi kotisivu. Tässä esimerkissä se on NGINX-käänteisen välityspalvelimen reitti (`https://demo-oauth2.2.rahtiapp.fi`)
- Authorization callback URL: Sovelluksesi callback-osoite. Tässä esimerkissä se on muotoa `https://demo-oauth2.2.rahtiapp.fi/oauth2/callback`

## Ota OAuth2 Proxy käyttöön { #deploy-oauth2-proxy }

OAuth2 Proxyn käyttöönottoon käytämme .yaml-tiedostoa. Luo uusi tiedosto nimeltä `oauth2.yaml` ja kopioi seuraava:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  labels:
    k8s-app: oauth2-proxy
  name: oauth2-proxy
spec:
  replicas: 1
  selector:
    matchLabels:
      k8s-app: oauth2-proxy
  template:
    metadata:
      labels:
        k8s-app: oauth2-proxy
    spec:
      containers:
      - args:
        - --provider=github
        - --client-id=<CLIENT_ID_FROM_GITHUB>
        - --client-secret=<CLIENT_SECRET_FROM_GITHUB>
        - --redirect-url=https://demo-oauth2.2.rahtiapp.fi/oauth2/callback
        - --email-domain=*
        - --reverse-proxy=true
        - --upstream=static://200
        - --http-address=0.0.0.0:4180
        - --set-authorization-header=true
        - --set-xauthrequest=true
        - --pass-access-token=true
        - --pass-authorization-header=true
        - --pass-user-headers=true
        - --pass-host-header=true
        - --cookie-secret=<YOUR_COOKIE_SECRET>
        image: quay.io/oauth2-proxy/oauth2-proxy:latest
        imagePullPolicy: Always
        name: oauth2-proxy
        ports:
        - containerPort: 4180
          protocol: TCP
        resources: {}

---

apiVersion: v1
kind: Service
metadata:
  labels:
    k8s-app: oauth2-proxy
  name: oauth2-proxy
spec:
  ports:
  - name: http
    port: 4180
    protocol: TCP
    targetPort: 4180
  selector:
    k8s-app: oauth2-proxy
```

Tärkeimmät asiat ovat:

- `--provider=github`
- `--client-id=` Kopioi aiemmin luomastasi GitHub OAuth -sovelluksesta
- `--client-secret=` Kopioi aiemmin luomastasi GitHub OAuth -sovelluksesta
- `--cookied-secret=` Voit luoda sen ajamalla tämän komennon: `docker run -ti --rm python:3-alpine python -c 'import secrets,base64; print(base64.b64encode(base64.b64encode(secrets.token_bytes(16))));'`

Kun olet valmis, ota konfiguraatio käyttöön:

```sh
oc apply -f oauth2.yaml
```

## Melkein valmista { #almost-done }

Nyt meillä on:

1. Sovelluksemme
2. NGINX käänteisenä välityspalvelimena
3. GitHub OAuth -sovelluksemme
4. OAuth2 Proxy otettuna käyttöön

Meidän täytyy määrittää NGINX kommunikoimaan OAuth2 Proxyn kanssa, joka ottaa yhteyden GitHubiin ja päästää meidät web-sovellukseen.

Tässä on kaavio:

![OAuth2-kaavio](../../img/oauth2.png)

Muistatko, että loimme aiemmin ConfigMapin? Mikä sen tarkoitus on? Siitä tulee NGINX:n uusi oletuskonfiguraatiotiedosto.

Luo tiedosto `patch-configmap.yaml`:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-okd
spec:
  template:
    spec:
      containers:
        - name: nginx-okd
          volumeMounts:
            - mountPath: /etc/nginx/conf.d/
              name: nginx-default
      volumes:
        - configMap:
            name: nginx-default
            defaultMode: 420
          name: nginx-default
```

Päivitä deployment:

```sh
oc patch deploy/nginx-okd --patch-file=patch-configmap.yaml
```

Tämä käynnistää automaattisesti uuden NGINX-podin käyttöönoton.

Kun podi on valmis, voit kokeilla uutta konfiguraatiotasi. Avaa web-sovelluksesi sivusto (sen pitäisi olla NGINX:ää käyttöönotettaessa luotu Route, joten tässä esimerkissä https://demo-oauth2.2.rahtiapp.fi).

Sinun pitäisi nähdä OAuth2 Proxyn aloitussivu ja painike **Sign in with GitHub**.

![OAuth2 Proxy -aloitussivu](../../img/oauth2-proxy-homepage.png)

Jatka.

Kun olet vahvistanut tunnistetietosi ja antanut GitHubille luvan käyttää tietojasi, sinut pitäisi ohjata web-sovellukseen:

![Flask-kotisivu](../../img/flask-demo-homepage.png)

# Muutamia huomioita { #few-comments }

Onnittelut! Onnistuit ottamaan käyttöön OAuth2 Proxyn sivustollesi pääsyä varten.

Pidä mielessä, että tämä esimerkki ei rajoita nimen, käyttäjätunnuksen tai sähköpostin perusteella. Hyvän sovelluksen tulee esimerkiksi pystyä tarkistamaan sähköpostiosoite ja päästämään käyttäjän sovelluksiin tai estämään pääsyn.

Tässä esimerkki OAuth2 Proxysta ja Kubernetes-Dashboardista: <https://kubernetes.github.io/ingress-nginx/examples/auth/oauth-external-auth/#example-oauth2-proxy-kubernetes-dashboard>

Tässä esimerkissä klusteriin voidaan antaa pääsy hallitsemalla käyttäjän sähköpostia [Kubernetesin RBACin](https://kubernetes.io/docs/reference/access-authn-authz/rbac/) avulla.