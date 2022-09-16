# abqpy 2016

[![Documentation Status](https://img.shields.io/readthedocs/abqpy?label=docs)](https://readthedocs.org/projects/abqpy/)
[![Documentation Status](https://img.shields.io/readthedocs/abqpy-zh-cn?label=docs-zh-cn)](https://readthedocs.org/projects/abqpy-zh-cn/)
[![Tests](https://github.com/haiiliin/abqpy/actions/workflows/tests.yaml/badge.svg)](https://github.com/haiiliin/abqpy/actions/workflows/tests.yaml)
[![CodeQL](https://github.com/haiiliin/abqpy/actions/workflows/codeql.yml/badge.svg)](https://github.com/haiiliin/abqpy/actions/workflows/codeql.yml)
[![Total alerts](https://img.shields.io/lgtm/alerts/g/haiiliin/abqpy.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/haiiliin/abqpy/alerts/)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/haiiliin/abqpy.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/haiiliin/abqpy/context:python)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/abqpy.svg)](https://www.python.org/)
[![GitHub release (latest by date)](https://img.shields.io/github/v/release/haiiliin/abqpy)](https://github.com/haiiliin/abqpy/releases/latest)
[![PyPI download month](https://img.shields.io/pypi/dm/abqpy.svg?color=blue)](https://pypi.python.org/pypi/abqpy/)

其它语言版本: [English](README.md), [简体中文](README-zh-cn.md).

Abaqus/Python 脚本的类型提示

`abqpy` 是一个 Python 包，为 Abaqus 的 Python 脚本提供类型提示，您可以使用它方便地编写 Abaqus Python 脚本。 
它还提供了一些简单的 API 来执行 Abaqus 命令，以便您可以运行 Python 脚本来创建模型、
提交作业并提取输出数据，即使不打开 Abaqus/CAE。

## 该项目的其他链接

- GitHub 仓库: [github.com/haiiliin/abqpy](https://github.com/haiiliin/abqpy)
- PyPI: [pypi.org/project/abqpy](https://pypi.org/project/abqpy/)
- Anaconda: [anaconda.org/haiiliin/abqpy](https://anaconda.org/haiiliin/abqpy)
- Read the Docs: [readthedocs.org/projects/abqpy](https://readthedocs.org/projects/abqpy/)
- 中文文档: [abqpy.haiiliin.com/zh_CN/latest](https://abqpy.haiiliin.com/zh_CN/latest/)

## 欢迎拉取合并请求

由于`abqpy`是从 Abaqus 官方文档中重构出来的，很多文档字符串的格式还不完善，比如
数学方程，对象的属性，由于我的时间有限，这些东西还没有完成，如果有人愿意做出任何贡献，
请随时创建您的拉取请求。

## 安装

`abqpy` 支持 Python 3.7 或更高的版本。 如果您使用的是 Python 3.6 或更早的版本，请升级到 Python 3.7 或更高版本。

`abqpy` 已经被上传到 [PyPI](https://pypi.org/project/abqpy)，你可以简单地使用 `pip` 进行安装：
```shell
pip install abqpy
```

`abqpy`也已经上传到 [anaconda](https://anaconda.org/haiiliin/abqpy)，你可以使用 `conda` 来安装：
```shell
conda install -c haiiliin abqpy
```

您也可以通过克隆 [GitHub 仓库](https://github.com/haiiliin/abqpy) 来安装最新的版本，
并使用 `python` 从本地目录安装：

```shell
git clone https://github.com/haiiliin/abqpy.git
cd abqpy
pip install -r requirements.txt
python setup.py install
```

## 安装特定的版本

您可以在安装 `abqpy` 时指定版本号，例如：
```shell
pip install abqpy==2016.3.2
conda install -c haiiliin abqpy=2016.3.2
```
更好的方法是使用 * 来匹配特定版本：
```shell
pip install abqpy==2016.*
```

## 可选依赖

您可以将 Abaqus/Python 脚本放入 Jupyter Notebook。 当您运行该 Notebook 时，
`abqpy` 会将该 Notebook 转换为具有相同名称 `.ipynb` 文件，然后将其提交给 Abaqus。

访问 [案例页](examples) 查看使用 Jupyter Notebook 创建 Abaqus 模型的案例。
 
为了使用 **Jupyter Notebook** 功能，您必须安装 `ipynbname`：
```shell
pip install ipynbname 
```

## 设置 Abaqus 环境

为了使用 Abaqus 命令执行 Python 脚本并提交作业，您需要告诉 `abqpy` 
Abaqus 命令所在的位置。 通常，Abaqus 命令位于如下目录中：

```
C:/SIMULIA/Commands/abaqus.bat
```

您可以将目录 `C:/SIMULIA/Commands` 添加到系统环境变量 `Path` 中，也可以创建一个名为 
`ABAQUS_BAT_PATH` 的新系统变量，并将值设置为 Abaqus 命令的文件路径，即 
`C:/SIMULIA/Commands/abaqus.bat`。

## 截图

- 创建 Abaqus 模型

  ![Model](docs/source/images/model-code.gif "Create an Abaqus Model")

- 读取输出数据

  ![Output](docs/source/images/output-code.gif "Extract Output Data")

## 更多

更详细使用请参考 [文档](https://abqpy.haiiliin.com/)。
