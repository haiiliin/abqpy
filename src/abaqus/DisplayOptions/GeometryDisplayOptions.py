from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from ..UtilityAndView.abaqusConstants import *


@abaqus_class_doc
class GeometryDisplayOptions:
    """The GeometryDisplayOptions object stores settings that specify how assemblies are to be
    displayed in a particular viewport. The GeometryDisplayOptions object has no
    constructor. When you create a new viewport, the settings are copied from the current
    viewport.

    .. note::
        This object can be accessed by::

            session.viewports[name].assemblyDisplay.geometryOptions
            session.viewports[name].layers[name].assemblyDisplay.geometryOptions
            session.viewports[name].layers[name].partDisplay.geometryOptions
            session.viewports[name].partDisplay.geometryOptions
    """

    @abaqus_method_doc
    def setValues(
        self,
        geometryEdgesInShaded: Boolean = ON,
        geometryHiddenEdges: Boolean = OFF,
        geometrySilhouetteEdges: Boolean = ON,
        datumAxes: Boolean = ON,
        datumCoordSystems: Boolean = ON,
        datumPlanes: Boolean = ON,
        referencePointLabels: Boolean = ON,
        referencePointSymbols: Boolean = ON,
        referenceRepresentation: Boolean = OFF,
        referenceRepTranslucency: Boolean = ON,
    ):
        """This method modifies the GeometryDisplayOptions object.

        Parameters
        ----------
        geometryEdgesInShaded
            A Boolean specifying whether geometry edges are displayed in shaded mode. The default
            value is ON.
        geometryHiddenEdges
            A Boolean specifying whether geometry hidden edges are displayed (dotted) in hidden line
            mode. The default value is OFF.
        geometrySilhouetteEdges
            A Boolean specifying whether geometry silhouette edges are displayed. The default value
            is ON.
        datumAxes
            A Boolean specifying whether datum axes are shown. The default value is ON.
        datumCoordSystems
            A Boolean specifying whether datum coordinate systems are shown. The default value is
            ON.
        datumPlanes
            A Boolean specifying whether datum planes are shown. The default value is ON.
        referencePointLabels
            A Boolean specifying whether referencePoint labels are shown. The default value is ON.
        referencePointSymbols
            A Boolean specifying whether referencePoint symbols are shown. The default value is ON.
        referenceRepresentation
            A Boolean specifying whether geometry that belongs to the reference representation of
            the Part or Instance is shown. The default value is OFF.
        referenceRepTranslucency
            A Boolean specifying whether to apply translucency to the geometry that belongs to the
            reference representation of the Part or Instance. The default value is ON.

        Raises
        ------
        RangeError
        """
        ...
