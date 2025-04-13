
!!! varoitus "Keskitaso"
Sinun on tutustuttava Kubernetes [NetworkPolicy](https://kubernetes.io/docs/concepts/services-networking/network-policies/) API:iin.  
Tässä ohjeessa käytämme OpenShift CLI -työkalua [oc](../usage/cli.md)

# Edistyneet NetworkPoliciet {#advanced-networkpolicies}

Alla olevassa YAML-esimerkissä on `NetworkPolicy`, joka sallii yhteyden muodostamisen **aloitettuna toisesta** nimialueesta `<TOISEN NIMIALUEEN NIMI>` nykyiseen nimialueeseen:

```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: 'namespacelink'
spec:
  podSelector: {}
  policyTypes:
    - Ingress
  ingress:
    - from:
        - podSelector: {}
          namespaceSelector:
            matchLabels:
              kubernetes.io/metadata.name: <TOISEN NIMIALUEEN NIMI>
```

Tämä NetworkPolicy tulee luoda nykyisessä nimialueessa.

Sen soveltamiseksi sinun tarvitsee vain luoda tiedosto yllä olevilla sisällöillä, muista vaihtaa nimialueen arvo. Kun tiedosto on luotu:

```sh
oc create -f file.yaml
```

Voit tarkistaa, että NetworkPolicy luotiin oikein seuraavasti:

```sh
$ oc describe NetworkPolicy namespacelink
Name:         namespacelink
Namespace:    test-httpd2
Created on:   2024-01-22 11:35:41 +0200 EET
Labels:       <none>
Annotations:  <none>
Spec:
  PodSelector:     <none> (Allowing the specific traffic to all pods in this namespace)
  Allowing ingress traffic:
    To Port: <any> (traffic allowed to all ports)
    From:
      NamespaceSelector: kubernetes.io/metadata.name=test-rc
      PodSelector: <none>
  Not affecting egress traffic
  Policy Types: Ingress
```

Lisätietoja saat verkkosivultamme [Network](../networking.md) tietosivulta.