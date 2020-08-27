# cProfile: Python profiler

[cProfile](https://docs.python.org/3.8/library/profile.html#module-cProfile)
is a built-in profiler for Python programs. There are two ways to use the
profiler. Within the code (or from the interpreter):

```
import cProfile
cProfile.run('functba(list_parameters)')
```

Now the script can be ran as a normal Python job. This will give information
about how long and how many times the function gets called.

Alternatively cProfile can also be invoked as a script to profile another
script:

```
python -m cProfile [-o output_file] [-s sort_order] myscript.py
```

The results can be printed out or saved to a file. By default they are ordered
by name, but other options are available, too.

A report saved in a file can e.g. be visualized and interpreted by a
graphical tool such as `pyprof2calltree`. Here is an example of a profiling
done for a function:

```
93 function calls in 0.065 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.065    0.065 <string>:1(<module>)
        1    0.000    0.000    0.028    0.028 _numpy_fft.py:1086(irfftn)
        1    0.000    0.000    0.003    0.003 arraypad.py:102(_do_append)
        2    0.000    0.000    0.000    0.000 arraypad.py:107(_prepend_const)
        2    0.000    0.000    0.004    0.002 arraypad.py:136(_append_const)
        1    0.000    0.000    0.008    0.008 arraypad.py:964(pad)
        1    0.000    0.000    0.065    0.065 compute_correlations.py:4(compute_correlations)
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

Keep in mind that running the profiler has to be done in the same way as
running a ([puhti](running/example-job-scripts-puhti.md)  or [mahti](running/example-job-scripts-mahti.md)) batch or
[interactive](running/interactive-usage.md) job.
