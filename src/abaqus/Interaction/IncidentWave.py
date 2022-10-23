from typing import Optional

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from typing_extensions import Literal

from .Interaction import Interaction
from ..Region.Region import Region
from ..UtilityAndView.abaqusConstants import PRESSURE, SymbolicConstant
from ..UtilityAndView.abaqusConstants import abaqusConstants as C


@abaqus_class_doc
class IncidentWave(Interaction):
    """The IncidentWave object defines incident wave interactions for acoustic and coupled
    acoustic-structural analyses.
    The IncidentWave object is derived from the Interaction object.

    .. note::
        This object can be accessed by::

            import interaction
            mdb.models[name].interactions[name]

        The corresponding analysis keywords are:

        - INCIDENT WAVE INTERACTION
    """

    #: A String specifying the repository key.
    name: str

    #: A String specifying the name of the step in which the IncidentWave object is created.
    createStepName: str

    #: A :py:class:`~abaqus.Region.Region.Region` object specifying the incident wave source point.
    sourcePoint: Region

    #: A :py:class:`~abaqus.Region.Region.Region` object specifying the incident wave standoff point.This argument is not valid
    #: when **definition** = CONWEP.
    standoffPoint: Region

    #: A :py:class:`~abaqus.Region.Region.Region` object specifying the surface defining the incident wave interaction. In
    #: problems involving fluid/surface boundaries, both the fluid surface and the solid
    #: surface comprising the boundary must have an incident wave interaction specified.
    surface: Region

    #: A String specifying the IncidentWaveProperty object associated with this interaction.
    interactionProperty: str

    #: A SymbolicConstant specifying the type of incident wave to be defined. The value must be
    #: PRESSURE for linear perturbation steps. An Explicit step is required when the value is
    #: set to CONWEP. Possible values are PRESSURE, ACCELERATION, UNDEX, and CONWEP. The
    #: default value is PRESSURE.
    definition: SymbolicConstant = PRESSURE

    #: A String specifying the name of the Amplitude object that defines the fluid pressure
    #: time history at the standoff point, if **definition** = PRESSURE. If
    #: **definition** = ACCELERATION, then this string specifies the name of the Amplitude object
    #: that defines the fluid particle acceleration time history at the standoff point. This
    #: member can be specified only if **definition** = PRESSURE or ACCELERATION. The default value
    #: is an empty string.
    amplitude: str = ""

    #: A String specifying the name of the Amplitude object that defines the imaginary
    #: component of the fluid pressure time history at the standoff point. This member is
    #: applicable only for linear perturbation steps and if **definition** = PRESSURE. The default
    #: value is an empty string.
    imaginaryAmplitude: str = ""

    #: A sequence of three Floats specifying the X, Y, and Z components of the direction cosine
    #: of the fluid surface normal.This argument is valid only when **definition** = UNDEX.
    surfaceNormal: tuple = ()

    #: None or a Float specifying the initial depth of the UNDEX bubble. The default value is
    #: None.This argument is valid only when **definition** = UNDEX.
    initialDepth: Optional[float] = None

    #: A Float specifying the reference magnitude.This argument is not valid when
    #: **definition** = CONWEP.
    referenceMagnitude: Optional[float] = None

    #: A Float specifying the time of detonation, given in total time.This argument is valid
    #: only when **definition** = CONWEP.
    detonationTime: Optional[float] = None

    #: A Float specifying the magnitude scale factor. The default value is 1.0.This argument is
    #: valid only when **definition** = CONWEP.
    magnitudeFactor: float = 1

    @abaqus_method_doc
    def __init__(
        self,
        name: str,
        createStepName: str,
        sourcePoint: Region,
        standoffPoint: Region,
        surface: Region,
        interactionProperty: str,
        definition: Literal[C.PRESSURE, C.UNDEX, C.CONWEP, C.ACCELERATION] = PRESSURE,
        amplitude: str = "",
        imaginaryAmplitude: str = "",
        surfaceNormal: tuple = (),
        initialDepth: Optional[float] = None,
        referenceMagnitude: Optional[float] = None,
        detonationTime: Optional[float] = None,
        magnitudeFactor: float = 1,
    ):
        """This method creates an IncidentWave object.

        .. note::
            This function can be accessed by::

                mdb.models[name].IncidentWave

        Parameters
        ----------
        name
            A String specifying the repository key.
        createStepName
            A String specifying the name of the step in which the IncidentWave object is created.
        sourcePoint
            A :py:class:`~abaqus.Region.Region.Region` object specifying the incident wave source point.
        standoffPoint
            A :py:class:`~abaqus.Region.Region.Region` object specifying the incident wave standoff point.This argument is not valid
            when **definition** = CONWEP.
        surface
            A :py:class:`~abaqus.Region.Region.Region` object specifying the surface defining the incident wave interaction. In
            problems involving fluid/surface boundaries, both the fluid surface and the solid
            surface comprising the boundary must have an incident wave interaction specified.
        interactionProperty
            A String specifying the IncidentWaveProperty object associated with this interaction.
        definition
            A SymbolicConstant specifying the type of incident wave to be defined. The value must be
            PRESSURE for linear perturbation steps. An Explicit step is required when the value is
            set to CONWEP. Possible values are PRESSURE, ACCELERATION, UNDEX, and CONWEP. The
            default value is PRESSURE.
        amplitude
            A String specifying the name of the Amplitude object that defines the fluid pressure
            time history at the standoff point, if **definition** = PRESSURE. If
            **definition** = ACCELERATION, then this string specifies the name of the Amplitude object
            that defines the fluid particle acceleration time history at the standoff point. This
            member can be specified only if **definition** = PRESSURE or ACCELERATION. The default value
            is an empty string.
        imaginaryAmplitude
            A String specifying the name of the Amplitude object that defines the imaginary
            component of the fluid pressure time history at the standoff point. This member is
            applicable only for linear perturbation steps and if **definition** = PRESSURE. The default
            value is an empty string.
        surfaceNormal
            A sequence of three Floats specifying the X, Y, and Z components of the direction cosine
            of the fluid surface normal.This argument is valid only when **definition** = UNDEX.
        initialDepth
            None or a Float specifying the initial depth of the UNDEX bubble. The default value is
            None.This argument is valid only when **definition** = UNDEX.
        referenceMagnitude
            A Float specifying the reference magnitude.This argument is not valid when
            **definition** = CONWEP.
        detonationTime
            A Float specifying the time of detonation, given in total time.This argument is valid
            only when **definition** = CONWEP.
        magnitudeFactor
            A Float specifying the magnitude scale factor. The default value is 1.0.This argument is
            valid only when **definition** = CONWEP.

        Returns
        -------
        IncidentWave
            An :py:class:`~abaqus.Interaction.IncidentWave.IncidentWave` object.
        """
        super().__init__()

    @abaqus_method_doc
    def setValues(
        self,
        definition: Literal[C.PRESSURE, C.UNDEX, C.CONWEP, C.ACCELERATION] = PRESSURE,
        amplitude: str = "",
        imaginaryAmplitude: str = "",
        surfaceNormal: tuple = (),
        initialDepth: Optional[float] = None,
        referenceMagnitude: Optional[float] = None,
        detonationTime: Optional[float] = None,
        magnitudeFactor: float = 1,
    ):
        """This method modifies the IncidentWave object.

        Parameters
        ----------
        definition
            A SymbolicConstant specifying the type of incident wave to be defined. The value must be
            PRESSURE for linear perturbation steps. An Explicit step is required when the value is
            set to CONWEP. Possible values are PRESSURE, ACCELERATION, UNDEX, and CONWEP. The
            default value is PRESSURE.
        amplitude
            A String specifying the name of the Amplitude object that defines the fluid pressure
            time history at the standoff point, if **definition** = PRESSURE. If
            **definition** = ACCELERATION, then this string specifies the name of the Amplitude object
            that defines the fluid particle acceleration time history at the standoff point. This
            member can be specified only if **definition** = PRESSURE or ACCELERATION. The default value
            is an empty string.
        imaginaryAmplitude
            A String specifying the name of the Amplitude object that defines the imaginary
            component of the fluid pressure time history at the standoff point. This member is
            applicable only for linear perturbation steps and if **definition** = PRESSURE. The default
            value is an empty string.
        surfaceNormal
            A sequence of three Floats specifying the X, Y, and Z components of the direction cosine
            of the fluid surface normal.This argument is valid only when **definition** = UNDEX.
        initialDepth
            None or a Float specifying the initial depth of the UNDEX bubble. The default value is
            None.This argument is valid only when **definition** = UNDEX.
        referenceMagnitude
            A Float specifying the reference magnitude.This argument is not valid when
            **definition** = CONWEP.
        detonationTime
            A Float specifying the time of detonation, given in total time.This argument is valid
            only when **definition** = CONWEP.
        magnitudeFactor
            A Float specifying the magnitude scale factor. The default value is 1.0.This argument is
            valid only when **definition** = CONWEP.
        """
        ...
