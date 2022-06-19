from abaqusConstants import *


class InputFile:
    """The InputFile object is used to store the definitions in an Abaqus input file. InputFile
    objects can be created using the methods described in this section.

    Attributes
    ----------
    file: str
        A String specifying the source file name of the Abaqus input file.
    directory: str
        A String specifying the directory where the input file is located.
    includes: tuple
        A sequence of Strings specifying any additional input files included in the specified
        input file.
    missingIncludes: tuple
        A sequence of Strings for input files included in the specified input file that could
        not be located.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import inpParser

    """

    # A String specifying the source file name of the Abaqus input file.
    file: str = ""

    # A String specifying the directory where the input file is located.
    directory: str = ""

    # A sequence of Strings specifying any additional input files included in the specified
    # input file.
    includes: tuple = ()

    # A sequence of Strings for input files included in the specified input file that could
    # not be located.
    missingIncludes: tuple = ()

    def __init__(self, file: str, directory: str = ""):
        """This method creates an InputFile object by reading an Abaqus input file.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            inpParser.InputFile

        Parameters
        ----------
        file
            A String specifying the path to the input file.
        directory
            A String specifying the path to the directory containing the input file.

        Returns
        -------
            An InputFile object.
        """
        pass

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
            A KeywordSequence object.

        Raises
        ------
            If you parse an input file more than once, a ValueError is raised for each subsequent
            parsing.
        """
        pass
