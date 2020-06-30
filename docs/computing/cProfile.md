# Profilling in Python with cProfile
[cProfile](https://docs.python.org/2/library/profile.html#module-cProfile) is one of the deterministic built-in deterministic profiler. There are two ways to use the profiler. Within the  code (or from the interpreter):
```
import  cProfile
cProfile.run('functba(list_parameters)')
```
Now the script can be ran the normal as a normal python job. This will give information about how long  and how many times the function gets called. 

Alternatively  cProfile can also be invoked as a script to profile another script:
```
python -m cProfile [-o output_file] [-s sort_order] myscript.py
```
The results can be output to the Stdout or saved to a file. By default they are ordered by name, but other options are as well available. The report save in ```output_file``` can be visualized and interpreted by graphical tools, such as ```pyprof2calltree```. Here is an example of a profilling done for a function:

```
93 function calls in 0.065 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.065    0.065 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 _methods.py:138(_std)
        1    0.000    0.000    0.000    0.000 _methods.py:30(_amin)
        1    0.000    0.000    0.028    0.028 _numpy_fft.py:1086(irfftn)
        1    0.000    0.000    0.003    0.003 arraypad.py:102(_do_append)
        2    0.000    0.000    0.000    0.000 arraypad.py:107(_prepend_const)
        2    0.000    0.000    0.004    0.002 arraypad.py:136(_append_const)
        3    0.000    0.000    0.000    0.000 arraypad.py:160(<genexpr>)
        2    0.000    0.000    0.000    0.000 arraypad.py:889(_as_pairs)
        1    0.000    0.000    0.008    0.008 arraypad.py:964(pad)
        1    0.000    0.000    0.065    0.065 compute_correlations.py:4(compute_correlations)
        1    0.000    0.000    0.000    0.000 function_base.py:258(iterable)
        1    0.000    0.000    0.000    0.000 getlimits.py:365(__new__)
        1    0.032    0.032    0.065    0.065 normxcorr2.py:33(normxcorr2)
        1    0.000    0.000    0.065    0.065 {built-in method builtins.exec}
        1    0.003    0.003    0.003    0.003 {built-in method numpy.concatenate}
        2    0.002    0.001    0.002    0.001 {built-in method numpy.copyto}
        1    0.002    0.002    0.002    0.002 {built-in method numpy.where}
        1    0.000    0.000    0.000    0.000 {built-in method numpy.zeros}
        2    0.000    0.000    0.000    0.000 {method 'astype' of 'numpy.ndarray' objects}
        2    0.003    0.002    0.003    0.002 {method 'copy' of 'numpy.ndarray' objects}
        1    0.020    0.020    0.028    0.028 {mkl_fft._pydfti.irfftn_numpy}
```
Keep in mind that running the profiler has to be done in the same as running as a [batch](running/example-job-scripts.md) or [interactive](running/interactive-usage.md) job. 
