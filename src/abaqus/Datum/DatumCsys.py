from typing import Optional

from abqpy.decorators import abaqus_class_doc

from .Datum import Datum
from .DatumAxis import DatumAxis
from .DatumPoint import DatumPoint
from ..UtilityAndView.abaqusConstants import SymbolicConstant


@abaqus_class_doc
class DatumCsys(Datum):
    """The DatumCsys object has no direct constructor; it is created when a Feature object is
    created. For example, the DatumCsysByOffset method creates a Feature object that creates
    a DatumCsys object.
    The DatumCsys object is derived from the Datum object.

    .. note:: 
        This object can be accessed by::

            import part
            mdb.models[name].parts[name].datums[i]
            import assembly
            mdb.models[name].rootAssembly.allInstances[name].datums[i]
            mdb.models[name].rootAssembly.connectorOrientations[i].localCsys1
            mdb.models[name].rootAssembly.connectorOrientations[i].localCsys2
            mdb.models[name].rootAssembly.datums[i]
            mdb.models[name].rootAssembly.instances[name].datums[i]
            import odbAccess
            session.odbs[name].rootAssembly.connectorOrientations[i].localCsys1
            session.odbs[name].rootAssembly.connectorOrientations[i].localCsys2
    """

    #: A SymbolicConstant specifying the type of the coordinate system. Possible values are
    #: CARTESIAN, CYLINDRICAL, and SPHERICAL.
    coordSysType: Optional[SymbolicConstant] = None

    #: A :py:class:`~abaqus.Datum.DatumPoint.DatumPoint` object specifying the origin of the coordinate system.
    origin: DatumPoint = DatumPoint()

    #: A :py:class:`~abaqus.Datum.DatumAxis.DatumAxis` object specifying the 1-direction of the coordinate system.
    axis1: DatumAxis = DatumAxis()

    #: A :py:class:`~abaqus.Datum.DatumAxis.DatumAxis` object specifying the 2-direction of the coordinate system.
    axis2: DatumAxis = DatumAxis()

    #: A :py:class:`~abaqus.Datum.DatumAxis.DatumAxis` object specifying the 3-direction of the coordinate system.
    axis3: DatumAxis = DatumAxis()
