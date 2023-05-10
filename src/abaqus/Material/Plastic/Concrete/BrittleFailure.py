from typing_extensions import Literal

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from ....UtilityAndView.abaqusConstants import OFF, UNIDIRECTIONAL, Boolean
from ....UtilityAndView.abaqusConstants import abaqusConstants as C


@abaqus_class_doc
class BrittleFailure:
    """The BrittleFailure object specifies the brittle failure of the material.

    .. note::
        This object can be accessed by::

            import material
            mdb.models[name].materials[name].brittleCracking.brittleFailure
            import odbMaterial
            session.odbs[name].materials[name].brittleCracking.brittleFailure

        The table data for this object are:

        - If parent BrittleCracking member **type** = STRAIN the table data specify the following:

            - Direct cracking failure strain.
            - Temperature, if the data depend on temperature.
            - Value of the first field variable, if the data depend on field variables.
            - Value of the second field variable.
            - Etc.
        - If parent BrittleCracking member **type** = DISPLACEMENT or **type** = GFI the table data specify the following:

            - Direct cracking failure displacement.
            - Temperature, if the data depend on temperature.
            - Value of the first field variable, if the data depend on field variables.
            - Value of the second field variable.
            - Etc.

        The corresponding analysis keywords are:

        - BRITTLE FAILURE
    """

    @abaqus_method_doc
    def __init__(
        self,
        table: tuple,
        temperatureDependency: Boolean = OFF,
        dependencies: int = 0,
        failureCriteria: Literal[C.BIDIRECTIONAL, C.UNIDIRECTIONAL, C.TRIDIRECTIONAL] = UNIDIRECTIONAL,
    ):
        """This method creates a BrittleFailure object.

        .. note::
            This function can be accessed by::

                mdb.models[name].materials[name].brittleCracking.BrittleFailure
                session.odbs[name].materials[name].brittleCracking.BrittleFailure

        Parameters
        ----------
        table
            A sequence of sequences of Floats specifying the items described below.
        temperatureDependency
            A Boolean specifying whether the data depend on temperature. The default value is OFF.
        dependencies
            An Int specifying the number of field variable dependencies. The default value is 0.
        failureCriteria
            A SymbolicConstant specifying the failure criteria. Possible values are UNIDIRECTIONAL,
            BIDIRECTIONAL, and TRIDIRECTIONAL. The default value is UNIDIRECTIONAL.

        Returns
        -------
        BrittleFailure
            A BrittleFailure object.

        Raises
        ------
        RangeError
        """
        ...

    @abaqus_method_doc
    def setValues(self, *args, **kwargs):
        """This method modifies the BrittleFailure object.

        Raises
        ------
        RangeError
        """
        ...
