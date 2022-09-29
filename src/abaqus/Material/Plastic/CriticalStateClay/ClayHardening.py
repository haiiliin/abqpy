from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from ....UtilityAndView.abaqusConstants import Boolean, OFF


@abaqus_class_doc
class ClayHardening:
    """The ClayHardening object specifies hardening for the clay plasticity model.

    .. note:: 
        This object can be accessed by::

            import material
            mdb.models[name].materials[name].clayPlasticity.clayHardening
            import odbMaterial
            session.odbs[name].materials[name].clayPlasticity.clayHardening

        The table data for this object are:

        - The hydrostatic pressure stress at yield, :math:`p_c`.
        - The absolute value of the corresponding volumetric Plastic strain.
        - Temperature, if the data depend on temperature.
        - Value of the first field variable, if the data depend on field variables.
        - Value of the second field variable.
        - Etc.

        The corresponding analysis keywords are:

        - CLAY HARDENING
    """

    @abaqus_method_doc
    def __init__(
        self, table: tuple, temperatureDependency: Boolean = OFF, dependencies: int = 0
    ):
        """This method creates a ClayHardening object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].materials[name].clayPlasticity.ClayHardening
                session.odbs[name].materials[name].clayPlasticity.ClayHardening

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
        ClayHardening
            A :py:class:`~abaqus.Material.Plastic.CriticalStateClay.ClayHardening.ClayHardening` object.

        Raises
        ------
        RangeError
        """
        ...

    @abaqus_method_doc
    def setValues(self, *args, **kwargs):
        """This method modifies the ClayHardening object.

        Raises
        ------
        RangeError
        """
        ...
