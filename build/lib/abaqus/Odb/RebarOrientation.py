from typing import Optional

from abqpy.decorators import abaqus_class_doc
from .OdbDatumCsys import OdbDatumCsys
from .OdbSet import OdbSet
from ..UtilityAndView.abaqusConstants import SymbolicConstant


@abaqus_class_doc
class RebarOrientation:
    """The RebarOrientation object represents the orientation of the rebar reference.

    .. note:: 
        This object can be accessed by::

            import odbAccess
            session.odbs[name].parts[name].rebarOrientations[i]
            session.odbs[name].rootAssembly.instances[name].rebarOrientations[i]
            session.odbs[name].steps[name].frames[i].fieldOutputs[name].values[i].instance.rebarOrientations[i]
    """

    #: A SymbolicConstant specifying the axis of a cylindrical or spherical datum coordinate
    #: system about which an additional rotation is applied. Possible values are AXIS_1,
    #: AXIS_2, and AXIS_3.
    axis: Optional[SymbolicConstant] = None

    #: A Float specifying the angle of the additional rotation.
    angle: Optional[float] = None

    #: An :py:class:`~abaqus.Odb.OdbSet.OdbSet` object specifying a region for which the rebar orientation is defined.
    region: OdbSet = OdbSet("set", ())

    #: An :py:class:`~abaqus.Odb.OdbDatumCsys.OdbDatumCsys` object specifying a datum coordinates system.
    csys: OdbDatumCsys = OdbDatumCsys()
