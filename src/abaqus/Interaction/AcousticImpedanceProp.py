from abaqusConstants import *
from .ContactProperty import ContactProperty


class AcousticImpedanceProp(ContactProperty):
    """The AcousticImpedanceProp object is an interaction property that defines the properties
    referred to by an AcousticImpedance object.
    The AcousticImpedanceProp object is derived from the InteractionProperty object.

    .. note:: 
        This object can be accessed by:

        .. code-block:: python

            import interaction
            mdb.models[name].interactionProperties[name]

        The corresponding analysis keywords are:

        - IMPEDANCE PROPERTY
    """

    #: A String specifying the interaction property repository key.
    name: str

    #: A SymbolicConstant specifying the type of tabular data to be defined. Possible values
    #: are IMPEDANCE and ADMITTANCE.
    tableType: SymbolicConstant

    #: A sequence of sequences of Floats specifying acoustic impedance properties.If
    #: **tableType** = IMPEDANCE, each sequence of the table data specifies:The real part of the
    #: complex impedance.The imaginary part of the complex impedance.Frequency, if the data
    #: depend on frequency.If **tableType** = ADMITTANCE, each sequence of the table data
    #: specifies:The real part of the complex admittance.The imaginary part of the complex
    #: admittance.Frequency, if the data depend on frequency.
    table: tuple

    #: A Boolean specifying whether the **table** data depend on frequency. The default value is
    #: OFF.
    frequencyDependency: Boolean = OFF

    def __init__(
        self,
        name: str,
        tableType: SymbolicConstant,
        table: tuple,
        frequencyDependency: Boolean = OFF,
    ):
        """This method creates an AcousticImpedanceProp object.

        .. note:: 
            This function can be accessed by:

            .. code-block:: python

                mdb.models[name].AcousticImpedanceProp

        Parameters
        ----------
        name
            A String specifying the interaction property repository key.
        tableType
            A SymbolicConstant specifying the type of tabular data to be defined. Possible values
            are IMPEDANCE and ADMITTANCE.
        table
            A sequence of sequences of Floats specifying acoustic impedance properties.If
            **tableType** = IMPEDANCE, each sequence of the table data specifies:The real part of the
            complex impedance.The imaginary part of the complex impedance.Frequency, if the data
            depend on frequency.If **tableType** = ADMITTANCE, each sequence of the table data
            specifies:The real part of the complex admittance.The imaginary part of the complex
            admittance.Frequency, if the data depend on frequency.
        frequencyDependency
            A Boolean specifying whether the **table** data depend on frequency. The default value is
            OFF.

        Returns
        -------
        AcousticImpedanceProp
            An :py:class:`~abaqus.Interaction.AcousticImpedanceProp.AcousticImpedanceProp` object.
        """
        super().__init__(name)
        pass

    def setValues(self, frequencyDependency: Boolean = OFF):
        """This method modifies the AcousticImpedanceProp object.

        Parameters
        ----------
        frequencyDependency
            A Boolean specifying whether the **table** data depend on frequency. The default value is
            OFF.
        """
        pass
