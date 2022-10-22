from typing import Optional, Tuple

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from .OdbMeshNode import OdbMeshNode
from ..UtilityAndView.abaqusConstants import SymbolicConstant


@abaqus_class_doc
class OdbDatumCsys:
    """The OdbDatumCsys object contains a coordinate system that can be stored in an output
    database. You can create the datum coordinate system in the Visualization module during
    an Abaqus/CAE session and save the datum coordinate system to the output database before
    you exit Abaqus/CAE. Alternatively, the analysis code can write the datum coordinate
    system to the output database.

    .. note:: 
        This object can be accessed by::

            import odbAccess
            session.odbs[name].rootAssembly.datumCsyses[name]
    """

    #: A String specifying the repository key.
    name: str = ""

    #: A SymbolicConstant specifying the type of coordinate system. Possible values are
    #: CARTESIAN, CYLINDRICAL, and SPHERICAL.
    coordSysType: Optional[SymbolicConstant] = None

    #: A tuple of Floats specifying the coordinates of the origin of the datum coordinate
    #: system.
    origin: Optional[float] = None

    #: A tuple of Floats specifying a point on the **X**-axis.
    xAxis: Optional[float] = None

    #: A tuple of Floats specifying a point on the **Y**-axis.
    yAxis: Optional[float] = None

    #: A tuple of Floats specifying a point on the **Z**-axis.
    zAxis: Optional[float] = None

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
        ...

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

                session.odbs[name].rootAssembly.DatumCsysByThreePoints

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
        ...

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

                session.odbs[name].rootAssembly.DatumCsysByThreePoints

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
        ...

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

                session.odbs[name].rootAssembly.DatumCsysByThreePoints

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
        ...

    @abaqus_method_doc
    def DatumCsys(self, name: str, datumCsys: "OdbDatumCsys"):
        """This method copies oneOdbDatumCsys object to a new OdbDatumCsys object.

        .. note:: 
            This function can be accessed by::

                session.odbs[name].rootAssembly.DatumCsysByThreePoints

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
        ...

    @abaqus_method_doc
    def globalToLocal(
        self, coordinates: Tuple[float, float, float]
    ) -> Tuple[float, float, float]:
        """This method transforms specified coordinates in the global coordinate system into this
        local coordinate system.

        .. versionadded:: 2022
            The `globalToLocal` method was added.

        Parameters
        ----------
        coordinates
            A tuple of three Floats representing the coordinates in the global coordinate system.

        Returns
        -------
        Tuple[float, float, float]
            A tuple of three Floats representing the coordinates in this local coordinate system.
        """
        ...

    @abaqus_method_doc
    def localToGlobal(
        self, coordinates: Tuple[float, float, float]
    ) -> Tuple[float, float, float]:
        """This method transforms specified coordinates in this local coordinate system into the global coordinate system.

        .. versionadded:: 2022
            The `localToGlobal` method was added.

        Parameters
        ----------
        coordinates
            A tuple of three Floats representing the coordinates in the local coordinate system.

        Returns
        -------
        Tuple[float, float, float]
            A tuple of three Floats representing the coordinates in this global coordinate system.
        """
        ...
