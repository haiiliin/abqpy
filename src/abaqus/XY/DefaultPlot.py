from abqpy.decorators import abaqus_class_doc

from .Area import Area
from .Title import Title


@abaqus_class_doc
class DefaultPlot:
    """The DefaultPlot object is used to hold on default plot attributes. The DefaultPlot object attributes are
    used whenever an XYPlot object is created. A DefaultPlot object is automatically created when opening a
    session.

    .. note::
        This object can be accessed by::

            import visualization
            session.defaultPlot
    """

    #: An Area object specifying an Area used to hold on to the default display properties for
    #: the plot area.
    area: Area = Area()

    #: A Title object specifying a Title object used to hold on to the default properties of
    #: the XY-Plot title.
    title: Title = Title()
