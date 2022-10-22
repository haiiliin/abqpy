from typing import Optional

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from ..Datum.DatumCsys import DatumCsys
from ..Region.Set import Set
from ..UtilityAndView.abaqusConstants import AXIS_1, Boolean, ON, SymbolicConstant


@abaqus_class_doc
class ConnectorOrientation:
    """The ConnectorOrientation object is used to assign a connector orientation to a
    connector.

    .. note:: 
        This object can be accessed by::

            import assembly
            mdb.models[name].rootAssembly.connectorOrientations[i]
            import odbAccess
            session.odbs[name].rootAssembly.connectorOrientations[i]
    """

    region: Set
    localCsys1: DatumCsys = DatumCsys()
    axis1: SymbolicConstant = (AXIS_1,)
    angle1: float = 0
    orient2sameAs1: Boolean = ON
    localCsys2: DatumCsys = DatumCsys()
    axis2: SymbolicConstant = AXIS_1
    angle2: float = 0

    #: A :py:class:`~abaqus.Region.Set.Set` object specifying the region to which the orientation is assigned.
    region: Set

    #: A :py:class:`~abaqus.Datum.DatumCsys.DatumCsys` object specifying the local coordinate system of the first connector point.
    #: This value may be None, indicating the global coordinate system.
    localCsys1: Optional[DatumCsys] = None

    #: A SymbolicConstant specifying the axis of a datum coordinate system about which an
    #: additional rotation is applied. Possible values are AXIS_1, AXIS_2, and AXIS_3. The
    #: default value is AXIS_1.
    axis1: SymbolicConstant = AXIS_1

    #: A Float specifying the angle of the additional rotation. The default value is 0.0.
    angle1: float = 0

    #: A Boolean specifying whether or not the second connector point is to use the same local
    #: coordinate system, axis, and angle as the first point. The default value is ON.
    orient2sameAs1: Boolean = ON

    #: A :py:class:`~abaqus.Datum.DatumCsys.DatumCsys` object specifying the local coordinate system of the second connector point.
    #: This value may be None, indicating the global coordinate system.
    localCsys2: Optional[DatumCsys] = None

    #: A SymbolicConstant specifying the axis of a datum coordinate system about which an
    #: additional rotation is applied. Possible values are AXIS_1, AXIS_2, and AXIS_3. The
    #: default value is AXIS_1.
    axis2: SymbolicConstant = AXIS_1

    #: A Float specifying the angle of the additional rotation. The default value is 0.0.
    angle2: float = 0

    @abaqus_method_doc
    def __init__(
        self,
        region: Set,
        localCsys1: Optional[DatumCsys] = None,
        axis1: SymbolicConstant = AXIS_1,
        angle1: float = 0,
        orient2sameAs1: Boolean = ON,
        localCsys2: Optional[DatumCsys] = None,
        axis2: SymbolicConstant = AXIS_1,
        angle2: float = 0,
    ):
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
        ...

    @abaqus_method_doc
    def setValues(self, *args, **kwargs):
        """This method modifies the ConnectorOrientation object."""
        ...
