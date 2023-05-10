from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from ..UtilityAndView.abaqusConstants import OFF, Boolean
from .ContactProperty import ContactProperty


@abaqus_class_doc
class CavityRadiationProp(ContactProperty):
    """The CavityRadiationProp object is an interaction property that defines emissivity as a function of
    temperature and field variables. The CavityRadiationProp object is derived from the InteractionProperty
    object.

    .. note::
        This object can be accessed by::

            import interaction
            mdb.models[name].interactionProperties[name]

        The corresponding analysis keywords are:

        - EMISSIVITY
    """

    #: A String specifying the interaction property repository key.
    name: str

    #: A Boolean specifying whether the data depend on temperature. The default value is OFF.
    temperatureDependency: Boolean = OFF

    #: An Int specifying the number of field variable dependencies. The default value is 0.
    dependencies: int = 0

    #: A sequence of sequences of Floats specifying the following:The emissivity,
    #: ϵϵ.Temperature, if the data depend on temperature.Value of the first field variable, if
    #: the data depend on field variables.Value of the second field variable.Etc.
    property: tuple = ()

    @abaqus_method_doc
    def __init__(
        self,
        name: str,
        temperatureDependency: Boolean = OFF,
        dependencies: int = 0,
        property: tuple = (),
    ):
        """This method creates a CavityRadiationProp object.

        .. note::
            This function can be accessed by::

                mdb.models[name].CavityRadiationProp

        Parameters
        ----------
        name
            A String specifying the interaction property repository key.
        temperatureDependency
            A Boolean specifying whether the data depend on temperature. The default value is OFF.
        dependencies
            An Int specifying the number of field variable dependencies. The default value is 0.
        property
            A sequence of sequences of Floats specifying the following:The emissivity,
            ϵϵ.Temperature, if the data depend on temperature.Value of the first field variable, if
            the data depend on field variables.Value of the second field variable.Etc.

        Returns
        -------
        CavityRadiationProp
            A CavityRadiationProp object.
        """
        super().__init__(name)

    @abaqus_method_doc
    def setValues(
        self,
        temperatureDependency: Boolean = OFF,
        dependencies: int = 0,
        property: tuple = (),
    ):
        """This method modifies the CavityRadiationProp object.

        Parameters
        ----------
        temperatureDependency
            A Boolean specifying whether the data depend on temperature. The default value is OFF.
        dependencies
            An Int specifying the number of field variable dependencies. The default value is 0.
        property
            A sequence of sequences of Floats specifying the following:The emissivity,
            ϵϵ.Temperature, if the data depend on temperature.Value of the first field variable, if
            the data depend on field variables.Value of the second field variable.Etc.
        """
        ...
