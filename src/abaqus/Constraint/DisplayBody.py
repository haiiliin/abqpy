from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from ..Assembly.PartInstance import PartInstance
from ..BasicGeometry.ModelDotArray import ModelDotArray
from ..UtilityAndView.abaqusConstants import OFF, Boolean
from .Constraint import Constraint


@abaqus_class_doc
class DisplayBody(Constraint):
    """The DisplayBody object defines a constraint such that the specified instance is used for display only and
    does not take part in the analysis. However it will still be visible during postprocessing and its position
    at any frame will be defined by the translation and rotation of the specified control points. The
    DisplayBody object is derived from the ConstrainedSketchConstraint object.

    .. note::
        This object can be accessed by::

            import interaction
            mdb.models[name].constraints[name]

        The corresponding analysis keywords are:

        - DISPLAY BODY
    """

    #: A Boolean specifying whether the constraint is suppressed or not. The default value is
    #: OFF.
    suppressed: Boolean = OFF

    #: A String specifying the constraint repository key.
    name: str

    #: A PartInstance object specifying the part instance that is to be used for display only.
    instance: PartInstance

    #: A ModelDotArray object specifying the motion of the PartInstance. The control points may
    #: be ConstrainedSketchVertex, ReferencePoint, or MeshNode objects. Their motion will control the motion of
    #: the PartInstance. If this argument is set to an empty sequence, the PartInstance will
    #: remain fixed in space during the analysis. The sequence can have either one object or
    #: three objects.
    controlPoints: ModelDotArray

    @abaqus_method_doc
    def __init__(self, name: str, instance: PartInstance, controlPoints: ModelDotArray):
        """This method creates a DisplayBody object.

        .. note::
            This function can be accessed by::

                mdb.models[name].DisplayBody

        Parameters
        ----------
        name
            A String specifying the constraint repository key.
        instance
            A PartInstance object specifying the part instance that is to be used for display only.
        controlPoints
            A ModelDotArray object specifying the motion of the PartInstance. The control points may
            be ConstrainedSketchVertex, ReferencePoint, or MeshNode objects. Their motion will control the motion of
            the PartInstance. If this argument is set to an empty sequence, the PartInstance will
            remain fixed in space during the analysis. The sequence can have either one object or
            three objects.

        Returns
        -------
        DisplayBody
            A DisplayBody object.
        """
        super().__init__()

    @abaqus_method_doc
    def setValues(self, *args, **kwargs):
        """This method modifies the DisplayBody object."""
        ...
