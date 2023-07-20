# Abaqus Scripting Interface data types

This section describe the most common Abaqus Scripting Interface data type The standard {ref}`python-data-types` described in Python data types include integers, floats, strings, and sequences. The Abaqus Scripting Interface adds over 500 additional data types.

## SymbolicConstants

Some arguments require that you provide a SymbolicConstant. SymbolicConstants are defined by the Abaqus Scripting Interface and are written in all capital letters. If your script uses a SymbolicConstant defined by the Abaqus Scripting Interface, you must import the SymbolicConstant with the following statement before you refer to it:

```python2
from abaqusConstants import *
```

When an argument to a command is a SymbolicConstant, the description in the {doc}`/reference/index` lists all its possible values. For example, when you are printing an image, the image can be rendered in one of the following formats: BLACK_AND_WHITE, GREYSCALE, or COLOR.

Similarly, a data member can be a SymbolicConstant. For example, the type member of the Elastic object can be one of the following SymbolicConstants: ISOTROPIC, ORTHOTROPIC, ANISOTROPIC, ENGINEERING_CONSTANTS, LAMINA, TRACTION, or COUPLED_TRACTION.

If the SymbolicConstants provided by the Abaqus Scripting Interface do not meet your needs, you can create your own SymbolicConstants using the SymbolicConstant constructor. For more information, see SymbolicConstant object.

## Booleans

Python defines two Boolean values, True and False. The type of a Python Boolean is \<type 'bool'>.

```python2
myPythonBoolean = True
type(myPythonBoolean)
<type 'bool'>
```

In addition, the Abaqus Scripting Interface defines a Boolean object, derived from the SymbolicConstant object, which can take the values ON and OFF. For example, `noPartsInputFile` is a member of a Model object that indicates whether the input file will be written with parts and assemblies. The type of the `noPartsInputFile` member is \<type 'AbaqusBoolean'>.

Abaqus recommends that you use the Python Boolean in your scripts and that you convert existing scripts to use the Python Boolean.

The value of a Boolean argument can appear to be ambiguous; for example,

```python2
newModel = mdb.ModelFromInputFile(name='beamTutorial',
    inputFileName='Deform')
newModel.setValues(noPartsInputFile=False)
print newModel.noPartsInputFile
OFF
```

Because of this ambiguity, you should test a Boolean for a positive or negative value, as opposed to comparing it to a specific value like 0, OFF, or False. For example, the following statements show how you should test the value of a Boolean member:

```python2
if (newModel.noPartsInputFile):
    print 'Input file will be written without parts and assemblies. '
else:
    print 'Input file will be written with parts and assemblies.'
```

(repositories)=

## Repositories

Repositories are containers that store a particular type of object; for example, the steps repository contains all the steps defined in the model. A repository maps to a set of information and is similar to a Python dictionary; for more information, see {ref}`using-dictionaries`. However, only a constructor can add an object to a repository. In addition, all the objects in a repository are of the same type. For example, the following repository contains all the models in the model database:

```python2
mdb.models
```

In turn, the following repository contains all the parts in the model `Model-1`:

```python2
mdb.models['Model-1'].parts
```

As with dictionaries, you can refer to an object in a repository using its key. The key is typically the name you provided in the constructor command when the object was created. For example, the Viewport constructor creates a new Viewport object in the viewports repository.

```python2
session.Viewport(name='Side view',
    origin = (10,10), width=50, height=50)
```

The key to this new Viewport object in the viewports repository is Side view. You use this key to access this particular Viewport object. For example,

```python2
session.viewports['Side view'].viewportAnnotationOptions.setValues(legend=OFF, title=OFF)
```

You can make your scripts more readable by assigning a variable to an object in a repository. For example, you could rewrite the previous statement after assigning the Viewport object to the variable myViewport:

```python2
myViewport = session.viewports['Side view']
myViewport.viewportAnnotationOptions.setValues(
    legend=OFF, title=OFF)
```

In general, if the user can create the object, its repository key is a string. In some cases Abaqus/CAE creates an object, and the key can be a string, an integer, or a SymbolicConstant.

As with dictionaries, you can use the keys() method to access the repository keys.

```python2
>>> session.Viewport(name='Side view')
>>> session.Viewport(name='Top view')
>>> session.Viewport(name='Front view')
>>> for key in session.viewports.keys():
        ...
        print key
Front view
Top view
Side view
```

You can use the `keys()[i]` method to access an individual key; however, most repositories are not ordered, and this is not recommended.

You can use the `changeKey()` method to change the name of a key in a repository. For example,

```python2
myPart = mdb.models['Model-1'].Part(name='housing',
    dimensionality=THREE_D, type=DEFORMABLE_BODY)
mdb.models['Model-1'].parts.changeKey(fromName='housing', toName='form')
```
