from typing import Optional, Union

from typing_extensions import Literal

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from ..Model.ModelBase import ModelBase
from ..Region.Region import Region
from ..Step.AnnealStep import AnnealStep
from ..Step.BuckleStep import BuckleStep
from ..Step.ComplexFrequencyStep import ComplexFrequencyStep
from ..Step.CoupledTempDisplacementStep import CoupledTempDisplacementStep
from ..Step.CoupledThermalElectricalStructuralStep import (
    CoupledThermalElectricalStructuralStep,
)
from ..Step.CoupledThermalElectricStep import CoupledThermalElectricStep
from ..Step.DirectCyclicStep import DirectCyclicStep
from ..Step.EmagTimeHarmonicStep import EmagTimeHarmonicStep
from ..Step.ExplicitDynamicsStep import ExplicitDynamicsStep
from ..Step.FrequencyStep import FrequencyStep
from ..Step.GeostaticStep import GeostaticStep
from ..Step.HeatTransferStep import HeatTransferStep
from ..Step.ImplicitDynamicsStep import ImplicitDynamicsStep
from ..Step.MassDiffusionStep import MassDiffusionStep
from ..Step.ModalDynamicsStep import ModalDynamicsStep
from ..Step.RandomResponseStep import RandomResponseStep
from ..Step.ResponseSpectrumStep import ResponseSpectrumStep
from ..Step.SoilsStep import SoilsStep
from ..Step.StaticLinearPerturbationStep import StaticLinearPerturbationStep
from ..Step.StaticRiksStep import StaticRiksStep
from ..Step.StaticStep import StaticStep
from ..Step.SteadyStateDirectStep import SteadyStateDirectStep
from ..Step.SteadyStateModalStep import SteadyStateModalStep
from ..Step.SteadyStateSubspaceStep import SteadyStateSubspaceStep
from ..Step.SubspaceDynamicsStep import SubspaceDynamicsStep
from ..Step.SubstructureGenerateStep import SubstructureGenerateStep
from ..Step.TempDisplacementDynamicsStep import TempDisplacementDynamicsStep
from ..Step.ViscoStep import ViscoStep
from ..StepMiscellaneous.CompositeDamping import CompositeDamping
from ..StepMiscellaneous.DirectDamping import DirectDamping
from ..StepMiscellaneous.DirectDampingByFrequency import DirectDampingByFrequency
from ..StepMiscellaneous.EmagTimeHarmonicFrequencyArray import (
    EmagTimeHarmonicFrequencyArray,
)
from ..StepMiscellaneous.MassScalingArray import MassScalingArray
from ..StepMiscellaneous.RandomResponseFrequencyArray import (
    RandomResponseFrequencyArray,
)
from ..StepMiscellaneous.RayleighDamping import RayleighDamping
from ..StepMiscellaneous.RayleighDampingByFrequency import RayleighDampingByFrequency
from ..StepMiscellaneous.ResponseSpectrumComponentArray import (
    ResponseSpectrumComponentArray,
)
from ..StepMiscellaneous.SteadyStateDirectFrequencyArray import (
    SteadyStateDirectFrequencyArray,
)
from ..StepMiscellaneous.SteadyStateModalFrequencyArray import (
    SteadyStateModalFrequencyArray,
)
from ..StepMiscellaneous.SteadyStateSubspaceFrequencyArray import (
    SteadyStateSubspaceFrequencyArray,
)
from ..StepMiscellaneous.StructuralDamping import StructuralDamping
from ..StepMiscellaneous.StructuralDampingByFrequency import (
    StructuralDampingByFrequency,
)
from ..StepMiscellaneous.SubstructureGenerateFrequencyArray import (
    SubstructureGenerateFrequencyArray,
)
from ..StepMiscellaneous.SubstructureGenerateModesArray import (
    SubstructureGenerateModesArray,
)
from ..UtilityAndView.abaqusConstants import (
    ABS,
    AC_ON,
    ALL,
    ALL_FREQUENCIES,
    ANALYSIS_PRODUCT_DEFAULT,
    AUTOMATIC,
    AUTOMATIC_GLOBAL,
    COMPLEX,
    DEFAULT,
    DIRECT,
    DISPLACEMENT,
    FULL_NEWTON,
    IMPLICIT,
    IMPLICIT_EXPLICIT,
    LINEAR,
    LOG,
    LOGARITHMIC,
    NONE,
    OFF,
    ON,
    PERIOD,
    PREVIOUS_STEP,
    PROPAGATED,
    RAMP,
    SINGLE_DIRECTION,
    SOLVER_DEFAULT,
    STEP,
    SUBSPACE,
    TRANSIENT,
    VALUE,
    WHOLE_MODEL,
    Boolean,
    SymbolicConstant,
)
from ..UtilityAndView.abaqusConstants import abaqusConstants as C


