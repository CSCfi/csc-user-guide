
!!! success "Perustaso"
Sinulla tulee olla OpenShift CLI -työkalun [oc](../usage/cli.md) ja Kubernetesin [huomautusten](https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/) tietämys.

# Huomautukset {#annotations}

Voit käyttää Kubernetes-huomautuksia liittääksesi mielivaltaista, ei-tunnistettavaa metadataa objekteihin. Asiakkaat, kuten työkalut ja kirjastot, voivat noutaa tätä metadataa. Huomautukset, kuten etiketit, ovat avain/arvo-karttoja.

Huomautuksia voidaan lisätä mihin tahansa objektiin yksinkertaisesti seuraavasti:

```
oc annotate <object_type> <object_name> <key>=<value>
```

Tässä on joitakin esimerkkejä, joissa käytetään huomautuksia:

* [Suojautuminen DDoS-hyökkäyksiltä](../../../support/faq/DDos.md)
* [Reitti huomautukset](../concepts.md#route)
* [Mukautetut verkkotunnukset ja turvallinen siirto](custom-domain.md)