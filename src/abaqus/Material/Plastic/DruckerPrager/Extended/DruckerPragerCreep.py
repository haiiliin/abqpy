from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from .....UtilityAndView.abaqusConstants import Boolean, OFF, STRAIN, SymbolicConstant


@abaqus_class_doc
class DruckerPragerCreep:
    r"""The DruckerPragerCreep object specifies creep for Drucker-Prager plasticity models.

    .. note:: 
        This object can be accessed by::

            import material
            mdb.models[name].materials[name].druckerPrager.druckerPragerCreep
            import odbMaterial
            session.odbs[name].materials[name].druckerPrager.druckerPragerCreep

        The table data for this object are:

        - If **law** = TIME or **law** = STRAIN, the table data specify the following:
        
            - A. (Units of :math:`\mathrm{F}^{-n} \mathrm{~L}^{2 n} \mathrm{~T}^{-1-m}`.)
            - :math:`n`.
            - :math:`m`.
            - Temperature, if the data depend on temperature.
            - Value of the first field variable, if the data depend on field variables.
            - Value of the second field variable.
            - Etc.
        - If **law** = SINGHM, the table data specify the following:
        
            - A. (Units of :math:`\mathrm{T}^{-1}`. )
            - :math:`\alpha`. (Units of :math:`F^{-1} L^{2}`.)
            - :math:`m`.
            - :math:`t_{1} \cdot` (Units of :math:`\mathrm{T}`.)
            - Temperature, if the data depend on temperature.
            - Value of the first field variable, if the data depend on field variables.
            - Value of the second field variable.
            - Etc.

        The corresponding analysis keywords are:

        - DRUCKER PRAGER CREEP
    """

    @abaqus_method_doc
    def __init__(
        self,
        table: tuple,
        law: SymbolicConstant = STRAIN,
        temperatureDependency: Boolean = OFF,
        dependencies: int = 0,
    ):
        """This method creates a DruckerPragerCreep object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].materials[name].druckerPrager.DruckerPragerCreep
                session.odbs[name].materials[name].druckerPrager.DruckerPragerCreep

        Parameters
        ----------
        table
            A sequence of sequences of Floats specifying the items described below.
        law
            A SymbolicConstant specifying the type of data defining the creep law. Possible values
            are:STRAIN, specifying a strain-hardening power law.TIME, specifying a time-hardening
            power law.SINGHM, specifying a Singh-Mitchell type law.USER, specifying the creep law is
            input from user subroutine CREEP.The default value is STRAIN.
        temperatureDependency
            A Boolean specifying whether the data depend on temperature. The default value is OFF.
        dependencies
            An Int specifying the number of field variable dependencies. The default value is 0.

        Returns
        -------
        DruckerPragerCreep
            A :py:class:`~abaqus.Material.Plastic.DruckerPrager.Extended.DruckerPragerCreep.DruckerPragerCreep` object.

        Raises
        ------
        RangeError
        """
        ...

    @abaqus_method_doc
    def setValues(self, *args, **kwargs):
        """This method modifies the DruckerPragerCreep object.

        Raises
        ------
        RangeError
        """
        ...
