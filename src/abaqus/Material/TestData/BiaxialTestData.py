from __future__ import annotations

from abqpy.decorators import abaqus_class_doc

from ...UtilityAndView.abaqusConstants import OFF, Boolean


@abaqus_class_doc
class BiaxialTestData:
    """The BiaxialTestData object provides equibiaxial test data (compression and/or tension).

    .. note::
        This object can be accessed by::

            import material
            mdb.models[name].materials[name].hyperelastic.biaxialTestData
            mdb.models[name].materials[name].hyperfoam.biaxialTestData
            mdb.models[name].materials[name].mullinsEffect.biaxialTests[i]
            import odbMaterial
            session.odbs[name].materials[name].hyperelastic.biaxialTestData
            session.odbs[name].materials[name].hyperfoam.biaxialTestData
            session.odbs[name].materials[name].mullinsEffect.biaxialTests[i]

        The corresponding analysis keywords are:

        - BIAXIAL TEST DATA
    """

    def __init__(
        self,
        table: tuple,
        smoothing: int | None = None,
        lateralNominalStrain: Boolean = OFF,
        temperatureDependency: Boolean = OFF,
        dependencies: int = 0,
    ):
        """This method creates a BiaxialTestData object.

        .. note::
            This function can be accessed by::

                mdb.models[name].materials[name].hyperelastic.BiaxialTestData
                mdb.models[name].materials[name].hyperfoam.BiaxialTestData
                mdb.models[name].materials[name].mullinsEffect.BiaxialTestData
                session.odbs[name].materials[name].hyperelastic.BiaxialTestData
                session.odbs[name].materials[name].hyperfoam.BiaxialTestData
                session.odbs[name].materials[name].mullinsEffect.BiaxialTestData

        Parameters
        ----------
        table
            A sequence of sequences of Floats specifying the following:

            - Nominal stress, TB.
            - Nominal strain, ϵB.
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
        BiaxialTestData
            A BiaxialTestData object.
        """
        ...

    def setValues(self, *args, **kwargs):
        """This method modifies the BiaxialTestData object."""
        ...
