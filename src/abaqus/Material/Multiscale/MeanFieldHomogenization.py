from typing import Optional
from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from .MeanFieldInclusion import MeanFieldInclusion
from .MeanFieldMatrix import MeanFieldMatrix
from .MeanFieldVoid import MeanFieldVoid
from ...UtilityAndView.abaqusConstants import *


@abaqus_class_doc
class MeanFieldHomogenization:
    """The MeanFieldHomogenization object specifies the multiscale material definition.

    .. note::
        This object can be accessed by::

            import material
            mdb.models[name].materials[name].meanFieldHomogenization
            import odbMaterial
            session.odbs[name].materials[name].meanFieldHomogenization

        The corresponding analysis keywords are:

        - MEAN FIELD HOMOGENIZATION

    .. versionadded:: 2018
        The `MeanFieldHomogenization` class was added.
    """

    @abaqus_method_doc
    def __init__(
        self,
        angleSubdivision: Optional[int] = None,
        formulation: SymbolicConstant = MT,
        isotropization: SymbolicConstant = ALLISO,
        uniformMatrixStrain: SymbolicConstant = NO,
    ):
        """This method creates a MeanFieldHomogenization object.

        .. note::
            This function can be accessed by::

                mdb.models[name].materials[name].MeanFieldHomogenization
                session.odbs[name].materials[name].MeanFieldHomogenization

        Parameters
        ----------
        angleSubdivision
            An Int specifying the number of angle increments used for the discretization of the
            orientation space.
        formulation
            A SymbolicConstant specifying the type of homogenization model. Possible values are MT,
            REUSS, VOIGT, INVERSED_MT, BALANCED, and UNSPECIFIED. The default value is MT.
        isotropization
            A SymbolicConstant specifying the type of isotropization method. Possible values are
            ALLISO, EISO, and PISO. The default value is ALLISO.
        uniformMatrixStrain
            A SymbolicConstant specifying whether the average strain in the matrix is uniform across
            all pseudo-grains. Possible values are NO and YES. The default value is NO.

        Returns
        -------
            A MeanFieldHomogenization object.

        Raises
        ------
        RangeError
        """
        ...

    @abaqus_method_doc
    def MeanFieldInclusion(
        self,
        name: str,
        table: tuple,
        material: str = "",
        isotropizationCoefficient: Optional[float] = None,
        volumeFractionType: SymbolicConstant = UNIFORM,
        volumeFractionFieldName: str = "",
        aspectRatioType: SymbolicConstant = UNIFORM,
        aspectRatioFieldName: str = "",
        orientationTensorType: SymbolicConstant = UNIFORM,
        orientationTensorFieldName: str = "",
        shape: SymbolicConstant = SPHERE,
        direction: Optional[SymbolicConstant] = None,
        strainConcentrationTensor: tuple = (),
        temperatureGradientConcentrationTensor: tuple = (),
    ):
        """This method creates a MeanFieldInclusion object.

        .. note::
            This function can be accessed by::

                mdb.models[name].materials[name].meanFieldHomogenization.MeanFieldInclusion
                session.odbs[name].materials[name].meanFieldHomogenization.MeanFieldInclusion

        Parameters
        ----------
        name
            A String specifying the constituent repository key.
        table
            A sequence of sequences of Floats specifying the items described below.
        material
            A String specifying the name of the material.
        isotropizationCoefficient
            A Float specifying the factor used for scaling the Plastic strain of the constituent
            when calculating the isotropic part of the tangent.
        volumeFractionType
            A SymbolicConstant specifying the type of volume fraction. Possible values are UNIFORM,
            ANALYTICAL_FIELD, and DISCRETE_FIELD. The default value is UNIFORM.
        volumeFractionFieldName
            A String specifying the name of the AnalyticalField object or DiscreteField object.
        aspectRatioType
            A SymbolicConstant specifying the type of aspect ratio. Possible values are UNIFORM,
            ANALYTICAL_FIELD, and DISCRETE_FIELD. The default value is UNIFORM.
        aspectRatioFieldName
            A String specifying the name of the AnalyticalField object or DiscreteField object.
        orientationTensorType
            A SymbolicConstant specifying the type of orientation tensor. Possible values are
            UNIFORM, ANALYTICAL_FIELD, and DISCRETE_FIELD. The default value is UNIFORM.
        orientationTensorFieldName
            A String specifying the name of the AnalyticalField object or DiscreteField object.
        shape
            A SymbolicConstant specifying the type of inclusion shapes. Possible values are SPHERE,
            PROLATE, OBLATE, CYLINDER, PENNY, and ELLIPTIC_CYLINDER. The default value is SPHERE.
        direction
            A SymbolicConstant specifying the type of inclusion direction. Possible values are
            FIXED, RANDOM3D, and ORIENTATION_TENSOR.
        strainConcentrationTensor
            A sequence of Floats defining the 36 components of the strain concentration tensor.
        temperatureGradientConcentrationTensor
            A sequence of Floats defining the 9 components of the temperature gradient concentration
            tensor.

        Returns
        -------
            A MeanFieldInclusion object.

        Raises
        ------
        RangeError
        """
        return MeanFieldInclusion(
            name,
            table,
            material,
            isotropizationCoefficient,
            volumeFractionType,
            volumeFractionFieldName,
            aspectRatioType,
            aspectRatioFieldName,
            orientationTensorType,
            orientationTensorFieldName,
            shape,
            direction,
            strainConcentrationTensor,
            temperatureGradientConcentrationTensor,
        )

    @abaqus_method_doc
    def MeanFieldMatrix(
        self, name: str, material: str = "", isotropizationCoefficient: Optional[float] = None
    ):
        """This method creates a MeanFieldMatrix object.

        .. note::
            This function can be accessed by::

                mdb.models[name].materials[name].meanFieldHomogenization.MeanFieldMatrix
                session.odbs[name].materials[name].meanFieldHomogenization.MeanFieldMatrix

        Parameters
        ----------
        name
            A String specifying the constituent repository key.
        material
            A String specifying the name of the material.
        isotropizationCoefficient
            A Float specifying the factor used for scaling the Plastic strain of the constituent
            when calculating the isotropic part of the tangent.

        Returns
        -------
            A MeanFieldMatrix object.

        Raises
        ------
        RangeError
        """
        return MeanFieldMatrix(name, material, isotropizationCoefficient)

    @abaqus_method_doc
    def MeanFieldVoid(
        self,
        name: str,
        table: tuple,
        material: str = "",
        isotropizationCoefficient: Optional[float] = None,
        volumeFractionType: SymbolicConstant = UNIFORM,
        volumeFractionFieldName: str = "",
        aspectRatioType: SymbolicConstant = UNIFORM,
        aspectRatioFieldName: str = "",
        orientationTensorType: SymbolicConstant = UNIFORM,
        orientationTensorFieldName: str = "",
        shape: SymbolicConstant = SPHERE,
        direction: Optional[SymbolicConstant] = None,
        strainConcentrationTensor: tuple = (),
        temperatureGradientConcentrationTensor: tuple = (),
    ):
        """This method creates a MeanFieldVoid object.

        .. note::
            This function can be accessed by::

                mdb.models[name].materials[name].meanFieldHomogenization.MeanFieldVoid
                session.odbs[name].materials[name].meanFieldHomogenization.MeanFieldVoid

        Parameters
        ----------
        name
            A String specifying the constituent repository key.
        table
            A sequence of sequences of Floats specifying the items described below.
        material
            A String specifying the name of the material.
        isotropizationCoefficient
            A Float specifying the factor used for scaling the Plastic strain of the constituent
            when calculating the isotropic part of the tangent.
        volumeFractionType
            A SymbolicConstant specifying the type of volume fraction. Possible values are UNIFORM,
            ANALYTICAL_FIELD, and DISCRETE_FIELD. The default value is UNIFORM.
        volumeFractionFieldName
            A String specifying the name of the AnalyticalField object or DiscreteField object.
        aspectRatioType
            A SymbolicConstant specifying the type of aspect ratio. Possible values are UNIFORM,
            ANALYTICAL_FIELD, and DISCRETE_FIELD. The default value is UNIFORM.
        aspectRatioFieldName
            A String specifying the name of the AnalyticalField object or DiscreteField object.
        orientationTensorType
            A SymbolicConstant specifying the type of orientation tensor. Possible values are
            UNIFORM, ANALYTICAL_FIELD, and DISCRETE_FIELD. The default value is UNIFORM.
        orientationTensorFieldName
            A String specifying the name of the AnalyticalField object or DiscreteField object.
        shape
            A SymbolicConstant specifying the type of inclusion shapes. Possible values are SPHERE,
            PROLATE, OBLATE, CYLINDER, PENNY, and ELLIPTIC_CYLINDER. The default value is SPHERE.
        direction
            A SymbolicConstant specifying the type of inclusion direction. Possible values are
            FIXED, RANDOM3D, and ORIENTATION_TENSOR.
        strainConcentrationTensor
            A sequence of Floats defining the 36 components of the strain concentration tensor.
        temperatureGradientConcentrationTensor
            A sequence of Floats defining the 9 components of the temperature gradient concentration
            tensor.

        Returns
        -------
            A MeanFieldVoid object.

        Raises
        ------
        RangeError
        """
        return MeanFieldVoid(
            name,
            table,
            material,
            isotropizationCoefficient,
            volumeFractionType,
            volumeFractionFieldName,
            aspectRatioType,
            aspectRatioFieldName,
            orientationTensorType,
            orientationTensorFieldName,
            shape,
            direction,
            strainConcentrationTensor,
            temperatureGradientConcentrationTensor,
        )

    @abaqus_method_doc
    def setValues(self):
        """This method modifies the MeanFieldHomogenization object.

        Raises
        ------
        RangeError
        """
        ...
