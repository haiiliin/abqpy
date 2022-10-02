---
title: "Getting Started"
---

## Installation

### Prerequisites

`abqpy` supports Python 3.7 or a later version. If you are using Python 3.6 or an earlier version, please upgrade to Python 3.7 
or a later version.

### Install with pip

`abqpy` is uploaded to [PyPI](https://pypi.org/project/abqpy), you can simply install 
it using `pip`:
```shell
pip install abqpy
```

### Install with conda

`abqpy` is also uploaded to [anaconda](https://anaconda.org/haiiliin/abqpy), you can use 
`conda` to install it:
```shell
conda install -c haiiliin abqpy
```

### Install from source

You may install the latest development version by cloning the 
[GitHub repository](https://github.com/haiiliin/abqpy) and use `python` to install from 
the local directory:

```shell
git clone https://github.com/haiiliin/abqpy.git
cd abqpy
pip install -r requirements.txt
python setup.py install
```

### Install A Specific Version

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

### Optional Requirements

You can put your Abaqus/Python script into a Jupyter Notebook.
When you run the notebook, the package will convert the notebook into a plain Python file 
with the same name but with `.py` suffix instead of `.ipynb`, and then it will be submitted 
to Abaqus kernel. 

Go [examples](https://github.com/haiiliin/abqpy/tree/main/examples) for examples 
using Jupyter Notebooks to build the Abaqus model.
 
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

  ![Model](/images/model-code.gif "Create an Abaqus Model")

- Extract Output Data

  ![Output](/images/output-code.gif "Extract Output Data")

## Explore more

For detailed usage of this package, please refer to the [documentation](https://docs.abqpy.com/).
