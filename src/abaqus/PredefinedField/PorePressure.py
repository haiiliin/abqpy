from typing import Union
from typing_extensions import Literal

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from .PredefinedField import PredefinedField
from ..Region.Region import Region
from ..UtilityAndView.abaqusConstants import abaqusConstants as C
from ..UtilityAndView.abaqusConstants import UNIFORM, CONSTANT_RATIO, MAGNITUDE


@abaqus_class_doc
class PorePressure(PredefinedField):
    """The PorePressure object stores the data for an initial pore pressure predefined field.
    The PorePressure object is derived from the PredefinedField object.

    .. note::
    
        This object can be accessed by::

            import load
            mdb.models[name].predefinedFields[name]

        The corresponding analysis keywords are:

        - INITIAL CONDITIONS

    .. versionadded:: 2021
        The `PorePressure` class was added.

    """

    @abaqus_method_doc
    def __init__(
        self,
        name: str,
        region: Region,
        distributionType: Literal[C.UNIFORM, C.FROM_FILE, C.USER_DEFINED] = UNIFORM,
        porePressure1: float = ...,
        porePressure2: float = ...,
        coord1: float = ...,
        coord2: float = ...,
        pressure2Distribution: Literal[C.MAGNITUDE, C.ANALYTICAL_FIELD] = MAGNITUDE,
        pressure2Field: str = ...,
        variation: Literal[C.CONSTANT_RATIO, C.VARIABLE_RATIO] = CONSTANT_RATIO,
        fileName: str = ...,
        increment: Union[int, Literal[C.LAST_INCREMENT]] = ...,
        step: Union[int, Literal[C.LAST_STEP]] = ...,
        interpolate: bool = ...,
    ) -> None:
        """This method creates a PorePressure predefined field object.

        .. note::

            This function can be accessed by::

                mdb.models[name].PorePressure

        Parameters
        ----------
        name
            A String specifying the repository key.
        region
            A Region object specifying the region to which the predefined field is applied. Region
            is ignored if the predefined field has **distributionType** = FROM_FILE.
        distributionType
            A SymbolicConstant specifying whether the load is uniform. Possible values are UNIFORM,
            FROM_FILE and USER_DEFINED. The default value is UNIFORM.
        porePressure1
            ...
        porePressure2
            ...
        coord1
            ...
        coord2
            ...
        pressure2Distribution
            ...
        pressure2Field
            ...
        variation
            ...
        fileName
            ...
        increment
            ...
        step
            ...
        interpolate
            ...

        Returns
        -------
            A PorePressure object.
        """
        super().__init__()

    @abaqus_method_doc
    def setValues(
        self,
        distributionType: Literal[C.UNIFORM, C.FROM_FILE, C.USER_DEFINED] = UNIFORM,
        porePressure1: float = ...,
        porePressure2: float = ...,
        coord1: float = ...,
        coord2: float = ...,
        pressure2Distribution: Literal[C.MAGNITUDE, C.ANALYTICAL_FIELD] = MAGNITUDE,
        pressure2Field: str = ...,
        variation: Literal[C.CONSTANT_RATIO, C.VARIABLE_RATIO] = CONSTANT_RATIO,
        fileName: str = ...,
        increment: Union[int, Literal[C.LAST_INCREMENT]] = ...,
        step: Union[int, Literal[C.LAST_STEP]] = ...,
        interpolate: bool = ...,
    ) -> None:
        """This method modifies the PorePressure object.

        Parameters
        ----------
        distributionType
            A SymbolicConstant specifying whether the load is uniform. Possible values are UNIFORM,
            FROM_FILE and USER_DEFINED. The default value is UNIFORM.
        porePressure1
            ...
        porePressure2
            ...
        coord1
            ...
        coord2
            ...
        pressure2Distribution
            ...
        pressure2Field
            ...
        variation
            ...
        fileName
            ...
        increment
            ...
        step
            ...
        interpolate
            ...

        Returns
        -------
            None
        """
        ...
