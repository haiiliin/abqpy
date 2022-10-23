from typing import Optional

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from typing_extensions import Literal

from .Load import Load
from ..Region.Region import Region
from ..UtilityAndView.abaqusConstants import Boolean, OFF, SymbolicConstant, UNIFORM, UNSET
from ..UtilityAndView.abaqusConstants import abaqusConstants as C


@abaqus_class_doc
class RotationalBodyForce(Load):
    """The RotationalBodyForce object stores the data for a rotational body force.
    The RotationalBodyForce object is derived from the Load object.

    .. note:: 
        This object can be accessed by::

            import load
            mdb.models[name].loads[name]
    """

    #: A String specifying the load repository key.
    name: str = ""

    #: A SymbolicConstant specifying how the load is distributed spatially. Possible values are
    #: UNIFORM and FIELD. The default value is UNIFORM.
    distributionType: SymbolicConstant = UNIFORM

    #: A Boolean specifying whether or not the effect of the load is centrifugal. The default
    #: value is OFF.Note:At least one of **centrifugal** or **rotaryAcceleration** must be
    #: specified and only one must have the value ON.
    centrifugal: Boolean = OFF

    #: A Boolean specifying whether or not the effect of the load is rotary acceleration. The
    #: default value is OFF.Note:At least one of **centrifugal** or **rotaryAcceleration** must be
    #: specified and only one must have the value ON.
    rotaryAcceleration: Boolean = OFF

    #: A tuple of Floats specifying the first point on the axis of rotation for the load.
    point1: Optional[float] = None

    #: A tuple of Floats specifying the second point on the axis of rotation for the load.
    point2: Optional[float] = None

    #: A String specifying the name of the AnalyticalField object associated with this load.
    #: The **field** argument applies only when **distributionType** = FIELD. The default value is an
    #: empty string.
    field: str = ""

    #: A :py:class:`~abaqus.Region.Region.Region` object specifying the region to which the load is applied.
    region: Region = Region()

    @abaqus_method_doc
    def __init__(
        self,
        name: str,
        createStepName: str,
        region: Region,
        magnitude: float,
        point1: tuple,
        point2: tuple,
        distributionType: Literal[C.FIELD, C.UNIFORM] = UNIFORM,
        field: str = "",
        centrifugal: Boolean = OFF,
        rotaryAcceleration: Boolean = OFF,
        amplitude: str = UNSET,
    ):
        """This method creates a RotationalBodyForce object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].RotationalBodyForce

        Parameters
        ----------
        name
            A String specifying the load repository key.
        createStepName
            A String specifying the name of the step in which the load is created. This must be the
            first analysis step name.
        region
            A :py:class:`~abaqus.Region.Region.Region` object specifying the region to which the load is applied.
        magnitude
            A Float specifying the load magnitude.
        point1
            A sequence of Floats specifying the first point on the axis of rotation for the load.
        point2
            A sequence of Floats specifying the second point on the axis of rotation for the load.
        distributionType
            A SymbolicConstant specifying how the load is distributed spatially. Possible values are
            UNIFORM and FIELD. The default value is UNIFORM.
        field
            A String specifying the name of the AnalyticalField object associated with this load.
            The **field** argument applies only when **distributionType** = FIELD. The default value is an
            empty string.
        centrifugal
            A Boolean specifying whether or not the effect of the load is centrifugal. The default
            value is OFF.Note:At least one of **centrifugal** or **rotaryAcceleration** must be
            specified and only one must have the value ON.
        rotaryAcceleration
            A Boolean specifying whether or not the effect of the load is rotary acceleration. The
            default value is OFF.Note:At least one of **centrifugal** or **rotaryAcceleration** must be
            specified and only one must have the value ON.
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
            UNSET should be used if the load has no amplitude reference. The default value is UNSET.
            You should provide the **amplitude** argument only if it is valid for the specified step.

        Returns
        -------
        RotationalBodyForce
            A :py:class:`~abaqus.Load.RotationalBodyForce.RotationalBodyForce` object.
        """
        super().__init__()

    @abaqus_method_doc
    def setValues(
        self,
        distributionType: Literal[C.FIELD, C.UNIFORM] = UNIFORM,
        field: str = "",
        centrifugal: Boolean = OFF,
        rotaryAcceleration: Boolean = OFF,
        amplitude: str = UNSET,
    ):
        """This method modifies the data for an existing RotationalBodyForce object in the step
        where it is created.

        Parameters
        ----------
        distributionType
            A SymbolicConstant specifying how the load is distributed spatially. Possible values are
            UNIFORM and FIELD. The default value is UNIFORM.
        field
            A String specifying the name of the AnalyticalField object associated with this load.
            The **field** argument applies only when **distributionType** = FIELD. The default value is an
            empty string.
        centrifugal
            A Boolean specifying whether or not the effect of the load is centrifugal. The default
            value is OFF.Note:At least one of **centrifugal** or **rotaryAcceleration** must be
            specified and only one must have the value ON.
        rotaryAcceleration
            A Boolean specifying whether or not the effect of the load is rotary acceleration. The
            default value is OFF.Note:At least one of **centrifugal** or **rotaryAcceleration** must be
            specified and only one must have the value ON.
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
            UNSET should be used if the load has no amplitude reference. The default value is UNSET.
            You should provide the **amplitude** argument only if it is valid for the specified step.
        """
        ...

    @abaqus_method_doc
    def setValuesInStep(
        self, stepName: str, magnitude: Optional[float] = None, amplitude: str = ""
    ):
        """This method modifies the propagating data for an existing RotationalBodyForce object in
        the specified step.

        Parameters
        ----------
        stepName
            A String specifying the name of the step in which the load is modified.
        magnitude
            A Float specifying the load magnitude.
        amplitude
            A String or a SymbolicConstant specifying the name of the amplitude reference. Possible
            values for the SymbolicConstant are UNCHANGED and FREED. UNCHANGED should be used if the
            amplitude is propagated from the previous static analysis step. FREED should be used if
            the load is changed to have no amplitude reference. You should provide the **amplitude**
            argument only if it is valid for the specified step.
        """
        ...
