from abqpy.decorators import abaqus_class_doc

from .DGCommonOptions import DGCommonOptions
from .DGContourOptions import DGContourOptions
from .DGDisplayBodyOptions import DGDisplayBodyOptions
from .DGOrientationOptions import DGOrientationOptions
from .DGSuperimposeOptions import DGSuperimposeOptions
from .DGSymbolOptions import DGSymbolOptions


@abaqus_class_doc
class OdbDisplayOptions:
    """The OdbDisplayOptions object stores the display options associated with an OdbInstance object. This
    object does not have a constructor. Abaqus creates the OdbDisplayOptions object when an OdbInstance object
    is created using the display options associated with the current viewport at the time of creation.

    .. note::
        This object can be accessed by::

            import assembly
            session.viewports[name].assemblyDisplay.displayGroupInstances[name].odbDisplayOptions
            session.viewports[name].layers[name].assemblyDisplay.displayGroupInstances[name].odbDisplayOptions
            import visualization
            session.viewports[name].layers[name].odbDisplay.displayGroupInstances[name].odbDisplayOptions
            import part
            session.viewports[name].layers[name].partDisplay.displayGroupInstances[name].odbDisplayOptions
            session.viewports[name].odbDisplay.displayGroupInstances[name].odbDisplayOptions
            session.viewports[name].partDisplay.displayGroupInstances[name].odbDisplayOptions
    """

    #: A DGCommonOptions object.
    commonOptions: DGCommonOptions = DGCommonOptions()

    #: A DGSuperimposeOptions object.
    superimposeOptions: DGSuperimposeOptions = DGSuperimposeOptions()

    #: A DGContourOptions object.
    contourOptions: DGContourOptions = DGContourOptions()

    #: A DGSymbolOptions object.
    symbolOptions: DGSymbolOptions = DGSymbolOptions()

    #: A DGOrientationOptions object.
    materialOrientationOptions: DGOrientationOptions = DGOrientationOptions()

    #: A DGDisplayBodyOptions object.
    displayBodyOptions: DGDisplayBodyOptions = DGDisplayBodyOptions()
