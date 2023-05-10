from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from ...UtilityAndView.abaqusConstants import OFF, Boolean


@abaqus_class_doc
class Potential:
    """The Potential object defines an anisotropic yield/creep model.

    .. note::
        This object can be accessed by::

            import material
            mdb.models[name].materials[name].creep.potential
            mdb.models[name].materials[name].Plastic.potential
            mdb.models[name].materials[name].viscous.potential
            import odbMaterial
            session.odbs[name].materials[name].creep.potential
            session.odbs[name].materials[name].Plastic.potential
            session.odbs[name].materials[name].viscous.potential

        The table data for this object are:

        - :math:`R_{11}`.
        - :math:`R_{22}`.
        - :math:`R_{33}`.
        - :math:`R_{12}`.
        - :math:`R_{13}`.
        - :math:`R_{23}`.
        - Temperature, if the data depend on temperature.
        - Value of the first field variable, if the data depend on field variables.
        - Value of the second field variable.
        - Etc.

        The corresponding analysis keywords are:

        - POTENTIAL
    """

    @abaqus_method_doc
    def __init__(self, table: tuple, temperatureDependency: Boolean = OFF, dependencies: int = 0):
        """This method creates a Potential object.

        .. note::
            This function can be accessed by::

                mdb.models[name].materials[name].creep.Potential
                mdb.models[name].materials[name].Plastic.Potential
                mdb.models[name].materials[name].viscous.Potential
                session.odbs[name].materials[name].creep.Potential
                session.odbs[name].materials[name].Plastic.Potential
                session.odbs[name].materials[name].viscous.Potential

        Parameters
        ----------
        table
            A sequence of sequences of Floats specifying the items described below.
        temperatureDependency
            A Boolean specifying whether the data depend on temperature. The default value is OFF.
        dependencies
            An Int specifying the number of field variable dependencies. The default value is 0.

        Returns
        -------
        Potential
            A Potential object.

        Raises
        ------
        RangeError
        """
        ...

    @abaqus_method_doc
    def setValues(self, *args, **kwargs):
        """This method modifies the Potential object.

        Raises
        ------
        RangeError
        """
        ...
