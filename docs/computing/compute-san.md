# compute-sanitizer: functional correctness checking suite for CUDA programs

## Available
    Puhti: 2022.2.0
    Mahti: 2021.3.0
## Usage    
[compute-sanitizer](https://docs.nvidia.com/cuda/compute-sanitizer/index.html) is a functional correctness checking suite included in the CUDA toolkit (starting from version 11). 
In order to use the tool, the CUDA code has to be compiled with the extra flags
`-g` and `-G`.

Debugging is started in an [interactive session](running/interactive-usage.md) 
by running:

```bash
compute-sanitizer  --tool <tool> ./cuda_program
```
where `<tool>` is one of the several sub-tools for different type of checks:

* `memcheck`: is capable of precisely detecting and attributing out of bounds and misaligned memory access errors in CUDA applications. It can also report hardware exceptions encountered by the GPU (default)

* `racecheck`: can report shared memory data access hazards that can cause data races.

* `initcheck`: can report cases where the GPU performs uninitialized accesses to global memory 

* `synccheck`: can report cases where the application is attempting invalid usages of synchronization primitives
