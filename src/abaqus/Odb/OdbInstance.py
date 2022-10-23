from typing import Sequence

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from .OdbInstanceBase import OdbInstanceBase
from .OdbMeshNode import OdbMeshNode
from .OdbSet import OdbSet


@abaqus_class_doc
class OdbInstance(OdbInstanceBase):
    @abaqus_method_doc
    def NodeSet(self, name: str, nodes: Sequence[OdbMeshNode]) -> OdbSet:
        """This method creates a node set from an array of OdbMeshNode objects (for part
        instance-level sets) or from a sequence of arrays of OdbMeshNode objects (for
        assembly-level sets).

        .. note::
            This function can be accessed by::

                session.odbs[name].parts[name].NodeSet
                session.odbs[name].rootAssembly.instances[name].NodeSet
                session.odbs[name].rootAssembly.NodeSet

        Parameters
        ----------
        name
            A String specifying the name of the set and the repository key.
        nodes
            A sequence of OdbMeshNode objects. For example, for a part:`nodes=part1.nodes[1:5]`For
            an assembly:`nodes=(instance1.nodes[6:7], instance2.nodes[1:5])`

        Returns
        -------
        OdbSet
            An :py:class:`~abaqus.Odb.OdbSet.OdbSet` object.
        """
        self.nodeSets[name] = odbSet = OdbSet(name, nodes)
        return odbSet
