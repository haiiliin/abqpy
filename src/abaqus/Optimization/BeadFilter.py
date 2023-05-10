from typing import Union

from typing_extensions import Literal

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from ..Region.Region import Region
from ..UtilityAndView.abaqusConstants import ABSOLUTE_VALUE, FILTER_REGION
from ..UtilityAndView.abaqusConstants import abaqusConstants as C
from .GeometricRestriction import GeometricRestriction


@abaqus_class_doc
class BeadFilter(GeometricRestriction):
    """The BeadFilter object defines a growth geometric restriction. The BeadFilter object is derived from the
    GeometricRestriction object.

    .. note::
        This object can be accessed by::

            import optimization
            mdb.models[name].optimizationTasks[name].geometricRestrictions[name]

    .. versionadded:: 2023

        The ``BeadFilter`` class was added.
    """

    #: A String specifying the geometric restriction repository key.
    name: str

    #: A Region object specifying the region to which the geometric restriction is applied.
    region: Region

    #: A Float specifying the filter radius. The default value is double the average edge length of the model.
    radius: float = None

    #: The SymbolicConstant defines whether the filter radius is in absolute or relative units. For an absolute
    #: radius, the value is ABSOLUTE_VALUE. For a relative radius, the value is RELATIVE. The default value is
    #: ABSOLUTE_VALUE.
    filterRadiusBy: Literal[C.ABSOLUTE_VALUE, C.RELATIVE] = ABSOLUTE_VALUE

    #: The SymbolicConstant FILTER_REGION or a Region object specifying the filter check region. If the value is
    #: FILTER_REGION, the value of the region is used as both the filter region and the filter check region.
    #: The default value is FILTER_REGION.
    filterCheckRegion: Union[Literal[C.FILTER_REGION], Region] = FILTER_REGION

    @abaqus_method_doc
    def __init__(
        self,
        name: str,
        region: Region,
        radius: float = None,
        filterRadiusBy: Literal[C.ABSOLUTE_VALUE, C.RELATIVE] = ABSOLUTE_VALUE,
        filterCheckRegion: Union[Literal[C.FILTER_REGION], Region] = FILTER_REGION,
    ):
        """This method creates a BeadFilter object.

        .. note::
            This function can be accessed by::

                mdb.models[name].optimizationTasks[name].BeadFilter

        Parameters
        ----------
        name
            A String specifying the geometric restriction repository key.
        region
            A Region object specifying the region to which the geometric restriction is applied.
        radius
            A Float specifying the filter radius. The default value is double the average edge length of the model.
        filterRadiusBy
            The SymbolicConstant defines whether the filter radius is in absolute or relative units. For an absolute
            radius, the value is ABSOLUTE_VALUE. For a relative radius, the value is RELATIVE. The default value is
            ABSOLUTE_VALUE.
        filterCheckRegion
            The SymbolicConstant FILTER_REGION or a Region object specifying the filter check region. If the value is
            FILTER_REGION, the value of the region is used as both the filter region and the filter check region.
            The default value is FILTER_REGION.

        Returns
        -------
        BeadFilter
            A BeadFilter object.
        """
        super().__init__()

    @abaqus_method_doc
    def setValues(
        self,
        region: Region,
        radius: float = None,
        filterRadiusBy: Literal[C.ABSOLUTE_VALUE, C.RELATIVE] = ABSOLUTE_VALUE,
        filterCheckRegion: Union[Literal[C.FILTER_REGION], Region] = FILTER_REGION,
    ):
        """This method modifies the BeadFilter object.

        Parameters
        ----------
        region
            A Region object specifying the region to which the geometric restriction is applied.
        radius
            A Float specifying the filter radius. The default value is double the average edge length of the model.
        filterRadiusBy
            The SymbolicConstant defines whether the filter radius is in absolute or relative units. For an absolute
            radius, the value is ABSOLUTE_VALUE. For a relative radius, the value is RELATIVE. The default value is
            ABSOLUTE_VALUE.
        filterCheckRegion
            The SymbolicConstant FILTER_REGION or a Region object specifying the filter check region. If the value is
            FILTER_REGION, the value of the region is used as both the filter region and the filter check region.
            The default value is FILTER_REGION.
        """
        ...
