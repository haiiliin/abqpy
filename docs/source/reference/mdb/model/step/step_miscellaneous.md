# Step Miscellaneous

Miscellaneous Step commands are used for configuring controls, damping, and frequency tables.

## Other Classes

```{eval-rst}

.. toggle::

    .. autoclass:: abaqus.StepMiscellaneous.CompositeDamping.CompositeDamping
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.StepMiscellaneous.CompositeDampingComponent.CompositeDampingComponent
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.StepMiscellaneous.CompositeDampingComponentArray.CompositeDampingComponentArray
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.StepMiscellaneous.Control.Control
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.StepMiscellaneous.DirectDamping.DirectDamping
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.StepMiscellaneous.DirectDampingByFrequency.DirectDampingByFrequency
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.StepMiscellaneous.DirectDampingByFrequencyComponent.DirectDampingByFrequencyComponent
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.StepMiscellaneous.DirectDampingByFrequencyComponentArray.DirectDampingByFrequencyComponentArray
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.StepMiscellaneous.DirectDampingComponent.DirectDampingComponent
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.StepMiscellaneous.DirectDampingComponentArray.DirectDampingComponentArray
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.StepMiscellaneous.EmagTimeHarmonicFrequency.EmagTimeHarmonicFrequency
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.StepMiscellaneous.EmagTimeHarmonicFrequencyArray.EmagTimeHarmonicFrequencyArray
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.StepMiscellaneous.MassScaling.MassScaling
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.StepMiscellaneous.MassScalingArray.MassScalingArray
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.StepMiscellaneous.RandomResponseFrequency.RandomResponseFrequency
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.StepMiscellaneous.RandomResponseFrequencyArray.RandomResponseFrequencyArray
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.StepMiscellaneous.RayleighDamping.RayleighDamping
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.StepMiscellaneous.RayleighDampingByFrequency.RayleighDampingByFrequency
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.StepMiscellaneous.RayleighDampingByFrequencyComponent.RayleighDampingByFrequencyComponent
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.StepMiscellaneous.RayleighDampingByFrequencyComponentArray.RayleighDampingByFrequencyComponentArray
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.StepMiscellaneous.RayleighDampingComponent.RayleighDampingComponent
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.StepMiscellaneous.RayleighDampingComponentArray.RayleighDampingComponentArray
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.StepMiscellaneous.ResponseSpectrumComponent.ResponseSpectrumComponent
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.StepMiscellaneous.ResponseSpectrumComponentArray.ResponseSpectrumComponentArray
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.StepMiscellaneous.SolverControl.SolverControl
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.StepMiscellaneous.SteadyStateDirectFrequency.SteadyStateDirectFrequency
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.StepMiscellaneous.SteadyStateDirectFrequencyArray.SteadyStateDirectFrequencyArray
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.StepMiscellaneous.SteadyStateModalFrequency.SteadyStateModalFrequency
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.StepMiscellaneous.SteadyStateModalFrequencyArray.SteadyStateModalFrequencyArray
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.StepMiscellaneous.SteadyStateSubspaceFrequency.SteadyStateSubspaceFrequency
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.StepMiscellaneous.SteadyStateSubspaceFrequencyArray.SteadyStateSubspaceFrequencyArray
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.StepMiscellaneous.StructuralDamping.StructuralDamping
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.StepMiscellaneous.StructuralDampingByFrequency.StructuralDampingByFrequency
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.StepMiscellaneous.StructuralDampingByFrequencyComponent.StructuralDampingByFrequencyComponent
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.StepMiscellaneous.StructuralDampingByFrequencyComponentArray.StructuralDampingByFrequencyComponentArray
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.StepMiscellaneous.StructuralDampingComponent.StructuralDampingComponent
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.StepMiscellaneous.StructuralDampingComponentArray.StructuralDampingComponentArray
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.StepMiscellaneous.SubstructureGenerateFrequency.SubstructureGenerateFrequency
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.StepMiscellaneous.SubstructureGenerateFrequencyArray.SubstructureGenerateFrequencyArray
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.StepMiscellaneous.SubstructureGenerateModes.SubstructureGenerateModes
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.StepMiscellaneous.SubstructureGenerateModesArray.SubstructureGenerateModesArray
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::
```
