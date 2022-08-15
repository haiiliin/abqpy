from ..UtilityAndView.abaqusConstants import *
from .GeometricRestriction import GeometricRestriction
from ..Region.Region import Region


class BeadRotationalSymmetry(GeometricRestriction):
    """The BeadRotationalSymmetry object defines a bead rotational symmetry geometric
    restriction.
    The BeadRotationalSymmetry object is derived from the GeometricRestriction object.

    .. note:: 
        This object can be accessed by:

        .. code-block:: python

            import optimization
            mdb.models[name].optimizationTasks[name].geometricRestrictions[name]
    """

    #: A String specifying the geometric restriction repository key.
    name: str

    #: A Float specifying the repeating segment size, an angle in degrees.
    angle: float

    #: A :py:class:`~abaqus.Region.Region.Region` object specifying the region to which the geometric restriction is applied.
    region: Region

    #: A SymbolicConstant specifying the axis of symmetry. Possible values are AXIS_1, AXIS_2,
    #: and AXIS_3. The default value is AXIS_1.
    axis: SymbolicConstant = AXIS_1

    #: None or a DatumCsys object specifying the local coordinate system. If **csys** = None, the
    #: global coordinate system is used. When this member is queried, it returns an Int. The
    #: default value is None.
    csys: int = None

    def __init__(
        self,
        name: str,
        angle: float,
        region: Region,
        axis: SymbolicConstant = AXIS_1,
        csys: int = None,
    ):
        """This method creates a BeadRotationalSymmetry object.

        .. note:: 
            This function can be accessed by:

            .. code-block:: python

                mdb.models[name].optimizationTasks[name].BeadRotationalSymmetry

        Parameters
        ----------
        name
            A String specifying the geometric restriction repository key.
        angle
            A Float specifying the repeating segment size, an angle in degrees.
        region
            A :py:class:`~abaqus.Region.Region.Region` object specifying the region to which the geometric restriction is applied.
        axis
            A SymbolicConstant specifying the axis of symmetry. Possible values are AXIS_1, AXIS_2,
            and AXIS_3. The default value is AXIS_1.
        csys
            None or a DatumCsys object specifying the local coordinate system. If **csys** = None, the
            global coordinate system is used. When this member is queried, it returns an Int. The
            default value is None.

        Returns
        -------
        BeadRotationalSymmetry
            A :py:class:`~abaqus.Optimization.BeadRotationalSymmetry.BeadRotationalSymmetry` object.
        """
        super().__init__()

    def setValues(self, axis: SymbolicConstant = AXIS_1, csys: int = None):
        """This method modifies the BeadRotationalSymmetry object.

        Parameters
        ----------
        axis
            A SymbolicConstant specifying the axis of symmetry. Possible values are AXIS_1, AXIS_2,
            and AXIS_3. The default value is AXIS_1.
        csys
            None or a DatumCsys object specifying the local coordinate system. If **csys** = None, the
            global coordinate system is used. When this member is queried, it returns an Int. The
            default value is None.
        """
        ...
