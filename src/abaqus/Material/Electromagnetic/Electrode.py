from __future__ import annotations

from typing_extensions import Literal

from abaqusConstants import ANODE
from abaqusConstants import abaqusConstants as C
from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from .ElectrodeParticle import ElectrodeParticle


@abaqus_class_doc
class Electrode:
    """The Electrode object specifies electrode material properties.

    .. note::
        This object can be accessed by::

            import material
            mdb.models[name].materials[name].electrode

        The corresponding analysis keywords are:

        - ABQ_EChemPET_Electrode_Definition

    .. versionadded:: 2026
        The ``Electrode`` class was added.
    """

    particles: dict[str, ElectrodeParticle] = {}

    @abaqus_method_doc
    def __init__(
        self,
        type: Literal[C.ANODE, C.CATHODE, C.SEPARATOR] = ANODE,
        solidPhaseVolFraction: float = 0,
        liqPhaseVolFraction: float = 0,
        binderVolFraction: float = 0,
        inactiveSolidPhaseVolFraction: float = 0,
        utilizationFraction: float = 0,
        bruggemanZ: float = 0,
        bruggemanX: float = 0,
        bruggemanY: float = 0,
        convection: float = 0,
    ):
        """This method creates an Electrode object.

        .. note::
            This function can be accessed by::

                mdb.models[name].materials[name].Electrode

        Parameters
        ----------
        type
            A SymbolicConstant specifying the type of electrode. Possible
            values are ``ANODE``, ``CATHODE``, and ``SEPERATOR``.
        solidPhaseVolFraction
            A Float specifying the volume fraction of the solid phase in the
            electrode. The default value is 0.
        liqPhaseVolFraction
            A Float specifying the volume fraction of the liquid phase or
            electrolyte in the electrode. The default value is 0.
        binderVolFraction
            A Float specifying the volume fraction of the binder material in
            the electrode. The default value is 0.
        inactiveSolidPhaseVolFraction
            A Float specifying the volume fraction of the inactive solid phase
            in the electrode. The default value is 0.
        utilizationFraction
            A Float specifying the fraction of utilization of the cathode and
            anode regions. The default value is 0.
        bruggemanZ
            A Float specifying the Bruggeman exponent in the thickness
            direction. The default value is 0.
        bruggemanX
            A Float specifying the Bruggeman exponent in the manufacturing
            direction. The default value is 0.
        bruggemanY
            A Float specifying the Bruggeman exponent in the transverse
            direction. The default value is 0.
        convection
            A Float specifying the convection effects of the electrolyte due
            to swelling in the electrode. The default value is 0.

        Returns
        -------
            An Electrode object.

        Raises
        ------
        RangeError
            If a specified value is outside the valid range.
        """
        super().__init__()

    @abaqus_method_doc
    def setValues(
        self,
        solidPhaseVolFraction: float = 0,
        liqPhaseVolFraction: float = 0,
        binderVolFraction: float = 0,
        inactiveSolidPhaseVolFraction: float = 0,
        utilizationFraction: float = 0,
        bruggemanZ: float = 0,
        bruggemanX: float = 0,
        bruggemanY: float = 0,
        convection: float = 0,
    ):
        """This method modifies the Electrode object.

        Parameters
        ----------
        solidPhaseVolFraction
            A Float specifying the volume fraction of the solid phase in the
            electrode. The default value is 0.
        liqPhaseVolFraction
            A Float specifying the volume fraction of the liquid phase or
            electrolyte in the electrode. The default value is 0.
        binderVolFraction
            A Float specifying the volume fraction of the binder material in
            the electrode. The default value is 0.
        inactiveSolidPhaseVolFraction
            A Float specifying the volume fraction of the inactive solid phase
            in the electrode. The default value is 0.
        utilizationFraction
            A Float specifying the fraction of utilization of the cathode and
            anode regions. The default value is 0.
        bruggemanZ
            A Float specifying the Bruggeman exponent in the thickness
            direction. The default value is 0.
        bruggemanX
            A Float specifying the Bruggeman exponent in the manufacturing
            direction. The default value is 0.
        bruggemanY
            A Float specifying the Bruggeman exponent in the transverse
            direction. The default value is 0.
        convection
            A Float specifying the convection effects of the electrolyte due
            to swelling in the electrode. The default value is 0.

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
        """This method specifies the details of the Electrode object.

        Parameters
        ----------
        subType
            A String specifying the property or parameter table type that
            describes the behavior of the electrode. Possible values are
            ``ABQ_EChemPET_Arrhenius``,
            ``ABQ_EChemPET_CubicSplineC2``,
            ``ABQ_EChemPET_Electrode_Swelling``,
            ``ABQ_EChemPET_Electrode_ElecCond_Tabular``, and
            ``ABQ_EChemPET_LogScale_Tabular``.
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
        """This method modifies the details of the Electrode object.

        Parameters
        ----------
        subType
            A String specifying the property or parameter table type that
            describes the behavior of the electrode. Possible values are
            ``ABQ_EChemPET_Arrhenius``,
            ``ABQ_EChemPET_CubicSplineC2``,
            ``ABQ_EChemPET_Electrode_Swelling``,
            ``ABQ_EChemPET_Electrode_ElecCond_Tabular``, and
            ``ABQ_EChemPET_LogScale_Tabular``.
        data
            An array of properties of the specified material definition type.

        Raises
        ------
        RangeError
            If a specified value is outside the valid range.
        """
        ...

    @abaqus_method_doc
    def Particle(
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
        self.particles[name] = ElectrodeParticle(
            name=name,
            particleOuterRadius=particleOuterRadius,
            particleVolumeFraction=particleVolumeFraction,
            particleIonConcentration=particleIonConcentration,
        )
