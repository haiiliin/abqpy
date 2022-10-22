from typing_extensions import Literal
from typing import Optional

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from .Load import Load
from ..Region.Region import Region
from ..UtilityAndView.abaqusConstants import abaqusConstants as C
from ..UtilityAndView.abaqusConstants import SymbolicConstant, UNIFORM, UNSET


@abaqus_class_doc
class Pressure(Load):
    """The Pressure object defines a pressure load.
    The Pressure object is derived from the Load object.

    .. note:: 
        This object can be accessed by::

            import load
            mdb.models[name].loads[name]
    """

    #: A String specifying the load repository key.
    name: str = ""

    #: A SymbolicConstant specifying how the pressure is distributed spatially. Possible values
    #: are UNIFORM, USER_DEFINED, FIELD, HYDROSTATIC, STAGNATION, VISCOUS, TOTAL_FORCE, and
    #: DISCRETE_FIELD. The default value is UNIFORM.
    distributionType: SymbolicConstant = UNIFORM

    #: A String specifying the name of the AnalyticalField or DiscreteField object associated
    #: with this load. The **field** argument applies only when **distributionType** = FIELD or
    #: **distributionType** = DISCRETE_FIELD. The default value is an empty string.
    field: str = ""

    #: A :py:class:`~abaqus.Region.Region.Region` object specifying the region to which the load is applied.
    region: Region = Region()

    @abaqus_method_doc
    def __init__(
        self,
        name: str,
        createStepName: str,
        region: Region,
        magnitude: float = 0.0,
        hZero: float = 0.0,
        hReference: float = 0.0,
        field: str = "",
        refPoint: str = "",
        distributionType: Literal[C.FIELD, C.DISCRETE_FIELD, C.STAGNATION, C.VISCOUS, C.TOTAL_FORCE, C.HYDROSTATIC, C.UNIFORM, C.USER_DEFINED] = UNIFORM,
        amplitude: str = UNSET,
    ):
        """This method creates a Pressure object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].Pressure

        Parameters
        ----------
        name
            A String specifying the load repository key.
        createStepName
            A String specifying the name of the step in which the pressure is created.
        region
            A :py:class:`~abaqus.Region.Region.Region` object specifying the region to which the load is applied.
        magnitude
            A Float or a Complex specifying the pressure magnitude.Note:*magnitude* is optional if
            **distributionType** = USER_DEFINED.
        hZero
            A Float specifying the height of the zero pressure level when
            **distributionType** = HYDROSTATIC.
        hReference
            A Float specifying the height of the reference pressure level when
            **distributionType** = HYDROSTATIC.
        field
            A String specifying the name of the AnalyticalField or DiscreteField object associated
            with this load. The **field** argument applies only when **distributionType** = FIELD or
            **distributionType** = DISCRETE_FIELD. The default value is an empty string.
        refPoint
            A Region specifying the reference point from which the relative velocity is determined
            when **distributionType** = STAGNATION or VISCOUS.
        distributionType
            A SymbolicConstant specifying how the pressure is distributed spatially. Possible values
            are UNIFORM, USER_DEFINED, FIELD, HYDROSTATIC, STAGNATION, VISCOUS, TOTAL_FORCE, and
            DISCRETE_FIELD. The default value is UNIFORM.
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
            UNSET should be used if the load has no amplitude reference. The default value is UNSET.
            You should provide the **amplitude** argument only if it is valid for the specified step.

        Returns
        -------
        Pressure
            A :py:class:`~abaqus.Load.Pressure.Pressure` object.
        """
        super().__init__()

    @abaqus_method_doc
    def setValues(
        self,
        field: str = "",
        refPoint: str = "",
        distributionType: Literal[C.FIELD, C.DISCRETE_FIELD, C.STAGNATION, C.VISCOUS, C.TOTAL_FORCE, C.HYDROSTATIC, C.UNIFORM, C.USER_DEFINED] = UNIFORM,
        amplitude: str = UNSET,
    ):
        """This method modifies the data for an existing Pressure object in the step where it is
        created.

        Parameters
        ----------
        field
            A String specifying the name of the AnalyticalField or DiscreteField object associated
            with this load. The **field** argument applies only when **distributionType** = FIELD or
            **distributionType** = DISCRETE_FIELD. The default value is an empty string.
        refPoint
            A Region specifying the reference point from which the relative velocity is determined
            when **distributionType** = STAGNATION or VISCOUS.
        distributionType
            A SymbolicConstant specifying how the pressure is distributed spatially. Possible values
            are UNIFORM, USER_DEFINED, FIELD, HYDROSTATIC, STAGNATION, VISCOUS, TOTAL_FORCE, and
            DISCRETE_FIELD. The default value is UNIFORM.
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
            UNSET should be used if the load has no amplitude reference. The default value is UNSET.
            You should provide the **amplitude** argument only if it is valid for the specified step.
        """
        ...

    @abaqus_method_doc
    def setValuesInStep(
        self,
        stepName: str,
        magnitude: Optional[float] = None,
        hZero: Optional[float] = None,
        hReference: Optional[float] = None,
        amplitude: str = "",
    ):
        """This method modifies the propagating data for an existing Pressure object in the
        specified step.

        Parameters
        ----------
        stepName
            A String specifying the name of the step in which the load is modified.
        magnitude
            A Float or a Complex specifying the pressure magnitude.
        hZero
            A Float specifying the height of the zero pressure level when
            **distributionType** = HYDROSTATIC.
        hReference
            A Float specifying the height of the reference pressure level when
            **distributionType** = HYDROSTATIC.
        amplitude
            A String or a SymbolicConstant specifying the name of the amplitude reference. Possible
            values for the SymbolicConstant are UNCHANGED and FREED. UNCHANGED should be used if the
            amplitude is propagated from the previous analysis step. FREED should be used if the
            load has no amplitude reference. You should provide the **amplitude** argument only if it
            is valid for the specified step.
        """
        ...
