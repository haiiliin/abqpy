from ..Odb.Odb import Odb
from ..Part.Part import Part
from ..Region.Region import Region


class PlyStackPlot:
    """The PlyStackPlot object is used to plot the stacking of plies in a composite layup or in
    a composite shell section.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import section
        import visualization

    """


def MdbPlyStackPlot(part: Part, region: Region):
    """This method creates a PlyStackPlot object from a region of a part that contains a
    composite shell layup.

    Notes
    -----
        This function can be accessed by:

        .. code-block:: python

            section.MdbPlyStackPlot

    Parameters
    ----------
    part
        A Part object.
    region
        A Region object which contains a composite shell layup.

    Returns
    -------
        A PlyStackPlot object.

    Exceptions
    ----------
        None.
    """
    return PlyStackPlot()


def OdbPlyStackPlot(odb: Odb, sectionName: str, offset: float = 0):
    """This method creates a PlyStackPlot object from a composite shell section of an Odb
    object.

    Notes
    -----
        This function can be accessed by:

        .. code-block:: python

            visualization.OdbPlyStackPlot

    Parameters
    ----------
    odb
        An Odb object.
    sectionName
        A String specifying the section name that contains a composite shell section.
    offset
        A Float specifying the shell offset. The default value is 0.0.

    Returns
    -------
        A PlyStackPlot object.

    Exceptions
    ----------
        None.
    """
    return PlyStackPlot()
