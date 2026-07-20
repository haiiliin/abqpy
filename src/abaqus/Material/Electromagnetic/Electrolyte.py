from __future__ import annotations

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc


@abaqus_class_doc
class Electrolyte:
    """The Electrolyte object specifies electrolyte material properties.

    .. note::
        This object can be accessed by::

            import material
            mdb.models[name].materials[name].electrolyte

        The corresponding analysis keywords are:

        - ABQ_EChemPET_Electrolyte

    .. versionadded:: 2026
        The ``Electrolyte`` class was added.
    """

    @abaqus_method_doc
    def __init__(self, chargeNum: float):
        """This method creates an Electrolyte object.

        .. note::
            This function can be accessed by::

                mdb.models[name].materials[name].Electrolyte

        Parameters
        ----------
        chargeNum
            A Float specifying the charge number of the lithium ion battery.

        Returns
        -------
            An Electrolyte object.

        Raises
        ------
        RangeError
            If a specified value is outside the valid range.
        """
        super().__init__()

    @abaqus_method_doc
    def setValues(
        self,
        chargeNum: float = 0,
    ):
        """This method modifies the Electrolyte object.

        Parameters
        ----------
        chargeNum
            A Float specifying the charge number of the lithium ion battery.

        Raises
        ------
        RangeError
            If a specified value is outside the valid range.
        """
        ...

    @abaqus_method_doc
    def DefineDetails(
        self,
        subType: str,
        data: tuple,
    ):
        """This method specifies the details of the Electrolyte object.

        Parameters
        ----------
        subType
            A String specifying the property or parameter table type that
            describes the behavior of the electrolyte. Possible values are

            - ``ABQ_EChemPET_Electrolyte_MolarActivityCoeff_fPM``
            - ``ABQ_EChemPET_Electrolyte_DiffTabular``
            - ``ABQ_EChemPET_Electrolyte_ElecCond_Tabular``
            - ``ABQ_EChemPET_Electrolyte_Transference``
        data
            An array of properties of the specified material definition type.

        Raises
        ------
        RangeError
            If a specified value is outside the valid range.
        """
        ...

    @abaqus_method_doc
    def EditDetails(
        self,
        subType: str,
        data: tuple,
    ):
        """This method modifies the details of the Electrolyte object.

        Parameters
        ----------
        subType
            A String specifying the property or parameter table type that
            describes the behavior of the electrolyte. Possible values are

            - ``ABQ_EChemPET_Electrolyte_MolarActivityCoeff_fPM``
            - ``ABQ_EChemPET_Electrolyte_DiffTabular``
            - ``ABQ_EChemPET_Electrolyte_ElecCond_Tabular``
            - ``ABQ_EChemPET_Electrolyte_Transference``
        data
            An array of properties of the specified material definition type.

        Raises
        ------
        RangeError
            If a specified value is outside the valid range.
        """
        ...
