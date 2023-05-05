from typing import Optional

from abqpy.decorators import abaqus_class_doc

from .SectionCategory import SectionCategory


@abaqus_class_doc
class OdbMeshElement:
    """OdbMeshElement objects are created with the part.addElements or rootAssembly.addElements methods.

    .. note::
        This object can be accessed by::

            import odbAccess
            session.odbs[name].parts[name].elements[i]
            session.odbs[name].parts[name].elementSets[name].elements[i]
            session.odbs[name].parts[name].nodeSets[name].elements[i]
            session.odbs[name].parts[name].surfaces[name].elements[i]
            session.odbs[name].rootAssembly.elements[i]
            session.odbs[name].rootAssembly.elementSets[name].elements[i]
            session.odbs[name].rootAssembly.instances[name].elements[i]
            session.odbs[name].rootAssembly.instances[name].elementSets[name].elements[i]
            session.odbs[name].rootAssembly.instances[name].nodeSets[name].elements[i]
            session.odbs[name].rootAssembly.instances[name].surfaces[name].elements[i]
            session.odbs[name].rootAssembly.nodeSets[name].elements[i]
            session.odbs[name].rootAssembly.surfaces[name].elements[i]
            session.odbs[name].steps[name].frames[i].fieldOutputs[name].values[i].instance.elements[i]
            session.odbs[name].steps[name].frames[i].fieldOutputs[name].values[i].instance.elementSets[name].elements[i]
            session.odbs[name].steps[name].frames[i].fieldOutputs[name].values[i].instance.nodeSets[name].elements[i]
            session.odbs[name].steps[name].frames[i].fieldOutputs[name].values[i].instance.surfaces[name].elements[i]
    """

    #: An Int specifying the element label.
    label: Optional[int] = None

    #: A String specifying the element type.
    type: str = ""

    #: A SectionCategory object specifying the element section properties.
    sectionCategory: Optional[SectionCategory] = None

    #: A tuple of Ints specifying the element connectivity. For connector elements connected to
    #: ground, the other node is repeated in the connectivity data. The position of the ground
    #: node cannot be ascertained. This is a limitation. It is important to note the difference
    #: with MeshElement object of MDB where the connectivity is node indices instead of node
    #: labels.
    connectivity: Optional[int] = None

    #: A tuple of Strings specifying the instance names for nodes in the element connectivity.
    instanceNames: tuple = ()

    #: A String specifying the instance name.
    instanceName: str = ""
