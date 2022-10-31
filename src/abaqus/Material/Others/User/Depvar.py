from abqpy.decorators import abaqus_class_doc, abaqus_method_doc


@abaqus_class_doc
class Depvar:
    """The Depvar object specifies solution-dependent state variables.

    .. note::
        This object can be accessed by::

            import material
            mdb.models[name].materials[name].depvar
            import odbMaterial
            session.odbs[name].materials[name].depvar

        The corresponding analysis keywords are:

        - DEPVAR
    """

    @abaqus_method_doc
    def __init__(self, deleteVar: int = 0, n: int = 0):
        """This method creates a Depvar object.

        .. note::
            This function can be accessed by::

                mdb.models[name].materials[name].Depvar
                session.odbs[name].materials[name].Depvar

        Parameters
        ----------
        deleteVar
            An Int specifying the state variable number controlling the element deletion flag. The
            default value is 0.This argument applies only to Abaqus/Explicit analyses.
        n
            An Int specifying the number of solution-dependent state variables required at each
            integration point. The default value is 0.

        Returns
        -------
        Depvar
            A Depvar object.

        Raises
        ------
        RangeError
        """
        ...

    @abaqus_method_doc
    def setValues(self, *args, **kwargs):
        """This method modifies the Depvar object.

        Raises
        ------
        RangeError
        """
        ...
