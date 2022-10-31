from typing import Dict, Sequence

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from typing_extensions import Literal

from .BCDisplayOptions import BCDisplayOptions
from .ConstraintDisplayOptions import ConstraintDisplayOptions
from .EngineeringFeatureDisplayOptions import EngineeringFeatureDisplayOptions
from .GeometricRestrictionDisplayOptions import GeometricRestrictionDisplayOptions
from .GeometryDisplayOptions import GeometryDisplayOptions
from .InteractionDisplayOptions import InteractionDisplayOptions
from .LoadDisplayOptions import LoadDisplayOptions
from .MeshDisplayOptions import MeshDisplayOptions
from .OptimizationTaskDisplayOptions import OptimizationTaskDisplayOptions
from .PredefinedFieldDisplayOptions import PredefinedFieldDisplayOptions
from .StopConditionDisplayOptions import StopConditionDisplayOptions
from .SymbolDisplayOptions import SymbolDisplayOptions
from ..DisplayGroup.DisplayGroup import DisplayGroup
from ..DisplayGroup.DisplayGroupInstance import DisplayGroupInstance
from ..DisplayGroup.Leaf import Leaf
from ..UtilityAndView.abaqusConstants import Boolean, EMPTY_LEAF, OFF, ON, SymbolicConstant, WIREFRAME
from ..UtilityAndView.abaqusConstants import abaqusConstants as C


