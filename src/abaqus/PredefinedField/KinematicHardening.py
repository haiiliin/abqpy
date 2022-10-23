from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from typing_extensions import Literal

from .PredefinedField import PredefinedField
from ..Region.Region import Region
from ..UtilityAndView.abaqusConstants import KINEMATIC_HARDENING, MAGNITUDE, SymbolicConstant
from ..UtilityAndView.abaqusConstants import abaqusConstants as C


@abaqus_class_doc
class KinematicHardening(PredefinedField):
    """The KinematicHardening object stores the data for initial equivalent Plastic strains
    and, if relevant, the initial backstress tensor.
    The KinematicHardening object is derived from the PredefinedField object.

    .. note::
        This object can be accessed by::

            import load
            mdb.models[name].predefinedFields[name]

        The corresponding analysis keywords are:

        - INITIAL CONDITIONS
    """

    #: A String specifying the name of the AnalyticalField object associated with this
    #: predefined field. The **field** argument applies only when
    #: **distributionType** = ANALYTICAL_FIELD. The default value is an empty string.
    field: str = ""

    #: A String specifying the repository key.
    name: str

    #: A :py:class:`~abaqus.Region.Region.Region` object specifying the region to which the predefined field is applied.
    region: Region

    #: An Int specifying the number of backstresses. The default value is 1.
    numBackStress: int = 1

    #: A sequence of Floats specifying the initial equivalent Plastic strain.
    equivPlasticStrain: tuple = ()

    #: A sequence of sequences of Floats specifying the initial backstress tensor for kinematic
    #: hardening models. The default value is an empty sequence.
    backStress: tuple = ()

    #: A sequence of Ints specifying section point numbers. This argument is valid only when
    #: **definition** = SECTION_PTS.
    sectPtNum: tuple = ()

    #: A SymbolicConstant specifying different types of kinematic hardening. Possible values
    #: are KINEMATIC_HARDENING, CRUSHABLE_FOAM, REBAR, SECTION_PTS, and USER_DEFINED. The
    #: default value is KINEMATIC_HARDENING.
    definition: SymbolicConstant = KINEMATIC_HARDENING

    #: A sequence of Strings specifying rebar layer names. This argument is valid only when
    #: **definition** = REBAR.
    rebarLayerNames: tuple = ()

    #: A SymbolicConstant specifying whether the load is uniform. Possible values are MAGNITUDE
    #: and ANALYTICAL_FIELD. The default value is MAGNITUDE.
    distributionType: SymbolicConstant = MAGNITUDE

    @abaqus_method_doc
    def __init__(
        self,
        name: str,
        region: Region,
        numBackStress: int = 1,
        equivPlasticStrain: tuple = (),
        backStress: tuple = (),
        sectPtNum: tuple = (),
        definition: Literal[
            C.CRUSHABLE_FOAM, C.KINEMATIC_HARDENING, C.REBAR, C.USER_DEFINED, C.SECTION_PTS
        ] = KINEMATIC_HARDENING,
        rebarLayerNames: tuple = (),
        distributionType: Literal[C.MAGNITUDE, C.ANALYTICAL_FIELD] = MAGNITUDE,
    ):
        """This method creates a KinematicHardening object.

        .. note::
            This function can be accessed by::

                mdb.models[name].KinematicHardening

        Parameters
        ----------
        name
            A String specifying the repository key.
        region
            A :py:class:`~abaqus.Region.Region.Region` object specifying the region to which the predefined field is applied.
        numBackStress
            An Int specifying the number of backstresses. The default value is 1.
        equivPlasticStrain
            A sequence of Floats specifying the initial equivalent Plastic strain.
        backStress
            A sequence of sequences of Floats specifying the initial backstress tensor for kinematic
            hardening models. The default value is an empty sequence.
        sectPtNum
            A sequence of Ints specifying section point numbers. This argument is valid only when
            **definition** = SECTION_PTS.
        definition
            A SymbolicConstant specifying different types of kinematic hardening. Possible values
            are KINEMATIC_HARDENING, CRUSHABLE_FOAM, REBAR, SECTION_PTS, and USER_DEFINED. The
            default value is KINEMATIC_HARDENING.
        rebarLayerNames
            A sequence of Strings specifying rebar layer names. This argument is valid only when
            **definition** = REBAR.
        distributionType
            A SymbolicConstant specifying whether the load is uniform. Possible values are MAGNITUDE
            and ANALYTICAL_FIELD. The default value is MAGNITUDE.

        Returns
        -------
        KinematicHardening
            A :py:class:`~abaqus.PredefinedField.KinematicHardening.KinematicHardening` object.
        """
        super().__init__()

    @abaqus_method_doc
    def setValues(
        self,
        numBackStress: int = 1,
        equivPlasticStrain: tuple = (),
        backStress: tuple = (),
        sectPtNum: tuple = (),
        definition: Literal[
            C.CRUSHABLE_FOAM, C.KINEMATIC_HARDENING, C.REBAR, C.USER_DEFINED, C.SECTION_PTS
        ] = KINEMATIC_HARDENING,
        rebarLayerNames: tuple = (),
        distributionType: Literal[C.MAGNITUDE, C.ANALYTICAL_FIELD] = MAGNITUDE,
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
            **definition** = SECTION_PTS.
        definition
            A SymbolicConstant specifying different types of kinematic hardening. Possible values
            are KINEMATIC_HARDENING, CRUSHABLE_FOAM, REBAR, SECTION_PTS, and USER_DEFINED. The
            default value is KINEMATIC_HARDENING.
        rebarLayerNames
            A sequence of Strings specifying rebar layer names. This argument is valid only when
            **definition** = REBAR.
        distributionType
            A SymbolicConstant specifying whether the load is uniform. Possible values are MAGNITUDE
            and ANALYTICAL_FIELD. The default value is MAGNITUDE.
        """
        ...
