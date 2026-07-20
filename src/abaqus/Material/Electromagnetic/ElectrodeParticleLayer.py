from __future__ import annotations

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc


@abaqus_class_doc
class ElectrodeParticleLayer:
    """The Electrode Particle Layer object specifies electrode particle layer
    material properties.

    .. note::
        This object can be accessed by::

            import material
            mdb.models[name].materials[name].electrode.particles[name].layers

        The corresponding analysis keywords are:

        - ABQ_EChemPET_Electrode_Particle_Layers

    .. versionadded:: 2026
        The ``ElectrodeParticleLayer`` class was added.
    """

    @abaqus_method_doc
    def __init__(
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
        super().__init__()

    @abaqus_method_doc
    def setValues(
        self,
        name: str = "",
        weightFraction: float = 0,
    ):
        """This method modifies the Electrode Particle Layer object.

        Parameters
        ----------
        name
            A String specifying the unique name of the particle layer.
        weightFraction
            A Float specifying the weight fraction of the layer.

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
        """This method specifies the details of the Electrode Particle Layer
        object.

        Parameters
        ----------
        subType
            A String specifying the property table or parameter table type that
            describes the behavior of the layer. Possible values are

            - ``ABQ_EChemPET_Electrode_Particle_Layer_Diffusion``
            - ``ABQ_EChemPET_Electrode_Particle_Layer_Discretization``
            - ``ABQ_EChemPET_Electrode_Particle_Layer_DsTabular``
            - ``ABQ_EChemPET_Electrode_Particle_Layer_OCPTabular``
            - ``ABQ_EChemPET_Electrode_Particle_Layer_SwellingTabular``
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
        """This method modifies the details of the Electrode Particle Layer
        object.

        Parameters
        ----------
        subType
            A String specifying the property table or parameter table type that
            describes the behavior of the layer. Possible values are

            - ``ABQ_EChemPET_Electrode_Particle_Layer_Diffusion``
            - ``ABQ_EChemPET_Electrode_Particle_Layer_Discretization``
            - ``ABQ_EChemPET_Electrode_Particle_Layer_DsTabular``
            - ``ABQ_EChemPET_Electrode_Particle_Layer_OCPTabular``
            - ``ABQ_EChemPET_Electrode_Particle_Layer_SwellingTabular``
        data
            An array of properties of the specified material definition type.

        Raises
        ------
        RangeError
            If a specified value is outside the valid range.
        """
        ...
