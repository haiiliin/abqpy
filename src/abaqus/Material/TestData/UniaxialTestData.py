from typing import Optional

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from ...UtilityAndView.abaqusConstants import OFF, Boolean


@abaqus_class_doc
class UniaxialTestData:
    r"""The UniaxialTestData object provides uniaxial test data (compression and/or tension).

    .. note::
        This object can be accessed by::

            import material
            mdb.models[name].materials[name].hyperelastic.uniaxialTestData
            mdb.models[name].materials[name].hyperfoam.uniaxialTestData
            mdb.models[name].materials[name].lowDensityFoam.uniaxialCompressionTestData
            mdb.models[name].materials[name].lowDensityFoam.uniaxialTensionTestData
            mdb.models[name].materials[name].mullinsEffect.uniaxialTests[i]
            import odbMaterial
            session.odbs[name].materials[name].hyperelastic.uniaxialTestData
            session.odbs[name].materials[name].hyperfoam.uniaxialTestData
            session.odbs[name].materials[name].lowDensityFoam.uniaxialCompressionTestData
            session.odbs[name].materials[name].lowDensityFoam.uniaxialTensionTestData
            session.odbs[name].materials[name].mullinsEffect.uniaxialTests[i]

        The table data for this object are:

        - For a hyperelastic material model, the table data specify the following:

            - Nominal stress, :math:`T_{U}`.
            - Nominal strain, :math:`\epsilon_{U}`.
        - For a hyperfoam material model, the table data specify the following:

            - Nominal stress, :math:`T_{L}`.
            - Nominal strain, :math:`\epsilon_{U}`.
            - Nominal lateral strain, :math:`\epsilon_{2}=\epsilon_{3}`. The default value is 0 .
        - For a low-density foam material model, the table data specify the following:

            - Nominal stress, :math:`T_{U}`.
            - Nominal strain, :math:`\epsilon_{U}`.
            - Nominal strain rate, :math:`\dot{\epsilon_{U}}`.

        The corresponding analysis keywords are:

        - UNIAXIAL TEST DATA
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
        """This method creates a UniaxialTestData object.

        .. note::
            This function can be accessed by::

                mdb.models[name].materials[name].hyperelastic.UniaxialTestData
                mdb.models[name].materials[name].hyperfoam.UniaxialTestData
                mdb.models[name].materials[name].lowDensityFoam.UniaxialTestData
                mdb.models[name].materials[name].mullinsEffect.UniaxialTestData
                session.odbs[name].materials[name].hyperelastic.UniaxialTestData
                session.odbs[name].materials[name].hyperfoam.UniaxialTestData
                session.odbs[name].materials[name].lowDensityFoam.UniaxialTestData
                session.odbs[name].materials[name].mullinsEffect.UniaxialTestData

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
        UniaxialTestData
            A UniaxialTestData object.
        """
        ...

    @abaqus_method_doc
    def setValues(self, *args, **kwargs):
        """This method modifies the UniaxialTestData object."""
        ...
