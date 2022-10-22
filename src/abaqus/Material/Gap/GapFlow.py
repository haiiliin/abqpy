from typing import Optional

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from ...UtilityAndView.abaqusConstants import Boolean, NEWTONIAN, OFF, SymbolicConstant


@abaqus_class_doc
class GapFlow:
    """The GapFlow object specifies tangential flow constitutive parameters for pore pressure
    cohesive elements.

    .. note:: 
        This object can be accessed by::

            import material
            mdb.models[name].materials[name].gapFlow
            import odbMaterial
            session.odbs[name].materials[name].gapFlow

        The table data for this object are:

        - If **type** = NEWTONIAN the table data specify the following:
        
            - Pore viscosity.
            - Temperature, if the data depend on temperature.
            - Value of the first field variable, if the data depend on field variables.
            - Value of the second field variable.
            - Etc.
        - If **type** = POWER_LAW the table data specify the following:
        
            - Consistency.
            - Exponent.
            - Temperature, if the data depend on temperature.
            - Value of the first field variable, if the data depend on field variables.
            - Value of the second field variable.
            - Etc.

        The corresponding analysis keywords are:

        - GAP FLOW
    """

    @abaqus_method_doc
    def __init__(
        self,
        table: tuple,
        kmax: Optional[float] = None,
        temperatureDependency: Boolean = OFF,
        dependencies: int = 0,
        type: SymbolicConstant = NEWTONIAN,
    ):
        """This method creates a GapFlow object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].materials[name].GapFlow
                session.odbs[name].materials[name].GapFlow

        Parameters
        ----------
        table
            A sequence of sequences of Floats specifying the items described below.
        kmax
            None or a Float specifying the maximum permeability value that should be used. If
            **kmax** = None, Abaqus assumes that the permeability is not bounded. This value is
            meaningful only when **type** = NEWTONIAN. The default value is None.
        temperatureDependency
            A Boolean specifying whether the data depend on temperature. The default value is OFF.
        dependencies
            An Int specifying the number of field variable dependencies. The default value is 0.
        type
            A SymbolicConstant specifying the type of gap flow. Possible values are NEWTONIAN and
            POWER_LAW. The default value is NEWTONIAN.

        Returns
        -------
        GapFlow
            A :py:class:`~abaqus.Material.Gap.GapFlow.GapFlow` object.
        """
        ...

    @abaqus_method_doc
    def setValues(self, *args, **kwargs):
        """This method modifies the GapFlow object."""
        ...
