from abaqusConstants import *


class GapConductance:
    """The GapConductance object specifies conductive heat transfer between closely adjacent
    (or contacting) surfaces.

    .. note::
    This object can be accessed by:

    .. code-block:: python

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

    """

    def __init__(
        self,
        pressureDependency: Boolean = OFF,
        dependencies: int = 0,
        table: tuple = (),
    ):
        """This method creates a GapConductance object.

        Notes
        -----
            This function can be accessed by:

            .. code-block:: python

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
        pass

    def setValues(self):
        """This method modifies the GapConductance object.

        Returns
        -------

        Raises
        ------
        """
        pass
