# Executing a script that accesses an output database

If your script accesses and manipulates data in an output database, you can use either of the following methods to execute the script:

- Type abaqus python **scriptname.py** at the system prompt.
- Select **File -> Run Script** from the Abaqus/CAE main menu bar, and select the file to execute.

Your script must contain the following statement:

```python2
from odbAccess import *
```

In addition, if your script refers to any of the Symbolic Constants defined in the Abaqus Scripting Interface, your script must contain the following statement:

```python2
from abaqusConstants import *
```

If your script accesses or creates material objects, or if it accesses or creates section or beam profile objects, it must contain the following statements, respectively:

```python2
from odbMaterial import *
from odbSection import *
```
