from __future__ import annotations

from .AFXObjectKeyword import AFXObjectKeyword
from .AFXProcedure import AFXProcedure
from .AFXStep import AFXStep
from .AFXTupleKeyword import AFXTupleKeyword


class AFXPickStep(AFXStep):
    """This class is used to provide pick steps in GUI procedures."""

    #: Allow only one entity to be picked.
    ONE: int = hash("ONE")

    #: Allow one or more entities to be picked.
    MANY: int = hash("MANY")

    #: Allow only straight entities to be picked.
    STRAIGHT: int = hash("STRAIGHT")

    #: Allow only wire entities to be picked.
    WIRE: int = hash("WIRE")

    #: Allow only planar entities to be picked.
    PLANAR: int = hash("PLANAR")

    #: Allow only conical entities to be picked.
    CONICAL: int = hash("CONICAL")

    #: Allow only shell entities to be picked.
    SHELL: int = hash("SHELL")

    #: Allow only orphan mesh entities to be picked.
    ORPHAN_MESH: int = hash("ORPHAN_MESH")

    #: Allow only solid entities to be picked.
    SOLID: int = hash("SOLID")

    #: Allow only geometry entities to be picked.
    GEOMETRY: int = hash("GEOMETRY")

    #: Allow only point entities to be picked.
    POINT: int = hash("POINT")

    #: Allow only background entities to be picked while sketching.
    BACKGROUND: int = hash("BACKGROUND")

    #: Allow only sketch entities to be picked.
    FOREGROUND: int = hash("FOREGROUND")

    #: Allow only vertical geometric sketch entities to be picked.
    VERTICAL: int = hash("VERTICAL")

    #: Allow only horizontal geometric sketch entities to be picked.
    HORIZONTAL: int = hash("HORIZONTAL")

    #: Allow only construction sketch entities to be picked.
    CONSTRUCTION: int = hash("CONSTRUCTION")

    #: Allow only non-construction geometric sketch entities to be picked.
    NO_CONSTRUCTION: int = hash("NO_CONSTRUCTION")

    #: Allow only spot sketch entities to be picked.
    SPOT: int = hash("SPOT")

    #: Allow only circular sketch entities to be picked.
    CIRCULAR: int = hash("CIRCULAR")

    #: Allow only interior entities to be picked.
    INTERIOR: int = hash("INTERIOR")

    #: Allow only exterior entities to be picked.
    EXTERIOR: int = hash("EXTERIOR")

    #: Allow vertices to be picked.
    VERTICES: int = hash("VERTICES")

    #: Allow edges to be picked.
    EDGES: int = hash("EDGES")

    #: Allow faces to be picked.
    FACES: int = hash("FACES")

    #: Allow cells to be picked.
    CELLS: int = hash("CELLS")

    #: Allow stringers to be picked.
    STRINGERS: int = hash("STRINGERS")

    #: Allow skins to be picked.
    SKINS: int = hash("SKINS")

    #: Allow element edges to be picked.
    ELEMENT_EDGES: int = hash("ELEMENT_EDGES")

    #: Allow element faces to be picked.
    ELEMENT_FACES: int = hash("ELEMENT_FACES")

    #: Allow nodes to be picked.
    NODES: int = hash("NODES")

    #: Allow elements to be picked.
    ELEMENTS: int = hash("ELEMENTS")

    #: Allow part instances in the model database to be picked.
    INSTANCES: int = hash("INSTANCES")

    #: Allow picking only objects of the highest dimension (1D, 2D, 3D).
    MAX_DIMENSION: int = hash("MAX_DIMENSION")

    #: Allow reference points to be picked.
    REFERENCE_POINTS: int = hash("REFERENCE_POINTS")

    #: Allow interesting points to be picked.
    INTERESTING_POINTS: int = hash("INTERESTING_POINTS")

    #: Allow datum points to be picked.
    DATUM_POINTS: int = hash("DATUM_POINTS")

    #: Allow datum axes to be picked.
    DATUM_AXES: int = hash("DATUM_AXES")

    #: Allow datsum planes be picked.
    DATUM_PLANES: int = hash("DATUM_PLANES")

    #: Allow datum CSYS's to be picked.
    DATUM_CSYS: int = hash("DATUM_CSYS")

    #: Allow edges to be removed from face selections.
    REMOVABLE_EDGES: int = hash("REMOVABLE_EDGES")

    #: Allow features to be picked.
    FEATURES: int = hash("FEATURES")

    #: Allow sketch vertices to be picked.
    SKETCH_VERTICES: int = hash("SKETCH_VERTICES")

    #: Allow sketch geometries to be picked.
    SKETCH_GEOMETRIES: int = hash("SKETCH_GEOMETRIES")

    #: Allow sketch dimensions to be picked.
    SKETCH_DIMENSIONS: int = hash("SKETCH_DIMENSIONS")

    #: Allow sketch constraints to be picked.
    SKETCH_CONSTRAINTS: int = hash("SKETCH_CONSTRAINTS")

    #: Allow sketch coordinates to be picked must add keyin.
    SKETCH_COORDINATES: int = hash("SKETCH_COORDINATES")

    #: Allow elements on skins to be picked.
    SKIN_ELEMENTS: int = hash("SKIN_ELEMENTS")

    #: Allow elements on stringers to be picked.
    STRINGER_ELEMENTS: int = hash("STRINGER_ELEMENTS")

    #: Allow all types of points to be picked.
    POINTS: int = hash("POINTS")

    #: Allow all types of lines to be picked.
    LINES: int = hash("LINES")

    #: Allow all types of planes to be picked.
    PLANES: int = hash("PLANES")

    #: Allow picking of XY coordinates from an XY plot.
    XY_POINT: int = hash("XY_POINT")

    #: Allow picking of XY coordinates from an XY plot, with the option to type in XY values.
    XY_COORDINATE: int = hash("XY_COORDINATE")

    #: Specify pick as a comma separated tuple of single items.
    TUPLE: int = hash("TUPLE")

    #: Specify pick as a plus separated sequence items.
    ARRAY: int = hash("ARRAY")

    def __init__(
        self,
        owner: AFXProcedure,
        keyword: AFXObjectKeyword,
        prompt: str,
        entitiesToPick: int,
        numberToPick=ONE,
        highlightLevel: int = 1,
        sequenceStyle=ARRAY,
    ):
        """Constructor.

        Parameters
        ----------
        owner : AFXProcedure
            Procedure creating the step.
        keyword : AFXObjectKeyword
            Object kwd containing pick variable. Part of AFXGuiCommand.
        prompt : str
            Step's prompt displayed in prompt area.
        entitiesToPick : int
            Type of entities to pick.
        numberToPick : pickAmountEnum
            How many entities to pick.
        highlightLevel : int
            Highlight level.
        sequenceStyle : sequenceStyleEnum
            Sequence style of picked variables in the command.
        """

    def addElementSetSelection(self, name: str):
        """Adds an element set to the step's selections.

        Parameters
        ----------
        name : str
            Name of set.
        """

    def addGeometrySetSelection(self, name: str):
        """Adds a geometry set to the step's selections.

        Parameters
        ----------
        name : str
            Name of set.
        """

    def addNodeSetSelection(self, name: str):
        """Adds a node set to the step's selections.

        Parameters
        ----------
        name : str
            Name of set.
        """

    def addPointKeyIn(self, keyword: AFXTupleKeyword):
        """Creates a textfield on the prompt line as an alternative method of specifying a point.

        Parameters
        ----------
        keyword : AFXTupleKeyword
            Keyword
        """

    def addSurfaceSelection(self, name: str):
        """Adds a surface to the step's selections.

        Parameters
        ----------
        name : str
            Name of surface.
        """

    def allowRepeatedSelections(self, value: bool = True):
        """Allows the picking of prior selections (from prior pick steps of the procedure).

        Parameters
        ----------
        value : bool
            If True, allow repeated selections between steps.
        """

    def onCancel(self):
        """Called when the step is cancelled.

        Reimplemented from AFXStep. Reimplemented in AFXOrderedPickStep.
        """

    def onExecute(self):
        """Called to execute the steps returned by getFirstStep and getNextStep.

        Reimplemented from AFXStep. Reimplemented in AFXOrderedPickStep.
        """

    def onResume(self):
        """Called when the step is resumed.

        Reimplemented from AFXStep.
        """

    def onSuspend(self):
        """Called when the step is suspended.

        Reimplemented from AFXStep.
        """

    def reset(self):
        """Allows a step to reset any of its data (if needed) when looping.

        Reimplemented from AFXStep. Reimplemented in AFXOrderedPickStep.
        """

    def setEdgeRefinements(self, refinement: int):
        """Sets the refinements to be used when picking edges.

        Parameters
        ----------
        refinement : int
            Refinement flag.
        """

    def setElementEdgeRefinements(self, refinement: int):
        """Sets the refinements to be used when picking element edges.

        Parameters
        ----------
        refinement : int
            Refinement flag.
        """

    def setElementFaceRefinements(self, refinement: int):
        """Sets the refinements to be used when picking element faces.

        Parameters
        ----------
        refinement : int
            Refinement flag.
        """

    def setElementRefinements(self, refinement: int):
        """Sets the refinements to be used when picking elements.

        Parameters
        ----------
        refinement : int
            Refinement flag.
        """

    def setFaceRefinements(self, refinement: int):
        """Sets the refinements to be used when picking faces.

        Parameters
        ----------
        refinement : int
            Refinement flag.
        """

    def setInstanceRefinements(self, refinement: int):
        """Sets the refinements to be used when picking instances.

        Parameters
        ----------
        refinement : int
            Refinement flag.
        """

    def setNodeRefinements(self, refinement: int):
        """Sets the refinements to be used when picking nodes.

        Parameters
        ----------
        refinement : int
            Refinement flag.
        """

    def setSketchRefinements(self, refinement: int):
        """Sets the refinements to be used when picking sketches.

        Parameters
        ----------
        refinement : int
            Refinement flag.
        """

    def setXyRefinements(self, refinement: int):
        """Sets the refinements to be used when picking xy objects.

        Parameters
        ----------
        refinement : int
            Refinement flag.
        """
