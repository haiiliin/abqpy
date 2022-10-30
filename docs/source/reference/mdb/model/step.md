# Step

The Step commands described in this chapter are used to create and configure analysis steps. Step commands (output) describes the commands used to create and configure output requests and integrated output sections and the commands to configure diagnostic printing, monitoring, and restart. Step commands (miscellaneous) describes the commands used to configure controls, damping, and frequency tables.

```{toctree}
:caption: Objects in Step
:maxdepth: 1

step/step_miscellaneous
```

## Create steps

```{eval-rst}
.. autoclass:: abaqus.Step.StepModel.StepModel
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

## Other Classes

```{eval-rst}

.. toggle::

    .. autoclass:: abaqus.Step.Step.Step
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Step.StepBase.StepBase
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Adaptivity.AdaptivityStep.AdaptivityStep
        :members:
        :special-members: __init__
        :show-inheritance:
        :noindex:

        .. autoclasstoc::

    .. autoclass:: abaqus.StepOutput.OutputStep.OutputStep
        :members:
        :special-members: __init__
        :show-inheritance:
        :noindex:

        .. autoclasstoc::

    .. autoclass:: abaqus.Step.AnalysisStep.AnalysisStep
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Step.AnnealStep.AnnealStep
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Step.BuckleStep.BuckleStep
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Step.ComplexFrequencyStep.ComplexFrequencyStep
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Step.CoupledTempDisplacementStep.CoupledTempDisplacementStep
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Step.CoupledThermalElectricalStructuralStep.CoupledThermalElectricalStructuralStep
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Step.CoupledThermalElectricStep.CoupledThermalElectricStep
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Step.DirectCyclicStep.DirectCyclicStep
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Step.EmagTimeHarmonicStep.EmagTimeHarmonicStep
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Step.ExplicitDynamicsStep.ExplicitDynamicsStep
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Step.FrequencyStep.FrequencyStep
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Step.GeostaticStep.GeostaticStep
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Step.HeatTransferStep.HeatTransferStep
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Step.ImplicitDynamicsStep.ImplicitDynamicsStep
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Step.InitialStep.InitialStep
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Step.MassDiffusionStep.MassDiffusionStep
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Step.ModalDynamicsStep.ModalDynamicsStep
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Step.RandomResponseStep.RandomResponseStep
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Step.ResponseSpectrumStep.ResponseSpectrumStep
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Step.SoilsStep.SoilsStep
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Step.StaticLinearPerturbationStep.StaticLinearPerturbationStep
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Step.StaticRiksStep.StaticRiksStep
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Step.StaticStep.StaticStep
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Step.SteadyStateDirectStep.SteadyStateDirectStep
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Step.SteadyStateModalStep.SteadyStateModalStep
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Step.SteadyStateSubspaceStep.SteadyStateSubspaceStep
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Step.SubspaceDynamicsStep.SubspaceDynamicsStep
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Step.SubstructureGenerateStep.SubstructureGenerateStep
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Step.TempDisplacementDynamicsStep.TempDisplacementDynamicsStep
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Step.ViscoStep.ViscoStep
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::
```
