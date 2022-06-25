from abaqusConstants import *
from .AnalyticSurface import AnalyticSurface
from .OdbInstanceBase import OdbInstanceBase
from .OdbMeshNode import OdbMeshNode
from .OdbRigidBody import OdbRigidBody
from .OdbSet import OdbSet


class OdbInstance(OdbInstanceBase):
    def OdbRigidBody(
        self,
        referenceNode: OdbSet,
        position: SymbolicConstant = INPUT,
        isothermal: Boolean = ON,
        elements: OdbSet = OdbSet("set", tuple[OdbMeshNode]()),
        tieNodes: OdbSet = OdbSet("set", tuple[OdbMeshNode]()),
        pinNodes: OdbSet = OdbSet("set", tuple[OdbMeshNode]()),
        analyticSurface: AnalyticSurface = None, 
    ) -> OdbRigidBody:
        """This method creates a OdbRigidBody object.

        .. note:: 
            This function can be accessed by:

            .. code-block:: python

                session.odbs[name].rootAssembly.instances[name].RigidBody
                session.odbs[name].rootAssembly.RigidBody

        Parameters
        ----------
        referenceNode
            An :py:class:`~abaqus.Odb.OdbSet.OdbSet` object specifying the reference node set associated with the rigid body.
        position
            A SymbolicConstant specifying the specific location of the OdbRigidBody reference node
            relative to the rest of the rigid body. Possible values are INPUT and CENTER_OF_MASS.
            The default value is INPUT.
        isothermal
            A Boolean specifying specify whether the OdbRigidBody can have temperature gradients or
            be isothermal. This is used only for fully coupled thermal-stress analysis The default
            value is ON.
        elements
            An :py:class:`~abaqus.Odb.OdbSet.OdbSet` object specifying the element set whose motion is governed by the motion of
            rigid body reference node.
        tieNodes
            An :py:class:`~abaqus.Odb.OdbSet.OdbSet` object specifying the node set which have both translational and rotational
            degrees of freedom associated with the rigid body.
        pinNodes
            An :py:class:`~abaqus.Odb.OdbSet.OdbSet` object specifying the node set which have only translational degrees of
            freedom associated with the rigid body.
        analyticSurface
            An :py:class:`~abaqus.Odb.AnalyticSurface.AnalyticSurface` object specifying the analytic surface whose motion is governed by
            the motion of rigid body reference node.

        Returns
        -------
        OdbRigidBody
            An :py:class:`~abaqus.Odb.OdbRigidBody.OdbRigidBody` object.
        """
        odbRigidBody = OdbRigidBody(
            referenceNode,
            position,
            isothermal,
            elements,
            tieNodes,
            pinNodes,
            analyticSurface,
        )
        self.rigidBodies.append(odbRigidBody)
        return odbRigidBody

    def NodeSet(self, name: str, nodes: tuple[OdbMeshNode]) -> OdbSet:
        """This method creates a node set from an array of OdbMeshNode objects (for part
        instance-level sets) or from a sequence of arrays of OdbMeshNode objects (for
        assembly-level sets).

        .. note:: 
            This function can be accessed by:

            .. code-block:: python

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
