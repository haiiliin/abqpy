import typing

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from .Load import Load
from ..Region.Region import Region
from ..UtilityAndView.abaqusConstants import *


@abaqus_class_doc
class SurfaceTraction(Load):
    """The SurfaceTraction object defines surface traction on a region.
    The SurfaceTraction object is derived from the Load object.

    .. note:: 
        This object can be accessed by::

            import load
            mdb.models[name].loads[name]
    """

    #: A String specifying the load repository key.
    name: str = ""

    #: A Float specifying an additional rotation of **directionVector** about an axis. The
    #: default value is 0.0.
    angle: float = 0

    #: A SymbolicConstant specifying the axis about which to apply an additional rotation of
    #: **directionVector**. Possible values are AXIS_1, AXIS_2, and AXIS_3. The default value is
    #: AXIS_1.
    axis: SymbolicConstant = AXIS_1

    #: A Boolean specifying whether the direction of the force changes with rotation. The
    #: default value is ON.This parameter may be modified only if **traction** is GENERAL. You
    #: should provide the **follower** argument only if it is valid for the specified step.
    follower: Boolean = ON

    #: A Boolean specifying whether the to maintain a constant resultant force by defining
    #: traction per unit undeformed area. If **resultant** is OFF, traction is defined per unit
    #: deformed area. The default value is OFF.You should provide the **resultant** argument only
    #: if it is valid for the specified step.
    resultant: Boolean = OFF

    #: A SymbolicConstant specifying how to apply surface traction. Possible values are SHEAR
    #: and GENERAL. The default value is SHEAR.
    traction: SymbolicConstant = SHEAR

    #: A SymbolicConstant specifying how the surface traction is distributed spatially.
    #: Possible values are UNIFORM, USER_DEFINED, and FIELD. The default value is UNIFORM.
    distributionType: SymbolicConstant = UNIFORM

    #: A String specifying the name of the AnalyticalField object associated with this load.
    #: The **field** argument applies only when **distributionType** = FIELD. The default value is an
    #: empty string.
    field: str = ""

    #: A String specifying a CSYS defined by a user-subroutine. If **userCsys** = None, the degrees
    #: of freedom are defined in the global coordinate system or by the **localCsys** parameter
    #: if defined. The default value is "None".
    userCsys: str = ""

    #: None or a DatumCsys object specifying the local coordinate system of the load's degrees
    #: of freedom. If **localCsys** = None, the degrees of freedom are defined in the global
    #: coordinate system or by the **userCsys** parameter if defined. When this member is
    #: queried, it returns an Int. The default value is None.
    localCsys: typing.Optional[int] = None

    #: A :py:class:`~abaqus.BasicGeometry.VertexArray.VertexArray` object of length 2 specifying the direction of the load. Instead of
    #: through a ConstrainedSketchVertex, each point may be specified through a tuple of coordinates. If
    #: **traction** is SHEAR, then **directionVector** will be projected onto the region surface.
    #: This parameter is available only if **traction** is GENERAL or SHEAR.
    directionVector: tuple = ()

    #: A :py:class:`~abaqus.Region.Region.Region` object specifying the region to which the load is applied.
    region: Region = Region()

    @abaqus_method_doc
    def __init__(
        self,
        name: str,
        createStepName: str,
        region: Region,
        magnitude: float,
        distributionType: SymbolicConstant = UNIFORM,
        field: str = "",
        amplitude: str = UNSET,
        angle: float = 0,
        axis: SymbolicConstant = AXIS_1,
        localCsys: typing.Optional[int] = None,
        userCsys: str = "",
        directionVector: tuple = (),
        follower: Boolean = ON,
        resultant: Boolean = OFF,
        traction: SymbolicConstant = SHEAR,
    ):
        """This method creates a SurfaceTraction object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].SurfaceTraction

        Parameters
        ----------
        name
            A String specifying the load repository key.
        createStepName
            A String specifying the name of the step in which the load is created.
        region
            A :py:class:`~abaqus.Region.Region.Region` object specifying the region to which the load is applied.
        magnitude
            A Float or Complex specifying the load magnitude. **magnitude** is optional if
            **distributionType** = USER_DEFINED.
        distributionType
            A SymbolicConstant specifying how the surface traction is distributed spatially.
            Possible values are UNIFORM, USER_DEFINED, and FIELD. The default value is UNIFORM.
        field
            A String specifying the name of the AnalyticalField object associated with this load.
            The **field** argument applies only when **distributionType** = FIELD. The default value is an
            empty string.
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
            UNSET should be used if the load has no amplitude reference. The default value is UNSET.
            You should provide the **amplitude** argument only if it is valid for the specified step.
        angle
            A Float specifying an additional rotation of **directionVector** about an axis. The
            default value is 0.0.
        axis
            A SymbolicConstant specifying the axis about which to apply an additional rotation of
            **directionVector**. Possible values are AXIS_1, AXIS_2, and AXIS_3. The default value is
            AXIS_1.
        localCsys
            None or a DatumCsys object specifying the local coordinate system of the load's degrees
            of freedom. If **localCsys** = None, the degrees of freedom are defined in the global
            coordinate system or by the **userCsys** parameter if defined. When this member is
            queried, it returns an Int. The default value is None.
        userCsys
            A String specifying a CSYS defined by a user-subroutine. If **userCsys** = None, the degrees
            of freedom are defined in the global coordinate system or by the **localCsys** parameter
            if defined. The default value is "None".
        directionVector
            A :py:class:`~abaqus.BasicGeometry.VertexArray.VertexArray` object of length 2 specifying the direction of the load. Instead of
            through a ConstrainedSketchVertex, each point may be specified through a tuple of coordinates. If
            **traction** is SHEAR, then **directionVector** will be projected onto the region surface.
            This parameter is available only if **traction** is GENERAL or SHEAR.
        follower
            A Boolean specifying whether the direction of the force changes with rotation. The
            default value is ON.This parameter may be modified only if **traction** is GENERAL. You
            should provide the **follower** argument only if it is valid for the specified step.
        resultant
            A Boolean specifying whether the to maintain a constant resultant force by defining
            traction per unit undeformed area. If **resultant** is OFF, traction is defined per unit
            deformed area. The default value is OFF.You should provide the **resultant** argument only
            if it is valid for the specified step.
        traction
            A SymbolicConstant specifying how to apply surface traction. Possible values are SHEAR
            and GENERAL. The default value is SHEAR.

        Returns
        -------
        SurfaceTraction
            A :py:class:`~abaqus.Load.SurfaceTraction.SurfaceTraction` object.
        """
        super().__init__()

    @abaqus_method_doc
    def setValues(
        self,
        distributionType: SymbolicConstant = UNIFORM,
        field: str = "",
        amplitude: str = UNSET,
        angle: float = 0,
        axis: SymbolicConstant = AXIS_1,
        localCsys: typing.Optional[int] = None,
        userCsys: str = "",
        directionVector: tuple = (),
        follower: Boolean = ON,
        resultant: Boolean = OFF,
        traction: SymbolicConstant = SHEAR,
    ):
        """This method modifies the data for an existing SurfaceTraction object in the step where
        it is created.

        Parameters
        ----------
        distributionType
            A SymbolicConstant specifying how the surface traction is distributed spatially.
            Possible values are UNIFORM, USER_DEFINED, and FIELD. The default value is UNIFORM.
        field
            A String specifying the name of the AnalyticalField object associated with this load.
            The **field** argument applies only when **distributionType** = FIELD. The default value is an
            empty string.
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
            UNSET should be used if the load has no amplitude reference. The default value is UNSET.
            You should provide the **amplitude** argument only if it is valid for the specified step.
        angle
            A Float specifying an additional rotation of **directionVector** about an axis. The
            default value is 0.0.
        axis
            A SymbolicConstant specifying the axis about which to apply an additional rotation of
            **directionVector**. Possible values are AXIS_1, AXIS_2, and AXIS_3. The default value is
            AXIS_1.
        localCsys
            None or a DatumCsys object specifying the local coordinate system of the load's degrees
            of freedom. If **localCsys** = None, the degrees of freedom are defined in the global
            coordinate system or by the **userCsys** parameter if defined. When this member is
            queried, it returns an Int. The default value is None.
        userCsys
            A String specifying a CSYS defined by a user-subroutine. If **userCsys** = None, the degrees
            of freedom are defined in the global coordinate system or by the **localCsys** parameter
            if defined. The default value is "None".
        directionVector
            A :py:class:`~abaqus.BasicGeometry.VertexArray.VertexArray` object of length 2 specifying the direction of the load. Instead of
            through a ConstrainedSketchVertex, each point may be specified through a tuple of coordinates. If
            **traction** is SHEAR, then **directionVector** will be projected onto the region surface.
            This parameter is available only if **traction** is GENERAL or SHEAR.
        follower
            A Boolean specifying whether the direction of the force changes with rotation. The
            default value is ON.This parameter may be modified only if **traction** is GENERAL. You
            should provide the **follower** argument only if it is valid for the specified step.
        resultant
            A Boolean specifying whether the to maintain a constant resultant force by defining
            traction per unit undeformed area. If **resultant** is OFF, traction is defined per unit
            deformed area. The default value is OFF.You should provide the **resultant** argument only
            if it is valid for the specified step.
        traction
            A SymbolicConstant specifying how to apply surface traction. Possible values are SHEAR
            and GENERAL. The default value is SHEAR.
        """
        ...

    @abaqus_method_doc
    def setValuesInStep(
        self,
        stepName: str,
        magnitude: typing.Union[SymbolicConstant, float] = None,
        amplitude: str = "",
    ):
        """This method modifies the propagating data for an existing SurfaceTraction object in the
        specified step.

        Parameters
        ----------
        stepName
            A String specifying the name of the step in which the load is modified.
        magnitude
            A Float, a Complex, or the SymbolicConstant UNCHANGED specifying the load magnitude.
            UNCHANGED should be used if the magnitude is propagated from the previous analysis step.
        amplitude
            A String or a SymbolicConstant specifying the name of the amplitude reference. Possible
            values for the SymbolicConstant are UNCHANGED and FREED. UNCHANGED should be used if the
            amplitude is propagated from the previous analysis step. FREED should be used if the
            load has no amplitude reference. You should provide the **amplitude** argument only if it
            is valid for the specified step.
        """
        ...
