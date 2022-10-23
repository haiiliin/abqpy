from abqpy.decorators import abaqus_class_doc, abaqus_method_doc


@abaqus_class_doc
class CommandRegister:
    """This class allows you to derive a general class that can be queried from the GUI and is
    capable of notifying the GUI when the contents of the class change.

    .. note::
        This object can be accessed by::

            import customKernel
    """

    @abaqus_method_doc
    def __init__(self):
        """This class allows you to derive a general class that can be queried from the GUI and is
        capable of notifying the GUI when the contents of the class change.

        .. note::
            This function can be accessed by::

                customKernel.CommandRegister

        Returns
        -------
        CommandRegister
            A :py:class:`~abaqus.CustomKernel.CommandRegister.CommandRegister` object.
        """
        ...
