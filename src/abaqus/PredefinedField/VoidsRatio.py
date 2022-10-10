from typing import Union
from typing_extensions import Literal

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from .PredefinedField import PredefinedField
from ..Region.Region import Region
from ..UtilityAndView.abaqusConstants import abaqusConstants as C
from ..UtilityAndView.abaqusConstants import UNIFORM, CONSTANT_RATIO, MAGNITUDE


@abaqus_class_doc
class VoidsRatio(PredefinedField):
    """The VoidsRatio object stores the data for an initial void ratio predefined field.
    The VoidsRatio object is derived from the PredefinedField object.

    .. note::
    
        This object can be accessed by::

            import load
            mdb.models[name].predefinedFields[name]

        The corresponding analysis keywords are:

        - INITIAL CONDITIONS
    """

    @abaqus_method_doc
    def __init__(
        self,
        name: str,
        region: Region,
        distributionType: Literal[C.UNIFORM, C.FROM_FILE, C.USER_DEFINED] = UNIFORM,
        voidsRatio1: float = ...,
        voidsRatio2: float = ...,
        coord1: float = ...,
        coord2: float = ...,
        ratio2Distribution: Literal[C.MAGNITUDE, C.ANALYTICAL_FIELD] = MAGNITUDE,
        ratio2Field: str = ...,
        variation: Literal[C.CONSTANT_RATIO, C.VARIABLE_RATIO] = CONSTANT_RATIO,
        fileName: str = ...,
        increment: Union[int, Literal[C.LAST_INCREMENT]] = ...,
        step: Union[int, Literal[C.LAST_STEP]] = ...,
        interpolate: bool = ...,
    ) -> None:
        """This method creates a PorePressure predefined field object.

        .. note::
            This function can be accessed by::

                mdb.models[name].VoidsRatio

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
        voidsRatio1
            ...
        voidsRatio2
            ...
        coord1
            ...
        coord2
            ...
        ratio2Distribution
            ...
        ratio2Field
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
            A VoidsRatio object.
        """
        super().__init__()

    @abaqus_method_doc
    def setValues(
        self,
        distributionType: Literal[C.UNIFORM, C.FROM_FILE, C.USER_DEFINED] = UNIFORM,
        voidsRatio1: float = ...,
        voidsRatio2: float = ...,
        coord1: float = ...,
        coord2: float = ...,
        ratio2Distribution: Literal[C.MAGNITUDE, C.ANALYTICAL_FIELD] = MAGNITUDE,
        ratio2Field: str = ...,
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
        voidsRatio1
            ...
        voidsRatio2
            ...
        coord1
            ...
        coord2
            ...
        ratio2Distribution
            ...
        ratio2Field
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
