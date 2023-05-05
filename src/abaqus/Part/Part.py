from abqpy.decorators import abaqus_class_doc

from ..BasicGeometry.BasicGeometryPart import BasicGeometryPart
from ..Canvas.Displayable import Displayable
from ..EditMesh.MeshEditPart import MeshEditPart
from ..Mesh.MeshPart import MeshPart
from ..Property.PropertyPart import PropertyPart
from ..Region.Region import Region
from ..Region.RegionPart import RegionPart


@abaqus_class_doc
class Part(BasicGeometryPart, MeshEditPart, MeshPart, PropertyPart, RegionPart, Displayable):
    """The Part object defines the physical attributes of a structure. Parts are instanced into the assembly and
    positioned before an analysis.

    .. note::
        This object can be accessed by::

            import part
            mdb.models[name].parts[name]
    """

    ...

    def insertElements(self, faces: Region):
        """Insert elements on the Part."""
        ...
