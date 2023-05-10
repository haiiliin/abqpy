from typing import Dict

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from ..BasicGeometry.EdgeArray import EdgeArray
from ..BasicGeometry.ReferencePoint import ReferencePoint
from ..BasicGeometry.VertexArray import VertexArray
from ..Datum.Datum import Datum
from ..Mesh.MeshElementArray import MeshElementArray
from ..Mesh.MeshNodeArray import MeshNodeArray
from ..Region.Set import Set
from ..Region.Surface import Surface
from ..UtilityAndView.abaqusConstants import OFF, Boolean


# prevent circular imports
class Model:
    ...


@abaqus_class_doc
class ModelInstance:
    """A ModelInstance object is an instance of a Model.

    .. note::
        This object can be accessed by::

            import assembly
            mdb.models[name].rootAssembly.modelInstances[i]
    """

    #: A repository of Set objects specifying the sets created on the assembly. For more
    #: information, see [Region
    #: commands](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-m-RegPyc-sb.htm?ContextScope=all).
    sets: Dict[str, Set] = {}

    #: A repository of Surface objects specifying the surfaces created on the assembly. For
    #: more information, see [Region
    #: commands](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-m-RegPyc-sb.htm?ContextScope=all).
    surfaces: Dict[str, Surface] = {}

    #: A VertexArray object.
    vertices: VertexArray = VertexArray([])

    #: An EdgeArray object.
    edges: EdgeArray = EdgeArray([])

    #: A MeshElementArray object.
    elements: MeshElementArray = MeshElementArray([])

    #: A MeshNodeArray object.
    nodes: MeshNodeArray = MeshNodeArray([])

    #: A repository of Datum objects.
    datums: Dict[str, Datum] = {}

    #: A repository of ReferencePoint objects.
    referencePoints: Dict[str, ReferencePoint] = {}

    @abaqus_method_doc
    def __init__(self, name: str, model: Model, autoOffset: Boolean = OFF):
        """This method creates a ModelInstance object and puts it into the instances repository.

        .. note::
            This function can be accessed by::

                mdb.models[name].rootAssembly.Instance

        Parameters
        ----------
        name
            The repository key. The name must be a valid Abaqus object name.
        model
            A Model object to be instanced. If the model does not exist, no ModelInstance object is
            created.
        autoOffset
            A Boolean specifying whether to apply an auto offset to the new instance that will
            offset it from existing instances. The default value is OFF.

        Returns
        -------
        ModelInstance
            A ModelInstance object.
        """
        ...

    @abaqus_method_doc
    def ConvertConstraints(self):
        """This method converts the position constraints of an instance to absolute positions.

        The method deletes the constraint features on the instance but preserves the position in space.
        """
        ...

    @abaqus_method_doc
    def getPosition(self):
        """This method prints the sum of the translations and rotations applied to the ModelInstance object."""
        ...

    @abaqus_method_doc
    def replace(self, instanceOf: Model, applyConstraints: Boolean = True):
        """This method replaces one instance with an instance of another model.

        .. versionadded:: 2019
            The ``replace`` method was added.

        Parameters
        ----------
        instanceOf
            A Model object to be instanced. If the model does not exist, no ModelInstance object is
            created.
        applyConstraints
            A Boolean specifying whether to apply existing constraints on the new instance or to
            position the new instance in the same place as the original instance. The default value
            is True. A value of False indicates that constraints applies to the instance are deleted
            will be deleted from the feature list.
        """
        ...

    @abaqus_method_doc
    def translate(self, vector: tuple):
        """This method translates an instance by the specified amount.

        Parameters
        ----------
        vector
            A sequence of three Floats specifying a translation vector.
        """
        ...
