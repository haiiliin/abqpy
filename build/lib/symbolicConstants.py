"""
symbolicConstants.py

Replacement for Abaqus symbolicConstants module.

Defines new style class SymbolicConstant (and SymbolicConstantType)
and AbaqusBoolean (and AbaqusBooleanType).

Defines TRUE, FALSE as Python Boolean objects (True, False).
Also defines an AbaqusBoolean, used for ON, and OFF.

Each SymbolicConstant object is a singleton.
The id of each SymbolicConstant is set in the constructor.

AbaqusBoolean is derived from int; there are 2 instances, ON and OFF.
The AbaqusBoolean objects are singletons, they are also in the same cache
as the SymbolicConstant objects.

The following applies to Abaqus/CAE only:

It is important that id's of Python SymbolicConstant objects are the same as
the id's of C++ omu_SymbolicConstantData objects in omu_SymbolicConstantTable.
It is prefereable that id's of SymbolicConstants are the same in Abaqus/CAE
kernel and GUI. To ensure that the id's of the SymbolicConstants in
abaqusConstants are the same in GUI and kernel of CAE, the _symConstCacheInit
module is imported in SMAPybPyoinitialize.
This creates all the SymbolicConstant objects in the abaqusConstants module,
and makes this module aware of the cache by adding the _addSymConstToTable
function to this module.
Outside Abaqus/CAE, we do not have the same requirement.
"""
from abaqusConstants import *