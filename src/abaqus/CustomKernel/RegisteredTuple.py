from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from .CommandRegister import CommandRegister


@abaqus_class_doc
class RegisteredTuple(CommandRegister, tuple):
    """This class allows you to create a tuple that can be queried from the GUI and is capable of notifying the
    GUI when the contents of any of the tuple's members change. The RegisteredTuple object is derived from the
    CommandRegister object.

    .. note::
        This object can be accessed by::

            import customKernel
    """

    @abaqus_method_doc
    def __init__(self, tuple: tuple):
        """This method creates a RegisteredTuple object.

        .. note::
            This function can be accessed by::

                customKernel.RegisteredTuple

        Parameters
        ----------
        tuple
            A tuple of objects. These objects must be derived from the CommandRegister class.

        Returns
        -------
        RegisteredTuple
            A RegisteredTuple object.
        """
        super().__init__()

    @abaqus_method_doc
    def Methods(self):
        """The RegisteredTuple object supports the same methods as a standard Python list object."""
        # TODO: Implement this method
        ...
