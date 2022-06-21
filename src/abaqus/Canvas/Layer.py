from .Displayable import Displayable
from ..DisplayOptions.AssemblyDisplayOptions import AssemblyDisplayOptions
from ..DisplayOptions.PartDisplayOptions import PartDisplayOptions
from ..OdbDisplay.OdbDisplay import OdbDisplay
from ..UtilityAndView.View import View


class Layer:
    """Objects can be superimposed by displaying them in different layers of a viewport.

    Attributes
    ----------
    displayedObject: Displayable
        A :py:class:`~abaqus.Canvas.Displayable.Displayable` object specifying :py:class:`~.the` object to be displayed. The :py:class:`~abaqus.Canvas.Displayable.Displayable` type is an
        abstract generalization. The concrete possible types are Part, Assembly,
        ConstrainedSketch, Odb, or XYPlot.
    view: View
        A :py:class:`~abaqus.UtilityAndView.View.View` object specifying :py:class:`~.the` object that controls viewing of :py:class:`~.the` layer.
    odbDisplay: OdbDisplay
        An :py:class:`~abaqus.:py:class:`~abaqus.Odb.Odb.Odb`Display.:py:class:`~abaqus.Odb.Odb.Odb`Display.:py:class:`~abaqus.Odb.Odb.Odb`Display` object specifying the display options for the :py:class:`~abaqus.Odb.Odb.Odb` object.
    partDisplay: PartDisplayOptions
        A :py:class:`~abaqus.DisplayOptions.:py:class:`~abaqus.Part.Part.Part`DisplayOptions.:py:class:`~abaqus.Part.Part.Part`DisplayOptions` object specifying the display options for the :py:class:`~abaqus.Part.Part.Part` object.
    assemblyDisplay: AssemblyDisplayOptions
        An :py:class:`~abaqus.DisplayOptions.:py:class:`~abaqus.Assembly.Assembly.Assembly`DisplayOptions.:py:class:`~abaqus.Assembly.Assembly.Assembly`DisplayOptions` object specifying the display options for the :py:class:`~abaqus.Assembly.Assembly.Assembly` object.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        session.viewports[name].layers[name]
    """

    # A :py:class:`~abaqus.Canvas.Displayable.Displayable` object specifying the object to be displayed. The Displayable type is an
    # abstract generalization. The concrete possible types are Part, Assembly,
    # ConstrainedSketch, Odb, or XYPlot.
    displayedObject: Displayable = Displayable()

    # A :py:class:`~abaqus.UtilityAndView.View.View` object specifying the object that controls viewing of the layer.
    view: View = None

    # An :py:class:`~abaqus.OdbDisplay.OdbDisplay.OdbDisplay` object specifying the display options for the Odb object.
    odbDisplay: OdbDisplay = OdbDisplay()

    # A :py:class:`~abaqus.DisplayOptions.PartDisplayOptions.PartDisplayOptions` object specifying the display options for the Part object.
    partDisplay: PartDisplayOptions = PartDisplayOptions()

    # An :py:class:`~abaqus.DisplayOptions.AssemblyDisplayOptions.AssemblyDisplayOptions` object specifying the display options for the Assembly object.
    assemblyDisplay: AssemblyDisplayOptions = AssemblyDisplayOptions()

    def __init__(self, name: str, copyViewName: str = ""):
        """This method creates a Layer object in the Layer repository.

        Notes
        -----
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
