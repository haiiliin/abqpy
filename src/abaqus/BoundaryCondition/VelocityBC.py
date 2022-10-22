from typing import Union, Optional

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from .BoundaryCondition import BoundaryCondition
from ..Region.Region import Region
from ..UtilityAndView.abaqusConstants import SET, SymbolicConstant, UNIFORM, UNSET


@abaqus_class_doc
class VelocityBC(BoundaryCondition):
    """The VelocityBC object stores the data for a velocity boundary condition.
    The VelocityBC object is derived from the BoundaryCondition object.

    .. note:: 
        This object can be accessed by::

            import load
            mdb.models[name].boundaryConditions[name]
    """

    #: A String specifying the boundary condition repository key.
    name: str = ""

    #: A SymbolicConstant specifying how the boundary condition is distributed spatially.
    #: Possible values are UNIFORM, USER_DEFINED, and FIELD. The default value is UNIFORM.
    distributionType: SymbolicConstant = UNIFORM

    #: A String specifying the name of the AnalyticalField object associated with this boundary
    #: condition. The **fieldName** argument applies only when **distributionType** = FIELD. The
    #: default value is an empty string.
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
        v1: Union[SymbolicConstant, float] = UNSET,
        v2: Union[SymbolicConstant, float] = UNSET,
        v3: Union[SymbolicConstant, float] = UNSET,
        vr1: Union[SymbolicConstant, float] = UNSET,
        vr2: Union[SymbolicConstant, float] = UNSET,
        vr3: Union[SymbolicConstant, float] = UNSET,
        amplitude: str = UNSET,
        localCsys: Optional[str] = None,
        distributionType: SymbolicConstant = UNIFORM,
    ):
        """This method creates a VelocityBC object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].VelocityBC

        Parameters
        ----------
        name
            A String specifying the boundary condition repository key.
        createStepName
            A String specifying the name of the step in which the boundary condition is created.
        region
            A :py:class:`~abaqus.Region.Region.Region` object specifying the region to which the boundary condition is applied.
        fieldName
            A String specifying the name of the AnalyticalField object associated with this boundary
            condition. The **fieldName** argument applies only when **distributionType** = FIELD. The
            default value is an empty string.
        v1
            A Float or a SymbolicConstant specifying the velocity component in the 1-direction.
            Possible values for the SymbolicConstant are UNSET and SET. The default value is
            UNSET.Note:Although **v1**, **v2**, **v3**, **vr1**, **vr2**, and **vr3** are optional arguments, at
            least one of them must be specified.
        v2
            A Float or a SymbolicConstant specifying the velocity component in the 2-direction.
            Possible values for the SymbolicConstant are UNSET and SET. The default value is UNSET.
        v3
            A Float or a SymbolicConstant specifying the velocity component in the 3-direction.
            Possible values for the SymbolicConstant are UNSET and SET. The default value is UNSET.
        vr1
            A Float or a SymbolicConstant specifying the rotational velocity component about the
            1-direction. Possible values for the SymbolicConstant are UNSET and SET. The default
            value is UNSET.
        vr2
            A Float or a SymbolicConstant specifying the rotational velocity component about the
            2-direction. Possible values for the SymbolicConstant are UNSET and SET. The default
            value is UNSET.
        vr3
            A Float or a SymbolicConstant specifying the rotational velocity component about the
            3-direction. Possible values for the SymbolicConstant are UNSET and SET. The default
            value is UNSET.
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
            UNSET should be used if the boundary condition has no amplitude reference. The default
            value is UNSET. You should provide the **amplitude** argument only if it is valid for the
            specified step.
        localCsys
            None or a DatumCsys object specifying the local coordinate system of the boundary
            condition's degrees of freedom. If **localCsys** = None, the degrees of freedom are defined
            in the global coordinate system. The default value is None.
        distributionType
            A SymbolicConstant specifying how the boundary condition is distributed spatially.
            Possible values are UNIFORM, USER_DEFINED, and FIELD. The default value is UNIFORM.

        Returns
        -------
        VelocityBC
            A :py:class:`~abaqus.BoundaryCondition.VelocityBC.VelocityBC` object.
        """
        super().__init__()

    @abaqus_method_doc
    def setValues(
        self,
        fieldName: str = "",
        v1: Union[SymbolicConstant, float] = UNSET,
        v2: Union[SymbolicConstant, float] = UNSET,
        v3: Union[SymbolicConstant, float] = UNSET,
        vr1: Union[SymbolicConstant, float] = UNSET,
        vr2: Union[SymbolicConstant, float] = UNSET,
        vr3: Union[SymbolicConstant, float] = UNSET,
        amplitude: str = UNSET,
        localCsys: Optional[str] = None,
        distributionType: SymbolicConstant = UNIFORM,
    ):
        """This method modifies the data for an existing VelocityBC object in the step where it is
        created.

        Parameters
        ----------
        fieldName
            A String specifying the name of the AnalyticalField object associated with this boundary
            condition. The **fieldName** argument applies only when **distributionType** = FIELD. The
            default value is an empty string.
        v1
            A Float or a SymbolicConstant specifying the velocity component in the 1-direction.
            Possible values for the SymbolicConstant are UNSET and SET. The default value is
            UNSET.Note:Although **v1**, **v2**, **v3**, **vr1**, **vr2**, and **vr3** are optional arguments, at
            least one of them must be specified.
        v2
            A Float or a SymbolicConstant specifying the velocity component in the 2-direction.
            Possible values for the SymbolicConstant are UNSET and SET. The default value is UNSET.
        v3
            A Float or a SymbolicConstant specifying the velocity component in the 3-direction.
            Possible values for the SymbolicConstant are UNSET and SET. The default value is UNSET.
        vr1
            A Float or a SymbolicConstant specifying the rotational velocity component about the
            1-direction. Possible values for the SymbolicConstant are UNSET and SET. The default
            value is UNSET.
        vr2
            A Float or a SymbolicConstant specifying the rotational velocity component about the
            2-direction. Possible values for the SymbolicConstant are UNSET and SET. The default
            value is UNSET.
        vr3
            A Float or a SymbolicConstant specifying the rotational velocity component about the
            3-direction. Possible values for the SymbolicConstant are UNSET and SET. The default
            value is UNSET.
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
            UNSET should be used if the boundary condition has no amplitude reference. The default
            value is UNSET. You should provide the **amplitude** argument only if it is valid for the
            specified step.
        localCsys
            None or a DatumCsys object specifying the local coordinate system of the boundary
            condition's degrees of freedom. If **localCsys** = None, the degrees of freedom are defined
            in the global coordinate system. The default value is None.
        distributionType
            A SymbolicConstant specifying how the boundary condition is distributed spatially.
            Possible values are UNIFORM, USER_DEFINED, and FIELD. The default value is UNIFORM.
        """
        ...

    @abaqus_method_doc
    def setValuesInStep(
        self,
        stepName: str,
        v1: Union[SymbolicConstant, float] = SET,
        v2: Union[SymbolicConstant, float] = SET,
        v3: Union[SymbolicConstant, float] = SET,
        vr1: Union[SymbolicConstant, float] = SET,
        vr2: Union[SymbolicConstant, float] = SET,
        vr3: Union[SymbolicConstant, float] = SET,
        amplitude: str = "",
    ):
        """This method modifies the propagating data for an existing VelocityBC object in the
        specified step.

        Parameters
        ----------
        stepName
            A String specifying the name of the step in which the boundary condition is modified.
        v1
            A Float or a SymbolicConstant specifying the velocity component in the 1-direction.
            Possible values for the SymbolicConstant are SET and FREED.
        v2
            A Float or a SymbolicConstant specifying the velocity component in the 2-direction.
            Possible values for the SymbolicConstant are SET and FREED.
        v3
            A Float or a SymbolicConstant specifying the velocity component in the 3-direction.
            Possible values for the SymbolicConstant are SET and FREED.
        vr1
            A Float or a SymbolicConstant specifying the rotational velocity component about the
            1-direction. Possible values for the SymbolicConstant are SET and FREED.
        vr2
            A Float or a SymbolicConstant specifying the rotational velocity component about the
            2-direction. Possible values for the SymbolicConstant are SET and FREED.
        vr3
            A Float or a SymbolicConstant specifying the rotational velocity component about the
            3-direction. Possible values for the SymbolicConstant are SET and FREED.
        amplitude
            A String or a SymbolicConstant specifying the name of the amplitude reference. Possible
            values for the SymbolicConstant are UNCHANGED and FREED. UNCHANGED should be used if the
            amplitude is propagated from the previous analysis step. FREED should be used if the
            boundary condition is changed to have no amplitude reference. You should provide the
            **amplitude** argument only if it is valid for the specified step.
        """
        ...
