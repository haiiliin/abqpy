from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from ..Region.Region import Region
from .GeometricRestriction import GeometricRestriction


@abaqus_class_doc
class FrozenArea(GeometricRestriction):
    """The FrozenArea object defines a frozen area geometric restriction. The FrozenArea object is derived from
    the GeometricRestriction object.

    .. note::
        This object can be accessed by::

            import optimization
            mdb.models[name].optimizationTasks[name].geometricRestrictions[name]
    """

    #: A String specifying the geometric restriction repository key.
    name: str

    #: A Region object specifying the region to which the geometric restriction is applied.
    #: When used with a TopologyTask, there is no default value. When used with a ShapeTask,
    #: the default value is MODEL.
    region: Region = Region()

    @abaqus_method_doc
    def __init__(self, name: str, region: Region = Region()):
        """This method creates a FrozenArea object.

        .. note::
            This function can be accessed by::

                mdb.models[name].optimizationTasks[name].FrozenArea

        Parameters
        ----------
        name
            A String specifying the geometric restriction repository key.
        region
            A Region object specifying the region to which the geometric restriction is applied.
            When used with a TopologyTask, there is no default value. When used with a ShapeTask,
            the default value is MODEL.

        Returns
        -------
        FrozenArea
            A FrozenArea object.
        """
        super().__init__()

    @abaqus_method_doc
    def setValues(self, region: Region = Region()):
        """This method modifies the FrozenArea object.

        Parameters
        ----------
        region
            A Region object specifying the region to which the geometric restriction is applied.
            When used with a TopologyTask, there is no default value. When used with a ShapeTask,
            the default value is MODEL.
        """
        ...
