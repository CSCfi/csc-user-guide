---
tags:
  - Academic
system:
  - www-puhti
---

# COMSOL Multiphysics

The COMSOL Multiphysics simulation environment facilitates
all steps in the modeling process; defining your geometry, specifying
your physics, meshing, solving and then post-processing your results.

Setting up the model up is quick, thanks to a number of predefined modeling
interfaces for applications ranging from fluid flow and heat transfer to
structural mechanics and electromagnetic analyses. Material properties,
source terms and boundary conditions can all be arbitrary functions of
the dependent variables.

## Available
 
- Puhti: 6.2, 6.1, 6.0

## License
The terms of use of this software allow it to be used only by affiliates (staff
and students) of Finnish higher education institutions.

## Usage

The following modules are currently available:

-   Acoustics
-   AC/DC
-   CAD Import
-   CFD
-   Heat Transfer
-   Particle Tracing
-   Structural Mechanics

The preferred method to use COMSOL interactively is via [the Puhti web interface
desktop application](../computing/webinterface/desktop.md). In the web interface,
select `Desktop` from the `Apps` view and specify the required resources (cores,
execution time and memory). Remember to add your billing project, too.

Wait for a while as your interactive job sits in the queue and after that you can start
COMSOL with double-clinking its icon (tick the box if you want to receive an email when your session starts).

!!! Note
    You can now also enable [interactive visualization with GPU
    acceleration](../computing/webinterface/accelerated-visualization.md) for better
    performance. In this case, select `Accelerated visualization` instead of `Desktop`
    in the Puhti web interface.

Sometimes, you may encounter errors relating to OpenGL rendering during
the launch. The solution is to force COMSOL to start with software
rendering from Desktop app `Terminal` using

```bash
module load comsol
comsol -3drend sw
```


## More information

- [COMSOL Multiphysics home page](https://www.comsol.com)
