from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from ..UtilityAndView.abaqusConstants import Boolean


@abaqus_class_doc
class InputFile:
    """The InputFile object is used to store the definitions in an Abaqus input file. InputFile objects can be
    created using the methods described in this section.

    .. note::
        This object can be accessed by::

            import inpParser
    """

    #: A String specifying the source file name of the Abaqus input file.
    file: str = ""

    #: A String specifying the directory where the input file is located.
    directory: str = ""

    #: A sequence of Strings specifying any additional input files included in the specified
    #: input file.
    includes: tuple = ()

    #: A sequence of Strings for input files included in the specified input file that could
    #: not be located.
    missingIncludes: tuple = ()

    @abaqus_method_doc
    def __init__(self, file: str, directory: str = ""):
        """This method creates an InputFile object by reading an Abaqus input file.

        .. note::
            This function can be accessed by::

                inpParser.InputFile

        Parameters
        ----------
        file
            A String specifying the path to the input file.
        directory
            A String specifying the path to the directory containing the input file.

        Returns
        -------
        InputFile
            An InputFile object.
        """
        ...

    @abaqus_method_doc
    def parse(
        self,
        organize: Boolean = False,
        verbose: Boolean = False,
        bulk: Boolean = True,
        usePyArray: Boolean = False,
    ):
        """This method parses the input file associated with the InputFile object.

        Parameters
        ----------
        organize
            A Boolean specifying whether keywords should be organized into suboptions. The default
            is False.
        verbose
            A Boolean specifying whether verbose output is to be printed. If **verbose** is True,
            information about fatal errors is printed. If no fatal errors occur, there is no output.
            The default is False.
        bulk
            A Boolean specifying whether the input file includes bulk data that should be parsed.
            The default is True.
        usePyArray
            A Boolean specifying that parse method can return an AbaqusNDarray object for a keyword
            data value. In cases where large amounts of numerical data (i.e., large node arrays) are
            expected, it is recommended that you use the option usePyArray=True. The default is
            False.

        Returns
        -------
        KeywordSequence
            A KeywordSequence object.

        Raises
        ------
        ValueError
            If you parse an input file more than once, a ValueError is raised for each subsequent
            parsing.
        """
        ...
