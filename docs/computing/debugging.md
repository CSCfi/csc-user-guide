# Virheenkorjaus {#debugging}

## Valmistele koodi virheenkorjausta varten {#prepare-code-for-debugging}

Jotta saadaan kaikki virheenkorjaustiedot, ohjelma täytyy yleensä kääntää uudelleen virheenkorjauslipun (`-g`) kanssa aktivoituna. Esimerkiksi GNU-kääntäjällä:

```
gcc -g -o example example.c
```

## Muistivuodot {#memory-leaks}

Hyvä paikka aloittaa, on tarkistaa muistivuodot [Valgrindilla](https://valgrind.org/). Se on monipuolinen työkalu, jota käytetään yleisimmin koodin muistivuotojen havaitsemiseen, mutta sitä voidaan käyttää myös esim. säikeitysvirheiden tai kasan ja välimuistin käytön tutkimiseen.

Jotta voit käyttää Valgrindia, aseta ympäristö tarvittavaksi koodillesi normaalisti ja käännä koodi uudelleen virheenkorjauslipun (`-g`) lisättynä.

Valgrind-analyysin suorittaminen on yksinkertaista ja sen voi tehdä joko [interaktiivisessa istunnossa](running/interactive-usage.md) tai [lähetettynä työnä](running/submitting-jobs.md). Interaktiivisessa istunnossa käytettävä komento on `valgrind ./myprogram`, kun taas lähetetyssä työssä komento on `srun valgrind ./myprogram`.

Esimerkiksi, tarkistaaksesi muistivuodot interaktiivisessa istunnossa:

```bash
module load valgrind

valgrind ./example
```

Jotta saman analyysin voi suorittaa normaalina ei-interaktiivisena työnä, esim. debuggattaessa rinnakkaisohjelmaa, käytettävä komento on `srun valgrind ./example`.

## Debuggerit {#debuggers}

Täysimittaisia debuggaustyökaluja tarvitaan usein koodin suorittamisen tarkkaan tutkimiseen ja suoritusajan virheiden ratkaisemiseen. CSC:llä on saatavilla useita debuggaustyökaluja:

* [Arm DDT](../apps/ddt.md) on debuggertyökalu sarjallisia ja rinnakkaisohjelmia (MPI, OpenMP, CUDA) varten ja siinä on sekä graafinen että komentoriviliittymä
* [GDB](../apps/gdb.md) on komentorividebuggertyökalu käännetyille ohjelmille (C, C++, Fortran, jne.)
* [PDB](../apps/pdb.md) on interaktiivinen debuggertyökalu Python-ohjelmille
* [CUDA-GDB](../apps/cuda-gdb.md) on komentorividebuggertyökalu CUDA-ohjelmille
* [compute-sanitizer](../apps/compute-san.md) on komentorivitoiminnallisuuden tarkistustyökalupaketti