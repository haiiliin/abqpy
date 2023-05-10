from typing_extensions import Literal

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from ....UtilityAndView.abaqusConstants import WLF
from ....UtilityAndView.abaqusConstants import abaqusConstants as C


@abaqus_class_doc
class Trs:
    r"""The Trs object defines the temperature-time shift for time history viscoelastic analysis.

    .. note::
        This object can be accessed by::

            import material
            mdb.models[name].materials[name].viscoelastic.trs
            mdb.models[name].materials[name].viscosity.trs
            import odbMaterial
            session.odbs[name].materials[name].viscoelastic.trs
            session.odbs[name].materials[name].viscosity.trs

        The table data for this object are:

        - Reference temperature, :math:`\theta_{0}`.
        - Calibration constant, :math:`C_{1}`.
        - Calibration constant, :math:`C_{2}`.

        The corresponding analysis keywords are:

        - TRS
    """

    @abaqus_method_doc
    def __init__(self, definition: Literal[C.USER, C.WLF, C.ARRHENIUS] = WLF, table: tuple = ()):
        """This method creates a Trs object.

        .. note::
            This function can be accessed by::

                mdb.models[name].materials[name].viscoelastic.Trs
                mdb.models[name].materials[name].viscosity.Trs
                session.odbs[name].materials[name].viscoelastic.Trs
                session.odbs[name].materials[name].viscosity.Trs

        Parameters
        ----------
        definition
            A SymbolicConstant specifying the definition of the shift function. Possible values are
            WLF, ARRHENIUS, and USER. The default value is WLF.
        table
            A sequence of sequences of Floats specifying the items described below. The default
            value is an empty sequence.This argument is valid only when **definition** = WLF.

        Returns
        -------
        Trs
            A Trs object.
        """
        ...

    @abaqus_method_doc
    def setValues(self, *args, **kwargs):
        """This method modifies the Trs object."""
        ...
