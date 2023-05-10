from typing import Optional

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from ..DisplayOptions.AssemblyDisplayOptions import AssemblyDisplayOptions
from ..DisplayOptions.PartDisplayOptions import PartDisplayOptions
from ..OdbDisplay.OdbDisplay import OdbDisplay
from ..UtilityAndView.View import View
from .Displayable import Displayable


@abaqus_class_doc
class Layer:
    """Objects can be superimposed by displaying them in different layers of a viewport.

    .. note::
        This object can be accessed by::

            session.viewports[name].layers[name]
    """

    #: A Displayable object specifying the object to be displayed. The
    #: Displayable type is an abstract generalization. The concrete possible types are Part, Assembly,
    #: ConstrainedSketch, Odb, or XYPlot.
    displayedObject: Displayable = Displayable()

    #: A View object specifying the object that controls viewing of the layer.
    view: Optional[View] = None

    #: An OdbDisplay object specifying the display options for the Odb object.
    odbDisplay: OdbDisplay = OdbDisplay()

    #: A PartDisplayOptions object specifying the display options
    #: for the Part object.
    partDisplay: PartDisplayOptions = PartDisplayOptions()

    #: An AssemblyDisplayOptions object specifying the
    #: display options for the Assembly object.
    assemblyDisplay: AssemblyDisplayOptions = AssemblyDisplayOptions()

    #: A String specifying the repository key.
    name: str

    #: A String specifying the name of the layer to copy.
    copyViewName: str = ""

    @abaqus_method_doc
    def __init__(self, name: str, copyViewName: str = ""):
        """This method creates a Layer object in the Layer repository.

        .. note::
            This function can be accessed by::

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
            A Layer object.
        """
        self.name = name
        self.copyViewName = copyViewName

    @abaqus_method_doc
    def moveBefore(self, name: str):
        """This method moves the layer object before another object in the layer repository.

        Parameters
        ----------
        name
            A String specifying the name of the other Layer object.
        """
        # TODO: implement this method
        ...

    @abaqus_method_doc
    def moveAfter(self, name: str):
        """This method moves the layer object after another object in the layer repository.

        Parameters
        ----------
        name
            A String specifying the name of the other Layer object.
        """
        # TODO: implement this method
        ...
