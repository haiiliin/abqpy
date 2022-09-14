from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from .CastIronCompressionHardening import CastIronCompressionHardening
from .CastIronTensionHardening import CastIronTensionHardening
from .....UtilityAndView.abaqusConstants import *


@abaqus_class_doc
class CastIronPlasticity:
    r"""The CastIronPlasticity object specifies the Cast Iron plasticity model.

    .. note:: 
        This object can be accessed by::

            import material
            mdb.models[name].materials[name].castIronPlasticity
            import odbMaterial
            session.odbs[name].materials[name].castIronPlasticity

        The table data for this object are:

        - Plastic Poisson's ratio, :math:`\nu_{pl}` (dimensionless).
        - Temperature, if the data depend on temperature.
        - Value of the first field variable, if the data depend on field variables.
        - Value of the second field variable.
        - Etc.

        The corresponding analysis keywords are:

        - CAST IRON PLASTICITY
    """

    #: A :py:class:`~abaqus.Material.Plastic.Metal.CastIron.CastIronTensionHardening.CastIronTensionHardening` object.
    castIronTensionHardening: CastIronTensionHardening = CastIronTensionHardening(((),))

    #: A :py:class:`~abaqus.Material.Plastic.Metal.CastIron.CastIronCompressionHardening.CastIronCompressionHardening` object.
    castIronCompressionHardening: CastIronCompressionHardening = (
        CastIronCompressionHardening(((),))
    )

    @abaqus_method_doc
    def __init__(
        self, table: tuple, temperatureDependency: Boolean = OFF, dependencies: int = 0
    ):
        """This method creates a CastIronPlasticity object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].materials[name].CastIronPlasticity
                session.odbs[name].materials[name].CastIronPlasticity

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
        CastIronPlasticity
            A :py:class:`~abaqus.Material.Plastic.Metal.CastIron.CastIronPlasticity.CastIronPlasticity` object.

        Raises
        ------
        RangeError
        """
        ...

    @abaqus_method_doc
    def setValues(self, *args, **kwargs):
        """This method modifies the CastIronPlasticity object.

        Raises
        ------
        RangeError
        """
        ...
