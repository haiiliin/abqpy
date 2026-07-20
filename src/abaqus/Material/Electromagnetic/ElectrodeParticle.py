from __future__ import annotations

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from .ElectrodeParticleLayer import ElectrodeParticleLayer


@abaqus_class_doc
class ElectrodeParticle:
    """The Electrode Particle object specifies electrode particle material
    properties.

    .. note::
        This object can be accessed by::

            import material
            mdb.models[name].materials[name].electrode.particles

        The corresponding analysis keywords are:

        - ABQ_EChemPET_Electrode_Particles

    .. versionadded:: 2026
        The ``ElectrodeParticle`` class was added.
    """

    layers: dict[str, ElectrodeParticleLayer] = {}

    @abaqus_method_doc
    def __init__(
        self,
        name: str,
        particleOuterRadius: float,
        particleVolumeFraction: float,
        particleIonConcentration: float,
    ):
        """This method creates an Electrode Particle object.

        .. note::
            This function can be accessed by::

                mdb.models[name].materials[name].electrode.Particle

        Parameters
        ----------
        name
            A String specifying the unique name of the microscale particle.
        particleOuterRadius
            A Float specifying the outer radius of the microscale particle.
        particleVolumeFraction
            A Float specifying the ratio of the volume fraction of the particle
            with respect to the solid volume fraction of the electrode.
        particleIonConcentration
            A Float specifying the initial concentration of the lithium in the
            microscale particle.

        Returns
        -------
            An Electrode Particle object.

        Raises
        ------
        RangeError
            If a specified value is outside the valid range.
        """
        super().__init__()

    @abaqus_method_doc
    def setValues(
        self,
        name: str = "",
        particleOuterRadius: float = 0,
        particleVolumeFraction: float = 0,
        particleIonConcentration: float = 0,
    ):
        """This method modifies the Electrode Particle object.

        Parameters
        ----------
        name
            A String specifying the unique name of the microscale particle.
        particleOuterRadius
            A Float specifying the outer radius of the microscale particle.
        particleVolumeFraction
            A Float specifying the ratio of the volume fraction of the particle
            with respect to the solid volume fraction of the electrode.
        particleIonConcentration
            A Float specifying the initial concentration of the lithium in the
            microscale particle.

        Raises
        ------
        RangeError
            If a specified value is outside the valid range.
        """
        ...

    @abaqus_method_doc
    def DefineDetails(
        self,
        subType: str,
        data: tuple,
    ):
        """This method specifies the details of the Electrode Particle object.

        Parameters
        ----------
        subType
            A String specifying the property table or parameter table type that
            describes the behavior of the particle. Possible values are

            - ``ABQ_EChemPET_Electrode_Particle_ButlerVolmer``
            - ``ABQ_EChemPET_Electrode_Particle_ElectrodeDissolution``
            - ``ABQ_EChemPET_Electrode_Particle_PowerLoss``
            - ``ABQ_EChemPET_Electrode_Particle_CurrXchgDens_CrackSEI_Tabular``
            - ``ABQ_EChemPET_Electrode_Particle_CurrXchgDens_ElecDiss_Tabular``
            - ``ABQ_EChemPET_Electrode_Particle_CurrXchgDens_LPL_Tabular``
            - ``ABQ_EChemPET_Electrode_Particle_CurrXchgDens_SEI_Tabular``
            - ``ABQ_EChemPET_Electrode_Particle_CurrXchgDens_Tabular``
            - ``ABQ_EChemPET_Electrode_Particle_dUdTEntropy_Tabular``
            - ``ABQ_EChemPET_Electrode_Particle_SEI_CrackFunction_Tabular``
            - ``ABQ_EChemPET_Electrode_Particle_SEI_OCPTabular``
            - ``ABQ_EChemPET_Electrode_Particle_ElecDiss_OCPTabular``
            - ``ABQ_EChemPET_Electrode_Particle_SEI_DiffTabular``
            - ``ABQ_EChemPET_Electrode_Particle_SEI_ElecCondTabular``
            - ``ABQ_EChemPET_Electrode_Particle_SEI_IonCondTabular``
            - ``ABQ_EChemPET_Electrode_Particle_SEI``
            - ``ABQ_EChemPET_Electrode_PowerLoss`` and
            - ``ABQ_EChemPET_Electrode_Particle_LPL``.
        data
            An array of properties of the specified material definition type.

        Raises
        ------
        RangeError
            If a specified value is outside the valid range.
        """
        ...

    @abaqus_method_doc
    def EditDetails(
        self,
        subType: str,
        data: tuple,
    ):
        """This method specifies the details of the Electrode Particle object.

        Parameters
        ----------
        subType
            A String specifying the property table or parameter table type that
            describes the behavior of the particle. Possible values are

            - ``ABQ_EChemPET_Electrode_Particle_ButlerVolmer``
            - ``ABQ_EChemPET_Electrode_Particle_ElectrodeDissolution``
            - ``ABQ_EChemPET_Electrode_Particle_PowerLoss``
            - ``ABQ_EChemPET_Electrode_Particle_CurrXchgDens_CrackSEI_Tabular``
            - ``ABQ_EChemPET_Electrode_Particle_CurrXchgDens_ElecDiss_Tabular``
            - ``ABQ_EChemPET_Electrode_Particle_CurrXchgDens_LPL_Tabular``
            - ``ABQ_EChemPET_Electrode_Particle_CurrXchgDens_SEI_Tabular``
            - ``ABQ_EChemPET_Electrode_Particle_CurrXchgDens_Tabular``
            - ``ABQ_EChemPET_Electrode_Particle_dUdTEntropy_Tabular``
            - ``ABQ_EChemPET_Electrode_Particle_SEI_CrackFunction_Tabular``
            - ``ABQ_EChemPET_Electrode_Particle_SEI_OCPTabular``
            - ``ABQ_EChemPET_Electrode_Particle_ElecDiss_OCPTabular``
            - ``ABQ_EChemPET_Electrode_Particle_SEI_DiffTabular``
            - ``ABQ_EChemPET_Electrode_Particle_SEI_ElecCondTabular``
            - ``ABQ_EChemPET_Electrode_Particle_SEI_IonCondTabular``
            - ``ABQ_EChemPET_Electrode_Particle_SEI``
            - ``ABQ_EChemPET_Electrode_PowerLoss`` and
            - ``ABQ_EChemPET_Electrode_Particle_LPL``.
        data
            An array of properties of the specified material definition type.

        Raises
        ------
        RangeError
            If a specified value is outside the valid range.
        """
        ...

    @abaqus_method_doc
    def Layer(
        self,
        name: str = "",
        weightFraction: float = 0,
    ):
        """This method creates a Layer object.

        .. note::
            This function can be accessed by::

                mdb.models[name].materials[name].electrode.particles[name].Layer

        Parameters
        ----------
        name
            A String specifying the unique name of the particle layer.
        weightFraction
            A Float specifying the weight fraction of the layer.

        Returns
        -------
            An Electrode Particle Layer object.

        Raises
        ------
        RangeError
            If a specified value is outside the valid range.
        """
        self.layers[name] = ElectrodeParticleLayer(
            name=name,
            weightFraction=weightFraction,
        )
