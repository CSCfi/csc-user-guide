---
tags:
  - Free
---

# PLUMED

PLUMED (PLUgin for MolEcular Dynamics) is an open-source, community-developed
library that provides a wide  range of different methods for enhanced sampling
in molecular dynamics. It can be used with several MD codes.

[TOC]

## Available

-   Puhti: 2.7.4, 2.8.0
-   Mahti: 2.6.3, 2.7.2

## License

The PLUMED license (L-GPL) also allows it to be interfaced with proprietary software.

## Usage

The standalone module of PLUMED is for building your own applications and linking with
PLUMED, or analysing results performed with such code. To use, first give `module spider`
to locate all versions and their library dependencies:

```bash
module spider plumed
module load <dependencies reported by the spider command> plumed/<version>
```

If you want to run molecular dynamics with PLUMED, either compile your MD engine of
choice with PLUMED (see [selection e.g. here](https://www.plumed.org/)), or use e.g.
[GROMACS](gromacs.md), which is available at CSC.

## References

Cite your work with PLUMED with:

```text
This work was carried out using the open-source, community-developed PLUMED library 
[1], version 2.x [2] (or alternatively version 1.x [3]).
```

[1] The PLUMED consortium. _Promoting transparency and reproducibility in enhanced
molecular simulations_, [Nat. Methods 16, 670 (2019)](https://doi.org/10.1038/s41592-019-0506-8)

[2] G.A. Tribello, M. Bonomi, D. Branduardi, C. Camilloni, G. Bussi. _PLUMED2: New
feathers for an old bird_, [Comp. Phys. Comm. 185, 604 (2014)](http://doi.org/10.1016/j.cpc.2013.09.018),
preprint available as [arXiv:1310.0980](https://arxiv.org/abs/1310.0980)

[3] M. Bonomi, D. Branduardi, G. Bussi, C. Camilloni, D. Provasi, P. Raiteri,
D. Donadio, F. Marinelli, F. Pietrucci, R.A. Broglia and M. Parrinello. _PLUMED:
a portable plugin for free energy calculations with molecular dynamics_, [Comp.
Phys. Comm. 180, 1961 (2009)](http://doi.org/10.1016/j.cpc.2009.05.011),
preprint available as [arXiv:0902.0874](http://arxiv.org/abs/0902.0874)

## More information

-   [PLUMED home page](https://www.plumed.org)
-   [PLUMED tutorials (v2.8)](https://www.plumed.org/doc-v2.8/user-doc/html/tutorials.html)
