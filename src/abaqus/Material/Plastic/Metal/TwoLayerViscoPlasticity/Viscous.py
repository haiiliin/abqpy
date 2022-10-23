from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from typing_extensions import Literal

from ...Potential import Potential
from .....UtilityAndView.abaqusConstants import Boolean, OFF, STRAIN, TOTAL
from .....UtilityAndView.abaqusConstants import abaqusConstants as C


@abaqus_class_doc
class Viscous:
    r"""The Viscous object specifies the viscous properties for a two-layer viscoplastic
    material model.

    .. note:: 
        This object can be accessed by::

            import material
            mdb.models[name].materials[name].viscous
            import odbMaterial
            session.odbs[name].materials[name].viscous

        The table data for this object are:

        - If **law** = STRAIN or **law** = TIME, the table data specify the following:
        
            - :math:`A`.
            - :math:`n`.
            - :math:`m`.
            - :math:`f`.
            - Temperature, if the data depend on temperature.
            - Value of the first field variable, if the data depend on field variables.
            - Value of the second field variable.
            - Etc.
        - If **law** = USER, the table data specify the following:
        
            - :math:`f`.
            - Temperature, if the data depend on temperature.
            - Value of the first field variable, if the data depend on field variables.
            - Value of the second field variable.
            - Etc.

        The corresponding analysis keywords are:

        - VISCOUS
    """

    #: A :py:class:`~abaqus.Material.Plastic.Potential.Potential` object.
    potential: Potential = Potential(((),))

    @abaqus_method_doc
    def __init__(
        self,
        table: tuple,
        law: Literal[C.DARVEAUX, C.ANAND, C.TIME, C.POWER_LAW, C.USER, C.STRAIN, C.TIME_POWER_LAW, C.DOUBLE_POWER] = STRAIN,
        temperatureDependency: Boolean = OFF,
        dependencies: int = 0,
        time: Literal[C.TOTAL, C.CREEP] = TOTAL,
    ):
        """This method creates a Viscous object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].materials[name].Viscous
                session.odbs[name].materials[name].Viscous

        Parameters
        ----------
        table
            A sequence of sequences of Floats specifying the items described below.
        law
            A SymbolicConstant specifying the creep law. Possible values are STRAIN, TIME and USER.
        temperatureDependency
            A Boolean specifying whether the data depend on temperature. The default value is OFF.
        dependencies
            An Int specifying the number of field variable dependencies. The default value is 0.
        time
            A SymbolicConstant specifying the time interval for relevant laws. Possible values are
            CREEP and TOTAL. The default value is TOTAL.

        Returns
        -------
        Viscous
            A :py:class:`~abaqus.Material.Plastic.Metal.TwoLayerViscoPlasticity.Viscous.Viscous` object.
        """
        ...

    @abaqus_method_doc
    def setValues(self, *args, **kwargs):
        """This method modifies the Viscous object."""
        ...
