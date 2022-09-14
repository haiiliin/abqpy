from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from .GeometricRestriction import GeometricRestriction
from ..Region.Region import Region
from ..UtilityAndView.abaqusConstants import *


@abaqus_class_doc
class TopologyOverhangControl(GeometricRestriction):
    """The TopologyOverhangControl object defines a topology overhang control geometric
    restriction.
    The TopologyOverhangControl object is derived from the GeometricRestriction object.

    .. note::
        This object can be accessed by::

            import optimization
            mdb.models[name].optimizationTasks[name].geometricRestrictions[name]

    .. versionadded:: 2019
        The `TopologyOverhangControl` class was added.
    """

    @abaqus_method_doc
    def __init__(
        self,
        name: str,
        pullDirection: tuple,
        region: Region,
        csys: int = None,
        draftAngle: float = 45,
        overhangCheckRegion: SymbolicConstant = OVERHANG_REGION,
        pointRegion: Region = Region(),
        radius: float = None,
        technique: SymbolicConstant = AUTO,
    ):
        """This method creates a TopologyOverhangControl object.

        .. note::
            This function can be accessed by::

                mdb.models[name].optimizationTasks[name].TopologyOverhangControl

        Parameters
        ----------
        name
            A String specifying the geometric restriction repository key.
        pullDirection
            A VertexArray object of length 2 specifying the overhang control print direction.
            Instead of through a ConstrainedSketchVertex, each point can be specified through a tuple of coordinates.
        region
            A Region object specifying the region to which the geometric restriction is applied.
        csys
            None or a DatumCsys object specifying the local coordinate system of the
            *pullDirection*. If **csys** = None, the global coordinate system is used. When this member
            is queried, it returns an Int indicating the identifier of the DatumCsys. The default
            value is None.
        draftAngle
            A Float specifying the overhang angle. The default value is 45.0.
        overhangCheckRegion
            The SymbolicConstant OVERHANG_REGION or a Region object specifying the overhang check
            region. If the value is OVERHANG_REGION, the value of **region** is used as both the
            overhang control region and the overhang check region. The default value is
            OVERHANG_REGION.
        pointRegion
            A Region object specifying the point on a plane perpendicular to the *pullDirection*
            that is used to specify the base plane when **technique** is POINT.
        radius
            A Float specifying the radius to define the size of the cones that are used in the
            internal check for the overhang criteria.
        technique
            A SymbolicConstant specifying the overhang control technique used to define the base
            plane. Possible values are AUTO, POINT, and NONE. The default value is AUTO.

        Returns
        -------
            A TopologyOverhangControl object.
        """
        super().__init__()

    @abaqus_method_doc
    def setValues(
        self,
        csys: int = None,
        draftAngle: float = 45,
        overhangCheckRegion: SymbolicConstant = OVERHANG_REGION,
        pointRegion: Region = Region(),
        radius: float = None,
        technique: SymbolicConstant = AUTO,
    ):
        """This method modifies the TopologyOverhangControl object.

        Parameters
        ----------
        csys
            None or a DatumCsys object specifying the local coordinate system of the
            *pullDirection*. If **csys** = None, the global coordinate system is used. When this member
            is queried, it returns an Int indicating the identifier of the DatumCsys. The default
            value is None.
        draftAngle
            A Float specifying the overhang angle. The default value is 45.0.
        overhangCheckRegion
            The SymbolicConstant OVERHANG_REGION or a Region object specifying the overhang check
            region. If the value is OVERHANG_REGION, the value of **region** is used as both the
            overhang control region and the overhang check region. The default value is
            OVERHANG_REGION.
        pointRegion
            A Region object specifying the point on a plane perpendicular to the *pullDirection*
            that is used to specify the base plane when **technique** is POINT.
        radius
            A Float specifying the radius to define the size of the cones that are used in the
            internal check for the overhang criteria.
        technique
            A SymbolicConstant specifying the overhang control technique used to define the base
            plane. Possible values are AUTO, POINT, and NONE. The default value is AUTO.
        """
        ...
