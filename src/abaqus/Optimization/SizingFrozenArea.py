from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from .GeometricRestriction import GeometricRestriction
from ..Region.Region import Region


@abaqus_class_doc
class SizingFrozenArea(GeometricRestriction):
    """The SizingFrozenArea object defines a sizing frozen area geometric restriction.
    The SizingFrozenArea object is derived from the GeometricRestriction object.

    .. note:: 
        This object can be accessed by::

            import optimization
            mdb.models[name].optimizationTasks[name].geometricRestrictions[name]
    """

    #: A String specifying the geometric restriction repository key.
    name: str

    #: A :py:class:`~abaqus.Region.Region.Region` object specifying the region to which the geometric restriction is applied.
    region: Region

    @abaqus_method_doc
    def __init__(self, name: str, region: Region):
        """This method creates a SizingFrozenArea object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].optimizationTasks[name].SizingFrozenArea

        Parameters
        ----------
        name
            A String specifying the geometric restriction repository key.
        region
            A :py:class:`~abaqus.Region.Region.Region` object specifying the region to which the geometric restriction is applied.

        Returns
        -------
        SizingFrozenArea
            A :py:class:`~abaqus.Optimization.SizingFrozenArea.SizingFrozenArea` object.
        """
        super().__init__()

    @abaqus_method_doc
    def setValues(self, *args, **kwargs):
        """This method modifies the SizingFrozenArea object."""
        ...
