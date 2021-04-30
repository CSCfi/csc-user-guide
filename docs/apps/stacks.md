# Stacks
## Description

Stacks is a software pipeline for building loci from short-read sequences, such as those generated on the 
Illumina platform. Stacks was developed to work with restriction enzyme-based data, such as RAD-seq, for 
the purpose of building genetic maps and conducting population genomics and phylogeography.

[TOC]

## License

Free to use and open source under [GNU GPLv3](https://www.gnu.org/licenses/gpl-3.0.html).

## Available
Puhti: 2.54 

## Usage

The command line tools of the Stacks pagage are installed in Puhti. To set up the most recent stacks environment in Puhti, 
run command:
```text
module load biokit
```

After that you can launch Stacks commands like _denovo_map.pl_ . for example:
```text
denovo_map.pl  -m 3 -M 2 -n 3 -T 4 -S -b 1 -t -a 2010-11-30 -o ./stacks  -p ./samples/male.fa  -p ./samples/female.fa -r ./samples/progeny_1.fa  -r ./samples/progeny_2.fa  -r ./samples/progeny_3.fa
```
As stacks jobs can be rather heavy they should be executed as batch jobs.  The Stacks installation in Puhti is not linked to 
a stacks result database and web interface. Because of that you should use option -S ( and not options -B and -D) in 
_denovo_map.pl_ runs.

It is howerver possible to set up your own Stacks database and WWW interface to a virtual machine running in the 
cPouta cloud environment of CSC. (Link to instrctions to set up a Stacks server in cPouta can be found form the end of this page.)



Manual

*   [Stacks home page](http://catchenlab.life.illinois.edu/stacks/)
*   Setting up a stacks server in cPouta
