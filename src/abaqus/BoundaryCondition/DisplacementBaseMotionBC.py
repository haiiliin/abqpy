import typing
from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from .BoundaryCondition import BoundaryCondition
from ..Amplitude.Correlation import Correlation
from ..Region.Region import Region
from ..UtilityAndView.abaqusConstants import *


@abaqus_class_doc
class DisplacementBaseMotionBC(BoundaryCondition):
    """The DisplacementBaseMotionBC object stores the data for a displacement base motion
    boundary condition.
    The DisplacementBaseMotionBC object is derived from the BoundaryCondition object.

    .. note:: 
        This object can be accessed by::

            import load
            mdb.models[name].boundaryConditions[name]
    """

    #: A String specifying the boundary condition repository key.
    name: str = ""

    #: A Float specifying the scale factor for the amplitude curve. The default value is 1.0.
    amplitudeScaleFactor: float = 1

    #: A Boolean specifying whether to define the imaginary (out-of-plane) portion of the base
    #: motion record given by amplitude definition. The default value is OFF.
    useComplex: Boolean = OFF

    #: A :py:class:`~abaqus.BasicGeometry.ModelDot.ModelDot` object specifying a tuple containing one center of rotation. The default
    #: value is the global origin. This argument applies only when **dof** = UR1, UR2, or UR3.
    centerOfRotation: tuple = ()

    #: A :py:class:`~abaqus.Amplitude.Correlation.Correlation` object.
    correlation: Correlation = Correlation()

    #: A String specifying the name of the SecondaryBaseBC object associated with this boundary
    #: condition. The default value is an empty string.
    secondaryBase: str = ""

    #: A SymbolicConstant specifying the category of the boundary condition. Possible values
    #: are MECHANICAL and THERMAL.
    category: typing.Optional[SymbolicConstant] = None

    #: A :py:class:`~abaqus.Region.Region.Region` object specifying the region to which the boundary condition is applied.
    region: Region = Region()

    #: None or a DatumCsys object specifying the local coordinate system of the boundary
    #: condition's degrees of freedom. If **localCsys** = None, the degrees of freedom are defined
    #: in the global coordinate system. The default value is None.
    localCsys: typing.Optional[str] = None

    @abaqus_method_doc
    def __init__(
        self,
        name: str,
        createStepName: str,
        dof: SymbolicConstant,
        amplitudeScaleFactor: float = 1,
        centerOfRotation: tuple = (),
        correlation: typing.Optional[Correlation] = None,
        secondaryBase: str = "",
        useComplex: Boolean = OFF,
        amplitude: str = UNSET,
    ):
        """This method creates a DisplacementBaseMotionBC object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].DisplacementBaseMotionBC

        Parameters
        ----------
        name
            A String specifying the boundary condition repository key.
        createStepName
            A String specifying the name of the step in which the boundary condition is created.
        dof
            A SymbolicConstant specifying the constrained degree-of-freedom. Possible values for the
            SymbolicConstant are U1, U2, U3, UR1, UR2, UR3. The default value is U1.
        amplitudeScaleFactor
            A Float specifying the scale factor for the amplitude curve. The default value is 1.0.
        centerOfRotation
            A :py:class:`~abaqus.BasicGeometry.ModelDot.ModelDot` object specifying a tuple containing one center of rotation. The default
            value is the global origin. This argument applies only when **dof** = UR1, UR2, or UR3.
        correlation
            A :py:class:`~abaqus.Amplitude.Correlation.Correlation` object.
        secondaryBase
            A String specifying the name of the SecondaryBaseBC object associated with this boundary
            condition. The default value is an empty string.
        useComplex
            A Boolean specifying whether to define the imaginary (out-of-plane) portion of the base
            motion record given by amplitude definition. The default value is OFF.
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
            UNSET should be used if the boundary condition has no amplitude reference. The default
            value is UNSET. You should provide the **amplitude** argument only if it is valid for the
            specified step.

        Returns
        -------
        DisplacementBaseMotionBC
            A :py:class:`~abaqus.BoundaryCondition.DisplacementBaseMotionBC.DisplacementBaseMotionBC` object.
        """
        super().__init__()

    @abaqus_method_doc
    def setValues(
        self,
        amplitudeScaleFactor: float = 1,
        centerOfRotation: tuple = (),
        correlation: typing.Optional[Correlation] = None,
        secondaryBase: str = "",
        useComplex: Boolean = OFF,
        amplitude: str = UNSET,
    ):
        """This method modifies the data for an existing DisplacementBaseMotionBC object in the
        step where it is created.

        Parameters
        ----------
        amplitudeScaleFactor
            A Float specifying the scale factor for the amplitude curve. The default value is 1.0.
        centerOfRotation
            A :py:class:`~abaqus.BasicGeometry.ModelDot.ModelDot` object specifying a tuple containing one center of rotation. The default
            value is the global origin. This argument applies only when **dof** = UR1, UR2, or UR3.
        correlation
            A :py:class:`~abaqus.Amplitude.Correlation.Correlation` object.
        secondaryBase
            A String specifying the name of the SecondaryBaseBC object associated with this boundary
            condition. The default value is an empty string.
        useComplex
            A Boolean specifying whether to define the imaginary (out-of-plane) portion of the base
            motion record given by amplitude definition. The default value is OFF.
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
            UNSET should be used if the boundary condition has no amplitude reference. The default
            value is UNSET. You should provide the **amplitude** argument only if it is valid for the
            specified step.
        """
        ...

    @abaqus_method_doc
    def setValuesInStep(self, stepName: str, amplitude: str = ""):
        """This method modifies the propagating data for an existing DisplacementBaseMotionBC
        object in the specified step.

        Parameters
        ----------
        stepName
            A String specifying the name of the step in which the boundary condition is modified.
        amplitude
            A String or a SymbolicConstant specifying the name of the amplitude reference. Possible
            values for the SymbolicConstant are UNCHANGED and FREED. UNCHANGED should be used if the
            amplitude is propagated from the previous analysis step. FREED should be used if the
            boundary condition is changed to have no amplitude reference. You should provide the
            **amplitude** argument only if it is valid for the specified step.
        """
        ...
