# Class References

Before you can access the Abaqus model and output database, you need to import some modules. In most cases, `abaqus`, `abaqusConstants`, and `driverUtils` are required:

```python
from abaqus import *
from abaqusConstants import *
from driverUtils import *
```

In the module `abaqus`, two important objects are provided, `mdb` and `session`, which represent the Abaqus model database and a object controls the Abaqus options.

- The `mdb` object is the high-level Abaqus model database. A model database stores models and analysis controls. For more information about the `mdb` object, see {doc}`/mdb API Reference <../reference/mdb>`.
- The `odb` object is the in-memory representation of an output database (ODB) file. For more information about the `odb` object, see  {doc}`/odb API Reference <../reference/odb>`.
- The `session` object has no constructor. Abaqus creates the session member when a session is started. For more information about the `session` object, see {doc}`/session API Reference <../reference/session>`.

In the module `abaqusConstants`, all the constant strings used in the Abaqus modeling are provided such as `THREE_D` (which specifies a 3-D model), for more constant strings, please refer to the API reference.

In the module `driverUtils`, an important function `executeOnCaeStartup` is implemented, this function will be execute each time we open the Abaqus, so we need to call this function in our Python script.

```python
executeOnCaeStartup()
```

Other modules like `field`, `material`, `mesh` can be imported whenever required.

```{toctree}
:caption: Modules
:maxdepth: 1

reference/mdb
reference/odb
reference/session
reference/kernel
```
