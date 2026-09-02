---
tags:
  - Free
catalog:
  name: Python Data
  description: Collection of Python libraries for data analytics and machine learning
  license_type: Free
  disciplines:
    - Data Analytics and Machine Learning
  available_on:
    - Roihu
    
---

# Python Data

Collection of Python libraries for data analytics and machine learning.

!!! info "News"
     **31.3.2026** Python-data is now available on Roihu. The default version on Roihu-CPU is `python-data/3.12-31.03` and
     `python-data/3.12-20.04` on Roihu-GPU.

     **12.9.2025** Installed `python-data/3.12-25.09` with newer packages of popular Python 
     modules.

     **2.5.2024** Installed `python-data/3.10-24.04` with newer packages of popular Python 
     modules.

    **28.11.2023** Installed `python-data/3.10-23.11` with newer packages of popular Python 
     modules.

     **28.11.2023** Installed `python-data/3.10-23.11` with newer packages of popular Python 
     modules.

     **4.7.2023** Installed `python-data/3.10-23.07` with newer packages of popular Python 
     modules.

    **28.10.2022** Module `python-data/3.8` was added for those who
    specifically need Python 3.8.


## Available

Versions are numbered as `X.Z-YY.MM`, where `X.Z` is the version of
the Python interpreter, and `YY.MM` is the year and month of the
installation. Typically the module will include the newest versions of
libraries at installation time, to the extent software dependencies
allow.

Current versions in Roihu are: 

- Roihu-CPU: (default version) `python-data/3.12-31.03`: installed in March 2026,
  includes for example Scikit-learn 1.8.0, SciPy 1.17.1, Pandas 2.3.3
  and JupyterLab 4.5.6.

- Roihu-GPU: (default version) `python-data/3.12-20.04`: installed in April 2026,
  includes for example Cupy 14.0.1 in addition to the Python libraries available in Roihu-CPU python-data.

- Roihu-GPU: `python-data/3.10-17.04`: installed in April 2026,
  includes the Python libraries available in the default Roihu-GPU python-data environment with Python 3.10.
  
- Roihu-CPU: `python-data/3.10-03.07`: installed in July 2026,
  includes the Python libraries available in the default Roihu-CPU python-data environment with Python 3.10.

Python-data tries to include a comprehensive selection of Python libraries for
data analytics and machine learning, for example:

