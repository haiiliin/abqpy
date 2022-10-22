from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from .CommandRegister import CommandRegister


@abaqus_class_doc
class RegisteredDictionary(CommandRegister, dict):
    """This class allows you to create a dictionary that can be queried from the GUI and is
    capable of notifying the GUI when the contents of the dictionary change. The keys to a
    RegisteredDictionary must be either strings or integers.
    The RegisteredDictionary object is derived from the CommandRegister object.

    .. note:: 
        This object can be accessed by::

            import customKernel
    """

    @abaqus_method_doc
    def __init__(self):
        """This method creates a RegisteredDictionary object.

        .. note:: 
            This function can be accessed by::

                customKernel.RegisteredDictionary

        Returns
        -------
        RegisteredDictionary
            A :py:class:`~abaqus.CustomKernel.RegisteredDictionary.RegisteredDictionary` object.
        """
        super().__init__()

    @abaqus_method_doc
    def Methods(self):
        """The RegisteredDictionary object supports the same methods as a Python dictionary. In
        addition, the RegisteredDictionary object supports the changeKey method.
        """
        # TODO: Implement this method
        ...

    @abaqus_method_doc
    def changeKey(self, fromName: str, toName: str):
        """This method changes the name of a key in the dictionary.

        Parameters
        ----------
        fromName
            A String or an integer specifying the name of the key to be changed.
        toName
            A String or an integer specifying the new name for the key.
        """
        if fromName in self:
            self[toName] = self[fromName]
            del self[fromName]
