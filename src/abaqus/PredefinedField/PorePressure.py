from typing import Union
from typing_extensions import Literal

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from .PredefinedField import PredefinedField
from ..Region.Region import Region
from ..UtilityAndView.abaqusConstants import abaqusConstants as C
from ..UtilityAndView.abaqusConstants import Boolean, UNIFORM, CONSTANT_RATIO, MAGNITUDE


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
        interpolate: Boolean = ...,
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
            The initial pore pressure in the first region in your model.
        porePressure2
            The pore pressure of the second location in your model
        coord1
            Vertical position of the first location in your model for which you are specifying initial pore pressure.
        coord2
            The vertical position of the second location in your model.
        pressure2Distribution
            A SymbolicConstant specifying either the magnitude of a uniform distribution for pore pressure at the
            second elevation or an analytical field to define a spatially varying initial pore pressure at the second elevation.
            Possible values are MAGNITUDE and ANALYTICAL_FIELD.
        pressure2Field
            A String specifying the name of the AnalyticalField object associated with this predefined field.
            The `pressure2Field` argument applies only when `distributionType` = ANALYTICAL_FIELD.
        variation
            A SymbolicConstant selecting the elevation distribution options, either Linear or Constant.
            Possible values are CONSTANT_RATIO and VARIABLE_RATIO.
        fileName
            A String specifying the name of the file from which the Field values are to be read when 
            `distributionType` = FROM_FILE.
        increment
            The SymbolicConstant LAST_INCREMENT or an Int specifying the increment, interval or iteration
            of the step when `distributionType` = FROM_FILE.
        step
            The SymbolicConstant LAST_STEP or an Int specifying the increment, interval or iteration
            of the step when `distributionType` = FROM_FILE.
        interpolate
            A Boolean specifying whether to interpolate a field read from an output database or results file.

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
            The initial pore pressure in the first region in your model.
        porePressure2
            The pore pressure of the second location in your model
        coord1
            Vertical position of the first location in your model for which you are specifying initial pore pressure.
        coord2
            The vertical position of the second location in your model.
        pressure2Distribution
            A SymbolicConstant specifying either the magnitude of a uniform distribution for pore pressure at the
            second elevation or an analytical field to define a spatially varying initial pore pressure at the second elevation.
            Possible values are MAGNITUDE and ANALYTICAL_FIELD.
        pressure2Field
            A String specifying the name of the AnalyticalField object associated with this predefined field.
            The `pressure2Field` argument applies only when `distributionType` = ANALYTICAL_FIELD.
        variation
            A SymbolicConstant selecting the elevation distribution options, either Linear or Constant.
            Possible values are CONSTANT_RATIO and VARIABLE_RATIO.
        fileName
            A String specifying the name of the file from which the Field values are to be read when 
            `distributionType` = FROM_FILE.
        increment
            The SymbolicConstant LAST_INCREMENT or an Int specifying the increment, interval or iteration
            of the step when `distributionType` = FROM_FILE.
        step
            The SymbolicConstant LAST_STEP or an Int specifying the increment, interval or iteration
            of the step when `distributionType` = FROM_FILE.
        interpolate
            A Boolean specifying whether to interpolate a field read from an output database or results file.

        Returns
        -------
            None
        """
        ...
