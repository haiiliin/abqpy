from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from typing_extensions import Literal

from .ContactProperty import ContactProperty
from ..UtilityAndView.abaqusConstants import Boolean, OFF, SymbolicConstant
from ..UtilityAndView.abaqusConstants import abaqusConstants as C


@abaqus_class_doc
class AcousticImpedanceProp(ContactProperty):
    """The AcousticImpedanceProp object is an interaction property that defines the properties
    referred to by an AcousticImpedance object.
    The AcousticImpedanceProp object is derived from the InteractionProperty object.

    .. note::
        This object can be accessed by::

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

    @abaqus_method_doc
    def __init__(
        self,
        name: str,
        tableType: Literal[C.ADMITTANCE, C.IMPEDANCE],
        table: tuple,
        frequencyDependency: Boolean = OFF,
    ):
        """This method creates an AcousticImpedanceProp object.

        .. note::
            This function can be accessed by::

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

    @abaqus_method_doc
    def setValues(self, frequencyDependency: Boolean = OFF):
        """This method modifies the AcousticImpedanceProp object.

        Parameters
        ----------
        frequencyDependency
            A Boolean specifying whether the **table** data depend on frequency. The default value is
            OFF.
        """
        ...
