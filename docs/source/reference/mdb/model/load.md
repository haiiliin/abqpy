# Load

A specific type of load object and a specific type of load state object are designed for each type of load. A load object stores the nonpropagating data of a load as well as a number of instances of the corresponding load state object, each of which stores the propagating data of the load in a single step. Instances of the load state object are created and deleted internally by its corresponding load object.

Load Case commands are used for configuring load cases in specific types of steps that may use them.

## Load

The Load object is the abstract base type for other Load objects. The Load object has no explicit constructor. The methods and members of the Load object are common to all objects derived from Load.

### Create loads

```{eval-rst}
.. autoclass:: abaqus.Load.LoadModel.LoadModel

    .. autoclasstoc::

```

### Classes

```{eval-rst}

.. collapse:: Click here to Expand

    .. autoclass:: abaqus.Load.Load.Load

        .. autoclasstoc::

    .. autoclass:: abaqus.Load.LoadState.LoadState

        .. autoclasstoc::

    .. autoclass:: abaqus.Load.BodyCharge.BodyCharge

        .. autoclasstoc::

    .. autoclass:: abaqus.Load.BodyChargeState.BodyChargeState

        .. autoclasstoc::

    .. autoclass:: abaqus.Load.BodyConcentrationFlux.BodyConcentrationFlux

        .. autoclasstoc::

    .. autoclass:: abaqus.Load.BodyConcentrationFluxState.BodyConcentrationFluxState

        .. autoclasstoc::

    .. autoclass:: abaqus.Load.BodyCurrent.BodyCurrent

        .. autoclasstoc::

    .. autoclass:: abaqus.Load.BodyCurrentDensity.BodyCurrentDensity

        .. autoclasstoc::

    .. autoclass:: abaqus.Load.BodyCurrentState.BodyCurrentState

        .. autoclasstoc::

    .. autoclass:: abaqus.Load.BodyForce.BodyForce

        .. autoclasstoc::

    .. autoclass:: abaqus.Load.BodyForceState.BodyForceState

        .. autoclasstoc::

    .. autoclass:: abaqus.Load.BodyHeatFlux.BodyHeatFlux

        .. autoclasstoc::

    .. autoclass:: abaqus.Load.BodyHeatFluxState.BodyHeatFluxState

        .. autoclasstoc::

    .. autoclass:: abaqus.Load.BoltLoad.BoltLoad

        .. autoclasstoc::

    .. autoclass:: abaqus.Load.BoltLoadState.BoltLoadState

        .. autoclasstoc::

    .. autoclass:: abaqus.Load.ConcCharge.ConcCharge

        .. autoclasstoc::

    .. autoclass:: abaqus.Load.ConcConcFlux.ConcConcFlux

        .. autoclasstoc::

    .. autoclass:: abaqus.Load.ConcCurrent.ConcCurrent

        .. autoclasstoc::

    .. autoclass:: abaqus.Load.ConcCurrentState.ConcCurrentState

        .. autoclasstoc::

    .. autoclass:: abaqus.Load.ConcentratedChargeState.ConcentratedChargeState

        .. autoclasstoc::

    .. autoclass:: abaqus.Load.ConcentratedConcentrationFluxState.ConcentratedConcentrationFluxState

        .. autoclasstoc::

    .. autoclass:: abaqus.Load.ConcentratedForce.ConcentratedForce

        .. autoclasstoc::

    .. autoclass:: abaqus.Load.ConcentratedForceState.ConcentratedForceState

        .. autoclasstoc::

    .. autoclass:: abaqus.Load.ConcentratedHeatFlux.ConcentratedHeatFlux

        .. autoclasstoc::

    .. autoclass:: abaqus.Load.ConcentratedHeatFluxState.ConcentratedHeatFluxState

        .. autoclasstoc::

    .. autoclass:: abaqus.Load.ConcentratedPoreFluidState.ConcentratedPoreFluidState

        .. autoclasstoc::

    .. autoclass:: abaqus.Load.ConcPoreFluid.ConcPoreFluid

        .. autoclasstoc::

    .. autoclass:: abaqus.Load.ConnectorForce.ConnectorForce

        .. autoclasstoc::

    .. autoclass:: abaqus.Load.ConnectorForceState.ConnectorForceState

        .. autoclasstoc::

    .. autoclass:: abaqus.Load.ConnectorMoment.ConnectorMoment

        .. autoclasstoc::

    .. autoclass:: abaqus.Load.ConnectorMomentState.ConnectorMomentState

        .. autoclasstoc::

    .. autoclass:: abaqus.Load.CoriolisForce.CoriolisForce

        .. autoclasstoc::

    .. autoclass:: abaqus.Load.CoriolisForceState.CoriolisForceState

        .. autoclasstoc::

    .. autoclass:: abaqus.Load.Gravity.Gravity

        .. autoclasstoc::

    .. autoclass:: abaqus.Load.GravityState.GravityState

        .. autoclasstoc::

    .. autoclass:: abaqus.Load.HydrostaticFluidFlowState.HydrostaticFluidFlowState

        .. autoclasstoc::

    .. autoclass:: abaqus.Load.InertiaRelief.InertiaRelief

        .. autoclasstoc::

    .. autoclass:: abaqus.Load.InertiaReliefState.InertiaReliefState

        .. autoclasstoc::

    .. autoclass:: abaqus.Load.InwardVolAccel.InwardVolAccel

        .. autoclasstoc::

    .. autoclass:: abaqus.Load.InwardVolAccelState.InwardVolAccelState

        .. autoclasstoc::

    .. autoclass:: abaqus.Load.LineLoad.LineLoad

        .. autoclasstoc::

    .. autoclass:: abaqus.Load.LineLoadState.LineLoadState

        .. autoclasstoc::

    .. autoclass:: abaqus.Load.Moment.Moment

        .. autoclasstoc::

    .. autoclass:: abaqus.Load.MomentState.MomentState

        .. autoclasstoc::

    .. autoclass:: abaqus.Load.PEGLoad.PEGLoad

        .. autoclasstoc::

    .. autoclass:: abaqus.Load.PEGLoadState.PEGLoadState

        .. autoclasstoc::

    .. autoclass:: abaqus.Load.PipePressure.PipePressure

        .. autoclasstoc::

    .. autoclass:: abaqus.Load.PipePressureState.PipePressureState

        .. autoclasstoc::

    .. autoclass:: abaqus.Load.Pressure.Pressure

        .. autoclasstoc::

    .. autoclass:: abaqus.Load.PressureState.PressureState

        .. autoclasstoc::

    .. autoclass:: abaqus.Load.RotationalBodyForce.RotationalBodyForce

        .. autoclasstoc::

    .. autoclass:: abaqus.Load.RotationalBodyForceState.RotationalBodyForceState

        .. autoclasstoc::

    .. autoclass:: abaqus.Load.ShellEdgeLoad.ShellEdgeLoad

        .. autoclasstoc::

    .. autoclass:: abaqus.Load.ShellEdgeLoadState.ShellEdgeLoadState

        .. autoclasstoc::

    .. autoclass:: abaqus.Load.SubmodelSB.SubmodelSB

        .. autoclasstoc::

    .. autoclass:: abaqus.Load.SubmodelSBState.SubmodelSBState

        .. autoclasstoc::

    .. autoclass:: abaqus.Load.SubstructureLoad.SubstructureLoad

        .. autoclasstoc::

    .. autoclass:: abaqus.Load.SubstructureLoadState.SubstructureLoadState

        .. autoclasstoc::

    .. autoclass:: abaqus.Load.SurfaceCharge.SurfaceCharge

        .. autoclasstoc::

    .. autoclass:: abaqus.Load.SurfaceChargeState.SurfaceChargeState

        .. autoclasstoc::

    .. autoclass:: abaqus.Load.SurfaceConcentrationFlux.SurfaceConcentrationFlux

        .. autoclasstoc::

    .. autoclass:: abaqus.Load.SurfaceConcentrationFluxState.SurfaceConcentrationFluxState

        .. autoclasstoc::

    .. autoclass:: abaqus.Load.SurfaceCurrent.SurfaceCurrent

        .. autoclasstoc::

    .. autoclass:: abaqus.Load.SurfaceCurrentDensity.SurfaceCurrentDensity

        .. autoclasstoc::

    .. autoclass:: abaqus.Load.SurfaceCurrentState.SurfaceCurrentState

        .. autoclasstoc::

    .. autoclass:: abaqus.Load.SurfaceHeatFlux.SurfaceHeatFlux

        .. autoclasstoc::

    .. autoclass:: abaqus.Load.SurfaceHeatFluxState.SurfaceHeatFluxState

        .. autoclasstoc::

    .. autoclass:: abaqus.Load.SurfacePoreFluid.SurfacePoreFluid

        .. autoclasstoc::

    .. autoclass:: abaqus.Load.SurfacePoreFluidState.SurfacePoreFluidState

        .. autoclasstoc::

    .. autoclass:: abaqus.Load.SurfaceTraction.SurfaceTraction

        .. autoclasstoc::

    .. autoclass:: abaqus.Load.SurfaceTractionState.SurfaceTractionState

        .. autoclasstoc::
```

## Load case

The LoadCase object is used to define the loads and constraints comprising a particular loading condition and the linear response of a structure subjected to that loading condition.

### Create load cases

```{eval-rst}
.. autoclass:: abaqus.Load.LoadStep.LoadStep

    .. autoclasstoc::

```

### Classes

```{eval-rst}

.. collapse:: Click here to Expand

    .. autoclass:: abaqus.Load.LoadCase.LoadCase

        .. autoclasstoc::
```
