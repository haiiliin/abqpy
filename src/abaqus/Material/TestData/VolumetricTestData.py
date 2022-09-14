from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from ...UtilityAndView.abaqusConstants import *


@abaqus_class_doc
class VolumetricTestData:
    r"""The VolumetricTestData object provides volumetric test data.

    .. note:: 
        This object can be accessed by::

            import material
            mdb.models[name].materials[name].hyperelastic.volumetricTestData
            mdb.models[name].materials[name].hyperfoam.volumetricTestData
            mdb.models[name].materials[name].viscoelastic.volumetricTestData
            import odbMaterial
            session.odbs[name].materials[name].hyperelastic.volumetricTestData
            session.odbs[name].materials[name].hyperfoam.volumetricTestData
            session.odbs[name].materials[name].viscoelastic.volumetricTestData

        The table data for this object are:

        - For a hyperelastic or hyperfoam material model, the table data specify the following:
        
            - Pressure, :math:`p`.
            - Volume ratio, :math:`J` (current volume/original volume).
            
        - For a viscoelastic material model, the values depend on the value of the **time** member of the 
          :py:class:`~abaqus.Material.Elastic.HyperElastic.ViscoElastic.Viscoelastic.Viscoelastic` object.
            
            - If **time** = RELAXATION_TEST_DATA, the table data specify the following:
            
                - Normalized volumetric (bulk) modulus :math:`k_{R}(t), \quad\left(0 \leq k_{R}(t) \leq 1\right)`
                - Time :math:`t (t>0)`.
                
            - If **time** = CREEP_TEST_DATA, the table data specify the following:
            
                - Normalized volumetric (bulk) compliance :math:`j_{K}(t), \quad\left(j_{K}(t) \geq 1\right)`.
                - Time :math:`t(t>0)`

        The corresponding analysis keywords are:

        - VOLUMETRIC TEST DATA
    """

    @abaqus_method_doc
    def __init__(
        self,
        table: tuple,
        volinf: float = None,
        smoothing: int = None,
        temperatureDependency: Boolean = OFF,
        dependencies: int = 0,
    ):
        """This method creates a VolumetricTestData object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].materials[name].hyperelastic.VolumetricTestData
                mdb.models[name].materials[name].hyperfoam.VolumetricTestData
                mdb.models[name].materials[name].viscoelastic.VolumetricTestData
                session.odbs[name].materials[name].hyperelastic.VolumetricTestData
                session.odbs[name].materials[name].hyperfoam.VolumetricTestData
                session.odbs[name].materials[name].viscoelastic.VolumetricTestData

        Parameters
        ----------
        table
            A sequence of sequences of Floats specifying the items described below.
        volinf
            None or a Float specifying a normalized volumetric value that depends on the value of
            the **time** member of the Viscoelastic object. The default value is None.If
            **time** = RELAXATION_TEST_DATA, **volinf** specifies the value of the long-term, normalized
            volumetric modulus, kR⁢(∞). If **time** = CREEP_TEST_DATA, **volinf** specifies the value of
            the long-term, normalized volumetric compliance, K⁢(∞).This argument is valid only for a
            viscoelastic material model.
        smoothing
            None or an Int specifying the value for smoothing. If **smoothing** = None, no smoothing is
            employed. The default value is None.
        temperatureDependency
            A Boolean specifying whether the data depend on temperature. The default value is OFF.
        dependencies
            An Int specifying the number of field variable dependencies. The default value is 0.

        Returns
        -------
        VolumetricTestData
            A :py:class:`~abaqus.Material.TestData.VolumetricTestData.VolumetricTestData` object.
        """
        ...

    @abaqus_method_doc
    def setValues(self, *args, **kwargs):
        """This method modifies the VolumetricTestData object."""
        ...
