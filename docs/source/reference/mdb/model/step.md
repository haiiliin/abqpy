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

## Classes

### Step

```{eval-rst}
.. autoclass:: abaqus.Step.Step.Step
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### StepBase

```{eval-rst}
.. autoclass:: abaqus.Step.StepBase.StepBase
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### AdaptivityStep

```{eval-rst}
.. autoclass:: abaqus.Adaptivity.AdaptivityStep.AdaptivityStep
    :members:
    :special-members: __init__
    :show-inheritance:
    :noindex:

    .. autoclasstoc::
```

### OutputStep

```{eval-rst}
.. autoclass:: abaqus.StepOutput.OutputStep.OutputStep
    :members:
    :special-members: __init__
    :show-inheritance:
    :noindex:

    .. autoclasstoc::
```

### AnalysisStep

```{eval-rst}
.. autoclass:: abaqus.Step.AnalysisStep.AnalysisStep
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### AnnealStep

```{eval-rst}
.. autoclass:: abaqus.Step.AnnealStep.AnnealStep
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### BuckleStep

```{eval-rst}
.. autoclass:: abaqus.Step.BuckleStep.BuckleStep
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### ComplexFrequencyStep

```{eval-rst}
.. autoclass:: abaqus.Step.ComplexFrequencyStep.ComplexFrequencyStep
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### CoupledTempDisplacementStep

```{eval-rst}
.. autoclass:: abaqus.Step.CoupledTempDisplacementStep.CoupledTempDisplacementStep
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### CoupledThermalElectricalStructuralStep

```{eval-rst}
.. autoclass:: abaqus.Step.CoupledThermalElectricalStructuralStep.CoupledThermalElectricalStructuralStep
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### CoupledThermalElectricStep

```{eval-rst}
.. autoclass:: abaqus.Step.CoupledThermalElectricStep.CoupledThermalElectricStep
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### DirectCyclicStep

```{eval-rst}
.. autoclass:: abaqus.Step.DirectCyclicStep.DirectCyclicStep
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### EmagTimeHarmonicStep

```{eval-rst}
.. autoclass:: abaqus.Step.EmagTimeHarmonicStep.EmagTimeHarmonicStep
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### ExplicitDynamicsStep

```{eval-rst}
.. autoclass:: abaqus.Step.ExplicitDynamicsStep.ExplicitDynamicsStep
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### FrequencyStep

```{eval-rst}
.. autoclass:: abaqus.Step.FrequencyStep.FrequencyStep
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### GeostaticStep

```{eval-rst}
.. autoclass:: abaqus.Step.GeostaticStep.GeostaticStep
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### HeatTransferStep

```{eval-rst}
.. autoclass:: abaqus.Step.HeatTransferStep.HeatTransferStep
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### ImplicitDynamicsStep

```{eval-rst}
.. autoclass:: abaqus.Step.ImplicitDynamicsStep.ImplicitDynamicsStep
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### InitialStep

```{eval-rst}
.. autoclass:: abaqus.Step.InitialStep.InitialStep
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### MassDiffusionStep

```{eval-rst}
.. autoclass:: abaqus.Step.MassDiffusionStep.MassDiffusionStep
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### ModalDynamicsStep

```{eval-rst}
.. autoclass:: abaqus.Step.ModalDynamicsStep.ModalDynamicsStep
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### RandomResponseStep

```{eval-rst}
.. autoclass:: abaqus.Step.RandomResponseStep.RandomResponseStep
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### ResponseSpectrumStep

```{eval-rst}
.. autoclass:: abaqus.Step.ResponseSpectrumStep.ResponseSpectrumStep
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### SoilsStep

```{eval-rst}
.. autoclass:: abaqus.Step.SoilsStep.SoilsStep
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### StaticLinearPerturbationStep

```{eval-rst}
.. autoclass:: abaqus.Step.StaticLinearPerturbationStep.StaticLinearPerturbationStep
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### StaticRiksStep

```{eval-rst}
.. autoclass:: abaqus.Step.StaticRiksStep.StaticRiksStep
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### StaticStep

```{eval-rst}
.. autoclass:: abaqus.Step.StaticStep.StaticStep
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### SteadyStateDirectStep

```{eval-rst}
.. autoclass:: abaqus.Step.SteadyStateDirectStep.SteadyStateDirectStep
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### SteadyStateModalStep

```{eval-rst}
.. autoclass:: abaqus.Step.SteadyStateModalStep.SteadyStateModalStep
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### SteadyStateSubspaceStep

```{eval-rst}
.. autoclass:: abaqus.Step.SteadyStateSubspaceStep.SteadyStateSubspaceStep
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### SubspaceDynamicsStep

```{eval-rst}
.. autoclass:: abaqus.Step.SubspaceDynamicsStep.SubspaceDynamicsStep
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### SubstructureGenerateStep

```{eval-rst}
.. autoclass:: abaqus.Step.SubstructureGenerateStep.SubstructureGenerateStep
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### TempDisplacementDynamicsStep

```{eval-rst}
.. autoclass:: abaqus.Step.TempDisplacementDynamicsStep.TempDisplacementDynamicsStep
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### ViscoStep

```{eval-rst}
.. autoclass:: abaqus.Step.ViscoStep.ViscoStep
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```