@abaqus_class_doc
class StepModel(ModelBase):
    """Abaqus creates a Model object named `Model-1` when a session is started.

    .. note::
        This object can be accessed by::

            mdb.models[name]
    """

    @abaqus_method_doc
    def AnnealStep(
        self,
        name: str,
        previous: str,
        description: str = "",
        refTemp: Optional[float] = None,
        maintainAttributes: Boolean = False,
    ) -> AnnealStep:
        """This method creates an AnnealStep object.

        .. note::
            This function can be accessed by::

                mdb.models[name].AnnealStep

        Parameters
        ----------
        name
            A String specifying the repository key.
        previous
            A String specifying the name of the previous step. The new step appears after this step
            in the list of analysis steps.
        description
            A String specifying a description of the new step. The default value is an empty string.
        refTemp
            A Float specifying the post-anneal reference temperature. The default value is the
            current temperature at all nodes in the model after the annealing has completed.
        maintainAttributes
            A Boolean specifying whether to retain attributes from an existing step with the same
            name. The default value is False.

        Returns
        -------
        step: AnnealStep
            An AnnealStep object.
        """
        self.steps[name] = step = AnnealStep(name, previous, description, refTemp, maintainAttributes)
        return step

    @abaqus_method_doc
    def BuckleStep(
        self,
        name: str,
        previous: str,
        numEigen: int,
        description: str = "",
        eigensolver: Literal[C.LANCZOS, C.SUBSPACE] = SUBSPACE,
        minEigen: Optional[float] = None,
        maxEigen: Optional[float] = None,
        vectors: Optional[int] = None,
        maxIterations: int = 30,
        blockSize: Literal[C.DEFAULT] = DEFAULT,
        maxBlocks: Literal[C.LANCZOS, C.DEFAULT] = DEFAULT,
        matrixStorage: Literal[C.SYMMETRIC, C.SOLVER_DEFAULT, C.UNSYMMETRIC] = SOLVER_DEFAULT,
        maintainAttributes: Boolean = False,
    ) -> BuckleStep:
        """This method creates a BuckleStep object.

        .. note::
            This function can be accessed by::

                mdb.models[name].BuckleStep

        Parameters
        ----------
        name
            A String specifying the repository key.
        previous
            A String specifying the name of the previous step. The new step appears after this step
            in the list of analysis steps.
        numEigen
            An Int specifying the number of eigenvalues to be estimated.
        description
            A String specifying a description of the new step. The default value is an empty string.
        eigensolver
            A SymbolicConstant specifying the eigensolver. Possible values are SUBSPACE and LANCZOS.
            The default value is SUBSPACE.
        minEigen
            None or a Float specifying the minimum eigenvalue of interest. The default value is
            None.
        maxEigen
            None or a Float specifying the maximum eigenvalue of interest. The default value is
            None.
        vectors
            An Int specifying the number of vectors used in the iteration. The default value is the
            minimum of (2*n*, **n** + 8), where **n** is the number of eigenvalues requested.
        maxIterations
            An Int specifying the maximum number of iterations. The default value is 30.
        blockSize
            The SymbolicConstant DEFAULT or an Int specifying the size of the Lanczos block steps.
            The default value is DEFAULT.
        maxBlocks
            The SymbolicConstant DEFAULT or an Int specifying the maximum number of Lanczos block
            steps within each Lanczos run. The default value is DEFAULT. Note: *minEigen*,
            **blockSize**, and **maxBlocks** are ignored unless **eigensolver** = LANCZOS.
        matrixStorage
            A SymbolicConstant specifying the type of matrix storage. Possible values are SYMMETRIC,
            UNSYMMETRIC, and SOLVER_DEFAULT. The default value is SOLVER_DEFAULT.
        maintainAttributes
            A Boolean specifying whether to retain attributes from an existing step with the same
            name. The default value is False.

        Returns
        -------
        step: BuckleStep
            A BuckleStep object.
        """
        self.steps[name] = step = BuckleStep(
            name,
            previous,
            numEigen,
            description,
            eigensolver,
            minEigen,
            maxEigen,
            vectors,
            maxIterations,
            blockSize,
            maxBlocks,
            matrixStorage,
            maintainAttributes,
        )
        return step

    @abaqus_method_doc
    def ComplexFrequencyStep(
        self,
        name: str,
        previous: str,
        numEigen: Literal[C.ALL] = ALL,
        description: str = "",
        shift: Optional[float] = None,
        frictionDamping: Boolean = OFF,
        matrixStorage: Literal[C.SYMMETRIC, C.SOLVER_DEFAULT, C.UNSYMMETRIC] = SOLVER_DEFAULT,
        maintainAttributes: Boolean = False,
        minEigen: Optional[float] = None,
        maxEigen: Optional[float] = None,
        propertyEvaluationFrequency: Optional[float] = None,
    ) -> ComplexFrequencyStep:
        """This method creates a ComplexFrequencyStep object.

        .. note::
            This function can be accessed by::

                mdb.models[name].ComplexFrequencyStep

        Parameters
        ----------
        name
            A String specifying the repository key.
        previous
            A String specifying the name of the previous step. The new step appears after this step
            in the list of analysis steps.
        numEigen
            The SymbolicConstant ALL or an Int specifying the number of complex eigenmodes to be
            calculated or a SymbolicConstant ALL. The default value is ALL.
        description
            A String specifying a description of the new step. The default value is an empty string.
        shift
            None or a Float specifying the shift point in cycles per time. The default value is
            None.
        frictionDamping
            A Boolean specifying whether to add to the damping matrix contributions due to friction
            effects. The default value is OFF.
        matrixStorage
            A SymbolicConstant specifying the type of matrix storage. Possible values are SYMMETRIC,
            UNSYMMETRIC, and SOLVER_DEFAULT. The default value is SOLVER_DEFAULT.
        maintainAttributes
            A Boolean specifying whether to retain attributes from an existing step with the same
            name. The default value is False.
        minEigen
            None or a Float specifying the minimum frequency of interest in cycles per time. The
            default value is None.
        maxEigen
            None or a Float specifying the maximum frequency of interest in cycles per time. The
            default value is None.
        propertyEvaluationFrequency
            None or a Float specifying the frequency at which to evaluate frequency-dependent
            properties for viscoelasticity, springs, and dashpots during the eigenvalue extraction.
            If the value is None, the analysis product will evaluate the stiffness associated with
            frequency-dependent springs and dashpots at zero frequency and will not consider the
            stiffness contributions from frequency-domain viscoelasticity in the step. The default
            value is None.

        Returns
        -------
        step: ComplexFrequencyStep
            A ComplexFrequencyStep object.
        """
        self.steps[name] = step = ComplexFrequencyStep(
            name,
            previous,
            numEigen,
            description,
            shift,
            frictionDamping,
            matrixStorage,
            maintainAttributes,
            minEigen,
            maxEigen,
            propertyEvaluationFrequency,
        )
        return step

    @abaqus_method_doc
    def CoupledTempDisplacementStep(
        self,
        name: str,
        previous: str,
        description: str = "",
        response: Literal[C.TRANSIENT, C.STEADY_STATE] = TRANSIENT,
        timePeriod: float = 1,
        nlgeom: Boolean = OFF,
        stabilizationMethod: Literal[C.DAMPING_FACTOR, C.DISSIPATED_ENERGY_FRACTION, C.NONE] = NONE,
        stabilizationMagnitude: Optional[float] = None,
        timeIncrementationMethod: Literal[C.AUTOMATIC, C.FIXED] = AUTOMATIC,
        maxNumInc: int = 100,
        initialInc: Optional[float] = None,
        minInc: Optional[float] = None,
        maxInc: Optional[float] = None,
        deltmx: float = 0,
        cetol: float = 0,
        creepIntegration: Literal[C.EXPLICIT, C.IMPLICIT, C.NONE] = IMPLICIT,
        solutionTechnique: Literal[C.SEPARATED, C.FULL_NEWTON] = FULL_NEWTON,
        matrixStorage: Literal[C.SYMMETRIC, C.SOLVER_DEFAULT, C.UNSYMMETRIC] = SOLVER_DEFAULT,
        amplitude: Literal[C.STEP, C.RAMP] = STEP,
        extrapolation: Literal[C.PARABOLIC, C.NONE, C.LINEAR] = LINEAR,
        maintainAttributes: Boolean = False,
        convertSDI: Literal[C.CONVERT_SDI_OFF, C.PROPAGATED, C.CONVERT_SDI_ON] = PROPAGATED,
        adaptiveDampingRatio: float = 0,
        continueDampingFactors: Boolean = OFF,
    ) -> CoupledTempDisplacementStep:
        """This method creates a CoupledTempDisplacementStep object.

        .. note::
            This function can be accessed by::

                mdb.models[name].CoupledTempDisplacementStep

        Parameters
        ----------
        name
            A String specifying the repository key.
        previous
            A String specifying the name of the previous step. The new step appears after this step
            in the list of analysis steps.
        description
            A String specifying a description of the new step. The default value is an empty string.
        response
            A SymbolicConstant specifying the analysis type. Possible values are STEADY_STATE and
            TRANSIENT. The default value is TRANSIENT.
        timePeriod
            A Float specifying the total time period for the step. The default value is 1.0.
        nlgeom
            A Boolean specifying whether geometric nonlinearities should be accounted for during the
            step. The default value is OFF.
        stabilizationMethod
            A SymbolicConstant specifying the stabilization type. Possible values are NONE,
            DISSIPATED_ENERGY_FRACTION, and DAMPING_FACTOR. The default value is NONE.
        stabilizationMagnitude
            A Float specifying the damping intensity of the automatic damping algorithm if the
            problem is expected to be unstable and **stabilizationMethod** ≠ NONE. The default value is
            2x10⁻⁴.
        timeIncrementationMethod
            A SymbolicConstant specifying the time incrementation method to be used. Possible values
            are FIXED and AUTOMATIC. The default value is AUTOMATIC.
        maxNumInc
            An Int specifying the maximum number of increments in a step. The default value is 100.
        initialInc
            A Float specifying the initial time increment. The default value is the total time
            period for the step.
        minInc
            A Float specifying the minimum time increment allowed. The default value is the smaller
            of the suggested initial time increment or 10−5 times the total time period.
        maxInc
            A Float specifying the maximum time increment allowed. The default value is the total
            time period for the step.
        deltmx
            A Float specifying the maximum temperature change to be allowed in an increment in a
            transient analysis. The default value is 0.0.
        cetol
            A Float specifying the maximum difference in the creep strain increment calculated from
            the creep strain rates at the beginning and end of the increment. The default value is
            0.0.
        creepIntegration
            A SymbolicConstant specifying the type of integration to be used for creep and swelling
            effects throughout the step. Possible values are IMPLICIT, EXPLICIT, and NONE. The
            default value is IMPLICIT.
        solutionTechnique
            A SymbolicConstant specifying the type of solution technique. Possible values are
            FULL_NEWTON and SEPARATED. The default value is FULL_NEWTON.
        matrixStorage
            A SymbolicConstant specifying the type of matrix storage. Possible values are SYMMETRIC,
            UNSYMMETRIC, and SOLVER_DEFAULT. The default value is SOLVER_DEFAULT.
        amplitude
            A SymbolicConstant specifying the amplitude variation for loading magnitudes during the
            step. The default value is STEP. Possible values are STEP and RAMP.
        extrapolation
            A SymbolicConstant specifying the type of extrapolation to use in determining the
            incremental solution for a nonlinear analysis. Possible values are NONE, LINEAR, and
            PARABOLIC. The default value is LINEAR.
        maintainAttributes
            A Boolean specifying whether to retain attributes from an existing step with the same
            name. The default value is False.
        convertSDI
            A SymbolicConstant specifying whether to force a new iteration if severe discontinuities
            occur during an iteration. Possible values are PROPAGATED, CONVERT_SDI_OFF, and
            CONVERT_SDI_ON. The default value is PROPAGATED.
        adaptiveDampingRatio
            A Float specifying the maximum allowable ratio of the stabilization energy to the total
            strain energy and can be used only if **stabilizationMethod** is not NONE. The default
            value is 0.05.
        continueDampingFactors
            A Boolean specifying whether this step will carry over the damping factors from the
            results of the preceding general step. This parameter must be used in conjunction with
            the **adaptiveDampingRatio** parameter. The default value is OFF.

        Returns
        -------
        step: CoupledTempDisplacementStep
            A CoupledTempDisplacementStep object.
        """
        self.steps[name] = step = CoupledTempDisplacementStep(
            name,
            previous,
            description,
            response,
            timePeriod,
            nlgeom,
            stabilizationMethod,
            stabilizationMagnitude,
            timeIncrementationMethod,
            maxNumInc,
            initialInc,
            minInc,
            maxInc,
            deltmx,
            cetol,
            creepIntegration,
            solutionTechnique,
            matrixStorage,
            amplitude,
            extrapolation,
            maintainAttributes,
            convertSDI,
            adaptiveDampingRatio,
            continueDampingFactors,
        )
        return step

    @abaqus_method_doc
    def CoupledThermalElectricalStructuralStep(
        self,
        name: str,
        previous: str,
        description: str = "",
        response: Literal[C.TRANSIENT, C.STEADY_STATE] = TRANSIENT,
        timePeriod: float = 1,
        nlgeom: Boolean = OFF,
        stabilizationMethod: Literal[C.DAMPING_FACTOR, C.DISSIPATED_ENERGY_FRACTION, C.NONE] = NONE,
        stabilizationMagnitude: Optional[float] = None,
        timeIncrementationMethod: Literal[C.AUTOMATIC, C.FIXED] = AUTOMATIC,
        maxNumInc: int = 100,
        initialInc: Optional[float] = None,
        minInc: Optional[float] = None,
        maxInc: Optional[float] = None,
        deltmx: float = 0,
        cetol: float = 0,
        creepIntegration: Literal[C.EXPLICIT, C.IMPLICIT, C.NONE] = IMPLICIT,
        matrixStorage: Literal[C.SYMMETRIC, C.SOLVER_DEFAULT, C.UNSYMMETRIC] = SOLVER_DEFAULT,
        amplitude: Literal[C.STEP, C.RAMP] = STEP,
        extrapolation: Literal[C.PARABOLIC, C.NONE, C.LINEAR] = LINEAR,
        maintainAttributes: Boolean = False,
        convertSDI: Literal[C.CONVERT_SDI_OFF, C.PROPAGATED, C.CONVERT_SDI_ON] = PROPAGATED,
        adaptiveDampingRatio: float = 0,
        continueDampingFactors: Boolean = OFF,
    ) -> CoupledThermalElectricalStructuralStep:
        """This method creates a CoupledThermalElectricalStructuralStep object.

        .. note::
            This function can be accessed by::

                mdb.models[name].CoupledThermalElectricalStructuralStep

        Parameters
        ----------
        name
            A String specifying the repository key.
        previous
            A String specifying the name of the previous step. The new step appears after this step
            in the list of analysis steps.
        description
            A String specifying a description of the new step. The default value is an empty string.
        response
            A SymbolicConstant specifying the analysis type. Possible values are STEADY_STATE and
            TRANSIENT. The default value is TRANSIENT.
        timePeriod
            A Float specifying the total time period for the step. The default value is 1.0.
        nlgeom
            A Boolean specifying whether geometric nonlinearities should be accounted for during the
            step. The default value is OFF.
        stabilizationMethod
            A SymbolicConstant specifying the stabilization type. Possible values are NONE,
            DISSIPATED_ENERGY_FRACTION, and DAMPING_FACTOR. The default value is NONE.
        stabilizationMagnitude
            A Float specifying the damping intensity of the automatic damping algorithm if the
            problem is expected to be unstable and **stabilizationMethod** ≠ NONE. The default value is
            2x10⁻⁴.
        timeIncrementationMethod
            A SymbolicConstant specifying the time incrementation method to be used. Possible values
            are FIXED and AUTOMATIC. The default value is AUTOMATIC.
        maxNumInc
            An Int specifying the maximum number of increments in a step. The default value is 100.
        initialInc
            A Float specifying the initial time increment. The default value is the total time
            period for the step.
        minInc
            A Float specifying the minimum time increment allowed. The default value is the smaller
            of the suggested initial time increment or 10−5 times the total time period.
        maxInc
            A Float specifying the maximum time increment allowed. The default value is the total
            time period for the step.
        deltmx
            A Float specifying the maximum temperature change to be allowed in an increment in a
            transient analysis. The default value is 0.0.
        cetol
            A Float specifying the maximum difference in the creep strain increment calculated from
            the creep strain rates at the beginning and end of the increment. The default value is
            0.0.
        creepIntegration
            A SymbolicConstant specifying the type of integration to be used for creep and swelling
            effects throughout the step. Possible values are IMPLICIT, EXPLICIT, and NONE. The
            default value is IMPLICIT.
        matrixStorage
            A SymbolicConstant specifying the type of matrix storage. Possible values are SYMMETRIC,
            UNSYMMETRIC, and SOLVER_DEFAULT. The default value is SOLVER_DEFAULT.
        amplitude
            A SymbolicConstant specifying the amplitude variation for loading magnitudes during the
            step. The default value is STEP. Possible values are STEP and RAMP.
        extrapolation
            A SymbolicConstant specifying the type of extrapolation to use in determining the
            incremental solution for a nonlinear analysis. Possible values are NONE, LINEAR, and
            PARABOLIC. The default value is LINEAR.
        maintainAttributes
            A Boolean specifying whether to retain attributes from an existing step with the same
            name. The default value is False.
        convertSDI
            A SymbolicConstant specifying whether to force a new iteration if severe discontinuities
            occur during an iteration. Possible values are PROPAGATED, CONVERT_SDI_OFF, and
            CONVERT_SDI_ON. The default value is PROPAGATED.
        adaptiveDampingRatio
            A Float specifying the maximum allowable ratio of the stabilization energy to the total
            strain energy and can be used only if **stabilizationMethod** is not NONE. The default
            value is 0.05.
        continueDampingFactors
            A Boolean specifying whether this step will carry over the damping factors from the
            results of the preceding general step. This parameter must be used in conjunction with
            the **adaptiveDampingRatio** parameter. The default value is OFF.

        Returns
        -------
        step: CoupledThermalElectricalStructuralStep
            A CoupledThermalElectricalStructuralStep object.
        """
        self.steps[name] = step = CoupledThermalElectricalStructuralStep(
            name,
            previous,
            description,
            response,
            timePeriod,
            nlgeom,
            stabilizationMethod,
            stabilizationMagnitude,
            timeIncrementationMethod,
            maxNumInc,
            initialInc,
            minInc,
            maxInc,
            deltmx,
            cetol,
            creepIntegration,
            matrixStorage,
            amplitude,
            extrapolation,
            maintainAttributes,
            convertSDI,
            adaptiveDampingRatio,
            continueDampingFactors,
        )
        return step

    @abaqus_method_doc
    def CoupledThermalElectricStep(
        self,
        name: str,
        previous: str,
        description: str = "",
        response: Literal[C.TRANSIENT, C.STEADY_STATE] = TRANSIENT,
        timePeriod: float = 1,
        timeIncrementationMethod: Literal[C.AUTOMATIC, C.FIXED] = AUTOMATIC,
        maxNumInc: int = 100,
        initialInc: Optional[float] = None,
        minInc: Optional[float] = None,
        maxInc: Optional[float] = None,
        end: Literal[C.SS, C.PERIOD] = PERIOD,
        deltmx: float = 0,
        mxdem: float = 0,
        solutionTechnique: Literal[C.SEPARATED, C.FULL_NEWTON] = FULL_NEWTON,
        matrixStorage: Literal[C.SYMMETRIC, C.SOLVER_DEFAULT, C.UNSYMMETRIC] = SOLVER_DEFAULT,
        amplitude: Literal[C.STEP, C.RAMP] = STEP,
        extrapolation: Literal[C.PARABOLIC, C.NONE, C.LINEAR] = LINEAR,
        maintainAttributes: Boolean = False,
        convertSDI: Literal[C.CONVERT_SDI_OFF, C.PROPAGATED, C.CONVERT_SDI_ON] = PROPAGATED,
    ) -> CoupledThermalElectricStep:
        """This method creates a CoupledThermalElectricStep object.

        .. note::
            This function can be accessed by::

                mdb.models[name].CoupledThermalElectricStep

        Parameters
        ----------
        name
            A String specifying the repository key.
        previous
            A String specifying the name of the previous step. The new step appears after this step
            in the list of analysis steps.
        description
            A String specifying a description of the new step. The default value is an empty string.
        response
            A SymbolicConstant specifying the analysis type. Possible values are STEADY_STATE and
            TRANSIENT. The default value is TRANSIENT.
        timePeriod
            A Float specifying the total time period for the step. The default value is 1.0.
        timeIncrementationMethod
            A SymbolicConstant specifying the time incrementation method to be used. Possible values
            are FIXED and AUTOMATIC. The default value is AUTOMATIC.
        maxNumInc
            An Int specifying the maximum number of increments in a step. The default value is 100.
        initialInc
            A Float specifying the initial time increment. The default value is the total time
            period for the step.
        minInc
            A Float specifying the minimum time increment allowed. The default value is the smaller
            of the suggested initial time increment or 10−5 times the total time period.
        maxInc
            A Float specifying the maximum time increment allowed. The default value is the total
            time period for the step.
        end
            A SymbolicConstant specifying the time period to be analyzed in a transient analysis.
            Possible values are PERIOD and SS. The default value is PERIOD.
        deltmx
            A Float specifying the maximum temperature change to be allowed in an increment in a
            transient analysis. The default value is 0.0.
        mxdem
            A Float specifying the maximum allowable emissivity change with temperature and field
            variables during an increment. The default value is 0.1.
        solutionTechnique
            A SymbolicConstant specifying the type of solution technique. Possible values are
            FULL_NEWTON and SEPARATED. The default value is FULL_NEWTON.
        matrixStorage
            A SymbolicConstant specifying the type of matrix storage. Possible values are SYMMETRIC,
            UNSYMMETRIC, and SOLVER_DEFAULT. The default value is SOLVER_DEFAULT.
        amplitude
            A SymbolicConstant specifying the amplitude variation for loading magnitudes during the
            step. The default value is STEP. Possible values are STEP and RAMP.
        extrapolation
            A SymbolicConstant specifying the type of extrapolation to use in determining the
            incremental solution for a nonlinear analysis. Possible values are NONE, LINEAR, and
            PARABOLIC. The default value is LINEAR.
        maintainAttributes
            A Boolean specifying whether to retain attributes from an existing step with the same
            name. The default value is False.
        convertSDI
            A SymbolicConstant specifying whether to force a new iteration if severe discontinuities
            occur during an iteration. Possible values are PROPAGATED, CONVERT_SDI_OFF, and
            CONVERT_SDI_ON. The default value is PROPAGATED.

        Returns
        -------
        step: CoupledThermalElectricStep
            A CoupledThermalElectricStep object.
        """
        self.steps[name] = step = CoupledThermalElectricStep(
            name,
            previous,
            description,
            response,
            timePeriod,
            timeIncrementationMethod,
            maxNumInc,
            initialInc,
            minInc,
            maxInc,
            end,
            deltmx,
            mxdem,
            solutionTechnique,
            matrixStorage,
            amplitude,
            extrapolation,
            maintainAttributes,
            convertSDI,
        )
        return step

    @abaqus_method_doc
    def DirectCyclicStep(
        self,
        name: str,
        previous: str,
        description: str = "",
        timePeriod: float = 1,
        timeIncrementationMethod: Literal[C.AUTOMATIC, C.FIXED] = AUTOMATIC,
        maxNumInc: int = 100,
        initialInc: Optional[float] = None,
        minInc: Optional[float] = None,
        maxInc: Optional[float] = None,
        maxNumIterations: int = 200,
        initialTerms: int = 11,
        maxTerms: int = 25,
        termsIncrement: int = 5,
        deltmx: float = 0,
        cetol: float = 0,
        timePoints: str = NONE,
        fatigue: Boolean = OFF,
        continueAnalysis: Boolean = OFF,
        minCycleInc: int = 100,
        maxCycleInc: int = 1000,
        maxNumCycles: Literal[C.DEFAULT] = DEFAULT,
        damageExtrapolationTolerance: float = 1,
        matrixStorage: Literal[C.SYMMETRIC, C.SOLVER_DEFAULT, C.UNSYMMETRIC] = SOLVER_DEFAULT,
        extrapolation: Literal[C.PARABOLIC, C.NONE, C.LINEAR] = LINEAR,
        maintainAttributes: Boolean = False,
        convertSDI: Literal[C.CONVERT_SDI_OFF, C.PROPAGATED, C.CONVERT_SDI_ON] = PROPAGATED,
    ) -> DirectCyclicStep:
        """This method creates a DirectCyclicStep object.

        .. note::
            This function can be accessed by::

                mdb.models[name].DirectCyclicStep

        Parameters
        ----------
        name
            A String specifying the repository key.
        previous
            A String specifying the name of the previous step. The new step appears after this step
            in the list of analysis steps.
        description
            A String specifying a description of the new step. The default value is an empty string.
        timePeriod
            A Float specifying the time of single loading cycle. The default value is 1.0.
        timeIncrementationMethod
            A SymbolicConstant specifying the time incrementation method to be used. Possible values
            are FIXED and AUTOMATIC. The default value is AUTOMATIC.
        maxNumInc
            An Int specifying the maximum number of increments in a step. The default value is 100.
        initialInc
            A Float specifying the initial time increment. The default value is the total time
            period for the step.
        minInc
            A Float specifying the minimum time increment allowed. The default value is the smaller
            of the suggested initial time increment or 10−5 times the total time period.
        maxInc
            A Float specifying the maximum time increment allowed. The default value is the total
            time period for the step.
        maxNumIterations
            An Int specifying the maximum number of iterations in a step. The default value is 200.
        initialTerms
            An Int specifying the initial number of terms in the Fourier series. The default value
            is 11.
        maxTerms
            An Int specifying the maximum number of terms in the Fourier series. The default value
            is 25.
        termsIncrement
            An Int specifying the increment in number of terms in the Fourier series. The default
            value is 5.
        deltmx
            A Float specifying the maximum temperature change to be allowed in an increment. The
            default value is 0.0.
        cetol
            A Float specifying the maximum difference in the creep strain increment calculated from
            the creep strain rates at the beginning and end of the increment. The default value is
            0.0.
        timePoints
            None or a String specifying a String specifying the name of a time point object used to
            determine at which times the response of the structure will be evaluated. The default
            value is NONE.
        fatigue
            A Boolean specifying whether to include low-cycle fatigue analysis. The default value is
            OFF.
        continueAnalysis
            A Boolean specifying whether the displacement solution in the Fourier series obtained in
            the previous direct cyclic step is used as the starting values for the current step. The
            default value is OFF.
        minCycleInc
            An Int specifying the minimum number of cycles over which the damage is extrapolated
            forward. The default value is 100.
        maxCycleInc
            An Int specifying the maximum number of cycles over which the damage is extrapolated
            forward. The default value is 1000.
        maxNumCycles
            The SymbolicConstant DEFAULT or an Int specifying the maximum number of cycles allowed
            in a step or DEFAULT. A value of 1 plus half of the maximum number of cycles will be
            used if DEFAULT is specified. The default value is DEFAULT.
        damageExtrapolationTolerance
            A Float specifying the maximum extrapolated damage increment. The default value is 1.0.
        matrixStorage
            A SymbolicConstant specifying the type of matrix storage. Possible values are SYMMETRIC,
            UNSYMMETRIC, and SOLVER_DEFAULT. The default value is SOLVER_DEFAULT.
        extrapolation
            A SymbolicConstant specifying the type of extrapolation to use in determining the
            incremental solution for a nonlinear analysis. Possible values are NONE, LINEAR, and
            PARABOLIC. The default value is LINEAR.
        maintainAttributes
            A Boolean specifying whether to retain attributes from an existing step with the same
            name. The default value is False.
        convertSDI
            A SymbolicConstant specifying whether to force a new iteration if severe discontinuities
            occur during an iteration. Possible values are PROPAGATED, CONVERT_SDI_OFF, and
            CONVERT_SDI_ON. The default value is PROPAGATED.

        Returns
        -------
        step: DirectCyclicStep
            A DirectCyclicStep object.
        """
        self.steps[name] = step = DirectCyclicStep(
            name,
            previous,
            description,
            timePeriod,
            timeIncrementationMethod,
            maxNumInc,
            initialInc,
            minInc,
            maxInc,
            maxNumIterations,
            initialTerms,
            maxTerms,
            termsIncrement,
            deltmx,
            cetol,
            timePoints,
            fatigue,
            continueAnalysis,
            minCycleInc,
            maxCycleInc,
            maxNumCycles,
            damageExtrapolationTolerance,
            matrixStorage,
            extrapolation,
            maintainAttributes,
            convertSDI,
        )
        return step

    @abaqus_method_doc
    def EmagTimeHarmonicStep(
        self,
        name: str,
        previous: str,
        frequencyRange: EmagTimeHarmonicFrequencyArray,
        description: str = "",
        factorization: Literal[C.COMPLEX, C.REAL_ONLY] = COMPLEX,
    ) -> EmagTimeHarmonicStep:
        """This method creates a EmagTimeHarmonicStep object.

        .. note::
            This function can be accessed by::

                mdb.models[name].EmagTimeHarmonicStep

        Parameters
        ----------
        name
            A String specifying the repository key.
        previous
            A String specifying the name of the previous step. The new step appears after this step
            in the list of analysis steps.
        frequencyRange
            An EmagTimeHarmonicFrequencyArray object.
        description
            A String specifying a description of the new step. The default value is an empty string.
        factorization
            A SymbolicConstant specifying whether damping terms are to be ignored so that a real,
            rather than a complex, system matrix is factored. Possible values are REAL_ONLY and
            COMPLEX. The default value is COMPLEX.

        Returns
        -------
        step: EmagTimeHarmonicStep
            An EmagTimeHarmonicStep object.
        """
        self.steps[name] = step = EmagTimeHarmonicStep(name, previous, frequencyRange, description, factorization)
        return step

    @abaqus_method_doc
    def ExplicitDynamicsStep(
        self,
        name: str,
        previous: str,
        description: str = "",
        timePeriod: float = 1,
        nlgeom: Boolean = ON,
        adiabatic: Boolean = OFF,
        timeIncrementationMethod: Literal[
            C.FIXED_EBE, C.AUTOMATIC_GLOBAL, C.AUTOMATIC_EBE, C.FIXED_USER_DEFINED_INC
        ] = AUTOMATIC_GLOBAL,
        maxIncrement: Optional[float] = None,
        scaleFactor: float = 1,
        massScaling: Union[MassScalingArray, Literal[C.PREVIOUS_STEP]] = PREVIOUS_STEP,
        linearBulkViscosity: float = 0,
        quadBulkViscosity: float = 1,
        userDefinedInc: Optional[float] = None,
        maintainAttributes: Boolean = False,
        improvedDtMethod: Boolean = ON,
    ) -> ExplicitDynamicsStep:
        """This method creates an ExplicitDynamicsStep object.

        .. note::
            This function can be accessed by::

                mdb.models[name].ExplicitDynamicsStep

        Parameters
        ----------
        name
            A String specifying the repository key.
        previous
            A String specifying the name of the previous step. The new step appears after this step
            in the list of analysis steps.
        description
            A String specifying a description of the new step. The default value is an empty string.
        timePeriod
            A Float specifying the total time period for the step. The default value is 1.0.
        nlgeom
            A Boolean specifying whether geometric nonlinearities should be accounted for during the
            step. The default value is ON.
        adiabatic
            A Boolean specifying that an adiabatic stress analysis is to be performed. The default
            value is OFF.
        timeIncrementationMethod
            A SymbolicConstant specifying the time incrementation method to be used. Possible values
            are AUTOMATIC_GLOBAL, AUTOMATIC_EBE, FIXED_USER_DEFINED_INC, and FIXED_EBE. The default
            value is AUTOMATIC_GLOBAL.
        maxIncrement
            None or a Float specifying the maximum time increment. If there is no upper limit,
            **maxIncrement** = None. This argument is required only when
            **timeIncrementationMethod** = AUTOMATIC_GLOBAL or AUTOMATIC_EBE. The default value is None.
        scaleFactor
            A Float specifying the factor that is used to scale the time increment. This argument is
            required only when **timeIncrementationMethod** = AUTOMATIC_GLOBAL, AUTOMATIC_EBE, or
            FIXED_EBE. The default value is 1.0.
        massScaling
            A MassScalingArray object specifying
            mass scaling controls. The default value is PREVIOUS_STEP.
        linearBulkViscosity
            A Float specifying the linear bulk viscosity parameter, b1b1. The default value is 0.06.
        quadBulkViscosity
            A Float specifying the quadratic bulk viscosity parameter, b2b2. The default value is
            1.2.
        userDefinedInc
            None or a Float specifying the user-defined time increment. This argument is required
            only when **timeIncrementationMethod** = FIXED_USER_DEFINED_INC. The default value is None.
        maintainAttributes
            A Boolean specifying whether to retain attributes from an existing step with the same
            name. The default value is False.
        improvedDtMethod
            A Boolean specifying whether to use the "improved" (**improvedDtMethod** = ON) or
            "conservative" (**improvedDtMethod** = OFF) method to estimate the element stable time
            increment for three-dimensional continuum elements and elements with plane stress
            formulations (shell, membrane, and two-dimensional plane stress elements). The default
            value is ON.

            .. versionadded:: 2018
                The **improvedDtMethod** argument was added.

        Returns
        -------
        step: ExplicitDynamicsStep
            An ExplicitDynamicsStep object.
        """
        self.steps[name] = step = ExplicitDynamicsStep(
            name,
            previous,
            description,
            timePeriod,
            nlgeom,
            adiabatic,
            timeIncrementationMethod,
            maxIncrement,
            scaleFactor,
            massScaling,
            linearBulkViscosity,
            quadBulkViscosity,
            userDefinedInc,
            maintainAttributes,
            improvedDtMethod,
        )
        return step

    @abaqus_method_doc
    def FrequencyStep(
        self,
        name: str,
        previous: str,
        eigensolver: Literal[C.AMS, C.LANCZOS, C.SUBSPACE],
        numEigen: Literal[C.ALL] = ALL,
        description: str = "",
        shift: float = 0,
        minEigen: Optional[float] = None,
        maxEigen: Optional[float] = None,
        vectors: Optional[int] = None,
        maxIterations: int = 30,
        blockSize: Literal[C.DEFAULT] = DEFAULT,
        maxBlocks: Literal[C.DEFAULT] = DEFAULT,
        normalization: Literal[C.MASS, C.DISPLACEMENT] = DISPLACEMENT,
        propertyEvaluationFrequency: Optional[float] = None,
        projectDamping: Boolean = ON,
        acousticCoupling: Literal[C.AC_OFF, C.AC_ON, C.TIE, C.AC_PROJECTION] = AC_ON,
        acousticRangeFactor: float = 1,
        frictionDamping: Boolean = OFF,
        matrixStorage: Literal[C.SYMMETRIC, C.SOLVER_DEFAULT, C.UNSYMMETRIC] = SOLVER_DEFAULT,
        maintainAttributes: Boolean = False,
        simLinearDynamics: Boolean = OFF,
        residualModes: Boolean = OFF,
        substructureCutoffMultiplier: float = 5,
        firstCutoffMultiplier: float = 1,
        secondCutoffMultiplier: float = 1,
        residualModeRegion: Optional[str] = None,
        residualModeDof: Optional[str] = None,
        limitSavedEigenvectorRegion: Optional[SymbolicConstant] = None,
    ) -> FrequencyStep:
        """This method creates a FrequencyStep object.

        .. note::
            This function can be accessed by::

                mdb.models[name].FrequencyStep

        Parameters
        ----------
        name
            A String specifying the repository key.
        previous
            A String specifying the name of the previous step. The new step appears after this step
            in the list of analysis steps.
        eigensolver
            A SymbolicConstant specifying the eigensolver. Possible values are LANCZOS, SUBSPACE,
            and AMS.The following optional arguments are ignored unless **eigensolver** = LANCZOS:
            **blockSize**, **maxBlocks**, **normalization**, **propertyEvaluationFrequency**.The following
            optional arguments are ignored unless **eigensolver** = LANCZOS or AMS: **minEigen**,
            **maxEigen**, and **acousticCoupling**.The following optional arguments are ignored unless
            **eigensolver** = AMS: **projectDamping**, **acousticRangeFactor**,
            **substructureCutoffMultiplier**, **firstCutoffMultiplier**, **secondCutoffMultiplier**,
            **residualModeRegion**, **regionalModeDof**, and **limitSavedEigenvectorRegion**.
        numEigen
            The SymbolicConstant ALL or an Int specifying the number of eigenvalues to be calculated
            or ALL. The default value is ALL.
        description
            A String specifying a description of the new step. The default value is an empty string.
        shift
            A Float specifying the shift point in cycles per time. The default value is 0.0.
        minEigen
            None or a Float specifying the minimum frequency of interest in cycles per time. The
            default value is None.
        maxEigen
            None or a Float specifying the maximum frequency of interest in cycles per time. The
            default value is None.
        vectors
            None or an Int specifying the number of vectors used in the iteration. The default is
            the minimum of (2*n*, **n** + 8), where **n** is the number of eigenvalues requested. The
            default value is None.
        maxIterations
            An Int specifying the maximum number of iterations. The default value is 30.
        blockSize
            A SymbolicConstant specifying the size of the Lanczos block steps. The default value is
            DEFAULT.
        maxBlocks
            A SymbolicConstant specifying the maximum number of Lanczos block steps within each
            Lanczos run. The default value is DEFAULT.
        normalization
            A SymbolicConstant specifying the method for normalizing eigenvectors. Possible values
            are DISPLACEMENT and MASS. The default value is DISPLACEMENT.A value of DISPLACEMENT
            indicates normalizing the eigenvectors so that the largest displacement entry in each
            vector is unity. A value of MASS indicates normalizing the eigenvectors with respect to
            the structure's mass matrix, which results in scaling the eigenvectors so that the
            generalized mass for each vector is unity.
        propertyEvaluationFrequency
            None or a Float specifying the frequency at which to evaluate frequency-dependent
            properties for viscoelasticity, springs, and dashpots during the eigenvalue extraction.
            If the value is None, the analysis product will evaluate the stiffness associated with
            frequency-dependent springs and dashpots at zero frequency and will not consider the
            stiffness contributions from frequency-domain viscoelasticity in the step. The default
            value is None.
        projectDamping
            A Boolean specifying whether to include projection of viscous and structural damping
            operators during **AMS** eigenvalue extraction. Valid only when **eigenSolver** = AMS. The
            default value is ON.
        acousticCoupling
            A SymbolicConstant specifying the type of acoustic-structural coupling in models with
            acoustic and structural elements coupled using the TIE option or in models with ASI-type
            elements. Possible values are AC_ON, AC_OFF, and AC_PROJECTION. The default value is
            AC_ON.
        acousticRangeFactor
            A Float specifying the ratio of the maximum acoustic frequency to the maximum structural
            frequency. The default value is 1.0.
        frictionDamping
            A Boolean specifying whether to add to the damping matrix contributions due to friction
            effects. The default value is OFF.
        matrixStorage
            A SymbolicConstant specifying the type of matrix storage. Possible values are SYMMETRIC,
            UNSYMMETRIC, and SOLVER_DEFAULT. The default value is SOLVER_DEFAULT.
        maintainAttributes
            A Boolean specifying whether to retain attributes from an existing step with the same
            name. The default value is False.
        simLinearDynamics
            A Boolean specifying whether to activate the SIM-based linear dynamics procedures. The
            default value is OFF.
        residualModes
            A Boolean specifying whether to include residual modes from an immediately preceding
            Static, Linear Perturbation step. The default value is OFF.
        substructureCutoffMultiplier
            A Float specifying the cutoff frequency for substructure eigenproblems, defined as a
            multiplier of the maximum frequency of interest. The default value is 5.0.
        firstCutoffMultiplier
            A Float specifying the first cutoff frequency for a reduced eigenproblem, defined as a
            multiplier of the maximum frequency of interest. The default value is 1.7.
        secondCutoffMultiplier
            A Float specifying the second cutoff frequency for a reduced eigenproblem defined as a
            multiplier of the maximum frequency of interest. The default value is 1.1.
        residualModeRegion
            None or a sequence of Strings specifying the name of a region for which residual modes
            are requested. The default value is None.
        residualModeDof
            None or a sequence of Ints specifying the degree of freedom for which residual modes are
            requested. The default value is None.
        limitSavedEigenvectorRegion
            None or a Region object specifying a region for which eigenvectors should be saved or
            the SymbolicConstant None representing the whole model. The default value is None.

        Returns
        -------
        step: FrequencyStep
            A FrequencyStep object.
        """
        self.steps[name] = step = FrequencyStep(
            name,
            previous,
            eigensolver,
            numEigen,
            description,
            shift,
            minEigen,
            maxEigen,
            vectors,
            maxIterations,
            blockSize,
            maxBlocks,
            normalization,
            propertyEvaluationFrequency,
            projectDamping,
            acousticCoupling,
            acousticRangeFactor,
            frictionDamping,
            matrixStorage,
            maintainAttributes,
            simLinearDynamics,
            residualModes,
            substructureCutoffMultiplier,
            firstCutoffMultiplier,
            secondCutoffMultiplier,
            residualModeRegion,
            residualModeDof,
            limitSavedEigenvectorRegion,
        )
        return step

    @abaqus_method_doc
    def GeostaticStep(
        self,
        name: str,
        previous: str,
        description: str = "",
        nlgeom: Boolean = OFF,
        matrixSolver: Literal[C.DIRECT, C.ITERATIVE] = DIRECT,
        matrixStorage: Literal[C.SYMMETRIC, C.SOLVER_DEFAULT, C.UNSYMMETRIC] = SOLVER_DEFAULT,
        maintainAttributes: Boolean = False,
        solutionTechnique: Literal[C.QUASI_NEWTON, C.FULL_NEWTON] = FULL_NEWTON,
        reformKernel: int = 8,
        convertSDI: Literal[C.CONVERT_SDI_OFF, C.PROPAGATED, C.CONVERT_SDI_ON] = PROPAGATED,
        utol: Optional[float] = None,
        timePeriod: float = 1,
        timeIncrementationMethod: Literal[C.AUTOMATIC, C.FIXED] = AUTOMATIC,
        maxNumInc: int = 100,
        initialInc: Optional[float] = None,
        minInc: Optional[float] = None,
        maxInc: Optional[float] = None,
    ) -> GeostaticStep:
        """This method creates a GeostaticStep object.

        .. note::
            This function can be accessed by::

                mdb.models[name].GeostaticStep

        Parameters
        ----------
        name
            A String specifying the repository key.
        previous
            A String specifying the name of the previous step. The new step appears after this step
            in the list of analysis steps.
        description
            A String specifying a description of the new step. The default value is an empty string.
        nlgeom
            A Boolean specifying whether geometric nonlinearities should be accounted for during the
            step. The default value is OFF.
        matrixSolver
            A SymbolicConstant specifying the type of solver. Possible values are DIRECT and
            ITERATIVE. The default value is DIRECT.
        matrixStorage
            A SymbolicConstant specifying the type of matrix storage. Possible values are SYMMETRIC,
            UNSYMMETRIC, and SOLVER_DEFAULT. The default value is SOLVER_DEFAULT.
        maintainAttributes
            A Boolean specifying whether to retain attributes from an existing step with the same
            name. The default value is False.
        solutionTechnique
            A SymbolicConstant specifying the technique used to for solving nonlinear equations.
            Possible values are FULL_NEWTON and QUASI_NEWTON. The default value is FULL_NEWTON.
        reformKernel
            An Int specifying the number of quasi-Newton iterations allowed before the kernel matrix
            is reformed.. The default value is 8.
        convertSDI
            A SymbolicConstant specifying whether to force a new iteration if severe discontinuities
            occur during an iteration. Possible values are PROPAGATED, CONVERT_SDI_OFF, and
            CONVERT_SDI_ON. The default value is PROPAGATED.
        utol
            None or a Float specifying the tolerance for maximum change of displacements. The
            default value is None.
        timePeriod
            A Float specifying the total time period. The default value is 1.0. Note: This parameter
            is ignored unless **timeIncrementationMethod** = AUTOMATIC.
        timeIncrementationMethod
            A SymbolicConstant specifying the time incrementation method to be used. Possible values
            are FIXED and AUTOMATIC. The default value is AUTOMATIC.
        maxNumInc
            An Int specifying the maximum number of increments in a step. The default value is 100.

            .. versionadded:: 2017
                The ``maxNumInc`` attribute was added to the GeostaticStep class.
        initialInc
            A Float specifying the initial time increment. The default value is the total time
            period for the step. Note: This parameter is ignored unless
            **timeIncrementationMethod** = AUTOMATIC.
        minInc
            A Float specifying the minimum time increment allowed. The default value is the smaller
            of the suggested initial time increment or 10−5 times the total time period. Note: This
            parameter is ignored unless **timeIncrementationMethod** = AUTOMATIC.
        maxInc
            A Float specifying the maximum time increment allowed. The default value is the total
            time period for the step. Note: This parameter is ignored unless
            **timeIncrementationMethod** = AUTOMATIC.

        Returns
        -------
        step: GeostaticStep
            A GeostaticStep object.
        """
        self.steps[name] = step = GeostaticStep(
            name,
            previous,
            description,
            nlgeom,
            matrixSolver,
            matrixStorage,
            maintainAttributes,
            solutionTechnique,
            reformKernel,
            convertSDI,
            utol,
            timePeriod,
            timeIncrementationMethod,
            maxNumInc,
            initialInc,
            minInc,
            maxInc,
        )
        return step

    @abaqus_method_doc
    def HeatTransferStep(
        self,
        name: str,
        previous: str,
        description: str = "",
        response: Literal[C.TRANSIENT, C.STEADY_STATE] = TRANSIENT,
        timePeriod: float = 1,
        timeIncrementationMethod: Literal[C.AUTOMATIC, C.FIXED] = AUTOMATIC,
        maxNumInc: int = 100,
        initialInc: Optional[float] = None,
        minInc: Optional[float] = None,
        maxInc: Optional[float] = None,
        end: Optional[float] = None,
        deltmx: float = 0,
        mxdem: float = 0,
        amplitude: Literal[C.STEP, C.RAMP] = STEP,
        extrapolation: Literal[C.PARABOLIC, C.NONE, C.LINEAR] = LINEAR,
        matrixSolver: Literal[C.DIRECT, C.ITERATIVE] = DIRECT,
        matrixStorage: Literal[C.SYMMETRIC, C.SOLVER_DEFAULT, C.UNSYMMETRIC] = SOLVER_DEFAULT,
        maintainAttributes: Boolean = False,
        solutionTechnique: Literal[C.QUASI_NEWTON, C.FULL_NEWTON] = FULL_NEWTON,
        reformKernel: int = 8,
        convertSDI: Literal[C.CONVERT_SDI_OFF, C.PROPAGATED, C.CONVERT_SDI_ON] = PROPAGATED,
    ) -> HeatTransferStep:
        """This method creates a HeatTransferStep object.

        .. note::
            This function can be accessed by::

                mdb.models[name].HeatTransferStep

        Parameters
        ----------
        name
            A String specifying the repository key.
        previous
            A String specifying the name of the previous step. The new step appears after this step
            in the list of analysis steps.
        description
            A String specifying a description of the new step. The default value is an empty string.
        response
            A SymbolicConstant specifying the analysis type. Possible values are STEADY_STATE and
            TRANSIENT. The default value is TRANSIENT.
        timePeriod
            A Float specifying the total time period. The default value is 1.0.
        timeIncrementationMethod
            A SymbolicConstant specifying the time incrementation method to be used. Possible values
            are FIXED and AUTOMATIC. The default value is AUTOMATIC.
        maxNumInc
            An Int specifying the maximum number of increments in a step. The default value is 100.
        initialInc
            A Float specifying the initial time increment. The default value is the total time
            period for the step.
        minInc
            A Float specifying the minimum time increment allowed. The default value is the smaller
            of 0.8 times the initial time increment or 10−5 times the total time period.
        maxInc
            A Float specifying the maximum time increment allowed. The default value is the total
            time period for the step.
        end
            None or a Float specifying the temperature change rate (temperature per time) used to
            define steady state. When all nodal temperatures are changing at less than this rate,
            the solution terminates. The default value is None. Note: This parameter is ignored unless
            **response** = STEADY_STATE.
        deltmx
            A Float specifying the maximum temperature change to be allowed in an increment during a
            transient heat transfer analysis. The default value is 0.0.
        mxdem
            A Float specifying the maximum allowable emissivity change with temperature and field
            variables during an increment. The default value is 0.1.
        amplitude
            A SymbolicConstant specifying the amplitude variation for loading magnitudes during the
            step. The default is STEP. Possible values are STEP and RAMP.
        extrapolation
            A SymbolicConstant specifying the type of extrapolation to use in determining the
            incremental solution for a nonlinear analysis. Possible values are NONE, LINEAR, and
            PARABOLIC. The default value is LINEAR.
        matrixSolver
            A SymbolicConstant specifying the type of solver. Possible values are DIRECT and
            ITERATIVE. The default value is DIRECT.
        matrixStorage
            A SymbolicConstant specifying the type of matrix storage. Possible values are SYMMETRIC,
            UNSYMMETRIC, and SOLVER_DEFAULT. The default value is SOLVER_DEFAULT.
        maintainAttributes
            A Boolean specifying whether to retain attributes from an existing step with the same
            name. The default value is False.
        solutionTechnique
            A SymbolicConstant specifying the technique used to for solving nonlinear equations.
            Possible values are FULL_NEWTON and QUASI_NEWTON. The default value is FULL_NEWTON.
        reformKernel
            An Int specifying the number of quasi-Newton iterations allowed before the kernel matrix
            is reformed.. The default value is 8.
        convertSDI
            A SymbolicConstant specifying whether to force a new iteration if severe discontinuities
            occur during an iteration. Possible values are PROPAGATED, CONVERT_SDI_OFF, and
            CONVERT_SDI_ON. The default value is PROPAGATED.

        Returns
        -------
        step: HeatTransferStep
            A HeatTransferStep object.
        """
        self.steps[name] = step = HeatTransferStep(
            name,
            previous,
            description,
            response,
            timePeriod,
            timeIncrementationMethod,
            maxNumInc,
            initialInc,
            minInc,
            maxInc,
            end,
            deltmx,
            mxdem,
            amplitude,
            extrapolation,
            matrixSolver,
            matrixStorage,
            maintainAttributes,
            solutionTechnique,
            reformKernel,
            convertSDI,
        )
        return step

    @abaqus_method_doc
    def ImplicitDynamicsStep(
        self,
        name: str,
        previous: str,
        description: str = "",
        timePeriod: float = 1,
        nlgeom: Boolean = OFF,
        matrixStorage: Literal[C.SYMMETRIC, C.SOLVER_DEFAULT, C.UNSYMMETRIC] = SOLVER_DEFAULT,
        application: Literal[
            C.ANALYSIS_PRODUCT_DEFAULT, C.QUASI_STATIC, C.TRANSIENT_FIDELITY, C.MODERATE_DISSIPATION
        ] = ANALYSIS_PRODUCT_DEFAULT,
        adiabatic: Boolean = OFF,
        timeIncrementationMethod: Literal[C.AUTOMATIC, C.FIXED] = AUTOMATIC,
        maxNumInc: int = 100,
        initialInc: Optional[float] = None,
        minInc: Optional[float] = None,
        maxInc: Union[Literal[C.DEFAULT], float] = DEFAULT,
        hafTolMethod: Literal[C.ANALYSIS_PRODUCT_DEFAULT, C.VALUE, C.SCALE] = VALUE,
        haftol: Optional[float] = None,
        halfIncScaleFactor: Optional[float] = None,
        nohaf: Boolean = OFF,
        amplitude: Literal[C.STEP, C.RAMP] = STEP,
        alpha: Union[Literal[C.DEFAULT], float] = DEFAULT,
        initialConditions: Literal[C.BYPASS, C.DEFAULT, C.ALLOW] = DEFAULT,
        extrapolation: Literal[
            C.ANALYSIS_PRODUCT_DEFAULT, C.PARABOLIC, C.VELOCITY_PARABOLIC, C.NONE, C.LINEAR
        ] = ANALYSIS_PRODUCT_DEFAULT,
        noStop: Boolean = OFF,
        maintainAttributes: Boolean = False,
        solutionTechnique: Literal[C.QUASI_NEWTON, C.FULL_NEWTON] = FULL_NEWTON,
        reformKernel: int = 8,
        convertSDI: Literal[C.CONVERT_SDI_OFF, C.PROPAGATED, C.CONVERT_SDI_ON] = PROPAGATED,
    ) -> ImplicitDynamicsStep:
        """This method creates an ImplicitDynamicsStep object.

        .. note::
            This function can be accessed by::

                mdb.models[name].ImplicitDynamicsStep

        Parameters
        ----------
        name
            A String specifying the repository key.
        previous
            A String specifying the name of the previous step. The new step appears after this step
            in the list of analysis steps.
        description
            A String specifying a description of the new step. The default value is an empty string.
        timePeriod
            A Float specifying the total time period of the step. The default value is 1.0.
        nlgeom
            A Boolean specifying whether geometric nonlinearities should be accounted for during the
            step. The default value is based on the previous step.
        matrixStorage
            A SymbolicConstant specifying the type of matrix storage. Possible values are SYMMETRIC,
            UNSYMMETRIC, and SOLVER_DEFAULT. The default value is SOLVER_DEFAULT.
        application
            A SymbolicConstant specifying the application type of the step. Possible values are
            ANALYSIS_PRODUCT_DEFAULT, TRANSIENT_FIDELITY, MODERATE_DISSIPATION, and QUASI_STATIC.
            The default value is ANALYSIS_PRODUCT_DEFAULT.
        adiabatic
            A Boolean specifying whether an adiabatic stress analysis is to be performed. The
            default value is OFF.
        timeIncrementationMethod
            A SymbolicConstant specifying the time incrementation method to be used. Possible values
            are FIXED and AUTOMATIC. The default value is AUTOMATIC.
        maxNumInc
            An Int specifying the maximum number of increments in a step. The default value is 100.
        initialInc
            A Float specifying the initial time increment. The default value is the total time
            period for the step.
        minInc
            A Float specifying the minimum time increment allowed. The default value is the smaller
            of the suggested initial time increment or 10−5 times the total time period.
        maxInc
            The SymbolicConstant DEFAULT or a Float specifying the maximum time increment allowed.
        hafTolMethod
            A SymbolicConstant specifying the way of specifying half-increment residual tolerance
            with the automatic time incrementation scheme. Possible values are
            ANALYSIS_PRODUCT_DEFAULT, VALUE, and SCALE. The default value is VALUE.
        haftol
            None or a Float specifying the half-increment residual tolerance to be used with the
            automatic time incrementation scheme. The default value is None.
        halfIncScaleFactor
            None or a Float specifying the half-increment residual tolerance scale factor to be used
            with the automatic time incrementation scheme. The default value is None.
        nohaf
            A Boolean specifying whether to suppress calculation of the half-increment residual. The
            default value is OFF.
        amplitude
            A SymbolicConstant specifying the amplitude variation for loading magnitudes during the
            step. Possible values are STEP and RAMP. The default value is STEP.
        alpha
            The SymbolicConstant DEFAULT or a Float specifying the nondefault value of the numerical
            (artificial) damping control parameter, αα, in the implicit operator. Possible values
            are −.333 <α< 0. The default value is DEFAULT.
        initialConditions
            A SymbolicConstant specifying whether accelerations should be calculated or recalculated
            at the beginning of the step. Possible values are DEFAULT, BYPASS, and ALLOW. The
            default value is DEFAULT.
        extrapolation
            A SymbolicConstant specifying the type of extrapolation to use in determining the
            incremental solution for a nonlinear analysis. Possible values are NONE, LINEAR,
            PARABOLIC, VELOCITY_PARABOLIC, and ANALYSIS_PRODUCT_DEFAULT. The default value is
            ANALYSIS_PRODUCT_DEFAULT.
        noStop
            A Boolean specifying whether to accept the solution to an increment after the maximum
            number of iterations allowed have been completed, even if the equilibrium tolerances are
            not satisfied. The default value is OFF.Warning:You should set **noStop** = OFF only in
            special cases when you have a thorough understanding of how to interpret the results.
        maintainAttributes
            A Boolean specifying whether to retain attributes from an existing step with the same
            name. The default value is False.
        solutionTechnique
            A SymbolicConstant specifying the technique used to for solving nonlinear equations.
            Possible values are FULL_NEWTON and QUASI_NEWTON. The default value is FULL_NEWTON.
        reformKernel
            An Int specifying the number of quasi-Newton iterations allowed before the kernel matrix
            is reformed.. The default value is 8.
        convertSDI
            A SymbolicConstant specifying whether to force a new iteration if severe discontinuities
            occur during an iteration. Possible values are PROPAGATED, CONVERT_SDI_OFF, and
            CONVERT_SDI_ON. The default value is PROPAGATED.

        Returns
        -------
        step: ImplicitDynamicsStep
            An ImplicitDynamicsStep object.
        """
        self.steps[name] = step = ImplicitDynamicsStep(
            name,
            previous,
            description,
            timePeriod,
            nlgeom,
            matrixStorage,
            application,
            adiabatic,
            timeIncrementationMethod,
            maxNumInc,
            initialInc,
            minInc,
            maxInc,
            hafTolMethod,
            haftol,
            halfIncScaleFactor,
            nohaf,
            amplitude,
            alpha,
            initialConditions,
            extrapolation,
            noStop,
            maintainAttributes,
            solutionTechnique,
            reformKernel,
            convertSDI,
        )
        return step

    @abaqus_method_doc
    def MassDiffusionStep(
        self,
        name: str,
        previous: str,
        description: str = "",
        response: Literal[C.TRANSIENT, C.STEADY_STATE] = TRANSIENT,
        timePeriod: float = 1,
        timeIncrementationMethod: Literal[C.AUTOMATIC, C.FIXED] = AUTOMATIC,
        maxNumInc: int = 100,
        initialInc: Optional[float] = None,
        minInc: Optional[float] = None,
        maxInc: Optional[float] = None,
        end: Literal[C.SS, C.PERIOD] = PERIOD,
        dcmax: float = 0,
        amplitude: Literal[C.STEP, C.RAMP] = STEP,
        extrapolation: Literal[C.PARABOLIC, C.NONE, C.LINEAR] = LINEAR,
        maintainAttributes: Boolean = False,
        convertSDI: Literal[C.CONVERT_SDI_OFF, C.PROPAGATED, C.CONVERT_SDI_ON] = PROPAGATED,
    ) -> MassDiffusionStep:
        """This method creates a MassDiffusionStep object.

        .. note::
            This function can be accessed by::

                mdb.models[name].MassDiffusionStep

        Parameters
        ----------
        name
            A String specifying the repository key.
        previous
            A String specifying the name of the previous step. The new step appears after this step
            in the list of analysis steps.
        description
            A String specifying a description of the new step. The default value is an empty string.
        response
            A SymbolicConstant specifying the analysis type. Possible values are STEADY_STATE and
            TRANSIENT. The default value is TRANSIENT.
        timePeriod
            A Float specifying the total time period. The default value is 1.0.
        timeIncrementationMethod
            A SymbolicConstant specifying the time incrementation method to be used. Possible values
            are FIXED and AUTOMATIC. The default value is AUTOMATIC.
        maxNumInc
            An Int specifying the maximum number of increments in a step. The default value is 100.
        initialInc
            A Float specifying the initial time increment. The default value is the total time
            period for the step.
        minInc
            A Float specifying the minimum time increment allowed. The default value is the smaller
            of 0.8 times the initial time increment or 10−5 times the total time period.
        maxInc
            A Float specifying the maximum time increment allowed. The default value is the total
            time period for the step.
        end
            A SymbolicConstant specifying the time period to be analyzed in a transient analysis.
            Possible values are PERIOD and SS. The default value is PERIOD.
        dcmax
            A Float specifying the maximum normalized concentration change to be allowed in an
            increment. The default value is 0.0.
        amplitude
            A SymbolicConstant specifying the amplitude variation for loading magnitudes during the
            step. The default is STEP. Possible values are STEP and RAMP.
        extrapolation
            A SymbolicConstant specifying the type of extrapolation to use in determining the
            incremental solution for a nonlinear analysis. Possible values are NONE, LINEAR, and
            PARABOLIC. The default value is LINEAR.
        maintainAttributes
            A Boolean specifying whether to retain attributes from an existing step with the same
            name. The default value is False.
        convertSDI
            A SymbolicConstant specifying whether to force a new iteration if severe discontinuities
            occur during an iteration. Possible values are PROPAGATED, CONVERT_SDI_OFF, and
            CONVERT_SDI_ON. The default value is PROPAGATED.

        Returns
        -------
        step: MassDiffusionStep
            A MassDiffusionStep object.
        """
        self.steps[name] = step = MassDiffusionStep(
            name,
            previous,
            description,
            response,
            timePeriod,
            timeIncrementationMethod,
            maxNumInc,
            initialInc,
            minInc,
            maxInc,
            end,
            dcmax,
            amplitude,
            extrapolation,
            maintainAttributes,
            convertSDI,
        )
        return step

    @abaqus_method_doc
    def ModalDynamicsStep(
        self,
        name: str,
        previous: str,
        description: str = "",
        continueAnalysis: Boolean = OFF,
        timePeriod: float = 1,
        incSize: float = 1,
        directDamping: Optional[DirectDamping] = None,
        compositeDamping: Optional[CompositeDamping] = None,
        rayleighDamping: Optional[RayleighDamping] = None,
        amplitude: Literal[C.STEP, C.RAMP] = STEP,
        maintainAttributes: Boolean = False,
        directDampingByFrequency: Optional[DirectDampingByFrequency] = None,
        rayleighDampingByFrequency: Optional[RayleighDampingByFrequency] = None,
    ) -> ModalDynamicsStep:
        """This method creates a ModalDynamicsStep object.

        .. note::
            This function can be accessed by::

                mdb.models[name].ModalDynamicsStep

        Parameters
        ----------
        name
            A String specifying the repository key.
        previous
            A String specifying the name of the previous step. The new step appears after this step
            in the list of analysis steps.
        description
            A String specifying a description of the new step. The default value is an empty string.
        continueAnalysis
            A Boolean specifying that the step starts with zero initial conditions. The default
            value is OFF.
        timePeriod
            A Float specifying the total time period. The default value is 1.0.
        incSize
            A Float specifying the time increment to be used. The default value is 1.0.
        directDamping
            A DirectDamping object.
        compositeDamping
            A CompositeDamping object.
        rayleighDamping
            A RayleighDamping object.
        amplitude
            A SymbolicConstant specifying the amplitude variation for loading magnitudes during the
            step. Possible values are STEP and RAMP. The default value is STEP.
        maintainAttributes
            A Boolean specifying whether to retain attributes from an existing step with the same
            name. The default value is False.
        directDampingByFrequency
            A DirectDampingByFrequency object.
        rayleighDampingByFrequency
            A RayleighDampingByFrequency object.

        Returns
        -------
        step: ModalDynamicsStep
            A ModalDynamicsStep object.
        """
        self.steps[name] = step = ModalDynamicsStep(
            name,
            previous,
            description,
            continueAnalysis,
            timePeriod,
            incSize,
            directDamping,
            compositeDamping,
            rayleighDamping,
            amplitude,
            maintainAttributes,
            directDampingByFrequency,
            rayleighDampingByFrequency,
        )
        return step

    @abaqus_method_doc
    def RandomResponseStep(
        self,
        name: str,
        previous: str,
        freq: RandomResponseFrequencyArray,
        description: str = "",
        scale: Literal[C.LOG, C.LINEAR] = LOG,
        directDamping: Optional[DirectDamping] = None,
        compositeDamping: Optional[CompositeDamping] = None,
        rayleighDamping: Optional[RayleighDamping] = None,
        structuralDamping: Optional[StructuralDamping] = None,
        directDampingByFrequency: Optional[DirectDampingByFrequency] = None,
        rayleighDampingByFrequency: Optional[RayleighDampingByFrequency] = None,
        structuralDampingByFrequency: Optional[StructuralDampingByFrequency] = None,
        maintainAttributes: Boolean = False,
    ) -> RandomResponseStep:
        """This method creates a RandomResponseStep object.

        .. note::
            This function can be accessed by::

                mdb.models[name].RandomResponseStep

        Parameters
        ----------
        name
            A String specifying the repository key.
        previous
            A String specifying the name of the previous step. The new step appears after this step
            in the list of analysis steps.
        freq
            A RandomResponseFrequencyArray object specifying frequencies over ranges of modes.
        description
            A String specifying a description of the new step. The default value is an empty string.
        scale
            A SymbolicConstant specifying the frequency scale. Possible values are LINEAR and LOG.
            The default value is LOG.
        directDamping
            A DirectDamping object.
        compositeDamping
            A CompositeDamping object.
        rayleighDamping
            A RayleighDamping object.
        structuralDamping
            A StructuralDamping object.
        directDampingByFrequency
            A DirectDampingByFrequency object.
        rayleighDampingByFrequency
            A RayleighDampingByFrequency object.
        structuralDampingByFrequency
            A StructuralDampingByFrequency object.
        maintainAttributes
            A Boolean specifying whether to retain attributes from an existing step with the same
            name. The default value is False.

        Returns
        -------
        step: RandomResponseStep
            A RandomResponseStep object.
        """
        self.steps[name] = step = RandomResponseStep(
            name,
            previous,
            freq,
            description,
            scale,
            directDamping,
            compositeDamping,
            rayleighDamping,
            structuralDamping,
            directDampingByFrequency,
            rayleighDampingByFrequency,
            structuralDampingByFrequency,
            maintainAttributes,
        )
        return step

    @abaqus_method_doc
    def ResponseSpectrumStep(
        self,
        name: str,
        previous: str,
        components: ResponseSpectrumComponentArray,
        description: str = "",
        comp: Literal[
            C.MULTIPLE_DIRECTION_FORTY_PERCENT_RULE,
            C.MULTIPLE_DIRECTION_THIRTY_PERCENT_RULE,
            C.MULTIPLE_DIRECTION_ABSOLUTE_SUM,
            C.MULTIPLE_DIRECTION_SRSS_SUM,
            C.SINGLE_DIRECTION,
        ] = SINGLE_DIRECTION,
        sum: Literal[C.DSC, C.NRL, C.CQC, C.TENP, C.GRP, C.ABS, C.SRSS] = ABS,
        directDamping: Optional[DirectDamping] = None,
        compositeDamping: Optional[CompositeDamping] = None,
        rayleighDamping: Optional[RayleighDamping] = None,
        directDampingByFrequency: Optional[DirectDampingByFrequency] = None,
        rayleighDampingByFrequency: Optional[RayleighDampingByFrequency] = None,
        maintainAttributes: Boolean = False,
    ) -> ResponseSpectrumStep:
        """This method creates a ResponseSpectrumStep object.

        .. note::
            This function can be accessed by::

                mdb.models[name].ResponseSpectrumStep

        Parameters
        ----------
        name
            A String specifying the repository key.
        previous
            A String specifying the name of the previous step. The new step appears after this step
            in the list of analysis steps.
        components
            A ResponseSpectrumComponentArray object.
        description
            A String specifying a description of the new step. The default value is an empty string.
        comp
            A SymbolicConstant specifying the order and method used to sum the components. Possible
            values are SINGLE_DIRECTION, MULTIPLE_DIRECTION_ABSOLUTE_SUM,
            MULTIPLE_DIRECTION_SRSS_SUM, MULTIPLE_DIRECTION_THIRTY_PERCENT_RULE, and
            MULTIPLE_DIRECTION_FORTY_PERCENT_RULE. The default value is SINGLE_DIRECTION.
        sum
            A SymbolicConstant specifying the method used to sum the components. Possible values are
            ABS, CQC, NRL, SRSS, TENP, DSC, and GRP. The default value is ABS.
        directDamping
            A DirectDamping object.
        compositeDamping
            A CompositeDamping object.
        rayleighDamping
            A RayleighDamping object.
        directDampingByFrequency
            A DirectDampingByFrequency object.
        rayleighDampingByFrequency
            A RayleighDampingByFrequency object.
        maintainAttributes
            A Boolean specifying whether to retain attributes from an existing step with the same
            name. The default value is False.

        Returns
        -------
        step: ResponseSpectrumStep
            A ResponseSpectrumStep object.
        """
        self.steps[name] = step = ResponseSpectrumStep(
            name,
            previous,
            components,
            description,
            comp,
            sum,
            directDamping,
            compositeDamping,
            rayleighDamping,
            directDampingByFrequency,
            rayleighDampingByFrequency,
            maintainAttributes,
        )
        return step

    @abaqus_method_doc
    def SoilsStep(
        self,
        name: str,
        previous: str,
        description: str = "",
        response: Literal[C.STEADY_STATE, C.TRANSIENT] = TRANSIENT,
        timePeriod: float = 1,
        nlgeom: Boolean = OFF,
        stabilizationMethod: Literal[C.NONE, C.DISSIPATED_ENERGY_FRACTION, C.DAMPING_FACTOR] = NONE,
        stabilizationMagnitude: Optional[float] = None,
        creep: Boolean = ON,
        timeIncrementationMethod: Literal[C.FIXED, C.AUTOMATIC] = AUTOMATIC,
        initialInc: Optional[float] = None,
        minInc: Optional[float] = None,
        maxInc: Optional[float] = None,
        maxNumInc: int = 100,
        end: Optional[Literal[C.SS, C.PERIOD]] = PERIOD,
        utol: Optional[float] = None,
        cetol: Optional[float] = 0,
        amplitude: Literal[C.STEP, C.RAMP] = STEP,
        extrapolation: Literal[C.PARABOLIC, C.LINEAR] = LINEAR,
        matrixSolver: Literal[C.ITERATIVE, C.DIRECT] = DIRECT,
        matrixStorage: Literal[C.SYMMETRIC, C.UNSYMMETRIC, C.SOLVER_DEFAULT] = SOLVER_DEFAULT,
        maintainAttributes: Boolean = False,
        solutionTechnique: Literal[C.FULL_NEWTON, C.QUASI_NEWTON] = FULL_NEWTON,
        reformKernel: int = 8,
        convertSDI: Literal[C.PROPAGATED, C.CONVERT_SDI_OFF, C.CONVERT_SDI_ON] = PROPAGATED,
        adaptiveDampingRatio: float = 0,
        continueDampingFactors: Boolean = OFF,
    ) -> SoilsStep:
        """This method creates a SoilsStep object.

        .. note::
            This function can be accessed by::

                mdb.models[name].SoilsStep

        Parameters
        ----------
        name
            A String specifying the repository key.
        previous
            A String specifying the name of the previous step. The new step appears after this step
            in the list of analysis steps.
        description
            A String specifying a description of the new step. The default value is an empty string.
        response
            A SymbolicConstant specifying the analysis type. Possible values are STEADY_STATE and
            TRANSIENT. The default value is TRANSIENT.
        timePeriod
            A Float specifying the total time period. The default value is 1.0.
        nlgeom
            A Boolean specifying whether geometric nonlinearities should be accounted for during the
            step. The default value is OFF.
        stabilizationMethod
            A SymbolicConstant specifying the stabilization type. Possible values are NONE,
            DISSIPATED_ENERGY_FRACTION, and DAMPING_FACTOR. The default value is NONE.
        stabilizationMagnitude
            A Float specifying the damping intensity of the automatic damping algorithm if the
            problem is expected to be unstable, and **stabilizationMethod** is not NONE. The default
            value is 2x10⁻⁴.
        creep
            A Boolean specifying whether a creep response occurs during this step. The default value
            is ON.
        timeIncrementationMethod
            A SymbolicConstant specifying the time incrementation method to be used. Possible values
            are FIXED and AUTOMATIC. The default value is AUTOMATIC.
        initialInc
            A Float specifying the initial time increment. The default value is the total time
            period for the step.
        minInc
            A Float specifying the minimum time increment allowed. The default value is the smaller
            of the suggested initial time increment or 10−5 times the total time period.
        maxInc
            A Float specifying the maximum time increment allowed. The default value is the total
            time period for the step.
        maxNumInc
            An Int specifying the maximum number of increments in a step. The default value is 100.
        end
            A SymbolicConstant specifying the time period to be analyzed in a transient analysis.
            Possible values are PERIOD and SS. The default value is PERIOD.
        utol
            None or a Float specifying the maximum pore pressure change permitted in any increment
            (in pressure units) in a transient consolidation analysis. The default value is None.
        cetol
            A Float specifying the maximum allowable difference in the creep strain increment
            calculated from the creep strain rates at the beginning and end of the increment. The
            default value is 0.0.
        amplitude
            A SymbolicConstant specifying the amplitude variation for loading magnitudes during the
            step. The default value is STEP. Possible values are STEP and RAMP.
        extrapolation
            A SymbolicConstant specifying the type of extrapolation to use in determining the
            incremental solution for a nonlinear analysis. Possible values are NONE, LINEAR, and
            PARABOLIC. The default value is LINEAR.
        matrixSolver
            A SymbolicConstant specifying the type of solver. Possible values are DIRECT and
            ITERATIVE. The default value is DIRECT.
        matrixStorage
            A SymbolicConstant specifying the type of matrix storage. Possible values are SYMMETRIC,
            UNSYMMETRIC, and SOLVER_DEFAULT. The default value is SOLVER_DEFAULT.
        maintainAttributes
            A Boolean specifying whether to retain attributes from an existing step with the same
            name. The default value is False.
        solutionTechnique
            A SymbolicConstant specifying the technique used to for solving nonlinear equations.
            Possible values are FULL_NEWTON and QUASI_NEWTON. The default value is FULL_NEWTON.
        reformKernel
            An Int specifying the number of quasi-Newton iterations allowed before the kernel matrix
            is reformed.. The default value is 8.
        convertSDI
            A SymbolicConstant specifying whether to force a new iteration if severe discontinuities
            occur during an iteration. Possible values are PROPAGATED, CONVERT_SDI_OFF, and
            CONVERT_SDI_ON. The default value is PROPAGATED.
        adaptiveDampingRatio
            A Float specifying the maximum allowable ratio of the stabilization energy to the total
            strain energy and can be used only if **stabilizationMethod** is not NONE. The default
            value is 0.05.
        continueDampingFactors
            A Boolean specifying whether this step will carry over the damping factors from the
            results of the preceding general step. This parameter must be used in conjunction with
            the **adaptiveDampingRatio** parameter. The default value is OFF.

        Returns
        -------
        step: SoilsStep
            A SoilsStep object.
        """
        self.steps[name] = step = SoilsStep(
            name,
            previous,
            description,
            response,
            timePeriod,
            nlgeom,
            stabilizationMethod,
            stabilizationMagnitude,
            creep,
            timeIncrementationMethod,
            initialInc,
            minInc,
            maxInc,
            maxNumInc,
            end,
            utol,
            cetol,
            amplitude,
            extrapolation,
            matrixSolver,
            matrixStorage,
            maintainAttributes,
            solutionTechnique,
            reformKernel,
            convertSDI,
            adaptiveDampingRatio,
            continueDampingFactors,
        )
        return step

    @abaqus_method_doc
    def StaticLinearPerturbationStep(
        self,
        name: str,
        previous: str,
        description: str = "",
        matrixSolver: Literal[C.DIRECT, C.ITERATIVE] = DIRECT,
        matrixStorage: Literal[C.SYMMETRIC, C.SOLVER_DEFAULT, C.UNSYMMETRIC] = SOLVER_DEFAULT,
        maintainAttributes: Boolean = False,
    ) -> StaticLinearPerturbationStep:
        """This method creates a StaticLinearPerturbationStep object.

        .. note::
            This function can be accessed by::

                mdb.models[name].StaticLinearPerturbationStep

        Parameters
        ----------
        name
            A String specifying the repository key.
        previous
            A String specifying the name of the previous step. The new step appears after this step
            in the list of analysis steps.
        description
            A String specifying a description of the new step. The default value is an empty string.
        matrixSolver
            A SymbolicConstant specifying the type of solver. Possible values are DIRECT and
            ITERATIVE. The default value is DIRECT.
        matrixStorage
            A SymbolicConstant specifying the type of matrix storage. Possible values are SYMMETRIC,
            UNSYMMETRIC, and SOLVER_DEFAULT. The default value is SOLVER_DEFAULT.
        maintainAttributes
            A Boolean specifying whether to retain attributes from an existing step with the same
            name. The default value is False.

        Returns
        -------
        step: StaticLinearPerturbationStep
            A StaticLinearPerturbationStep object.
        """
        self.steps[name] = step = StaticLinearPerturbationStep(
            name, previous, description, matrixSolver, matrixStorage, maintainAttributes
        )
        return step

    @abaqus_method_doc
    def StaticRiksStep(
        self,
        name: str,
        previous: str,
        description: str = "",
        nlgeom: Boolean = OFF,
        adiabatic: Boolean = OFF,
        maxLPF: Optional[float] = None,
        nodeOn: Boolean = OFF,
        maximumDisplacement: float = 0,
        dof: int = 0,
        region: Optional[Region] = None,
        timeIncrementationMethod: Literal[C.AUTOMATIC, C.FIXED] = AUTOMATIC,
        maxNumInc: int = 100,
        totalArcLength: float = 1,
        initialArcInc: Optional[float] = None,
        minArcInc: Optional[float] = None,
        maxArcInc: Optional[float] = None,
        matrixStorage: Literal[C.SYMMETRIC, C.SOLVER_DEFAULT, C.UNSYMMETRIC] = SOLVER_DEFAULT,
        extrapolation: Literal[C.PARABOLIC, C.NONE, C.LINEAR] = LINEAR,
        fullyPlastic: str = "",
        noStop: Boolean = OFF,
        maintainAttributes: Boolean = False,
        useLongTermSolution: Boolean = OFF,
        convertSDI: Literal[C.CONVERT_SDI_OFF, C.PROPAGATED, C.CONVERT_SDI_ON] = PROPAGATED,
    ) -> StaticRiksStep:
        """This method creates a StaticRiksStep object.

        .. note::
            This function can be accessed by::

                mdb.models[name].StaticRiksStep

        Parameters
        ----------
        name
            A String specifying the repository key.
        previous
            A String specifying the name of the previous step. The new step appears after this step
            in the list of analysis steps.
        description
            A String specifying a description of the new step. The default value is an empty string.
        nlgeom
            A Boolean specifying whether to allow for geometric nonlinearity. The default value is
            OFF.
        adiabatic
            A Boolean specifying whether to perform an adiabatic stress analysis. The default value
            is OFF.
        maxLPF
            None or a Float specifying the maximum value of the load proportionality factor. The
            default value is None.
        nodeOn
            A Boolean specifying whether to monitor the finishing displacement value at a node. The
            default value is OFF.
        maximumDisplacement
            A Float specifying the value of the total displacement (or rotation) at the node and
            degree of freedom that, if crossed during an increment, ends the step at the current
            increment. This argument is required when **nodeOn** = ON. The default value is 0.0.
        dof
            An Int specifying the degree of freedom being monitored. This argument is required when
            **nodeOn** = ON. The default value is 0.
        region
            A Region object specifying the vertex at which the finishing displacement value is being
            monitored. This argument is required when **nodeOn** = ON.
        timeIncrementationMethod
            A SymbolicConstant specifying the time incrementation method to be used. Possible values
            are FIXED and AUTOMATIC. The default value is AUTOMATIC.
        maxNumInc
            An Int specifying the maximum number of increments in a step. The default value is 100.
        totalArcLength
            A Float specifying the total load proportionality factor associated with the load in
            this step. The default value is 1.0.
        initialArcInc
            A Float specifying the initial load proportionality factor. The default value is the
            total load proportionality factor for the step.
        minArcInc
            A Float specifying the minimum arc length increment allowed. The default value is the
            smaller of the suggested initial load proportionality factor or 10−5 times the total
            load proportionality factor for the step.
        maxArcInc
            A Float specifying the maximum arc length increment allowed. The default value is the
            total load proportionality factor for the step.
        matrixStorage
            A SymbolicConstant specifying the type of matrix storage. Possible values are SYMMETRIC,
            UNSYMMETRIC, and SOLVER_DEFAULT. The default value is SOLVER_DEFAULT.
        extrapolation
            A SymbolicConstant specifying the type of extrapolation to use in determining the
            incremental solution for a nonlinear analysis. Possible values are NONE, LINEAR, and
            PARABOLIC. The default value is LINEAR.
        fullyPlastic
            A String specifying the name of the region being monitored for fully Plastic behavior.
            The default value is an empty string.
        noStop
            A Boolean specifying whether to accept the solution to an increment after the maximum
            number of iterations allowed have been completed, even if the equilibrium tolerances are
            not satisfied. The default value is OFF.Warning:You should set **noStop** = ON only in
            special cases when you have a thorough understanding of how to interpret the results.
        maintainAttributes
            A Boolean specifying whether to retain attributes from an existing step with the same
            name. The default value is False.
        useLongTermSolution
            A Boolean specifying wether to obtain the fully relaxed long-term elastic solution with
            time-domain viscoelasticity or the long-term elastic-Plastic solution for two-layer
            viscoplasticity. The default value is OFF.
        convertSDI
            A SymbolicConstant specifying whether to force a new iteration if severe discontinuities
            occur during an iteration. Possible values are PROPAGATED, CONVERT_SDI_OFF, and
            CONVERT_SDI_ON. The default value is PROPAGATED.

        Returns
        -------
        step: StaticRiksStep
            A StaticRiksStep object.
        """
        self.steps[name] = step = StaticRiksStep(
            name,
            previous,
            description,
            nlgeom,
            adiabatic,
            maxLPF,
            nodeOn,
            maximumDisplacement,
            dof,
            region,
            timeIncrementationMethod,
            maxNumInc,
            totalArcLength,
            initialArcInc,
            minArcInc,
            maxArcInc,
            matrixStorage,
            extrapolation,
            fullyPlastic,
            noStop,
            maintainAttributes,
            useLongTermSolution,
            convertSDI,
        )
        return step

    @abaqus_method_doc
    def StaticStep(
        self,
        name: str,
        previous: str,
        description: str = "",
        timePeriod: float = 1,
        nlgeom: Boolean = OFF,
        stabilizationMethod: Literal[C.DAMPING_FACTOR, C.DISSIPATED_ENERGY_FRACTION, C.NONE] = NONE,
        stabilizationMagnitude: Optional[float] = None,
        adiabatic: Boolean = OFF,
        timeIncrementationMethod: Literal[C.AUTOMATIC, C.FIXED] = AUTOMATIC,
        maxNumInc: int = 100,
        initialInc: Optional[float] = None,
        minInc: Optional[float] = None,
        maxInc: Optional[float] = None,
        matrixSolver: Literal[C.DIRECT, C.ITERATIVE] = DIRECT,
        matrixStorage: Literal[C.SYMMETRIC, C.SOLVER_DEFAULT, C.UNSYMMETRIC] = SOLVER_DEFAULT,
        amplitude: Literal[C.STEP, C.RAMP] = RAMP,
        extrapolation: Literal[C.PARABOLIC, C.NONE, C.LINEAR] = LINEAR,
        fullyPlastic: str = "",
        noStop: Boolean = OFF,
        maintainAttributes: Boolean = False,
        useLongTermSolution: Boolean = OFF,
        solutionTechnique: Literal[C.QUASI_NEWTON, C.FULL_NEWTON] = FULL_NEWTON,
        reformKernel: int = 8,
        convertSDI: Literal[C.CONVERT_SDI_OFF, C.PROPAGATED, C.CONVERT_SDI_ON] = PROPAGATED,
        adaptiveDampingRatio: float = 0,
        continueDampingFactors: Boolean = OFF,
    ) -> StaticStep:
        """This method creates a StaticStep object.

        .. note::
            This function can be accessed by::

                mdb.models[name].StaticStep

        Parameters
        ----------
        name
            A String specifying the repository key.
        previous
            A String specifying the name of the previous step. The new step appears after this step
            in the list of analysis steps.
        description
            A String specifying a description of the new step. The default value is an empty string.
        timePeriod
            A Float specifying the total time period. The default value is 1.0.
        nlgeom
            A Boolean specifying whether to allow for geometric nonlinearity. The default value is
            OFF.
        stabilizationMethod
            A SymbolicConstant specifying the stabilization type. Possible values are NONE,
            DISSIPATED_ENERGY_FRACTION, and DAMPING_FACTOR. The default value is NONE.
        stabilizationMagnitude
            A Float specifying the damping intensity of the automatic damping algorithm if the
            problem is expected to be unstable, and **stabilizationMethod** is not NONE. The default
            value is 2x10⁻⁴.
        adiabatic
            A Boolean specifying whether to perform an adiabatic stress analysis. The default value
            is OFF.
        timeIncrementationMethod
            A SymbolicConstant specifying the time incrementation method to be used. Possible values
            are FIXED and AUTOMATIC. The default value is AUTOMATIC.
        maxNumInc
            An Int specifying the maximum number of increments in a step. The default value is 100.
        initialInc
            A Float specifying the initial time increment. The default value is the total time
            period for the step.
        minInc
            A Float specifying the minimum time increment allowed. The default value is the smaller
            of the suggested initial time increment or 10⁻⁵ times the total time period.
        maxInc
            A Float specifying the maximum time increment allowed. The default value is the total
            time period for the step.
        matrixSolver
            A SymbolicConstant specifying the type of solver. Possible values are DIRECT and
            ITERATIVE. The default value is DIRECT.
        matrixStorage
            A SymbolicConstant specifying the type of matrix storage. Possible values are SYMMETRIC,
            UNSYMMETRIC, and SOLVER_DEFAULT. The default value is SOLVER_DEFAULT.
        amplitude
            A SymbolicConstant specifying the amplitude variation for loading magnitudes during the
            step. Possible values are STEP and RAMP. The default value is RAMP.
        extrapolation
            A SymbolicConstant specifying the type of extrapolation to use in determining the
            incremental solution for a nonlinear analysis. Possible values are NONE, LINEAR, and
            PARABOLIC. The default value is LINEAR.
        fullyPlastic
            A String specifying the region being monitored for fully Plastic behavior. The default
            value is an empty string.
        noStop
            A Boolean specifying whether to accept the solution to an increment after the maximum
            number of iterations allowed has been completed, even if the equilibrium tolerances are
            not satisfied. The default value is OFF.Warning:You should set **noStop** = ON only in
            special cases when you have a thorough understanding of how to interpret the results.
        maintainAttributes
            A Boolean specifying whether to retain attributes from an existing step with the same
            name. The default value is False.
        useLongTermSolution
            A Boolean specifying wether to obtain the fully relaxed long-term elastic solution with
            time-domain viscoelasticity or the long-term elastic-Plastic solution for two-layer
            viscoplasticity. The default value is OFF.
        solutionTechnique
            A SymbolicConstant specifying the technique used to for solving nonlinear equations.
            Possible values are FULL_NEWTON and QUASI_NEWTON. The default value is FULL_NEWTON.
        reformKernel
            An Int specifying the number of quasi-Newton iterations allowed before the kernel matrix
            is reformed.. The default value is 8.
        convertSDI
            A SymbolicConstant specifying whether to force a new iteration if severe discontinuities
            occur during an iteration. Possible values are PROPAGATED, CONVERT_SDI_OFF, and
            CONVERT_SDI_ON. The default value is PROPAGATED.
        adaptiveDampingRatio
            A Float specifying the maximum allowable ratio of the stabilization energy to the total
            strain energy and can be used only if **stabilizationMethod** is not NONE. The default
            value is 0.05.
        continueDampingFactors
            A Boolean specifying whether this step will carry over the damping factors from the
            results of the preceding general step. This parameter must be used in conjunction with
            the **adaptiveDampingRatio** parameter. The default value is OFF.

        Returns
        -------
        step: StaticRiksStep
            A StaticRiksStep object.
        """
        self.steps[name] = step = StaticStep(
            name,
            previous,
            description,
            timePeriod,
            nlgeom,
            stabilizationMethod,
            stabilizationMagnitude,
            adiabatic,
            timeIncrementationMethod,
            maxNumInc,
            initialInc,
            minInc,
            maxInc,
            matrixSolver,
            matrixStorage,
            amplitude,
            extrapolation,
            fullyPlastic,
            noStop,
            maintainAttributes,
            useLongTermSolution,
            solutionTechnique,
            reformKernel,
            convertSDI,
            adaptiveDampingRatio,
            continueDampingFactors,
        )
        return step

    @abaqus_method_doc
    def SteadyStateDirectStep(
        self,
        name: str,
        previous: str,
        frequencyRange: SteadyStateDirectFrequencyArray,
        description: str = "",
        factorization: Literal[C.COMPLEX, C.REAL_ONLY] = COMPLEX,
        scale: Literal[C.LINEAR, C.LOGARITHMIC] = LOGARITHMIC,
        matrixStorage: Literal[C.SYMMETRIC, C.SOLVER_DEFAULT, C.UNSYMMETRIC] = SOLVER_DEFAULT,
        maintainAttributes: Boolean = False,
        subdivideUsingEigenfrequencies: Boolean = OFF,
        frictionDamping: Boolean = OFF,
    ) -> SteadyStateDirectStep:
        """This method creates a SteadyStateDirectStep object.

        .. note::
            This function can be accessed by::

                mdb.models[name].SteadyStateDirectStep

        Parameters
        ----------
        name
            A String specifying the repository key.
        previous
            A String specifying the name of the previous step. The new step appears after this step
            in the list of analysis steps.
        frequencyRange
            A SteadyStateDirectFrequencyArray object.
        description
            A String specifying a description of the new step. The default value is an empty string.
        factorization
            A SymbolicConstant specifying whether damping terms are to be ignored so that a real,
            rather than a complex, system matrix is factored. Possible values are REAL_ONLY and
            COMPLEX. The default value is COMPLEX.
        scale
            A SymbolicConstant specifying whether a logarithmic or linear scale is used for output.
            Possible values are LOGARITHMIC and LINEAR. The default value is LOGARITHMIC.
        matrixStorage
            A SymbolicConstant specifying the type of matrix storage. Possible values are SYMMETRIC,
            UNSYMMETRIC, and SOLVER_DEFAULT. The default value is SOLVER_DEFAULT.
        maintainAttributes
            A Boolean specifying whether to retain attributes from an existing step with the same
            name. The default value is False.
        subdivideUsingEigenfrequencies
            A Boolean specifying whether to subdivide each frequency range using the
            eigenfrequencies of the system. The default value is OFF.
        frictionDamping
            A Boolean specifying whether to add to the damping matrix contributions due to friction
            effects. The default value is OFF.

        Returns
        -------
        step: SteadyStateDirectStep
            A SteadyStateDirectStep object.
        """
        self.steps[name] = step = SteadyStateDirectStep(
            name,
            previous,
            frequencyRange,
            description,
            factorization,
            scale,
            matrixStorage,
            maintainAttributes,
            subdivideUsingEigenfrequencies,
            frictionDamping,
        )
        return step

    @abaqus_method_doc
    def SteadyStateModalStep(
        self,
        name: str,
        previous: str,
        frequencyRange: SteadyStateModalFrequencyArray,
        description: str = "",
        scale: Literal[C.LINEAR, C.LOGARITHMIC] = LOGARITHMIC,
        directDamping: Optional[DirectDamping] = None,
        compositeDamping: Optional[CompositeDamping] = None,
        rayleighDamping: Optional[RayleighDamping] = None,
        structuralDamping: Optional[StructuralDamping] = None,
        directDampingByFrequency: Optional[DirectDampingByFrequency] = None,
        rayleighDampingByFrequency: Optional[RayleighDampingByFrequency] = None,
        structuralDampingByFrequency: Optional[StructuralDampingByFrequency] = None,
        maintainAttributes: Boolean = False,
        subdivideUsingEigenfrequencies: Boolean = ON,
    ) -> SteadyStateModalStep:
        """This method creates a SteadyStateModalStep object.

        .. note::
            This function can be accessed by::

                mdb.models[name].SteadyStateModalStep

        Parameters
        ----------
        name
            A String specifying the repository key.
        previous
            A String specifying the name of the previous step. The new step appears after this step
            in the list of analysis steps.
        frequencyRange
            A SteadyStateModalFrequencyArray object.
        description
            A String specifying a description of the new step. The default value is an empty string.
        scale
            A SymbolicConstant specifying whether a logarithmic or linear scale is used for output.
            Possible values are LOGARITHMIC and LINEAR. The default value is LOGARITHMIC.
        directDamping
            A DirectDamping object.
        compositeDamping
            A CompositeDamping object.
        rayleighDamping
            A RayleighDamping object.
        structuralDamping
            A StructuralDamping object.
        directDampingByFrequency
            A DirectDampingByFrequency object.
        rayleighDampingByFrequency
            A RayleighDampingByFrequency object.
        structuralDampingByFrequency
            A StructuralDampingByFrequency object.
        maintainAttributes
            A Boolean specifying whether to retain attributes from an existing step with the same
            name. The default value is False.
        subdivideUsingEigenfrequencies
            A Boolean specifying whether to subdivide each frequency range using the
            eigenfrequencies of the system. The default value is ON.

        Returns
        -------
        step: SteadyStateModalStep
            A SteadyStateModalStep object.
        """
        self.steps[name] = step = SteadyStateModalStep(
            name,
            previous,
            frequencyRange,
            description,
            scale,
            directDamping,
            compositeDamping,
            rayleighDamping,
            structuralDamping,
            directDampingByFrequency,
            rayleighDampingByFrequency,
            structuralDampingByFrequency,
            maintainAttributes,
            subdivideUsingEigenfrequencies,
        )
        return step

    @abaqus_method_doc
    def SteadyStateSubspaceStep(
        self,
        name: str,
        previous: str,
        frequencyRange: SteadyStateSubspaceFrequencyArray,
        description: str = "",
        factorization: Literal[C.COMPLEX, C.REAL_ONLY] = COMPLEX,
        scale: Literal[C.LINEAR, C.LOGARITHMIC] = LOGARITHMIC,
        matrixStorage: Literal[C.SYMMETRIC, C.SOLVER_DEFAULT, C.UNSYMMETRIC] = SOLVER_DEFAULT,
        maintainAttributes: Boolean = False,
        subdivideUsingEigenfrequencies: Boolean = ON,
        projection: Literal[
            C.CONSTANT, C.RANGE, C.ALL_FREQUENCIES, C.PROPERTY_CHANGE, C.EIGENFREQUENCY
        ] = ALL_FREQUENCIES,
        maxDampingChange: float = 0,
        maxStiffnessChange: float = 0,
        frictionDamping: Boolean = OFF,
    ) -> SteadyStateSubspaceStep:
        """This method creates a SteadyStateSubspaceStep object.

        .. note::
            This function can be accessed by::

                mdb.models[name].SteadyStateSubspaceStep

        Parameters
        ----------
        name
            A String specifying the repository key.
        previous
            A String specifying the name of the previous step. The new step appears after this step
            in the list of analysis steps.
        frequencyRange
            A SteadyStateSubspaceFrequencyArray object.
        description
            A String specifying a description of the new step. The default value is an empty string.
        factorization
            A SymbolicConstant specifying whether damping terms are to be ignored so that a real,
            rather than a complex, system matrix is factored. Possible values are REAL_ONLY and
            COMPLEX. The default value is COMPLEX.
        scale
            A SymbolicConstant specifying whether a logarithmic or linear scale is used for output.
            Possible values are LOGARITHMIC and LINEAR. The default value is LOGARITHMIC.
        matrixStorage
            A SymbolicConstant specifying the type of matrix storage. Possible values are SYMMETRIC,
            UNSYMMETRIC, and SOLVER_DEFAULT. The default value is SOLVER_DEFAULT.
        maintainAttributes
            A Boolean specifying whether to retain attributes from an existing step with the same
            name. The default value is False.
        subdivideUsingEigenfrequencies
            A Boolean specifying whether to subdivide each frequency range using the
            eigenfrequencies of the system. The default value is ON.
        projection
            A SymbolicConstant specifying how often to perform subspace projections onto the modal
            subspace. Possible values are ALL_FREQUENCIES, CONSTANT, EIGENFREQUENCY,
            PROPERTY_CHANGE, and RANGE. The default value is ALL_FREQUENCIES.
        maxDampingChange
            A Float specifying the maximum relative change in damping material properties before a
            new projection is to be performed. The default value is 0.1.
        maxStiffnessChange
            A Float specifying the maximum relative change in stiffness material properties before a
            new projection is to be performed. The default value is 0.1.
        frictionDamping
            A Boolean specifying whether to add to the damping matrix contributions due to friction
            effects. The default value is OFF.

        Returns
        -------
        step: SteadyStateSubspaceStep
            A SteadyStateSubspaceStep object.
        """
        self.steps[name] = step = SteadyStateSubspaceStep(
            name,
            previous,
            frequencyRange,
            description,
            factorization,
            scale,
            matrixStorage,
            maintainAttributes,
            subdivideUsingEigenfrequencies,
            projection,
            maxDampingChange,
            maxStiffnessChange,
            frictionDamping,
        )
        return step

    @abaqus_method_doc
    def SubspaceDynamicsStep(
        self,
        name: str,
        previous: str,
        description: str = "",
        timePeriod: float = 1,
        vectors: Literal[C.ALL] = ALL,
        nlgeom: Boolean = OFF,
        maxNumInc: int = 100,
        incSize: float = 0,
        amplitude: Literal[C.STEP, C.RAMP] = STEP,
        maintainAttributes: Boolean = False,
    ) -> SubspaceDynamicsStep:
        """This method creates a SubspaceDynamicsStep object.

        .. note::
            This function can be accessed by::

                mdb.models[name].SubspaceDynamicsStep

        Parameters
        ----------
        name
            A String specifying the repository key.
        previous
            A String specifying the name of the previous step. The new step appears after this step
            in the list of analysis steps.
        description
            A String specifying a description of the new step. The default value is an empty string.
        timePeriod
            A Float specifying the total time period of the step. The default value is 1.0.
        vectors
            The SymbolicConstant ALL or an Int specifying the number of modes to be used for
            subspace projection. The possible value for the SymbolicConstant is ALL. The default
            value is ALL.
        nlgeom
            A Boolean specifying whether to allow for geometric nonlinearity. The default value is
            OFF.
        maxNumInc
            An Int specifying the maximum number of increments in a step. The default value is 100.
        incSize
            A Float specifying the suggested time increment. The default value is 0.0.
        amplitude
            A SymbolicConstant specifying the amplitude variation for loading magnitudes during the
            step. Possible values are STEP and RAMP. The default value is STEP.
        maintainAttributes
            A Boolean specifying whether to retain attributes from an existing step with the same
            name. The default value is False.

        Returns
        -------
        step: SubspaceDynamicsStep
            A SubspaceDynamicsStep object.
        """
        self.steps[name] = step = SubspaceDynamicsStep(
            name,
            previous,
            description,
            timePeriod,
            vectors,
            nlgeom,
            maxNumInc,
            incSize,
            amplitude,
            maintainAttributes,
        )
        return step

    @abaqus_method_doc
    def SubstructureGenerateStep(
        self,
        name: str,
        previous: str,
        substructureIdentifier: int,
        description: str = "",
        recoveryMatrix: Literal[C.WHOLE_MODEL, C.REGION, C.NONE] = WHOLE_MODEL,
        recoveryRegion: Optional[Region] = None,
        computeGravityLoadVectors: Boolean = False,
        computeReducedMassMatrix: Boolean = False,
        computeReducedStructuralDampingMatrix: Boolean = False,
        computeReducedViscousDampingMatrix: Boolean = False,
        evaluateFrequencyDependentProperties: Boolean = False,
        frequency: float = 0,
        retainedEigenmodesMethod: Literal[C.MODE_RANGE, C.FREQUENCY_RANGE, C.NONE] = NONE,
        modeRange: Optional[SubstructureGenerateModesArray] = None,
        frequencyRange: Optional[SubstructureGenerateFrequencyArray] = None,
        globalDampingField: Literal[C.ACOUSTIC, C.ALL, C.MECHANICAL, C.NONE] = NONE,
        alphaDampingRatio: float = 0,
        betaDampingRatio: float = 0,
        structuralDampingRatio: float = 0,
        viscousDampingControl: Literal[C.COMBINED, C.NONE, C.FACTOR, C.ELEMENT] = NONE,
        structuralDampingControl: Literal[C.COMBINED, C.NONE, C.FACTOR, C.ELEMENT] = NONE,
    ) -> SubstructureGenerateStep:
        """This method creates a SubstructureGenerateStep object.

        .. note::
            This function can be accessed by::

                mdb.models[name].SubstructureGenerateStep

        Parameters
        ----------
        name
            A String specifying the repository key.
        previous
            A String specifying the name of the previous step. The new step appears after this step
            in the list of analysis steps.
        substructureIdentifier
            An Integer specifying a unique identifier for the substructure.
        description
            A String specifying a description of the new step. The default value is an empty string.
        recoveryMatrix
            A SymbolicConstant specifying the subtructure recovery to be computed. Possible values
            are WHOLE_MODEL, REGION, and NONE. The default value is WHOLE_MODEL.
        recoveryRegion
            A Region object specifying the region for substructure recovery. This argument is
            required when **recoveryMatrix** = REGION.
        computeGravityLoadVectors
            A Boolean specifying whether to compute the gravity load vectors. The default value is
            False.
        computeReducedMassMatrix
            A Boolean specifying whether to compute the reduced mass matrix. The default value is
            False.
        computeReducedStructuralDampingMatrix
            A Boolean specifying whether to compute the reduced structural damping matrix. The
            default value is False.
        computeReducedViscousDampingMatrix
            A Boolean specifying whether to compute the reduced viscous damping matrix. The default
            value is False.
        evaluateFrequencyDependentProperties
            A Boolean specifying whether to evaluate the frequency dependent properties. The default
            value is False.
        frequency
            A Float specifying the frequency at which to evaluate the frequency dependent
            properties. The default value is 0.0.
        retainedEigenmodesMethod
            A SymbolicConstant specifying the eigenmodes to be retained. Possible values are
            MODE_RANGE, FREQUENCY_RANGE, and NONE. The default value is NONE.
        modeRange
            A SubstructureGenerateModesArray object.
        frequencyRange
            A SubstructureGenerateFrequencyArray object.
        globalDampingField
            A SymbolicConstant specifying the field to which the global damping factors should be
            applied. Possible values are ALL, ACOUSTIC, MECHANICAL, and NONE. The default value is
            NONE.
        alphaDampingRatio
            A Float specifying the factor to create global Rayleigh mass proportional damping. The
            default value is 0.0.
        betaDampingRatio
            A Float specifying the factor to create global Rayleigh stiffness proportional damping.
            The default value is 0.0.
        structuralDampingRatio
            A Float specifying the factor to create frequency-independent stiffness proportional
            structural damping. The default value is 0.0.
        viscousDampingControl
            A SymbolicConstant specifying the damping control to include the viscous damping matrix.
            Possible values are ELEMENT, FACTOR, COMBINED, and NONE. The default value is NONE.
        structuralDampingControl
            A SymbolicConstant specifying the damping control to include the structural damping
            matrix. Possible values are ELEMENT, FACTOR, COMBINED, and NONE. The default value is
            NONE.

        Returns
        -------
        step: SubstructureGenerateStep
            A SubstructureGenerateStep object.
        """
        self.steps[name] = step = SubstructureGenerateStep(
            name,
            previous,
            substructureIdentifier,
            description,
            recoveryMatrix,
            recoveryRegion,
            computeGravityLoadVectors,
            computeReducedMassMatrix,
            computeReducedStructuralDampingMatrix,
            computeReducedViscousDampingMatrix,
            evaluateFrequencyDependentProperties,
            frequency,
            retainedEigenmodesMethod,
            modeRange,
            frequencyRange,
            globalDampingField,
            alphaDampingRatio,
            betaDampingRatio,
            structuralDampingRatio,
            viscousDampingControl,
            structuralDampingControl,
        )
        return step

    @abaqus_method_doc
    def TempDisplacementDynamicsStep(
        self,
        name: str,
        previous: str,
        description: str = "",
        timePeriod: float = 1,
        nlgeom: Boolean = OFF,
        timeIncrementationMethod: Literal[
            C.FIXED_EBE, C.AUTOMATIC_GLOBAL, C.AUTOMATIC_EBE, C.FIXED_USER_DEFINED_INC
        ] = AUTOMATIC_GLOBAL,
        maxIncrement: Optional[float] = None,
        scaleFactor: float = 1,
        userDefinedInc: Optional[float] = None,
        massScaling: Union[MassScalingArray, Literal[C.PREVIOUS_STEP]] = PREVIOUS_STEP,
        linearBulkViscosity: float = 0,
        quadBulkViscosity: float = 1,
        maintainAttributes: Boolean = False,
        improvedDtMethod: Boolean = ON,
    ) -> TempDisplacementDynamicsStep:
        """This method creates a TempDisplacementDynamicsStep object.

        .. note::
            This function can be accessed by::

                mdb.models[name].TempDisplacementDynamicsStep

        Parameters
        ----------
        name
            A String specifying the repository key.
        previous
            A String specifying the name of the previous step. The new step appears after this step
            in the list of analysis steps.
        description
            A String specifying a description of the new step. The default value is an empty string.
        timePeriod
            A Float specifying the time period of the step. The default value is 1.0.
        nlgeom
            A Boolean specifying whether geometric nonlinearities should be accounted for during the
            step. The default value is OFF.
        timeIncrementationMethod
            A SymbolicConstant specifying the time incrementation method to be used. Possible values
            are AUTOMATIC_GLOBAL, AUTOMATIC_EBE, FIXED_USER_DEFINED_INC, and FIXED_EBE. The default
            value is AUTOMATIC_GLOBAL.
        maxIncrement
            None or a Float specifying the maximum time increment allowed. If there is no upper
            limit, **maxIncrement** = None. The default value is None.
        scaleFactor
            A Float specifying the factor that is used to scale the time increment. This argument is
            required only when **timeIncrementationMethod** = AUTOMATIC_GLOBAL, AUTOMATIC_EBE, or
            FIXED_EBE. The default value is 1.0.
        userDefinedInc
            None or a Float specifying the user-defined time increment. The default value is None.
        massScaling
            A MassScalingArray object specifying mass scaling controls. The default value is
            PREVIOUS_STEP.
        linearBulkViscosity
            A Float specifying the linear bulk viscosity parameter, b1b1. The default value is 0.06.
        quadBulkViscosity
            A Float specifying the quadratic bulk viscosity parameter, b2b2. The default value is
            1.2.
        maintainAttributes
            A Boolean specifying whether to retain attributes from an existing step with the same
            name. The default value is False.
        improvedDtMethod
            A Boolean specifying whether to use the "improved" (**improvedDtMethod** = ON) or
            "conservative" (**improvedDtMethod** = OFF) method to estimate the element stable time
            increment for three-dimensional continuum elements and elements with plane stress
            formulations (shell, membrane, and two-dimensional plane stress elements). The default
            value is ON.

            .. versionadded:: 2018
                The **improvedDtMethod** argument was added.

        Returns
        -------
        step: TempDisplacementDynamicsStep
            A TempDisplacementDynamicsStep object.
        """
        self.steps[name] = step = TempDisplacementDynamicsStep(
            name,
            previous,
            description,
            timePeriod,
            nlgeom,
            timeIncrementationMethod,
            maxIncrement,
            scaleFactor,
            userDefinedInc,
            massScaling,
            linearBulkViscosity,
            quadBulkViscosity,
            maintainAttributes,
        )
        return step

    @abaqus_method_doc
    def ViscoStep(
        self,
        name: str,
        previous: str,
        description: str = "",
        timePeriod: float = 1,
        nlgeom: Boolean = OFF,
        stabilizationMethod: Literal[C.DAMPING_FACTOR, C.DISSIPATED_ENERGY_FRACTION, C.NONE] = NONE,
        stabilizationMagnitude: Optional[float] = None,
        timeIncrementationMethod: Literal[C.AUTOMATIC, C.FIXED] = AUTOMATIC,
        matrixSolver: Literal[C.DIRECT, C.ITERATIVE] = DIRECT,
        matrixStorage: Literal[C.SYMMETRIC, C.SOLVER_DEFAULT, C.UNSYMMETRIC] = SOLVER_DEFAULT,
        initialInc: Optional[float] = None,
        maxNumInc: int = 100,
        minInc: Optional[float] = None,
        maxInc: float = 1,
        integration: Literal[C.EXPLICIT_ONLY, C.IMPLICIT_EXPLICIT] = IMPLICIT_EXPLICIT,
        cetol: float = 0,
        amplitude: Literal[C.STEP, C.RAMP] = STEP,
        extrapolation: Literal[C.PARABOLIC, C.NONE, C.LINEAR] = LINEAR,
        maintainAttributes: Boolean = False,
        solutionTechnique: Literal[C.QUASI_NEWTON, C.FULL_NEWTON] = FULL_NEWTON,
        reformKernel: int = 8,
        convertSDI: Literal[C.CONVERT_SDI_OFF, C.PROPAGATED, C.CONVERT_SDI_ON] = PROPAGATED,
        adaptiveDampingRatio: float = 0,
        continueDampingFactors: Boolean = OFF,
    ) -> ViscoStep:
        """This method creates a ViscoStep object.

        .. note::
            This function can be accessed by::

                mdb.models[name].ViscoStep

        Parameters
        ----------
        name
            A String specifying the repository key.
        previous
            A String specifying the name of the previous step. The new step appears after this step
            in the list of analysis steps.
        description
            A String specifying a description of the new step. The default value is an empty string.
        timePeriod
            A Float specifying the total time period. The default value is 1.0.
        nlgeom
            A Boolean specifying whether to allow for geometric nonlinearity. The default value is
            OFF.
        stabilizationMethod
            A SymbolicConstant specifying the stabilization type. Possible values are NONE,
            DISSIPATED_ENERGY_FRACTION, and DAMPING_FACTOR. The default value is NONE.
        stabilizationMagnitude
            A Float specifying the damping intensity of the automatic damping algorithm if the
            problem is expected to be unstable, and **stabilizationMethod** is not NONE. The default
            value is 2x10⁻⁴.
        timeIncrementationMethod
            A SymbolicConstant specifying the time incrementation method to be used. Possible values
            are FIXED and AUTOMATIC. The default value is AUTOMATIC.
        matrixSolver
            A SymbolicConstant specifying the type of solver. Possible values are DIRECT and
            ITERATIVE. The default value is DIRECT.
        matrixStorage
            A SymbolicConstant specifying the type of matrix storage. Possible values are SYMMETRIC,
            UNSYMMETRIC, and SOLVER_DEFAULT. The default value is SOLVER_DEFAULT.
        initialInc
            A Float specifying the initial time increment. The default value is the total time
            period for the step.
        maxNumInc
            An Int specifying the maximum number of increments in a step. The default value is 100.
        minInc
            A Float specifying the minimum time increment allowed. The default value is the smaller
            of the suggested initial time increment or 10−5 times the total time period.
        maxInc
            A Float specifying the maximum time increment allowed. The default is the total time
            period for the step. The default value is 1.0.
        integration
            A SymbolicConstant specifying which type of integration to use throughout the step.
            Possible values are IMPLICIT_EXPLICIT and EXPLICIT_ONLY. The default value is
            IMPLICIT_EXPLICIT.
        cetol
            A Float specifying the maximum difference in the creep strain increment calculated from
            the creep strain rates at the beginning and end of the increment. The default value is
            0.0.
        amplitude
            A SymbolicConstant specifying the amplitude variation for loading magnitudes during the
            step. Possible values are STEP and RAMP. The default value is STEP.
        extrapolation
            A SymbolicConstant specifying the type of extrapolation to use in determining the
            incremental solution for a nonlinear analysis. Possible values are NONE, LINEAR, and
            PARABOLIC. The default value is LINEAR.
        maintainAttributes
            A Boolean specifying whether to retain attributes from an existing step with the same
            name. The default value is False.
        solutionTechnique
            A SymbolicConstant specifying the technique used to for solving nonlinear equations.
            Possible values are FULL_NEWTON and QUASI_NEWTON. The default value is FULL_NEWTON.
        reformKernel
            An Int specifying the number of quasi-Newton iterations allowed before the kernel matrix
            is reformed.. The default value is 8.
        convertSDI
            A SymbolicConstant specifying whether to force a new iteration if severe discontinuities
            occur during an iteration. Possible values are PROPAGATED, CONVERT_SDI_OFF, and
            CONVERT_SDI_ON. The default value is PROPAGATED.
        adaptiveDampingRatio
            A Float specifying the maximum allowable ratio of the stabilization energy to the total
            strain energy and can be used only if **stabilizationMethod** is not NONE. The default
            value is 0.05.
        continueDampingFactors
            A Boolean specifying whether this step will carry over the damping factors from the
            results of the preceding general step. This parameter must be used in conjunction with
            the **adaptiveDampingRatio** parameter. The default value is OFF.

        Returns
        -------
        step: ViscoStep
            A ViscoStep object.
        """
        self.steps[name] = step = ViscoStep(
            name,
            previous,
            description,
            timePeriod,
            nlgeom,
            stabilizationMethod,
            stabilizationMagnitude,
            timeIncrementationMethod,
            matrixSolver,
            matrixStorage,
            initialInc,
            maxNumInc,
            minInc,
            maxInc,
            integration,
            cetol,
            amplitude,
            extrapolation,
            maintainAttributes,
            solutionTechnique,
            reformKernel,
            convertSDI,
            adaptiveDampingRatio,
            continueDampingFactors,
        )
        return step
