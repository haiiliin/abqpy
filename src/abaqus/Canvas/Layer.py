from .Displayable import Displayable
from ..DisplayOptions.AssemblyDisplayOptions import AssemblyDisplayOptions
from ..DisplayOptions.PartDisplayOptions import PartDisplayOptions
from ..OdbDisplay.OdbDisplay import OdbDisplay
from ..UtilityAndView.View import View


class Layer:
    """Objects can be superimposed by displaying them in different layers of a viewport.

    .. note:: 
        This object can be accessed by:

        .. code-block:: python

            session.viewports[name].layers[name]
    """

    #: A :py:class:`~abaqus.Canvas.Displayable.Displayable` object specifying the object to be displayed. The Displayable type is an
    #: abstract generalization. The concrete possible types are Part, Assembly,
    #: ConstrainedSketch, Odb, or XYPlot.
    displayedObject: Displayable = Displayable()

    #: A :py:class:`~abaqus.UtilityAndView.View.View` object specifying the object that controls viewing of the layer.
    view: View = None

    #: An :py:class:`~abaqus.OdbDisplay.OdbDisplay.OdbDisplay` object specifying the display options for the Odb object.
    odbDisplay: OdbDisplay = OdbDisplay()

    #: A :py:class:`~abaqus.DisplayOptions.PartDisplayOptions.PartDisplayOptions` object specifying the display options for the Part object.
    partDisplay: PartDisplayOptions = PartDisplayOptions()

    #: An :py:class:`~abaqus.DisplayOptions.AssemblyDisplayOptions.AssemblyDisplayOptions` object specifying the display options for the Assembly object.
    assemblyDisplay: AssemblyDisplayOptions = AssemblyDisplayOptions()

    #: A String specifying the repository key.
    name: str

    #: A String specifying the name of the layer to copy.
    copyViewName: str = ""

    def __init__(self, name: str, copyViewName: str = ""):
        """This method creates a Layer object in the Layer repository.

        .. note:: 
            This function can be accessed by:

            .. code-block:: python

                session.viewports[name].Layer

        Parameters
        ----------
        name
            A String specifying the repository key.
        copyViewName
            A String specifying the name of the layer to copy.

        Returns
        -------
        Layer
            A :py:class:`~abaqus.Canvas.Layer.Layer` object.
        """
        pass

    def moveBefore(self, name: str):
        """This method moves the layer object before another object in the layer repository.

        Parameters
        ----------
        name
            A String specifying the name of the other Layer object.
        """
        pass

    def moveAfter(self, name: str):
        """This method moves the layer object after another object in the layer repository.

        Parameters
        ----------
        name
            A String specifying the name of the other Layer object.
        """
        pass
