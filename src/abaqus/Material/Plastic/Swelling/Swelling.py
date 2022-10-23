from typing_extensions import Literal
from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from ...Ratios import Ratios
from ....UtilityAndView.abaqusConstants import abaqusConstants as C
from ....UtilityAndView.abaqusConstants import Boolean, INPUT, OFF


@abaqus_class_doc
class Swelling:
    """The Swelling object specifies time-dependent volumetric swelling for a material.

    .. note:: 
        This object can be accessed by::

            import material
            mdb.models[name].materials[name].swelling
            import odbMaterial
            session.odbs[name].materials[name].swelling

        The table data for this object are:

        - Volumetric swelling strain rate.
        - Temperature, if the data depend on temperature.
        - Value of the first field variable, if the data depend on field variables.
        - Value of the second field variable.
        - Etc.

        The corresponding analysis keywords are:

        - SWELLING
    """

    #: A :py:class:`~abaqus.Material.Ratios.Ratios` object.
    ratios: Ratios = Ratios(((),))

    @abaqus_method_doc
    def __init__(
        self,
        table: tuple,
        law: Literal[C.INPUT, C.USER] = INPUT,
        temperatureDependency: Boolean = OFF,
        dependencies: int = 0,
    ):
        """This method creates a Swelling object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].materials[name].Swelling
                session.odbs[name].materials[name].Swelling

        Parameters
        ----------
        table
            A sequence of sequences of Floats specifying the items described below.This argument is
            valid only when **law** = INPUT.
        law
            A SymbolicConstant specifying the type of data defining the swelling behavior. Possible
            values are INPUT and USER. The default value is INPUT.
        temperatureDependency
            A Boolean specifying whether the data depend on temperature. The default value is OFF.
        dependencies
            An Int specifying the number of field variable dependencies. The default value is 0.

        Returns
        -------
        Swelling
            A :py:class:`~abaqus.Material.Plastic.Swelling.Swelling.Swelling` object.

        Raises
        ------
        RangeError
        """
        ...

    @abaqus_method_doc
    def setValues(self, *args, **kwargs):
        """This method modifies the Swelling object.

        Raises
        ------
        RangeError
        """
        ...
