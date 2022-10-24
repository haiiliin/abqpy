# abqpy 2022

[![pytest](https://github.com/haiiliin/abqpy/actions/workflows/pytest.yml/badge.svg)](https://github.com/haiiliin/abqpy/actions/workflows/pytest.yml)
[![docs-test](https://github.com/haiiliin/abqpy/actions/workflows/docs-test.yml/badge.svg)](https://github.com/haiiliin/abqpy/actions/workflows/docs-test.yml)

Read this in other languages: [English](README.md), [简体中文](README-zh-cn.md).

Type hints for Abaqus/Python scripting

`abqpy` is a Python package providing type hints for Python scripting of Abaqus, you can 
use it to write your Python script of Abaqus fluently, even without doing anything in Abaqus. 
It also provides some simple APIs to execute the Abaqus commands so that you can run your 
Python script to build the model, submit the job and extract the output data in just one 
Python script, even without opening the Abaqus/CAE. 

- Homepage: [https://abqpy.com](https://abqpy.com)
- GitHub repository: [https://github.com/haiiliin/abqpy](https://github.com/haiiliin/abqpy)
- PyPI: [https://pypi.org/project/abqpy](https://pypi.org/project/abqpy)
- Anaconda: [https://anaconda.org/haiiliin/abqpy](https://anaconda.org/haiiliin/abqpy)
- Read the Docs: [https://readthedocs.org/projects/abqpy](https://readthedocs.org/projects/abqpy)
- Documentation: [https://docs.abqpy.com/en/latest](https://docs.abqpy.com/en/latest)
- Bug report: [https://github.com/haiiliin/abqpy/issues](https://github.com/haiiliin/abqpy/issues)

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
