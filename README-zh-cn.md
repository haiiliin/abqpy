# abqpy 2017

[![tests](https://github.com/haiiliin/abqpy/actions/workflows/tests.yml/badge.svg)](https://github.com/haiiliin/abqpy/actions/workflows/tests.yml)
[![rtd](https://readthedocs.org/projects/abqpy/badge/?version=latest)](https://readthedocs.org/projects/abqpy/)
[![coveralls](https://coveralls.io/repos/github/haiiliin/abqpy/badge.svg?branch=2017)](https://coveralls.io/github/haiiliin/abqpy?branch=2017)
[![python](https://img.shields.io/badge/Python-3.7%2B-brightgreen)](https://www.python.org/downloads/)
[![abaqus](https://img.shields.io/badge/Abaqus-2016%2B-brightgreen)](https://www.3ds.com/products-services/simulia/products/abaqus/)
[![Crowdin](https://badges.crowdin.net/abqpy-locale/localized.svg)](https://crowdin.com/project/abqpy-locale)

其它语言版本: [English](README.md), [简体中文](README-zh-cn.md).

Abaqus/Python 脚本的类型提示

`abqpy` 是一个 Python 包，为 Abaqus 的 Python 脚本提供类型提示，您可以使用它方便地编写 Abaqus Python 脚本。
它还提供了一些简单的 API 来执行 Abaqus 命令，以便您可以运行 Python 脚本来创建模型、
提交作业并提取输出数据，即使不打开 Abaqus/CAE。

- GitHub 仓库: [https://github.com/haiiliin/abqpy](https://github.com/haiiliin/abqpy)
- PyPI: [https://pypi.org/project/abqpy](https://pypi.org/project/abqpy)
- 中文文档: [https://docs.abqpy.com/en/stable](https://docs.abqpy.com/zh_CN/stable)

## 快速开始

确保 <a href="https://www.python.org/downloads/"> <img src="https://img.shields.io/badge/Python-3.7%2B-brightgreen" align=center /> </a> 和
<a href="https://www.3ds.com/products-services/simulia/products/abaqus/"> <img src="https://img.shields.io/badge/Abaqus-2016%2B-brightgreen" align=center /> </a>
已经安装成功，然后打开 `cmd` 或者 `terminal`，输入：

```
pip install abqpy==2017.*  # 将主版本号替换为你的 Abaqus 版本号
```

然后，在你喜欢的开发环境中使用 Python 3.7+ 运行你的 Abaqus/Python 脚本，看看奇迹如何发生。
更多信息，请参阅 [文档](https://docs.abqpy.com/zh_CN/stable).

## 欢迎拉取合并请求

由于`abqpy`是从 Abaqus 官方文档中重构出来的，很多文档字符串的格式还不完善，比如
数学方程，对象的属性，由于我的时间有限，这些东西还没有完成，如果有人愿意做出任何贡献，
请随时创建您的拉取请求。

请参阅 [CONTRIBUTING](https://github.com/haiiliin/abqpy/blob/main/.github/CONTRIBUTING.md) 了解贡献指南.

## 截图

![screenshot](https://raw.githubusercontent.com/haiiliin/abqpy/main/docs/source/images/model-code.gif)

![screenshot](https://raw.githubusercontent.com/haiiliin/abqpy/main/docs/source/images/output-code.gif)
