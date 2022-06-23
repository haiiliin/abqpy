from abaqusConstants import *
from .OdbDatumCsys import OdbDatumCsys
from .OdbMeshNode import OdbMeshNode
from .OdbSet import OdbSet


class RebarOrientation:
    """The RebarOrientation object represents the orientation of the rebar reference.

    Attributes
    ----------
    axis: SymbolicConstant
        A SymbolicConstant specifying the axis of a cylindrical or spherical datum coordinate
        system about which an additional rotation is applied. Possible values are AXIS_1,
        AXIS_2, and AXIS_3.
    angle: float
        A Float specifying the angle of the additional rotation.
    region: OdbSet
        An :py:class:`~abaqus.Odb.OdbSet.OdbSet` object specifying a region for which the rebar orientation is defined.
    csys: OdbDatumCsys
        An :py:class:`~abaqus.Odb.OdbDatumCsys.OdbDatumCsys` object specifying a datum coordinates system.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import odbAccess
        session.odbs[name].parts[name].rebarOrientations[i]
        session.odbs[name].rootAssembly.instances[name].rebarOrientations[i]
        session.odbs[name].steps[name].frames[i].fieldOutputs[name].values[i].instance.rebarOrientations[i]
    """

    #: A SymbolicConstant specifying the axis of a cylindrical or spherical datum coordinate
    #: system about which an additional rotation is applied. Possible values are AXIS_1,
    #: AXIS_2, and AXIS_3.
    axis: SymbolicConstant = None

    #: A Float specifying the angle of the additional rotation.
    angle: float = None

    #: An :py:class:`~abaqus.Odb.OdbSet.OdbSet` object specifying a region for which the rebar orientation is defined.
    region: OdbSet = OdbSet("set", tuple[OdbMeshNode]())

    #: An :py:class:`~abaqus.Odb.OdbDatumCsys.OdbDatumCsys` object specifying a datum coordinates system.
    csys: OdbDatumCsys = OdbDatumCsys()
