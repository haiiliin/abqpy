from .CommandRegister import CommandRegister


class RegisteredList(CommandRegister, list):
    """This class allows you to create a list that can be queried from the GUI and is capable
    of notifying the GUI when the contents of the list change.
    The RegisteredList object is derived from the CommandRegister object.

    .. note:: 
        This object can be accessed by:

        .. code-block:: python

            import customKernel
    """

    def __init__(self):
        """This method creates a RegisteredList object.

        .. note:: 
            This function can be accessed by:

            .. code-block:: python

                customKernel.RegisteredList

        Returns
        -------
        RegisteredList
            A :py:class:`~abaqus.CustomKernel.RegisteredList.RegisteredList` object.
        """
        super().__init__()

    def Methods(self):
        """The RegisteredList object supports the same methods as a standard Python list object."""
        # TODO: Implement this method
        ...
