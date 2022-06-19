from abaqusConstants import *
from .PredefinedField import PredefinedField
from ..Region.Region import Region


class KinematicHardening(PredefinedField):
    """The KinematicHardening object stores the data for initial equivalent Plastic strains
    and, if relevant, the initial backstress tensor.
    The KinematicHardening object is derived from the PredefinedField object.

    Attributes
    ----------
    field: str
        A String specifying the name of the :py:class:`~abaqus.Field.AnalyticalField.AnalyticalField` object associated with this
        predefined field. The **field** argument applies only when
        **distributionType=ANALYTICAL_FIELD**. The default value is an empty string.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import load
        mdb.models[name].predefinedFields[name]

    The corresponding analysis keywords are:

    - INITIAL CONDITIONS
    """

    # A String specifying the name of the AnalyticalField object associated with this
    # predefined field. The **field** argument applies only when
    # **distributionType**=ANALYTICAL_FIELD. The default value is an empty string.
    field: str = ""

    def __init__(
        self,
        name: str,
        region: Region,
        numBackStress: int = 1,
        equivPlasticStrain: tuple = (),
        backStress: tuple = (),
        sectPtNum: tuple = (),
        definition: SymbolicConstant = KINEMATIC_HARDENING,
        rebarLayerNames: tuple = (),
        distributionType: SymbolicConstant = MAGNITUDE,
    ):
        """This method creates a KinematicHardening object.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            mdb.models[name].KinematicHardening

        Parameters
        ----------
        name
            A String specifying the repository key.
        region
            A Region object specifying the region to which the predefined field is applied.
        numBackStress
            An Int specifying the number of backstresses. The default value is 1.
        equivPlasticStrain
            A sequence of Floats specifying the initial equivalent Plastic strain.
        backStress
            A sequence of sequences of Floats specifying the initial backstress tensor for kinematic
            hardening models. The default value is an empty sequence.
        sectPtNum
            A sequence of Ints specifying section point numbers. This argument is valid only when
            **definition**=SECTION_PTS.
        definition
            A SymbolicConstant specifying different types of kinematic hardening. Possible values
            are KINEMATIC_HARDENING, CRUSHABLE_FOAM, REBAR, SECTION_PTS, and USER_DEFINED. The
            default value is KINEMATIC_HARDENING.
        rebarLayerNames
            A sequence of Strings specifying rebar layer names. This argument is valid only when
            **definition**=REBAR.
        distributionType
            A SymbolicConstant specifying whether the load is uniform. Possible values are MAGNITUDE
            and ANALYTICAL_FIELD. The default value is MAGNITUDE.

        Returns
        -------
            A KinematicHardening object.
        """
        super().__init__()
        pass

    def setValues(
        self,
        numBackStress: int = 1,
        equivPlasticStrain: tuple = (),
        backStress: tuple = (),
        sectPtNum: tuple = (),
        definition: SymbolicConstant = KINEMATIC_HARDENING,
        rebarLayerNames: tuple = (),
        distributionType: SymbolicConstant = MAGNITUDE,
    ):
        """This method modifies the KinematicHardening object.

        Parameters
        ----------
        numBackStress
            An Int specifying the number of backstresses. The default value is 1.
        equivPlasticStrain
            A sequence of Floats specifying the initial equivalent Plastic strain.
        backStress
            A sequence of sequences of Floats specifying the initial backstress tensor for kinematic
            hardening models. The default value is an empty sequence.
        sectPtNum
            A sequence of Ints specifying section point numbers. This argument is valid only when
            **definition**=SECTION_PTS.
        definition
            A SymbolicConstant specifying different types of kinematic hardening. Possible values
            are KINEMATIC_HARDENING, CRUSHABLE_FOAM, REBAR, SECTION_PTS, and USER_DEFINED. The
            default value is KINEMATIC_HARDENING.
        rebarLayerNames
            A sequence of Strings specifying rebar layer names. This argument is valid only when
            **definition**=REBAR.
        distributionType
            A SymbolicConstant specifying whether the load is uniform. Possible values are MAGNITUDE
            and ANALYTICAL_FIELD. The default value is MAGNITUDE.
        """
        pass
