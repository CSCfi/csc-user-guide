
# Tekniset yksityiskohdat Helmistä

## Arkkitehtuuri ja Topologia {#architecture-and-topology}

Helmi on 5-kubit kvanttitietokone, jonka VTT ja IQM ovat kehittäneet yhdessä käyttäen suprajohtavia kubitteja. Kubitit on järjestetty **tähtimäiseen** topologiaan, jossa keskuskubitti Qubit 3 (QB3) on yhdistetty neljään muuhun kubittiin. Tämä tarkoittaa, että mikä tahansa kahden kubitin portti toimii QB3:n ja minkä tahansa muun kubitin välillä, kun taas yhden kubitin portit voidaan kohdistaa mihin tahansa ympäröivistä neljästä kubitista. 

<p align="center">
    <img src="../../../../img/helmi_mapping.png" alt="Helmin solmukartta">
</p>

### Alkuperäiset portit {#native-gates}

Helmin alkuperäiset portit ovat kahden kubitin ohjattu-z-portti ja yhden kubitin vaiheittainen rx-portti.

### Topologian ja porttien määrittely Qiskitissa ja Cirqissa {#defining-topology-and-gates-in-qiskit-and-cirq}

Topologia, tuetut ohjeet ja backend-spesifiset metatiedot voidaan tiedustella suoraan [Qiskitilla IQM:llä](https://iqm-finland.github.io/qiskit-on-iqm/) tai [Cirqilla IQM:llä](https://iqm-finland.github.io/cirq-on-iqm/). Esimerkiksi:

```python
# Qiskit
from iqm.qiskit_iqm import IQMProvider
provider = IQMProvider(iqm_server_url)
backend = provider.get_backend()
print(f'Native operations of the backend: {backend.operation_names}')
print(f'Coupling map of the backend: {backend.coupling_map}')
```

```python
# Cirq
from iqm.cirq_iqm import Adonis
adonis = Adonis()
print(adonis.metadata.qubit_set)
print(adonis.metadata.gateset)
print(adonis.metadata.nx_graph)
```

## Lisälukemista {#further-reading}

* [Erityiset ohjeet LUMI Helmi -osiolle](fiqci-partition.md)
* [Qiskit-sovitin IQM-laitteille](https://iqm-finland.github.io/qiskit-on-iqm/)
* [Cirq-sovitin IQM-laitteille](https://iqm-finland.github.io/cirq-on-iqm/)