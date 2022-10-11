from typing_extensions import Literal

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from .PredefinedField import PredefinedField
from ..Region.Region import Region
from ..UtilityAndView.abaqusConstants import abaqusConstants as C
from ..UtilityAndView.abaqusConstants import UNIFORM


@abaqus_class_doc
class Saturation(PredefinedField):
    """The Saturation object stores the data for a saturation predefined field.
    The Saturation object is derived from the PredefinedField object.

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
        distributionType: Literal[C.UNIFORM, C.FIELD] = UNIFORM,
        field: str = "",
        value: float = ...,
    ) -> None:
        """This method creates a Saturation predefined field object.

        .. note::

            This function can be accessed by::

                mdb.models[name].Saturation

        Parameters
        ----------
        name
            A String specifying the repository key.
        region
            A Region object specifying the region to which the predefined field is applied.
        distributionType
            A SymbolicConstant specifying whether the load is uniform. Possible values are UNIFORM,
            and FIELD. The default value is UNIFORM.
        field
            A String specifying the name of the AnalyticalField object associated
            with this predefined field. The **field** argument applies only when
            **distributionType** = FIELD. The default value is an empty string.
        value
            A float specifying an initial saturation value for the region between 0.0 (for no
            saturation) and 1.0 (for full saturation).

        Returns
        -------
            A Saturation object.
        """
        super().__init__()

    @abaqus_method_doc
    def setValues(
        self,
        name: str,
        region: Region,
        distributionType: Literal[C.UNIFORM, C.FIELD] = UNIFORM,
        field: str = "",
        value: float = ...,
    ) -> None:
        """This method modifies the Saturation object.

        Parameters
        ----------
        name
            A String specifying the repository key.
        region
            A Region object specifying the region to which the predefined field is applied.
        distributionType
            A SymbolicConstant specifying whether the load is uniform. Possible values are UNIFORM,
            and FIELD. The default value is UNIFORM.
        field
            A String specifying the name of the AnalyticalField object associated
            with this predefined field. The **field** argument applies only when
            **distributionType** = FIELD. The default value is an empty string.
        value
            A float specifying an initial saturation value for the region between 0.0 (for no
            saturation) and 1.0 (for full saturation).

        Returns
        -------
            None
        """
        ...
