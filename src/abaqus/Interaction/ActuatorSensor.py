from abaqusConstants import *
from .Interaction import Interaction
from ..Region.Region import Region


class ActuatorSensor(Interaction):
    """The ActuatorSensor object defines a single point actuator where the actuation is
    determined by a user subroutine (UEL). The subroutine senses the data at the same point
    as the actuator.
    The ActuatorSensor object is derived from the Interaction object.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import interaction
        mdb.models[name].interactions[name]

    The corresponding analysis keywords are:

    - ELEMENT
            - USER ELEMENT
            - INITIAL CONDITIONS

    """

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

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            mdb.models[name].ActuatorSensor

        Parameters
        ----------
        name
            A String specifying the repository key.
        createStepName
            A String specifying the name of the step in which the actuator/sensor interaction is
            created. **createStepName** must be set to 'Initial'.
        point
            A Region object specifying the point at which the constraint is applied.
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
            An ActuatorSensor object.
        """
        super().__init__()
        pass

    def setValues(self):
        """This method modifies the ActuatorSensor object."""
        pass
