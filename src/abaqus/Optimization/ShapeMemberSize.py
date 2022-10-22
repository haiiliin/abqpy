from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from .GeometricRestriction import GeometricRestriction
from ..Region.Region import Region
from ..UtilityAndView.abaqusConstants import MINIMUM, OFF, SymbolicConstant


@abaqus_class_doc
class ShapeMemberSize(GeometricRestriction):
    """The ShapeMemberSize object defines a shape member size geometric restriction.
    The ShapeMemberSize object is derived from the GeometricRestriction object.

    .. note:: 
        This object can be accessed by::

            import optimization
            mdb.models[name].optimizationTasks[name].geometricRestrictions[name]
    """

    #: A String specifying the geometric restriction repository key.
    name: str

    #: A :py:class:`~abaqus.Region.Region.Region` object specifying the region to which the geometric restriction is applied.
    #: When used with a TopologyTask, there is no default value. When used with a ShapeTask,
    #: the default value is MODEL.
    region: Region

    #: A Float specifying the maximum thickness. The default value is 0.0.
    maxThickness: float = 0

    #: A Float specifying the minimum thickness. The default value is 0.0.
    minThickness: float = 0

    #: A SymbolicConstant specifying whether to restrict the minimum or maximum thickness.
    #: Possible values are MAXIMUM and MINIMUM. The default value is MINIMUM.
    sizeRestriction: SymbolicConstant = MINIMUM

    #: A bool specifying whether to use the node group region. The default value is OFF.
    #:
    #: .. versionadded:: 2022
    #:     The `assignNodeGroupRegion` attribute was added.
    assignNodeGroupRegion: str = OFF

    #: A Node Region object specifying the check node group.
    #:
    #: .. versionadded:: 2022
    #:     The `nodeGroupRegion` attribute was added.
    nodeGroupRegion: str = ""

    @abaqus_method_doc
    def __init__(
        self,
        name: str,
        region: Region,
        maxThickness: float = 0,
        minThickness: float = 0,
        sizeRestriction: SymbolicConstant = MINIMUM,
        assignNodeGroupRegion: str = OFF,
        nodeGroupRegion: str = "",
    ):
        """This method creates a ShapeMemberSize object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].optimizationTasks[name].ShapeMemberSize

        Parameters
        ----------
        name
            A String specifying the geometric restriction repository key.
        region
            A :py:class:`~abaqus.Region.Region.Region` object specifying the region to which the geometric restriction is applied.
            When used with a TopologyTask, there is no default value. When used with a ShapeTask,
            the default value is MODEL.
        maxThickness
            A Float specifying the maximum thickness. The default value is 0.0.
        minThickness
            A Float specifying the minimum thickness. The default value is 0.0.
        sizeRestriction
            A SymbolicConstant specifying whether to restrict the minimum or maximum thickness.
            Possible values are MAXIMUM and MINIMUM. The default value is MINIMUM.
        assignNodeGroupRegion
            A bool specifying whether to use the node group region. The default value is OFF.

            .. versionadded:: 2022
                The `assignNodeGroupRegion` argument was added.
        nodeGroupRegion
            A Node Region object specifying the check node group.

            .. versionadded:: 2022
                The `nodeGroupRegion` argument was added.

        Returns
        -------
        ShapeMemberSize
            A :py:class:`~abaqus.Optimization.ShapeMemberSize.ShapeMemberSize` object.
        """
        super().__init__()

    @abaqus_method_doc
    def setValues(
        self,
        maxThickness: float = 0,
        minThickness: float = 0,
        sizeRestriction: SymbolicConstant = MINIMUM,
        assignNodeGroupRegion: str = OFF,
        nodeGroupRegion: str = "",
    ):
        """This method modifies the ShapeMemberSize object.

        Parameters
        ----------
        maxThickness
            A Float specifying the maximum thickness. The default value is 0.0.
        minThickness
            A Float specifying the minimum thickness. The default value is 0.0.
        sizeRestriction
            A SymbolicConstant specifying whether to restrict the minimum or maximum thickness.
            Possible values are MAXIMUM and MINIMUM. The default value is MINIMUM.
        assignNodeGroupRegion
            A bool specifying whether to use the node group region. The default value is OFF.

            .. versionadded:: 2022
                The `assignNodeGroupRegion` argument was added.
        nodeGroupRegion
            A Node Region object specifying the check node group.

            .. versionadded:: 2022
                The `nodeGroupRegion` argument was added.
        """
        ...
