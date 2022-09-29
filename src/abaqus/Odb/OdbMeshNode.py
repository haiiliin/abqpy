from typing import Optional

from abqpy.decorators import abaqus_class_doc


@abaqus_class_doc
class OdbMeshNode:
    """OdbMeshNode objects are created with the part.addNodes method.

    .. note:: 
        This object can be accessed by::

            import odbAccess
            session.odbs[name].parts[name].nodes[i]
            session.odbs[name].parts[name].nodeSets[name].nodes[i]
            session.odbs[name].parts[name].surfaces[name].nodes[i]
            session.odbs[name].rootAssembly.instances[name].nodes[i]
            session.odbs[name].rootAssembly.instances[name].nodeSets[name].nodes[i]
            session.odbs[name].rootAssembly.instances[name].surfaces[name].nodes[i]
            session.odbs[name].rootAssembly.nodes[i]
            session.odbs[name].rootAssembly.nodeSets[name].nodes[i]
            session.odbs[name].rootAssembly.surfaces[name].nodes[i]
            session.odbs[name].steps[name].frames[i].fieldOutputs[name].values[i].instance.nodes[i]
            session.odbs[name].steps[name].frames[i].fieldOutputs[name].values[i].instance.nodeSets[name].nodes[i]
            session.odbs[name].steps[name].frames[i].fieldOutputs[name].values[i].instance.surfaces[name].nodes[i]
    """

    #: An Int specifying the node label.
    label: Optional[int] = None

    #: A tuple of Floats specifying the nodal coordinates in the global Cartesian coordinate
    #: system.
    coordinates: Optional[float] = None
