from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from .LayerPropertiesArray import LayerPropertiesArray
from ..UtilityAndView.abaqusConstants import *


@abaqus_class_doc
class RebarLayers:
    """The RebarLayers object defines the rebar properties of a section.

    .. note:: 
        This object can be accessed by::

            import section
            mdb.models[name].parts[name].compositeLayups[i].section.rebarLayers
            mdb.models[name].sections[name].rebarLayers
            import odbSection
            session.odbs[name].sections[name].rebarLayers

        The corresponding analysis keywords are:

        - REBAR LAYER
    """

    #: A SymbolicConstant specifying the type of rebar geometry. Possible values are CONSTANT,
    #: ANGULAR, and LIFT_EQUATION.
    rebarSpacing: SymbolicConstant

    #: A :py:class:`~abaqus.Section.LayerPropertiesArray.LayerPropertiesArray` object specifying the layers of reinforcement.
    layerTable: LayerPropertiesArray

    @abaqus_method_doc
    def __init__(
        self, rebarSpacing: SymbolicConstant, layerTable: LayerPropertiesArray
    ):
        """This method creates a RebarLayers object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].parts[name].compositeLayups[i].section.RebarLayers
                mdb.models[name].sections[name].RebarLayers
                session.odbs[name].sections[name].RebarLayers

        Parameters
        ----------
        rebarSpacing
            A SymbolicConstant specifying the type of rebar geometry. Possible values are CONSTANT,
            ANGULAR, and LIFT_EQUATION.
        layerTable
            A :py:class:`~abaqus.Section.LayerPropertiesArray.LayerPropertiesArray` object specifying the layers of reinforcement.

        Returns
        -------
        RebarLayers
            A :py:class:`~abaqus.Section.RebarLayers.RebarLayers` object.
        """
        ...

    @abaqus_method_doc
    def setValues(self, *args, **kwargs):
        """This method modifies the RebarLayers object."""
        ...
