---
hero: Type hints for Abaqus/Python scripting
---

# abqpy documentation

Type hints for Abaqus/Python scripting.

`abqpy` is a Python package providing type hints for Python scripting of Abaqus, you can
use it to write you Python script of Abaqus fluently, even without doing anything in Abaqus.
It also provides some simple APIs to execute the Abaqus commands so that you can run your
Python script to build the model, submit the job and extract the output data in just one
Python script, even without opening the Abaqus/CAE.

```{note}
The abqpy is built in Python 3 but the Python interpreter of Abaqus is Python 2, so you
must write codes that are compatiable with Python 2 and Python 3.
```

# Contents

```{toctree}
:caption: User Manual
:maxdepth: 1

getting_started
envvars
cli
```

```{toctree}
:caption: Tutorials & Examples
:maxdepth: 1

tutorials
examples/index
```

```{toctree}
:caption: References
:maxdepth: 1

user/index
reference/index
CHANGES
autoapi/index
localization
```

```{toctree}
:caption: Policy & License
:maxdepth: 1
:hidden:

policy
```

# Indices and tables

- {ref}`genindex`
- {ref}`modindex`
- {ref}`search`
