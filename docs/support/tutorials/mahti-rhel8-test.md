# Mahti RHEL8 test system documentation

## RHEL8 login nodes

!!! Note
    These test system nodes share the same filesystem on
    `/projappl`, `/scratch` and `/users`. So all settings that you
    have in your normal login scripts and environment are visible and
    active on RHEL8 nodes too. Please make sure that you clean your
    `.bashrc` and other relevant files before logging in.

!!! Note
    Lmod caches module information into your home folder under
    `~/.lmod.d/.cache` and may give you wrong listing of modules when
    working on both RHEL7 and RHEL8 nodes. Please use `--ignore-cache`
    option on module commands or clean the cache folder when
    necessary.

## CPU and GPU nodes with RHEL8
