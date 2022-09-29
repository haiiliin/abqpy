from typing import Optional

from abqpy.decorators import abaqus_function_doc
from .Material import Material
from ..UtilityAndView.abaqusConstants import *

""" This command evaluates the behavior of a hyperelastic material under standard test 
conditions. 


.. note::
    This object can be accessed by::
    
        from material import evaluateMaterial

"""


@abaqus_function_doc
def evaluateMaterial(
    material: Material,
    simulationName: str,
    dataSource: Optional[SymbolicConstant] = None,
    strainEnergyPotentials: Optional[SymbolicConstant] = None,
    marlowData: Optional[SymbolicConstant] = None,
    marlowDataType: Optional[SymbolicConstant] = None,
    testDataTypes: Optional[SymbolicConstant] = None,
    uniaxialStrainRange: Optional[float] = None,
    biaxialStrainRange: Optional[float] = None,
    planarStrainRange: Optional[float] = None,
    volumeRatioRange: Optional[float] = None,
    simpleShearStrainRange: Optional[float] = None,
    viscoDataSource: Optional[SymbolicConstant] = None,
    viscoTestDataTypes: Optional[SymbolicConstant] = None,
    relaxationTime: Optional[float] = None,
    creepTime: Optional[float] = None,
):
    """This method evaluates the behavior of a hyperelastic material under standard test
    conditions.

    .. note:: 
        This function can be accessed by::

            evaluateMaterial

    Parameters
    ----------
    material
        A :py:class:`~abaqus.Material.Material.Material` object.
    simulationName
        A String specifying the name to be used for the material evaluation simulation.
    dataSource
        A SymbolicConstant specifying whether test data or coefficients should be used for the
        material definition in the unit element tests. Possible values are TEST_DATA or
        COEFFICIENTS.
    strainEnergyPotentials
        A sequence of SymbolicConstants specifying for which material models the material is to
        be evaluated. Possible values are 
        
        - POLY_N1
        - POLY_N2
        - POLY_N3
        - POLY_N4
        - POLY_N5
        - POLY_N6,
        - OGDEN_N1
        - OGDEN_N2
        - OGDEN_N3
        - OGDEN_N4
        - OGDEN_N5
        - OGDEN_N6
        - REDUCED_POLY_N1,
        - REDUCED_POLY_N2
        - REDUCED_POLY_N3
        - REDUCED_POLY_N4
        - REDUCED_POLY_N5
        - REDUCED_POLY_N6,
        - ARRUDA_BOYCE
        - VAN_DER_WAALS
        - YEOH
        - MOONEY_RIVLIN
        - NEO_HOOKE. 
        
        **Note**: The options
        POLY_N3, POLY_N4, POLY_N5, and POLY_N6 are valid only if the material was defined by
        providing coefficients of the strain energy potential.
    marlowData
        None or a sequence of SymbolicConstants specifying the types of test data to be included
        in the material definition of the Marlow material that is being evaluated. Possible
        values are UNIAXIAL, BIAXIAL, PLANAR, or VOLUMETRIC. The default value is None.
    marlowDataType
        None or a SymbolicConstant specifying the input data type for the Marlow material model.
        Possible values are TENSION, COMPRESSION, or BOTH.
    testDataTypes
        A sequence of SymbolicConstants specifying the types of test data to be included in the
        material definition of the material being evaluated. Possible values are UNIAXIAL,
        BIAXIAL, PLANAR, and VOLUMETRIC.
    uniaxialStrainRange
        A tuple of Floats specifying minimum and maximum nominal strains to be applied in the
        uniaxial tension test.
    biaxialStrainRange
        A tuple of Floats specifying the minimum and maximum nominal strains to be applied in
        the biaxial tension test.
    planarStrainRange
        A tuple of Floats specifying the minimum and maximum nominal strains to be applied in
        the planar test. The planar test is equivalent to a pure shear test.
    volumeRatioRange
        A tuple of Floats specifying the minimum and maximum compressive volume ratio.
    simpleShearStrainRange
        A tuple of Floats specifying the minimum and maximum nominal strains to be applied in
        the simple shear test.
    viscoDataSource
        None or a SymbolicConstant specifying whether test data or coefficients should be used
        for the viscoelastic material definition in the element tests. Possible values are
        TEST_DATA or COEFFICIENTS. The default value is None.
    viscoTestDataTypes
        None or a sequence of SymbolicConstants specifying the types of test data to be included
        in the material definition of the viscoelastic material being evaluated. Possible values
        are UNIAXIAL, BIAXIAL, PLANAR, or VOLUMETRIC. The default value is None.
    relaxationTime
        None or a Float specifying the time period for the stress relaxation response mode. The
        default value is None.
    creepTime
        None or a Float specifying the time period for the creep response mode. The default
        value is None.

    Raises
    ------
    MaterialEvaluationError: POLY_N3, POLY_N4, POLY_N5, or POLY_N6 not allowed for **dataSource** = TEST_DATA
        If **dataSource** = TEST_DATA and **strainEnergyPotentials** contains POLY_N3, POLY_N4,
        POLY_N5, or POLY_N6.
    MaterialEvaluationError: material evaluation failed, see **path to data file**
        If the material evaluation failed.
    MaterialEvaluationError: Material evaluation is currentlysupported only for hyperelastic materials
        If the material type of the material to be evaluated is not hyperelastic.
    """
    ...
