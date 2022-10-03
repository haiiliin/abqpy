from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from ..UtilityAndView.abaqusConstants import Boolean, ON


@abaqus_class_doc
class SymbolDisplayOptions:
    """The SymbolDisplayOptions object stores settings that specify how the assembly is
    displayed in a particular viewport. The SymbolDisplayOptions object has no constructor.
    When you create a new viewport, the settings are copied from the current viewport.

    .. note::
        This object can be accessed by::

            session.viewports[name].assemblyDisplay.symbolOptions
            session.viewports[name].layers[name].assemblyDisplay.symbolOptions
    """

    @abaqus_method_doc
    def setValues(
        self,
        otherSymbolSize: int = 12,
        arrowSymbolSize: int = 12,
        faceSymbolDensity: int = 5,
        edgeSymbolDensity: int = 5,
        meshSymbolFraction: float = 1,
        showFields: Boolean = ON,
    ):
        """This method modifies the SymbolDisplayOptions object.

        Parameters
        ----------
        otherSymbolSize
            An Int specifying the size of the scalar attribute symbols. Possible values are 1 ≤
            **scalarSymbolSize** ≤ 30. The default value is 12.
        arrowSymbolSize
            An Int specifying the size of the vector and tensor attribute symbols. Possible values
            are 1 ≤ **vectorSymbolSize** ≤ 30. The default value is 12.
        faceSymbolDensity
            An Int specifying the relative density of the attribute symbols drawn on geometric
            faces. Possible values are 1 ≤ **faceSymbolDensity** ≤ 10. The default value is 5.
        edgeSymbolDensity
            An Int specifying the relative density of the attribute symbols drawn on geometric
            edges. Possible values are 1 ≤ **edgeSymbolDensity** ≤ 10. The default value is 5.
        meshSymbolFraction
            A Float specifying the fraction of the attribute symbols drawn on orphan mesh regions.
            Possible values are 0.0 ≤ **meshSymbolFraction** ≤ 1.0. The default value is 1.0.
        showFields
            A Boolean specifying whether symbols should be scaled based on analytical field value.
            The default value is ON.
        """
        ...
