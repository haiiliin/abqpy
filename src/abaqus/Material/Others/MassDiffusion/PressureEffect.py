from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from ....UtilityAndView.abaqusConstants import Boolean, OFF


@abaqus_class_doc
class PressureEffect:
    r"""The PressureEffect object defines equivalent pressure stress driven mass diffusion.

    .. note:: 
        This object can be accessed by::

            import material
            mdb.models[name].materials[name].diffusivity.pressureEffect
            import odbMaterial
            session.odbs[name].materials[name].diffusivity.pressureEffect

        The table data for this object are:

        - Pressure stress factor, :math:`\kappa_p`.
        - Concentration.
        - Temperature, if the data depend on temperature.
        - Value of the first field variable, if the data depend on field variables.
        - Value of the second field variable.
        - Etc.

        The corresponding analysis keywords are:

        - KAPPA
    """

    @abaqus_method_doc
    def __init__(
        self, table: tuple, temperatureDependency: Boolean = OFF, dependencies: int = 0
    ):
        """This method creates a PressureEffect object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].materials[name].diffusivity.PressureEffect
                session.odbs[name].materials[name].diffusivity.PressureEffect

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
        PressureEffect
            A :py:class:`~abaqus.Material.Others.MassDiffusion.PressureEffect.PressureEffect` object.

        Raises
        ------
        RangeError
        """
        ...

    @abaqus_method_doc
    def setValues(self, *args, **kwargs):
        """This method modifies the PressureEffect object.

        Raises
        ------
        RangeError
        """
        ...
