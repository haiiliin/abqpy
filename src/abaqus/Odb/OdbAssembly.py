from typing import Optional, Sequence

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from .AnalyticSurface import AnalyticSurface
from .OdbAssemblyBase import OdbAssemblyBase
from .OdbDatumCsys import OdbDatumCsys
from .OdbInstance import OdbInstance
from .OdbMeshNode import OdbMeshNode
from .OdbPart import OdbPart
from .OdbRigidBody import OdbRigidBody
from .OdbSet import OdbSet
from ..UtilityAndView.abaqusConstants import Boolean, INPUT, ON, SymbolicConstant


@abaqus_class_doc
class OdbAssembly(OdbAssemblyBase):
    @abaqus_method_doc
    def DatumCsysByThreePoints(
        self,
        name: str,
        coordSysType: SymbolicConstant,
        origin: tuple,
        point1: tuple,
        point2: tuple,
    ):
        """This method creates an OdbDatumCsys object using three points. A datum coordinate system
        created with this method results in a fixed system.

        .. note:: 
            This function can be accessed by::

                session.odbs[name].rootAssembly.DatumCsysByThreePoints

        Parameters
        ----------
        name
            A String specifying the repository key.
        coordSysType
            A SymbolicConstant specifying the type of coordinate system. Possible values are
            CARTESIAN, CYLINDRICAL, and SPHERICAL.
        origin
            A sequence of Floats specifying the coordinates of the origin of the datum coordinate
            system.
        point1
            A sequence of Floats specifying the coordinates of a point on the local 1- or rr-axis.
        point2
            A sequence of Floats specifying the coordinates of a point in the 1-2 or rr-θθ plane.

        Returns
        -------
        OdbDatumCsys
            An :py:class:`~abaqus.Odb.OdbDatumCsys.OdbDatumCsys` object.
        """
        self.datumCsyses[name] = datumCsys = OdbDatumCsys()
        return datumCsys

    @abaqus_method_doc
    def DatumCsysByThreeNodes(
        self,
        name: str,
        coordSysType: SymbolicConstant,
        origin: OdbMeshNode,
        point1: OdbMeshNode,
        point2: OdbMeshNode,
    ):
        """This method creates an OdbDatumCsys object using the coordinates of three OdbMeshNode
        objects. A datum coordinate system created with this method results in a system that
        follows the position of the three nodes. Results, such as those for displacement, are
        resolved into the orientation of the datum coordinate system without regard to the
        position of its origin. The last three arguments are given in the form of an OdbMeshNode
        object.

        .. note:: 
            This function can be accessed by::

                session.odbs[name].rootAssembly.DatumCsysByThreeNodes

        Parameters
        ----------
        name
            A String specifying the repository key.
        coordSysType
            A SymbolicConstant specifying the type of coordinate system. Possible values are
            CARTESIAN, CYLINDRICAL, and SPHERICAL.
        origin
            An :py:class:`~abaqus.Odb.OdbMeshNode.OdbMeshNode` object specifying a node at the origin of the datum coordinate system.
        point1
            An :py:class:`~abaqus.Odb.OdbMeshNode.OdbMeshNode` object specifying a node on the local 1- or rr-axis.
        point2
            An :py:class:`~abaqus.Odb.OdbMeshNode.OdbMeshNode` object specifying a node in the 1-2 or rr-θθ plane.

        Returns
        -------
        OdbDatumCsys
            An :py:class:`~abaqus.Odb.OdbDatumCsys.OdbDatumCsys` object.
        """
        self.datumCsyses[name] = datumCsys = OdbDatumCsys()
        return datumCsys

    @abaqus_method_doc
    def DatumCsysByThreeCircNodes(
        self,
        name: str,
        coordSysType: SymbolicConstant,
        node1Arc: OdbMeshNode,
        node2Arc: OdbMeshNode,
        node3Arc: OdbMeshNode,
    ):
        """This method is convenient to use where there are no nodes along the axis of a hollow
        cylinder or at the center of a hollow sphere. The three nodes that you provide as
        arguments determine a circle in space. The center of the circle is the origin of the
        datum coordinate system. The normal to the circle is parallel to the zz-axis of a
        cylindrical coordinate system or to the ϕϕ-axis of a spherical coordinate system. The
        line from the origin to the first node defines the rr-axis.

        .. note:: 
            This function can be accessed by::

                session.odbs[name].rootAssembly.DatumCsysByThreeCircNodes

        Parameters
        ----------
        name
            A String specifying the repository key.
        coordSysType
            A SymbolicConstant specifying the type of coordinate system. Possible values are
            CARTESIAN, CYLINDRICAL, and SPHERICAL.
        node1Arc
            An :py:class:`~abaqus.Odb.OdbMeshNode.OdbMeshNode` object that lies on the circular arc.
        node2Arc
            An :py:class:`~abaqus.Odb.OdbMeshNode.OdbMeshNode` object that lies on the circular arc.
        node3Arc
            An :py:class:`~abaqus.Odb.OdbMeshNode.OdbMeshNode` object that lies on the circular arc.

        Returns
        -------
        OdbDatumCsys
            An :py:class:`~abaqus.Odb.OdbDatumCsys.OdbDatumCsys` object.
        """
        self.datumCsyses[name] = datumCsys = OdbDatumCsys()
        return datumCsys

    @abaqus_method_doc
    def DatumCsysBy6dofNode(
        self, name: str, coordSysType: SymbolicConstant, origin: OdbMeshNode
    ):
        """A datum coordinate system created with this method results in a system that follows the
        position of a node. The node location defines the origin of the datum coordinate system.
        The rotational displacement (UR1, UR2, UR3) of the node defines the orientation of the
        coordinate system axes. Results, such as those for displacement, are resolved into the
        orientation of the datum coordinate system without regard to the position of its origin.
        The last argument is given in the form of an OdbMeshNode object.

        .. note:: 
            This function can be accessed by::

                session.odbs[name].rootAssembly.DatumCsysBy6dofNode

        Parameters
        ----------
        name
            A String specifying the repository key.
        coordSysType
            A SymbolicConstant specifying the type of coordinate system. Possible values are
            CARTESIAN, CYLINDRICAL, and SPHERICAL.
        origin
            An :py:class:`~abaqus.Odb.OdbMeshNode.OdbMeshNode` object specifying the origin of the datum coordinate system.

        Returns
        -------
        OdbDatumCsys
            An :py:class:`~abaqus.Odb.OdbDatumCsys.OdbDatumCsys` object.
        """
        self.datumCsyses[name] = datumCsys = OdbDatumCsys()
        return datumCsys

    @abaqus_method_doc
    def DatumCsys(self, name: str, datumCsys: OdbDatumCsys):
        """This method copies oneOdbDatumCsys object to a new OdbDatumCsys object.

        .. note:: 
            This function can be accessed by::

                session.odbs[name].rootAssembly.DatumCsys

        Parameters
        ----------
        name
            A String specifying the repository key.
        datumCsys
            An :py:class:`~abaqus.Odb.OdbDatumCsys.OdbDatumCsys` object specifying the object to be copied.

        Returns
        -------
        OdbDatumCsys
            An :py:class:`~abaqus.Odb.OdbDatumCsys.OdbDatumCsys` object.
        """
        self.datumCsyses[name] = datumCsys = OdbDatumCsys()
        return datumCsys

    @abaqus_method_doc
    def Instance(
        self, name: str, object: OdbPart, localCoordSystem: tuple = ()
    ) -> OdbInstance:
        """This method creates an OdbInstance object from an OdbPart object.

        .. note:: 
            This function can be accessed by::

                session.odbs[name].rootAssembly.Instance

        Parameters
        ----------
        name
            A String specifying the instance name.
        object
            An :py:class:`~abaqus.Odb.OdbPart.OdbPart` object.
        localCoordSystem
            A sequence of sequences of three Floats specifying the rotation and translation of the
            part instance in the global Cartesian coordinate system. The first three sequences
            specify the new local coordinate system with its center at the origin.The first sequence
            specifies a point on the 1-axis.The second sequence specifies a point on the 2-axis.The
            third sequence specifies a point on the 3-axis.The fourth sequence specifies the
            translation of the local coordinate system from the origin to its intended location.For
            example, the following sequence moves a part 10 units in the **X**-direction with no
            rotation:`localCoordSystem = ((1, 0, 0), (0, 1, 0), (0, 0, 1), (10, 0, 0))`The following
            sequence moves a part 5 units in the **X**-direction with rotation:
            `localCoordSystem = ((0, 1, 0), (1, 0, 0), (0, 0, 1), (5, 0, 0))`transforms a part
            containing the two points`Pt1= (1,0,0) Pt2= (2,0,0)` to `Pt1 = (0, 6, 0) Pt2 = (0, 7, 0)`

        Returns
        -------
        OdbInstance
            An :py:class:`~abaqus.Odb.OdbInstance.OdbInstance` object.
        """
        self.instances[name] = odbInstance = OdbInstance(name, object, localCoordSystem)
        return odbInstance

    @abaqus_method_doc
    def RigidBody(
        self,
        referenceNode: OdbSet,
        position: SymbolicConstant = INPUT,
        isothermal: Boolean = ON,
        elements: OdbSet = OdbSet("set", ()),
        tieNodes: OdbSet = OdbSet("set", ()),
        pinNodes: OdbSet = OdbSet("set", ()),
        analyticSurface: Optional[AnalyticSurface] = None, 
    ) -> OdbRigidBody:
        """This method creates a OdbRigidBody object.

        .. note:: 
            This function can be accessed by::

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
