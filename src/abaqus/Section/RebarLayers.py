from abaqusConstants import *
from .LayerPropertiesArray import LayerPropertiesArray


class RebarLayers:
    """The RebarLayers object defines the rebar properties of a section.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import section
        mdb.models[name].parts[name].compositeLayups[i].section.rebarLayers
        mdb.models[name].sections[name].rebarLayers
        import odbSection
        session.odbs[name].sections[name].rebarLayers

    The corresponding analysis keywords are:

    - REBAR LAYER
    """

    def __init__(
        self, rebarSpacing: SymbolicConstant, layerTable: LayerPropertiesArray
    ):
        """This method creates a RebarLayers object.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            mdb.models[name].parts[name].compositeLayups[i].section.RebarLayers
            mdb.models[name].sections[name].RebarLayers
            session.odbs[name].sections[name].RebarLayers

        Parameters
        ----------
        rebarSpacing
            A SymbolicConstant specifying the type of rebar geometry. Possible values are CONSTANT,
            ANGULAR, and LIFT_EQUATION.
        layerTable
            A LayerPropertiesArray object specifying the layers of reinforcement.

        Returns
        -------
            A RebarLayers object.
        """
        pass

    def setValues(self):
        """This method modifies the RebarLayers object."""
        pass
