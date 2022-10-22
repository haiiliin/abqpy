from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from ..UtilityAndView.abaqusConstants import Boolean, ON


@abaqus_class_doc
class ConstraintDisplayOptions:
    """The ConstraintDisplayOptions object stores settings that specify how assemblies are to
    be displayed in a particular viewport when
    session.viewports[name].assemblyDisplay.constraints=ON
    The ConstraintDisplayOptions object has no constructor. When you create a new viewport,
    the settings are copied from the current viewport.

    .. note::
        This object can be accessed by::
        
            session.viewports[name].assemblyDisplay.constraintOptions
            session.viewports[name].layers[name].assemblyDisplay.constraintOptions
    """

    @abaqus_method_doc
    def setValues(
        self,
        constraintEquation: Boolean = ON,
        tieConstraint: Boolean = ON,
        rigidBodyConstraint: Boolean = ON,
        displayBodyConstraint: Boolean = ON,
        couplingConstrain: Boolean = ON,
    ):
        """This method modifies the ConstraintDisplayOptions object.

        Parameters
        ----------
        constraintEquation
            A Boolean specifying whether constraint equation symbols are shown. The default value is
            ON.
        tieConstraint
            A Boolean specifying whether tie constraint symbols are shown. The default value is ON.
        rigidBodyConstraint
            A Boolean specifying whether rigid body constraint symbols are shown. The default value
            is ON.
        displayBodyConstraint
            A Boolean specifying whether display body constraint symbols are shown. The default
            value is ON.
        couplingConstrain
            A Boolean specifying whether coupling constraint symbols are shown. The default value is
            ON.
        """
        ...
