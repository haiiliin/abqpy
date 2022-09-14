from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from .ContactProperty import ContactProperty


@abaqus_class_doc
class ActuatorSensorProp(ContactProperty):
    """The ActuatorSensorProp object is an interaction property that defines the properties
    referred to by an ActuatorSensor object.
    The ActuatorSensorProp object is derived from the InteractionProperty object.

    .. note:: 
        This object can be accessed by::

            import interaction
            mdb.models[name].interactionProperties[name]

        The corresponding analysis keywords are:

        - UEL PROPERTY
    """

    #: A String specifying the interaction property repository key.
    name: str

    #: A sequence of Floats specifying the PROPS array used by user subroutine UEL. The default
    #: value is an empty sequence.
    realProperties: tuple = ()

    #: A sequence of Ints specifying the JPROPS array used by user subroutine UEL. The default
    #: value is an empty sequence.
    integerProperties: tuple = ()

    @abaqus_method_doc
    def __init__(
        self, name: str, realProperties: tuple = (), integerProperties: tuple = ()
    ):
        """This method creates an ActuatorSensorProp object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].ActuatorSensorProp

        Parameters
        ----------
        name
            A String specifying the interaction property repository key.
        realProperties
            A sequence of Floats specifying the PROPS array used by user subroutine UEL. The default
            value is an empty sequence.
        integerProperties
            A sequence of Ints specifying the JPROPS array used by user subroutine UEL. The default
            value is an empty sequence.

        Returns
        -------
        ActuatorSensorProp
            An :py:class:`~abaqus.Interaction.ActuatorSensorProp.ActuatorSensorProp` object.
        """
        super().__init__(name)

    @abaqus_method_doc
    def setValues(self, realProperties: tuple = (), integerProperties: tuple = ()):
        """This method modifies the ActuatorSensorProp object.

        Parameters
        ----------
        realProperties
            A sequence of Floats specifying the PROPS array used by user subroutine UEL. The default
            value is an empty sequence.
        integerProperties
            A sequence of Ints specifying the JPROPS array used by user subroutine UEL. The default
            value is an empty sequence.
        """
        ...
