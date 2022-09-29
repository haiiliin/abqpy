import typing

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from .AccelerationBC import AccelerationBC
from .AccelerationBCState import AccelerationBCState
from .AccelerationBaseMotionBC import AccelerationBaseMotionBC
from .AccelerationBaseMotionBCState import AccelerationBaseMotionBCState
from .AcousticPressureBC import AcousticPressureBC
from .AcousticPressureBCState import AcousticPressureBCState
from .ConcentrationBC import ConcentrationBC
from .ConcentrationBCState import ConcentrationBCState
from .ConnAccelerationBC import ConnAccelerationBC
from .ConnAccelerationBCState import ConnAccelerationBCState
from .ConnDisplacementBC import ConnDisplacementBC
from .ConnDisplacementBCState import ConnDisplacementBCState
from .ConnVelocityBC import ConnVelocityBC
from .ConnVelocityBCState import ConnVelocityBCState
from .DisplacementBC import DisplacementBC
from .DisplacementBCState import DisplacementBCState
from .DisplacementBaseMotionBC import DisplacementBaseMotionBC
from .DisplacementBaseMotionBCState import DisplacementBaseMotionBCState
from .ElectricPotentialBC import ElectricPotentialBC
from .ElectricPotentialBCState import ElectricPotentialBCState
from .EulerianBC import EulerianBC
from .EulerianBCState import EulerianBCState
from .EulerianMotionBC import EulerianMotionBC
from .EulerianMotionBCState import EulerianMotionBCState
from .FluidCavityPressureBC import FluidCavityPressureBC
from .FluidCavityPressureBCState import FluidCavityPressureBCState
from .MagneticVectorPotentialBC import MagneticVectorPotentialBC
from .MaterialFlowBC import MaterialFlowBC
from .MaterialFlowBCState import MaterialFlowBCState
from .PorePressureBC import PorePressureBC
from .PorePressureBCState import PorePressureBCState
from .RetainedNodalDofsBC import RetainedNodalDofsBC
from .SecondaryBaseBC import SecondaryBaseBC
from .SecondaryBaseBCState import SecondaryBaseBCState
from .SubmodelBC import SubmodelBC
from .SubmodelBCState import SubmodelBCState
from .TemperatureBC import TemperatureBC
from .TemperatureBCState import TemperatureBCState
from .TypeBC import TypeBC
from .VelocityBC import VelocityBC
from .VelocityBCState import VelocityBCState
from .VelocityBaseMotionBC import VelocityBaseMotionBC
from .VelocityBaseMotionBCState import VelocityBaseMotionBCState
from ..Amplitude.Correlation import Correlation
from ..Model.ModelBase import ModelBase
from ..Region.Region import Region
from ..Region.RegionArray import RegionArray
from ..UtilityAndView.abaqusConstants import *


