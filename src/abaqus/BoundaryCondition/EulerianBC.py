from typing_extensions import Literal
from typing import Optional

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from .BoundaryCondition import BoundaryCondition
from ..Region.Region import Region
from ..UtilityAndView.abaqusConstants import abaqusConstants as C
from ..UtilityAndView.abaqusConstants import FREE, INFLOW, SymbolicConstant, ZERO_PRESSURE


@abaqus_class_doc
class EulerianBC(BoundaryCondition):
    """The EulerianBC object stores the data for an Eulerian boundary condition.
    The EulerianBC object is derived from the BoundaryCondition object.

    .. note:: 
        This object can be accessed by::

            import load
            mdb.models[name].boundaryConditions[name]
    """

    #: A String specifying the boundary condition repository key.
    name: str = ""

    #: A SymbolicConstant specifying the flow conditions to be defined. Possible values are
    #: INFLOW, OUTFLOW, and BOTH. The default value is INFLOW.
    definition: SymbolicConstant = INFLOW

    #: A SymbolicConstant specifying the control of material flow into the Eulerian domain.
    #: Possible values are FREE, NONE, and VOID. The default value is FREE.
    inflowType: SymbolicConstant = FREE

    #: A SymbolicConstant specifying the control of flow of material out of the Eulerian
    #: domain. Possible values are ZERO_PRESSURE, FREE, NON_REFLECTING, and EQUILIBRIUM. The
    #: default value is ZERO_PRESSURE.
    outflowType: SymbolicConstant = ZERO_PRESSURE

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
        definition: Literal[C.BOTH, C.INFLOW, C.OUTFLOW] = INFLOW,
        inflowType: Literal[C.VOID, C.FREE, C.NONE] = FREE,
        outflowType: Literal[C.FREE, C.ZERO_PRESSURE, C.EQUILIBRIUM, C.NON_REFLECTING] = ZERO_PRESSURE,
    ):
        """This method creates a EulerianBC object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].EulerianBC

        Parameters
        ----------
        name
            A String specifying the boundary condition repository key.
        createStepName
            A String specifying the name of the step in which the boundary condition is created.
        region
            A :py:class:`~abaqus.Region.Region.Region` object specifying the region to which the boundary condition is applied.
        definition
            A SymbolicConstant specifying the flow conditions to be defined. Possible values are
            INFLOW, OUTFLOW, and BOTH. The default value is INFLOW.
        inflowType
            A SymbolicConstant specifying the control of material flow into the Eulerian domain.
            Possible values are FREE, NONE, and VOID. The default value is FREE.
        outflowType
            A SymbolicConstant specifying the control of flow of material out of the Eulerian
            domain. Possible values are ZERO_PRESSURE, FREE, NON_REFLECTING, and EQUILIBRIUM. The
            default value is ZERO_PRESSURE.

        Returns
        -------
        EulerianBC
            An :py:class:`~abaqus.BoundaryCondition.EulerianBC.EulerianBC` object.
        """
        super().__init__()

    @abaqus_method_doc
    def setValues(
        self,
        region: Region,
        definition: Literal[C.BOTH, C.INFLOW, C.OUTFLOW] = INFLOW,
        inflowType: Literal[C.VOID, C.FREE, C.NONE] = FREE,
        outflowType: Literal[C.FREE, C.ZERO_PRESSURE, C.EQUILIBRIUM, C.NON_REFLECTING] = ZERO_PRESSURE,
    ):
        """This method modifies the data for an existing EulerianBC object in the step where it is
        created.

        Parameters
        ----------
        region
            A :py:class:`~abaqus.Region.Region.Region` object specifying the region to which the boundary condition is applied.
        definition
            A SymbolicConstant specifying the material flow conditions to be defined. Possible
            values are INFLOW, OUTFLOW, and BOTH. The default value is INFLOW.
        inflowType
            A SymbolicConstant specifying the control of material flow into the Eulerian domain.
            Possible values are FREE, NONE, and VOID. The default value is FREE.
        outflowType
            A SymbolicConstant specifying the control of material flow out of the Eulerian domain.
            Possible values are ZERO_PRESSURE, FREE, NON_REFLECTING, and EQUILIBRIUM. The default
            value is ZERO_PRESSURE.
        """
        ...

    @abaqus_method_doc
    def setValuesInStep(
        self,
        stepName: str,
        definition: Literal[C.BOTH, C.INFLOW, C.OUTFLOW] = INFLOW,
        inflowType: Literal[C.VOID, C.FREE, C.NONE] = FREE,
        outflowType: Literal[C.FREE, C.ZERO_PRESSURE, C.EQUILIBRIUM, C.NON_REFLECTING] = ZERO_PRESSURE,
    ):
        """This method modifies the propagating data for an existing EulerianBC object in the
        specified step.

        Parameters
        ----------
        stepName
            A String specifying the name of the step in which the boundary condition is modified.
        definition
            A SymbolicConstant specifying the material flow conditions to be defined. Possible
            values are INFLOW, OUTFLOW, and BOTH. The default value is INFLOW.
        inflowType
            A SymbolicConstant specifying the control of material flow into the Eulerian domain.
            Possible values are FREE, NONE, and VOID. The default value is FREE.
        outflowType
            A SymbolicConstant specifying the control of material flow out of the Eulerian domain.
            Possible values are ZERO_PRESSURE, FREE, NON_REFLECTING, and EQUILIBRIUM. The default
            value is ZERO_PRESSURE.
        """
        ...
