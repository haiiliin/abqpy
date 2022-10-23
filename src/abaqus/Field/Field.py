from abqpy.decorators import abaqus_class_doc


@abaqus_class_doc
class Field:
    """The Field object is the abstract base type for other Field objects. The Field object has
    no explicit constructor. The methods and members of the Field object are common to all
    objects derived from the Field.

    .. note::
        This object can be accessed by::

            import fields
    """

    #: A String specifying the repository key.
    name: str = ""

    #: A String specifying the description of the field. The default value is an empty string.
    description: str = ""
