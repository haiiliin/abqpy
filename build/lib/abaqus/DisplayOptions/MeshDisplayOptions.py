from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from ..UtilityAndView.abaqusConstants import Boolean, EXTERIOR, OFF, ON, SymbolicConstant


@abaqus_class_doc
class MeshDisplayOptions:
    """The MeshDisplayOptions object stores settings that specify how the assembly is displayed
    in a particular viewport when
    session.viewports[name].assemblyDisplay.mesh=ON
    The MeshDisplayOptions object has no constructor. When you create a new viewport, the
    settings are copied from the current viewport.

    .. note::
        This object can be accessed by::

            session.viewports[name].assemblyDisplay.meshOptions
            session.viewports[name].layers[name].assemblyDisplay.meshOptions
            session.viewports[name].layers[name].partDisplay.meshOptions
            session.viewports[name].partDisplay.meshOptions
    """

    @abaqus_method_doc
    def setValues(
        self,
        nodeLabels: Boolean = OFF,
        elementLabels: Boolean = OFF,
        meshVisibleEdges: SymbolicConstant = EXTERIOR,
        featureAngle: float = 20,
        meshEdgesInShaded: Boolean = ON,
        meshTechnique: Boolean = OFF,
        seeds: Boolean = OFF,
    ):
        """This method modifies the MeshDisplayOptions object.

        Parameters
        ----------
        nodeLabels
            A Boolean specifying whether node labels are shown. The default value is OFF.
        elementLabels
            A Boolean specifying whether element labels are shown. The default value is OFF.
        meshVisibleEdges
            A SymbolicConstant specifying how the mesh's edges are drawn. Possible values are:

            - ALL, specifying that all edges are shown.
            - EXTERIOR, specifying that only exterior edges are shown.
            - FEATURE, specifying that edges are shown based on **featureAngle**.
            - FREE, specifying that only free edges are shown.
            - NONE, specifying that no display edges are shown.
            
            The default value is EXTERIOR.
        featureAngle
            A Float specifying the angle in degrees to be used in calculating a feature edge plot.
            Possible values are 0 ≤ **featureAngle** ≤ 90. The default value is 20.0.
        meshEdgesInShaded
            A Boolean specifying whether mesh edges are displayed in shaded mode. The default value
            is ON.
        meshTechnique
            A Boolean specifying whether the regions of the assembly will be color coded based on
            the meshing technique assigned to the regions. This argument is ignored in partDisplay.
            The default value is OFF.
        seeds
            A Boolean specifying whether seeds are shown. This argument is ignored in partDisplay.
            The default value is OFF.

        Raises
        ------
        RangeError
        """
        ...
