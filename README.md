# abqpy 2018a6

[![OSCS Status](https://www.oscs1024.com/platform/badge/haiiliin/abqpy.svg?size=small)](https://www.oscs1024.com/project/haiiliin/abqpy?ref=badge_small)
[![Documentation Status](https://readthedocs.org/projects/abqpy/badge/?version=latest)](https://readthedocs.org/projects/abqpy)
[![Pages](https://github.com/haiiliin/abqpy/actions/workflows/pages.yaml/badge.svg)](https://github.com/haiiliin/abqpy/actions/workflows/pages.yaml)
[![Upload Python Package to PyPI](https://github.com/haiiliin/abqpy/actions/workflows/python-publish-pypi.yml/badge.svg)](https://github.com/haiiliin/abqpy/actions/workflows/python-publish-pypi.yml)
[![Build and Upload Conda Package](https://github.com/haiiliin/abqpy/actions/workflows/python-publish-conda.yml/badge.svg)](https://github.com/haiiliin/abqpy/actions/workflows/python-publish-conda.yml)

[![PyPI license](https://img.shields.io/pypi/l/ansicolortags.svg)](https://github.com/haiiliin/abqpy/blob/main/LICENSE)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/abqpy.svg)](https://www.python.org/)
[![Anaconda platforms](https://anaconda.org/haiiliin/abqpy/badges/platforms.svg)](https://anaconda.org/haiiliin/abqpy)
[![GitHub release](https://img.shields.io/github/release/haiiliin/abqpy.svg)](https://GitHub.com/haiiliin/abqpy/releases/)
[![PyPI download month](https://img.shields.io/pypi/dm/abqpy.svg)](https://pypi.python.org/pypi/abqpy/)

Migrating pyabaqus to abqpy.

Type hints for Abaqus/Python scripting

`abqpy` is a Python package providing type hints for Python scripting of Abaqus, you can 
use it to write your Python script of Abaqus fluently, even without doing anything in Abaqus. 
It also provides some simple APIs to execute the Abaqus commands so that you can run your 
Python script to build the model, submit the job and extract the output data in just one 
Python script, even without opening the Abaqus/CAE. 

## Other links for this project

- GitHub repository: [github.com/haiiliin/abqpy](https://github.com/haiiliin/abqpy)
- PyPI: [pypi.org/project/abqpy](https://pypi.org/project/abqpy/)
- Anaconda: [anaconda.org/haiiliin/abqpy](https://anaconda.org/haiiliin/abqpy)
- Read the Docs: [readthedocs.org/projects/abqpy](https://readthedocs.org/projects/abqpy/)
- Documentation: [abqpy.haiiliin.com](https://abqpy.haiiliin.com/en/latest/)

## Pull Requests are Welcome

Since `abqpy` is reconstructed from the official Abaqus documentation,
many of the docstrings are not well formatted, for example, the Raises section, 
the math equations, the attributes of the objects, due to the limitation of 
my time, those things are left behind, if anyone is willing to make any 
contributions, please feel free to create your pull requests.

## Installation

`abqpy` is using type hints features that require Python 3.9 or a later version, 
please upgrade it to Python 3.9 or a later version if you are using an earlier version.

`abqpy` is uploaded to [PyPI](https://pypi.org/project/abqpy), you can simply install 
it using pip:
```shell
pip install abqpy
```

`abqpy` is also uploaded to [anaconda](https://anaconda.org/haiiliin/abqpy), you can use 
`conda` to install it:
```shell
conda install -c haiiliin abqpy
```

## Optional Requirements

You can put your Abaqus/Python script into a Jupyter Notebook.
When you run the notebook, the package will convert the notebook into a plain Python file 
with the same name but with `.py` suffix instead of `.ipynb`, and then it will be submitted 
to Abaqus kernel. 

Go [github.com/haiiliin/abqpy/tree/main/examples](https://github.com/haiiliin/abqpy/tree/main/examples)
for tests using Jupyter Notebooks to build the Abaqus model.
 
In order to use the **Jupyter Notebook** feature, you have to install the following packages:
```shell
pip install ipynbname  # to read the file name of the notebook
pip install notebook
pip install jupyterlab
```
Or use `conda` to install (the `ipynbname` package is only distributed in `PyPI`, 
so you have to install it using `pip`):
```shell
conda install jupyterlab
conda install jupyter notebook
```

Try the following command to make sure the `jupyter` command is available. 
```shell
jupyter --version
```

You may install the latest development version by cloning the 
[GitHub repository](https://github.com/haiiliin/abqpy) and use `python` to install from 
the local directory:

```shell
git clone https://github.com/haiiliin/abqpy.git
cd abqpy
python setup.py install
```

## Setup Abaqus Environment

In order to use Abaqus command to execute the Python script and submit the job, you need to tell
`abqpy` where the Abaqus command is located. Usually, Abaqus command locates in a directory like this:

```
C:/SIMULIA/Commands/abaqus.bat
```

You can add the directory `C:/SIMULIA/Commands` to the system environment variable `Path`, or you can create a new
system variable named `ABAQUS_BAT_PATH`, and set the value to the file path of the Abaqus command, i.e.,
`C:/SIMULIA/Commands/abaqus.bat`.

## Screenshots

- Create an Abaqus Model

  ![Model](https://github.com/haiiliin/abqpy/blob/main/docs/source/images/model-code.gif "Create an Abaqus Model")

- Extract Output Data

  ![Output](https://github.com/haiiliin/abqpy/blob/main/docs/source/images/output-code.gif "Extract Output Data")

## Explore more

For detailed usage of this package, please refer to the [documentation](https://haiiliin.com/abqpy/).
