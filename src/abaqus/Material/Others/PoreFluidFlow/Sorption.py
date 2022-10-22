from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from ....UtilityAndView.abaqusConstants import Boolean, OFF, SymbolicConstant, TABULAR


@abaqus_class_doc
class Sorption:
    r"""The Sorption object defines absorption and exsorption behaviors of a partially saturated
    porous medium in the analysis of coupled wetting liquid flow and porous medium stress.

    .. note:: 
        This object can be accessed by::

            import material
            mdb.models[name].materials[name].sorption
            import odbMaterial
            session.odbs[name].materials[name].sorption

        The table data for this object are:

        - If **lawAbsorption** = TABULAR or **lawExsorption** = TABULAR, the **absorptionTable** and **exsorptionTable** data respectively specify the following:

            - Pore pressure, :math:`u_{w}`.
            - Saturation, :math:`\boldsymbol{S}`.

        - If **lawAbsorption** = LOG or **lawExsorption** = LOG, the **absorptionTable** and **exsorptionTable** data respectively specify the following:

            - :math:`A`.
            - :math:`B`.
            - :math:`\boldsymbol{s}_{0}`.
            - :math:`\boldsymbol{s}_{1}`.

        The corresponding analysis keywords are:

        - SORPTION
    """

    @abaqus_method_doc
    def __init__(
        self,
        absorptionTable: tuple,
        lawAbsorption: SymbolicConstant = TABULAR,
        exsorption: Boolean = OFF,
        lawExsorption: SymbolicConstant = TABULAR,
        scanning: float = 0,
        exsorptionTable: tuple = (),
    ):
        r"""This method creates a Sorption object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].materials[name].Sorption
                session.odbs[name].materials[name].Sorption

        Parameters
        ----------
        absorptionTable
            A sequence of sequences of Floats specifying the items described below.
        lawAbsorption
            A SymbolicConstant specifying absorption behavior. Possible values are LOG and TABULAR.
            The default value is TABULAR.
        exsorption
            A Boolean specifying whether the exsorption data is specified. The default value is OFF.
        lawExsorption
            A SymbolicConstant specifying exsorption behavior. Possible values are LOG and TABULAR.
            The default value is TABULAR.
        scanning
            A Float specifying the slope of the scanning line, :math:`\left.\left(d u_{w} / d s\right)\right|_{s}`. 
            This slope must be positive and larger than the slope of the absorption or exsorption behaviors. The
            default value is 0.0.
        exsorptionTable
            A sequence of sequences of Floats specifying the items described below. The default
            value is an empty sequence.

        Returns
        -------
        Sorption
            A :py:class:`~abaqus.Material.Others.PoreFluidFlow.Sorption.Sorption` object.

        Raises
        ------
        RangeError
        """
        ...

    @abaqus_method_doc
    def setValues(self, *args, **kwargs):
        """This method modifies the Sorption object.

        Raises
        ------
        RangeError
        """
        ...
