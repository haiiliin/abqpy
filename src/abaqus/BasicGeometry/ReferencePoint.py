from typing import Union

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from ..BasicGeometry.InterestingPoint import InterestingPoint
from ..BasicGeometry.Vertex import Vertex
from ..Datum.Datum import Datum
from ..Mesh.MeshNode import MeshNode


@abaqus_class_doc
class ReferencePoint:
    """The ReferencePoint object has no direct constructor; it is created when a Feature object is created. The
    ReferencePoint method creates a Feature object that creates a ReferencePoint object.

    .. note::
        This object can be accessed by::

            import part
            mdb.models[name].parts[name].allInternalSets[name].referencePoints[i]
            mdb.models[name].parts[name].allSets[name].referencePoints[i]
            mdb.models[name].parts[name].referencePoints[i]
            mdb.models[name].parts[name].sets[name].referencePoints[i]
            import assembly
            mdb.models[name].rootAssembly.allInstances[name].referencePoints[i]
            mdb.models[name].rootAssembly.allInstances[name].sets[name].referencePoints[i]
            mdb.models[name].rootAssembly.allInternalSets[name].referencePoints[i]
            mdb.models[name].rootAssembly.allSets[name].referencePoints[i]
            mdb.models[name].rootAssembly.instances[name].referencePoints[i]
            mdb.models[name].rootAssembly.instances[name].sets[name].referencePoints[i]
            mdb.models[name].rootAssembly.modelInstances[i].referencePoints[i]
            mdb.models[name].rootAssembly.modelInstances[i].sets[name].referencePoints[i]
            mdb.models[name].rootAssembly.referencePoints[i]
            mdb.models[name].rootAssembly.sets[name].referencePoints[i]
    """

    @abaqus_method_doc
    def __init__(
        self,
        point: Union[tuple, Vertex, InterestingPoint, MeshNode, Datum],
        instanceName: str = "",
    ):
        """This method creates a Feature object and a ReferencePoint object at the specified location.

        .. note::
            This function can be accessed by::

                mdb.models[name].rootAssembly.ReferencePoint
                mdb.models[name].parts[name].ReferencePoint

        Parameters
        ----------
        point
            A ConstrainedSketchVertex, InterestingPoint, a MeshNode, or a Datum object specifying a reference point.
            **point** can also be a sequence of three Floats representing the **X**, **Y**, and
            **Z** coordinates of the point.
        instanceName
            Used internally by the input file writer.

        Returns
        -------
        Feature
            A Feature object.
        """
