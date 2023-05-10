from typing_extensions import Literal

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from .._OptionsBase import _OptionsBase
from ..UtilityAndView.abaqusConstants import (
    OFF,
    ON,
    SHADED,
    SOLID,
    UNSYMMETRIC,
    VERY_THIN,
    Boolean,
    SymbolicConstant,
)
from ..UtilityAndView.abaqusConstants import abaqusConstants as C


@abaqus_class_doc
class PlyStackPlotOptions(_OptionsBase):
    """The PlyStackPlotOptions object stores values and attributes associated with aViewport
    object. The PlyStackPlotOptions object has no constructor command. Abaqus creates the
    *detailPlotOptions.plyStackPlotPlotOptions* member whenever a Viewport is created.

    .. note::
        This object can be accessed by::

            session.viewports[name].detailPlotOptions.plyStackPlotOptions
    """

    #: A SymbolicConstant specifying how the plies in the viewport are rendered. Possible
    #: values are WIRE_FRAME, FILLED, and SHADED. The default value is SHADED.
    renderStyle: SymbolicConstant = SHADED

    #: A Boolean specifying whether to draw the edges for the plies. The default value is OFF.
    showEdges: Boolean = OFF

    #: A SymbolicConstant specifying the edge line style. Possible values are SOLID, DASHED,
    #: DOTTED, and DOT_DASH. The default value is SOLID.
    edgeStyle: SymbolicConstant = SOLID

    #: A SymbolicConstant specifying the edge line thickness. Possible values are VERY_THIN,
    #: THIN, MEDIUM, and THICK. The default value is VERY_THIN.
    edgeThickness: SymbolicConstant = VERY_THIN

    #: A SymbolicConstant specifying whether to display the plies in an unsymmetric staircase
    #: fashion or symmetric staircase fashion. Possible values are UNSYMMETRIC and SYMMETRIC.
    #: The default value is UNSYMMETRIC.
    plyDisplay: SymbolicConstant = UNSYMMETRIC

    #: An Int specifying the start ply. The default value is 1.
    startLayer: int = 1

    #: An Int specifying the number of plies to show. The default value is 30.
    numLayers: int = 30

    #: A String specifying the ply color for the even numbered plies. The numbering is based on
    #: the displayed plies and not on the actual ply number in the layup. The default value is
    #: "#A2B3FF".
    evenNumPlyColor: str = ""

    #: A String specifying the ply color for the odd numbered plies. The numbering is based on
    #: the displayed plies and not on the actual ply number in the layup. The default value is
    #: "#ECC9AD".
    oddNumPlyColor: str = ""

    #: A Boolean specifying whether to show the fibers. The default value is ON.
    showFibers: Boolean = ON

    #: A String specifying the fiber color. The default value is "Red".
    fiberColor: str = ""

    #: A SymbolicConstant specifying the fiber style. Possible values are SOLID, DASHED,
    #: DOTTED, and DOT_DASH. The default value is SOLID.
    fiberStyle: SymbolicConstant = SOLID

    #: A SymbolicConstant specifying the fiber thickness. Possible values are VERY_THIN, THIN,
    #: MEDIUM, and THICK. The default value is VERY_THIN.
    fiberThickness: SymbolicConstant = VERY_THIN

    #: A Float specifying the spacing between the fibers. The default value is 0.1.
    fiberSpacing: float = 0.1

    #: A Boolean specifying whether to show the reference surface. The default value is OFF.
    showReferencePlane: Boolean = OFF

    #: A String specifying the reference surface color. The default value is "White".
    referenceSurfaceColor: str = ""

    #: A Boolean specifying whether to set translucency. The default value is OFF.
    translucency: Boolean = OFF

    #: A Float specifying the translucency factor when **translucency** = ON. Possible values are
    #: 0.0≤ **translucencyFactor** ≤ 1.0. The default value is 0.3.
    translucencyFactor: float = 0.3

    #: A Boolean specifying whether to use depth sorting. The default value is OFF.
    translucencySort: Boolean = OFF

    #: A Boolean specifying whether to show the reference outline. The default value is OFF.
    showReferenceOutline: Boolean = OFF

    #: A String specifying the reference outline color. The default value is "Red".
    referenceOutlineColor: str = ""

    #: A SymbolicConstant specifying the reference outline style. Possible values are SOLID,
    #: DASHED, DOTTED, and DOT_DASH. The default value is SOLID.
    referenceOutlineStyle: SymbolicConstant = SOLID

    #: A SymbolicConstant specifying the reference outline thickness. Possible values are
    #: VERY_THIN, THIN, MEDIUM, and THICK. The default value is VERY_THIN.
    referenceOutlineThickness: SymbolicConstant = VERY_THIN

    #: A String specifying the font for all the labels. The default value is
    #: “-*-verdana-medium-r-normal-*-*-80-*-*-p-*-*-*” on Windows and
    #: “-*-verdana-medium-r-normal-*-*-90-*-*-p-*-*-*” on Linux platforms. The default value is
    #: an empty string.
    allLabelsFont: str = ""

    #: A Boolean specifying whether to show the material names. The default value is OFF.
    showMaterialNames: Boolean = OFF

    #: A String specifying the material names text color. The default value is "Green".
    materialNamesColor: str = ""

    #: A Boolean specifying whether to show the orientation names or the fiber angles. The
    #: default value is OFF.
    showOrientationNames: Boolean = OFF

    #: A String specifying the orientation names fiber angles text color. The default value is
    #: "Orange".
    orientationNamesColor: str = ""

    #: A Boolean specifying whether to show the state block. The default value is ON.
    showStateBlock: Boolean = ON

    #: A String specifying the state block text color. The default value is "White".
    stateBlockColor: str = ""

    #: A Boolean specifying whether to show the ply names. The default value is ON.
    showPlyNames: Boolean = ON

    #: A String specifying the ply names text color. The default value is "Yellow".
    plyNamesColor: str = ""

    #: A Boolean specifying whether to show the thickness labels. The default value is ON.
    showThicknessLabels: Boolean = ON

    #: A String specifying the thickness labels text color. The default value is "Red".
    thicknessLabelsColor: str = ""

    #: A Boolean specifying whether to show the through thickness integration points. The
    #: default value is OFF.
    showIntPoints: Boolean = OFF

    #: A String specifying the through thickness integration points color. The default value is
    #: "Blue".
    intPointsColor: str = ""

    #: A Float specifying the size of the ply in the X-direction. The default value is 1.5.
    sizeX: float = 1.5

    #: A Float specifying the size of the ply in the Y-direction. The default value is 1.0.
    sizeY: float = 1.0

    #: A Float specifying the size of the ply in the Z-direction. The default value is 0.8.
    sizeZ: float = 0.8

    @abaqus_method_doc
    def setValues(
        self,
        *,
        renderStyle: Literal[C.WIRE_FRAME, C.FILLED, C.SHADED] = SHADED,
        showEdges: Boolean = OFF,
        edgeStyle: Literal[C.DASHED, C.SOLID, C.DOT_DASH, C.DOTTED] = SOLID,
        edgeThickness: Literal[C.THIN, C.THICK, C.VERY_THIN, C.MEDIUM] = VERY_THIN,
        plyDisplay: Literal[C.SYMMETRIC, C.UNSYMMETRIC] = UNSYMMETRIC,
        startLayer: int = 1,
        numLayers: int = 30,
        evenNumPlyColor: str = "",
        oddNumPlyColor: str = "",
        showFibers: Boolean = ON,
        fiberColor: str = "",
        fiberStyle: Literal[C.DASHED, C.SOLID, C.DOT_DASH, C.DOTTED] = SOLID,
        fiberThickness: Literal[C.THIN, C.THICK, C.VERY_THIN, C.MEDIUM] = VERY_THIN,
        fiberSpacing: float = 0.1,
        showReferencePlane: Boolean = OFF,
        referenceSurfaceColor: str = "",
        translucency: Boolean = OFF,
        translucencyFactor: float = 0.3,
        translucencySort: Boolean = OFF,
        showReferenceOutline: Boolean = OFF,
        referenceOutlineColor: str = "",
        referenceOutlineStyle: Literal[C.DASHED, C.SOLID, C.DOT_DASH, C.DOTTED] = SOLID,
        referenceOutlineThickness: Literal[C.THIN, C.THICK, C.VERY_THIN, C.MEDIUM] = VERY_THIN,
        allLabelsFont: str = "",
        showMaterialNames: Boolean = OFF,
        materialNamesColor: str = "",
        showOrientationNames: Boolean = OFF,
        orientationNamesColor: str = "",
        showStateBlock: Boolean = ON,
        stateBlockColor: str = "",
        showPlyNames: Boolean = ON,
        plyNamesColor: str = "",
        showThicknessLabels: Boolean = ON,
        thicknessLabelsColor: str = "",
        showIntPoints: Boolean = OFF,
        intPointsColor: str = "",
        sizeX: float = 1.5,
        sizeY: float = 1.0,
        sizeZ: float = 0.8,
    ):
        """This method modifies the PlyStackPlotOptions object.

        Parameters
        ----------
        renderStyle
            A SymbolicConstant specifying how the plies in the viewport are rendered. Possible
            values are WIRE_FRAME, FILLED, and SHADED. The default value is SHADED.
        showEdges
            A Boolean specifying whether to draw the edges for the plies. The default value is OFF.
        edgeStyle
            A SymbolicConstant specifying the edge line style. Possible values are SOLID, DASHED,
            DOTTED, and DOT_DASH. The default value is SOLID.
        edgeThickness
            A SymbolicConstant specifying the edge line thickness. Possible values are VERY_THIN,
            THIN, MEDIUM, and THICK. The default value is VERY_THIN.
        plyDisplay
            A SymbolicConstant specifying whether to display the plies in an unsymmetric staircase
            fashion or symmetric staircase fashion. Possible values are UNSYMMETRIC and SYMMETRIC.
            The default value is UNSYMMETRIC.
        startLayer
            An Int specifying the start ply. The default value is 1.
        numLayers
            An Int specifying the number of plies to show. The default value is 30.
        evenNumPlyColor
            A String specifying the ply color for the even numbered plies. The numbering is based on
            the displayed plies and not on the actual ply number in the layup. The default value is
            "#A2B3FF".
        oddNumPlyColor
            A String specifying the ply color for the odd numbered plies. The numbering is based on
            the displayed plies and not on the actual ply number in the layup. The default value is
            "#ECC9AD".
        showFibers
            A Boolean specifying whether to show the fibers. The default value is ON.
        fiberColor
            A String specifying the fiber color. The default value is "Red".
        fiberStyle
            A SymbolicConstant specifying the fiber style. Possible values are SOLID, DASHED,
            DOTTED, and DOT_DASH. The default value is SOLID.
        fiberThickness
            A SymbolicConstant specifying the fiber thickness. Possible values are VERY_THIN, THIN,
            MEDIUM, and THICK. The default value is VERY_THIN.
        fiberSpacing
            A Float specifying the spacing between the fibers. The default value is 0.1.
        showReferencePlane
            A Boolean specifying whether to show the reference surface. The default value is OFF.
        referenceSurfaceColor
            A String specifying the reference surface color. The default value is "White".
        translucency
            A Boolean specifying whether to set translucency. The default value is OFF.
        translucencyFactor
            A Float specifying the translucency factor when **translucency** = ON. Possible values are
            0.0≤ **translucencyFactor** ≤ 1.0. The default value is 0.3.
        translucencySort
            A Boolean specifying whether to use depth sorting. The default value is OFF.
        showReferenceOutline
            A Boolean specifying whether to show the reference outline. The default value is OFF.
        referenceOutlineColor
            A String specifying the reference outline color. The default value is "Red".
        referenceOutlineStyle
            A SymbolicConstant specifying the reference outline style. Possible values are SOLID,
            DASHED, DOTTED, and DOT_DASH. The default value is SOLID.
        referenceOutlineThickness
            A SymbolicConstant specifying the reference outline thickness. Possible values are
            VERY_THIN, THIN, MEDIUM, and THICK. The default value is VERY_THIN.
        allLabelsFont
            A String specifying the font for all the labels. The default value is
            “-*-verdana-medium-r-normal-*-*-80-*-*-p-*-*-*” on Windows and
            “-*-verdana-medium-r-normal-*-*-90-*-*-p-*-*-*” on Linux platforms. The default value is
            an empty string.
        showMaterialNames
            A Boolean specifying whether to show the material names. The default value is OFF.
        materialNamesColor
            A String specifying the material names text color. The default value is "Green".
        showOrientationNames
            A Boolean specifying whether to show the orientation names or the fiber angles. The
            default value is OFF.
        orientationNamesColor
            A String specifying the orientation names fiber angles text color. The default value is
            "Orange".
        showStateBlock
            A Boolean specifying whether to show the state block. The default value is ON.
        stateBlockColor
            A String specifying the state block text color. The default value is "White".
        showPlyNames
            A Boolean specifying whether to show the ply names. The default value is ON.
        plyNamesColor
            A String specifying the ply names text color. The default value is "Yellow".
        showThicknessLabels
            A Boolean specifying whether to show the thickness labels. The default value is ON.
        thicknessLabelsColor
            A String specifying the thickness labels text color. The default value is "Red".
        showIntPoints
            A Boolean specifying whether to show the through thickness integration points. The
            default value is OFF.
        intPointsColor
            A String specifying the through thickness integration points color. The default value is
            "Blue".
        sizeX
            A Float specifying the size of the ply in the X-direction. The default value is 1.5.
        sizeY
            A Float specifying the size of the ply in the Y-direction. The default value is 1.0.
        sizeZ
            A Float specifying the size of the ply in the Z-direction. The default value is 0.8.
        """
        super().setValues(
            allLabelsFont=allLabelsFont,
            edgeStyle=edgeStyle,
            edgeThickness=edgeThickness,
            evenNumPlyColor=evenNumPlyColor,
            fiberColor=fiberColor,
            fiberSpacing=fiberSpacing,
            fiberStyle=fiberStyle,
            fiberThickness=fiberThickness,
            intPointsColor=intPointsColor,
            materialNamesColor=materialNamesColor,
            numLayers=numLayers,
            oddNumPlyColor=oddNumPlyColor,
            orientationNamesColor=orientationNamesColor,
            plyDisplay=plyDisplay,
            plyNamesColor=plyNamesColor,
            referenceOutlineColor=referenceOutlineColor,
            referenceOutlineStyle=referenceOutlineStyle,
            referenceOutlineThickness=referenceOutlineThickness,
            referenceSurfaceColor=referenceSurfaceColor,
            renderStyle=renderStyle,
            showEdges=showEdges,
            showFibers=showFibers,
            showIntPoints=showIntPoints,
            showMaterialNames=showMaterialNames,
            showOrientationNames=showOrientationNames,
            showPlyNames=showPlyNames,
            showReferenceOutline=showReferenceOutline,
            showReferencePlane=showReferencePlane,
            showStateBlock=showStateBlock,
            showThicknessLabels=showThicknessLabels,
            sizeX=sizeX,
            sizeY=sizeY,
            sizeZ=sizeZ,
            startLayer=startLayer,
            stateBlockColor=stateBlockColor,
            thicknessLabelsColor=thicknessLabelsColor,
            translucency=translucency,
            translucencyFactor=translucencyFactor,
            translucencySort=translucencySort,
        )
