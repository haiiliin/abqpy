from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from .....UtilityAndView.abaqusConstants import Boolean, OFF


@abaqus_class_doc
class CastIronTensionHardening:
    r"""The CastIronTensionHardening object specifies hardening for the Cast- Iron plasticity
    model.

    .. note:: 
        This object can be accessed by::

            import material
            mdb.models[name].materials[name].castIronPlasticity.castIronTensionHardening
            import odbMaterial
            session.odbs[name].materials[name].castIronPlasticity.castIronTensionHardening

        The table data for this object are:

        - Yield stress in uniaxial tension, :math:`\sigma_t`.
        - The absolute value of the corresponding Plastic strain.(The first tabular value entered must always be zero.)
        - Temperature, if the data depend on temperature.
        - Value of the first field variable, if the data depend on field variables.
        - Value of the second field variable.
        - Etc.

        The corresponding analysis keywords are:

        - CAST IRON TENSION HARDENING
    """

    @abaqus_method_doc
    def __init__(
        self, table: tuple, temperatureDependency: Boolean = OFF, dependencies: int = 0
    ):
        """This method creates a CastIronTensionHardening object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].materials[name].castIronPlasticity.CastIronTensionHardening.CastIronTensionHardeningrials[name].castIronPlasticity.CastIronTensionHardening
            
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
        CastIronTensionHardening
            A :py:class:`~abaqus.Material.Plastic.Metal.CastIron.CastIronTensionHardening.CastIronTensionHardening` object. 

        Raises
        ------
        RangeError
        """
        ...

    @abaqus_method_doc
    def setValues(self, *args, **kwargs):
        """This method modifies the CastIronTensionHardening object.

        Raises
        ------
        RangeError
        """
        ...
