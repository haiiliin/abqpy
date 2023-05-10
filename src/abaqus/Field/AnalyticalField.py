from typing import Optional

from typing_extensions import Literal

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from ..Datum.DatumCsys import DatumCsys
from ..UtilityAndView.abaqusConstants import (
    DEFAULT,
    EXTRAPOLATE_COMPUTE_AVERAGE,
    FIELD_OUTPUT,
    FLOAT,
    NONE,
    OFF,
    ON,
    REAL,
    SCALAR,
    UNDEFINED_POSITION,
)
from ..UtilityAndView.abaqusConstants import abaqusConstants as C
from ..UtilityAndView.SymbolicConstant import SymbolicConstant
from .Field import Field
from .OdbMeshRegionData import OdbMeshRegionData


@abaqus_class_doc
class AnalyticalField(Field):
    """The AnalyticalField object is the abstract base type for other AnalyticalField objects. The
    AnalyticalField object has no explicit constructor. The methods and members of the AnalyticalField object
    are common to all objects derived from the AnalyticalField. The AnalyticalField object is derived from the
    Field object.

    .. note::
        This object can be accessed by::

            import fields
            mdb.models[name].analyticalFields[name]
    """

    #: A String specifying the repository key.
    name: str = ""

    #: None or a DatumCsys object specifying the local coordinate system of the field. If
    #: **localCsys** = None, the field is defined in the global coordinate system. The default
    #: value is None.
    localCsys: DatumCsys = DatumCsys()

    #: A String specifying the description of the field. The default value is an empty string.
    description: str = ""

    #: An OdbMeshRegionData object.
    odbMeshRegionData: OdbMeshRegionData = OdbMeshRegionData("", "")

    @abaqus_method_doc
    def OdbMeshRegionData(
        self,
        odbFileName: str,
        variableLabel: str,
        stepIndex: int = 0,
        frameIndex: int = 0,
        outputPosition: Literal[
            C.ELEMENT_NODAL,
            C.ELEMENT_FACE,
            C.WHOLE_ELEMENT,
            C.NODAL,
            C.UNDEFINED_POSITION,
            C.INTEGRATION_POINT,
            C.ELEMENT_CENTROID,
            C.WHOLE_MODEL,
            C.GENERAL_PARTICLE,
            C.WHOLE_PART_INSTANCE,
            C.WHOLE_REGION,
        ] = UNDEFINED_POSITION,
        dataType: Literal[
            C.QUATERNION_3D,
            C.BOOLEAN,
            C.QUATERNION_2D,
            C.TENSOR_2D_SURFACE,
            C.VECTOR,
            C.INTEGER,
            C.TENSOR,
            C.SCALAR,
            C.TENSOR_3D_FULL,
            C.TENSOR_3D_SURFACE,
            C.ENUMERATION,
            C.TENSOR_2D_PLANAR,
            C.TENSOR_3D_PLANAR,
        ] = SCALAR,
        storageType: Literal[C.INTEGER, C.DOUBLE, C.FLOAT, C.BOOLEAN] = FLOAT,
        quantityToPlot: Literal[C.DISCONTINUITIES, C.FIELD_OUTPUT] = FIELD_OUTPUT,
        averageElementOutput: str = OFF,
        useRegionBoundaries: str = OFF,
        regionBoundaries: Literal[C.DISPLAY_GROUPS, C.ODB_REGIONS, C.NONE, C.ELEMENT_SET] = NONE,
        includeFeatureBoundaries: str = ON,
        featureAngle: float = 20,
        averageOnlyDisplayed: str = OFF,
        averagingThreshold: float = 75,
        computeOrder: Literal[
            C.EXTRAPOLATE_COMPUTE,
            C.RAW_DATA,
            C.EXTRAPOLATE_COMPUTE_DISCONTINUITIES,
            C.EXTRAPOLATE_COMPUTE_AVERAGE,
            C.EXTRAPOLATE_AVERAGE_COMPUTE,
        ] = EXTRAPOLATE_COMPUTE_AVERAGE,
        numericForm: Literal[C.COMPLEX_PHASE, C.COMPLEX_MAG_AT_ANGLE, C.REAL, C.IMAGINARY, C.COMPLEX_MAGNITUDE] = REAL,
        complexAngle: float = 0,
        transformationType: SymbolicConstant = DEFAULT,
        sectionPoint: str = "",
        refinementType: Optional[Literal[C.COMPONENT, C.NO_REFINEMENT, C.INVARIANT]] = None,
        refinementLabel: str = "",
        displayOutputPosition: Optional[
            Literal[
                C.ELEMENT_NODAL,
                C.ELEMENT_FACE,
                C.WHOLE_ELEMENT,
                C.NODAL,
                C.INTEGRATION_POINT,
                C.ELEMENT_CENTROID,
                C.WHOLE_MODEL,
                C.GENERAL_PARTICLE,
                C.WHOLE_PART_INSTANCE,
                C.WHOLE_REGION,
            ]
        ] = None,
    ) -> OdbMeshRegionData:
        """This method creates an OdbMeshRegionData object.

        .. note::
            This function can be accessed by::

                mdb.models[name].analyticalFields[name].OdbMeshRegionData

        Parameters
        ----------
        odbFileName
            A String specifying the name of the output database file (including the .odb extension)
            to be read into as the source data. This String can also be the full path to the output
            database file if it is located in another directory.
        variableLabel
            A String specifying the field output variable.
        stepIndex
            An Int specifying the step index. Possible values are 0 ≤ **stepIndex** ≤ (**numSteps** −
            1). The default value is 0.
        frameIndex
            An Int specifying the frame in the specified step. Valid values are 0 ≤ **frameIndex** ≤
            (**numFramesInStep** − 1). The default value is 0.
        outputPosition
            A SymbolicConstant specifying the position where the data is written in the output
            database. Data can be obtained only from the position at which it was written to the
            output database during the analysis. This position should be aligned with the field
            output variable. Possible values are:

            - UNDEFINED_POSITION
            - NODAL
            - INTEGRATION_POINT
            - ELEMENT_FACE
            - ELEMENT_NODAL
            - ELEMENT_CENTROID
            - WHOLE_ELEMENT
            - WHOLE_REGION
            - WHOLE_PART_INSTANCE
            - WHOLE_MODEL
            - GENERAL_PARTICLE

            The default value is UNDEFINED_POSITION.
        dataType
            A SymbolicConstant specifying the data type of the field output variable which should be
            aligned with the variable. Currently only SCALAR is supported. Possible values are:

            - ENUMERATION
            - BOOLEAN
            - INTEGER
            - SCALAR
            - VECTOR
            - QUATERNION_2D
            - QUATERNION_3D
            - TENSOR
            - TENSOR_3D_FULL
            - TENSOR_3D_PLANAR
            - TENSOR_3D_SURFACE
            - TENSOR_2D_PLANAR
            - TENSOR_2D_SURFACE

            The default value is SCALAR.
        storageType
            A SymbolicConstant specifying the storage type of the field output variable which
            should be aligned with the variable. Possible values are FLOAT, DOUBLE, INTEGER, and
            BOOLEAN. The default value is FLOAT.
        quantityToPlot
            A SymbolicConstant specifying the quantity to plot. Currently only FIELD_OUTPUT is
            supported. Possible values are FIELD_OUTPUT and DISCONTINUITIES. The default value is
            FIELD_OUTPUT.
        averageElementOutput
            A Boolean specifying whether to average the element output. The default value is OFF.
        useRegionBoundaries
            A Boolean specifying whether to use region boundaries when averaging. The default
            value is OFF.
        regionBoundaries
            A SymbolicConstant specifying the type of averaging region boundaries. Currently only
            NONE and ODB_REGIONS are supported. Possible values are NONE, ODB_REGIONS, ELEMENT_SET,
            and DISPLAY_GROUPS. The default value is NONE.
        includeFeatureBoundaries
            A Boolean specifying whether to include additional averaging boundaries for shells and
            membranes based on feature edges. The default value is ON.
        featureAngle
            A Float specifying the feature angle to be used when **includeFeatureBoundaries** = ON.
            The default value is 20.0.
        averageOnlyDisplayed
            A Boolean specifying whether to average only values on displayed elements. The default
            value is OFF.
        averagingThreshold
            A Float specifying the nodal averaging threshold percentage. 0 ≤ **averagingThreshold**
            ≤ 100. The default value is 75.0.
        computeOrder
            A SymbolicConstant specifying the order or the computations to be performed on the
            interested field output variable. Possible values are EXTRAPOLATE_AVERAGE_COMPUTE,
            EXTRAPOLATE_COMPUTE_AVERAGE, EXTRAPOLATE_COMPUTE, EXTRAPOLATE_COMPUTE_DISCONTINUITIES,
            and RAW_DATA. The default value is EXTRAPOLATE_COMPUTE_AVERAGE.
        numericForm
            A SymbolicConstant specifying the numeric form in which to display results that
            contain complex numbers. Possible values are COMPLEX_MAGNITUDE, COMPLEX_PHASE, REAL,
            IMAGINARY, and COMPLEX_MAG_AT_ANGLE. The default value is REAL.
        complexAngle
            A Float specifying the angle (in degrees) at which to display results that contain
            complex numbers when **numericForm = COMPLEX_MAG_AT_ANGLE = COMPLEX_MAG_AT_ANGLE**. The
            default value is 0.0.
        transformationType
            A SymbolicConstant specifying the type of the transformation to apply to the output.
            Possible values are DEFAULT, NODAL, ANGULAR, and LAYUP_ORIENTATION. The default is DEFAULT.
        sectionPoint
            A Dictionary with String keys and String values. Each key specifies a region in the
            model; the corresponding value specifies a section point within that region. For
            example::

                sectionPoint = {
                    'shell < MAT > < 7 section points >': 'SPOS, (fraction = 1.0)',
                    'shell < MAT > < 5 section points >': 'SPOS, (fraction = 1.0)',
                }

        refinementType
            A SymbolicConstant specifying the type of the FieldOutput object. Possible values for
            the SymbolicConstant are NO_REFINEMENT, INVARIANT and COMPONENT. Default argument is
            NO_REFINEMENT. **refinementType** is mandetory if **variableLabel** has an INVARIANT or a
            COMPONENT.
        refinementLabel
            A String specifying the Label of FieldOutput object. This is required only if the
            **refinementType** is INVARIANT or COMPONENT.
        displayOutputPosition
            A SymbolicConstant specifying the position from which to obtain the data. Possible
            values are NODAL, INTEGRATION_POINT, ELEMENT_FACE, ELEMENT_NODAL, ELEMENT_CENTROID,
            WHOLE_ELEMENT, WHOLE_REGION, WHOLE_PART_INSTANCE, WHOLE_MODEL, and GENERAL_PARTICLE.

        Returns
        -------
        OdbMeshRegionData
            An OdbMeshRegionData object.

        Raises
        ------
        TextException
        """
        self.odbMeshRegionData = OdbMeshRegionData(
            odbFileName,
            variableLabel,
            stepIndex,
            frameIndex,
            outputPosition,
            dataType,
            storageType,
            quantityToPlot,
            averageElementOutput,
            useRegionBoundaries,
            regionBoundaries,
            includeFeatureBoundaries,
            featureAngle,
            averageOnlyDisplayed,
            averagingThreshold,
            computeOrder,
            numericForm,
            complexAngle,
            transformationType,
            sectionPoint,
            refinementType,
            refinementLabel,
            displayOutputPosition,
        )
        return self.odbMeshRegionData
