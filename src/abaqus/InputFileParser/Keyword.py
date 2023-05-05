from typing import Optional

from abqpy.decorators import abaqus_class_doc


@abaqus_class_doc
class Keyword:
    """The Keyword object is used to store a keyword definition from an Abaqus input file. Keyword objects are
    returned via the InputFile.parse() method.

    .. note::
        This object can be accessed by::

            import inpParser
    """

    #: A String specifying the name of the keyword.
    name: str = ""

    #: A Dictionary of Strings specifying the keyword parameters.
    parameter: Optional[dict] = None

    #: A sequence of sequences or an AbaqusNDarray object specifying the keyword data. The type
    #: of the leaf objects depends on the keyword. The AbaqusNDarray object is returned only if
    #: the data is suitable and if the InputFile.parse() method was called with the option
    #: usePyArray=True. In cases where large amounts of numerical data (i.e., large node
    #: arrays) are expected, it is recommended that you use the option usePyArray=True.
    data: tuple = ()

    #: A KeywordSequence specifying the suboptions of the keyword.
    suboptions: str = ""

    #: A sequence of Strings specifying the comments.
    comments: tuple = ()
