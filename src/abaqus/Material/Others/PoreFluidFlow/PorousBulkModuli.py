from ....UtilityAndView.abaqusConstants import *
from abqpy.decorators import abaqus_class_doc, abaqus_method_doc


@abaqus_class_doc
class PorousBulkModuli:
    """The PorousBulkModuli object defines bulk moduli for soils and rocks.

    .. note:: 
        This object can be accessed by:

        .. code-block:: python

            import material
            mdb.models[name].materials[name].porousBulkModuli
            import odbMaterial
            session.odbs[name].materials[name].porousBulkModuli

        The table data for this object are:

        - Bulk modulus of solid grains.
        - Bulk modulus of permeating fluid.
        - Temperature, if the data depend on temperature.

        The corresponding analysis keywords are:

        - POROUS BULK MODULI
    """

    @abaqus_method_doc
    def __init__(self, table: tuple, temperatureDependency: Boolean = OFF):
        """This method creates a PorousBulkModuli object.

        .. note:: 
            This function can be accessed by:

            .. code-block:: python

                mdb.models[name].materials[name].PorousBulkModuli
                session.odbs[name].materials[name].PorousBulkModuli

        Parameters
        ----------
        table
            A sequence of sequences of Floats specifying the items described below.
        temperatureDependency
            A Boolean specifying whether the data depend on temperature. The default value is OFF.

        Returns
        -------
        PorousBulkModuli
            A :py:class:`~abaqus.Material.Others.PoreFluidFlow.PorousBulkModuli.PorousBulkModuli` object.
        """
        ...

    @abaqus_method_doc
    def setValues(self, *args, **kwargs):
        """This method modifies the PorousBulkModuli object."""
        ...
