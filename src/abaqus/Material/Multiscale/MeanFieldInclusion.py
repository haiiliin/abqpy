from typing_extensions import Literal
from typing import Optional

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from ...UtilityAndView.abaqusConstants import abaqusConstants as C
from ...UtilityAndView.abaqusConstants import SPHERE, UNIFORM


@abaqus_class_doc
class MeanFieldInclusion:
    """The MeanFieldInclusion object specifies the inclusion type multiscale material property.

    .. note::
        This object can be accessed by::

            import material
            mdb.models[name].materials[name].constituents[name]
            import odbMaterial
            session.odbs[name].materials[name].constituents[name]

        The table data for this object are:

        - Volume fraction.
        - Aspect ratio.
        - Components of the direction vector defined in the local coordinate system when **direction** = FIXED.
          Components of the second-order orientation tensor in the local coordinate system when **direction** = ORIENTATION_TENSOR.
        - Etc.

        The corresponding analysis keywords are:

        - CONSTITUENT

    .. versionadded:: 2018
        The `MeanFieldInclusion` class was added.
    """

    @abaqus_method_doc
    def __init__(
        self,
        name: str,
        table: tuple,
        material: str = "",
        isotropizationCoefficient: Optional[float] = None,
        volumeFractionType: Literal[C.DISCRETE_FIELD, C.UNIFORM, C.ANALYTICAL_FIELD] = UNIFORM,
        volumeFractionFieldName: str = "",
        aspectRatioType: Literal[C.DISCRETE_FIELD, C.UNIFORM, C.ANALYTICAL_FIELD] = UNIFORM,
        aspectRatioFieldName: str = "",
        orientationTensorType: Literal[C.DISCRETE_FIELD, C.UNIFORM, C.ANALYTICAL_FIELD] = UNIFORM,
        orientationTensorFieldName: str = "",
        shape: Literal[C.SPHERE, C.PENNY, C.PROLATE, C.OBLATE, C.CYLINDER, C.ELLIPTIC_CYLINDER] = SPHERE,
        direction: Optional[Literal[C.RANDOM3D, C.ORIENTATION_TENSOR, C.FIXED]] = None,
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
        ...

    @abaqus_method_doc
    def setValues(self):
        """This method modifies the MeanFieldInclusion object.

        Raises
        ------
        RangeError
        """
        ...
