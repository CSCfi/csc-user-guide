# csc-env

`csc-env` is a command line tool for testing for common issues in the programming environment,
and resetting the login- and ssh-settings on CSC supercomputers.

The tool does the reset in a non-destructive manner by saving a copy of the current settings which 
can then be later restored.  

- **login-settings** -> The following files: `.bashrs`, `.bash_profile` and `.bash_logout` in the users home directory
- **ssh-settings** -> The `.ssh ` folder in the users home directory

Incorrect or extra variables in the login-settings are a common cause for strange and hard to track down issues.
CSC support staff also can't see a users login-settings, so catching issues here is difficult unless the user 
sends us their login-settings. 
Temporarily resetting the login-settings to system default allows us to rule out one possible cause.   

!!!Note "Only bash support at the moment"
    If you are using some other login shell (ksh, zsh ...) the tool can not reset your login-settings,
    you can use the tool to switch to bash.

Errors or missing keys in the ssh-settings can stop the user from connecting to CSC supercomputers using ssh-keys
or connecting to the compute nodes. Resetting the ssh-settings can sometimes fix these issues.  

!!!Note "Remeber your password"
    Resetting the ssh-settings will disable key-based login, so make sure you remember your password
    so that your are still able to login.


## Usage


## Help 

`csc-env help` will show the available commands and options.

### Test

`csc-env test` will check for common issues in the user environment by comparing 
them to the default settings. The test result can be included in your support request to the servicedesk. 
Below is an example test output: 

```
Info
---------------------
User: csc_user
Host: puhti-login1
Home: /users/csc_user
Home quota
    capacity: 23%
    files:    15%
Default shell: /bin/bash 



Environment test
---------------------
PATH has default value OK
LD_LIBRARY_PATH has default value OK
LD_PRELOAD has default value OK
PYTHONPATH has default value OK
MODULEPATH has default value OK
MODULEPATH_ROOT has default value OK
TMPDIR has default value OK
Command alias output differs NOTE
Command module list has default output OK


CSC ssh test
---------------------
CSC generated key pair exists: OK
$HOME permission is 0700: OK
CSC generated key pair seem valid: OK
SSH folder and key permissions correct: OK
CSC generated ssh config is present: OK


File diff test
---------------------
/users/csc_user/.bashrc is modified NOTE
/users/csc_user/.bash_profile same as default OK
/users/csc_user/.bash_logout same as default OK
```

`OK` indicates that the test matches the default and `FAILED` indicates that there is an incorrect setting.
`NOTE` does not indicate an error, just that the setting has been changed and might explain some issues.


