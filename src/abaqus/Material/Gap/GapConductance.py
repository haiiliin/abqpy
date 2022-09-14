from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from ...UtilityAndView.abaqusConstants import *


@abaqus_class_doc
class GapConductance:
    """The GapConductance object specifies conductive heat transfer between closely adjacent
    (or contacting) surfaces.

    .. note::
        This object can be accessed by::
        
            import material
            mdb.models[name].materials[name].gapConductance
            import odbMaterial
            session.odbs[name].materials[name].gapConductance

        The table data for this object are:

        - Gap Conductance or Cohesive Separation.
        - Gap Clearance, Gap Pressure (if optional parameter pressureDependency is used), or Closure, :math:`c`
          (for coupled temperature-displacement gasket elements).
        - Average Temperature if the data depend on temperature.
        - Mass Flow Rate per unit area if the data depend on the average mass flow rate.
        - Value of the first field variable if the data depend on field variables.
        - Value of the second field variable.
        - Etc.

        The corresponding analysis keywords are:

        - GAP CONDUCTANCE

    .. versionadded:: 2021
        The `GapConductance` class was added.
    """

    @abaqus_method_doc
    def __init__(
        self,
        pressureDependency: Boolean = OFF,
        dependencies: int = 0,
        table: tuple = (),
    ):
        """This method creates a GapConductance object.

        .. note::
            This function can be accessed by::

                mdb.models[name].materials[name].GapConductance
                session.odbs[name].materials[name].GapConductance

        Parameters
        ----------
        pressureDependency
            A Boolean specifying whether the data depend on pressure. The default value is OFF.
        dependencies
            An Int specifying the number of field variable dependencies. The default value is 0.
        table
            A sequence of sequences of Floats specifying the items described below.

        Returns
        -------
            A GapConductance object.

        Raises
        ------
        """
        ...

    @abaqus_method_doc
    def setValues(self):
        """This method modifies the GapConductance object.
        """
        ...
