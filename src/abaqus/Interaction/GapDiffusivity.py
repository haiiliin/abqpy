from __future__ import annotations

from typing_extensions import Literal

from abaqusConstants import abaqusConstants as C
from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from .Interaction import Interaction


@abaqus_class_doc
class GapDiffusivity(Interaction):
    """The GapDiffusivity object specifies gap diffusivity for a contact
    interaction property.

    .. note::
        This object can be accessed by::

            import interaction
            mdb.models[name].interactionProperties[name].diffusivity

        The corresponding analysis keywords are:

        - GAP DIFFUSIVITY

    .. versionadded:: 2026
        The ``GapDiffusivity`` class was added.
    """

    @abaqus_method_doc
    def __init__(
        self,
        type: Literal[C.ION_CONCENTRATION, C.SPECIES_CONCENTRATION],
        cutoffFlowAcrossDist: float | None = None,
        cutoffGapFillDist: float | None = None,
        dependencies: int = 0,
        concentrationDepTable: tuple = (),
    ):
        """This method creates a GapDiffusivity object.

        .. note::
            This function can be accessed by::

                mdb.models[name].interactionProperties[name].Diffusivity

        Parameters
        ----------
        type
            A SymbolicConstant specifying how the contact diffusivity is
            defined. Possible values are ``ION_CONCENTRATION`` and
            ``SPECIES_CONCENTRATION``.
        cutoffFlowAcrossDist
            A Float specifying a cutoff clearance distance above which no ion
            or species diffusion occurs across a contact interface.
        cutoffGapFillDist
            A Float specifying a cutoff clearance distance above which no ion
            or species diffusion occurs into or out of a contact interface due
            to changes in the clearance distance.
        dependencies
            An Int specifying the number of field variables to use with
            clearance dependency. The default value is 0.
        concentrationDepTable
            A sequence of sequences of Floats specifying concentration
            dependency data.

            For ``type=ION_CONCENTRATION``, each sequence contains the
            following values:

            - Contact diffusivity.
            - Contact pressure.
            - Average ion concentration.
            - Average temperature.
            - Values of the field variables, if applicable.

            For ``type=SPECIES_CONCENTRATION``, each sequence contains the
            following values:

            - Contact diffusivity.
            - Contact pressure.
            - Average species concentration.
            - Average temperature.
            - Values of the field variables, if applicable.

        Returns
        -------
            A GapDiffusivity object.
        """
        super().__init__()

    @abaqus_method_doc
    def setValues(
        self,
        type: Literal[C.ION_CONCENTRATION, C.SPECIES_CONCENTRATION],
        cutoffFlowAcrossDist: float | None = None,
        cutoffGapFillDist: float | None = None,
        dependencies: int = 0,
        concentrationDepTable: tuple = (),
    ):
        """This method modifies the GapDiffusivity object.

        Parameters
        ----------
        type
            A SymbolicConstant specifying how the contact diffusivity is
            defined. Possible values are ``ION_CONCENTRATION`` and
            ``SPECIES_CONCENTRATION``.
        cutoffFlowAcrossDist
            A Float specifying a cutoff clearance distance above which no ion
            or species diffusion occurs across a contact interface.
        cutoffGapFillDist
            A Float specifying a cutoff clearance distance above which no ion
            or species diffusion occurs into or out of a contact interface due
            to changes in the clearance distance.
        dependencies
            An Int specifying the number of field variables to use with
            clearance dependency. The default value is 0.
        concentrationDepTable
            A sequence of sequences of Floats specifying concentration
            dependency data.

            For ``type=ION_CONCENTRATION``, each sequence contains contact
            diffusivity, contact pressure, average ion concentration, average
            temperature, and field-variable values when applicable.

            For ``type=SPECIES_CONCENTRATION``, each sequence contains contact
            diffusivity, contact pressure, average species concentration,
            average temperature, and field-variable values when applicable.

        Returns
        -------
            None.
        """
        ...
