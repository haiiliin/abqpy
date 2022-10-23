from typing import Sequence

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from .OdbMeshNode import OdbMeshNode
from .OdbPartBase import OdbPartBase
from .OdbSet import OdbSet
from ..UtilityAndView.abaqusConstants import Boolean, INPUT, OFF


@abaqus_class_doc
class OdbPart(OdbPartBase):
    @abaqus_method_doc
    def RigidBody(
        self,
        referenceNode: str,
        position: str = INPUT,
        isothermal: Boolean = OFF,
        elset: str = "",
        pinNodes: str = "",
        tieNodes: str = "",
    ):
        """This method defines an OdbRigidBody on the part object.

        Parameters
        ----------
        referenceNode
            An OdbSet specifying the reference node assigned to the rigid body.
        position
            A symbolic constant specify if the location of the reference node is to be defined by
            the user. Possible values are INPUT and CENTER_OF_MASS. The default value is INPUT.
        isothermal
            A Boolean specifying an isothermal rigid body. The default value is OFF. This parameter
            is used only for a fully-coupled thermal stress analysis.
        elset
            An OdbSet specifying an element set assigned to the rigid body.
        pinNodes
            An OdbSet specifying pin-type nodes assigned to the rigid body.
        tieNodes
            An OdbSet specifying tie-type nodes assigned to the rigid body.

        Returns
        -------
        None.

        Raises
        ------
        OdbError: Rigid body definition requires a node set
            If **referenceNode** is not a node set.
        """
        ...

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
