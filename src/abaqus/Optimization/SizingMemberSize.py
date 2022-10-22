from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from .GeometricRestriction import GeometricRestriction
from ..Region.Region import Region


@abaqus_class_doc
class SizingMemberSize(GeometricRestriction):
    """The SizingMemberSize object defines a sizing member size geometric restriction.
    The SizingMemberSize object is derived from the GeometricRestriction object.

    .. note:: 
        This object can be accessed by::

            import optimization
            mdb.models[name].optimizationTasks[name].geometricRestrictions[name]
    """

    #: A String specifying the geometric restriction repository key.
    name: str

    #: A :py:class:`~abaqus.Region.Region.Region` object specifying the region to which the geometric restriction is applied.
    region: Region

    #: A Float specifying the min width.
    minWidth: float

    @abaqus_method_doc
    def __init__(self, name: str, region: Region, minWidth: float):
        """This method creates a SizingMemberSize object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].optimizationTasks[name].SizingMemberSize

        Parameters
        ----------
        name
            A String specifying the geometric restriction repository key.
        region
            A :py:class:`~abaqus.Region.Region.Region` object specifying the region to which the geometric restriction is applied.
        minWidth
            A Float specifying the min width.

        Returns
        -------

        Raises
        ------
        """
        super().__init__()

    @abaqus_method_doc
    def setValues(self, *args, **kwargs):
        """This method modifies the sizingMemberSize object."""
        ...
