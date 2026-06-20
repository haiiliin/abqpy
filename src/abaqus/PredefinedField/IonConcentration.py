from __future__ import annotations

from typing_extensions import Literal

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from ..Region.Region import Region
from ..UtilityAndView.abaqusConstants import SymbolicConstant
from ..UtilityAndView.abaqusConstants import abaqusConstants as C
from .PredefinedField import PredefinedField


@abaqus_class_doc
class IonConcentration(PredefinedField):
    """The IonConcentration object stores the data for an ion concentration predefined field.
    The IonConcentration object is derived from the PredefinedField object.

    .. note::
        This object can be accessed by::

            import load
            mdb.models[name].predefinedFields[name]

        The corresponding analysis keywords are:

        - INSTANCE

    .. versionadded:: 2025
        The ``IonConcentration`` class was added.
    """

    #: A String specifying the repository key.
    name: str = ""

    #: A Region object specifying the region to which the predefined field is applied.
    region: Region = Region()

    #: A SymbolicConstant specifying how the predefined field varies spatially. Possible values
    #: are UNIFORM, FIELD, and DISCRETE_FIELD. The default value is UNIFORM.
    distributionType: SymbolicConstant = C.UNIFORM

    #: A String specifying the name of the AnalyticalField or DiscreteField object associated with
    #: this predefined field. The field argument applies only when distributionType is FIELD or
    #: distributionType is DISCRETE_FIELD. The default value is an empty string.
    field: str = ""

    #: A Float specifying the initial value of ion concentration.
    value: float = 0.0

    @abaqus_method_doc
    def __init__(
        self,
        name: str,
        region: Region,
        distributionType: Literal[C.UNIFORM, C.FIELD, C.DISCRETE_FIELD] = C.UNIFORM,
        field: str = "",
        value: float = 0.0,
    ):
        """This method creates an IonConcentration predefined field object.

        .. note::
            This function can be accessed by::

                mdb.models[name].IonConcentration

        Parameters
        ----------
        name
            A String specifying the repository key.
        region
            A Region object specifying the region to which the predefined field is applied.
        distributionType
            A SymbolicConstant specifying how the predefined field varies spatially. Possible values
            are UNIFORM, FIELD, and DISCRETE_FIELD. The default value is UNIFORM.
        field
            A String specifying the name of the AnalyticalField or DiscreteField object associated
            with this predefined field. The field argument applies only when distributionType is FIELD
            or distributionType is DISCRETE_FIELD. The default value is an empty string.
        value
            A Float specifying the initial value of ion concentration.

        Returns
        -------
        IonConcentration
            An IonConcentration object.
        """
        super().__init__()

    @abaqus_method_doc
    def setValues(
        self,
        region: Region | None = None,
        distributionType: Literal[C.UNIFORM, C.FIELD, C.DISCRETE_FIELD] = C.UNIFORM,
        field: str = "",
        value: float = 0.0,
    ):
        """This method modifies the IonConcentration object.

        Parameters
        ----------
        region
            A Region object specifying the region to which the predefined field is applied.
        distributionType
            A SymbolicConstant specifying how the predefined field varies spatially. Possible values
            are UNIFORM, FIELD, and DISCRETE_FIELD. The default value is UNIFORM.
        field
            A String specifying the name of the AnalyticalField or DiscreteField object associated
            with this predefined field. The field argument applies only when distributionType is FIELD
            or distributionType is DISCRETE_FIELD. The default value is an empty string.
        value
            A Float specifying the initial value of ion concentration.
        """
        ...
