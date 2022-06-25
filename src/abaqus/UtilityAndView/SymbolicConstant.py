class SymbolicConstant:
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
        This object can be accessed by:

        .. code-block:: python

            from symbolicConstants import *
            from abaqusConstants import *
    """

    def __init__(self, text: str):
        """The SymbolicConstant method creates a SymbolicConstant object.

        .. note:: 
            This function can be accessed by:

            .. code-block:: python

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
        pass
