class UserOutputVariables:
    """The UserOutputVariables object specifies the number of user-defined output variables.

    .. note:: 
        This object can be accessed by:

        .. code-block:: python

            import material
            mdb.models[name].materials[name].userOutputVariables
            import odbMaterial
            session.odbs[name].materials[name].userOutputVariables

        The corresponding analysis keywords are:

        - USER OUTPUT VARIABLES
    """

    def __init__(self, n: int = 0):
        """This method creates a UserOutputVariables object.

        .. note:: 
            This function can be accessed by:

            .. code-block:: python

                mdb.models[name].materials[name].UserOutputVariables
                session.odbs[name].materials[name].UserOutputVariables

        Parameters
        ----------
        n
            An Int specifying the number of user-defined variables required at each material point.
            The default value is 0.

        Returns
        -------
        UserOutputVariables
            A :py:class:`~abaqus.Material.Others.User.UserOutputVariables.UserOutputVariables` object.

        Raises
        ------
        RangeError
        """
        pass

    def setValues(self, *args, **kwargs):
        """This method modifies the UserOutputVariables object.

        Raises
        ------
        RangeError
        """
        pass
