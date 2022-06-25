from .CommandRegister import CommandRegister


class RegisteredDictionary(CommandRegister):
    """This class allows you to create a dictionary that can be queried from the GUI and is
    capable of notifying the GUI when the contents of the dictionary change. The keys to a
    RegisteredDictionary must be either strings or integers.
    The RegisteredDictionary object is derived from the CommandRegister object.

    .. note:: 
        This object can be accessed by:

        .. code-block:: python

            import customKernel
    """

    def __init__(self):
        """This method creates a RegisteredDictionary object.

        .. note:: 
            This function can be accessed by:

            .. code-block:: python

                customKernel.RegisteredDictionary

        Returns
        -------
        RegisteredDictionary
            A :py:class:`~abaqus.CustomKernel.RegisteredDictionary.RegisteredDictionary` object.
        """
        super().__init__()
        pass

    def Methods(self):
        """The RegisteredDictionary object supports the same methods as a Python dictionary. In
        addition, the RegisteredDictionary object supports the changeKey method.
        """
        pass

    def changeKey(self, fromName: str, toName: str):
        """This method changes the name of a key in the dictionary.

        Parameters
        ----------
        fromName
            A String or an integer specifying the name of the key to be changed.
        toName
            A String or an integer specifying the new name for the key.
        """
        pass
