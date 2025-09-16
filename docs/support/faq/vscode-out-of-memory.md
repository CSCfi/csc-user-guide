# Connecting to CSC supercomputers via VS Code gives out-of-memory error

Connecting to CSC supercomputers using VS Code versions 1.101 and later may
fail with error `Out of memory: Cannot allocate Wasm memory for new instance`.
There are three workarounds to avoid this issue:

1. Add to your `.bashrc` file on CSC supercomputers the line
   `export NODE_OPTIONS="--disable-wasm-trap-handler"`, or
2. increase login node virtual memory limit by adding the line
   `ulimit -v "$(ulimit -Hv)"` to your `.bashrc` file on CSC supercomputers, or
3. downgrade your VS Code version to 1.100.
