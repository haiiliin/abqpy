# classes

class AbaqusBooleanType(int):
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


AbaqusBoolean = AbaqusBooleanType


class BooleanType(int):
    """
    bool(x) -> bool

    Returns True when the argument x is true, False otherwise.
    The builtins True and False are the only two instances of the class bool.
    The class bool is a subclass of the class int, and cannot be subclassed.
    """

    def __and__(self, y):  # real signature unknown; restored from __doc__
        """ x.__and__(y) <==> x&y """
        pass

    def __init__(self, *args, **kwargs):  # real signature unknown
        pass

    @staticmethod  # known case of __new__
    def __new__(S, *more):  # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __or__(self, y):  # real signature unknown; restored from __doc__
        """ x.__or__(y) <==> x|y """
        pass

    def __rand__(self, y):  # real signature unknown; restored from __doc__
        """ x.__rand__(y) <==> y&x """
        pass

    def __repr__(self):  # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    def __ror__(self, y):  # real signature unknown; restored from __doc__
        """ x.__ror__(y) <==> y|x """
        pass

    def __rxor__(self, y):  # real signature unknown; restored from __doc__
        """ x.__rxor__(y) <==> y^x """
        pass

    def __str__(self):  # real signature unknown; restored from __doc__
        """ x.__str__() <==> str(x) """
        pass

    def __xor__(self, y):  # real signature unknown; restored from __doc__
        """ x.__xor__(y) <==> x^y """
        pass


Boolean = BooleanType


class SymbolicConstantType(str):
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
    
    
SymbolicConstant = SymbolicConstantType