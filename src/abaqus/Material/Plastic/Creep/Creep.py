from typing_extensions import Literal

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from ....UtilityAndView.abaqusConstants import OFF, STRAIN, TOTAL, Boolean
from ....UtilityAndView.abaqusConstants import abaqusConstants as C
from ..Metal.ORNL.Ornl import Ornl
from ..Potential import Potential


@abaqus_class_doc
class Creep:
    r"""The Creep object defines a creep law.

    .. note::
        This object can be accessed by::

            import material
            mdb.models[name].materials[name].creep
            import odbMaterial
            session.odbs[name].materials[name].creep

        The table data for this object are:

        - If **law** = STRAIN or **law** = TIME, the table data specify the following:

            - :math:`A`.
            - :math:`n`.
            - :math:`m`.
            - Temperature, if the data depend on temperature.
            - Value of the first field variable, if the data depend on field variables.
            - Value of the second field variable.
            - Etc.
        - If **law** = HYPERBOLIC_SINE, the table data specify the following:

            - :math:`A`.
            - :math:`B`.
            - :math:`n`.
            - :math:`\triangle H`, if the data depend on temperature.
            - :math:`R`
            - Value of the first field variable, if the data depend on field variables.
            - Value of the second field variable.
            - Etc.

        The corresponding analysis keywords are:

        - CREEP
    """

    #: An Ornl object.
    ornl: Ornl = Ornl()

    #: A Potential object.
    potential: Potential = Potential(((),))

    @abaqus_method_doc
    def __init__(
        self,
        table: tuple,
        law: Literal[C.HYPERBOLIC_SINE, C.TIME, C.POWER_LAW, C.USER, C.STRAIN] = STRAIN,
        temperatureDependency: Boolean = OFF,
        dependencies: int = 0,
        time: Literal[C.TOTAL, C.CREEP] = TOTAL,
    ):
        """This method creates a Creep object.

        .. note::
            This function can be accessed by::

                mdb.models[name].materials[name].Creep
                session.odbs[name].materials[name].Creep

        Parameters
        ----------
        table
            A sequence of sequences of Floats specifying the items described below.
        law
            A SymbolicConstant specifying the strain-hardening law. Possible values are STRAIN,
            TIME, HYPERBOLIC_SINE and USER.
        temperatureDependency
            A Boolean specifying whether the data depend on temperature. The default value is OFF.
        dependencies
            An Int specifying the number of field variable dependencies. The default value is 0.
        time
            A SymbolicConstant specifying the time interval for relevant laws. Possible values are
            CREEP and TOTAL. The default value is TOTAL.

        Returns
        -------
        Creep
            A Creep object.

        Raises
        ------
        RangeError
        """
        ...

    @abaqus_method_doc
    def setValues(self, *args, **kwargs):
        """This method modifies the Creep object.

        Raises
        ------
        RangeError
        """
        ...
