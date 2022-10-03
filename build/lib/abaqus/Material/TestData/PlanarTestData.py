from typing import Optional

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from ...UtilityAndView.abaqusConstants import Boolean, OFF


@abaqus_class_doc
class PlanarTestData:
    r"""The PlanarTestData object specifies planar test (or pure shear) data (compression and/or
    tension).

    .. note:: 
        This object can be accessed by::

            import material
            mdb.models[name].materials[name].hyperelastic.planarTestData
            mdb.models[name].materials[name].hyperfoam.planarTestData
            mdb.models[name].materials[name].mullinsEffect.planarTests[i]
            import odbMaterial
            session.odbs[name].materials[name].hyperelastic.planarTestData
            session.odbs[name].materials[name].hyperfoam.planarTestData
            session.odbs[name].materials[name].mullinsEffect.planarTests[i]

        The table data for this object are:

        - For a hyperelastic material model, the table data specify the following:
        
            - Nominal stress, :math:`T_{S}`
            - Nominal strain in the direction of loading, :math:`\epsilon_{S}`.
        - For a hyperfoam material model, the table data specify the following:
        
            - Nominal stress, :math:`T_{L}`.
            - Nominal strain in the direction of loading, :math:`\epsilon_{p}`.
            - Nominal transverse strain, :math:`\epsilon_{3}`. The default value is 0 .

        The corresponding analysis keywords are:

        - PLANAR TEST DATA
    """

    @abaqus_method_doc
    def __init__(
        self,
        table: tuple,
        smoothing: Optional[int] = None,
        lateralNominalStrain: Boolean = OFF,
        temperatureDependency: Boolean = OFF,
        dependencies: int = 0,
    ):
        """This method creates a PlanarTestData object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].materials[name].hyperelastic.PlanarTestData
                mdb.models[name].materials[name].hyperfoam.PlanarTestData
                mdb.models[name].materials[name].mullinsEffect.PlanarTestData
                session.odbs[name].materials[name].hyperelastic.PlanarTestData
                session.odbs[name].materials[name].hyperfoam.PlanarTestData
                session.odbs[name].materials[name].mullinsEffect.PlanarTestData

        Parameters
        ----------
        table
            A sequence of sequences of Floats specifying the items described below.
        smoothing
            None or an Int specifying the value for smoothing. If **smoothing** = None, no smoothing is
            employed. The default value is None.
        lateralNominalStrain
            A Boolean specifying whether to include lateral nominal strain. The default value is
            OFF.
        temperatureDependency
            A Boolean specifying whether the data depend on temperature. The default value is OFF.
        dependencies
            An Int specifying the number of field variable dependencies. The default value is 0.

        Returns
        -------
        PlanarTestData
            A :py:class:`~abaqus.Material.TestData.PlanarTestData.PlanarTestData` object.
        """
        ...

    @abaqus_method_doc
    def setValues(self, *args, **kwargs):
        """This method modifies the PlanarTestData object."""
        ...
