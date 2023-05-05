from abqpy.decorators import abaqus_class_doc, abaqus_function_doc

from ..Odb.Odb import Odb
from ..Part.Part import Part
from ..Region.Region import Region


@abaqus_class_doc
class PlyStackPlot:
    """The PlyStackPlot object is used to plot the stacking of plies in a composite layup or in a composite
    shell section.

    .. note::
        This object can be accessed by::

            import section
            import visualization
    """


@abaqus_function_doc
def MdbPlyStackPlot(part: Part, region: Region) -> PlyStackPlot:
    """This method creates a PlyStackPlot object from a region of a part that contains a composite shell layup.

    .. note::
        This function can be accessed by::

            section.MdbPlyStackPlot

    Parameters
    ----------
    part
        A Part object.
    region
        A Region object which contains a composite shell layup.

    Returns
    -------
    PlyStackPlot
        A PlyStackPlot object.

    Raises
    ------
        None.
    """
    return PlyStackPlot()


@abaqus_function_doc
def OdbPlyStackPlot(odb: Odb, sectionName: str, offset: float = 0):
    """This method creates a PlyStackPlot object from a composite shell section of an Odb object.

    .. note::
        This function can be accessed by::

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

    Raises
    ------
        None.
    """
    return PlyStackPlot()
