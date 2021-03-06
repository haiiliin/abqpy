class UserDefinedField:
    """The UserDefinedField object redefines field variables at a material point.

    .. note:: 
        This object can be accessed by:

        .. code-block:: python

            import material
            mdb.models[name].materials[name].userDefinedField
            import odbMaterial
            session.odbs[name].materials[name].userDefinedField

        The corresponding analysis keywords are:

        - USER DEFINED FIELD
    """

    def __init__(self):
        """This method defines a UserDefinedField object.

        .. note:: 
            This function can be accessed by:

            .. code-block:: python

                mdb.models[name].materials[name].UserDefinedField
                session.odbs[name].materials[name].UserDefinedField

        Returns
        -------
        UserDefinedField
            A :py:class:`~abaqus.Material.Others.User.UserDefinedField.UserDefinedField` object.
        """
        pass
