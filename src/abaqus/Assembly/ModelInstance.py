from abaqusConstants import *
from ..BasicGeometry.EdgeArray import EdgeArray
from ..BasicGeometry.ReferencePoint import ReferencePoint
from ..BasicGeometry.VertexArray import VertexArray
from ..Datum.Datum import Datum
from ..Mesh.MeshElementArray import MeshElementArray
from ..Mesh.MeshNodeArray import MeshNodeArray

# from ..Model.Model import Model
from ..Region.Set import Set
from ..Region.Surface import Surface


# prevent circular imports
class Model:
    pass


class ModelInstance:
    """A :py:class:`~abaqus.Assembly.ModelInstance.ModelInstance` object is an instance of a Model.

    Attributes
    ----------
    sets: dict[str, Set]
        A repository of :py:class:`~abaqus.Region.Set.Set` objects specifying the sets created on the assembly. For more
        information, see [Region
        commands](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-m-RegPyc-sb.htm?ContextScope=all).
    surfaces: dict[str, Surface]
        A repository of :py:class:`~abaqus.Region.Surface.Surface` objects specifying the surfaces created on the assembly. For
        more information, see [Region
        commands](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-m-RegPyc-sb.htm?ContextScope=all).
    vertices: VertexArray
        A :py:class:`~abaqus.BasicGeometry.VertexArray.VertexArray` object.
    edges: EdgeArray
        An :py:class:`~abaqus.BasicGeometry.EdgeArray.EdgeArray` object.
    elements: MeshElementArray
        A :py:class:`~abaqus.Mesh.MeshElementArray.MeshElementArray` object.
    nodes: MeshNodeArray
        A :py:class:`~abaqus.Mesh.MeshNodeArray.MeshNodeArray` object.
    datums: dict[str, Datum]
        A repository of :py:class:`~abaqus.Datum.Datum.Datum` objects.
    referencePoints: dict[str, ReferencePoint]
        A repository of :py:class:`~abaqus.BasicGeometry.ReferencePoint.ReferencePoint` objects.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import assembly
        mdb.models[name].rootAssembly.modelInstances[i]
    """

    # A repository of Set objects specifying the sets created on the assembly. For more
    # information, see [Region
    # commands](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-m-RegPyc-sb.htm?ContextScope=all).
    sets: dict[str, Set] = dict[str, Set]()

    # A repository of Surface objects specifying the surfaces created on the assembly. For
    # more information, see [Region
    # commands](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-m-RegPyc-sb.htm?ContextScope=all).
    surfaces: dict[str, Surface] = dict[str, Surface]()

    # A :py:class:`~abaqus.BasicGeometry.VertexArray.VertexArray` object.
    vertices: VertexArray = VertexArray([])

    # An :py:class:`~abaqus.BasicGeometry.EdgeArray.EdgeArray` object.
    edges: EdgeArray = EdgeArray([])

    # A :py:class:`~abaqus.Mesh.MeshElementArray.MeshElementArray` object.
    elements: MeshElementArray = MeshElementArray([])

    # A :py:class:`~abaqus.Mesh.MeshNodeArray.MeshNodeArray` object.
    nodes: MeshNodeArray = MeshNodeArray([])

    # A repository of Datum objects.
    datums: dict[str, Datum] = dict[str, Datum]()

    # A repository of ReferencePoint objects.
    referencePoints: dict[str, ReferencePoint] = dict[str, ReferencePoint]()

    def __init__(self, name: str, model: Model, autoOffset: Boolean = OFF):
        """This method creates a ModelInstance object and puts it into the instances repository.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            mdb.models[name].rootAssembly.Instance

        Parameters
        ----------
        name
            The repository key. The name must be a valid Abaqus object name.
        model
            A :py:class:`~abaqus.Assembly.ModelInstance.Model` object to be instanced. If the model does not exist, no ModelInstance object is
            created.
        autoOffset
            A Boolean specifying whether to apply an auto offset to the new instance that will
            offset it from existing instances. The default value is OFF.

        Returns
        -------
        ModelInstance
            A :py:class:`~abaqus.Assembly.ModelInstance.ModelInstance` object.
        """
        pass

    def ConvertConstraints(self):
        """This method converts the position constraints of an instance to absolute positions. The
        method deletes the constraint features on the instance but preserves the position in
        space.
        """
        pass

    def getPosition(self):
        """This method prints the sum of the translations and rotations applied to the
        ModelInstance object.
        """
        pass

    def translate(self, vector: tuple):
        """This method translates an instance by the specified amount.

        Parameters
        ----------
        vector
            A sequence of three Floats specifying a translation vector.
        """
        pass
