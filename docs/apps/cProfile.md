---
tags:
  - Free
catalog:
  name: cProfile
  description: Built-in profiler for Python programs
  description_fi: Sisäänrakennettu profilointityökalu Python-ohjelmille
  license_type: Free
  disciplines:
    - Miscellaneous
  available_on:
    - Puhti
    - Mahti
---

# cProfile: Pythonin profilointityökalu { #cprofile-python-profiler }

## Saatavilla { #available }

- Mahti: Mikä tahansa Python-versio
- Puhti: Mikä tahansa Python-versio

## Lisenssi { #license }

Käyttö on mahdollista sekä akateemisiin että kaupallisiin tarkoituksiin.

## Käyttö { #usage }

[cProfile](https://docs.python.org/3.8/library/profile.html#module-cProfile)
on Python-ohjelmien sisäänrakennettu profiiloija. Profiiloijaa voi käyttää kahdella tavalla. Koodin sisällä (tai tulkista):

```
import cProfile
cProfile.run('functba(list_parameters)')
```

Nyt skriptiä voidaan ajaa kuten tavallista Python-ajoa. Tämä antaa tietoa siitä, kuinka kauan funktiokutsut kestävät ja kuinka monta kertaa funktiota kutsutaan.

Vaihtoehtoisesti cProfile voidaan myös ajaa skriptinä profiloimaan toista skriptiä:

```
python -m cProfile [-o output_file] [-s sort_order] myscript.py
```

Tulokset voidaan tulostaa tai tallentaa tiedostoon. Oletuksena ne järjestetään nimen mukaan, mutta muitakin vaihtoehtoja on saatavilla.

Tiedostoon tallennettu raportti voidaan esimerkiksi visualisoida ja tulkita graafisella työkalulla, kuten `pyprof2calltree`. Tässä esimerkki funktion profiloinnista:

```
93 function calls in 0.065 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.065    0.065 <string>:1(<module>)
        1    0.000    0.000    0.028    0.028 _numpy_fft.py:1086(irfftn)
        1    0.000    0.000    0.003    0.003 arraypad.py:102(_do_append)
        2    0.000    0.000    0.000    0.000 arraypad.py:107(_prepend_const)
        2    0.000    0.000    0.004    0.002 arraypad.py:136(_append_const)
        1    0.000    0.000    0.008    0.008 arraypad.py:964(pad)
        1    0.000    0.000    0.065    0.065 compute_correlations.py:4(compute_correlations)
        1    0.032    0.032    0.065    0.065 normxcorr2.py:33(normxcorr2)
        1    0.000    0.000    0.065    0.065 {built-in method builtins.exec}
        1    0.003    0.003    0.003    0.003 {built-in method numpy.concatenate}
        2    0.002    0.001    0.002    0.001 {built-in method numpy.copyto}
        1    0.002    0.002    0.002    0.002 {built-in method numpy.where}
        1    0.000    0.000    0.000    0.000 {built-in method numpy.zeros}
        2    0.000    0.000    0.000    0.000 {method 'astype' of 'numpy.ndarray' objects}
        2    0.003    0.002    0.003    0.002 {method 'copy' of 'numpy.ndarray' objects}
        1    0.020    0.020    0.028    0.028 {mkl_fft._pydfti.irfftn_numpy}
```

Huomaa, että profiilointi tulee suorittaa samalla tavalla kuin ajettaessa ([puhti](../computing/running/example-job-scripts-puhti.md)  tai [mahti](../computing/running/example-job-scripts-mahti.md)) eräajoa tai [interaktiivista](../computing/running/interactive-usage.md) ajoa.