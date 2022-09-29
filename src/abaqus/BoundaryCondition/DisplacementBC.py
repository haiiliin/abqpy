from typing import Optional, Union

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from .BoundaryCondition import BoundaryCondition
from ..Region.Region import Region
from ..UtilityAndView.abaqusConstants import *


@abaqus_class_doc
class DisplacementBC(BoundaryCondition):
    """The DisplacementBC object stores the data for a displacement/rotation boundary
    condition.
    The DisplacementBC object is derived from the BoundaryCondition object.

    .. note:: 
        This object can be accessed by::

            import load
            mdb.models[name].boundaryConditions[name]
    """

    #: A String specifying the boundary condition repository key.
    name: str = ""

    #: A SymbolicConstant specifying how the boundary condition is distributed spatially.
    #: Possible values are UNIFORM, USER_DEFINED, FIELD, and DISCRETE_FIELD. The default value
    #: is UNIFORM.
    distributionType: SymbolicConstant = UNIFORM

    #: A Boolean specifying whether the boundary condition should remain fixed at the current
    #: values at the start of the step. The default value is OFF.
    fixed: Boolean = OFF

    #: A SymbolicConstant specifying how the boundary condition is defined in a BUCKLE
    #: analysis. Possible values are NOT_APPLICABLE, STRESS_PERTURBATION, BUCKLING_MODES, and
    #: PERTURBATION_AND_BUCKLING. The default value is NOT_APPLICABLE.
    buckleCase: SymbolicConstant = NOT_APPLICABLE

    #: A String specifying the name of the AnalyticalField or DiscreteField object associated
    #: with this boundary condition. The **fieldName** argument applies only when
    #: **distributionType** = FIELD or **distributionType** = DISCRETE_FIELD. The default value is an
    #: empty string.
    fieldName: str = ""

    #: A SymbolicConstant specifying the category of the boundary condition. Possible values
    #: are MECHANICAL and THERMAL.
    category: Optional[SymbolicConstant] = None

    #: A :py:class:`~abaqus.Region.Region.Region` object specifying the region to which the boundary condition is applied.
    region: Region = Region()

    #: None or a DatumCsys object specifying the local coordinate system of the boundary
    #: condition's degrees of freedom. If **localCsys** = None, the degrees of freedom are defined
    #: in the global coordinate system. The default value is None.
    localCsys: Optional[str] = None

    @abaqus_method_doc
    def __init__(
        self,
        name: str,
        createStepName: str,
        region: Region,
        fieldName: str = "",
        u1: Union[SymbolicConstant, float] = UNSET,
        u2: Union[SymbolicConstant, float] = UNSET,
        u3: Union[SymbolicConstant, float] = UNSET,
        ur1: Union[SymbolicConstant, float] = UNSET,
        ur2: Union[SymbolicConstant, float] = UNSET,
        ur3: Union[SymbolicConstant, float] = UNSET,
        fixed: Boolean = OFF,
        amplitude: str = UNSET,
        distributionType: SymbolicConstant = UNIFORM,
        localCsys: Optional[str] = None,
        buckleCase: SymbolicConstant = NOT_APPLICABLE,
    ):
        """This method creates a DisplacementBC object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].DisplacementBC

        Parameters
        ----------
        name
            A String specifying the boundary condition repository key.
        createStepName
            A String specifying the name of the step in which the boundary condition is created.
        region
            A :py:class:`~abaqus.Region.Region.Region` object specifying the region to which the boundary condition is applied.
        fieldName
            A String specifying the name of the AnalyticalField or DiscreteField object associated
            with this boundary condition. The **fieldName** argument applies only when
            **distributionType** = FIELD or **distributionType** = DISCRETE_FIELD. The default value is an
            empty string.
        u1
            A Float, a Complex, or a SymbolicConstant specifying the displacement component in the
            1-direction. Possible values for the SymbolicConstant are UNSET and SET. The default
            value is UNSET.Note:Although **u1**, **u2**, **u3**, **ur1**, **ur2**, and **ur3** are optional
            arguments, at least one of them must be specified.
        u2
            A Float, a Complex, or a SymbolicConstant specifying the displacement component in the
            2-direction. Possible values for the SymbolicConstant are UNSET and SET. The default
            value is UNSET.
        u3
            A Float, a Complex, or a SymbolicConstant specifying the displacement component in the
            3-direction. Possible values for the SymbolicConstant are UNSET and SET. The default
            value is UNSET.
        ur1
            A Float, a Complex, or a SymbolicConstant specifying the rotational displacement
            component about the 1-direction. Possible values for the SymbolicConstant are UNSET and
            SET. The default value is UNSET.
        ur2
            A Float, a Complex, or a SymbolicConstant specifying the rotational displacement
            component about the 2-direction. Possible values for the SymbolicConstant are UNSET and
            SET. The default value is UNSET.
        ur3
            A Float, a Complex, or a SymbolicConstant specifying the rotational displacement
            component about the 3-direction. Possible values for the SymbolicConstant are UNSET and
            SET. The default value is UNSET.
        fixed
            A Boolean specifying whether the boundary condition should remain fixed at the current
            values at the start of the step. The default value is OFF.
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
            UNSET should be used if the boundary condition has no amplitude reference. The default
            value is UNSET. You should provide the **amplitude** argument only if it is valid for the
            specified step.
        distributionType
            A SymbolicConstant specifying how the boundary condition is distributed spatially.
            Possible values are UNIFORM, USER_DEFINED, FIELD, and DISCRETE_FIELD. The default value
            is UNIFORM.
        localCsys
            None or a DatumCsys object specifying the local coordinate system of the boundary
            condition's degrees of freedom. If **localCsys** = None, the degrees of freedom are defined
            in the global coordinate system. The default value is None.
        buckleCase
            A SymbolicConstant specifying how the boundary condition is defined in a BUCKLE
            analysis. Possible values are NOT_APPLICABLE, STRESS_PERTURBATION, BUCKLING_MODES, and
            PERTURBATION_AND_BUCKLING. The default value is NOT_APPLICABLE.

        Returns
        -------
        DisplacementBC
            A :py:class:`~abaqus.BoundaryCondition.DisplacementBC.DisplacementBC` object.
        """
        super().__init__()

    @abaqus_method_doc
    def setValues(
        self,
        fieldName: str = "",
        u1: Union[SymbolicConstant, float] = UNSET,
        u2: Union[SymbolicConstant, float] = UNSET,
        u3: Union[SymbolicConstant, float] = UNSET,
        ur1: Union[SymbolicConstant, float] = UNSET,
        ur2: Union[SymbolicConstant, float] = UNSET,
        ur3: Union[SymbolicConstant, float] = UNSET,
        fixed: Boolean = OFF,
        amplitude: str = UNSET,
        distributionType: SymbolicConstant = UNIFORM,
        localCsys: Optional[str] = None,
        buckleCase: SymbolicConstant = NOT_APPLICABLE,
    ):
        """This method modifies the data for an existing DisplacementBC object in the step where it
        is created.

        Parameters
        ----------
        fieldName
            A String specifying the name of the AnalyticalField or DiscreteField object associated
            with this boundary condition. The **fieldName** argument applies only when
            **distributionType** = FIELD or **distributionType** = DISCRETE_FIELD. The default value is an
            empty string.
        u1
            A Float, a Complex, or a SymbolicConstant specifying the displacement component in the
            1-direction. Possible values for the SymbolicConstant are UNSET and SET. The default
            value is UNSET.Note:Although **u1**, **u2**, **u3**, **ur1**, **ur2**, and **ur3** are optional
            arguments, at least one of them must be specified.
        u2
            A Float, a Complex, or a SymbolicConstant specifying the displacement component in the
            2-direction. Possible values for the SymbolicConstant are UNSET and SET. The default
            value is UNSET.
        u3
            A Float, a Complex, or a SymbolicConstant specifying the displacement component in the
            3-direction. Possible values for the SymbolicConstant are UNSET and SET. The default
            value is UNSET.
        ur1
            A Float, a Complex, or a SymbolicConstant specifying the rotational displacement
            component about the 1-direction. Possible values for the SymbolicConstant are UNSET and
            SET. The default value is UNSET.
        ur2
            A Float, a Complex, or a SymbolicConstant specifying the rotational displacement
            component about the 2-direction. Possible values for the SymbolicConstant are UNSET and
            SET. The default value is UNSET.
        ur3
            A Float, a Complex, or a SymbolicConstant specifying the rotational displacement
            component about the 3-direction. Possible values for the SymbolicConstant are UNSET and
            SET. The default value is UNSET.
        fixed
            A Boolean specifying whether the boundary condition should remain fixed at the current
            values at the start of the step. The default value is OFF.
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
            UNSET should be used if the boundary condition has no amplitude reference. The default
            value is UNSET. You should provide the **amplitude** argument only if it is valid for the
            specified step.
        distributionType
            A SymbolicConstant specifying how the boundary condition is distributed spatially.
            Possible values are UNIFORM, USER_DEFINED, FIELD, and DISCRETE_FIELD. The default value
            is UNIFORM.
        localCsys
            None or a DatumCsys object specifying the local coordinate system of the boundary
            condition's degrees of freedom. If **localCsys** = None, the degrees of freedom are defined
            in the global coordinate system. The default value is None.
        buckleCase
            A SymbolicConstant specifying how the boundary condition is defined in a BUCKLE
            analysis. Possible values are NOT_APPLICABLE, STRESS_PERTURBATION, BUCKLING_MODES, and
            PERTURBATION_AND_BUCKLING. The default value is NOT_APPLICABLE.
        """
        ...

    @abaqus_method_doc
    def setValuesInStep(
        self,
        stepName: str,
        u1: Union[SymbolicConstant, float] = SET,
        u2: Union[SymbolicConstant, float] = SET,
        u3: Union[SymbolicConstant, float] = SET,
        ur1: Union[SymbolicConstant, float] = SET,
        ur2: Union[SymbolicConstant, float] = SET,
        ur3: Union[SymbolicConstant, float] = SET,
        amplitude: str = "",
        buckleCase: SymbolicConstant = NOT_APPLICABLE,
    ):
        """This method modifies the propagating data for an existing DisplacementBC object in the
        specified step.

        Parameters
        ----------
        stepName
            A String specifying the name of the step in which the boundary condition is modified.
        u1
            A Float, a Complex, or a SymbolicConstant specifying the displacement component in the
            1-direction. Possible values for the SymbolicConstant are SET, UNCHANGED, and FREED.
        u2
            A Float, a Complex, or a SymbolicConstant specifying the displacement component in the
            2-direction. Possible values for the SymbolicConstant are SET, UNCHANGED, and FREED.
        u3
            A Float, a Complex, or a SymbolicConstant specifying the displacement component in the
            3-direction. Possible values for the SymbolicConstant are SET, UNCHANGED, and FREED.
        ur1
            A Float, a Complex, or a SymbolicConstant specifying the rotational displacement
            component about the 1-direction. Possible values for the SymbolicConstant are SET,
            UNCHANGED, and FREED.
        ur2
            A Float, a Complex, or a SymbolicConstant specifying the rotational displacement
            component about the 2-direction. Possible values for the SymbolicConstant are SET,
            UNCHANGED, and FREED.
        ur3
            A Float, a Complex, or a SymbolicConstant specifying the rotational displacement
            component about the 3-direction. Possible values for the SymbolicConstant are SET,
            UNCHANGED, and FREED.
        amplitude
            A String or a SymbolicConstant specifying the name of the amplitude reference. Possible
            values for the SymbolicConstant are UNCHANGED and FREED. UNCHANGED should be used if the
            amplitude is propagated from the previous analysis step. FREED should be used if the
            boundary condition is changed to have no amplitude reference. You should provide the
            **amplitude** argument only if it is valid for the specified step.
        buckleCase
            A SymbolicConstant specifying how the boundary condition is defined in a BUCKLE
            analysis. Possible values are NOT_APPLICABLE, STRESS_PERTURBATION, BUCKLING_MODES, and
            PERTURBATION_AND_BUCKLING. The default value is NOT_APPLICABLE.
        """
        ...
