# Debugging

... compile with `-g` ...  # FIXME

## Arm DDT

```bash
module load ddt
```

An example interactive debug session (for a MPI program):
```bash
salloc --nodes=2 --ntasks-per-node=20 --time=00:30:00 --partition=large \
  --account=<project> ddt srun ./debug_enabled_program
```

User's Guide (puhti.csc.fi): /appl/opt/ddt/19.1.2/doc/userguide-forge.pdf
