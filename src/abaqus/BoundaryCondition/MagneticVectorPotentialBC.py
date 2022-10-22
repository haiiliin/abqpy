from typing_extensions import Literal
from typing import Optional

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from .BoundaryCondition import BoundaryCondition
from ..Region.Region import Region
from ..UtilityAndView.abaqusConstants import abaqusConstants as C
from ..UtilityAndView.abaqusConstants import SymbolicConstant, UNIFORM, UNSET


@abaqus_class_doc
class MagneticVectorPotentialBC(BoundaryCondition):
    """The MagneticVectorPotentialBC object stores the data for a magnetic vector potential
    boundary condition.
    The MagneticVectorPotentialBC object is derived from the BoundaryCondition object.

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
        component1: Optional[Literal[C.SET, C.UNSET]] = None,
        component2: Literal[C.SET, C.UNSET] = UNSET,
        component3: Literal[C.SET, C.UNSET] = UNSET,
        amplitude: str = UNSET,
        distributionType: Literal[C.USER_DEFINED, C.UNIFORM] = UNIFORM,
        localCsys: Optional[str] = None,
    ):
        """This method creates a MagneticVectorPotentialBC object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].MagneticVectorPotentialBC

        Parameters
        ----------
        name
            A String specifying the boundary condition repository key.
        createStepName
            A String specifying the name of the step in which the boundary condition is created.
        region
            A :py:class:`~abaqus.Region.Region.Region` object specifying the region to which the boundary condition is applied.
        component1
            A Complex, or a SymbolicConstant specifying the magnetic vector potential component in
            the 1-direction. Possible values for the SymbolicConstant are UNSET and SET. The default
            value is UNSET
        component2
            A Complex, or a SymbolicConstant specifying the magnetic vector potential component in
            the 2-direction. Possible values for the SymbolicConstant are UNSET and SET. The default
            value is UNSET.
        component3
            A Complex, or a SymbolicConstant specifying the magnetic vector potential component in
            the 3-direction. Possible values for the SymbolicConstant are UNSET and SET. The default
            value is UNSET.
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
            UNSET should be used if the boundary condition has no amplitude reference. The default
            value is UNSET. You should provide the **amplitude** argument only if it is valid for the
            specified step.
        distributionType
            A SymbolicConstant specifying how the boundary condition is distributed spatially.
            Possible values are UNIFORM and USER_DEFINED. The default value is UNIFORM.
        localCsys
            None or a DatumCsys object specifying the local coordinate system of the boundary
            condition's degrees of freedom. If **localCsys** = None, the degrees of freedom are defined
            in the global coordinate system. The default value is None.

        Returns
        -------
        MagneticVectorPotentialBC
            A :py:class:`~abaqus.BoundaryCondition.MagneticVectorPotentialBC.MagneticVectorPotentialBC` object.
        """
        super().__init__()

    @abaqus_method_doc
    def setValues(
        self,
        component1: Optional[Literal[C.SET, C.UNSET]] = None,
        component2: Literal[C.SET, C.UNSET] = UNSET,
        component3: Literal[C.SET, C.UNSET] = UNSET,
        amplitude: str = UNSET,
        distributionType: Literal[C.USER_DEFINED, C.UNIFORM] = UNIFORM,
        localCsys: Optional[str] = None,
    ):
        """This method modifies the data for an existing MagneticVectorPotentialBC object in the
        step where it is created.

        Parameters
        ----------
        component1
            A Complex, or a SymbolicConstant specifying the magnetic vector potential component in
            the 1-direction. Possible values for the SymbolicConstant are UNSET and SET. The default
            value is UNSET
        component2
            A Complex, or a SymbolicConstant specifying the magnetic vector potential component in
            the 2-direction. Possible values for the SymbolicConstant are UNSET and SET. The default
            value is UNSET.
        component3
            A Complex, or a SymbolicConstant specifying the magnetic vector potential component in
            the 3-direction. Possible values for the SymbolicConstant are UNSET and SET. The default
            value is UNSET.
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
            UNSET should be used if the boundary condition has no amplitude reference. The default
            value is UNSET. You should provide the **amplitude** argument only if it is valid for the
            specified step.
        distributionType
            A SymbolicConstant specifying how the boundary condition is distributed spatially.
            Possible values are UNIFORM and USER_DEFINED. The default value is UNIFORM.
        localCsys
            None or a DatumCsys object specifying the local coordinate system of the boundary
            condition's degrees of freedom. If **localCsys** = None, the degrees of freedom are defined
            in the global coordinate system. The default value is None.
        """
        ...

    @abaqus_method_doc
    def setValuesInStep(
        self,
        stepName: str,
        component1: Optional[Literal[C.SET, C.UNCHANGED]] = None,
        component2: Optional[Literal[C.SET, C.UNCHANGED]] = None,
        component3: Optional[Literal[C.UNCHANGED]] = None,
        amplitude: str = "",
    ):
        """This method modifies the propagating data for an existing MagneticVectorPotentialBC
        object in the specified step.

        Parameters
        ----------
        stepName
            A String specifying the name of the step in which the boundary condition is modified.
        component1
            A Complex, or a SymbolicConstant specifying the magnetic vector potential component in
            the 1-direction. Possible values for the SymbolicConstant are SET and UNCHANGED.
        component2
            A Complex, or a SymbolicConstant specifying the magnetic vector potential component in
            the 2-direction. Possible values for the SymbolicConstant are SET and UNCHANGED.
        component3
            A Complex, or a SymbolicConstant specifying the magnetic vector potential component in
            the 3-direction. Possible values for the SymbolicConstant areSET and UNCHANGED.
        amplitude
            A String or a SymbolicConstant specifying the name of the amplitude reference. Possible
            values for the SymbolicConstant are UNCHANGED and FREED. UNCHANGED should be used if the
            amplitude is propagated from the previous analysis step. FREED should be used if the
            boundary condition is changed to have no amplitude reference. You should provide the
            **amplitude** argument only if it is valid for the specified step.
        """
        ...
