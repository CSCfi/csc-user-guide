# Profilling in Python with cProfile
[cProfile](https://docs.python.org/2/library/profile.html#module-cProfile) is one of the deterministic built-in deterministic profiler. within the  code, or from the interpreter:
```
import  cProfile
cProfile.run('functba(list_parameters)')
```
Now the script can be ran the normal as a normal pythin job. This will give information about how long  and how many times the function gets called. 

Alternatively  cProfile can also be invoked as a script to profile another script:
```
python -m cProfile [-o output_file] [-s sort_order] myscript.py
```
The results can be output to the Stdout or saved to a file. By default they are ordered by name, but other options are as well available. The report save in ```output_file``` cab vbe visualized and interpreted by graphical tools, such as ```pyprof2calltree```.
