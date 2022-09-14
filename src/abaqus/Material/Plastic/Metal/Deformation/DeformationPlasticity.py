from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from .....UtilityAndView.abaqusConstants import *


@abaqus_class_doc
class DeformationPlasticity:
    r"""The DeformationPlasticity object specifies the deformation plasticity model.

    .. note:: 
        This object can be accessed by::

            import material
            mdb.models[name].materials[name].deformationPlasticity
            import odbMaterial
            session.odbs[name].materials[name].deformationPlasticity

        The table data for this object are:

        - Young's modulus, :math:`E`.
        - Poisson's ratio, :math:`\nu`.
        - Yield stress, :math:`\sigma^{0}`
        - Exponent, :math:`n`.
        - Yield offset, :math:`\alpha`.
        - Temperature, if the data depend on temperature.

        The corresponding analysis keywords are:

        - DEFORMATION PLASTICITY
    """

    @abaqus_method_doc
    def __init__(self, table: tuple, temperatureDependency: Boolean = OFF):
        """This method creates a DeformationPlasticity object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].materials[name].DeformationPlasticity
                session.odbs[name].materials[name].DeformationPlasticity

        Parameters
        ----------
        table
            A sequence of sequences of Floats specifying the items described below.
        temperatureDependency
            A Boolean specifying whether the data depend on temperature. The default value is OFF.

        Returns
        -------
        DeformationPlasticity
            A :py:class:`~abaqus.Material.Plastic.Metal.Deformation.DeformationPlasticity.DeformationPlasticity` object.

        Raises
        ------
        RangeError
        """
        ...

    @abaqus_method_doc
    def setValues(self, *args, **kwargs):
        """This method modifies the DeformationPlasticity object.

        Raises
        ------
        RangeError
        """
        ...
