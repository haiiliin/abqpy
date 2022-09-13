from ..EditMesh.MeshEditPart import MeshEditPart
from ..Mesh.MeshPart import MeshPart
from ..Property.PropertyPart import PropertyPart
from ..Region.RegionPart import RegionPart
from abqpy.decorators import abaqus_class_doc


@abaqus_class_doc
class Part(MeshEditPart, MeshPart, PropertyPart, RegionPart):
    """The Part object defines the physical attributes of a structure. Parts are instanced into
    the assembly and positioned before an analysis.

    .. note:: 
        This object can be accessed by:

        .. code-block:: python

            import part
            mdb.models[name].parts[name]
    """
    ...