@abaqus_class_doc
class AssemblyDisplayOptions:
    """The AssemblyDisplayOptions object stores settings that specify how assemblies are to be
    displayed in a particular viewport. The AssemblyDisplayOptions object has no
    constructor. When you create a new viewport, the settings are copied from the current
    viewport.

    .. note::
        This object can be accessed by::

            import assembly
            session.viewports[name].assemblyDisplay
            session.viewports[name].layers[name].assemblyDisplay
    """

    #: A Boolean specifying whether boundary conditions are shown. The default value is OFF.
    bcs: Boolean = OFF

    #: A Boolean specifying whether connectors are shown. The default value is OFF.
    connectors: Boolean = OFF

    #: A Boolean specifying whether the connector end points are shown. This member is
    #: applicable only if **connectors** = ON. The default value is ON.
    cnxEndPoints: Boolean = ON

    #: A Boolean specifying whether the connector local coordinate system axes are shown. This
    #: member is applicable only if **connectors** = ON. The default value is ON.
    cnxLocalAxes: Boolean = ON

    #: A Boolean specifying whether the connector section type labels are shown. This member is
    #: applicable only if **connectors** = ON. The default value is ON.
    cnxTypeLabels: Boolean = ON

    #: A Boolean specifying whether the tag information is displayed along with the connector
    #: section type labels. This member is applicable only if **connectors** = ON and if
    #: **cnxTypeLabels** = ON. The default value is OFF.
    cnxTagDisplay: Boolean = OFF

    #: A Boolean specifying whether constraints are shown. The default value is OFF.
    constraints: Boolean = OFF

    #: A Boolean specifying whether to display engineering features. The default value is OFF.
    engineeringFeatures: Boolean = OFF

    #: A Boolean specifying whether geometric restrictions are shown. The default value is OFF.
    geometricRestrictions: Boolean = OFF

    #: A Boolean specifying whether to render the beam profiles. The default value is OFF.
    renderBeamProfiles: Boolean = OFF

    #: A Float specifying the beam profile scale factor. The beamScaleFactor must be greater
    #: than zero. The default value is 1.0.
    beamScaleFactor: float = 1

    #: A Boolean specifying whether fields and initial conditions are shown. The default value
    #: is OFF.
    predefinedFields: Boolean = OFF

    #: A Boolean specifying whether interactions are shown. The default value is OFF.
    interactions: Boolean = OFF

    #: A Boolean specifying whether loads are shown. The default value is OFF.
    loads: Boolean = OFF

    #: A Boolean specifying whether the mesh is shown. The default value is OFF.
    mesh: Boolean = OFF

    #: A Boolean specifying whether optimization tasks are shown. The default value is OFF.
    optimizationTasks: Boolean = OFF

    #: A Boolean specifying whether stop conditions are shown. The default value is OFF.
    stopConditions: Boolean = OFF

    #: A SymbolicConstant specifying how the image in the viewport is rendered. Possible values
    #: are WIREFRAME, HIDDEN, SHADED, and FILLED. The default value is WIREFRAME.
    renderStyle: SymbolicConstant = WIREFRAME

    #: A BCDisplayOptions object.
    bcOptions: BCDisplayOptions = BCDisplayOptions()

    #: A ConstraintDisplayOptions object.
    constraintOptions: ConstraintDisplayOptions = ConstraintDisplayOptions()

    #: A DisplayGroup object specifying the current display group and referring to an object in
    #: the **displayGroups** member of Session.
    displayGroup: DisplayGroup = DisplayGroup("dg", Leaf(EMPTY_LEAF))

    #: A repository of DisplayGroupInstance objects.
    displayGroupInstances: Dict[str, DisplayGroupInstance] = {}

    #: An EngineeringFeatureDisplayOptions object.
    engineeringFeatureOptions: EngineeringFeatureDisplayOptions = EngineeringFeatureDisplayOptions()

    #: A PredefinedFieldDisplayOptions object.
    predefinedFieldOptions: PredefinedFieldDisplayOptions = PredefinedFieldDisplayOptions()

    #: A GeometricRestrictionDisplayOptions object.
    geometricRestrictionOptions: GeometricRestrictionDisplayOptions = GeometricRestrictionDisplayOptions()

    #: A GeometryDisplayOptions object.
    geometryOptions: GeometryDisplayOptions = GeometryDisplayOptions()

    #: An InteractionDisplayOptions object.
    interactionOptions: InteractionDisplayOptions = InteractionDisplayOptions()

    #: A LoadDisplayOptions object.
    loadOptions: LoadDisplayOptions = LoadDisplayOptions()

    #: A MeshDisplayOptions object.
    meshOptions: MeshDisplayOptions = MeshDisplayOptions()

    #: An OptimizationTaskDisplayOptions object.
    optimizationTaskOptions: OptimizationTaskDisplayOptions = OptimizationTaskDisplayOptions()

    #: A StopConditionDisplayOptions object.
    stopConditionOptions: StopConditionDisplayOptions = StopConditionDisplayOptions()

    #: A SymbolDisplayOptions object.
    symbolOptions: SymbolDisplayOptions = SymbolDisplayOptions()

    #: A tuple of Strings specifying the names of the part instances that are visible in the
    #: viewport. The default value is an empty sequence.
    visibleInstances: tuple = ()

    #: A String specifying the step for which objects are to be displayed. Possible values are
    #: any valid step name. The default value is "Initial".
    step: str = ""

    @abaqus_method_doc
    def setValues(
        self,
        visibleInstances: tuple = (),
        step: str = "",
        renderStyle: Literal[C.SHADED, C.FILLED, C.WIREFRAME, C.HIDDEN] = WIREFRAME,
        mesh: Boolean = OFF,
        loads: Boolean = OFF,
        bcs: Boolean = OFF,
        interactions: Boolean = OFF,
        constraints: Boolean = OFF,
        connectors: Boolean = OFF,
        cnxEndPoints: Boolean = ON,
        cnxLocalAxes: Boolean = ON,
        cnxTypeLabels: Boolean = ON,
        cnxTagDisplay: Boolean = OFF,
        predefinedFields: Boolean = OFF,
        visibleDisplayGroups: Sequence[DisplayGroup] = (),
        engineeringFeatures: Boolean = OFF,
        renderBeamProfiles: Boolean = OFF,
        beamScaleFactor: float = 1,
        optimizationTasks: Boolean = OFF,
        geometricRestrictions: Boolean = OFF,
        stopConditions: Boolean = OFF,
    ):
        """This method modifies the AssemblyDisplayOptions object.

        Parameters
        ----------
        visibleInstances
            A sequence of Strings specifying the names of the part instances that are visible in the
            viewport. The default value is an empty sequence.
        step
            A String specifying the step for which objects are to be displayed. Possible values are
            any valid step name. The default value is "Initial".
        renderStyle
            A SymbolicConstant specifying how the image in the viewport is rendered. Possible values
            are WIREFRAME, HIDDEN, SHADED, and FILLED. The default value is WIREFRAME.
        mesh
            A Boolean specifying whether the mesh is shown. The default value is OFF.
        loads
            A Boolean specifying whether loads are shown. The default value is OFF.
        bcs
            A Boolean specifying whether boundary conditions are shown. The default value is OFF.
        interactions
            A Boolean specifying whether interactions are shown. The default value is OFF.
        constraints
            A Boolean specifying whether constraints are shown. The default value is OFF.
        connectors
            A Boolean specifying whether connectors are shown. The default value is OFF.
        cnxEndPoints
            A Boolean specifying whether the connector end points are shown. This member is
            applicable only if **connectors** = ON. The default value is ON.
        cnxLocalAxes
            A Boolean specifying whether the connector local coordinate system axes are shown. This
            member is applicable only if **connectors** = ON. The default value is ON.
        cnxTypeLabels
            A Boolean specifying whether the connector section type labels are shown. This member is
            applicable only if **connectors** = ON. The default value is ON.
        cnxTagDisplay
            A Boolean specifying whether the tag information is displayed along with the connector
            section type labels. This member is applicable only if **connectors** = ON and if
            **cnxTypeLabels** = ON. The default value is OFF.
        predefinedFields
            A Boolean specifying whether fields and initial conditions are shown. The default value
            is OFF.
        visibleDisplayGroups
            A sequence of DisplayGroup objects specifying the DisplayGroups visible in the viewport.
            Currently the sequence can contain a maximum of one DisplayGroup object. The default
            value is an empty sequence.
        engineeringFeatures
            A Boolean specifying whether to display engineering features. The default value is OFF.
        renderBeamProfiles
            A Boolean specifying whether to render the beam profiles. The default value is OFF.
        beamScaleFactor
            A Float specifying the beam profile scale factor. The beamScaleFactor must be greater
            than zero. The default value is 1.0.
        optimizationTasks
            A Boolean specifying whether optimization tasks are shown. The default value is OFF.
        geometricRestrictions
            A Boolean specifying whether geometric restrictions are shown. The default value is OFF.
        stopConditions
            A Boolean specifying whether stop conditions are shown. The default value is OFF.

        Raises
        ------
        RangeError
        """
        ...
