from typing_extensions import Literal
from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from ....UtilityAndView.abaqusConstants import abaqusConstants as C
from ....UtilityAndView.abaqusConstants import Boolean, OFF, STRAIN


@abaqus_class_doc
class TensionStiffening:
    """The TensionStiffening object defines the retained tensile stress normal to a crack in a
    Concrete model.

    .. note:: 
        This object can be accessed by::

            import material
            mdb.models[name].materials[name].concrete.tensionStiffening
            import odbMaterial
            session.odbs[name].materials[name].concrete.tensionStiffening

        The table data for this object are:

        - If **type** = STRAIN, the table data specify the following:
        
            - Fraction of remaining stress to stress at cracking.
            - Absolute value of the direct strain minus the direct strain at cracking.
            - Temperature, if the data depend on temperature.
            - Value of the first field variable, if the data depend on field variables.
            - Value of the second field variable.
            - Etc.
        - If **type** = DISPLACEMENT, the table data specify the following:
        
            - Displacement, u0u0, at which a linear loss of strength after cracking gives zero stress.
            - Temperature, if the data depend on temperature.
            - Value of the first field variable, if the data depend on field variables.
            - Value of the second field variable.
            - Etc.

        The corresponding analysis keywords are:

        - TENSION STIFFENING
    """

    @abaqus_method_doc
    def __init__(
        self,
        table: tuple,
        type: Literal[C.STRAIN, C.DISPLACEMENT] = STRAIN,
        temperatureDependency: Boolean = OFF,
        dependencies: int = 0,
    ):
        """This method creates a TensionStiffening object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].materials[name].concrete.TensionStiffening
                session.odbs[name].materials[name].concrete.TensionStiffening

        Parameters
        ----------
        table
            A sequence of sequences of Floats specifying the items described below.
        type
            A SymbolicConstant specifying how the postcracking behavior is defined. Possible values
            are DISPLACEMENT and STRAIN. The default value is STRAIN.
        temperatureDependency
            A Boolean specifying whether the data depend on temperature. The default value is OFF.
        dependencies
            An Int specifying the number of field variable dependencies. The default value is 0.

        Returns
        -------
        TensionStiffening
            A :py:class:`~abaqus.Material.Plastic.Concrete.TensionStiffening.TensionStiffening` object.

        Raises
        ------
        RangeError
        """
        ...

    @abaqus_method_doc
    def setValues(self, *args, **kwargs):
        """This method modifies the TensionStiffening object.

        Raises
        ------
        RangeError
        """
        ...
