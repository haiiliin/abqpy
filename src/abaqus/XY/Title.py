from typing import Optional

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from ..UtilityAndView.abaqusConstants import OFF, Boolean
from .Area import Area
from .TextStyle import TextStyle


@abaqus_class_doc
class Title:
    """The Title object is used to store the display attributes of the XYPlot title. An Title object is
    automatically created when creating a XYPlot object.

    .. note::
        This object can be accessed by::

            import visualization
            session.defaultPlot.title
            session.xyPlots[name].title
    """

    #: A Boolean specifying whether to show the default title. The default value is OFF.
    useDefault: Boolean = OFF

    #: An Area object specifying the area of the title.
    area: Area = Area()

    #: A String specifying the text to appear as a title. By default the title is set to the
    #: XYPlot object name. The default value is an empty string.
    text: str = ""

    #: A TextStyle object specifying the text properties used to display the legend title.
    titleStyle: TextStyle = TextStyle()

    @abaqus_method_doc
    def setValues(
        self,
        title: "Title",
        text: str = "",
        area: Optional[Area] = None,
        useDefault: Boolean = OFF,
        titleStyle: Optional[TextStyle] = None,
    ):
        """This method modifies the Title object.

        Parameters
        ----------
        title
            A Title object from which attributes are to be copied.
        text
            A String specifying the text to appear as a title. By default the title is set to the
            XYPlot object name. The default value is an empty string.
        area
            An Area object specifying the area of the title.
        useDefault
            A Boolean specifying whether to show the default title. The default value is OFF.
        titleStyle
            A TextStyle object specifying the text properties used to display the legend title.
        """
        ...
