from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from .GeometricRestriction import GeometricRestriction
from ..Region.Region import Region
from ..UtilityAndView.abaqusConstants import MINIMUM, SymbolicConstant


@abaqus_class_doc
class TopologyMemberSize(GeometricRestriction):
    """The TopologyMemberSize object defines a topology member size geometric restriction.
    The TopologyMemberSize object is derived from the GeometricRestriction object.

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

    #: A Float specifying the minimum gap. The default value is 0.0.
    separation: float = 0

    #: A SymbolicConstant specifying whether to restrict the minimum or maximum thickness or an
    #: envelope of both. Possible values are ENVELOPE, MAXIMUM, and MINIMUM. The default value
    #: is MINIMUM.
    sizeRestriction: SymbolicConstant = MINIMUM

    @abaqus_method_doc
    def __init__(
        self,
        name: str,
        region: Region,
        maxThickness: float = 0,
        minThickness: float = 0,
        separation: float = 0,
        sizeRestriction: SymbolicConstant = MINIMUM,
    ):
        """This method creates a TopologyMemberSize object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].optimizationTasks[name].TopologyMemberSize

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
        separation
            A Float specifying the minimum gap. The default value is 0.0.
        sizeRestriction
            A SymbolicConstant specifying whether to restrict the minimum or maximum thickness or an
            envelope of both. Possible values are ENVELOPE, MAXIMUM, and MINIMUM. The default value
            is MINIMUM.

        Returns
        -------
        TopologyMemberSize
            A :py:class:`~abaqus.Optimization.TopologyMemberSize.TopologyMemberSize` object.
        """
        super().__init__()

    @abaqus_method_doc
    def setValues(
        self,
        maxThickness: float = 0,
        minThickness: float = 0,
        separation: float = 0,
        sizeRestriction: SymbolicConstant = MINIMUM,
    ):
        """This method modifies the TopologyMemberSize object.

        Parameters
        ----------
        maxThickness
            A Float specifying the maximum thickness. The default value is 0.0.
        minThickness
            A Float specifying the minimum thickness. The default value is 0.0.
        separation
            A Float specifying the minimum gap. The default value is 0.0.
        sizeRestriction
            A SymbolicConstant specifying whether to restrict the minimum or maximum thickness or an
            envelope of both. Possible values are ENVELOPE, MAXIMUM, and MINIMUM. The default value
            is MINIMUM.
        """
        ...