- [Dask](https://dask.org/): Scalable analytics in Python
- [Gensim](https://radimrehurek.com/gensim/): Topic modelling
- [Jupyter](https://jupyter.org/index.html) and [JupyterLab](https://jupyterlab.readthedocs.io/en/stable/)
- [Marimo](https://marimo.io) (Roihu)
- [NLTK](https://matplotlib.org/): Natural language toolkit
- [Polars] (https://docs.pola.rs): Large-scale data analytics
- [PyTables](http://www.pytables.org/)
- [SciPy](https://www.scipy.org/), including [NumPy](https://www.numpy.org/), [Matplotlib](https://matplotlib.org/) and [Pandas](https://pandas.pydata.org/)
- [Scikit-learn](https://scikit-learn.org/stable/): Machine learning in Python
- [Seaborn](https://seaborn.pydata.org/): Statistical data visualization

??? info "Click to see full list of packages for python-data/3.12-31.03"

    <div class="pkg-table" markdown="1">

    - `absl-py` <span class="v">2.4.0</span>
    - `aiohappyeyeballs` <span class="v">2.6.1</span>
    - `aiohttp` <span class="v">3.13.5</span>
    - `aiohttp-cors` <span class="v">0.8.1</span>
    - `aiosignal` <span class="v">1.4.0</span>
    - `alabaster` <span class="v">1.0.0</span>
    - `alembic` <span class="v">1.18.4</span>
    - `altair` <span class="v">6.0.0</span>
    - `annotated-doc` <span class="v">0.0.4</span>
    - `annotated-types` <span class="v">0.7.0</span>
    - `anyio` <span class="v">4.13.0</span>
    - `argon2-cffi` <span class="v">25.1.0</span>
    - `argon2-cffi-bindings` <span class="v">25.1.0</span>
    - `arrow` <span class="v">1.4.0</span>
    - `arviz` <span class="v">1.1.0</span>
    - `arviz-base` <span class="v">1.1.0</span>
    - `arviz-plots` <span class="v">1.1.0</span>
    - `arviz-stats` <span class="v">1.1.0</span>
    - `ase` <span class="v">3.29.0</span>
    - `astroid` <span class="v">4.0.4</span>
    - `asttokens` <span class="v">3.0.1</span>
    - `async-lru` <span class="v">2.3.0</span>
    - `async-timeout` <span class="v">5.0.1</span>
    - `asyncssh` <span class="v">2.22.0</span>
    - `attrs` <span class="v">26.1.0</span>
    - `autopep8` <span class="v">2.0.4</span>
    - `babel` <span class="v">2.18.0</span>
    - `backports.tarfile` <span class="v">1.2.0</span>
    - `backports.zstd` <span class="v">1.3.0</span>
    - `banduppy` <span class="v">1.0.1.dev0</span>
    - `bcrypt` <span class="v">5.0.0</span>
    - `beautifulsoup4` <span class="v">4.14.3</span>
    - `bibtexparser` <span class="v">1.4.4</span>
    - `binaryornot` <span class="v">0.6.0</span>
    - `black` <span class="v">26.3.1</span>
    - `bleach` <span class="v">6.3.0</span>
    - `blinker` <span class="v">1.9.0</span>
    - `bokeh` <span class="v">3.9.0</span>
    - `boto3` <span class="v">1.42.89</span>
    - `botocore` <span class="v">1.42.89</span>
    - `Brotli` <span class="v">1.2.0</span>
    - `cached-property` <span class="v">1.5.2</span>
    - `cachetools` <span class="v">6.2.6</span>
    - `cattrs` <span class="v">26.1.0</span>
    - `certifi` <span class="v">2026.4.22</span>
    - `cffi` <span class="v">2.0.0</span>
    - `cftime` <span class="v">1.6.5</span>
    - `chardet` <span class="v">5.2.0</span>
    - `charset-normalizer` <span class="v">3.4.7</span>
    - `click` <span class="v">8.3.2</span>
    - `cloudpickle` <span class="v">3.1.2</span>
    - `colorama` <span class="v">0.4.6</span>
    - `colorful` <span class="v">0.5.8</span>
    - `comm` <span class="v">0.2.3</span>
    - `cons` <span class="v">0.4.7</span>
    - `contourpy` <span class="v">1.3.3</span>
    - `cookiecutter` <span class="v">2.7.1</span>
    - `cryptography` <span class="v">46.0.7</span>
    - `cycler` <span class="v">0.12.1</span>
    - `Cython` <span class="v">3.2.4</span>
    - `cytoolz` <span class="v">1.1.0</span>
    - `dash` <span class="v">4.1.0</span>
    - `dash-bootstrap-components` <span class="v">2.0.4</span>
    - `dash-bootstrap-templates` <span class="v">2.1.0</span>
    - `dask` <span class="v">2026.3.0</span>
    - `dask-glm` <span class="v">0.3.2</span>
    - `dask-jobqueue` <span class="v">0.9.0</span>
    - `dask_labextension` <span class="v">7.0.0</span>
    - `dask-ml` <span class="v">2025.1.0</span>
    - `databricks-sdk` <span class="v">0.102.0</span>
    - `debtcollector` <span class="v">3.1.0</span>
    - `debugpy` <span class="v">1.8.20</span>
    - `decorator` <span class="v">5.2.1</span>
    - `defusedxml` <span class="v">0.7.1</span>
    - `Deprecated` <span class="v">1.3.1</span>
    - `diff-match-patch` <span class="v">20241021</span>
    - `dill` <span class="v">0.4.1</span>
    - `distlib` <span class="v">0.4.0</span>
    - `distributed` <span class="v">2026.3.0</span>
    - `dnspython` <span class="v">2.8.0</span>
    - `docker` <span class="v">7.1.0</span>
    - `docstring-to-markdown` <span class="v">0.17</span>
    - `docutils` <span class="v">0.22.4</span>
    - `email-validator` <span class="v">2.3.0</span>
    - `entrypoints` <span class="v">0.4</span>
    - `et_xmlfile` <span class="v">2.0.0</span>
    - `etuples` <span class="v">0.3.10</span>
    - `exceptiongroup` <span class="v">1.3.1</span>
    - `executing` <span class="v">2.2.1</span>
    - `fastapi` <span class="v">0.135.3</span>
    - `fastapi-cli` <span class="v">0.0.23</span>
    - `fastar` <span class="v">0.11.0</span>
    - `fastjsonschema` <span class="v">2.21.2</span>
    - `fasttext` <span class="v">0.9.2</span>
    - `filelock` <span class="v">3.25.2</span>
    - `flake8` <span class="v">7.1.2</span>
    - `Flask` <span class="v">3.1.3</span>
    - `flask-cors` <span class="v">6.0.2</span>
    - `fonttools` <span class="v">4.62.0</span>
    - `fortio` <span class="v">0.4</span>
    - `fqdn` <span class="v">1.5.1</span>
    - `frozenlist` <span class="v">1.7.0</span>
    - `fsspec` <span class="v">2026.3.0</span>
    - `future` <span class="v">1.0.0</span>
    - `gensim` <span class="v">4.4.0</span>
    - `gitdb` <span class="v">4.0.12</span>
    - `GitPython` <span class="v">3.1.46</span>
    - `google-api-core` <span class="v">2.30.3</span>
    - `google-auth` <span class="v">2.49.2</span>
    - `googleapis-common-protos` <span class="v">1.74.0</span>
    - `graphene` <span class="v">3.4.3</span>
    - `graphql-core` <span class="v">3.2.8</span>
    - `graphql-relay` <span class="v">3.2.0</span>
    - `greenlet` <span class="v">3.4.0</span>
    - `grpcio` <span class="v">1.78.1</span>
    - `gssapi` <span class="v">1.11.1</span>
    - `gunicorn` <span class="v">23.0.0</span>
    - `h11` <span class="v">0.16.0</span>
    - `h2` <span class="v">4.3.0</span>
    - `h5py` <span class="v">3.16.0</span>
    - `hpack` <span class="v">4.1.0</span>
    - `httpcore` <span class="v">1.0.9</span>
    - `httptools` <span class="v">0.7.1</span>
    - `httpx` <span class="v">0.28.1</span>
    - `huey` <span class="v">2.6.0</span>
    - `hyperframe` <span class="v">6.1.0</span>
    - `hyperopt` <span class="v">0.2.7</span>
    - `idna` <span class="v">3.11</span>
    - `imagecodecs` <span class="v">2026.3.6</span>
    - `imageio` <span class="v">2.37.0</span>
    - `imagesize` <span class="v">2.0.0</span>
    - `imbalanced-learn` <span class="v">0.14.1</span>
    - `importlib_metadata` <span class="v">8.7.0</span>
    - `importlib_resources` <span class="v">7.1.0</span>
    - `inflection` <span class="v">0.5.1</span>
    - `iniconfig` <span class="v">2.3.0</span>
    - `intervaltree` <span class="v">3.1.0</span>
    - `invoke` <span class="v">3.0.3</span>
    - `ipdb` <span class="v">0.13.13</span>
    - `ipykernel` <span class="v">6.31.0</span>
    - `ipython` <span class="v">9.12.0</span>
    - `ipython-genutils` <span class="v">0.2.0</span>
    - `ipython_pygments_lexers` <span class="v">1.1.1</span>
    - `ipywidgets` <span class="v">8.1.8</span>
    - `irrep` <span class="v">3.1.1</span>
    - `iso8601` <span class="v">2.1.0</span>
    - `isodate` <span class="v">0.7.2</span>
    - `isoduration` <span class="v">20.11.0</span>
    - `isort` <span class="v">8.0.1</span>
    - `itsdangerous` <span class="v">2.2.0</span>
    - `jaraco.classes` <span class="v">3.4.0</span>
    - `jaraco.context` <span class="v">6.1.1</span>
    - `jaraco.functools` <span class="v">4.4.0</span>
    - `jedi` <span class="v">0.19.2</span>
    - `jeepney` <span class="v">0.9.0</span>
    - `jellyfish` <span class="v">1.2.1</span>
    - `Jinja2` <span class="v">3.1.6</span>
    - `jmespath` <span class="v">1.1.0</span>
    - `joblib` <span class="v">1.5.3</span>
    - `json5` <span class="v">0.14.0</span>
    - `jsonpointer` <span class="v">3.1.1</span>
    - `jsonschema` <span class="v">4.26.0</span>
    - `jsonschema-specifications` <span class="v">2025.9.1</span>
    - `jupyter_client` <span class="v">8.8.0</span>
    - `jupyter_core` <span class="v">5.9.1</span>
    - `jupyter-events` <span class="v">0.12.0</span>
    - `jupyter-lsp` <span class="v">2.3.1</span>
    - `jupyter-resource-usage` <span class="v">1.2.1</span>
    - `jupyter_server` <span class="v">2.17.0</span>
    - `jupyter_server_proxy` <span class="v">4.5.0</span>
    - `jupyter_server_terminals` <span class="v">0.5.4</span>
    - `jupyterlab` <span class="v">4.5.6</span>
    - `jupyterlab_git` <span class="v">0.52.0</span>
    - `jupyterlab_pygments` <span class="v">0.3.0</span>
    - `jupyterlab_server` <span class="v">2.28.0</span>
    - `jupyterlab_widgets` <span class="v">3.0.16</span>
    - `jupytext` <span class="v">1.19.1</span>
    - `kaggle` <span class="v">2.0.1</span>
    - `kagglesdk` <span class="v">0.1.17</span>
    - `keyring` <span class="v">25.7.0</span>
    - `keystoneauth1` <span class="v">5.13.1</span>
    - `kiwisolver` <span class="v">1.5.0</span>
    - `lark` <span class="v">1.3.1</span>
    - `lazy-loader` <span class="v">0.5</span>
    - `lightgbm` <span class="v">4.6.0</span>
    - `llvmlite` <span class="v">0.47.0</span>
    - `lmdb` <span class="v">2.1.1</span>
    - `locket` <span class="v">1.0.0</span>
    - `logical-unification` <span class="v">0.4.7</span>
    - `logzero` <span class="v">1.7.0</span>
    - `loro` <span class="v">1.10.3</span>
    - `lsprotocol` <span class="v">2025.0.0</span>
    - `lxml` <span class="v">6.1.1</span>
    - `lz4` <span class="v">4.4.5</span>
    - `Mako` <span class="v">1.3.10</span>
    - `marimo` <span class="v">0.23.1</span>
    - `Markdown` <span class="v">3.10.2</span>
    - `markdown-it-py` <span class="v">4.0.0</span>
    - `MarkupSafe` <span class="v">3.0.3</span>
    - `matplotlib` <span class="v">3.10.8</span>
    - `matplotlib-inline` <span class="v">0.2.1</span>
    - `mccabe` <span class="v">0.7.0</span>
    - `mdit-py-plugins` <span class="v">0.5.0</span>
    - `mdurl` <span class="v">0.1.2</span>
    - `miniKanren` <span class="v">1.0.5</span>
    - `mistune` <span class="v">3.2.0</span>
    - `mlflow` <span class="v">3.10.1</span>
    - `mlflow-skinny` <span class="v">3.10.1</span>
    - `mlflow-tracing` <span class="v">3.10.1</span>
    - `monty` <span class="v">2026.7.16</span>
    - `more-itertools` <span class="v">11.0.2</span>
    - `mpmath` <span class="v">1.3.0</span>
    - `msgpack` <span class="v">1.1.2</span>
    - `msgspec` <span class="v">0.21.0</span>
    - `multidict` <span class="v">6.7.1</span>
    - `multipledispatch` <span class="v">0.6.0</span>
    - `munkres` <span class="v">1.1.4</span>
    - `mypy_extensions` <span class="v">1.1.0</span>
    - `narwhals` <span class="v">2.19.0</span>
    - `nbclassic` <span class="v">1.3.3</span>
    - `nbclient` <span class="v">0.10.4</span>
    - `nbconvert` <span class="v">7.17.1</span>
    - `nbdime` <span class="v">4.0.4</span>
    - `nbformat` <span class="v">5.10.4</span>
    - `nest_asyncio` <span class="v">1.6.0</span>
    - `netaddr` <span class="v">1.3.0</span>
    - `netCDF4` <span class="v">1.7.4</span>
    - `networkx` <span class="v">3.6.1</span>
    - `nltk` <span class="v">3.9.4</span>
    - `notebook` <span class="v">7.5.5</span>
    - `notebook_shim` <span class="v">0.2.4</span>
    - `numba` <span class="v">0.65.0</span>
    - `numexpr` <span class="v">2.14.1</span>
    - `numpy` <span class="v">2.4.6</span>
    - `numpydoc` <span class="v">1.10.0</span>
    - `nvidia-nccl-cu12` <span class="v">2.29.7</span>
    - `odfpy` <span class="v">1.4.1</span>
    - `opencensus` <span class="v">0.11.3</span>
    - `opencensus-context` <span class="v">0.1.3</span>
    - `opencv-python` <span class="v">4.13.0</span>
    - `opencv-python-headless` <span class="v">4.13.0</span>
    - `openpyxl` <span class="v">3.1.5</span>
    - `opentelemetry-api` <span class="v">1.41.0</span>
    - `opentelemetry-exporter-prometheus` <span class="v">0.62b0</span>
    - `opentelemetry-proto` <span class="v">1.41.0</span>
    - `opentelemetry-sdk` <span class="v">1.41.0</span>
    - `opentelemetry-semantic-conventions` <span class="v">0.62b0</span>
    - `orjson` <span class="v">3.11.9</span>
    - `os-service-types` <span class="v">1.8.2</span>
    - `oslo.config` <span class="v">10.3.0</span>
    - `oslo.i18n` <span class="v">6.7.2</span>
    - `oslo.serialization` <span class="v">5.9.1</span>
    - `oslo.utils` <span class="v">10.0.1</span>
    - `overrides` <span class="v">7.7.0</span>
    - `packaging` <span class="v">26.0</span>
    - `palettable` <span class="v">3.3.3</span>
    - `pandas` <span class="v">2.3.3</span>
    - `pandocfilters` <span class="v">1.5.0</span>
    - `papermill` <span class="v">2.7.0</span>
    - `paramiko` <span class="v">4.0.0</span>
    - `parso` <span class="v">0.8.6</span>
    - `partd` <span class="v">1.4.2</span>
    - `pathspec` <span class="v">1.0.4</span>
    - `patsy` <span class="v">1.0.2</span>
    - `pbr` <span class="v">7.0.3</span>
    - `pexpect` <span class="v">4.9.0</span>
    - `pickleshare` <span class="v">0.7.5</span>
    - `pillow` <span class="v">12.2.0</span>
    - `pip` <span class="v">26.0.1</span>
    - `platformdirs` <span class="v">4.9.6</span>
    - `plotly` <span class="v">6.6.0</span>
    - `pluggy` <span class="v">1.6.0</span>
    - `ply` <span class="v">3.11</span>
    - `polars` <span class="v">1.44.1</span>
    - `prettytable` <span class="v">3.17.0</span>
    - `prometheus_client` <span class="v">0.25.0</span>
    - `prometheus_flask_exporter` <span class="v">0.23.2</span>
    - `prompt_toolkit` <span class="v">3.0.52</span>
    - `propcache` <span class="v">0.3.1</span>
    - `proto-plus` <span class="v">1.27.2</span>
    - `protobuf` <span class="v">6.33.5</span>
    - `psutil` <span class="v">7.2.2</span>
    - `ptyprocess` <span class="v">0.7.0</span>
    - `pure_eval` <span class="v">0.2.3</span>
    - `py-cpuinfo` <span class="v">9.0.0</span>
    - `py4j` <span class="v">0.10.9.9</span>
    - `pyarrow` <span class="v">23.0.1</span>
    - `pyasn1` <span class="v">0.6.3</span>
    - `pyasn1_modules` <span class="v">0.4.2</span>
    - `pybind11` <span class="v">3.0.3</span>
    - `pybind11-global` <span class="v">3.0.3</span>
    - `pycodestyle` <span class="v">2.12.1</span>
    - `pyconify` <span class="v">0.2.1</span>
    - `pycparser` <span class="v">2.22</span>
    - `pydantic` <span class="v">2.13.0</span>
    - `pydantic_core` <span class="v">2.46.0</span>
    - `pydantic-extra-types` <span class="v">2.11.2</span>
    - `pydantic-settings` <span class="v">2.14.0</span>
    - `pydeck` <span class="v">0.8.0b4</span>
    - `pydocstyle` <span class="v">6.3.0</span>
    - `pydot` <span class="v">4.0.1</span>
    - `pyflakes` <span class="v">3.2.0</span>
    - `PyGithub` <span class="v">2.9.0</span>
    - `Pygments` <span class="v">2.20.0</span>
    - `pyhdf` <span class="v">0.11.6</span>
    - `PyJWT` <span class="v">2.12.1</span>
    - `pylint` <span class="v">4.0.5</span>
    - `pylint-venv` <span class="v">3.0.4</span>
    - `pyls-spyder` <span class="v">0.4.0</span>
    - `pymatgen` <span class="v">2026.5.4</span>
    - `pymatgen-core` <span class="v">2026.8.13</span>
    - `pymc` <span class="v">6.0.1</span>
    - `pymdown-extensions` <span class="v">10.21.2</span>
    - `PyNaCl` <span class="v">1.6.2</span>
    - `pynndescent` <span class="v">0.5.13</span>
    - `pyocse` <span class="v">0.1.3</span>
    - `pyOpenSSL` <span class="v">26.0.0</span>
    - `pyparsing` <span class="v">3.3.2</span>
    - `pyproj` <span class="v">3.7.2</span>
    - `PyQt5` <span class="v">5.15.11</span>
    - `PyQt5_sip` <span class="v">12.17.0</span>
    - `PyQtWebEngine` <span class="v">5.15.7</span>
    - `PySide6` <span class="v">6.10.2</span>
    - `PySocks` <span class="v">1.7.1</span>
    - `pytensor` <span class="v">3.0.4</span>
    - `pytest` <span class="v">9.0.3</span>
    - `python-dateutil` <span class="v">2.9.0.post0</span>
    - `python-discovery` <span class="v">1.2.2</span>
    - `python-dotenv` <span class="v">1.2.2</span>
    - `python-json-logger` <span class="v">2.0.7</span>
    - `python-keystoneclient` <span class="v">5.8.0</span>
    - `python-lsp-black` <span class="v">2.0.0</span>
    - `python-lsp-jsonrpc` <span class="v">1.1.2</span>
    - `python-lsp-ruff` <span class="v">2.3.1</span>
    - `python-lsp-server` <span class="v">1.14.0</span>
    - `python-multipart` <span class="v">0.0.27</span>
    - `python-poppler` <span class="v">0.4.1</span>
    - `python-slugify` <span class="v">8.0.4</span>
    - `python-swiftclient` <span class="v">4.10.0</span>
    - `pytokens` <span class="v">0.4.1</span>
    - `pytoolconfig` <span class="v">1.2.5</span>
    - `pytz` <span class="v">2026.1.post1</span>
    - `pyu2f` <span class="v">0.1.5</span>
    - `pyuca` <span class="v">1.2</span>
    - `pyxdg` <span class="v">0.28</span>
    - `pyxtal` <span class="v">1.1.1</span>
    - `PyYAML` <span class="v">6.0.3</span>
    - `pyzmq` <span class="v">27.1.0</span>
    - `QDarkStyle` <span class="v">3.2.3</span>
    - `qstylizer` <span class="v">0.2.4</span>
    - `QtAwesome` <span class="v">1.4.2</span>
    - `qtconsole` <span class="v">5.7.2</span>
    - `QtPy` <span class="v">2.4.3</span>
    - `querystring_parser` <span class="v">1.2.4</span>
    - `ray` <span class="v">2.54.0</span>
    - `rdflib` <span class="v">7.6.0</span>
    - `redis` <span class="v">7.4.0</span>
    - `referencing` <span class="v">0.37.0</span>
    - `regex` <span class="v">2026.4.4</span>
    - `requests` <span class="v">2.33.1</span>
    - `retrying` <span class="v">1.4.2</span>
    - `rfc3339_validator` <span class="v">0.1.4</span>
    - `rfc3986` <span class="v">2.0.0</span>
    - `rfc3986-validator` <span class="v">0.1.1</span>
    - `rfc3987-syntax` <span class="v">1.1.0</span>
    - `rich` <span class="v">15.0.0</span>
    - `rich-toolkit` <span class="v">0.19.7</span>
    - `roman-numerals` <span class="v">4.1.0</span>
    - `rope` <span class="v">1.14.0</span>
    - `rpds-py` <span class="v">0.30.0</span>
    - `rsa` <span class="v">4.9.1</span>
    - `rtree` <span class="v">1.4.1</span>
    - `ruamel.yaml` <span class="v">0.19.1</span>
    - `ruff` <span class="v">0.15.10</span>
    - `s3cmd` <span class="v">2.4.0</span>
    - `s3transfer` <span class="v">0.16.0</span>
    - `scikit-image` <span class="v">0.26.0</span>
    - `scikit-learn` <span class="v">1.8.0</span>
    - `scipy` <span class="v">1.17.1</span>
    - `seaborn` <span class="v">0.13.2</span>
    - `SecretStorage` <span class="v">3.4.1</span>
    - `Send2Trash` <span class="v">2.1.0</span>
    - `setproctitle` <span class="v">1.2.2</span>
    - `setuptools` <span class="v">81.0.0</span>
    - `shellingham` <span class="v">1.5.4</span>
    - `shiboken6` <span class="v">6.10.2</span>
    - `simpervisor` <span class="v">1.0.0</span>
    - `sip` <span class="v">6.10.0</span>
    - `six` <span class="v">1.17.0</span>
    - `sklearn-compat` <span class="v">0.1.5</span>
    - `skops` <span class="v">0.13.0</span>
    - `smart_open` <span class="v">7.6.0</span>
    - `smmap` <span class="v">5.0.3</span>
    - `sniffio` <span class="v">1.3.1</span>
    - `snowballstemmer` <span class="v">3.0.1</span>
    - `sortedcontainers` <span class="v">2.4.0</span>
    - `soupsieve` <span class="v">2.8.3</span>
    - `sparse` <span class="v">0.18.0</span>
    - `spglib` <span class="v">2.7.0</span>
    - `Sphinx` <span class="v">9.1.0</span>
    - `sphinxcontrib-applehelp` <span class="v">2.0.0</span>
    - `sphinxcontrib-devhelp` <span class="v">2.0.0</span>
    - `sphinxcontrib-htmlhelp` <span class="v">2.1.0</span>
    - `sphinxcontrib-jsmath` <span class="v">1.0.1</span>
    - `sphinxcontrib-qthelp` <span class="v">2.0.0</span>
    - `sphinxcontrib-serializinghtml` <span class="v">1.1.10</span>
    - `spyder` <span class="v">6.1.4</span>
    - `spyder-kernels` <span class="v">3.1.4</span>
    - `SQLAlchemy` <span class="v">2.0.49</span>
    - `sqlparse` <span class="v">0.5.5</span>
    - `stack_data` <span class="v">0.6.3</span>
    - `starlette` <span class="v">1.0.0</span>
    - `statsmodels` <span class="v">0.14.6</span>
    - `stevedore` <span class="v">5.7.0</span>
    - `streamlit` <span class="v">1.56.0</span>
    - `superqt` <span class="v">0.8.0</span>
    - `sympy` <span class="v">1.14.0</span>
    - `tables` <span class="v">3.11.1</span>
    - `tabulate` <span class="v">0.10.0</span>
    - `tblib` <span class="v">3.2.2</span>
    - `tenacity` <span class="v">9.1.4</span>
    - `tensorboard` <span class="v">2.20.0</span>
    - `tensorboard_data_server` <span class="v">0.7.0</span>
    - `tensorboardX` <span class="v">2.6.2.2</span>
    - `terminado` <span class="v">0.18.1</span>
    - `text-unidecode` <span class="v">1.3</span>
    - `textdistance` <span class="v">4.6.3</span>
    - `threadpoolctl` <span class="v">3.6.0</span>
    - `three-merge` <span class="v">0.1.1</span>
    - `tifffile` <span class="v">2026.3.3</span>
    - `tinycss2` <span class="v">1.4.0</span>
    - `toml` <span class="v">0.10.2</span>
    - `tomli` <span class="v">2.4.1</span>
    - `tomlkit` <span class="v">0.14.0</span>
    - `toolz` <span class="v">1.1.0</span>
    - `tornado` <span class="v">6.5.5</span>
    - `tqdm` <span class="v">4.67.3</span>
    - `traitlets` <span class="v">5.14.3</span>
    - `typer` <span class="v">0.25.1</span>
    - `typing_extensions` <span class="v">4.15.0</span>
    - `typing-inspection` <span class="v">0.4.2</span>
    - `typing_utils` <span class="v">0.1.0</span>
    - `tzdata` <span class="v">2026.1</span>
    - `ujson` <span class="v">5.12.0</span>
    - `umap-learn` <span class="v">0.5.12</span>
    - `uncertainties` <span class="v">3.2.3</span>
    - `unicodedata2` <span class="v">17.0.1</span>
    - `uri-template` <span class="v">1.3.0</span>
    - `urllib3` <span class="v">2.6.3</span>
    - `uvicorn` <span class="v">0.44.0</span>
    - `uvloop` <span class="v">0.22.1</span>
    - `vasprun-xml` <span class="v">1.0.4</span>
    - `virtualenv` <span class="v">21.2.1</span>
    - `watchdog` <span class="v">6.0.0</span>
    - `watchfiles` <span class="v">1.1.1</span>
    - `wcwidth` <span class="v">0.6.0</span>
    - `webcolors` <span class="v">25.10.0</span>
    - `webencodings` <span class="v">0.5.1</span>
    - `websocket-client` <span class="v">1.9.0</span>
    - `websockets` <span class="v">16.0</span>
    - `Werkzeug` <span class="v">3.1.8</span>
    - `whatthepatch` <span class="v">1.0.7</span>
    - `wheel` <span class="v">0.46.3</span>
    - `widgetsnbextension` <span class="v">4.0.15</span>
    - `wrapt` <span class="v">2.1.2</span>
    - `wurlitzer` <span class="v">3.1.1</span>
    - `xarray` <span class="v">2026.4.0</span>
    - `xarray-einstats` <span class="v">0.10.0</span>
    - `xgboost` <span class="v">3.2.0</span>
    - `xlrd` <span class="v">2.0.2</span>
    - `xlwt` <span class="v">1.3.0</span>
    - `xmltodict` <span class="v">1.0.4</span>
    - `xyzservices` <span class="v">2026.3.0</span>
    - `yapf` <span class="v">0.43.0</span>
    - `yarl` <span class="v">1.23.0</span>
    - `zict` <span class="v">3.0.0</span>
    - `zipp` <span class="v">3.23.1</span>
    
    </div>

<style>
.pkg-table {
  margin-left: -1.6rem;
}
.pkg-table ul {
  list-style: none;
  padding-left: 0;
  margin: 0;
  font-size: 0.78rem;
}
.pkg-table li {
  display: flex;
  justify-content: space-between;
  gap: 12px;
  padding: 2px 8px 2px 0;
}
.pkg-table li .v {
  color: var(--md-default-fg-color--light);
}
</style>

If you find that some package is missing, you can often install it
yourself with `pip install --user`.  See [our Python
documentation](../support/tutorials/python-usage-guide.md#installing-python-packages-to-existing-modules)
for more information on how to install packages yourself.

It is also possible to use [Python virtual
environments](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment).
To create a virtual environment use the command `python3 -m venv
--system-site-packages venv`.

If you think that some important package should be included in the
module provided by CSC, please [contact our
servicedesk](../support/contact.md). Note that some machine learning
frameworks have their own specific modules, for example in Roihu:
[python-pytorch](pytorch.md), [python-vllm](vllm.md), [python-tensorflow](tensorflow.md), and [python-jax](jax.md).

!!! info "Note about multi-threading"

    Loading the `python-data` module will set the environment variable
    `OMP_NUM_THREADS=1`, which essentially disables OpenMP multi-threading
    support. This is a reasonable setting in most cases, and fixes some
    issues related to multi-processing runs. If you know that you need to
    use OpenMP multi-threading, please set this variable manually, for
    example in your Slurm job script:

        export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK


## License

All packages are licensed under various free and open source licenses (FOSS).

## Usage

To use this software on Roihu, initialize it with:

```text
module load python-data
```

to access the default version, or if you wish to have a specific version ([see
above for available versions](#available)):

```text
module load python-data/3.12-31.03   # on Roihu
```

If you just want the most recent version with a specific Python version, you can also run:

```text
module load python-data/3.12
```

This will show all available versions:

```text
module avail python-data
```

To check the exact packages and versions included in the loaded module you can run:

```text
list-packages
```

!!! warning

    Note that Roihu login nodes are not intended for heavy computing, please use
    slurm batch jobs instead. See our [instructions on how to use the batch job
    system](../computing/running/getting-started.md).

Please also check [CSC's general Python documentation](python.md).

### Local storage

All nodes in Roihu have fast local storage which is useful for
IO-intensive applications. See our [general instructions on how to
take the fast local storage into
use](../computing/running/creating-job-scripts-roihu.md#local-temporary-storage).
