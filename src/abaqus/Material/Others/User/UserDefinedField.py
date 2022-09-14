from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

@abaqus_class_doc
class UserDefinedField:
    """The UserDefinedField object redefines field variables at a material point.

    .. note:: 
        This object can be accessed by::

            import material
            mdb.models[name].materials[name].userDefinedField
            import odbMaterial
            session.odbs[name].materials[name].userDefinedField

        The corresponding analysis keywords are:

        - USER DEFINED FIELD
    """

    @abaqus_method_doc
    def __init__(self):
        """This method defines a UserDefinedField object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].materials[name].UserDefinedField
                session.odbs[name].materials[name].UserDefinedField

        Returns
        -------
        UserDefinedField
            A :py:class:`~abaqus.Material.Others.User.UserDefinedField.UserDefinedField` object.
        """
        ...
