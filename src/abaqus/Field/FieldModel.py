from typing import Optional

from typing_extensions import Literal

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from ..Model.ModelBase import ModelBase
from ..UtilityAndView.abaqusConstants import (
    CARTESIAN,
    NODES,
    OFF,
    POINT,
    RELATIVE,
    SURFACE,
    XYPLANE,
    XYZ,
    Boolean,
)
from ..UtilityAndView.abaqusConstants import abaqusConstants as C
from .DataTableArray import DataTableArray
from .DiscreteField import DiscreteField
from .ExpressionField import ExpressionField
from .MappedField import MappedField


@abaqus_class_doc
class FieldModel(ModelBase):
    @abaqus_method_doc
    def DiscreteField(
        self,
        name: str,
        defaultValues: tuple,
        fieldType: Literal[C.PRESCRIBEDCONDITION_DOF, C.SCALAR, C.ORIENTATION],
        location: Literal[C.NODES, C.ELEMENTS] = NODES,
        dataWidth: int = 1,
        data: Optional[DataTableArray] = None,
        description: str = "",
        orientationType: Literal[C.CYLINDRICAL, C.CARTESIAN, C.SPHERICAL] = CARTESIAN,
        partLevelOrientation: Boolean = OFF,
    ) -> DiscreteField:
        """This method creates a DiscreteField object.

        .. note::
            This function can be accessed by::

                mdb.models[name].DiscreteField

        Parameters
        ----------
        name
            A String specifying the repository key.
        defaultValues
            A sequence of Floats specifying a sequence of floats specifying the default values.
        fieldType
            A SymbolicConstant or an Int specifying the type of data represented by this discrete
            field. Possible values are SCALAR, ORIENTATION, and PRESCRIBEDCONDITION_DOF.
        location
            A SymbolicConstant or an Int specifying the location of the domain data. Possible values
            are NODES and ELEMENTS. The default value is NODES.
        dataWidth
            An Int specifying the width of the supplied data. The default value is 1.
        data
            A DataTableArray object.
        description
            A String specifying the description of the field. The default value is an empty string.
        orientationType
            A SymbolicConstant specifying the type of the system being described by a discrete field
            used for an orientation. Possible values are CARTESIAN, CYLINDRICAL, and SPHERICAL. The
            default value is CARTESIAN.
        partLevelOrientation
            A Boolean specifying whether or not the orientations are described in terms of part
            level coordinates. The default value is OFF.

        Returns
        -------
        DiscreteField
            A DiscreteField object.

        Raises
        ------
        AbaqusException
        """
        self.discreteFields[name] = discreteField = DiscreteField(
            name,
            defaultValues,
            fieldType,
            location,
            dataWidth,
            data,
            description,
            orientationType,
            partLevelOrientation,
        )
        return discreteField

    @abaqus_method_doc
    def ExpressionField(
        self, name: str, expression: str, localCsys: Optional[str] = None, description: str = ""
    ) -> ExpressionField:
        """This method creates an ExpressionField object.

        .. note::
            This function can be accessed by::

                mdb.models[name].ExpressionField

        Parameters
        ----------
        name
            A String specifying the repository key.
        expression
            A String specifying the Python expression to evaluate in space. Variables are X, Y, and
            Z; R, Th, and Z; or R, Th, and P based on the selected coordinate system.
        localCsys
            None or a DatumCsys object specifying the local coordinate system of the field. If
            **localCsys** = None, the field is defined in the global coordinate system. The default
            value is None.
        description
            A String specifying the description of the field. The default value is an empty string.

        Returns
        -------
        ExpressionField
            An ExpressionField object.

        Raises
        ------
        TextException
        """
        self.analyticalFields[name] = expressionField = ExpressionField(name, expression, localCsys, description)
        return expressionField

    @abaqus_method_doc
    def MappedField(
        self,
        name: str,
        regionType: Literal[C.MESH, C.POINT, C.ODB] = POINT,
        partLevelData: Boolean = OFF,
        pointDataFormat: Literal[C.XYZ, C.GRID] = XYZ,
        gridPointPlane: Literal[C.XYPLANE, C.YZPLANE, C.XZPLANE] = XYPLANE,
        defaultUnMappedValue: float = 0,
        mappingAlgorithm: Literal[C.SURFACE, C.VOLUMETRIC] = SURFACE,
        searchTolType: Literal[C.RELATIVE, C.ABSOLUTE] = RELATIVE,
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
    ) -> MappedField:
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
            A MappedField object.

        Raises
        ------
        AbaqusException
        """
        self.analyticalFields[name] = mappedField = MappedField(
            name,
            regionType,
            partLevelData,
            pointDataFormat,
            gridPointPlane,
            defaultUnMappedValue,
            mappingAlgorithm,
            searchTolType,
            boundarySearchTol,
            neighborhoodSearchTol,
            negativeNormalSearchTol,
            positiveNormalSearchTol,
            scaleCoordinates,
            gridPointData,
            xyzPointData,
            coordinateScalingFactors,
            localCsys,
            description,
        )
        return mappedField
