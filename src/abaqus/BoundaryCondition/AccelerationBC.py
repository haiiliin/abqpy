from typing import Union, Optional

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from .BoundaryCondition import BoundaryCondition
from ..Region.Region import Region
from ..UtilityAndView.abaqusConstants import SET, SymbolicConstant, UNIFORM, UNSET


@abaqus_class_doc
class AccelerationBC(BoundaryCondition):
    """The AccelerationBC object stores the data for an acceleration boundary condition.
    The AccelerationBC object is derived from the BoundaryCondition object.

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
        a1: Union[SymbolicConstant, float] = UNSET,
        a2: Union[SymbolicConstant, float] = UNSET,
        a3: Union[SymbolicConstant, float] = UNSET,
        ar1: Union[SymbolicConstant, float] = UNSET,
        ar2: Union[SymbolicConstant, float] = UNSET,
        ar3: Union[SymbolicConstant, float] = UNSET,
        amplitude: str = UNSET,
        localCsys: Optional[str] = None,
        distributionType: SymbolicConstant = UNIFORM,
    ):
        """This method creates an AccelerationBC object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].AccelerationBC

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
        a1
            A Float or a SymbolicConstant specifying the acceleration component in the 1-direction.
            Possible values for the SymbolicConstant are UNSET and SET. The default value is
            UNSET.Note:Although **a1**, **a2**, **a3**, **ar1**, **ar2**, and **ar3** are optional arguments, at
            least one of them must be specified.
        a2
            A Float or a SymbolicConstant specifying the acceleration component in the 2-direction.
            Possible values for the SymbolicConstant are UNSET and SET. The default value is UNSET.
        a3
            A Float or a SymbolicConstant specifying the acceleration component in the 3-direction.
            Possible values for the SymbolicConstant are UNSET and SET. The default value is UNSET.
        ar1
            A Float or a SymbolicConstant specifying the rotational acceleration component about the
            1-direction. Possible values for the SymbolicConstant are UNSET and SET. The default
            value is UNSET.
        ar2
            A Float or a SymbolicConstant specifying the rotational acceleration component about the
            2-direction. Possible values for the SymbolicConstant are UNSET and SET. The default
            value is UNSET.
        ar3
            A Float or a SymbolicConstant specifying the rotational acceleration component about the
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
        AccelerationBC
            An :py:class:`~abaqus.BoundaryCondition.AccelerationBC.AccelerationBC` object.
        """
        super().__init__()

    @abaqus_method_doc
    def setValues(
        self,
        fieldName: str = "",
        a1: Union[SymbolicConstant, float] = UNSET,
        a2: Union[SymbolicConstant, float] = UNSET,
        a3: Union[SymbolicConstant, float] = UNSET,
        ar1: Union[SymbolicConstant, float] = UNSET,
        ar2: Union[SymbolicConstant, float] = UNSET,
        ar3: Union[SymbolicConstant, float] = UNSET,
        amplitude: str = UNSET,
        localCsys: Optional[str] = None,
        distributionType: SymbolicConstant = UNIFORM,
    ):
        """This method modifies the data for an existing AccelerationBC object in the step where it
        is created.

        Parameters
        ----------
        fieldName
            A String specifying the name of the AnalyticalField object associated with this boundary
            condition. The **fieldName** argument applies only when **distributionType** = FIELD. The
            default value is an empty string.
        a1
            A Float or a SymbolicConstant specifying the acceleration component in the 1-direction.
            Possible values for the SymbolicConstant are UNSET and SET. The default value is
            UNSET.Note:Although **a1**, **a2**, **a3**, **ar1**, **ar2**, and **ar3** are optional arguments, at
            least one of them must be specified.
        a2
            A Float or a SymbolicConstant specifying the acceleration component in the 2-direction.
            Possible values for the SymbolicConstant are UNSET and SET. The default value is UNSET.
        a3
            A Float or a SymbolicConstant specifying the acceleration component in the 3-direction.
            Possible values for the SymbolicConstant are UNSET and SET. The default value is UNSET.
        ar1
            A Float or a SymbolicConstant specifying the rotational acceleration component about the
            1-direction. Possible values for the SymbolicConstant are UNSET and SET. The default
            value is UNSET.
        ar2
            A Float or a SymbolicConstant specifying the rotational acceleration component about the
            2-direction. Possible values for the SymbolicConstant are UNSET and SET. The default
            value is UNSET.
        ar3
            A Float or a SymbolicConstant specifying the rotational acceleration component about the
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
        a1: Union[SymbolicConstant, float] = SET,
        a2: Union[SymbolicConstant, float] = SET,
        a3: Union[SymbolicConstant, float] = SET,
        ar1: Union[SymbolicConstant, float] = SET,
        ar2: Union[SymbolicConstant, float] = SET,
        ar3: Union[SymbolicConstant, float] = SET,
        amplitude: str = "",
    ):
        """This method modifies the propagating data for an existing AccelerationBC object in the
        specified step.

        Parameters
        ----------
        stepName
            A String specifying the name of the step in which the boundary condition is modified.
        a1
            A Float or a SymbolicConstant specifying the acceleration component in the 1-direction.
            Possible values for the SymbolicConstant are SET, UNCHANGED, and FREED.
        a2
            A Float or a SymbolicConstant specifying the acceleration component in the 2-direction.
            Possible values for the SymbolicConstant are SET, UNCHANGED, and FREED.
        a3
            A Float or a SymbolicConstant specifying the acceleration component in the 3-direction.
            Possible values for the SymbolicConstant are SET, UNCHANGED, and FREED.
        ar1
            A Float or a SymbolicConstant specifying the rotational acceleration component about the
            1-direction. Possible values for the SymbolicConstant are SET, UNCHANGED, and FREED.
        ar2
            A Float or a SymbolicConstant specifying the rotational acceleration component about the
            2-direction. Possible values for the SymbolicConstant are SET, UNCHANGED, and FREED.
        ar3
            A Float or a SymbolicConstant specifying the rotational acceleration component about the
            3-direction. Possible values for the SymbolicConstant are SET, UNCHANGED, and FREED.
        amplitude
            A String or a SymbolicConstant specifying the name of the amplitude reference. Possible
            values for the SymbolicConstant are UNCHANGED and FREED. UNCHANGED should be used if the
            amplitude is propagated from the previous analysis step. FREED should be used if the
            boundary condition is changed to have no amplitude reference. You should provide the
            **amplitude** argument only if it is valid for the specified step.
        """
        ...
