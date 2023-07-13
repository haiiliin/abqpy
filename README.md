# abqpy 2022

[![tests](https://github.com/haiiliin/abqpy/actions/workflows/tests.yml/badge.svg)](https://github.com/haiiliin/abqpy/actions/workflows/tests.yml)
[![rtd](https://readthedocs.org/projects/abqpy/badge/?version=latest)](https://readthedocs.org/projects/abqpy/)
[![coveralls](https://coveralls.io/repos/github/haiiliin/abqpy/badge.svg?branch=2022)](https://coveralls.io/github/haiiliin/abqpy?branch=2022)
[![python](https://img.shields.io/badge/Python-3.7%2B-brightgreen)](https://www.python.org/downloads/)
[![abaqus](https://img.shields.io/badge/Abaqus-2016%2B-brightgreen)](https://www.3ds.com/products-services/simulia/products/abaqus/)
[![Crowdin](https://badges.crowdin.net/abqpy-locale/localized.svg)](https://crowdin.com/project/abqpy-locale)

Read this in other languages: [English](README.md), [简体中文](README-zh-cn.md).

Type hints for Abaqus/Python scripting

`abqpy` is a Python package providing type hints for Python scripting of Abaqus, you can
use it to write your Python script of Abaqus fluently, even without doing anything in Abaqus.
It also provides some simple APIs to execute the Abaqus commands so that you can run your
Python script to build the model, submit the job and extract the output data in just one
Python script, even without opening the Abaqus/CAE.

- GitHub repository: [https://github.com/haiiliin/abqpy](https://github.com/haiiliin/abqpy)
- PyPI: [https://pypi.org/project/abqpy](https://pypi.org/project/abqpy)
- Documentation: [https://docs.abqpy.com/en/stable](https://docs.abqpy.com/en/stable)

## Quick Start

Make sure <a href="https://www.python.org/downloads/"> <img src="https://img.shields.io/badge/Python-3.7%2B-brightgreen" align=center /> </a> and
<a href="https://www.3ds.com/products-services/simulia/products/abaqus/"> <img src="https://img.shields.io/badge/Abaqus-2016%2B-brightgreen" align=center /> </a>
are installed on your computer,
open `cmd` or `terminal`, type:

```
pip install abqpy==2022.*  # change the major version to match your Abaqus version
```

Then, open your Abaqus/Python script in your favorite IDE with Python language support,
run the script with Python 3.7+ (just do it!), see the magic happens.
For more information, please refer to the [documentation](https://docs.abqpy.com/en/stable).

## Pull Requests are Welcome

Since `abqpy` is reconstructed from the official Abaqus documentation,
many of the docstrings are not well formatted, for example, the Raises section,
the math equations, the attributes of the objects, due to the limitation of
my time, those things are left behind, if anyone is willing to make any
contributions, please feel free to create your pull requests.

Please refer [CONTRIBUTING](https://github.com/haiiliin/abqpy/blob/main/.github/CONTRIBUTING.md) for contribution guidelines.

## Screenshots

![screenshot](https://raw.githubusercontent.com/haiiliin/abqpy/main/docs/source/images/model-code.gif)

![screenshot](https://raw.githubusercontent.com/haiiliin/abqpy/main/docs/source/images/output-code.gif)
