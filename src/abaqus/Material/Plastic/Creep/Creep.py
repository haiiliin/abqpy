from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from typing_extensions import Literal

from ..Metal.ORNL.Ornl import Ornl
from ..Potential import Potential
from ....UtilityAndView.abaqusConstants import Boolean, OFF, STRAIN, TOTAL
from ....UtilityAndView.abaqusConstants import abaqusConstants as C


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
        - If **law** = ANAND, the table data specify the following:
        
            - :math:`s_{1}`.
            - :math:`\frac{Q}{R}`.
            - :math:`A`.
            - :math:`\xi`.
            - :math:`m`.
            - :math:`A_{0}`.
            - :math:`\widehat{S}`
            - :math:`n`.
            - :math:`a`.
            - :math:`S_{2}`.
            - :math:`S_{3}`.
            - :math:`A_{1}`.
            - :math:`A_{2}`.
            - :math:`A_{3}`.
            - :math:`A_{4}`.
        - If **law** = DARVEAUX, the table data specify the following:
        
            - :math:`C_{s s}`.
            - :math:`\frac{Q}{R}`.
            - :math:`\alpha`.
            - :math:`n`.
            - :math:`\epsilon_{T}`.
            - :math:`B`.
        - If **law** = DOUBLE_POWER, the table data specify the following:
        
            - :math:`A_{1}`.
            - :math:`B_{1}`.
            - :math:`C_{1}`.
            - :math:`A_{2}`.
            - :math:`B_{2}`.
            - :math:`C_{2}`.
            - :math:`\sigma_{0}`.
        - If **law** = POWER_LAW or **law** = TIME_POWER_LAW, the table data specify the following:
        
            - :math:`q_{0}`
            - :math:`n`.
            - :math:`m`.
            - :math:`\varepsilon_{0}^{\bullet}`.
            - Temperature, if the data depend on temperature.
            - Value of the first field variable, if the data depend on field variables.
            - Value of the second field variable.
            - Etc.

        The corresponding analysis keywords are:

        - CREEP
    """

    #: An :py:class:`~abaqus.Material.Plastic.Metal.ORNL.Ornl.Ornl` object.
    ornl: Ornl = Ornl()

    #: A :py:class:`~abaqus.Material.Plastic.Potential.Potential` object.
    potential: Potential = Potential(((),))

    @abaqus_method_doc
    def __init__(
        self,
        table: tuple,
        law: Literal[C.DARVEAUX, C.HYPERBOLIC_SINE, C.ANAND, C.TIME, C.POWER_LAW, C.USER, C.STRAIN, C.TIME_POWER_LAW, C.DOUBLE_POWER] = STRAIN,
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
            TIME, HYPERBOLIC_SINE, USER, ANAND, DARVEAUX, DOUBLE_POWER, POWER_LAW, and
            TIME_POWER_LAW. The default value is STRAIN.
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
            A :py:class:`~abaqus.Material.Plastic.Creep.Creep.Creep` object.

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
