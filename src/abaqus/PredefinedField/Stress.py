from typing_extensions import Literal

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from .PredefinedField import PredefinedField
from ..Region.Region import Region
from ..UtilityAndView.abaqusConstants import UNIFORM
from ..UtilityAndView.abaqusConstants import abaqusConstants as C


@abaqus_class_doc
class Stress(PredefinedField):
    """The Stress object stores the data for an initial stress predefined field.
    The Stress object is derived from the PredefinedField object.

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
        distributionType: Literal[C.UNIFORM, C.FROM_FILE] = UNIFORM,
        sigma11: float = ...,
        sigma22: float = ...,
        sigma33: float = ...,
        sigma12: float = ...,
        sigma13: float = ...,
        sigma23: float = ...,
    ) -> None:
        """This method creates a Stress predefined field object.

        .. note::
        This function can be accessed by::

            mdb.models[name].Stress

        Parameters
        ----------
        name
            A String specifying the repository key.
        region
            A Region object specifying the region to which the predefined field is applied. Region
            is ignored if the predefined field has **distributionType** = FROM_FILE.
        distributionType
            A SymbolicConstant specifying whether the load is uniform. Possible values are UNIFORM
            and FROM_FILE. The default value is UNIFORM.
        sigma11
            A Float specifying the first principal component of the stress.
        sigma22
            A Float specifying the second principal component of the stress.
        sigma33
            A Float specifying the third principal component of the stress.
        sigma12
            A Float specifying the first shear component of the stress.
        sigma13
            A Float specifying the second shear component of the stress.
        sigma23
            A Float specifying the third shear component of the stress.

        Returns
        -------
            A Stress object.
        """
        super().__init__()

    @abaqus_method_doc
    def setValues(
        self,
        distributionType: Literal[C.UNIFORM, C.FROM_FILE] = UNIFORM,
        sigma11: float = ...,
        sigma22: float = ...,
        sigma33: float = ...,
        sigma12: float = ...,
        sigma13: float = ...,
        sigma23: float = ...,
    ) -> None:
        """This method modifies the Stress object.

        Parameters
        ----------
        distributionType
            A SymbolicConstant specifying whether the load is uniform. Possible values are UNIFORM
            and FROM_FILE. The default value is UNIFORM.
        sigma11
            A Float specifying the first principal component of the stress.
        sigma22
            A Float specifying the second principal component of the stress.
        sigma33
            A Float specifying the third principal component of the stress.
        sigma12
            A Float specifying the first shear component of the stress.
        sigma13
            A Float specifying the second shear component of the stress.
        sigma23
            A Float specifying the third shear component of the stress.

        Returns
        -------
            None
        """
        ...
