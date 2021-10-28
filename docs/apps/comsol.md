# COMSOL Multiphysics

The COMSOL Multiphysics simulation environment facilitates
all steps in the modeling process — defining your geometry, specifying
your physics, meshing, solving and then post-processing your results.

Setting up the model up is quick, thanks to a number of predefined modeling
interfaces for applications ranging from fluid flow and heat transfer to
structural mechanics and electromagnetic analyses. Material properties,
source terms and boundary conditions can all be arbitrary functions of
the dependent variables.

## Available
 
- Puhti: 5.6, 5.5, 5.4

## License
The terms of use of this software allow it to be used only by affiliates (staff and students) of Finnish higher education institutions.

## Usage

The following modules are currently available:

-   Acoustics
-   AC/DC
-   CAD Import
-   CFD
-   Heat Transfer
-   Particle Tracing
-   Structural Mechanics

The preferred method to use COMSOL interactively is via [NoMachine](nomachine.md) client. With the client, log in to Puhti and allocate computing resources.

```bash
$ srun --ntasks=1 --time=00:10:00 --mem=1G --x11=first --pty \
  --account=<project> --partition=small --mail-type=BEGIN \
   bash
```

You have to specify the execution time and memory requirement corresponding your needs. Remember to add your billing project, too. You will get an email notification, when requested computing resources are available. After that you can start COMSOL.

```bash
$ module load comsol 
```

and
```bash
$ comsol
```

Sometimes, you may encounter errors relating to OpenGL rendering during
the launch. The solution is to force COMSOL to start with software
rendering using the command

```bash
$ comsol -3drend sw
```

## More information

- COMSOL Multiphysics home page: [https://www.comsol.com](https://www.comsol.com)
