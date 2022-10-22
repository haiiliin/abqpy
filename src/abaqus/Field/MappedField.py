from typing import Optional

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from .AnalyticalField import AnalyticalField
from .OdbMeshRegionData import OdbMeshRegionData
from ..UtilityAndView.abaqusConstants import (Boolean, OFF, POINT, RELATIVE, SURFACE,
                                              SymbolicConstant, XYPLANE, XYZ)


@abaqus_class_doc
class MappedField(AnalyticalField):
    """The MappedField object defines a spatially varying field whose value is calculated from
    an external source data.
    The MappedField object is derived from the AnalyticalField object.

    .. note:: 
        This object can be accessed by::

            import fields
            mdb.models[name].analyticalFields[name]
    """

    #: A String specifying the repository key.
    name: str = ""

    #: A SymbolicConstant specifying the data source region type. It can be either an ODB mesh
    #: or a cloud of points. Possible values are MESH and POINT. The default value is POINT.
    regionType: SymbolicConstant = POINT

    #: A Boolean specifying whether or not the point cloud source data are described in terms
    #: of part level coordinates. If part level coordinates is employed, the local coordinate
    #: system defined in **localCsys** will be ignored. The default value is OFF.
    partLevelData: Boolean = OFF

    #: A SymbolicConstant specifying point cloud source data format. Possible values are GRID
    #: and XYZ. The default value is XYZ.
    pointDataFormat: SymbolicConstant = XYZ

    #: A SymbolicConstant specifying the plane on which the point cloud source data of grid
    #: format are described. Possible values are XYPLANE, YZPLANE, and XZPLANE. The default
    #: value is XYPLANE.
    gridPointPlane: SymbolicConstant = XYPLANE

    #: A Float specifying default parameter (field) value of target model region while its
    #: value cannot be calculated from the data source. The default value is 0.0.
    defaultUnMappedValue: float = 0

    #: A SymbolicConstant specifying the mapping algorithm for target surface, or on mesh
    #: target model when the parameter value are located at nodes, for example nodal
    #: temperatures. Possible values are SURFACE and VOLUMETRIC. The default value is SURFACE.
    mappingAlgorithm: SymbolicConstant = SURFACE

    #: A SymbolicConstant specifying searching tolerance type in terms of absolute value or a
    #: fraction of the average of all element characteristic length in target model region.
    #: Possible values are ABSOLUTE and RELATIVE. The default value is RELATIVE.
    searchTolType: SymbolicConstant = RELATIVE

    #: A Float specifying the search distance tolerance value on the exterior boundary of
    #: target model region. Source points within this distance will be included in computing
    #: the parameter value of target region. This tolerance applies to both surface and
    #: volumetric mapping. The default value is 0.01.
    boundarySearchTol: float = 0

    #: A Float specifying the search distance tolerance value used for distance weighting
    #: algorithm. Source points within this distance will be included in computing the
    #: parameter value of target region. This tolerance only applies to surface mapping. The
    #: default value is 1000000.0.
    neighborhoodSearchTol: float = 1000000

    #: A Float specifying the search distance tolerance value in the negative normal of target
    #: surface region. Source points within this distance will be included in computing the
    #: parameter value of target region. This tolerance only applies to surface mapping. The
    #: default value is 0.15.
    negativeNormalSearchTol: float = 0

    #: A Float specifying the search distance tolerance value in the positive normal of target
    #: surface region. Source points within this distance will be included in computing the
    #: parameter value of target region. This tolerance only applies to surface mapping. The
    #: default value is 0.05.
    positiveNormalSearchTol: float = 0

    #: A Boolean specifying whether or not to scale the user-supplied coordinate values from
    #: the point cloud or indicated ODB. The default value is OFF.
    scaleCoordinates: Boolean = OFF

    #: A tuple of tuples of Floats specifying the point cloud source data of grid format. The
    #: default value is an empty sequence.
    gridPointData: tuple = ()

    #: A tuple of tuples of Floats specifying the point cloud source data of XYZ format. Each
    #: data item is defining the XYZ coordinates of a point and its field value. The default
    #: value is an empty sequence.
    xyzPointData: tuple = ()

    #: An :py:class:`~abaqus.Field.OdbMeshRegionData.OdbMeshRegionData` object specifying the external source data from ODB mesh region.
    odbMeshRegionData: Optional[OdbMeshRegionData] = None

    #: A tuple of Floats specifying the scaling factors for the global 1, 2 and 3 directions.
    #: The default value is (1.0, 1.0, 1.0).
    coordinateScalingFactors: Optional[float] = None

    #: None or a DatumCsys object specifying the local coordinate system of the field. If
    #: **localCsys** = None, the field is defined in the global coordinate system. The default
    #: value is None.
    localCsys: Optional[str] = None

    #: A String specifying the description of the field. The default value is an empty string.
    description: str = ""

    @abaqus_method_doc
    def __init__(
        self,
        name: str,
        regionType: SymbolicConstant = POINT,
        partLevelData: Boolean = OFF,
        pointDataFormat: SymbolicConstant = XYZ,
        gridPointPlane: SymbolicConstant = XYPLANE,
        defaultUnMappedValue: float = 0,
        mappingAlgorithm: SymbolicConstant = SURFACE,
        searchTolType: SymbolicConstant = RELATIVE,
        boundarySearchTol: float = 0,
        neighborhoodSearchTol: float = 1000000,
        negativeNormalSearchTol: float = 0,
        positiveNormalSearchTol: float = 0,
        scaleCoordinates: Boolean = OFF,
        gridPointData: tuple = (),
        xyzPointData: tuple = (),
        coordinateScalingFactors: tuple = (),
        localCsys: Optional[str] = None,
        description: str = "",
    ):
        """This method creates an MappedField object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].MappedField

        Parameters
        ----------
        name
            A String specifying the repository key.
        regionType
            A SymbolicConstant specifying the data source region type. It can be either an ODB mesh
            or a cloud of points. Possible values are MESH and POINT. The default value is POINT.
        partLevelData
            A Boolean specifying whether or not the point cloud source data are described in terms
            of part level coordinates. If part level coordinates is employed, the local coordinate
            system defined in **localCsys** will be ignored. The default value is OFF.
        pointDataFormat
            A SymbolicConstant specifying point cloud source data format. Possible values are GRID
            and XYZ. The default value is XYZ.
        gridPointPlane
            A SymbolicConstant specifying the plane on which the point cloud source data of grid
            format are described. Possible values are XYPLANE, YZPLANE, and XZPLANE. The default
            value is XYPLANE.
        defaultUnMappedValue
            A Float specifying the parameter (field) value reported when a value cannot be
            calculated from the data source. The default value is 0.0.
        mappingAlgorithm
            A SymbolicConstant specifying the mapping algorithm for target surface, or on mesh
            target model when the parameter value are located at nodes, for example nodal
            temperatures. Possible values are SURFACE and VOLUMETRIC. The default value is SURFACE.
        searchTolType
            A SymbolicConstant specifying searching tolerance type in terms of absolute value or a
            fraction of the average of all element characteristic length in target model region.
            Possible values are ABSOLUTE and RELATIVE. The default value is RELATIVE.
        boundarySearchTol
            A Float specifying the search distance tolerance value on the exterior boundary of
            target model region. Source points within this distance will be included in computing
            the parameter value of target region. This tolerance applies to both surface and
            volumetric mapping. The default value is 0.01.
        neighborhoodSearchTol
            A Float specifying the search distance tolerance value used for distance weighting
            algorithm. Source points within this distance will be included in computing the
            parameter value of target region. This tolerance only applies to surface mapping. The
            default value is 1000000.0.
        negativeNormalSearchTol
            A Float specifying the search distance tolerance value in the negative normal of target
            surface region. Source points within this distance will be included in computing the
            parameter value of target region. This tolerance only applies to surface mapping. The
            default value is 0.15.
        positiveNormalSearchTol
            A Float specifying the search distance tolerance value in the positive normal of target
            surface region. Source points within this distance will be included in computing the
            parameter value of target region. This tolerance only applies to surface mapping. The
            default value is 0.05.
        scaleCoordinates
            A Boolean specifying whether or not to scale the user-supplied coordinate values from
            the point cloud or indicated ODB. The default value is OFF.
        gridPointData
            A sequence of sequences of Floats specifying the point cloud source data of grid format.
            The default value is an empty sequence.
        xyzPointData
            A sequence of sequences of Floats specifying the point cloud source data of XYZ format.
            Each data item is defining the XYZ coordinates of a point and its field value. The
            default value is an empty sequence.
        coordinateScalingFactors
            A sequence of Floats specifying the scaling factors for the global 1, 2 and 3
            directions. The default value is (1.0, 1.0, 1.0).
        localCsys
            None or a DatumCsys object specifying the local coordinate system of the field. If
            **localCsys** = None, the field is defined in the global coordinate system. The default
            value is None.
        description
            A String specifying the description of the field. The default value is an empty string.

        Returns
        -------
        MappedField
            A :py:class:`~abaqus.Field.MappedField.MappedField` object.

        Raises
        ------
        AbaqusException
        """
        super().__init__()

    @abaqus_method_doc
    def setValues(
        self,
        regionType: SymbolicConstant = POINT,
        partLevelData: Boolean = OFF,
        pointDataFormat: SymbolicConstant = XYZ,
        gridPointPlane: SymbolicConstant = XYPLANE,
        defaultUnMappedValue: float = 0,
        mappingAlgorithm: SymbolicConstant = SURFACE,
        searchTolType: SymbolicConstant = RELATIVE,
        boundarySearchTol: float = 0,
        neighborhoodSearchTol: float = 1000000,
        negativeNormalSearchTol: float = 0,
        positiveNormalSearchTol: float = 0,
        scaleCoordinates: Boolean = OFF,
        gridPointData: tuple = (),
        xyzPointData: tuple = (),
        coordinateScalingFactors: tuple = (),
        localCsys: Optional[str] = None,
        description: str = "",
    ):
        """This method modifies the MappedField object.

        Parameters
        ----------
        regionType
            A SymbolicConstant specifying the data source region type. It can be either an ODB mesh
            or a cloud of points. Possible values are MESH and POINT. The default value is POINT.
        partLevelData
            A Boolean specifying whether or not the point cloud source data are described in terms
            of part level coordinates. If part level coordinates is employed, the local coordinate
            system defined in **localCsys** will be ignored. The default value is OFF.
        pointDataFormat
            A SymbolicConstant specifying point cloud source data format. Possible values are GRID
            and XYZ. The default value is XYZ.
        gridPointPlane
            A SymbolicConstant specifying the plane on which the point cloud source data of grid
            format are described. Possible values are XYPLANE, YZPLANE, and XZPLANE. The default
            value is XYPLANE.
        defaultUnMappedValue
            A Float specifying the parameter (field) value reported when a value cannot be
            calculated from the data source. The default value is 0.0.
        mappingAlgorithm
            A SymbolicConstant specifying the mapping algorithm for target surface, or on mesh
            target model when the parameter value are located at nodes, for example nodal
            temperatures. Possible values are SURFACE and VOLUMETRIC. The default value is SURFACE.
        searchTolType
            A SymbolicConstant specifying searching tolerance type in terms of absolute value or a
            fraction of the average of all element characteristic length in target model region.
            Possible values are ABSOLUTE and RELATIVE. The default value is RELATIVE.
        boundarySearchTol
            A Float specifying the search distance tolerance value on the exterior boundary of
            target model region. Source points within this distance will be included in computing
            the parameter value of target region. This tolerance applies to both surface and
            volumetric mapping. The default value is 0.01.
        neighborhoodSearchTol
            A Float specifying the search distance tolerance value used for distance weighting
            algorithm. Source points within this distance will be included in computing the
            parameter value of target region. This tolerance only applies to surface mapping. The
            default value is 1000000.0.
        negativeNormalSearchTol
            A Float specifying the search distance tolerance value in the negative normal of target
            surface region. Source points within this distance will be included in computing the
            parameter value of target region. This tolerance only applies to surface mapping. The
            default value is 0.15.
        positiveNormalSearchTol
            A Float specifying the search distance tolerance value in the positive normal of target
            surface region. Source points within this distance will be included in computing the
            parameter value of target region. This tolerance only applies to surface mapping. The
            default value is 0.05.
        scaleCoordinates
            A Boolean specifying whether or not to scale the user-supplied coordinate values from
            the point cloud or indicated ODB. The default value is OFF.
        gridPointData
            A sequence of sequences of Floats specifying the point cloud source data of grid format.
            The default value is an empty sequence.
        xyzPointData
            A sequence of sequences of Floats specifying the point cloud source data of XYZ format.
            Each data item is defining the XYZ coordinates of a point and its field value. The
            default value is an empty sequence.
        coordinateScalingFactors
            A sequence of Floats specifying the scaling factors for the global 1, 2 and 3
            directions. The default value is (1.0, 1.0, 1.0).
        localCsys
            None or a DatumCsys object specifying the local coordinate system of the field. If
            **localCsys** = None, the field is defined in the global coordinate system. The default
            value is None.
        description
            A String specifying the description of the field. The default value is an empty string.
        """
        ...
