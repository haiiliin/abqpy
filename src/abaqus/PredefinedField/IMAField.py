from abqpy.decorators import abaqus_class_doc

from ..Region.Region import Region


@abaqus_class_doc
class IMAField:
    """A IMAField is an object used to define material instance name volume fractions for the
    MaterialAssignment predefined field.

    .. note::
        This object can be accessed by::

            import load
            mdb.models[name].predefinedFields[name].fieldList
    """

    #: A :py:class:`~abaqus.Region.Region.Region` object specifying the sub-region of the selected part instance to which the
    #: volume fractions will be applied.
    region: Region = Region()

    #: A tuple of Strings specifying the name of the discrete fields that contain the volume
    #: fraction data. The length of the tuple corresponds to the number of material instance
    #: names, as established by the assigned Eulerian section.
    discFieldList: tuple = ()
