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

# imports
import re
import sys
import os

# Variables with simple values

FALSE = False

OFF = 0

ON = 1

TRUE = True

# classes

class AbaqusBoolean(int):
    """
    AbaqusBoolean is derived from int, and prints as ON or OFF.
        A call to SymbolicConstant("ON/OFF") will return an AbaqusBoolean instance.
    """

    def getId(self, *args, **kwargs):  # real signature unknown
        pass

    def getText(self, *args, **kwargs):  # real signature unknown
        pass

    def isTrue(self, *args, **kwargs):  # real signature unknown
        pass

    def __copy__(self, *args, **kwargs):  # real signature unknown
        pass

    def __getstate__(self, *args, **kwargs):  # real signature unknown
        pass

    def __hash__(self, *args, **kwargs):  # real signature unknown
        pass

    def __init__(self, *args, **kwargs):  # real signature unknown
        pass

    @staticmethod  # known case of __new__
    def __new__(cls, *args, **kargs):  # reliably restored by inspect
        # no doc
        pass

    def __reduce__(self, *args, **kwargs):  # real signature unknown
        pass

    def __repr__(self, *args, **kwargs):  # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs):  # real signature unknown
        pass

    def __str__(self, *args, **kwargs):  # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""

    _abaqusBooleanOFF = 0
    _abaqusBooleanON = 1
    __dict__ = None  # (!) real value is 'dict_proxy({\'__module__\': \'symbolicConstants\', \'isTrue\': <function isTrue at 0x00000000031652E8>, \'__setstate__\': <function __setstate__ at 0x00000000031653C8>, \'__str__\': <function getText at 0x0000000003165208>, \'__reduce__\': <function __reduce__ at 0x00000000031654A8>, \'getText\': <function getText at 0x0000000003165208>, \'__dict__\': <attribute \'__dict__\' of \'AbaqusBoolean\' objects>, \'_abaqusBooleanON\': ON, \'__weakref__\': <attribute \'__weakref__\' of \'AbaqusBoolean\' objects>, \'_abaqusBooleanOFF\': OFF, \'__copy__\': <function __copy__ at 0x0000000003165438>, \'__new__\': <staticmethod object at 0x000000000314E6A8>, \'getId\': <function getId at 0x0000000003165278>, \'__init__\': <function __init__ at 0x0000000003165128>, \'__hash__\': <function __hash__ at 0x0000000003165198>, \'__getstate__\': <function __getstate__ at 0x0000000003165358>, \'__doc__\': \'\\n    AbaqusBoolean is derived from int, and prints as ON or OFF.\\n    A call to SymbolicConstant("ON/OFF") will return an AbaqusBoolean instance.\\n    \', \'__repr__\': <function getText at 0x0000000003165208>})'


AbaqusBooleanType = AbaqusBoolean

BooleanType = bool

Boolean = BooleanType


class SymbolicConstant(str):
    """
    SymbolicConstant(name <,scdId=-1>)
        Abaqus/CAE SymbolicConstant implemented in Python.
        SymbolicConstant('ON'|'OFF') will return an AbaqusBoolean instance.
    """

    def getId(self, *args, **kwargs):  # real signature unknown
        pass

    def getText(self, *args, **kwargs):  # real signature unknown
        pass

    @classmethod
    def _addToCache(cls, *args, **kwargs):  # real signature unknown
        """
        Helper method for __new__
                Also used by AbaqusBoolean.__new__
        """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""

    # _cache = {
    #     'ALL_METHODS': ALL_METHODS,  # (!) forward: ALL_METHODS, real value is 'ALL_METHODS'
    #     'ALL_TYPES': ALL_TYPES,  # (!) forward: ALL_TYPES, real value is 'ALL_TYPES'
    #     'BOTH': BOTH,  # (!) forward: BOTH, real value is 'BOTH'
    #     'EARLIEST': EARLIEST,  # (!) forward: EARLIEST, real value is 'EARLIEST'
    #     'GUI': GUI,  # (!) forward: GUI, real value is 'GUI'
    #     'KERNEL': KERNEL,  # (!) forward: KERNEL, real value is 'KERNEL'
    #     'LATEST': LATEST,  # (!) forward: LATEST, real value is 'LATEST'
    #     'OFF': 0,
    #     'ON': 1,
    #     '_UNSPECIFIED': _UNSPECIFIED,
    # }
    _counter = 10
    _p = None  # (!) real value is '<_sre.SRE_Pattern object at 0x0000000003106D40>'
    __dict__ = None  # (!) real value is 'dict_proxy({\'__module__\': \'symbolicConstants\', \'__setstate__\': <function __setstate__ at 0x000000000314FDD8>, \'__str__\': <function getText at 0x000000000314FF28>, \'__reduce__\': <function __reduce__ at 0x000000000314FEB8>, \'getText\': <function getText at 0x000000000314FF28>, \'__dict__\': <attribute \'__dict__\' of \'SymbolicConstant\' objects>, \'_cache\': {\'_UNSPECIFIED\': _UNSPECIFIED, \'ON\': ON, \'OFF\': OFF, \'ALL_TYPES\': ALL_TYPES, \'BOTH\': BOTH, \'GUI\': GUI, \'ALL_METHODS\': ALL_METHODS, \'EARLIEST\': EARLIEST, \'KERNEL\': KERNEL, \'LATEST\': LATEST}, \'__lt__\': <function __lt__ at 0x000000000314FC88>, \'__weakref__\': <attribute \'__weakref__\' of \'SymbolicConstant\' objects>, \'__init__\': <function __init__ at 0x000000000314FC18>, \'_counter\': 10, \'__getstate__\': <function __getstate__ at 0x000000000314FD68>, \'__new__\': <staticmethod object at 0x000000000314E678>, \'getId\': <function getId at 0x000000000314FF98>, \'_p\': <_sre.SRE_Pattern object at 0x0000000003106D40>, \'__repr__\': <function getText at 0x000000000314FF28>, \'__hash__\': <function __hash__ at 0x000000000314FCF8>, \'__copy__\': <function __copy__ at 0x000000000314FE48>, \'_addToCache\': <classmethod object at 0x000000000314E5E8>, \'__doc__\': "\\n    SymbolicConstant(name <,scdId=-1>)\\n    Abaqus/CAE SymbolicConstant implemented in Python.\\n    SymbolicConstant(\'ON\'|\'OFF\') will return an AbaqusBoolean instance.\\n    "})'
    
    
SymbolicConstantType = SymbolicConstant