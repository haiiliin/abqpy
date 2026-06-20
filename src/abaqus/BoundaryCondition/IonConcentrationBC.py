from __future__ import annotations

from typing_extensions import Literal

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from ..Region.Region import Region
from ..UtilityAndView.abaqusConstants import UNSET, SymbolicConstant
from ..UtilityAndView.abaqusConstants import abaqusConstants as C
from .BoundaryCondition import BoundaryCondition


@abaqus_class_doc
class IonConcentrationBC(BoundaryCondition):
    """The IonConcentrationBC object stores the data for an ion concentration boundary condition.
    The IonConcentrationBC object is derived from the BoundaryCondition object.

    .. note::
        This object can be accessed by::

            import load
            mdb.models[name].boundaryConditions[name]

    .. versionadded:: 2025
        The ``IonConcentrationBC`` class was added.
    """

    #: A String specifying the boundary condition repository key.
    name: str = ""

    #: A SymbolicConstant specifying how the boundary condition is distributed spatially.
    #: Possible values are UNIFORM, USER_DEFINED, and FIELD. The default value is UNIFORM.
    distributionType: SymbolicConstant = C.UNIFORM

    #: A String specifying the name of the AnalyticalField object associated with this boundary
    #: condition. The fieldName argument applies only when distributionType=FIELD. The default
    #: value is an empty string.
    fieldName: str = ""

    #: A SymbolicConstant specifying the category of the boundary condition. Possible values
    #: are MECHANICAL, ELECTROCHEMICAL, and THERMAL.
    category: SymbolicConstant

    #: A Region object specifying the region to which the boundary condition is applied.
    region: Region = Region()

    #: None or a DatumCsys object specifying the local coordinate system of the boundary
    #: condition's degrees of freedom. If **localCsys** = None, the degrees of freedom are defined
    #: in the global coordinate system. The default value is None.
    localCsys: str | None = None

    @abaqus_method_doc
    def __init__(
        self,
        name: str,
        createStepName: str,
        region: Region,
        distributionType: Literal[C.UNIFORM, C.FIELD, C.DISCRETE_FIELD] = C.UNIFORM,
        field: str = "",
        value: float = 0.0,
    ):
        """This method creates an IonConcentrationBC object.

        .. note::
            This function can be accessed by::

                mdb.models[name].IonConcentrationBC

        Parameters
        ----------
        name
            A String specifying the repository key.
        createStepName
            A String specifying the name of the step in which the boundary condition is created.
        region
            A Region object specifying the region to which the predefined field is applied.
        distributionType
            A SymbolicConstant specifying how the predefined field varies spatially. Possible
            values are UNIFORM, FIELD, and DISCRETE_FIELD. The default value is UNIFORM.
        field
            A String specifying the name of the AnalyticalField or DiscreteField object associated
            with this predefined field. The **field** argument applies only when
            **distributionType** = FIELD or **distributionType** = DISCRETE_FIELD. The default
            value is an empty string.
        value
            A Float specifying the initial value of ion concentration.

        Returns
        -------
        IonConcentrationBC
            An IonConcentrationBC object.
        """
        super().__init__()

    @abaqus_method_doc
    def setValues(
        self,
        distributionType: Literal[C.UNIFORM, C.FIELD, C.DISCRETE_FIELD] = C.UNIFORM,
        field: str = "",
        value: float = 0.0,
    ):
        """This method modifies the data for an existing IonConcentrationBC object in the step where it is
        created.

        Parameters
        ----------
        distributionType
            A SymbolicConstant specifying how the predefined field varies spatially. Possible
            values are UNIFORM, FIELD, and DISCRETE_FIELD. The default value is UNIFORM.
        field
            A String specifying the name of the AnalyticalField or DiscreteField object associated
            with this predefined field. The **field** argument applies only when
            **distributionType** = FIELD or **distributionType** = DISCRETE_FIELD. The default
            value is an empty string.
        value
            A Float specifying the initial value of ion concentration.
        """
        ...

    @abaqus_method_doc
    def setValuesInStep(
        self,
        stepName: str,
        distributionType: Literal[C.UNIFORM, C.FIELD, C.DISCRETE_FIELD] = C.UNIFORM,
        field: str = "",
        value: float | SymbolicConstant = UNSET,
    ):
        """This method modifies the propagating data for an existing IonConcentrationBC object in the
        specified step.

        Parameters
        ----------
        stepName
            A String specifying the name of the step in which the boundary condition is modified.
        distributionType
            A SymbolicConstant specifying how the predefined field varies spatially. Possible
            values are UNIFORM, FIELD, and DISCRETE_FIELD. The default value is UNIFORM.
        field
            A String specifying the name of the AnalyticalField or DiscreteField object associated
            with this predefined field. The **field** argument applies only when
            **distributionType** is FIELD or **distributionType** is DISCRETE_FIELD. The default
            value is an empty string.
        value
            A Float specifying the initial value of ion concentration.
        """
        ...
