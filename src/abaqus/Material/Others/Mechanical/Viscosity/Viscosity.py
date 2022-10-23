from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from typing_extensions import Literal

from .Trs import Trs
from .....UtilityAndView.abaqusConstants import Boolean, NEWTONIAN, OFF
from .....UtilityAndView.abaqusConstants import abaqusConstants as C


@abaqus_class_doc
class Viscosity:
    """The Viscosity object specifies mechanical viscosity.

    .. note::
        This object can be accessed by::

            import material
            mdb.models[name].materials[name].viscosity
            import odbMaterial
            session.odbs[name].materials[name].viscosity

        The table data for this object are:

        - If **type** = NEWTONIAN, the table data specify the following:

        - Viscosity, :math:`k`.
        - Temperature, if the data depend on temperature.
        - Value of the first field variable, if the data depend on field variables.
        - Value of the second field variable.
        - Etc.

        The corresponding analysis keywords are:

        - VISCOSITY
    """

    #: A :py:class:`~abaqus.Material.Others.Mechanical.Viscosity.Trs.Trs` object.
    trs: Trs = Trs()

    @abaqus_method_doc
    def __init__(
        self,
        table: tuple,
        type: Literal[C.NEWTONIAN] = NEWTONIAN,
        temperatureDependency: Boolean = OFF,
        dependencies: int = 0,
    ):
        """This method creates a Viscosity object.

        .. note::
            This function can be accessed by::

                mdb.models[name].materials[name].Viscosity
                session.odbs[name].materials[name].Viscosity

        Parameters
        ----------
        table
            A sequence of sequences of Floats specifying the items described below.
        type
            A SymbolicConstant specifying the type of viscosity. The default value is NEWTONIAN.
        temperatureDependency
            A Boolean specifying whether the data depend on temperature. The default value is OFF.
        dependencies
            An Int specifying the number of field variable dependencies. The default value is 0.

        Returns
        -------
        Viscosity
            A :py:class:`~abaqus.Material.Others.Mechanical.Viscosity.Viscosity.Viscosity` object.

        Raises
        ------
        RangeError
        """
        ...

    @abaqus_method_doc
    def setValues(self, *args, **kwargs):
        """This method modifies the Viscosity object.

        Raises
        ------
        RangeError
        """
        ...
