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

### Other Classes

```{eval-rst}

.. toggle::

    .. autoclass:: abaqus.Load.Load.Load
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Load.LoadState.LoadState
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Load.BodyCharge.BodyCharge
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Load.BodyChargeState.BodyChargeState
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Load.BodyConcentrationFlux.BodyConcentrationFlux
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Load.BodyConcentrationFluxState.BodyConcentrationFluxState
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Load.BodyCurrent.BodyCurrent
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Load.BodyCurrentDensity.BodyCurrentDensity
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Load.BodyCurrentState.BodyCurrentState
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Load.BodyForce.BodyForce
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Load.BodyForceState.BodyForceState
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Load.BodyHeatFlux.BodyHeatFlux
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Load.BodyHeatFluxState.BodyHeatFluxState
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Load.BoltLoad.BoltLoad
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Load.BoltLoadState.BoltLoadState
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Load.ConcCharge.ConcCharge
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Load.ConcConcFlux.ConcConcFlux
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Load.ConcCurrent.ConcCurrent
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Load.ConcCurrentState.ConcCurrentState
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Load.ConcentratedChargeState.ConcentratedChargeState
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Load.ConcentratedConcentrationFluxState.ConcentratedConcentrationFluxState
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Load.ConcentratedForce.ConcentratedForce
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Load.ConcentratedForceState.ConcentratedForceState
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Load.ConcentratedHeatFlux.ConcentratedHeatFlux
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Load.ConcentratedHeatFluxState.ConcentratedHeatFluxState
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Load.ConcentratedPoreFluidState.ConcentratedPoreFluidState
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Load.ConcPoreFluid.ConcPoreFluid
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Load.ConnectorForce.ConnectorForce
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Load.ConnectorForceState.ConnectorForceState
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Load.ConnectorMoment.ConnectorMoment
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Load.ConnectorMomentState.ConnectorMomentState
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Load.CoriolisForce.CoriolisForce
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Load.CoriolisForceState.CoriolisForceState
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Load.Gravity.Gravity
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Load.GravityState.GravityState
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Load.HydrostaticFluidFlowState.HydrostaticFluidFlowState
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Load.InertiaRelief.InertiaRelief
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Load.InertiaReliefState.InertiaReliefState
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Load.InwardVolAccel.InwardVolAccel
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Load.InwardVolAccelState.InwardVolAccelState
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Load.LineLoad.LineLoad
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Load.LineLoadState.LineLoadState
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Load.Moment.Moment
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Load.MomentState.MomentState
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Load.PEGLoad.PEGLoad
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Load.PEGLoadState.PEGLoadState
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Load.PipePressure.PipePressure
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Load.PipePressureState.PipePressureState
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Load.Pressure.Pressure
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Load.PressureState.PressureState
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Load.RotationalBodyForce.RotationalBodyForce
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Load.RotationalBodyForceState.RotationalBodyForceState
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Load.ShellEdgeLoad.ShellEdgeLoad
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Load.ShellEdgeLoadState.ShellEdgeLoadState
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Load.SubmodelSB.SubmodelSB
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Load.SubmodelSBState.SubmodelSBState
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Load.SubstructureLoad.SubstructureLoad
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Load.SubstructureLoadState.SubstructureLoadState
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Load.SurfaceCharge.SurfaceCharge
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Load.SurfaceChargeState.SurfaceChargeState
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Load.SurfaceConcentrationFlux.SurfaceConcentrationFlux
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Load.SurfaceConcentrationFluxState.SurfaceConcentrationFluxState
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Load.SurfaceCurrent.SurfaceCurrent
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Load.SurfaceCurrentDensity.SurfaceCurrentDensity
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Load.SurfaceCurrentState.SurfaceCurrentState
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Load.SurfaceHeatFlux.SurfaceHeatFlux
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Load.SurfaceHeatFluxState.SurfaceHeatFluxState
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Load.SurfacePoreFluid.SurfacePoreFluid
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Load.SurfacePoreFluidState.SurfacePoreFluidState
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Load.SurfaceTraction.SurfaceTraction
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

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

### Other Classes

```{eval-rst}

.. toggle::

    .. autoclass:: abaqus.Load.LoadCase.LoadCase
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::
```
