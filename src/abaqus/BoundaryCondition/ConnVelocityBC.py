from typing import Union, Optional

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from typing_extensions import Literal

from .BoundaryCondition import BoundaryCondition
from ..Region.Region import Region
from ..UtilityAndView.abaqusConstants import SET, SymbolicConstant, UNIFORM, UNSET
from ..UtilityAndView.abaqusConstants import abaqusConstants as C


@abaqus_class_doc
class ConnVelocityBC(BoundaryCondition):
    """The ConnVelocityBC object stores the data for a connector velocity boundary condition.
    The ConnVelocityBC object is derived from the BoundaryCondition object.

    .. note:: 
        This object can be accessed by::

            import load
            mdb.models[name].boundaryConditions[name]
    """

    #: A String specifying the boundary condition repository key.
    name: str = ""

    #: A SymbolicConstant specifying how the boundary condition is distributed spatially.
    #: Possible values are UNIFORM and USER_DEFINED. The default value is UNIFORM.
    distributionType: SymbolicConstant = UNIFORM

    #: A String specifying the name of the assembled fastener to which the boundary condition
    #: will be applied. This argument is not valid when **region** is specified. When this
    #: argument is specified, **fastenerSetName** must also be specified. The default value is an
    #: empty string.
    fastenerName: str = ""

    #: A String specifying the assembled fastener template model set to which the boundary
    #: condition will be applied. This argument is not valid when **region** is specified. When
    #: this argument is specified, **fastenerName** must also be specified. The default value is
    #: an empty string.
    fastenerSetName: str = ""

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
        region: str = "",
        fastenerName: str = "",
        fastenerSetName: str = "",
        v1: Union[Literal[C.SET, C.UNSET], float] = UNSET,
        v2: Union[Literal[C.SET, C.UNSET], float] = UNSET,
        v3: Union[Literal[C.SET, C.UNSET], float] = UNSET,
        vr1: Union[Literal[C.SET, C.UNSET], float] = UNSET,
        vr2: Union[Literal[C.SET, C.UNSET], float] = UNSET,
        vr3: Union[Literal[C.SET, C.UNSET], float] = UNSET,
        amplitude: str = UNSET,
        distributionType: Literal[C.USER_DEFINED, C.UNIFORM] = UNIFORM,
    ):
        """This method creates a ConnVelocityBC object on a wire region. Alternatively, the
        boundary condition may also be applied to a wire set referenced from an assembled
        fastener template model.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].ConnVelocityBC

        Parameters
        ----------
        name
            A String specifying the boundary condition repository key.
        createStepName
            A String specifying the name of the step in which the boundary condition is created.
        region
            The wire region to which the boundary condition is applied. This argument is not valid
            when **fastenerName** and **fastenerSetName** are specified.
        fastenerName
            A String specifying the name of the assembled fastener to which the boundary condition
            will be applied. This argument is not valid when **region** is specified. When this
            argument is specified, **fastenerSetName** must also be specified. The default value is an
            empty string.
        fastenerSetName
            A String specifying the assembled fastener template model set to which the boundary
            condition will be applied. This argument is not valid when **region** is specified. When
            this argument is specified, **fastenerName** must also be specified. The default value is
            an empty string.
        v1
            A Float or a SymbolicConstant specifying the velocity component in the connector's local
            1-direction. Possible values for the SymbolicConstant are UNSET and SET. The default
            value is UNSET.Note:Although **v1**, **v2**, **v3**, **vr1**, **vr2**, and **vr3** are optional
            arguments, at least one of them must be specified.
        v2
            A Float or a SymbolicConstant specifying the velocity component in the connector's local
            2-direction. Possible values for the SymbolicConstant are UNSET and SET. The default
            value is UNSET.
        v3
            A Float or a SymbolicConstant specifying the velocity component in the connector's local
            3-direction. Possible values for the SymbolicConstant are UNSET and SET. The default
            value is UNSET.
        vr1
            A Float or a SymbolicConstant specifying the rotational velocity component in the
            connector's local 4-direction. Possible values for the SymbolicConstant are UNSET and
            SET. The default value is UNSET.
        vr2
            A Float or a SymbolicConstant specifying the rotational velocity component in the
            connector's local 5-direction. Possible values for the SymbolicConstant are UNSET and
            SET. The default value is UNSET.
        vr3
            A Float or a SymbolicConstant specifying the rotational velocity component in the
            connector's local 6-direction. Possible values for the SymbolicConstant are UNSET and
            SET. The default value is UNSET.
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
            UNSET should be used if the boundary condition has no amplitude reference. The default
            value is UNSET. You should provide the **amplitude** argument only if it is valid for the
            specified step.
        distributionType
            A SymbolicConstant specifying how the boundary condition is distributed spatially.
            Possible values are UNIFORM and USER_DEFINED. The default value is UNIFORM.

        Returns
        -------
        ConnVelocityBC
            A :py:class:`~abaqus.BoundaryCondition.ConnVelocityBC.ConnVelocityBC` object.
        """
        super().__init__()

    @abaqus_method_doc
    def setValues(
        self,
        region: str = "",
        fastenerName: str = "",
        fastenerSetName: str = "",
        v1: Union[Literal[C.SET, C.UNSET], float] = UNSET,
        v2: Union[Literal[C.SET, C.UNSET], float] = UNSET,
        v3: Union[Literal[C.SET, C.UNSET], float] = UNSET,
        vr1: Union[Literal[C.SET, C.UNSET], float] = UNSET,
        vr2: Union[Literal[C.SET, C.UNSET], float] = UNSET,
        vr3: Union[Literal[C.SET, C.UNSET], float] = UNSET,
        amplitude: str = UNSET,
        distributionType: Literal[C.USER_DEFINED, C.UNIFORM] = UNIFORM,
    ):
        """This method modifies the data for an existing ConnVelocityBC object in the step where it
        is created.

        Parameters
        ----------
        region
            The wire region to which the boundary condition is applied. This argument is not valid
            when **fastenerName** and **fastenerSetName** are specified.
        fastenerName
            A String specifying the name of the assembled fastener to which the boundary condition
            will be applied. This argument is not valid when **region** is specified. When this
            argument is specified, **fastenerSetName** must also be specified. The default value is an
            empty string.
        fastenerSetName
            A String specifying the assembled fastener template model set to which the boundary
            condition will be applied. This argument is not valid when **region** is specified. When
            this argument is specified, **fastenerName** must also be specified. The default value is
            an empty string.
        v1
            A Float or a SymbolicConstant specifying the velocity component in the connector's local
            1-direction. Possible values for the SymbolicConstant are UNSET and SET. The default
            value is UNSET.Note:Although **v1**, **v2**, **v3**, **vr1**, **vr2**, and **vr3** are optional
            arguments, at least one of them must be specified.
        v2
            A Float or a SymbolicConstant specifying the velocity component in the connector's local
            2-direction. Possible values for the SymbolicConstant are UNSET and SET. The default
            value is UNSET.
        v3
            A Float or a SymbolicConstant specifying the velocity component in the connector's local
            3-direction. Possible values for the SymbolicConstant are UNSET and SET. The default
            value is UNSET.
        vr1
            A Float or a SymbolicConstant specifying the rotational velocity component in the
            connector's local 4-direction. Possible values for the SymbolicConstant are UNSET and
            SET. The default value is UNSET.
        vr2
            A Float or a SymbolicConstant specifying the rotational velocity component in the
            connector's local 5-direction. Possible values for the SymbolicConstant are UNSET and
            SET. The default value is UNSET.
        vr3
            A Float or a SymbolicConstant specifying the rotational velocity component in the
            connector's local 6-direction. Possible values for the SymbolicConstant are UNSET and
            SET. The default value is UNSET.
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
            UNSET should be used if the boundary condition has no amplitude reference. The default
            value is UNSET. You should provide the **amplitude** argument only if it is valid for the
            specified step.
        distributionType
            A SymbolicConstant specifying how the boundary condition is distributed spatially.
            Possible values are UNIFORM and USER_DEFINED. The default value is UNIFORM.
        """
        ...

    @abaqus_method_doc
    def setValuesInStep(
        self,
        stepName: str,
        v1: Union[Literal[C.SET, C.FREED], float] = SET,
        v2: Union[Literal[C.SET, C.FREED], float] = SET,
        v3: Union[Literal[C.SET, C.FREED], float] = SET,
        vr1: Union[Literal[C.SET, C.FREED], float] = SET,
        vr2: Union[Literal[C.SET, C.FREED], float] = SET,
        vr3: Union[Literal[C.SET, C.FREED], float] = SET,
        amplitude: str = "",
    ):
        """This method modifies the propagating data for an existing ConnVelocityBC object in the
        specified step.

        Parameters
        ----------
        stepName
            A String specifying the name of the step in which the boundary condition is modified.
        v1
            A Float or a SymbolicConstant specifying the velocity component in the connector's local
            1-direction. Possible values for the SymbolicConstant are SET and FREED.
        v2
            A Float or a SymbolicConstant specifying the velocity component in the connector's local
            2-direction. Possible values for the SymbolicConstant are SET and FREED.
        v3
            A Float or a SymbolicConstant specifying the velocity component in the connector's local
            3-direction. Possible values for the SymbolicConstant are SET and FREED.
        vr1
            A Float or a SymbolicConstant specifying the rotational velocity component in the
            connector's local 4-direction. Possible values for the SymbolicConstant are SET and
            FREED.
        vr2
            A Float or a SymbolicConstant specifying the rotational velocity component in the
            connector's local 5-direction. Possible values for the SymbolicConstant are SET and
            FREED.
        vr3
            A Float or a SymbolicConstant specifying the rotational velocity component in the
            connector's local 6-direction. Possible values for the SymbolicConstant are SET and
            FREED.
        amplitude
            A String or a SymbolicConstant specifying the name of the amplitude reference. Possible
            values for the SymbolicConstant are UNCHANGED and FREED. UNCHANGED should be used if the
            amplitude is propagated from the previous analysis step. FREED should be used if the
            boundary condition is changed to have no amplitude reference. You should provide the
            **amplitude** argument only if it is valid for the specified step.
        """
        ...
