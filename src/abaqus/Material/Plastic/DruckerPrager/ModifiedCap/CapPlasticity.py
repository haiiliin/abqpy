from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from .....UtilityAndView.abaqusConstants import OFF, Boolean
from .CapCreepCohesion import CapCreepCohesion
from .CapCreepConsolidation import CapCreepConsolidation
from .CapHardening import CapHardening


@abaqus_class_doc
class CapPlasticity:
    r"""The CapPlasticity object specifies the modified Drucker-Prager/Cap plasticity model.

    .. note::
        This object can be accessed by::

            import material
            mdb.models[name].materials[name].capPlasticity
            import odbMaterial
            session.odbs[name].materials[name].capPlasticity

        The table data for this object are:

        - Material cohesion, :math:`d`, in the :math:`p-t` plane (Abaqus/Standard) or in the :math:`p-q`
          plane (Abaqus/Explicit).
        - Material angle of friction, :math:`\beta`, in the :math:`p-t` plane (Abaqus/Standard) or
          in the :math:`p-q` plane (Abaqus/Explicit). Give the value in degrees.
        - Cap eccentricity parameter, :math:`R`. Its value must be greater than zero (typically
          :math:`0.0<R<1.0)`.
        - Initial cap yield surface position, :math:`\left.\varepsilon_{v o l}^{p l}\right|_{0}`
        - Transition surface radius parameter, :math:`\alpha`. The default value is :math:`0.0` (i.e.,
          no transition surface). Abaqus/Standard assumes :math:`K=1.0`.
        - Temperature, if the data depend on temperature.
        - Value of the first field variable, if the data depend on field variables.
        - Value of the second field variable.
        - Etc.

        The corresponding analysis keywords are:

        - CAP PLASTICITY
    """

    #: A CapCreepCohesion object.
    capCreepCohesion: CapCreepCohesion = CapCreepCohesion(((),))

    #: A CapCreepConsolidation object.
    capCreepConsolidation: CapCreepConsolidation = CapCreepConsolidation(((),))

    #: A CapHardening object.
    capHardening: CapHardening = CapHardening(((),))

    @abaqus_method_doc
    def __init__(self, table: tuple, temperatureDependency: Boolean = OFF, dependencies: int = 0):
        """This method creates a CapPlasticity object.

        .. note::
            This function can be accessed by::

                mdb.models[name].materials[name].CapPlasticity
                session.odbs[name].materials[name].CapPlasticity

        Parameters
        ----------
        table
            A sequence of sequences of Floats specifying the items described below.
        temperatureDependency
            A Boolean specifying whether the data depend on temperature. The default value is OFF.
        dependencies
            An Int specifying the number of field variable dependencies. The default value is 0.

        Returns
        -------
        CapPlasticity
            A CapPlasticity object.

        Raises
        ------
        RangeError
        """
        ...

    @abaqus_method_doc
    def setValues(self, *args, **kwargs):
        """This method modifies the CapPlasticity object.

        Raises
        ------
        RangeError
        """
        ...
