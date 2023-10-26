---
tags:
  - Free
---

# Octave

GNU Octave is a high-level interpreted language, primarily intended for numerical computations. It provides capabilities for the numerical solution of linear and nonlinear problems, and for performing other numerical experiments. It also provides extensive graphics capabilities for data visualization and manipulation. Octave is normally used through its interactive command line interface, but it can also be used to write non-interactive programs. The Octave language is quite similar to Matlab so that most programs are easily portable.

[TOC]

## Available

- Puhti: 5.1.0

## License

GNU General Public License (GPL)

## Usage

### Interactive use on Puhti

```bash
$ ssh puhti.csc.fi
$ module load octave-env
$ octave
```
Installing packages from Octave Forge for current user

```bash
> pkg install -forge -local <pkg_name>
```

Packages ['Structure Handling'](https://gnu-octave.github.io/packages/struct/) and ['Parallel Computing'](https://gnu-octave.github.io/packages/parallel/) have been installed for all users by default.

### Octave batch jobs

Example about a serial batch script job on Puhti

```bash
#!/bin/bash
#SBATCH --time=00:05:00
#SBATCH --partition=small
#SBATCH --ntasks=1
#SBATCH --account=<project>
##SBATCH --mail-type=END #uncomment to get mail

module load octave-env

srun octave my_code.m
```

Submit the script with `sbatch <script_name.sh>`

## References

In view of the many contributions made by numerous developers over many years it is common courtesy to cite Octave in publications when it has been used during the course of research or the preparation of figures. The citation function can automatically generate a recommended citation text for Octave or any of its packages. See the help text below on how to use citation.

```bash
> citation
> citation <package>
```

Above commands will display instructions for citing GNU Octave or its packages in publications. When called without an argument, display information on how to cite the core GNU Octave system. When given a package name package, display information on citing the specific named package. Note that some packages may not yet have instructions on how to cite them.

## More information

- Octave documentation [https://octave.org/doc/interpreter](https://octave.org/doc/interpreter)
