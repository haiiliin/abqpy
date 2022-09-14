from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from ..UtilityAndView.abaqusConstants import *


@abaqus_class_doc
class GeometricRestrictionDisplayOptions:
    """The GeometricRestrictionDisplayOptions object stores settings that specify how
    assemblies are to be displayed in a particular viewport when
    session.viewports[name].assemblyDisplay.geometricRestrictions=ON
    The GeometricRestrictionDisplayOptions object has no constructor. When you create a new
    viewport, the settings are copied from the current viewport.

    .. note::
        This object can be accessed by::
        
            session.viewports[name].assemblyDisplay.geometricRestrictionOptions
            session.viewports[name].layers[name].assemblyDisplay.geometricRestrictionOptions
    """

    @abaqus_method_doc
    def setValues(
        self,
        drillControl: Boolean = ON,
        fixedRegion: Boolean = ON,
        frozenArea: Boolean = ON,
        growth: Boolean = ON,
        penetrationCheck: Boolean = ON,
        shapeDemoldControl: Boolean = ON,
        designDirection: Boolean = ON,
        shapeMemberSize: Boolean = ON,
        shapePlanarSymmetry: Boolean = ON,
        shapePointSymmetry: Boolean = ON,
        shapeRotationalSymmetry: Boolean = ON,
        stampControl: Boolean = ON,
        slideRegionControl: Boolean = ON,
        topologyCyclicSymmetry: Boolean = ON,
        topologyDemoldControl: Boolean = ON,
        topologyMemberSize: Boolean = ON,
        topologyPlanarSymmetry: Boolean = ON,
        topologyPointSymmetry: Boolean = ON,
        topologyRotationalSymmetry: Boolean = ON,
        turnControl: Boolean = ON,
    ):
        """This method modifies the GeometricRestrictionDisplayOptions object.

        Parameters
        ----------
        drillControl
            A Boolean specifying whether drill control geometric restriction symbols are shown. The
            default value is ON.
        fixedRegion
            A Boolean specifying whether fixed region geometric restriction symbols are shown. The
            default value is ON.
        frozenArea
            A Boolean specifying whether frozen area geometric restriction symbols are shown. The
            default value is ON.
        growth
            A Boolean specifying whether growth geometric restriction symbols are shown. The default
            value is ON.
        penetrationCheck
            A Boolean specifying whether penetration check geometric restriction symbols are shown.
            The default value is ON.
        shapeDemoldControl
            A Boolean specifying whether demold control (shape) geometric restriction symbols are
            shown. The default value is ON.
        designDirection
            A Boolean specifying whether design direction geometric restriction symbols are shown.
            The default value is ON.
        shapeMemberSize
            A Boolean specifying whether member size (shape) geometric restriction symbols are
            shown. The default value is ON.
        shapePlanarSymmetry
            A Boolean specifying whether planar symmetry (shape) geometric restriction symbols are
            shown. The default value is ON.
        shapePointSymmetry
            A Boolean specifying whether point symmetry (shape) geometric restriction symbols are
            shown. The default value is ON.
        shapeRotationalSymmetry
            A Boolean specifying whether rotational symmetry (shape) geometric restriction symbols
            are shown. The default value is ON.
        stampControl
            A Boolean specifying whether stamp control geometric restriction symbols are shown. The
            default value is ON.
        slideRegionControl
            A Boolean specifying whether slide region control geometric restriction symbols are
            shown. The default value is ON.
        topologyCyclicSymmetry
            A Boolean specifying whether cyclic symmetry geometric restriction symbols are shown.
            The default value is ON.
        topologyDemoldControl
            A Boolean specifying whether demold control (topology) geometric restriction symbols are
            shown. The default value is ON.
        topologyMemberSize
            A Boolean specifying whether member size (topology) geometric restriction symbols are
            shown. The default value is ON.
        topologyPlanarSymmetry
            A Boolean specifying whether planar symmetry (topology) geometric restriction symbols
            are shown. The default value is ON.
        topologyPointSymmetry
            A Boolean specifying whether point symmetry (topology) geometric restriction symbols are
            shown. The default value is ON.
        topologyRotationalSymmetry
            A Boolean specifying whether rotational symmetry (topology) geometric restriction
            symbols are shown. The default value is ON.
        turnControl
            A Boolean specifying whether turn control geometric restriction symbols are shown. The
            default value is ON.

        Raises
        ------
        RangeError
        """
        ...
