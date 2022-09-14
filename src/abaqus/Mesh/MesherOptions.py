from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from ..UtilityAndView.abaqusConstants import *


@abaqus_class_doc
class MesherOptions:
    """The MesherOptions object controls the default settings that Abaqus uses for all meshing
    methods. The MesherOptions object has no constructor. Abaqus creates the **MesherOptions**
    member when a session is started.
    MesherOptions commands are intended for use at the beginning of scripts and in the
    abaqus_v6.env file only; they should not be used during an Abaqus/CAE session.

    .. note:: 
        This object can be accessed by::

            session.defaultMesherOptions
    """

    @abaqus_method_doc
    def setValues(
        self,
        elemShape2D: SymbolicConstant = QUAD_DOMINATED,
        elemShape3D: SymbolicConstant = HEX,
        quadAlgorithm: SymbolicConstant = ADVANCING_FRONT,
        allowMapped: Boolean = OFF,
        minTransition: Boolean = ON,
        guiPreferredElements: SymbolicConstant = None,
    ):
        """This method modifies the MesherOptions object.

        Parameters
        ----------
        elemShape2D
            A SymbolicConstant specifying the default element shape for meshing two-dimensional
            objects. Possible values are QUAD, QUAD_DOMINATED, and TRI. The default value is
            QUAD_DOMINATED.
        elemShape3D
            A SymbolicConstant specifying the default element shape for meshing three-dimensional
            objects. Possible values are HEX, HEX_DOMINATED, WEDGE, and TET. The default value is
            HEX.
        quadAlgorithm
            A SymbolicConstant specifying the default algorithm for meshing an object with quad- or
            quad-dominated elements. Possible values are ADVANCING_FRONT and MEDIAL_AXIS. The
            default value is ADVANCING_FRONT.
        allowMapped
            A Boolean specifying whether Abaqus/CAE should allow mapped meshing, where appropriate.
            The default value is OFF.
        minTransition
            A Boolean specifying whether Abaqus/CAE should attempt to minimize the mesh transition
            when it moves from a coarse mesh to a fine mesh. The default value is ON.
        guiPreferredElements
            A list of SymbolicConstants specifying preferred Abaqus element types. This setting is
            relevant only when Abaqus/CAE is run interactively. When a part or part instance that
            has never been assigned an element type is meshed, this list is consulted. If an element
            type appropriate to the geometry is found in the list, it is assigned to the geometry.
            Multiple element types representing different shapes (for example, triangles and
            quadrilaterals) can be assigned in combination, but only element types that are
            compatible with each other are used. When more than one appropriate element type is
            found in the list, the first element type encountered takes precedence. This list is
            also consulted when populating the element type dialog; preferred types are selected by
            default for a region not previously assigned any element types. The default value is an
            empty list.

            .. versionadded:: 2018
                The `guiPreferredElements` argument was added.
        """
        ...
