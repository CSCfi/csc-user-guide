## COMSOL Multiphysics

### Description

The COMSOL Multiphysics<sup>®</sup> simulation environment facilitates
all steps in the modeling process—defining your geometry, specifying
your physics, meshing, solving and then post-processing your results.

Model set up is quick, thanks to a number of predefined modeling
interfaces for applications ranging from fluid flow and heat transfer to
structural mechanics and electromagnetic analyses. Material properties,
source terms and boundary conditions can all be arbitrary functions of
the dependent variables.

------------------------------------------------------------------------

### Available

##### Version on CSC's Servers

Taito: 5.4, 5.3a and 5.3

------------------------------------------------------------------------

### Usage

The recommend method to use COMSOL at CSC is via the [NoMachine] client
on taito-shell. **The terms of use of this software allow its use for
only the affiliates (staff and students) of Finnish higher education
institutions.**

After logging in to Taito, type

    module load comsol 

then

    comsol

If you want to use an older version, for example 5.2a, then type

    module load comsol/53a

Sometimes, you may encounter errors relating to OpenGL rendering during
the start-up. The solution is to force COMSOL to start with software
rendering using command

    comsol -3drend sw

#### More information

The following modules are available:

-   Acoustics
-   AC/DC
-   CAD Import
-   CFD
-   Heat Transfer
-   Structural Mechanics

------------------------------------------------------------------------

### Discipline

Computational Engineering  
Other  

------------------------------------------------------------------------

### References

------------------------------------------------------------------------

### Support

servicedesk@csc.fi

------------------------------------------------------------------------

### Manual

------------------------------------------------------------------------

  [NoMachine]: https://research.csc.fi/-/nomachine
