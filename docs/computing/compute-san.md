# compute-sanitizer: command-line functional correctness checking suite for CUDA programs

## Available
    Puhti: 2020.2.0
    Mahti: 2020.3.1
## Usage    
[compute-sanitizer](https://docs.nvidia.com/cuda/compute-sanitizer/index.html) is a functional correctness checking suite included in the CUDA toolkit (starting from version 11). 
In order to use tool the CUDA code has to be compiled with the extra flags
`-g` and `-G`.

Next in an [interactive session](running/interactive-usage.md) one starts the
debugging by running:

```bash
compute-sanitizer  --<tool> ./cuda_program
```
`<tool>` can be of the several sub-tools available for performing different type of checks:
* `memcheck`: is capable of precisely detecting and attributing out of bounds and misaligned memory access errors in CUDA applications and it can also report hardware exceptions encountered by the GPU (default)
* `racecheck`: can report shared memory data access hazards that can cause data races.
* `initcheck`: can report cases where the GPU performs uninitialized accesses to global memory 
* `synccheck`: can report cases where the application is attempting invalid usages of synchronization primitives
