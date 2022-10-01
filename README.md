# abqpy 2022

[![Documentation Status](https://img.shields.io/readthedocs/abqpy?label=docs)](https://readthedocs.org/projects/abqpy/)
[![Documentation Status](https://img.shields.io/readthedocs/abqpy-zh-cn?label=docs-zh-cn)](https://readthedocs.org/projects/abqpy-zh-cn/)
[![pytest](https://github.com/haiiliin/abqpy/actions/workflows/pytest.yml/badge.svg)](https://github.com/haiiliin/abqpy/actions/workflows/pytest.yml)
[![docs-test](https://github.com/haiiliin/abqpy/actions/workflows/docs-test.yml/badge.svg)](https://github.com/haiiliin/abqpy/actions/workflows/docs-test.yml)
[![CodeQL](https://github.com/haiiliin/abqpy/actions/workflows/codeql.yml/badge.svg)](https://github.com/haiiliin/abqpy/actions/workflows/codeql.yml)

Read this in other languages: [English](README.md), [简体中文](README-zh-cn.md).

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
- Documentation: [docs.abqpy.com](https://docs.abqpy.com/en/latest/)

## Pull Requests are Welcome

Since `abqpy` is reconstructed from the official Abaqus documentation,
many of the docstrings are not well formatted, for example, the Raises section, 
the math equations, the attributes of the objects, due to the limitation of 
my time, those things are left behind, if anyone is willing to make any 
contributions, please feel free to create your pull requests.

## Installation

`abqpy` supports Python 3.7 or a later version. If you are using Python 3.6 or an earlier version, please upgrade to Python 3.7 
or a later version.

`abqpy` is uploaded to [PyPI](https://pypi.org/project/abqpy), you can simply install 
it using `pip`:
```shell
pip install abqpy
```

`abqpy` is also uploaded to [anaconda](https://anaconda.org/haiiliin/abqpy), you can use 
`conda` to install it:
```shell
conda install -c haiiliin abqpy
```

You may install the latest development version by cloning the 
[GitHub repository](https://github.com/haiiliin/abqpy) and use `python` to install from 
the local directory:

```shell
git clone https://github.com/haiiliin/abqpy.git
cd abqpy
pip install -r requirements.txt
python setup.py install
```

## Install A Specific Version

You can specify the version number when installing `abqpy`, for example:

Using `pip`:
```shell
pip install abqpy==2022.3.5
```
Using `conda`:
```shell
conda install -c haiiliin abqpy=2022.3.5
```
A better way is to use * to match specific version:
```shell
pip install abqpy==2022.*
```

## Optional Requirements

You can put your Abaqus/Python script into a Jupyter Notebook.
When you run the notebook, the package will convert the notebook into a plain Python file 
with the same name but with `.py` suffix instead of `.ipynb`, and then it will be submitted 
to Abaqus kernel. 

Go [examples](examples) for tests using Jupyter Notebooks to build the Abaqus model.
 
In order to use the **Jupyter Notebook** feature, you have to install `ipynbname`:
```shell
pip install ipynbname
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

  ![Model](docs/source/images/model-code.gif "Create an Abaqus Model")

- Extract Output Data

  ![Output](docs/source/images/output-code.gif "Extract Output Data")

## Explore more

For detailed usage of this package, please refer to the [documentation](https://docs.abqpy.com/).
