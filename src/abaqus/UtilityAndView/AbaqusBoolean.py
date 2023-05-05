from __future__ import annotations

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc


@abaqus_class_doc
class AbaqusBoolean(int):
    """The AbaqusBoolean object is used in a similar way to the SymbolicConstant object. If you pass an
    AbaqusBoolean object to the Python repr() function, the function returns the text without quotes. In effect,
    the text is the variable that, by convention, refers to the AbaqusBoolean object. An AbaqusBoolean object
    has a value of 0 or 1, and an AbaqusBoolean object can be tested in an if statement. You can use an
    AbaqusBoolean object as an argument to a method in place of 1 or 0. Conversely, you can pass a 0 or a 1 to
    an Abaqus Scripting Interface method that expects a Boolean argument, and the 0 or 1 will be coerced to the
    appropriate AbaqusBoolean value. There are only two possible values for an AbaqusBoolean object: 1 and 0.
    You can import both values from the symbolicConstants module or from the abaqus module. Abaqus Scripting
    Interface commands that expect an AbaqusBoolean object will also accept a Python bool (True, False), or a
    Python int (1, 0).

    .. note::
        This object can be accessed by::

            from symbolicConstants import *
            from abaqusConstants import *
    """

    @abaqus_method_doc
    def __init__(self, value: int) -> None:
        """The AbaqusBoolean method creates an AbaqusBoolean object.

        .. note::
            This function can be accessed by::

                AbaqusBoolean

        Parameters
        ----------
        value
            An Int specifying whether the AbaqusBoolean object will test true or false. Possible
            values are 0 and 1, which will create the AbaqusBoolean method OFF and ON, respectively.

        Returns
        -------
        AbaqusBoolean
            An AbaqusBoolean object.
        """
        super().__init__()
        if value not in (0, 1):
            raise ValueError(f"AbaqusBoolean must have value argument 0 or 1.  {value} supplied")

    @abaqus_method_doc
    def getId(self) -> int:
        ...

    def getText(self) -> str:
        if bool(self):
            return "ON"
        else:
            return "OFF"

    def isTrue(self) -> bool:
        return bool(self)

    def __copy__(self) -> AbaqusBoolean:
        ...

    def __getstate__(self) -> bool:
        ...

    def __hash__(self) -> int:
        ...

    # @staticmethod  # known case of __new__
    # def __new__(cls, *args, **kargs):  # reliably restored by inspect
    #     # no doc
    #     pass

    def __reduce__(self) -> tuple:  # known return case of __reduce__
        ...

    def __repr__(self) -> str:
        return self.getText()

    def __setstate__(self, *args) -> None:
        ...

    def __str__(self) -> str:
        return self.getText()

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """List of weak references to the object (if defined)"""
