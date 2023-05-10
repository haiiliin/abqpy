from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from ..Region.Region import Region
from ..UtilityAndView.abaqusConstants import OFF, Boolean
from .Constraint import Constraint


@abaqus_class_doc
class AdjustPoints(Constraint):
    """The AdjustPoints constraint object is used to adjust points (nodes) to a surface. The AdjustPoints object
    is derived from the ConstrainedSketchConstraint object.

    .. note::
        This object can be accessed by::

            import interaction
            mdb.models[name].constraints[name]

        The corresponding analysis keywords are:

        - ADJUST
    """

    #: A Boolean specifying whether the constraint is suppressed or not. The default value is
    #: OFF.
    suppressed: Boolean = OFF

    #: A String specifying the constraint repository key.
    name: str

    #: A Region object specifying the surface to which the **controlPoints** are adjusted.
    surface: Region

    #: A Region object specifying the constraint control points.
    controlPoints: Region

    @abaqus_method_doc
    def __init__(self, name: str, surface: Region, controlPoints: Region):
        """This method creates an AdjustPoints object.

        .. note::
            This function can be accessed by::

                mdb.models[name].AdjustPoints

        Parameters
        ----------
        name
            A String specifying the constraint repository key.
        surface
            A Region object specifying the surface to which the **controlPoints** are adjusted.
        controlPoints
            A Region object specifying the constraint control points.

        Returns
        -------
        AdjustPoints
            An AdjustPoints object.
        """
        super().__init__()

    @abaqus_method_doc
    def setValues(self, *args, **kwargs):
        """This method modifies the AdjustPoints object."""
        ...
