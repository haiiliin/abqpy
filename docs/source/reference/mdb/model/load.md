# Load

A specific type of load object and a specific type of load state object are designed for each type of load. A load object stores the nonpropagating data of a load as well as a number of instances of the corresponding load state object, each of which stores the propagating data of the load in a single step. Instances of the load state object are created and deleted internally by its corresponding load object.

Load Case commands are used for configuring load cases in specific types of steps that may use them.

## Load

The Load object is the abstract base type for other Load objects. The Load object has no explicit constructor. The methods and members of the Load object are common to all objects derived from Load.

### Create loads

```{eval-rst}
.. autoclass:: abaqus.Load.LoadModel.LoadModel
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::

```

### Object features of loads

#### Load

```{eval-rst}
.. autoclass:: abaqus.Load.Load.Load
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

#### LoadState

```{eval-rst}
.. autoclass:: abaqus.Load.LoadState.LoadState
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

#### BodyCharge

```{eval-rst}
.. autoclass:: abaqus.Load.BodyCharge.BodyCharge
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

#### BodyChargeState

```{eval-rst}
.. autoclass:: abaqus.Load.BodyChargeState.BodyChargeState
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

#### BodyConcentrationFlux

```{eval-rst}
.. autoclass:: abaqus.Load.BodyConcentrationFlux.BodyConcentrationFlux
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

#### BodyConcentrationFluxState

```{eval-rst}
.. autoclass:: abaqus.Load.BodyConcentrationFluxState.BodyConcentrationFluxState
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

#### BodyCurrent

```{eval-rst}
.. autoclass:: abaqus.Load.BodyCurrent.BodyCurrent
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

#### BodyCurrentDensity

```{eval-rst}
.. autoclass:: abaqus.Load.BodyCurrentDensity.BodyCurrentDensity
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

#### BodyCurrentState

```{eval-rst}
.. autoclass:: abaqus.Load.BodyCurrentState.BodyCurrentState
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

#### BodyForce

```{eval-rst}
.. autoclass:: abaqus.Load.BodyForce.BodyForce
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

#### BodyForceState

```{eval-rst}
.. autoclass:: abaqus.Load.BodyForceState.BodyForceState
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

#### BodyHeatFlux

```{eval-rst}
.. autoclass:: abaqus.Load.BodyHeatFlux.BodyHeatFlux
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

#### BodyHeatFluxState

```{eval-rst}
.. autoclass:: abaqus.Load.BodyHeatFluxState.BodyHeatFluxState
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

#### BoltLoad

```{eval-rst}
.. autoclass:: abaqus.Load.BoltLoad.BoltLoad
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

#### BoltLoadState

```{eval-rst}
.. autoclass:: abaqus.Load.BoltLoadState.BoltLoadState
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

#### ConcCharge

```{eval-rst}
.. autoclass:: abaqus.Load.ConcCharge.ConcCharge
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

#### ConcConcFlux

```{eval-rst}
.. autoclass:: abaqus.Load.ConcConcFlux.ConcConcFlux
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

#### ConcCurrent

```{eval-rst}
.. autoclass:: abaqus.Load.ConcCurrent.ConcCurrent
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

#### ConcCurrentState

```{eval-rst}
.. autoclass:: abaqus.Load.ConcCurrentState.ConcCurrentState
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

#### ConcentratedChargeState

```{eval-rst}
.. autoclass:: abaqus.Load.ConcentratedChargeState.ConcentratedChargeState
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

#### ConcentratedConcentrationFluxState

```{eval-rst}
.. autoclass:: abaqus.Load.ConcentratedConcentrationFluxState.ConcentratedConcentrationFluxState
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

#### ConcentratedForce

```{eval-rst}
.. autoclass:: abaqus.Load.ConcentratedForce.ConcentratedForce
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

#### ConcentratedForceState

```{eval-rst}
.. autoclass:: abaqus.Load.ConcentratedForceState.ConcentratedForceState
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

#### ConcentratedHeatFlux

```{eval-rst}
.. autoclass:: abaqus.Load.ConcentratedHeatFlux.ConcentratedHeatFlux
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

#### ConcentratedHeatFluxState

```{eval-rst}
.. autoclass:: abaqus.Load.ConcentratedHeatFluxState.ConcentratedHeatFluxState
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

#### ConcentratedPoreFluidState

```{eval-rst}
.. autoclass:: abaqus.Load.ConcentratedPoreFluidState.ConcentratedPoreFluidState
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

#### ConcPoreFluid

```{eval-rst}
.. autoclass:: abaqus.Load.ConcPoreFluid.ConcPoreFluid
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

#### ConnectorForce

```{eval-rst}
.. autoclass:: abaqus.Load.ConnectorForce.ConnectorForce
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

#### ConnectorForceState

```{eval-rst}
.. autoclass:: abaqus.Load.ConnectorForceState.ConnectorForceState
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

#### ConnectorMoment

```{eval-rst}
.. autoclass:: abaqus.Load.ConnectorMoment.ConnectorMoment
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

#### ConnectorMomentState

```{eval-rst}
.. autoclass:: abaqus.Load.ConnectorMomentState.ConnectorMomentState
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

#### CoriolisForce

```{eval-rst}
.. autoclass:: abaqus.Load.CoriolisForce.CoriolisForce
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

#### CoriolisForceState

```{eval-rst}
.. autoclass:: abaqus.Load.CoriolisForceState.CoriolisForceState
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

#### Gravity

```{eval-rst}
.. autoclass:: abaqus.Load.Gravity.Gravity
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

#### GravityState

