# csc-env command

`csc-env` is a command line tool for testing for common issues in the programming environment,
and resetting the login environment on CSC supercomputers.

The tool does the reset in a non-destructive manner by saving a copy of the current settings which 
can then be later restored.  

- **login-settings** -> The following files: `.bashrc`, `.bash_profile` and `.bash_logout` in the users home directory

Incorrect or extra variables in the login-settings are a common cause for strange and hard to track down issues.
CSC support staff also can't see a users login-settings, so catching issues here is difficult unless the user 
sends us their login-settings. 
Temporarily resetting the login-settings to system default allows us to rule out one possible cause.   

!!!Note "Only bash support at the moment"
    If you are using some other login shell (ksh, zsh ...) the tool can not reset your login-settings,
    you can use the tool to switch to bash.

!!!Note "CSC internal ssh changes"
    As of the RHEL8 update, ssh connections between nodes within the supercomputers no longer use keys and configs from "~/.ssh" instead using host based authentication. Due to this the capability to reset the ssh settings has been removed. 

## Usage


### Help 

`csc-env help` will show all the available commands and options.

### Test

`csc-env test` will check for common issues in the user environment by comparing 
them to the default settings. The test result can be included in your support request to the servicedesk. 
Below is an example test output: 

```
csc_user@puhti $ csc-env test

Info
---------------------
User: csc_user
Host: puhti-login11
Home: /users/csc_user
Home quota
    capacity: 23%
    files:    15%
Default shell: /bin/bash 



Environment test
---------------------
PATH is modified NOTE
LD_LIBRARY_PATH has default value OK
LD_PRELOAD has default value OK
PYTHONPATH has default value OK
MODULEPATH has default value OK
MODULEPATH_ROOT has default value OK
TMPDIR has default value OK
CDPATH has default value OK
Command alias output differs NOTE
Command module list has default output OK
$HOME permission is 0700: OK
SSH folder permission is 0700: OK



File diff test
---------------------
/users/csc_user/.bashrc is modified NOTE
/users/csc_user/.bash_profile same as default OK
/users/csc_user/.bash_logout same as default OK
```

`OK` indicates that the test matches the default and `FAILED` indicates that there is an incorrect setting.
`NOTE` does not indicate an error, just that the setting has been changed and might explain some issues.

### Basic usage

Here we present the basic reset + restore cycle.

`csc-env reset` will ask you what settings you want to reset, save the settings, and reset them to system defaults.
When the program prompts for input, press the number corresponding to your selection and then press enter. 

```
csc_user@puhti $ csc-env reset
[ INFO ] reset requires a target, please select one: 
1) login
2) shell
#? 1
[ INFO ] Files ~/.bashrc ~/.bash_profile and ~/.bash_logout have been saved to 
         /users/csc_user/.csc/csc_env_saves/login_auto/2021-01-18T14:42:44_reset_csc14 
[ INFO ] Resetting ~/.bashrc ~/.bash_profile and ~/.bash_logout 
Confirm
1) Yes
2) No
#? 1
[ INFO ] Reset completed
```

When you want to restore the settings, use the command `csc-env restore`. This will ask you what settings you want to restore, save the current settings, and
then restore the settings saved during the previous reset. 

```
csc_user@puhti $ csc-env restore
[ INFO ] restore requires a target, please select one: 
1) login
2) shell
#? 1
[ INFO ] Files ~/.bashrc ~/.bash_profile and ~/.bash_logout have been saved to
         /users/csc_user/.csc/csc_env_saves/login_auto/2021-01-18T14:47:59_restore_csc15 
[ INFO ] Restoring .bashrc .bash_profile and .bash_logout from 
         /users/csc_user/.csc/csc_env_saves/login_auto/2021-01-18T14:42:44_reset_csc14 
Confirm
1) Yes
2) No
#? 1
[ INFO ] Restore was completed
```

If you accidentally do `csc-env reset` twice in a row, do not panic, your files are not lost.
See the next chapter for information on how to recover them. 

### Advanced usage

#### Running commands in a clean environment

Using the command `csc-env run-base` the user can be dropped into a
new shell where no user modifications are present. This is useful for testing and debugging
without changes to any files. Running a command in a clean environment can be done with
`csc-env run-base -- -c "command args"`

Note that clean here means the default login settings (so default modules will be loaded)

#### Manually creating and selecting saves 

Each invocation of `csc-env reset` or `csc-env restore` automatically saves the current selected settings. 
The command `csc-env list-saved` will list all saves:

```
csc_user@puhti $ csc-env list-saved
Available restores in /users/csc_user/.csc/csc_env_saves

login
---------------------
MY_SAVE  save  2021-01-08T12:14:04

csc7  restore  2021-01-18T14:52:34
csc6  restore  2021-01-18T14:51:55
csc5  reset    2021-01-18T14:51:37
csc4  reset    2021-01-18T14:51:34
```
The first column is the name of the save, the second is the action which created the save and the last column is the creation time of the save.

To select a particular save to restore from you can use the `--sname` flag: `csc-env --sname=csc4 restore`
If you get tired of always selecting the target you can also specify that on the command line: `csc-env --sname=csc4 --target=login restore`

The command `csc-env save` can be used create a save of the settings without changing them. 
Both `save` and `reset` also accept the `--sname` for creating a save with a custom name (instead of the automatic _csc(number)_).
Note that `csc-env restore` will by default choose the most recent automatically named save created during a `save` or `reset`

If for some reason you don't like the default place for the saves (`$HOME/.csc/csc_env_saves`), you can change it with the `--sdir=/path/to/save/dir`. 
The tool will then both create new saves and search for existing ones in this directory. 

To remove the whole save directory, use the command `csc-env remove-saved`. **Warning!** this will permanently delete all saves in the directory.

There are still some additional options which you can view with `csc-env help`
