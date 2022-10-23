from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from .Interaction import Interaction
from ..Region.Region import Region
from ..UtilityAndView.abaqusConstants import Boolean


@abaqus_class_doc
class ActuatorSensor(Interaction):
    """The ActuatorSensor object defines a single point actuator where the actuation is
    determined by a user subroutine (UEL). The subroutine senses the data at the same point
    as the actuator.
    The ActuatorSensor object is derived from the Interaction object.

    .. note::
        This object can be accessed by::

            import interaction
            mdb.models[name].interactions[name]

        The corresponding analysis keywords are:

        - ELEMENT
        - USER ELEMENT
        - INITIAL CONDITIONS
    """

    #: A String specifying the repository key.
    name: str

    #: A String specifying the name of the step in which the actuator/sensor interaction is
    #: created. **createStepName** must be set to 'Initial'.
    createStepName: str

    #: A :py:class:`~abaqus.Region.Region.Region` object specifying the point at which the constraint is applied.
    point: Region

    #: A String specifying the ActuatorSensorProp object associated with this interaction.
    interactionProperty: str

    #: An Int specifying the number of coordinate components supplied to the user subroutine
    #: (UEL).
    noCoordComponents: int

    #: A Boolean specifying whether the element matrices are symmetric (ON) or unsymmetric
    #: (OFF). The default value is OFF.
    unsymm: Boolean

    #: An Int specifying the number of solution-dependent variables. The default value is 0.
    noSolutionDepVar: int

    #: A String specifying the name of the user subroutine (UEL) that defines the user element.
    userSubUel: str

    #: A String specifying the degrees of freedom, separated by commas.
    dof: str

    #: A sequence of Floats specifying the initial values of the solution-dependent variables.
    solutionDepVars: tuple

    @abaqus_method_doc
    def __init__(
        self,
        name: str,
        createStepName: str,
        point: Region,
        interactionProperty: str,
        noCoordComponents: int,
        unsymm: Boolean,
        noSolutionDepVar: int,
        userSubUel: str,
        dof: str,
        solutionDepVars: tuple,
    ):
        """This method creates an ActuatorSensor object.

        .. note::
            This function can be accessed by::

                mdb.models[name].ActuatorSensor

        Parameters
        ----------
        name
            A String specifying the repository key.
        createStepName
            A String specifying the name of the step in which the actuator/sensor interaction is
            created. **createStepName** must be set to 'Initial'.
        point
            A :py:class:`~abaqus.Region.Region.Region` object specifying the point at which the constraint is applied.
        interactionProperty
            A String specifying the ActuatorSensorProp object associated with this interaction.
        noCoordComponents
            An Int specifying the number of coordinate components supplied to the user subroutine
            (UEL).
        unsymm
            A Boolean specifying whether the element matrices are symmetric (ON) or unsymmetric
            (OFF). The default value is OFF.
        noSolutionDepVar
            An Int specifying the number of solution-dependent variables. The default value is 0.
        userSubUel
            A String specifying the name of the user subroutine (UEL) that defines the user element.
        dof
            A String specifying the degrees of freedom, separated by commas.
        solutionDepVars
            A sequence of Floats specifying the initial values of the solution-dependent variables.

        Returns
        -------
        ActuatorSensor
            An :py:class:`~abaqus.Interaction.ActuatorSensor.ActuatorSensor` object.
        """
        super().__init__()

    @abaqus_method_doc
    def setValues(self, *args, **kwargs):
        """This method modifies the ActuatorSensor object."""
        ...