```{eval-rst}
.. autoclass:: abaqus.Load.GravityState.GravityState
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

#### HydrostaticFluidFlowState

```{eval-rst}
.. autoclass:: abaqus.Load.HydrostaticFluidFlowState.HydrostaticFluidFlowState
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

#### InertiaRelief

```{eval-rst}
.. autoclass:: abaqus.Load.InertiaRelief.InertiaRelief
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

#### InertiaReliefState

```{eval-rst}
.. autoclass:: abaqus.Load.InertiaReliefState.InertiaReliefState
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

#### InwardVolAccel

```{eval-rst}
.. autoclass:: abaqus.Load.InwardVolAccel.InwardVolAccel
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

#### InwardVolAccelState

```{eval-rst}
.. autoclass:: abaqus.Load.InwardVolAccelState.InwardVolAccelState
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

#### LineLoad

```{eval-rst}
.. autoclass:: abaqus.Load.LineLoad.LineLoad
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

#### LineLoadState

```{eval-rst}
.. autoclass:: abaqus.Load.LineLoadState.LineLoadState
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

#### Moment

```{eval-rst}
.. autoclass:: abaqus.Load.Moment.Moment
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

#### MomentState

```{eval-rst}
.. autoclass:: abaqus.Load.MomentState.MomentState
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

#### PEGLoad

```{eval-rst}
.. autoclass:: abaqus.Load.PEGLoad.PEGLoad
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

#### PEGLoadState

```{eval-rst}
.. autoclass:: abaqus.Load.PEGLoadState.PEGLoadState
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

#### PipePressure

```{eval-rst}
.. autoclass:: abaqus.Load.PipePressure.PipePressure
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

#### PipePressureState

```{eval-rst}
.. autoclass:: abaqus.Load.PipePressureState.PipePressureState
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

#### Pressure

```{eval-rst}
.. autoclass:: abaqus.Load.Pressure.Pressure
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

#### PressureState

```{eval-rst}
.. autoclass:: abaqus.Load.PressureState.PressureState
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

#### RotationalBodyForce

```{eval-rst}
.. autoclass:: abaqus.Load.RotationalBodyForce.RotationalBodyForce
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

#### RotationalBodyForceState

```{eval-rst}
.. autoclass:: abaqus.Load.RotationalBodyForceState.RotationalBodyForceState
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

#### ShellEdgeLoad

```{eval-rst}
.. autoclass:: abaqus.Load.ShellEdgeLoad.ShellEdgeLoad
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

#### ShellEdgeLoadState

```{eval-rst}
.. autoclass:: abaqus.Load.ShellEdgeLoadState.ShellEdgeLoadState
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

#### SubmodelSB

```{eval-rst}
.. autoclass:: abaqus.Load.SubmodelSB.SubmodelSB
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

#### SubmodelSBState

```{eval-rst}
.. autoclass:: abaqus.Load.SubmodelSBState.SubmodelSBState
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

#### SubstructureLoad

```{eval-rst}
.. autoclass:: abaqus.Load.SubstructureLoad.SubstructureLoad
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

#### SubstructureLoadState

```{eval-rst}
.. autoclass:: abaqus.Load.SubstructureLoadState.SubstructureLoadState
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

#### SurfaceCharge

```{eval-rst}
.. autoclass:: abaqus.Load.SurfaceCharge.SurfaceCharge
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

#### SurfaceChargeState

```{eval-rst}
.. autoclass:: abaqus.Load.SurfaceChargeState.SurfaceChargeState
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

#### SurfaceConcentrationFlux

```{eval-rst}
.. autoclass:: abaqus.Load.SurfaceConcentrationFlux.SurfaceConcentrationFlux
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

#### SurfaceConcentrationFluxState

```{eval-rst}
.. autoclass:: abaqus.Load.SurfaceConcentrationFluxState.SurfaceConcentrationFluxState
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

#### SurfaceCurrent

```{eval-rst}
.. autoclass:: abaqus.Load.SurfaceCurrent.SurfaceCurrent
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

#### SurfaceCurrentDensity

```{eval-rst}
.. autoclass:: abaqus.Load.SurfaceCurrentDensity.SurfaceCurrentDensity
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

#### SurfaceCurrentState

```{eval-rst}
.. autoclass:: abaqus.Load.SurfaceCurrentState.SurfaceCurrentState
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

#### SurfaceHeatFlux

```{eval-rst}
.. autoclass:: abaqus.Load.SurfaceHeatFlux.SurfaceHeatFlux
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

#### SurfaceHeatFluxState

```{eval-rst}
.. autoclass:: abaqus.Load.SurfaceHeatFluxState.SurfaceHeatFluxState
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

#### SurfacePoreFluid

```{eval-rst}
.. autoclass:: abaqus.Load.SurfacePoreFluid.SurfacePoreFluid
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

#### SurfacePoreFluidState

```{eval-rst}
.. autoclass:: abaqus.Load.SurfacePoreFluidState.SurfacePoreFluidState
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

#### SurfaceTraction

```{eval-rst}
.. autoclass:: abaqus.Load.SurfaceTraction.SurfaceTraction
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

#### SurfaceTractionState

```{eval-rst}
.. autoclass:: abaqus.Load.SurfaceTractionState.SurfaceTractionState
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::

```

## Load case

The LoadCase object is used to define the loads and constraints comprising a particular loading condition and the linear response of a structure subjected to that loading condition.

### Create load cases

```{eval-rst}
.. autoclass:: abaqus.Load.LoadStep.LoadStep
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::

```

### Object features of load cases

```{eval-rst}
.. autoclass:: abaqus.Load.LoadCase.LoadCase
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```
