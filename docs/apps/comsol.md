# COMSOL Multiphysics

The COMSOL Multiphysics simulation environment facilitates
all steps in the modeling process—defining your geometry, specifying
your physics, meshing, solving and then post-processing your results.

Model set up is quick, thanks to a number of predefined modeling
interfaces for applications ranging from fluid flow and heat transfer to
structural mechanics and electromagnetic analyses. Material properties,
source terms and boundary conditions can all be arbitrary functions of
the dependent variables.

[TOC]

## Available

-  Puhti: 5.4

## License
The terms of use of this software allow its use for only the affiliates (staff and students) of Finnish higher education institutions.

## Usage

The following modules are currently available:

-   Acoustics
-   AC/DC
-   CAD Import
-   CFD
-   Heat Transfer
-   Particle Tracing
-   Structural Mechanics

To start using COMSOL, login to Puhti

```bash
$ ssh -Y <cscusername>@puhti.csc.fi
```

Then
```bash
$ module load comsol 
```

and
```bash
$ comsol
```

Sometimes, you may encounter errors relating to OpenGL rendering during
the start-up. The solution is to force COMSOL to start with software
rendering using command

```bash
$ comsol -3drend sw
```

## More information

- COMSOL Multiphysics home page: [https://www.comsol.com](https://www.comsol.com)