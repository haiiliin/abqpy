from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from .ContactProperty import ContactProperty
from ..UtilityAndView.abaqusConstants import Boolean, OFF


@abaqus_class_doc
class FilmConditionProp(ContactProperty):
    """The FilmConditionProp object is an interaction property that defines a film coefficient
    as a function of temperature and field variables.
    The FilmConditionProp object is derived from the InteractionProperty object.

    .. note:: 
        This object can be accessed by::

            import interaction
            mdb.models[name].interactionProperties[name]

        The corresponding analysis keywords are:

        - FILM PROPERTY
    """

    #: A String specifying the interaction property repository key.
    name: str

    #: A Boolean specifying whether the data depend on temperature. The default value is OFF.
    temperatureDependency: Boolean = OFF

    #: An Int specifying the number of field variable dependencies. The default value is 0.
    dependencies: int = 0

    #: A sequence of sequences of Floats specifying the following:
    #: 
    #: - The film coefficient, hh.
    #: - Temperature, if the data depend on temperature.
    #: - Value of the first field variable, if the data depend on field variables.
    #: - Value of the second field variable.
    #: - Etc.
    property: tuple = ()

    @abaqus_method_doc
    def __init__(
        self,
        name: str,
        temperatureDependency: Boolean = OFF,
        dependencies: int = 0,
        property: tuple = (),
    ):
        """This method creates a FilmConditionProp object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].FilmConditionProp

        Parameters
        ----------
        name
            A String specifying the interaction property repository key.
        temperatureDependency
            A Boolean specifying whether the data depend on temperature. The default value is OFF.
        dependencies
            An Int specifying the number of field variable dependencies. The default value is 0.
        property
            A sequence of sequences of Floats specifying the following:
            
            - The film coefficient, hh.
            - Temperature, if the data depend on temperature.
            - Value of the first field variable, if the data depend on field variables.
            - Value of the second field variable.
            - Etc.

        Returns
        -------
        FilmConditionProp
            A :py:class:`~abaqus.Interaction.FilmConditionProp.FilmConditionProp` object.
        """
        super().__init__(name)

    @abaqus_method_doc
    def setValues(
        self,
        temperatureDependency: Boolean = OFF,
        dependencies: int = 0,
        property: tuple = (),
    ):
        """This method modifies the FilmConditionProp object.

        Parameters
        ----------
        temperatureDependency
            A Boolean specifying whether the data depend on temperature. The default value is OFF.
        dependencies
            An Int specifying the number of field variable dependencies. The default value is 0.
        property
            A sequence of sequences of Floats specifying the following:
            
            - The film coefficient, hh.
            - Temperature, if the data depend on temperature.
            - Value of the first field variable, if the data depend on field variables.
            - Value of the second field variable.
            - Etc.
        """
        ...