@abaqus_class_doc
class BoundaryConditionModel(ModelBase):
    """Abaqus creates a Model object named `Model-1` when a session is started.

    .. note:: 
        This object can be accessed by::

            mdb.models[name]
    """

    @abaqus_method_doc
    def AccelerationBaseMotionBC(
        self,
        name: str,
        createStepName: str,
        dof: SymbolicConstant,
        amplitudeScaleFactor: float = 1,
        centerOfRotation: tuple = (),
        correlation: typing.Optional[Correlation] = None,
        secondaryBase: str = "",
        useComplex: Boolean = OFF,
        amplitude: str = UNSET,
    ) -> AccelerationBaseMotionBC:
        """This method creates a AccelerationBaseMotionBC object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].AccelerationBaseMotionBC

        Parameters
        ----------
        name
            A String specifying the boundary condition repository key.
        createStepName
            A String specifying the name of the step in which the boundary condition is created.
        dof
            A SymbolicConstant specifying the constrained degree-of-freedom. Possible values for the
            SymbolicConstant are U1, U2, U3, UR1, UR2, UR3. The default value is U1.
        amplitudeScaleFactor
            A Float specifying the scale factor for the amplitude curve. The default value is 1.0.
        centerOfRotation
            A :py:class:`~abaqus.BasicGeometry.ModelDot.ModelDot` object specifying a tuple containing one center of rotation. The default
            value is the global origin. This argument applies only when **dof** = UR1, UR2, or UR3.
        correlation
            A :py:class:`~abaqus.Amplitude.Correlation.Correlation` object.
        secondaryBase
            A String specifying the name of the SecondaryBaseBC object associated with this boundary
            condition. The default value is an empty string.
        useComplex
            A Boolean specifying whether to define the imaginary (out-of-plane) portion of the base
            motion record given by amplitude definition. The default value is OFF.
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
            UNSET should be used if the boundary condition has no amplitude reference. The default
            value is UNSET. You should provide the **amplitude** argument only if it is valid for the
            specified step.

        Returns
        -------
        bc: AccelerationBaseMotionBC
            An :py:class:`~abaqus.BoundaryCondition.AccelerationBaseMotionBC.AccelerationBaseMotionBC` object.
        """
        self.boundaryConditions[name] = boundaryCondition = AccelerationBaseMotionBC(
            name,
            createStepName,
            dof,
            amplitudeScaleFactor,
            centerOfRotation,
            correlation,
            secondaryBase,
            useComplex,
            amplitude,
        )
        self.steps[createStepName].boundaryConditionStates[
            name
        ] = AccelerationBaseMotionBCState()
        return boundaryCondition

    @abaqus_method_doc
    def AccelerationBC(
        self,
        name: str,
        createStepName: str,
        region: Region,
        fieldName: str = "",
        a1: typing.Union[SymbolicConstant, float] = UNSET,
        a2: typing.Union[SymbolicConstant, float] = UNSET,
        a3: typing.Union[SymbolicConstant, float] = UNSET,
        ar1: typing.Union[SymbolicConstant, float] = UNSET,
        ar2: typing.Union[SymbolicConstant, float] = UNSET,
        ar3: typing.Union[SymbolicConstant, float] = UNSET,
        amplitude: str = UNSET,
        localCsys: typing.Optional[str] = None,
        distributionType: SymbolicConstant = UNIFORM,
    ) -> AccelerationBC:
        """This method creates an AccelerationBC object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].AccelerationBC

        Parameters
        ----------
        name
            A String specifying the boundary condition repository key.
        createStepName
            A String specifying the name of the step in which the boundary condition is created.
        region
            A :py:class:`~abaqus.Region.Region.Region` object specifying the region to which the boundary condition is applied.
        fieldName
            A String specifying the name of the AnalyticalField object associated with this boundary
            condition. The **fieldName** argument applies only when **distributionType** = FIELD. The
            default value is an empty string.
        a1
            A Float or a SymbolicConstant specifying the acceleration component in the 1-direction.
            Possible values for the SymbolicConstant are UNSET and SET. The default value is
            UNSET.Note:Although **a1**, **a2**, **a3**, **ar1**, **ar2**, and **ar3** are optional arguments, at
            least one of them must be specified.
        a2
            A Float or a SymbolicConstant specifying the acceleration component in the 2-direction.
            Possible values for the SymbolicConstant are UNSET and SET. The default value is UNSET.
        a3
            A Float or a SymbolicConstant specifying the acceleration component in the 3-direction.
            Possible values for the SymbolicConstant are UNSET and SET. The default value is UNSET.
        ar1
            A Float or a SymbolicConstant specifying the rotational acceleration component about the
            1-direction. Possible values for the SymbolicConstant are UNSET and SET. The default
            value is UNSET.
        ar2
            A Float or a SymbolicConstant specifying the rotational acceleration component about the
            2-direction. Possible values for the SymbolicConstant are UNSET and SET. The default
            value is UNSET.
        ar3
            A Float or a SymbolicConstant specifying the rotational acceleration component about the
            3-direction. Possible values for the SymbolicConstant are UNSET and SET. The default
            value is UNSET.
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
            UNSET should be used if the boundary condition has no amplitude reference. The default
            value is UNSET. You should provide the **amplitude** argument only if it is valid for the
            specified step.
        localCsys
            None or a DatumCsys object specifying the local coordinate system of the boundary
            condition's degrees of freedom. If **localCsys** = None, the degrees of freedom are defined
            in the global coordinate system. The default value is None.
        distributionType
            A SymbolicConstant specifying how the boundary condition is distributed spatially.
            Possible values are UNIFORM, USER_DEFINED, and FIELD. The default value is UNIFORM.

        Returns
        -------
        bc: AccelerationBC
            An :py:class:`~abaqus.BoundaryCondition.AccelerationBC.AccelerationBC` object.
        """
        self.boundaryConditions[name] = boundaryCondition = AccelerationBC(
            name,
            createStepName,
            region,
            fieldName,
            a1,
            a2,
            a3,
            ar1,
            ar2,
            ar3,
            amplitude,
            localCsys,
            distributionType,
        )
        self.steps[createStepName].boundaryConditionStates[name] = AccelerationBCState()
        return boundaryCondition

    @abaqus_method_doc
    def AcousticPressureBC(
        self,
        name: str,
        createStepName: str,
        region: Region,
        fieldName: str = "",
        magnitude: float = 0,
        distributionType: SymbolicConstant = UNIFORM,
        amplitude: str = UNSET,
        fixed: Boolean = OFF,
    ) -> AcousticPressureBC:
        """This method creates a AcousticPressureBC object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].AcousticPressureBC

        Parameters
        ----------
        name
            A String specifying the boundary condition repository key.
        createStepName
            A String specifying the name of the step in which the boundary condition is created.
        region
            A :py:class:`~abaqus.Region.Region.Region` object specifying the region to which the boundary condition is applied.
        fieldName
            A String specifying the name of the AnalyticalField object associated with this boundary
            condition. The **fieldName** argument applies only when **distributionType** = FIELD. The
            default value is an empty string.
        magnitude
            A Float specifying the acoustic pressure magnitude. The default value is 0. The
            **magnitude** argument is optional if **distributionType** = USER_DEFINED.
        distributionType
            A SymbolicConstant specifying how the boundary condition is distributed spatially.
            Possible values are UNIFORM, USER_DEFINED, and FIELD. The default value is UNIFORM.
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
            UNSET should be used if the boundary condition has no amplitude reference. The default
            value is UNSET. You should provide the **amplitude** argument only if it is valid for the
            specified step.
        fixed
            A Boolean specifying whether the boundary condition should remain fixed at the current
            values at the start of the step. The default value is OFF.

        Returns
        -------
        bc: AcousticPressureBC
            An :py:class:`~abaqus.BoundaryCondition.AcousticPressureBC.AcousticPressureBC` object.
        """
        self.boundaryConditions[name] = boundaryCondition = AcousticPressureBC(
            name,
            createStepName,
            region,
            fieldName,
            magnitude,
            distributionType,
            amplitude,
            fixed,
        )
        self.steps[createStepName].boundaryConditionStates[
            name
        ] = AcousticPressureBCState()
        return boundaryCondition

    @abaqus_method_doc
    def ConcentrationBC(
        self,
        name: str,
        createStepName: str,
        region: Region,
        fieldName: str = "",
        magnitude: float = 0,
        distributionType: SymbolicConstant = UNIFORM,
        amplitude: str = UNSET,
        fixed: Boolean = OFF,
    ) -> ConcentrationBC:
        """This method creates a ConcentrationBC object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].ConcentrationBC

        Parameters
        ----------
        name
            A String specifying the boundary condition repository key.
        createStepName
            A String specifying the name of the step in which the boundary condition is created.
        region
            A :py:class:`~abaqus.Region.Region.Region` object specifying the region to which the boundary condition is applied.
        fieldName
            A String specifying the name of the AnalyticalField object associated with this boundary
            condition. The **fieldName** argument applies only when **distributionType** = FIELD. The
            default value is an empty string.
        magnitude
            A Float specifying the concentration magnitude. The default value is 0. The **magnitude**
            argument is optional if **distributionType** = USER_DEFINED.
        distributionType
            A SymbolicConstant specifying how the boundary condition is distributed spatially.
            Possible values are UNIFORM, USER_DEFINED, and FIELD. The default value is UNIFORM.
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
            UNSET should be used if the boundary condition has no amplitude reference. The default
            value is UNSET. You should provide the **amplitude** argument only if it is valid for the
            specified step.
        fixed
            A Boolean specifying whether the boundary condition should remain fixed at the current
            values at the start of the step. The default value is OFF.

        Returns
        -------
        bc: ConcentrationBC
            A :py:class:`~abaqus.BoundaryCondition.ConcentrationBC.ConcentrationBC` object.
        """
        self.boundaryConditions[name] = boundaryCondition = ConcentrationBC(
            name,
            createStepName,
            region,
            fieldName,
            magnitude,
            distributionType,
            amplitude,
            fixed,
        )
        self.steps[createStepName].boundaryConditionStates[
            name
        ] = ConcentrationBCState()
        return boundaryCondition

    @abaqus_method_doc
    def ConnAccelerationBC(
        self,
        name: str,
        createStepName: str,
        region: str = "",
        fastenerName: str = "",
        fastenerSetName: str = "",
        a1: typing.Union[SymbolicConstant, float] = UNSET,
        a2: typing.Union[SymbolicConstant, float] = UNSET,
        a3: typing.Union[SymbolicConstant, float] = UNSET,
        ar1: typing.Union[SymbolicConstant, float] = UNSET,
        ar2: typing.Union[SymbolicConstant, float] = UNSET,
        ar3: typing.Union[SymbolicConstant, float] = UNSET,
        amplitude: str = UNSET,
        distributionType: SymbolicConstant = UNIFORM,
    ) -> ConnAccelerationBC:
        """This method creates an ConnAccelerationBC object on a wire region. Alternatively, the
        boundary condition may also be applied to a wire set referenced from an assembled
        fastener template model.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].ConnAccelerationBC

        Parameters
        ----------
        name
            A String specifying the boundary condition repository key.
        createStepName
            A String specifying the name of the step in which the boundary condition is created.
        region
            The wire region to which the boundary condition is applied. This argument is not valid
            when **fastenerName** and **fastenerSetName** are specified.
        fastenerName
            A String specifying the name of the assembled fastener to which the boundary condition
            will be applied. This argument is not valid when **region** is specified. When this
            argument is specified, **fastenerSetName** must also be specified. The default value is an
            empty string.
        fastenerSetName
            A String specifying the assembled fastener template model set to which the boundary
            condition will be applied. This argument is not valid when **region** is specified. When
            this argument is specified, **fastenerName** must also be specified. The default value is
            an empty string.
        a1
            A Float or a SymbolicConstant specifying the acceleration component in the connector's
            local 1-direction. Possible values for the SymbolicConstant are UNSET and SET. The
            default value is UNSET.Note:Although **a1**, **a2**, **a3**, **ar1**, **ar2**, and **ar3** are
            optional arguments, at least one of them must be specified.
        a2
            A Float or a SymbolicConstant specifying the acceleration component in the connector's
            local 2-direction. Possible values for the SymbolicConstant are UNSET and SET. The
            default value is UNSET.
        a3
            A Float or a SymbolicConstant specifying the acceleration component in the connector's
            local 3-direction. Possible values for the SymbolicConstant are UNSET and SET. The
            default value is UNSET.
        ar1
            A Float or a SymbolicConstant specifying the rotational acceleration component in the
            connector's local 4-direction. Possible values for the SymbolicConstant are UNSET and
            SET. The default value is UNSET.
        ar2
            A Float or a SymbolicConstant specifying the rotational acceleration component in the
            connector's local 5-direction. Possible values for the SymbolicConstant are UNSET and
            SET. The default value is UNSET.
        ar3
            A Float or a SymbolicConstant specifying the rotational acceleration component in the
            connector's local 6-direction. Possible values for the SymbolicConstant are UNSET and
            SET. The default value is UNSET.
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
            UNSET should be used if the boundary condition has no amplitude reference. The default
            value is UNSET. You should provide the **amplitude** argument only if it is valid for the
            specified step.
        distributionType
            A SymbolicConstant specifying how the boundary condition is distributed spatially.
            Possible values are UNIFORM and USER_DEFINED. The default value is UNIFORM.

        Returns
        -------
        bc: ConnAccelerationBC
            A :py:class:`~abaqus.BoundaryCondition.ConnAccelerationBC.ConnAccelerationBC` object.
        """
        self.boundaryConditions[name] = boundaryCondition = ConnAccelerationBC(
            name,
            createStepName,
            region,
            fastenerName,
            fastenerSetName,
            a1,
            a2,
            a3,
            ar1,
            ar2,
            ar3,
            amplitude,
            distributionType,
        )
        self.steps[createStepName].boundaryConditionStates[
            name
        ] = ConnAccelerationBCState()
        return boundaryCondition

    @abaqus_method_doc
    def ConnDisplacementBC(
        self,
        name: str,
        createStepName: str,
        region: str = "",
        fastenerName: str = "",
        fastenerSetName: str = "",
        u1: typing.Union[SymbolicConstant, float] = UNSET,
        u2: typing.Union[SymbolicConstant, float] = UNSET,
        u3: typing.Union[SymbolicConstant, float] = UNSET,
        ur1: typing.Union[SymbolicConstant, float] = UNSET,
        ur2: typing.Union[SymbolicConstant, float] = UNSET,
        ur3: typing.Union[SymbolicConstant, float] = UNSET,
        fixed: Boolean = OFF,
        amplitude: str = UNSET,
        distributionType: SymbolicConstant = UNIFORM,
        buckleCase: SymbolicConstant = NOT_APPLICABLE,
    ) -> ConnDisplacementBC:
        """This method creates a ConnDisplacementBC object on a wire region. Alternatively, the
        boundary condition may also be applied to a wire set referenced from an assembled
        fastener template model.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].ConnDisplacementBC

        Parameters
        ----------
        name
            A String specifying the boundary condition repository key.
        createStepName
            A String specifying the name of the step in which the boundary condition is created.
        region
            The wire region to which the boundary condition is applied. This argument is not valid
            when **fastenerName** and **fastenerSetName** are specified.
        fastenerName
            A String specifying the name of the assembled fastener to which the boundary condition
            will be applied. This argument is not valid when **region** is specified. When this
            argument is specified, **fastenerSetName** must also be specified. The default value is an
            empty string.
        fastenerSetName
            A String specifying the assembled fastener template model set to which the boundary
            condition will be applied. This argument is not valid when **region** is specified. When
            this argument is specified, **fastenerName** must also be specified. The default value is
            an empty string.
        u1
            A Float, a Complex, or a SymbolicConstant specifying the displacement component in the
            connector's local 1-direction. Possible values for the SymbolicConstant are UNSET and
            SET. The default value is UNSET.Note:Although **u1**, **u2**, **u3**, **ur1**, **ur2**, and **ur3**
            are optional arguments, at least one of them must be specified.
        u2
            A Float, a Complex, or a SymbolicConstant specifying the displacement component in the
            connector's local 2-direction. Possible values for the SymbolicConstant are UNSET and
            SET. The default value is UNSET.
        u3
            A Float, a Complex, or a SymbolicConstant specifying the displacement component in the
            connector's local 3-direction. Possible values for the SymbolicConstant are UNSET and
            SET. The default value is UNSET.
        ur1
            A Float, a Complex, or a SymbolicConstant specifying the rotational component in the
            connector's local 4-direction. Possible values for the SymbolicConstant are UNSET and
            SET. The default value is UNSET.
        ur2
            A Float, a Complex, or a SymbolicConstant specifying the rotational component in the
            connector's local 5-direction. Possible values for the SymbolicConstant are UNSET and
            SET. The default value is UNSET.
        ur3
            A Float, a Complex, or a SymbolicConstant specifying the rotational component in the
            connector's local 6-direction. Possible values for the SymbolicConstant are UNSET and
            SET. The default value is UNSET.
        fixed
            A Boolean specifying whether the boundary condition should remain fixed at the current
            values at the start of the step. The default value is OFF.
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
            UNSET should be used if the boundary condition has no amplitude reference. The default
            value is UNSET. You should provide the **amplitude** argument only if it is valid for the
            specified step.
        distributionType
            A SymbolicConstant specifying how the boundary condition is distributed spatially.
            Possible values are UNIFORM and USER_DEFINED. The default value is UNIFORM.
        buckleCase
            A SymbolicConstant specifying how the boundary condition is defined in a BUCKLE
            analysis. Possible values are NOT_APPLICABLE, STRESS_PERTURBATION, BUCKLING_MODES, and
            PERTURBATION_AND_BUCKLING. The default value is NOT_APPLICABLE.

        Returns
        -------
        bc: ConnDisplacementBC
            A :py:class:`~abaqus.BoundaryCondition.ConnDisplacementBC.ConnDisplacementBC` object.
        """
        self.boundaryConditions[name] = boundaryCondition = ConnDisplacementBC(
            name,
            createStepName,
            region,
            fastenerName,
            fastenerSetName,
            u1,
            u2,
            u3,
            ur1,
            ur2,
            ur3,
            fixed,
            amplitude,
            distributionType,
            buckleCase,
        )
        self.steps[createStepName].boundaryConditionStates[
            name
        ] = ConnDisplacementBCState()
        return boundaryCondition

    @abaqus_method_doc
    def ConnVelocityBC(
        self,
        name: str,
        createStepName: str,
        region: str = "",
        fastenerName: str = "",
        fastenerSetName: str = "",
        v1: typing.Union[SymbolicConstant, float] = UNSET,
        v2: typing.Union[SymbolicConstant, float] = UNSET,
        v3: typing.Union[SymbolicConstant, float] = UNSET,
        vr1: typing.Union[SymbolicConstant, float] = UNSET,
        vr2: typing.Union[SymbolicConstant, float] = UNSET,
        vr3: typing.Union[SymbolicConstant, float] = UNSET,
        amplitude: str = UNSET,
        distributionType: SymbolicConstant = UNIFORM,
    ) -> ConnVelocityBC:
        """This method creates a ConnVelocityBC object on a wire region. Alternatively, the
        boundary condition may also be applied to a wire set referenced from an assembled
        fastener template model.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].ConnVelocityBC

        Parameters
        ----------
        name
            A String specifying the boundary condition repository key.
        createStepName
            A String specifying the name of the step in which the boundary condition is created.
        region
            The wire region to which the boundary condition is applied. This argument is not valid
            when **fastenerName** and **fastenerSetName** are specified.
        fastenerName
            A String specifying the name of the assembled fastener to which the boundary condition
            will be applied. This argument is not valid when **region** is specified. When this
            argument is specified, **fastenerSetName** must also be specified. The default value is an
            empty string.
        fastenerSetName
            A String specifying the assembled fastener template model set to which the boundary
            condition will be applied. This argument is not valid when **region** is specified. When
            this argument is specified, **fastenerName** must also be specified. The default value is
            an empty string.
        v1
            A Float or a SymbolicConstant specifying the velocity component in the connector's local
            1-direction. Possible values for the SymbolicConstant are UNSET and SET. The default
            value is UNSET.Note:Although **v1**, **v2**, **v3**, **vr1**, **vr2**, and **vr3** are optional
            arguments, at least one of them must be specified.
        v2
            A Float or a SymbolicConstant specifying the velocity component in the connector's local
            2-direction. Possible values for the SymbolicConstant are UNSET and SET. The default
            value is UNSET.
        v3
            A Float or a SymbolicConstant specifying the velocity component in the connector's local
            3-direction. Possible values for the SymbolicConstant are UNSET and SET. The default
            value is UNSET.
        vr1
            A Float or a SymbolicConstant specifying the rotational velocity component in the
            connector's local 4-direction. Possible values for the SymbolicConstant are UNSET and
            SET. The default value is UNSET.
        vr2
            A Float or a SymbolicConstant specifying the rotational velocity component in the
            connector's local 5-direction. Possible values for the SymbolicConstant are UNSET and
            SET. The default value is UNSET.
        vr3
            A Float or a SymbolicConstant specifying the rotational velocity component in the
            connector's local 6-direction. Possible values for the SymbolicConstant are UNSET and
            SET. The default value is UNSET.
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
            UNSET should be used if the boundary condition has no amplitude reference. The default
            value is UNSET. You should provide the **amplitude** argument only if it is valid for the
            specified step.
        distributionType
            A SymbolicConstant specifying how the boundary condition is distributed spatially.
            Possible values are UNIFORM and USER_DEFINED. The default value is UNIFORM.

        Returns
        -------
        bc: ConnVelocityBC
            A :py:class:`~abaqus.BoundaryCondition.ConnVelocityBC.ConnVelocityBC` object.
        """
        self.boundaryConditions[name] = boundaryCondition = ConnVelocityBC(
            name,
            createStepName,
            region,
            fastenerName,
            fastenerSetName,
            v1,
            v2,
            v3,
            vr1,
            vr2,
            vr3,
            amplitude,
            distributionType,
        )
        self.steps[createStepName].boundaryConditionStates[name] = ConnVelocityBCState()
        return boundaryCondition

    @abaqus_method_doc
    def DisplacementBaseMotionBC(
        self,
        name: str,
        createStepName: str,
        dof: SymbolicConstant,
        amplitudeScaleFactor: float = 1,
        centerOfRotation: tuple = (),
        correlation: typing.Optional[Correlation] = None,
        secondaryBase: str = "",
        useComplex: Boolean = OFF,
        amplitude: str = UNSET,
    ) -> DisplacementBaseMotionBC:
        """This method creates a DisplacementBaseMotionBC object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].DisplacementBaseMotionBC

        Parameters
        ----------
        name
            A String specifying the boundary condition repository key.
        createStepName
            A String specifying the name of the step in which the boundary condition is created.
        dof
            A SymbolicConstant specifying the constrained degree-of-freedom. Possible values for the
            SymbolicConstant are U1, U2, U3, UR1, UR2, UR3. The default value is U1.
        amplitudeScaleFactor
            A Float specifying the scale factor for the amplitude curve. The default value is 1.0.
        centerOfRotation
            A :py:class:`~abaqus.BasicGeometry.ModelDot.ModelDot` object specifying a tuple containing one center of rotation. The default
            value is the global origin. This argument applies only when **dof** = UR1, UR2, or UR3.
        correlation
            A :py:class:`~abaqus.Amplitude.Correlation.Correlation` object.
        secondaryBase
            A String specifying the name of the SecondaryBaseBC object associated with this boundary
            condition. The default value is an empty string.
        useComplex
            A Boolean specifying whether to define the imaginary (out-of-plane) portion of the base
            motion record given by amplitude definition. The default value is OFF.
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
            UNSET should be used if the boundary condition has no amplitude reference. The default
            value is UNSET. You should provide the **amplitude** argument only if it is valid for the
            specified step.

        Returns
        -------
        bc: DisplacementBaseMotionBC
            A :py:class:`~abaqus.BoundaryCondition.DisplacementBaseMotionBC.DisplacementBaseMotionBC` object.
        """
        self.boundaryConditions[name] = boundaryCondition = DisplacementBaseMotionBC(
            name,
            createStepName,
            dof,
            amplitudeScaleFactor,
            centerOfRotation,
            correlation,
            secondaryBase,
            useComplex,
            amplitude,
        )
        self.steps[createStepName].boundaryConditionStates[
            name
        ] = DisplacementBaseMotionBCState()
        return boundaryCondition

    @abaqus_method_doc
    def DisplacementBC(
        self,
        name: str,
        createStepName: str,
        region: Region,
        fieldName: str = "",
        u1: typing.Union[SymbolicConstant, float] = UNSET,
        u2: typing.Union[SymbolicConstant, float] = UNSET,
        u3: typing.Union[SymbolicConstant, float] = UNSET,
        ur1: typing.Union[SymbolicConstant, float] = UNSET,
        ur2: typing.Union[SymbolicConstant, float] = UNSET,
        ur3: typing.Union[SymbolicConstant, float] = UNSET,
        fixed: Boolean = OFF,
        amplitude: str = UNSET,
        distributionType: SymbolicConstant = UNIFORM,
        localCsys: typing.Optional[str] = None,
        buckleCase: SymbolicConstant = NOT_APPLICABLE,
    ) -> DisplacementBC:
        """This method creates a DisplacementBC object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].DisplacementBC

        Parameters
        ----------
        name
            A String specifying the boundary condition repository key.
        createStepName
            A String specifying the name of the step in which the boundary condition is created.
        region
            A :py:class:`~abaqus.Region.Region.Region` object specifying the region to which the boundary condition is applied.
        fieldName
            A String specifying the name of the AnalyticalField or DiscreteField object associated
            with this boundary condition. The **fieldName** argument applies only when
            **distributionType** = FIELD or **distributionType** = DISCRETE_FIELD. The default value is an
            empty string.
        u1
            A Float, a Complex, or a SymbolicConstant specifying the displacement component in the
            1-direction. Possible values for the SymbolicConstant are UNSET and SET. The default
            value is UNSET.Note:Although **u1**, **u2**, **u3**, **ur1**, **ur2**, and **ur3** are optional
            arguments, at least one of them must be specified.
        u2
            A Float, a Complex, or a SymbolicConstant specifying the displacement component in the
            2-direction. Possible values for the SymbolicConstant are UNSET and SET. The default
            value is UNSET.
        u3
            A Float, a Complex, or a SymbolicConstant specifying the displacement component in the
            3-direction. Possible values for the SymbolicConstant are UNSET and SET. The default
            value is UNSET.
        ur1
            A Float, a Complex, or a SymbolicConstant specifying the rotational displacement
            component about the 1-direction. Possible values for the SymbolicConstant are UNSET and
            SET. The default value is UNSET.
        ur2
            A Float, a Complex, or a SymbolicConstant specifying the rotational displacement
            component about the 2-direction. Possible values for the SymbolicConstant are UNSET and
            SET. The default value is UNSET.
        ur3
            A Float, a Complex, or a SymbolicConstant specifying the rotational displacement
            component about the 3-direction. Possible values for the SymbolicConstant are UNSET and
            SET. The default value is UNSET.
        fixed
            A Boolean specifying whether the boundary condition should remain fixed at the current
            values at the start of the step. The default value is OFF.
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
            UNSET should be used if the boundary condition has no amplitude reference. The default
            value is UNSET. You should provide the **amplitude** argument only if it is valid for the
            specified step.
        distributionType
            A SymbolicConstant specifying how the boundary condition is distributed spatially.
            Possible values are UNIFORM, USER_DEFINED, FIELD, and DISCRETE_FIELD. The default value
            is UNIFORM.
        localCsys
            None or a DatumCsys object specifying the local coordinate system of the boundary
            condition's degrees of freedom. If **localCsys** = None, the degrees of freedom are defined
            in the global coordinate system. The default value is None.
        buckleCase
            A SymbolicConstant specifying how the boundary condition is defined in a BUCKLE
            analysis. Possible values are NOT_APPLICABLE, STRESS_PERTURBATION, BUCKLING_MODES, and
            PERTURBATION_AND_BUCKLING. The default value is NOT_APPLICABLE.

        Returns
        -------
        bc: DisplacementBC
            A :py:class:`~abaqus.BoundaryCondition.DisplacementBC.DisplacementBC` object
        """
        self.boundaryConditions[name] = boundaryCondition = DisplacementBC(
            name,
            createStepName,
            region,
            fieldName,
            u1,
            u2,
            u3,
            ur1,
            ur2,
            ur3,
            fixed,
            amplitude,
            distributionType,
            localCsys,
            buckleCase,
        )
        self.steps[createStepName].boundaryConditionStates[name] = DisplacementBCState()
        return boundaryCondition

    @abaqus_method_doc
    def ElectricPotentialBC(
        self,
        name: str,
        createStepName: str,
        region: Region,
        fieldName: str = "",
        magnitude: float = 0,
        distributionType: SymbolicConstant = UNIFORM,
        amplitude: str = UNSET,
        fixed: Boolean = OFF,
    ) -> ElectricPotentialBC:
        """This method creates an ElectricPotentialBC object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].ElectricPotentialBC

        Parameters
        ----------
        name
            A String specifying the boundary condition repository key.
        createStepName
            A String specifying the name of the step in which the boundary condition is created.
        region
            A :py:class:`~abaqus.Region.Region.Region` object specifying the region to which the boundary condition is applied.
        fieldName
            A String specifying the name of the AnalyticalField object associated with this boundary
            condition. The **fieldName** argument applies only when **distributionType** = FIELD. The
            default value is an empty string.
        magnitude
            A Float specifying the electrical potential magnitude. The default value is 0. The
            **magnitude** argument is optional if **distributionType** = USER_DEFINED.
        distributionType
            A SymbolicConstant specifying how the boundary condition is distributed spatially.
            Possible values are UNIFORM, USER_DEFINED, and FIELD. The default value is UNIFORM.
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
            UNSET should be used if the boundary condition has no amplitude reference. The default
            value is UNSET. You should provide the **amplitude** argument only if it is valid for the
            specified step.
        fixed
            A Boolean specifying whether the boundary condition should remain fixed at the current
            values at the start of the step. The default value is OFF.

        Returns
        -------
        bc: ElectricPotentialBC
            An :py:class:`~abaqus.BoundaryCondition.ElectricPotentialBC.ElectricPotentialBC` object.
        """
        self.boundaryConditions[name] = boundaryCondition = ElectricPotentialBC(
            name,
            createStepName,
            region,
            fieldName,
            magnitude,
            distributionType,
            amplitude,
            fixed,
        )
        self.steps[createStepName].boundaryConditionStates[
            name
        ] = ElectricPotentialBCState()
        return boundaryCondition

    @abaqus_method_doc
    def EulerianBC(
        self,
        name: str,
        createStepName: str,
        region: Region,
        definition: SymbolicConstant = INFLOW,
        inflowType: SymbolicConstant = FREE,
        outflowType: SymbolicConstant = ZERO_PRESSURE,
    ) -> EulerianBC:
        """This method creates a EulerianBC object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].EulerianBC

        Parameters
        ----------
        name
            A String specifying the boundary condition repository key.
        createStepName
            A String specifying the name of the step in which the boundary condition is created.
        region
            A :py:class:`~abaqus.Region.Region.Region` object specifying the region to which the boundary condition is applied.
        definition
            A SymbolicConstant specifying the flow conditions to be defined. Possible values are
            INFLOW, OUTFLOW, and BOTH. The default value is INFLOW.
        inflowType
            A SymbolicConstant specifying the control of material flow into the Eulerian domain.
            Possible values are FREE, NONE, and VOID. The default value is FREE.
        outflowType
            A SymbolicConstant specifying the control of flow of material out of the Eulerian
            domain. Possible values are ZERO_PRESSURE, FREE, NON_REFLECTING, and EQUILIBRIUM. The
            default value is ZERO_PRESSURE.

        Returns
        -------
        bc: EulerianBC
            An :py:class:`~abaqus.BoundaryCondition.EulerianBC.EulerianBC` object.
        """
        self.boundaryConditions[name] = boundaryCondition = EulerianBC(
            name, createStepName, region, definition, inflowType, outflowType
        )
        self.steps[createStepName].boundaryConditionStates[name] = EulerianBCState()
        return boundaryCondition

    @abaqus_method_doc
    def EulerianMotionBC(
        self,
        name: str,
        createStepName: str,
        instanceName: str,
        followRegion: Boolean = ON,
        region: typing.Optional[Region] = None,
        materialName: str = "",
        ctrPosition1: SymbolicConstant = FREE,
        posPosition1: SymbolicConstant = FREE,
        negPosition1: SymbolicConstant = FREE,
        expansionRatio1: typing.Optional[float] = None,
        contractRatio1: float = 0,
        ctrPosition2: SymbolicConstant = FREE,
        posPosition2: SymbolicConstant = FREE,
        negPosition2: SymbolicConstant = FREE,
        expansionRatio2: typing.Optional[float] = None,
        contractRatio2: float = 0,
        ctrPosition3: SymbolicConstant = FREE,
        posPosition3: SymbolicConstant = FREE,
        negPosition3: SymbolicConstant = FREE,
        expansionRatio3: typing.Optional[float] = None,
        contractRatio3: float = 0,
        allowContraction: Boolean = ON,
        aspectLimit: float = 10,
        vmaxFactor: float = 1,
        volThreshold: float = 0,
        bufferSize: float = 2,
    ) -> EulerianMotionBC:
        """This method creates an EulerianMotionBC object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].EulerianMotionBC

        Parameters
        ----------
        name
            A String specifying the boundary condition repository key.
        createStepName
            A String specifying the name of the step in which the boundary condition is created.
        instanceName
            A String specifying the name of the Eulerian part instance.
        followRegion
            A Boolean specifying whether the mesh will follow a regular surface region or an
            Eulerian surface. The default value is ON.
        region
            A :py:class:`~abaqus.Region.Region.Region` object specifying the region to which the boundary condition is applied.
        materialName
            A String specifying the name of the Eulerian surface to follow. This argument applies
            only when **followRegion** = False.
        ctrPosition1
            A SymbolicConstant specifying the 1-direction translational constraint on the center of
            the Eulerian mesh. Possible values are FREE and FIXED. The default value is FREE.
        posPosition1
            A SymbolicConstant specifying the translational constraint on the positive (maximum)
            bounds of the mesh in the 1 direction. Possible values are FREE and FIXED. The default
            value is FREE.
        negPosition1
            A SymbolicConstant specifying the translational constraint on the negative (minimum)
            bounds of the mesh in the 1 direction. Possible values are FREE and FIXED. The default
            value is FREE.
        expansionRatio1
            None or a Float specifying the upper bounds on the allowable scaling of the mesh in the
            1 direction. If **expansionRatio1** = None, then there is no upper limit. The default value
            is None.
        contractRatio1
            A Float specifying the lower bounds on the allowable scaling of the mesh in the 1
            direction. The default value is 0.0.
        ctrPosition2
            A SymbolicConstant specifying the 2-direction translational constraint on the center of
            the Eulerian mesh. Possible values are FREE and FIXED. The default value is FREE.
        posPosition2
            A SymbolicConstant specifying the translational constraint on the positive (maximum)
            bounds of the mesh in the 2 direction. Possible values are FREE and FIXED. The default
            value is FREE.
        negPosition2
            A SymbolicConstant specifying the translational constraint on the negative (minimum)
            bounds of the mesh in the 2 direction. Possible values are FREE and FIXED. The default
            value is FREE.
        expansionRatio2
            None or a Float specifying the upper bounds on the allowable scaling of the mesh in the
            2 direction. If **expansionRatio2** = None, then there is no upper limit. The default value
            is None.
        contractRatio2
            A Float specifying the lower bounds on the allowable scaling of the mesh in the 2
            direction. The default value is 0.0.
        ctrPosition3
            A SymbolicConstant specifying the 3-direction translational constraint on the center of
            the Eulerian mesh. Possible values are FREE and FIXED. The default value is FREE.
        posPosition3
            A SymbolicConstant specifying the translational constraint on the positive (maximum)
            bounds of the mesh in the 3 direction. Possible values are FREE and FIXED. The default
            value is FREE.
        negPosition3
            A SymbolicConstant specifying the translational constraint on the negative (minimum)
            bounds of the mesh in the 3 direction. Possible values are FREE and FIXED. The default
            value is FREE.
        expansionRatio3
            None or a Float specifying the upper bounds on the allowable scaling of the mesh in the
            3 direction. If **expansionRatio3** = None, then there is no upper limit. The default value
            is None.
        contractRatio3
            A Float specifying the lower bounds on the allowable scaling of the mesh in the 3
            direction. The default value is 0.0.
        allowContraction
            A Boolean specifying whether the mesh is allowed to contract . The default value is ON.
        aspectLimit
            A Float specifying the maximum change in allowed aspect ratio (for any of the three mesh
            aspects, 1-2, 2-3, 3-1). The default value is 10.0.
        vmaxFactor
            A Float specifying the multiplier for the mesh nodal velocity limit. The default value
            is 1.01.
        volThreshold
            A Float specifying the lower bounds on the volume fraction when determining which nodes
            to include in the surface bounding box calculation for an Eulerian material surface.
            This argument applies only when **followRegion** = False. The default value is 0.5.
        bufferSize
            None or a Float specifying the buffer between the surface box and the Eulerian section
            mesh bounding box. The default value is 2.0.

        Returns
        -------
        bc: EulerianMotionBC
            An :py:class:`~abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC` object.
        """
        self.boundaryConditions[name] = boundaryCondition = EulerianMotionBC(
            name,
            createStepName,
            instanceName,
            followRegion,
            region,
            materialName,
            ctrPosition1,
            posPosition1,
            negPosition1,
            expansionRatio1,
            contractRatio1,
            ctrPosition2,
            posPosition2,
            negPosition2,
            expansionRatio2,
            contractRatio2,
            ctrPosition3,
            posPosition3,
            negPosition3,
            expansionRatio3,
            contractRatio3,
            allowContraction,
            aspectLimit,
            vmaxFactor,
            volThreshold,
            bufferSize,
        )
        self.steps[createStepName].boundaryConditionStates[
            name
        ] = EulerianMotionBCState()
        return boundaryCondition

    @abaqus_method_doc
    def FluidCavityPressureBC(
        self,
        name: str,
        createStepName: str,
        fluidCavity: str,
        magnitude: float = 0,
        amplitude: str = UNSET,
        fixed: Boolean = OFF,
    ) -> FluidCavityPressureBC:
        """This method creates a FluidCavityPressureBC object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].FluidCavityPressureBC

        Parameters
        ----------
        name
            A String specifying the boundary condition repository key.
        createStepName
            A String specifying the name of the step in which the boundary condition is created.
        fluidCavity
            A String specifying the name of a Fluid Cavity Interaction.
        magnitude
            A Float specifying the fluid cavity pressure magnitude. The default value is 0.
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
            UNSET should be used if the boundary condition has no amplitude reference. The default
            value is UNSET. You should provide the **amplitude** argument only if it is valid for the
            specified step.
        fixed
            A Boolean specifying whether the boundary condition should remain fixed at the current
            values at the start of the step. The default value is OFF.

        Returns
        -------
        bc: FluidCavityPressureBC
            A :py:class:`~abaqus.BoundaryCondition.FluidCavityPressureBC.FluidCavityPressureBC` object.
        """
        self.boundaryConditions[name] = boundaryCondition = FluidCavityPressureBC(
            name, createStepName, fluidCavity, magnitude, amplitude, fixed
        )
        self.steps[createStepName].boundaryConditionStates[
            name
        ] = FluidCavityPressureBCState()
        return boundaryCondition

    @abaqus_method_doc
    def MagneticVectorPotentialBC(
        self,
        name: str,
        createStepName: str,
        region: Region,
        component1: typing.Optional[SymbolicConstant] = None,
        component2: SymbolicConstant = UNSET,
        component3: SymbolicConstant = UNSET,
        amplitude: str = UNSET,
        distributionType: SymbolicConstant = UNIFORM,
        localCsys: typing.Optional[str] = None,
    ) -> MagneticVectorPotentialBC:
        """This method creates a MagneticVectorPotentialBC object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].MagneticVectorPotentialBC

        Parameters
        ----------
        name
            A String specifying the boundary condition repository key.
        createStepName
            A String specifying the name of the step in which the boundary condition is created.
        region
            A :py:class:`~abaqus.Region.Region.Region` object specifying the region to which the boundary condition is applied.
        component1
            A Complex, or a SymbolicConstant specifying the magnetic vector potential component in
            the 1-direction. Possible values for the SymbolicConstant are UNSET and SET. The default
            value is UNSET
        component2
            A Complex, or a SymbolicConstant specifying the magnetic vector potential component in
            the 2-direction. Possible values for the SymbolicConstant are UNSET and SET. The default
            value is UNSET.
        component3
            A Complex, or a SymbolicConstant specifying the magnetic vector potential component in
            the 3-direction. Possible values for the SymbolicConstant are UNSET and SET. The default
            value is UNSET.
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
            UNSET should be used if the boundary condition has no amplitude reference. The default
            value is UNSET. You should provide the **amplitude** argument only if it is valid for the
            specified step.
        distributionType
            A SymbolicConstant specifying how the boundary condition is distributed spatially.
            Possible values are UNIFORM and USER_DEFINED. The default value is UNIFORM.
        localCsys
            None or a DatumCsys object specifying the local coordinate system of the boundary
            condition's degrees of freedom. If **localCsys** = None, the degrees of freedom are defined
            in the global coordinate system. The default value is None.

        Returns
        -------
        bc: MagneticVectorPotentialBC
            A :py:class:`~abaqus.BoundaryCondition.MagneticVectorPotentialBC.MagneticVectorPotentialBC` object.
        """
        self.boundaryConditions[name] = boundaryCondition = MagneticVectorPotentialBC(
            name,
            createStepName,
            region,
            component1,
            component2,
            component3,
            amplitude,
            distributionType,
            localCsys,
        )
        return boundaryCondition

    @abaqus_method_doc
    def MaterialFlowBC(
        self,
        name: str,
        createStepName: str,
        region: Region,
        fieldName: str = "",
        magnitude: float = 0,
        distributionType: SymbolicConstant = UNIFORM,
        amplitude: str = UNSET,
        fixed: Boolean = OFF,
    ) -> MaterialFlowBC:
        """This method creates a MaterialFlowBC object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].MaterialFlowBC

        Parameters
        ----------
        name
            A String specifying the boundary condition repository key.
        createStepName
            A String specifying the name of the step in which the boundary condition is created.
        region
            A :py:class:`~abaqus.Region.Region.Region` object specifying the region to which the boundary condition is applied.
        fieldName
            A String specifying the name of the AnalyticalField object associated with this boundary
            condition. The **fieldName** argument applies only when **distributionType** = FIELD. The
            default value is an empty string.
        magnitude
            A Float specifying the material flow magnitude. The default value is 0. The **magnitude**
            argument is optional if **distributionType** = USER_DEFINED.
        distributionType
            A SymbolicConstant specifying how the boundary condition is distributed spatially.
            Possible values are UNIFORM, USER_DEFINED, and FIELD. The default value is UNIFORM.
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
            UNSET should be used if the boundary condition has no amplitude reference. The default
            value is UNSET. You should provide the **amplitude** argument only if it is valid for the
            specified step.
        fixed
            A Boolean specifying whether the boundary condition should remain fixed at the current
            values at the start of the step. The default value is OFF.

        Returns
        -------
        bc: MaterialFlowBC
            A :py:class:`~abaqus.BoundaryCondition.MaterialFlowBC.MaterialFlowBC` object.
        """
        self.boundaryConditions[name] = boundaryCondition = MaterialFlowBC(
            name,
            createStepName,
            region,
            fieldName,
            magnitude,
            distributionType,
            amplitude,
            fixed,
        )
        self.steps[createStepName].boundaryConditionStates[name] = MaterialFlowBCState()
        return boundaryCondition

    @abaqus_method_doc
    def PorePressureBC(
        self,
        name: str,
        createStepName: str,
        region: Region,
        fieldName: str = "",
        magnitude: float = 0,
        distributionType: SymbolicConstant = UNIFORM,
        amplitude: str = UNSET,
        fixed: Boolean = OFF,
    ) -> PorePressureBC:
        """This method creates a PorePressureBC object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].PorePressureBC

        Parameters
        ----------
        name
            A String specifying the boundary condition repository key.
        createStepName
            A String specifying the name of the step in which the boundary condition is created.
        region
            A :py:class:`~abaqus.Region.Region.Region` object specifying the region to which the boundary condition is applied.
        fieldName
            A String specifying the name of the AnalyticalField object associated with this boundary
            condition. The **fieldName** argument applies only when **distributionType** = FIELD. The
            default value is an empty string.
        magnitude
            A Float specifying the pore pressure magnitude. The default value is 0. The **magnitude**
            argument is optional if **distributionType** = USER_DEFINED.
        distributionType
            A SymbolicConstant specifying how the boundary condition is distributed spatially.
            Possible values are UNIFORM, USER_DEFINED, and FIELD. The default value is UNIFORM.
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
            UNSET should be used if the boundary condition has no amplitude reference. The default
            value is UNSET. You should provide the **amplitude** argument only if it is valid for the
            specified step.
        fixed
            A Boolean specifying whether the boundary condition should remain fixed at the current
            values at the start of the step. The default value is OFF.

        Returns
        -------
        bc: PorePressureBC
            A :py:class:`~abaqus.BoundaryCondition.PorePressureBC.PorePressureBC` object.
        """
        self.boundaryConditions[name] = boundaryCondition = PorePressureBC(
            name,
            createStepName,
            region,
            fieldName,
            magnitude,
            distributionType,
            amplitude,
            fixed,
        )
        self.steps[createStepName].boundaryConditionStates[name] = PorePressureBCState()
        return boundaryCondition

    @abaqus_method_doc
    def RetainedNodalDofsBC(
        self,
        name: str,
        createStepName: str,
        region: Region,
        u1: Boolean = OFF,
        u2: Boolean = OFF,
        u3: Boolean = OFF,
        ur1: Boolean = OFF,
        ur2: Boolean = OFF,
        ur3: Boolean = OFF,
    ) -> RetainedNodalDofsBC:
        """This method creates a RetainedNodalDofsBC object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].RetainedNodalDofsBC

        Parameters
        ----------
        name
            A String specifying the boundary condition repository key.
        createStepName
            A String specifying the name of the step in which the boundary condition is created.
        region
            A :py:class:`~abaqus.Region.Region.Region` object specifying the region to which the boundary condition is applied.
        u1
            A Boolean specifying whether to retain the degree of freedom in the 1-direction. The
            default value is OFF indicating that the degree of freedom is not retained.
        u2
            A Boolean specifying whether to retain the degree of freedom in the 2-direction. The
            default value is OFF indicating that the degree of freedom is not retained.
        u3
            A Boolean specifying whether to retain the degree of freedom in the 3-direction. The
            default value is OFF indicating that the degree of freedom is not retained.
        ur1
            A Boolean specifying whether to retain the rotational degree of freedom about the
            1-direction. The default value is OFF indicating that the degree of freedom is not
            retained.
        ur2
            A Boolean specifying whether to retain the rotational degree of freedom about the
            2-direction. The default value is OFF indicating that the degree of freedom is not
            retained.
        ur3
            A Boolean specifying whether to retain the rotational degree of freedom about the
            3-direction. The default value is OFF indicating that the degree of freedom is not
            retained.

        Returns
        -------
        bc: RetainedNodalDofsBC
            A :py:class:`~abaqus.BoundaryCondition.RetainedNodalDofsBC.RetainedNodalDofsBC` object.
        """
        self.boundaryConditions[name] = boundaryCondition = RetainedNodalDofsBC(
            name, createStepName, region, u1, u2, u3, ur1, ur2, ur3
        )
        return boundaryCondition

    @abaqus_method_doc
    def SecondaryBaseBC(
        self, name: str, createStepName: str, regions: RegionArray, dofs: tuple
    ) -> SecondaryBaseBC:
        """This method creates a SecondaryBaseBC object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].SecondaryBaseBC

        Parameters
        ----------
        name
            A String specifying the boundary condition repository key.
        createStepName
            A String specifying the name of the step in which the boundary condition is created.
        regions
            A :py:class:`~abaqus.Region.RegionArray.RegionArray` object specifying the region to which the boundary condition is applied.
            Note that the usual **region** is ignored. The default value is MODEL.
        dofs
            A sequence of sequences of Ints specifying the constrained degrees-of-freedom.

        Returns
        -------
        bc: SecondaryBaseBC
            A :py:class:`~abaqus.BoundaryCondition.SecondaryBaseBC.SecondaryBaseBC` object.
        """
        self.boundaryConditions[name] = boundaryCondition = SecondaryBaseBC(
            name, createStepName, regions, dofs
        )
        self.steps[createStepName].boundaryConditionStates[
            name
        ] = SecondaryBaseBCState()
        return boundaryCondition

    @abaqus_method_doc
    def SubmodelBC(
        self,
        name: str,
        createStepName: str,
        region: Region,
        dof: tuple,
        globalStep: str,
        timeScale: Boolean,
        shellThickness: float,
        globalDrivingRegion: str = "",
        absoluteExteriorTolerance: typing.Optional[float] = None,
        exteriorTolerance: float = 0,
        localCsys: typing.Optional[str] = None,
        globalIncrement: int = 0,
        centerZoneSize: typing.Optional[float] = None,
        intersectionOnly: Boolean = OFF,
    ) -> SubmodelBC:
        """This method creates a SubmodelBC object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].SubmodelBC

        Parameters
        ----------
        name
            A String specifying the boundary condition repository key.
        createStepName
            A String specifying the name of the step in which the boundary condition is created.
        region
            A :py:class:`~abaqus.Region.Region.Region` object specifying the region to which the boundary condition is applied.
        dof
            A sequence of Ints specifying the degrees of freedom to which the boundary condition is
            applied.
        globalStep
            A String specifying the step in the global model from which Abaqus reads the values of
            the variables that will drive the submodel analysis. The String indicates the position
            of the step in the sequence of analysis steps. For example, **globalStep** = '1' indicates
            the first step.
        timeScale
            A Boolean specifying whether to scale the time variable for the driven nodes' amplitude
            functions to match the submodel analysis step time. The default value is OFF.
        shellThickness
            A Float specifying the thickness of the shell in the global model. This argument is
            required for shell-to-solid submodeling and is not applicable to other submodels. The
            default value is 0.0.
        globalDrivingRegion
            A String specifying the element set in the global model that will be searched for
            elements whose responses will be used to drive the submodel. An empty string indicates
            that the entire global model will be searched. The default value is an empty string.
        absoluteExteriorTolerance
            None or a Float specifying the absolute value by which a driven node of the submodel can
            lie outside the region of the elements of the global model. The default value is None.
        exteriorTolerance
            None or a Float specifying the fraction of the average element size in the global model
            by which a driven node of the submodel can lie outside the region of the elements of the
            global model. The default value is 0.05.
        localCsys
            None or a DatumCsys object specifying the local coordinate system of the boundary
            condition's degrees of freedom. If **localCsys** = None, the degrees of freedom are defined
            in the global coordinate system. The default value is None.
        globalIncrement
            An Int specifying the increment number in the global model step from which the solution
            will be used to specify the values of the driven variables. If **globalIncrement** = 0, the
            solution from the last increment will be used. The **globalIncrement** argument is
            applicable only for linear perturbation steps. The default value is 0.
        centerZoneSize
            A Float specifying the thickness of the center zone size around the shell midsurface.
            The default value is None.
        intersectionOnly
            A Boolean specifying whether to ignore driven nodes that lie outside the region of
            elements of the global model after accounting for the exterior search tolerance. The
            default value is OFF.

            .. versionadded:: 2021
                The `intersectionOnly` argument was added.

        Returns
        -------
        bc: SubmodelBC
            A :py:class:`~abaqus.BoundaryCondition.SubmodelBC.SubmodelBC` object.
        """
        self.boundaryConditions[name] = boundaryCondition = SubmodelBC(
            name,
            createStepName,
            region,
            dof,
            globalStep,
            timeScale,
            shellThickness,
            globalDrivingRegion,
            absoluteExteriorTolerance,
            exteriorTolerance,
            localCsys,
            globalIncrement,
            centerZoneSize,
            intersectionOnly,
        )
        self.steps[createStepName].boundaryConditionStates[name] = SubmodelBCState()
        return boundaryCondition

    @abaqus_method_doc
    def TemperatureBC(
        self,
        name: str,
        createStepName: str,
        region: Region,
        fieldName: str = "",
        magnitude: float = 0,
        dof: tuple = (),
        amplitude: str = UNSET,
        distributionType: SymbolicConstant = UNIFORM,
        fixed: Boolean = OFF,
    ) -> TemperatureBC:
        """This method creates a TemperatureBC object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].TemperatureBC

        Parameters
        ----------
        name
            A String specifying the boundary condition repository key.
        createStepName
            A String specifying the name of the step in which the boundary condition is created.
        region
            A :py:class:`~abaqus.Region.Region.Region` object specifying the region to which the boundary condition is applied.
        fieldName
            A String specifying the name of the AnalyticalField object associated with this boundary
            condition. The **fieldName** argument applies only when **distributionType** = FIELD. The
            default value is an empty string.
        magnitude
            A Float specifying the temperature magnitude. The default value is 0.
        dof
            A sequence of Ints specifying the degrees of freedom to which the boundary condition is
            applied. The default value is (11,).
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
            UNSET should be used if the boundary condition has no amplitude reference. The default
            value is UNSET. You should provide the **amplitude** argument only if it is valid for the
            specified step.
        distributionType
            A SymbolicConstant specifying how the boundary condition is distributed spatially.
            Possible values are UNIFORM, USER_DEFINED, and FIELD. The default value is UNIFORM.
        fixed
            A Boolean specifying whether the boundary condition should remain fixed at the current
            values at the start of the step. The default value is OFF.

        Returns
        -------
        bc: TemperatureBC
            A :py:class:`~abaqus.BoundaryCondition.TemperatureBC.TemperatureBC` object.
        """
        self.boundaryConditions[name] = boundaryCondition = TemperatureBC(
            name,
            createStepName,
            region,
            fieldName,
            magnitude,
            dof,
            amplitude,
            distributionType,
            fixed,
        )
        self.steps[createStepName].boundaryConditionStates[name] = TemperatureBCState()
        return boundaryCondition

    @abaqus_method_doc
    def VelocityBaseMotionBC(
        self,
        name: str,
        createStepName: str,
        dof: SymbolicConstant,
        amplitudeScaleFactor: float = 1,
        centerOfRotation: tuple = (),
        correlation: typing.Optional[Correlation] = None,
        secondaryBase: str = "",
        useComplex: Boolean = OFF,
        amplitude: str = UNSET,
    ) -> VelocityBaseMotionBC:
        """This method creates a VelocityBaseMotionBC object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].VelocityBaseMotionBC

        Parameters
        ----------
        name
            A String specifying the boundary condition repository key.
        createStepName
            A String specifying the name of the step in which the boundary condition is created.
        dof
            A SymbolicConstant specifying the constrained degree-of-freedom. Possible values for the
            SymbolicConstant are U1, U2, U3, UR1, UR2, UR3. The default value is U1.
        amplitudeScaleFactor
            A Float specifying the scale factor for the amplitude curve. The default value is 1.0.
        centerOfRotation
            A :py:class:`~abaqus.BasicGeometry.ModelDot.ModelDot` object specifying a tuple containing one center of rotation. The default
            value is the global origin. This argument applies only when **dof** = UR1, UR2, or UR3.
        correlation
            A :py:class:`~abaqus.Amplitude.Correlation.Correlation` object.
        secondaryBase
            A String specifying the name of the SecondaryBaseBC object associated with this boundary
            condition. The default value is an empty string.
        useComplex
            A Boolean specifying whether to define the imaginary (out-of-plane) portion of the base
            motion record given by amplitude definition. The default value is OFF.
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
            UNSET should be used if the boundary condition has no amplitude reference. The default
            value is UNSET. You should provide the **amplitude** argument only if it is valid for the
            specified step.

        Returns
        -------
        bc: VelocityBaseMotionBC
            A :py:class:`~abaqus.BoundaryCondition.VelocityBaseMotionBC.VelocityBaseMotionBC` object.
        """
        self.boundaryConditions[name] = boundaryCondition = VelocityBaseMotionBC(
            name,
            createStepName,
            dof,
            amplitudeScaleFactor,
            centerOfRotation,
            correlation,
            secondaryBase,
            useComplex,
            amplitude,
        )
        self.steps[createStepName].boundaryConditionStates[
            name
        ] = VelocityBaseMotionBCState()
        return boundaryCondition

    @abaqus_method_doc
    def VelocityBC(
        self,
        name: str,
        createStepName: str,
        region: Region,
        fieldName: str = "",
        v1: typing.Union[SymbolicConstant, float] = UNSET,
        v2: typing.Union[SymbolicConstant, float] = UNSET,
        v3: typing.Union[SymbolicConstant, float] = UNSET,
        vr1: typing.Union[SymbolicConstant, float] = UNSET,
        vr2: typing.Union[SymbolicConstant, float] = UNSET,
        vr3: typing.Union[SymbolicConstant, float] = UNSET,
        amplitude: str = UNSET,
        localCsys: typing.Optional[str] = None,
        distributionType: SymbolicConstant = UNIFORM,
    ) -> VelocityBC:
        """This method creates a VelocityBC object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].VelocityBC

        Parameters
        ----------
        name
            A String specifying the boundary condition repository key.
        createStepName
            A String specifying the name of the step in which the boundary condition is created.
        region
            A :py:class:`~abaqus.Region.Region.Region` object specifying the region to which the boundary condition is applied.
        fieldName
            A String specifying the name of the AnalyticalField object associated with this boundary
            condition. The **fieldName** argument applies only when **distributionType** = FIELD. The
            default value is an empty string.
        v1
            A Float or a SymbolicConstant specifying the velocity component in the 1-direction.
            Possible values for the SymbolicConstant are UNSET and SET. The default value is
            UNSET.Note:Although **v1**, **v2**, **v3**, **vr1**, **vr2**, and **vr3** are optional arguments, at
            least one of them must be specified.
        v2
            A Float or a SymbolicConstant specifying the velocity component in the 2-direction.
            Possible values for the SymbolicConstant are UNSET and SET. The default value is UNSET.
        v3
            A Float or a SymbolicConstant specifying the velocity component in the 3-direction.
            Possible values for the SymbolicConstant are UNSET and SET. The default value is UNSET.
        vr1
            A Float or a SymbolicConstant specifying the rotational velocity component about the
            1-direction. Possible values for the SymbolicConstant are UNSET and SET. The default
            value is UNSET.
        vr2
            A Float or a SymbolicConstant specifying the rotational velocity component about the
            2-direction. Possible values for the SymbolicConstant are UNSET and SET. The default
            value is UNSET.
        vr3
            A Float or a SymbolicConstant specifying the rotational velocity component about the
            3-direction. Possible values for the SymbolicConstant are UNSET and SET. The default
            value is UNSET.
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
            UNSET should be used if the boundary condition has no amplitude reference. The default
            value is UNSET. You should provide the **amplitude** argument only if it is valid for the
            specified step.
        localCsys
            None or a DatumCsys object specifying the local coordinate system of the boundary
            condition's degrees of freedom. If **localCsys** = None, the degrees of freedom are defined
            in the global coordinate system. The default value is None.
        distributionType
            A SymbolicConstant specifying how the boundary condition is distributed spatially.
            Possible values are UNIFORM, USER_DEFINED, and FIELD. The default value is UNIFORM.

        Returns
        -------
        bc: VelocityBC
            A :py:class:`~abaqus.BoundaryCondition.VelocityBC.VelocityBC` object.
        """
        self.boundaryConditions[name] = boundaryCondition = VelocityBC(
            name,
            createStepName,
            region,
            fieldName,
            v1,
            v2,
            v3,
            vr1,
            vr2,
            vr3,
            amplitude,
            localCsys,
            distributionType,
        )
        self.steps[createStepName].boundaryConditionStates[name] = VelocityBCState()
        return boundaryCondition
    
    @abaqus_method_doc
    def EncastreBC(
        self,
        name: str,
        createStepName: str,
        region: Region,
        buckleCase: SymbolicConstant = NOT_APPLICABLE,
        localCsys: typing.Optional[str] = None,
    ) -> TypeBC:
        """This method creates an encastre TypeBC object.
        
        .. note:: 
            This function can be accessed by::

                mdb.models[name].EncastreBC

        Parameters
        ----------
        name
            A String specifying the boundary condition repository key.
        createStepName
            A String specifying the name of the step in which the boundary condition is created.
        region
            A :py:class:`~abaqus.Region.Region.Region` object specifying the region to which the boundary condition is applied.
        buckleCase
            A SymbolicConstant specifying how the boundary condition is defined in a BUCKLE
            analysis. Possible values are NOT_APPLICABLE, STRESS_PERTURBATION, BUCKLING_MODES, and
            PERTURBATION_AND_BUCKLING. The default value is NOT_APPLICABLE.
        localCsys
            None or a DatumCsys object specifying the local coordinate system of the boundary
            condition's degrees of freedom. If **localCsys** = None, the degrees of freedom are defined
            in the global coordinate system. The default value is None.
        
        Returns
        -------
        TypeBC
            A :py:class:`~abaqus.BoundaryCondition.TypeBC.TypeBC` object.
        """
        self.boundaryConditions[name] = boundaryCondition = TypeBC.EncastreBC(
            name,
            createStepName,
            region,
            buckleCase,
            localCsys,
        )
        return boundaryCondition

    @abaqus_method_doc
    def PinnedBC(
        self,
        name: str,
        createStepName: str,
        region: Region,
        buckleCase: SymbolicConstant = NOT_APPLICABLE,
        localCsys: typing.Optional[str] = None,
    ) -> TypeBC:
        """This method creates a pinned TypeBC object.
        
        .. note:: 
            This function can be accessed by::

                mdb.models[name].PinnedBC

        Parameters
        ----------
        name
            A String specifying the boundary condition repository key.
        createStepName
            A String specifying the name of the step in which the boundary condition is created.
        region
            A :py:class:`~abaqus.Region.Region.Region` object specifying the region to which the boundary condition is applied.
        buckleCase
            A SymbolicConstant specifying how the boundary condition is defined in a BUCKLE
            analysis. Possible values are NOT_APPLICABLE, STRESS_PERTURBATION, BUCKLING_MODES, and
            PERTURBATION_AND_BUCKLING. The default value is NOT_APPLICABLE.
        localCsys
            None or a DatumCsys object specifying the local coordinate system of the boundary
            condition's degrees of freedom. If **localCsys** = None, the degrees of freedom are defined
            in the global coordinate system. The default value is None.
        
        Returns
        -------
        TypeBC
            A :py:class:`~abaqus.BoundaryCondition.TypeBC.TypeBC` object.
        """
        self.boundaryConditions[name] = boundaryCondition = TypeBC.PinnedBC(
            name,
            createStepName,
            region,
            buckleCase,
            localCsys,
        )
        return boundaryCondition

    @abaqus_method_doc
    def XsymmBC(
        self,
        name: str,
        createStepName: str,
        region: Region,
        buckleCase: SymbolicConstant = NOT_APPLICABLE,
        localCsys: typing.Optional[str] = None,
    ) -> TypeBC:
        """This method creates a TypeBC object that specifies symmetry about the **X**-axis.
        
        .. note:: 
            This function can be accessed by::

                mdb.models[name].EncastreBC
                
        Parameters
        ----------
        name
            A String specifying the boundary condition repository key.
        createStepName
            A String specifying the name of the step in which the boundary condition is created.
        region
            A :py:class:`~abaqus.Region.Region.Region` object specifying the region to which the boundary condition is applied.
        buckleCase
            A SymbolicConstant specifying how the boundary condition is defined in a BUCKLE
            analysis. Possible values are NOT_APPLICABLE, STRESS_PERTURBATION, BUCKLING_MODES, and
            PERTURBATION_AND_BUCKLING. The default value is NOT_APPLICABLE.
        localCsys
            None or a DatumCsys object specifying the local coordinate system of the boundary
            condition's degrees of freedom. If **localCsys** = None, the degrees of freedom are defined
            in the global coordinate system. The default value is None.

        Returns
        -------
        TypeBC
            A :py:class:`~abaqus.BoundaryCondition.TypeBC.TypeBC` object.
        """
        self.boundaryConditions[name] = boundaryCondition = TypeBC.XsymmBC(
            name,
            createStepName,
            region,
            buckleCase,
            localCsys,
        )
        return boundaryCondition

    @abaqus_method_doc
    def YsymmBC(
        self,
        name: str,
        createStepName: str,
        region: Region,
        buckleCase: SymbolicConstant = NOT_APPLICABLE,
        localCsys: typing.Optional[str] = None,
    ) -> TypeBC:
        """This method creates a TypeBC object that specifies symmetry about the **Y**-axis.
        
        .. note:: 
            This function can be accessed by::

                mdb.models[name].YsymmBC
                
        Parameters
        ----------
        name
            A String specifying the boundary condition repository key.
        createStepName
            A String specifying the name of the step in which the boundary condition is created.
        region
            A :py:class:`~abaqus.Region.Region.Region` object specifying the region to which the boundary condition is applied.
        buckleCase
            A SymbolicConstant specifying how the boundary condition is defined in a BUCKLE
            analysis. Possible values are NOT_APPLICABLE, STRESS_PERTURBATION, BUCKLING_MODES, and
            PERTURBATION_AND_BUCKLING. The default value is NOT_APPLICABLE.
        localCsys
            None or a DatumCsys object specifying the local coordinate system of the boundary
            condition's degrees of freedom. If **localCsys** = None, the degrees of freedom are defined
            in the global coordinate system. The default value is None.

        Returns
        -------
        TypeBC
            A :py:class:`~abaqus.BoundaryCondition.TypeBC.TypeBC` object.
        """
        self.boundaryConditions[name] = boundaryCondition = TypeBC.YsymmBC(
            name,
            createStepName,
            region,
            buckleCase,
            localCsys,
        )
        return boundaryCondition

    @abaqus_method_doc
    def ZsymmBC(
        self,
        name: str,
        createStepName: str,
        region: Region,
        buckleCase: SymbolicConstant = NOT_APPLICABLE,
        localCsys: typing.Optional[str] = None,
    ) -> TypeBC:
        """This method creates a TypeBC object that specifies symmetry about the **Z**-axis.
        
        .. note:: 
            This function can be accessed by::

                mdb.models[name].EncastreBC
                
        Parameters
        ----------
        name
            A String specifying the boundary condition repository key.
        createStepName
            A String specifying the name of the step in which the boundary condition is created.
        region
            A :py:class:`~abaqus.Region.Region.Region` object specifying the region to which the boundary condition is applied.
        buckleCase
            A SymbolicConstant specifying how the boundary condition is defined in a BUCKLE
            analysis. Possible values are NOT_APPLICABLE, STRESS_PERTURBATION, BUCKLING_MODES, and
            PERTURBATION_AND_BUCKLING. The default value is NOT_APPLICABLE.
        localCsys
            None or a DatumCsys object specifying the local coordinate system of the boundary
            condition's degrees of freedom. If **localCsys** = None, the degrees of freedom are defined
            in the global coordinate system. The default value is None.

        Returns
        -------
        TypeBC
            A :py:class:`~abaqus.BoundaryCondition.TypeBC.TypeBC` object.
        """
        self.boundaryConditions[name] = boundaryCondition = TypeBC.ZsymmBC(
            name,
            createStepName,
            region,
            buckleCase,
            localCsys,
        )
        return boundaryCondition

    @abaqus_method_doc
    def XasymmBC(
        self,
        name: str,
        createStepName: str,
        region: Region,
        buckleCase: SymbolicConstant = NOT_APPLICABLE,
        localCsys: typing.Optional[str] = None,
    ) -> TypeBC:
        """This method creates a TypeBC object that specifies antisymmetry about the **X**-axis.
        
        .. note:: 
            This function can be accessed by::

                mdb.models[name].EncastreBC
                
        Parameters
        ----------
        name
            A String specifying the boundary condition repository key.
        createStepName
            A String specifying the name of the step in which the boundary condition is created.
        region
            A :py:class:`~abaqus.Region.Region.Region` object specifying the region to which the boundary condition is applied.
        buckleCase
            A SymbolicConstant specifying how the boundary condition is defined in a BUCKLE
            analysis. Possible values are NOT_APPLICABLE, STRESS_PERTURBATION, BUCKLING_MODES, and
            PERTURBATION_AND_BUCKLING. The default value is NOT_APPLICABLE.
        localCsys
            None or a DatumCsys object specifying the local coordinate system of the boundary
            condition's degrees of freedom. If **localCsys** = None, the degrees of freedom are defined
            in the global coordinate system. The default value is None.

        Returns
        -------
        TypeBC
            A :py:class:`~abaqus.BoundaryCondition.TypeBC.TypeBC` object.
        """
        self.boundaryConditions[name] = boundaryCondition = TypeBC.XasymmBC(
            name,
            createStepName,
            region,
            buckleCase,
            localCsys,
        )
        return boundaryCondition

    @abaqus_method_doc
    def YasymmBC(
        self,
        name: str,
        createStepName: str,
        region: Region,
        buckleCase: SymbolicConstant = NOT_APPLICABLE,
        localCsys: typing.Optional[str] = None,
    ) -> TypeBC:
        """This method creates a TypeBC object that specifies antisymmetry about the **Y**-axis.
        
        .. note:: 
            This function can be accessed by::

                mdb.models[name].YasymmBC
                
        Parameters
        ----------
        name
            A String specifying the boundary condition repository key.
        createStepName
            A String specifying the name of the step in which the boundary condition is created.
        region
            A :py:class:`~abaqus.Region.Region.Region` object specifying the region to which the boundary condition is applied.
        buckleCase
            A SymbolicConstant specifying how the boundary condition is defined in a BUCKLE
            analysis. Possible values are NOT_APPLICABLE, STRESS_PERTURBATION, BUCKLING_MODES, and
            PERTURBATION_AND_BUCKLING. The default value is NOT_APPLICABLE.
        localCsys
            None or a DatumCsys object specifying the local coordinate system of the boundary
            condition's degrees of freedom. If **localCsys** = None, the degrees of freedom are defined
            in the global coordinate system. The default value is None.

        Returns
        -------
        TypeBC
            A :py:class:`~abaqus.BoundaryCondition.TypeBC.TypeBC` object.
        """
        self.boundaryConditions[name] = boundaryCondition = TypeBC.YasymmBC(
            name,
            createStepName,
            region,
            buckleCase,
            localCsys,
        )
        return boundaryCondition

    @abaqus_method_doc
    def ZasymmBC(
        self,
        name: str,
        createStepName: str,
        region: Region,
        buckleCase: SymbolicConstant = NOT_APPLICABLE,
        localCsys: typing.Optional[str] = None,
    ) -> TypeBC:
        """This method creates a TypeBC object that specifies antisymmetry about the **Z**-axis.
        
        .. note::
            This function can be accessed by::
            
                mdb.models[name].ZasymmBC
            
        Parameters
        ----------
        name
            A String specifying the boundary condition repository key.
        createStepName
            A String specifying the name of the step in which the boundary condition is created.
        region
            A :py:class:`~abaqus.Region.Region.Region` object specifying the region to which the boundary condition is applied.
        buckleCase
            A SymbolicConstant specifying how the boundary condition is defined in a BUCKLE
            analysis. Possible values are NOT_APPLICABLE, STRESS_PERTURBATION, BUCKLING_MODES, and
            PERTURBATION_AND_BUCKLING. The default value is NOT_APPLICABLE.
        localCsys
            None or a DatumCsys object specifying the local coordinate system of the boundary
            condition's degrees of freedom. If **localCsys** = None, the degrees of freedom are defined
            in the global coordinate system. The default value is None.
        
        Returns
        -------
        TypeBC
            A :py:class:`~abaqus.BoundaryCondition.TypeBC.TypeBC` object.
        """
        self.boundaryConditions[name] = boundaryCondition = TypeBC.ZasymmBC(
            name,
            createStepName,
            region,
            buckleCase,
            localCsys,
        )
        return boundaryCondition
