from typing import Optional, Tuple

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

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

    @abaqus_method_doc
    def globalToLocal(self, coordinates: Tuple[float, float, float]) -> Tuple[float, float, float]:
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
    def localToGlobal(self, coordinates: Tuple[float, float, float]) -> Tuple[float, float, float]:
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
