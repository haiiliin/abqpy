from typing import Optional

from abqpy.decorators import abaqus_class_doc

from ..UtilityAndView.abaqusConstants import SymbolicConstant


@abaqus_class_doc
class OdbDataDatumCsys:
    """The OdbDataDatumCsys object stores coordinate system data.

    .. note:: 
        This object can be accessed by::

            import visualization
            session.odbData[name].datumCsyses[i]
    """

    #: A String specifying the coordinate system name. This String is read-only.
    name: str = ""

    #: A SymbolicConstant specifying the coordinate system type. This String is read-only.
    #: Possible values are CARTESIAN, CYLINDRICAL, and SPHERICAL.
    type: Optional[SymbolicConstant] = None

    #: A tuple of three Floats specifying a sequence of three floats specifying the x-Axis
    #: vector. The default value is (1, 0, 0).
    xAxis: tuple = ()

    #: A tuple of three Floats specifying a sequence of three floats specifying the y-Axis
    #: vector. The default value is (0, 1, 0).
    yAxis: tuple = ()

    #: A tuple of three Floats specifying a sequence of three floats specifying the z-Axis
    #: vector. The default value is (0, 0, 1).
    zAxis: tuple = ()

    #: A tuple of three Floats specifying a sequence of three floats specifying the origin. The
    #: default value is (0, 0, 0).
    origin: tuple = ()
