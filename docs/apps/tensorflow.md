# TensorFlow

Deep learning framework for Python.

## Available

The `tensorflow` module is available on Puhti only.  Currently supported TensorFlow versions:

- 1.14.0
- 1.13.1
- 1.13.1-hvd (with [Horovod](https://github.com/horovod/horovod) support)

Activates a conda environment that includes [TensorFlow](https://www.tensorflow.org/) and [Keras](https://keras.io/) with GPU support via CUDA.  Also includes all the packages from [Python Data](python-data.md).

If you find that some package is missing, you can often install it yourself with `pip install --user`.

If you think that some important TensorFlow-related package should be included in the module provided by CSC, you can send an email to <servicedesk@csc.fi>.

## License

TensorFlow is licensed under [Apache License 2.0](https://github.com/tensorflow/tensorflow/blob/master/LICENSE).

## Usage

To use this software on Puhti, initialize it with:

```bash
$ module load tensorflow
```

to access the default version.

This will show all available versions:

```bash
$ module avail tensorflow
```

To check the exact packages and version included a specific module, you can run for example:

```bash
$ module load tensorflow/1.14.0
$ conda list
```

!!! note 

    Note that Puhti login nodes are not intended for heavy
    computing. Please use slurm batch jobs instead.

## More information

- [TensorFlow overview](https://www.tensorflow.org/overview/)
- [Get Started with TensorFlow](https://www.tensorflow.org/tutorials)
- [TensorFlow API documentation](https://www.tensorflow.org/api_docs/python/tf)
- [Keras documentation](https://keras.io/)
