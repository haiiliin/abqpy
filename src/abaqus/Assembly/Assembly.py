import typing
from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from .ConnectorOrientation import ConnectorOrientation
from ..Canvas.Displayable import Displayable
from ..Datum.DatumCsys import DatumCsys
from ..EditMesh.MeshEditAssembly import MeshEditAssembly
from ..Mesh.MeshAssembly import MeshAssembly
from ..Property.PropertyAssembly import PropertyAssembly
from ..Region.RegionAssembly import RegionAssembly
from ..Region.Set import Set
from ..UtilityAndView.abaqusConstants import *


@abaqus_class_doc
class Assembly(MeshEditAssembly, MeshAssembly, PropertyAssembly, RegionAssembly, Displayable):
    """An :py:class:`~abaqus.Assembly.Assembly.Assembly` object is a container for instances of parts. The Assembly object has no
    constructor command. Abaqus creates the **rootAssembly** member when a Model object is
    created.

    .. note:: 
        This object can be accessed by::

            import assembly
            mdb.models[name].rootAssembly
    """

    @abaqus_method_doc
    def ConnectorOrientation(
        self,
        region: Set,
        localCsys1: typing.Optional[DatumCsys] = None,
        axis1: SymbolicConstant = AXIS_1,
        angle1: float = 0,
        orient2sameAs1: Boolean = ON,
        localCsys2: typing.Optional[DatumCsys] = None,
        axis2: SymbolicConstant = AXIS_1,
        angle2: float = 0,
    ) -> ConnectorOrientation:
        """This method creates a ConnectorOrientation object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].rootAssembly.ConnectorOrientation
                session.odbs[name].rootAssembly.ConnectorOrientation

        Parameters
        ----------
        region
            A :py:class:`~abaqus.Region.Set.Set` object specifying the region to which the orientation is assigned.
        localCsys1
            A :py:class:`~abaqus.Datum.DatumCsys.DatumCsys` object specifying the local coordinate system of the first connector point.
            This value may be None, indicating the global coordinate system.
        axis1
            A SymbolicConstant specifying the axis of a datum coordinate system about which an
            additional rotation is applied. Possible values are AXIS_1, AXIS_2, and AXIS_3. The
            default value is AXIS_1.
        angle1
            A Float specifying the angle of the additional rotation. The default value is 0.0.
        orient2sameAs1
            A Boolean specifying whether or not the second connector point is to use the same local
            coordinate system, axis, and angle as the first point. The default value is ON.
        localCsys2
            A :py:class:`~abaqus.Datum.DatumCsys.DatumCsys` object specifying the local coordinate system of the second connector point.
            This value may be None, indicating the global coordinate system.
        axis2
            A SymbolicConstant specifying the axis of a datum coordinate system about which an
            additional rotation is applied. Possible values are AXIS_1, AXIS_2, and AXIS_3. The
            default value is AXIS_1.
        angle2
            A Float specifying the angle of the additional rotation. The default value is 0.0.

        Returns
        -------
        ConnectorOrientation
            A :py:class:`~abaqus.Assembly.ConnectorOrientation.ConnectorOrientation` object.
        """
        connectorOrientation = ConnectorOrientation(
            region, localCsys1, axis1, angle1, orient2sameAs1, localCsys2, axis2, angle2
        )
        self.connectorOrientations.append(connectorOrientation)
        return connectorOrientation
