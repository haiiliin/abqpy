import typing

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from .FieldLocation import FieldLocation
from .FieldLocationArray import FieldLocationArray
from .FieldValueArray import FieldValueArray
from .OdbInstance import OdbInstance
from .OdbSet import OdbSet
from .SectionPoint import SectionPoint
from ..UtilityAndView.abaqusConstants import *


@abaqus_class_doc
class FieldOutput:
    """A :py:class:`~abaqus.Odb.FieldOutput.FieldOutput` object contains field data for a specific output variable.

    .. note:: 
        This object can be accessed by::

            import odbAccess
            session.odbs[name].steps[name].frames[i].fieldOutputs[name]
    """

    #: An Int specifying the dimension of vector or the first dimension (number of rows) of
    #: matrix.
    dim: typing.Optional[int] = None

    #: An Int specifying the second dimension (number of columns) of matrix.
    dim2: typing.Optional[int] = None

    #: A Boolean specifying whether the data are complex.
    isComplex: Boolean = OFF

    #: A :py:class:`~abaqus.Odb.FieldLocationArray.FieldLocationArray` object.
    locations: FieldLocationArray = []

    #: A :py:class:`~abaqus.Odb.FieldValueArray.FieldValueArray` object specifying the order of the objects in the array is determined
    #: by the Abaqus Scripting Interface; see the **data** argument to the addData method for a
    #: description of the order.
    values: typing.Optional[FieldValueArray] = None

    #: A String specifying the output variable name.
    name: str

    #: A String specifying the output variable. Colon (:) should not be used as a part of the
    #: field output description.
    description: str

    #: A SymbolicConstant specifying the output type. Possible values are SCALAR, VECTOR,
    #: TENSOR_3D_FULL, TENSOR_3D_PLANAR, TENSOR_3D_SURFACE, TENSOR_2D_PLANAR, and
    #: TENSOR_2D_SURFACE.
    type: SymbolicConstant

    #: A sequence of Strings specifying the labels for each component of the value. The length
    #: of the sequence must match the type. If **type** = TENSOR, the default value is **name** with
    #: the suffixes ('11', '22', '33', '12', '13', '23'). If **type** = VECTOR, the default value
    #: is **name** with the suffixes ('1', '2', '3'). If **type** = SCALAR, the default value is an
    #: empty sequence.
    componentLabels: tuple = ()

    #: A sequence of SymbolicConstants specifying which invariants should be calculated for
    #: this field. An empty sequence indicates that no invariants are valid for this field.
    #: Possible values
    #: are:MAGNITUDEMISESTRESCAPRESSINV3MAX_PRINCIPALMID_PRINCIPALMIN_PRINCIPALMAX_INPLANE_PRINCIPALMIN_INPLANE_PRINCIPALOUTOFPLANE_PRINCIPALThe
    #: default value is an empty sequence.
    validInvariants: typing.Optional[SymbolicConstant] = None

    #: A Boolean specifying whether the field is an engineering tensor or not. Setting
    #: isEngineeringTensor to true makes a tensor field behave as a strain like quantity where
    #: the off-diagonal components of tensor are halved for invariants computation. This
    #: parameter applies only to tensor field outputs. The default value is OFF.
    isEngineeringTensor: Boolean = OFF

    @abaqus_method_doc
    def __init__(
        self,
        name: str,
        description: str,
        type: SymbolicConstant,
        componentLabels: tuple = (),
        validInvariants: typing.Optional[SymbolicConstant] = None,
        isEngineeringTensor: Boolean = OFF,
    ):
        """This method creates a FieldOutput object.

        .. note:: 
            This function can be accessed by::

                session.odbs[name].steps[name].frames[i].FieldOutput

        Parameters
        ----------
        name
            A String specifying the output variable name.
        description
            A String specifying the output variable. Colon (:) should not be used as a part of the
            field output description.
        type
            A SymbolicConstant specifying the output type. Possible values are SCALAR, VECTOR,
            TENSOR_3D_FULL, TENSOR_3D_PLANAR, TENSOR_3D_SURFACE, TENSOR_2D_PLANAR, and
            TENSOR_2D_SURFACE.
        componentLabels
            A sequence of Strings specifying the labels for each component of the value. The length
            of the sequence must match the type. If **type** = TENSOR, the default value is **name** with
            the suffixes ('11', '22', '33', '12', '13', '23'). If **type** = VECTOR, the default value
            is **name** with the suffixes ('1', '2', '3'). If **type** = SCALAR, the default value is an
            empty sequence.
        validInvariants
            A sequence of SymbolicConstants specifying which invariants should be calculated for
            this field. An empty sequence indicates that no invariants are valid for this field.
            Possible values
            are:MAGNITUDEMISESTRESCAPRESSINV3MAX_PRINCIPALMID_PRINCIPALMIN_PRINCIPALMAX_INPLANE_PRINCIPALMIN_INPLANE_PRINCIPALOUTOFPLANE_PRINCIPALThe
            default value is an empty sequence.
        isEngineeringTensor
            A Boolean specifying whether the field is an engineering tensor or not. Setting
            isEngineeringTensor to true makes a tensor field behave as a strain like quantity where
            the off-diagonal components of tensor are halved for invariants computation. This
            parameter applies only to tensor field outputs. The default value is OFF.

        Returns
        -------
        FieldOutput
            A :py:class:`~abaqus.Odb.FieldOutput.FieldOutput` object.
        """
        ...

    @abaqus_method_doc
    def __init__(self, field: "FieldOutput", name: str = "", description: str = ""):
        """This method creates a FieldOutput object from an existing FieldOutput object of the same
        output database.

        .. note:: 
            This function can be accessed by::

                session.odbs[name].steps[name].frames[i].FieldOutput

        Parameters
        ----------
        field
            A :py:class:`~abaqus.Odb.FieldOutput.FieldOutput` object.
        name
            A String specifying the name of the FieldOutput object.
        description
            A String specifying the output variable. Colon (:) should not be used as a part of the
            field output description.

        Returns
        -------
        FieldOutput
            A :py:class:`~abaqus.Odb.FieldOutput.FieldOutput` object.
        """
        ...

    @abaqus_method_doc
    def __init__(self, *args, **kwargs):
        ...

    @typing.overload
    def addData(
        self,
        position: SymbolicConstant,
        instance: OdbInstance,
        labels: tuple,
        data: tuple,
        sectionPoint: typing.Optional[SectionPoint] = None,
        localCoordSystem: tuple = (),
    ):
        """This method adds data to a FieldOutput object.

        Parameters
        ----------
        position
            A SymbolicConstant specifying the position of the output. Possible values are:

            - NODAL, specifying the values calculated at the nodes.
            - INTEGRATION_POINT, specifying the values calculated at the integration points.
            - ELEMENT_NODAL, specifying the values obtained by extrapolating results calculated at
              the integration points.
            - CENTROID, specifying the value at the centroid obtained by extrapolating results
              calculated at the integration points.
            - ELEMENT_FACE_INTEGRATION_POINT, specifying the values calculated at the element face
              integration points.
            - SURFACE_INTEGRATION_POINT, specifying the values calculated at the surface integration
              points. Selecting this value prompts the Visualization module to calculate the sum of
            the values at the ELEMENT_FACE_INTEGRATION_POINT position from multiple surfaces.
        instance
            An :py:class:`~abaqus.Odb.OdbInstance.OdbInstance` object specifying the namespace for labels.
        labels
            A sequence of Ints specifying the labels of the nodes or elements where the values in
            **data** are located. For better performance, the node or element labels are preferred to
            be sorted in ascending order and must be specified in the same order as the values
            provided for the **data** argument.
        data
            A sequence of sequences of Floats specifying the data values for the specified
            **position**, **instance**, and **labels**. The values must be given in the correct order.
            Element nodal data follow the order of nodal connectivity defined in the Abaqus
            documentation. Integration point data follow the order defined in the Abaqus
            documentation. Section point data for beams and shells follow the convention given in
            the Abaqus documentation. For more information, see the Abaqus Elements Guide. These
            data create FieldValue objects internally.
        sectionPoint
            A :py:class:`~abaqus.Odb.SectionPoint.SectionPoint` object specifying the location in the section. Although **sectionPoint** is
            an optional argument to the addData method, omitting the argument does have consequences
            for visualization. If you omit the argument when you are writing field output data for a
            shell or a beam, you cannot subsequently select the section point to display when you
            are displaying the field output data using the Visualization module.
        localCoordSystem
            The **localCoordSystem** parameter can be specified using either of the following:A
            sequence of sequences of Floats specifying the 3 × 3 matrix of direction cosines of the
            local coordinate system. This argument is available only for fields with type=TENSOR or
            VECTOR.A sequence of matrices of floats specifying the direction cosines of the local
            coordinates systems, where the sequence is the same length as **data**. If
            **localCoordSystem** is a matrix, a different local coordinate system applies to each data
            value.User supplied values of localCoordSystem are transposed before storing in the
            database.

        Raises
        ------
        odbException: Transformation not allowed for scalar data.
            The addData method throws many exceptions of type odbException. For example, if the
            local coordinate system is specified for scalar data
        """
        ...

    @typing.overload
    @abaqus_method_doc
    def addData(self, field: "FieldOutput"):
        """This method adds the data from a field created using the getSubset method and
        mathematical operators to the database. The user must create a field to contain the new
        data and then use the addData method to assign the data from the fields.

        Parameters
        ----------
        field
            A :py:class:`~abaqus.Odb.FieldOutput.FieldOutput` object specifying the data to add.

        Raises
        ------
        odbException: Transformation not allowed for scalar data.
            The addData method throws many exceptions of type odbException. For example, if the
            local coordinate system is specified for scalar data
        """
        ...

    @typing.overload
    @abaqus_method_doc
    def addData(
        self,
        position: SymbolicConstant,
        set: OdbSet,
        data: tuple,
        sectionPoint: typing.Optional[SectionPoint] = None,
        conjugateData: typing.Optional[float] = None,
    ):
        """This method adds data to a FieldOutput object.

        Parameters
        ----------
        position
            A SymbolicConstant specifying the position of the output. Possible values are:NODAL,
            specifying the values calculated at the nodes.INTEGRATION_POINT, specifying the values
            calculated at the integration points.ELEMENT_NODAL, specifying the values obtained by
            extrapolating results calculated at the integration points.CENTROID, specifying the
            value at the centroid obtained by extrapolating results calculated at the integration
            points.ELEMENT_FACE_INTEGRATION_POINT, specifying the values calculated at the element
            face integration points.SURFACE_INTEGRATION_POINT, specifying the values calculated at
            the surface integration points. Selecting this value prompts the Visualization module to
            calculate the sum of the values at the ELEMENT_FACE_INTEGRATION_POINT position from
            multiple surfaces.
        set
            An :py:class:`~abaqus.Odb.OdbSet.OdbSet` object specifying the instance-level set defining the region for addData. The
            set must be defined in the same output database as the output database into which the
            new field output data is being written. For better performance, the node or element
            labels in the set are preferred to be sorted in ascending order and must be specified in
            the same order as the values provided for the **data** argument.
        data
            A sequence of sequences of Floats specifying the data values for the specified position
            and labels in the set. Each row of data provides the value at one unique position. The
            width of each row should match the number of required components for the data. The
            values must be given in the order that matches the ordering of labels in the set.The
            order of the element nodal data, integration point data, and section point data for
            beams and shells follows the conventions defined in the Abaqus Elements Guide.
        sectionPoint
            A :py:class:`~abaqus.Odb.SectionPoint.SectionPoint` object specifying the location in the section. Although*sectionPoint* is
            an optional argument to theaddData method, omitting the argument does have consequences
            for visualization. If you omit the argument when you are writing field output data for a
            shell or a beam, you cannot subsequently select the section point to display when you
            are displaying the field output data using the Visualization module.
        conjugateData
            An odb_SequenceSequenceFloat object specifying the imaginary data values for the
            specified position, instance, and labels. You must provide this data when you add
            complex fields to the output database. The order of the values follows the conventions
            defined in the Abaqus Elements Guide.

        Raises
        ------
        odbException: Entities from multiple instances present in set
            If you specify an odbSet containing entities from multiple instances
        dbException: Transformation not allowed for scalar data
            The addData method throws many exceptions of type odbException. For example, if the
            local coordinate system is specified for scalar data
        """
        ...

    @abaqus_method_doc
    def addData(self, *args, **kwargs):
        ...

    @typing.overload
    def getScalarField(self, invariant: SymbolicConstant):
        """This method generates a scalar field containing the extracted component or calculated
        invariant values. The new field will hold values for the same nodes or elements as the
        parent field. Abaqus will perform this operation on only the real part of the
        FieldOutput object. The operation is not performed on the conjugate data (the imaginary
        portion of a complex result).

        Parameters
        ----------
        invariant
            A SymbolicConstant specifying the invariant. Possible values areMAGNITUDE, MISES,
            TRESCA, PRESS, INV3, MAX_PRINCIPAL, MID_PRINCIPAL, MIN_PRINCIPAL, MAX_INPLANE_PRINCIPAL,
            MIN_INPLANE_PRINCIPAL, and OUTOFPLANE_PRINCIPAL.

        Returns
        -------
        FieldOutput
            A FieldOutput object.
        """
        ...

    @typing.overload
    @abaqus_method_doc
    def getScalarField(self, componentLabel: str):
        """This method generates a scalar field containing the extracted component or calculated
        invariant values. The new field will hold values for the same nodes or elements as the
        parent field. Abaqus will perform this operation on only the real part of the
        FieldOutput object. The operation is not performed on the conjugate data (the imaginary
        portion of a complex result).

        Parameters
        ----------
        componentLabel
            A String specifying the component label, such as “S11”.

        Returns
        -------
        FieldOutput
            A :py:class:`~abaqus.Odb.FieldOutput.FieldOutput` object.
        """
        ...

    @abaqus_method_doc
    def getScalarField(self, *args, **kwargs):
        ...

    @typing.overload
    def getSubset(self, position: typing.Optional[SymbolicConstant] = None, readOnly: Boolean = OFF):
        """A :py:class:`~abaqus.Odb.FieldOutput.FieldOutput` object with a subset of the field values.

        Parameters
        ----------
        position
            **position**
            A SymbolicConstant specifying the position of the output in the element. Possible values
            are:
            
            - NODAL, specifying the values calculated at the nodes.
            - INTEGRATION_POINT, specifying the values calculated at the integration points.
            - ELEMENT_NODAL, specifying the values obtained by extrapolating results calculated at
              the integration points.
            - CENTROID, specifying the value at the centroid obtained by extrapolating results
              calculated at the integration points.
              If the requested field values are not found in the output database at the specified
              ELEMENT_NODAL or CENTROID positions, they are extrapolated from the field data at the
              INTEGRATION_POINT position for the entire field region. If the field values are found at
              the specified positions, only these field values are returned without any extrapolation.
              This could potentially be only for a subset of the field region, depending on the output
              request.
        readOnly
            A Boolean specifying whether the extrapolated data returned by this call is written to
            the output database. The default value is OFF.

        Returns
        -------
        FieldOutput
            A :py:class:`~abaqus.Odb.FieldOutput.FieldOutput` object.
        """
        ...

    @typing.overload
    @abaqus_method_doc
    def getSubset(self, region: str = ""):
        """A :py:class:`~abaqus.Odb.FieldOutput.FieldOutput` object with a subset of the field values.

        Parameters
        ----------
        region
            An OdbSet specifying the region for which to extract values. For better performance, the
            node or element labels in the sets are preferred to be sorted in ascending order.

        Returns
        -------
        FieldOutput
            A :py:class:`~abaqus.Odb.FieldOutput.FieldOutput` object.
        """
        ...

    @typing.overload
    @abaqus_method_doc
    def getSubset(self, localCoordSystem: tuple = ()):
        """A :py:class:`~abaqus.Odb.FieldOutput.FieldOutput` object with a subset of the field values.

        Parameters
        ----------
        localCoordSystem
            A sequence of sequences of Floats specifying the 3 × 3 matrix of direction cosines.
            Field values associated with the supplied coordinate system will be extracted.

        Returns
        -------
        FieldOutput
            A :py:class:`~abaqus.Odb.FieldOutput.FieldOutput` object.
        """
        ...

    @typing.overload
    @abaqus_method_doc
    def getSubset(self, sectionPoint: typing.Optional[SectionPoint] = None):
        """A :py:class:`~abaqus.Odb.FieldOutput.FieldOutput` object with a subset of the field values.

        Parameters
        ----------
        sectionPoint
            A :py:class:`~abaqus.Odb.SectionPoint.SectionPoint` object.

        Returns
        -------
        FieldOutput
            A :py:class:`~abaqus.Odb.FieldOutput.FieldOutput` object.
        """
        ...

    @typing.overload
    @abaqus_method_doc
    def getSubset(self, location: FieldLocation = FieldLocation()):
        """A :py:class:`~abaqus.Odb.FieldOutput.FieldOutput` object with a subset of the field values.

        Parameters
        ----------
        location
            A :py:class:`~abaqus.Odb.FieldLocation.FieldLocation` object.

        Returns
        -------
        FieldOutput
            A :py:class:`~abaqus.Odb.FieldOutput.FieldOutput` object.
        """
        ...

    @typing.overload
    @abaqus_method_doc
    def getSubset(self, region: str = ""):
        """A :py:class:`~abaqus.Odb.FieldOutput.FieldOutput` object with a subset of the field values.

        Parameters
        ----------
        region
            An OdbMeshElement specifying the region for which to extract values.

        Returns
        -------
        FieldOutput
            A :py:class:`~abaqus.Odb.FieldOutput.FieldOutput` object.
        """
        ...

    @typing.overload
    @abaqus_method_doc
    def getSubset(self, region: str = ""):
        """A :py:class:`~abaqus.Odb.FieldOutput.FieldOutput` object with a subset of the field values.

        Parameters
        ----------
        region
            An OdbMeshNode specifying the region for which to extract values.

        Returns
        -------
        FieldOutput
            A :py:class:`~abaqus.Odb.FieldOutput.FieldOutput` object.
        """
        ...

    @typing.overload
    @abaqus_method_doc
    def getSubset(self, region: str = ""):
        """A :py:class:`~abaqus.Odb.FieldOutput.FieldOutput` object with a subset of the field values.

        Parameters
        ----------
        region
            An OdbInstance specifying the region for which to extract values.

        Returns
        -------
        FieldOutput
            A :py:class:`~abaqus.Odb.FieldOutput.FieldOutput` object.
        """
        ...

    @typing.overload
    @abaqus_method_doc
    def getSubset(self, elementType: str = ""):
        """A :py:class:`~abaqus.Odb.FieldOutput.FieldOutput` object with a subset of the field values.

        Parameters
        ----------
        elementType
            A String specifying the element type for which to extract values. The string must
            correspond to a valid Abaqus element type.

        Returns
        -------
        FieldOutput
            A :py:class:`~abaqus.Odb.FieldOutput.FieldOutput` object.
        """
        ...

    @abaqus_method_doc
    def getSubset(self, *args, **kwargs):
        ...

    @typing.overload
    def getTransformedField(
        self, datumCsys: str, projected22Axis: typing.Optional[int] = None, projectionTol: str = ""
    ):
        """This method generates a new vector or tensor field containing the transformed component
        values of the parent field. The new field will hold values for the same nodes or
        elements as the parent field. Results will be transformed based on the orientations
        specified by the input DatumCsys object. Abaqus will perform this operation on only the
        real part of the FieldOutput object. The operation is not performed on the conjugate
        data (the imaginary portion of a complex result).

        Parameters
        ----------
        datumCsys
            A valid DatumCsys object designating the coordinate system. Valid systems can be fixed
            or positioned with respect to nodes on the model and can be cartesian, cylindrical, or
            spherical.
        projected22Axis
            An Int specifying which axis of the coordinate system will be projected as the second
            component for local result orientations. Valid values are 1, 2, or 3; the default value
            is 2.
        projectionTol
            A Double specifying the minimum allowable angle (radians) between the specified
            projection axis and the element normal. The next axis will be used for projection if
            this tolerance test fails.

        Returns
        -------
        FieldOutput
            A :py:class:`~abaqus.Odb.FieldOutput.FieldOutput` object.

        Raises
        ------
        odbException: Cannot apply transformation to field containing assembly level nodes
            The getTransformedField method throws an exception if the field contains any assembly
            level nodes.
        """
        ...

    @typing.overload
    @abaqus_method_doc
    def getTransformedField(
        self,
        datumCsys: str,
        deformationField: typing.Optional["FieldOutput"] = None,
        projected22Axis: typing.Optional[int] = None,
        projectionTol: str = "",
    ):
        """This method generates a new vector or tensor field containing the transformed component
        values of the parent field. The new field will hold values for the same nodes or
        elements as the parent field. Results will be transformed based on the orientations
        specified by the input DatumCsys object. Abaqus will perform this operation on only the
        real part of the FieldOutput object. The operation is not performed on the conjugate
        data (the imaginary portion of a complex result).

        Parameters
        ----------
        datumCsys
            A valid DatumCsys object designating the coordinate system. Valid systems can be fixed
            or positioned with respect to nodes on the model and can be cartesian, cylindrical, or
            spherical.
        deformationField
            A :py:class:`~abaqus.Odb.FieldOutput.FieldOutput` object specifying the nodal displacement vectors required by moving
            coordinate systems to determine instantaneous configurations.
        projected22Axis
            An Int specifying which axis of the coordinate system will be projected as the second
            component for local result orientations. Valid values are 1, 2, or 3; the default value
            is 2.
        projectionTol
            A Double specifying the minimum allowable angle (radians) between the specified
            projection axis and the element normal. The next axis will be used for projection if
            this tolerance test fails.

        Returns
        -------
        FieldOutput
            A :py:class:`~abaqus.Odb.FieldOutput.FieldOutput` object.

        Raises
        ------
        odbException: Cannot apply transformation to field containing assembly level nodes
            The getTransformedField method throws an exception if the field contains any assembly
            level nodes.
        """
        ...

    @typing.overload
    @abaqus_method_doc
    def getTransformedField(
        self,
        datumCsys: str,
        deformationField: typing.Optional["FieldOutput"] = None,
        rotationField: typing.Optional["FieldOutput"] = None,
        projected22Axis: typing.Optional[int] = None,
        projectionTol: str = "",
    ):
        """This method generates a new vector or tensor field containing the transformed component
        values of the parent field. The new field will hold values for the same nodes or
        elements as the parent field. Results will be transformed based on the orientations
        specified by the input DatumCsys object. Abaqus will perform this operation on only the
        real part of the FieldOutput object. The operation is not performed on the conjugate
        data (the imaginary portion of a complex result).

        Parameters
        ----------
        datumCsys
            A valid DatumCsys object designating the coordinate system. Valid systems can be fixed
            or positioned with respect to nodes on the model and can be cartesian, cylindrical, or
            spherical.
        deformationField
            A :py:class:`~abaqus.Odb.FieldOutput.FieldOutput` object specifying the nodal displacement vectors required by moving
            coordinate systems to determine instantaneous configurations.
        rotationField
            A :py:class:`~abaqus.Odb.FieldOutput.FieldOutput` object specifying the nodal rotational displacement vectors required by
            moving coordinate systems that follow a 6-dof node, to determine instantaneous
            configurations.
        projected22Axis
            An Int specifying which axis of the coordinate system will be projected as the second
            component for local result orientations. Valid values are 1, 2, or 3; the default value
            is 2.
        projectionTol
            A Double specifying the minimum allowable angle (radians) between the specified
            projection axis and the element normal. The next axis will be used for projection if
            this tolerance test fails.

        Returns
        -------
        FieldOutput
            A :py:class:`~abaqus.Odb.FieldOutput.FieldOutput` object.

        Raises
        ------
        odbException: Cannot apply transformation to field containing assembly level nodes
            The getTransformedField method throws an exception if the field contains any assembly
            level nodes.
        """
        ...

    @abaqus_method_doc
    def getTransformedField(self, *args, **kwargs):
        ...

    def getConnectorFieldXformedToNodeA(self, deformationField: typing.Optional["FieldOutput"] = None):
        """This method generates a new vector field containing the transformed component values of
        the parent connector field to the node A coordinate system. The new field will hold
        values for the same connector elements as the parent field. Some connection types such
        as Axial, Link, Slip Ring, and Radial Thrust require that the deformationField be
        specified.

        Parameters
        ----------
        deformationField
            A :py:class:`~abaqus.Odb.FieldOutput.FieldOutput` object specifying the nodal displacement vectors required by moving
            coordinate systems to determine instantaneous configurations.

        Returns
        -------
        FieldOutput
            A :py:class:`~abaqus.Odb.FieldOutput.FieldOutput` object.

        Raises
        ------
        odbException: Deformation field is required for transforming this connector field.
            The getConnectorFieldXformedToNodeA method throws an exception if the field requires a
            deformationField and the argument is not supplied.
        """
        ...

    @abaqus_method_doc
    def setComponentLabels(self, componentLabels: tuple):
        """This method sets the component labels for the FieldOutput object.

        Parameters
        ----------
        componentLabels
            A sequence of Strings specifying the labels for each component of the value. The length
            of the sequence must match the type. If **type** = TENSOR, the default value is **name** with
            the suffixes ('11', '22', '33', '12', '13', '23'). If **type** = VECTOR, the default value
            is **name** with the suffixes ('1', '2', '3'). If **type** = SCALAR, the default value is an
            empty sequence.
        """
        ...

    @abaqus_method_doc
    def setDataType(self, type: SymbolicConstant):
        """This method sets the data type of a FieldOutput object.

        Parameters
        ----------
        type
            A SymbolicConstant specifying the output type. Possible values are SCALAR, VECTOR,
            TENSOR_3D_FULL, TENSOR_3D_PLANAR, TENSOR_3D_SURFACE, TENSOR_2D_PLANAR, and
            TENSOR_2D_SURFACE.
        """
        ...

    @abaqus_method_doc
    def setValidInvariants(self, validInvariants: SymbolicConstant):
        """This method sets the invariants valid for the FieldOutput object.

        Parameters
        ----------
        validInvariants
            A sequence of SymbolicConstants specifying which invariants should be calculated for
            this field. An empty sequence indicates that no invariants are valid for this field.
            Possible values are:

            - MAGNITUDE
            - MISES
            - TRESCA
            - PRESS
            - INV3
            - MAX_PRINCIPAL
            - MID_PRINCIPAL
            - MIN_PRINCIPAL
            - MAX_INPLANE_PRINCIPAL
            - MIN_INPLANE_PRINCIPAL
            - OUTOFPLANE_PRINCIPAL
            
            The default value is an empty sequence.
        """
        ...
