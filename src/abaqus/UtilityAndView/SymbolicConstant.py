from __future__ import annotations

from typing import Any, Union

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from .AbaqusBoolean import AbaqusBoolean


@abaqus_class_doc
class SymbolicConstant(str):
    """The SymbolicConstant object represents a string in a way that can be stored in a replay
    file and used as an argument to Abaqus Scripting Interface methods and functions. By
    convention the string representation of the SymbolicConstant object is the same as its
    variable name. If you pass a SymbolicConstant object to the Python repr() function, the
    function returns the text without quotes. In effect, the text is the variable that, by
    convention, refers to the SymbolicConstant object.
    Two SymbolicConstant objects with the same text are the same Python object, although you
    can assign them to different variables. All of the SymbolicConstant objects that are
    required in Abaqus Scripting Interface methods are defined in the abaqusConstants
    module. Some SymbolicConstant objects and the SymbolicConstant constructor are defined
    in the abaqus module. The SymbolicConstant constructor is also defined in the
    symbolicConstants module.

    .. note:: 
        This object can be accessed by::

            from symbolicConstants import *
            from abaqusConstants import *
    """

    @abaqus_method_doc
    def __init__(self, text: str) -> None:
        """The SymbolicConstant method creates a SymbolicConstant object.

        .. note:: 
            This function can be accessed by::

                SymbolicConstant

        Parameters
        ----------
        text
            A String specifying the text of the SymbolicConstant object. The String must contain
            only capital letters, digits, or underscores and must not start with a digit.

        Returns
        -------
        SymbolicConstant
            A :py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` object.
        """
        if not text.isupper() or not text.isidentifier():
            raise ValueError(f'SymbolicConstant name {text} may only contain upper case, digit or underscore')
        self.text = text

    @abaqus_method_doc
    def __copy__(self) -> SymbolicConstant:
        ...
    
    def __getstate__(self) -> str:
        return self.text
    
    def __hash__(self) -> int:
        ...
    
    def __lt__(self, other: Any) -> bool:
        """Sorting method; True if self is < other"""
        return self < other
    
    @abaqus_method_doc
    def __reduce__(self) -> tuple:  # known return case of __reduce__
        ...
    
    def __repr__(self) -> str: 
        return self.getText()
    
    def __setstate__(self, *args) -> None:
        ...
    
    def __str__(self) -> str:
        return self.text
    
    def getId(self) -> int:
        ...
    
    def getText(self) -> str:
        return self.text
    
    @staticmethod 
    def __new__(cls, name: str, *args, **kargs) -> Union[SymbolicConstant,AbaqusBoolean]:
        if name == "ON":
            return AbaqusBoolean(1)
        elif name == "OFF":
            return AbaqusBoolean(0)
        else:
            return super().__new__(cls)
    
    @classmethod
    def _addToCache(cls, *args, **kwargs):  # real signature unknown
        """
        Helper method for __new__
        Also used by AbaqusBoolean.__new__
        """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""