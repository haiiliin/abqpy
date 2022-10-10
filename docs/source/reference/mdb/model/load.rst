====
Load
====

A specific type of load object and a specific type of load state object are designed for each type of load. A load object stores the nonpropagating data of a load as well as a number of instances of the corresponding load state object, each of which stores the propagating data of the load in a single step. Instances of the load state object are created and deleted internally by its corresponding load object.

Load Case commands are used for configuring load cases in specific types of steps that may use them.

Load
----

The Load object is the abstract base type for other Load objects. The Load object has no explicit constructor. The methods and members of the Load object are common to all objects derived from Load.


Create loads
~~~~~~~~~~~~

.. autoclass:: abaqus.Load.LoadModel.LoadModel
    :members:
    :special-members: __init__

    .. autoclasstoc::


Object features of loads
~~~~~~~~~~~~~~~~~~~~~~~~

Load
****

.. autoclass:: abaqus.Load.Load.Load
    :members:
    :special-members: __init__

    .. autoclasstoc::

LoadState
*********

.. autoclass:: abaqus.Load.LoadState.LoadState
    :members:
    :special-members: __init__

    .. autoclasstoc::

BodyCharge
**********

.. autoclass:: abaqus.Load.BodyCharge.BodyCharge
    :members:
    :special-members: __init__

    .. autoclasstoc::

BodyChargeState
***************

.. autoclass:: abaqus.Load.BodyChargeState.BodyChargeState
    :members:
    :special-members: __init__

    .. autoclasstoc::

BodyConcentrationFlux
*********************

.. autoclass:: abaqus.Load.BodyConcentrationFlux.BodyConcentrationFlux
    :members:
    :special-members: __init__

    .. autoclasstoc::

BodyConcentrationFluxState
**************************

.. autoclass:: abaqus.Load.BodyConcentrationFluxState.BodyConcentrationFluxState
    :members:
    :special-members: __init__

    .. autoclasstoc::

BodyCurrent
***********

.. autoclass:: abaqus.Load.BodyCurrent.BodyCurrent
    :members:
    :special-members: __init__

    .. autoclasstoc::

BodyCurrentDensity
******************

.. autoclass:: abaqus.Load.BodyCurrentDensity.BodyCurrentDensity
    :members:
    :special-members: __init__

    .. autoclasstoc::

BodyCurrentState
****************

.. autoclass:: abaqus.Load.BodyCurrentState.BodyCurrentState
    :members:
    :special-members: __init__

    .. autoclasstoc::

BodyForce
*********

.. autoclass:: abaqus.Load.BodyForce.BodyForce
    :members:
    :special-members: __init__

    .. autoclasstoc::

BodyForceState
**************

.. autoclass:: abaqus.Load.BodyForceState.BodyForceState
    :members:
    :special-members: __init__

    .. autoclasstoc::

BodyHeatFlux
************

.. autoclass:: abaqus.Load.BodyHeatFlux.BodyHeatFlux
    :members:
    :special-members: __init__

    .. autoclasstoc::

BodyHeatFluxState
*****************

.. autoclass:: abaqus.Load.BodyHeatFluxState.BodyHeatFluxState
    :members:
    :special-members: __init__

    .. autoclasstoc::

BoltLoad
********

.. autoclass:: abaqus.Load.BoltLoad.BoltLoad
    :members:
    :special-members: __init__

    .. autoclasstoc::

BoltLoadState
*************

.. autoclass:: abaqus.Load.BoltLoadState.BoltLoadState
    :members:
    :special-members: __init__

    .. autoclasstoc::

ConcCharge
**********

.. autoclass:: abaqus.Load.ConcCharge.ConcCharge
    :members:
    :special-members: __init__

    .. autoclasstoc::

ConcConcFlux
************

.. autoclass:: abaqus.Load.ConcConcFlux.ConcConcFlux
    :members:
    :special-members: __init__

    .. autoclasstoc::

ConcCurrent
***********

.. autoclass:: abaqus.Load.ConcCurrent.ConcCurrent
    :members:
    :special-members: __init__

    .. autoclasstoc::

ConcCurrentState
****************

.. autoclass:: abaqus.Load.ConcCurrentState.ConcCurrentState
    :members:
    :special-members: __init__

    .. autoclasstoc::

ConcentratedChargeState
***********************

.. autoclass:: abaqus.Load.ConcentratedChargeState.ConcentratedChargeState
    :members:
    :special-members: __init__

    .. autoclasstoc::

ConcentratedConcentrationFluxState
**********************************

.. autoclass:: abaqus.Load.ConcentratedConcentrationFluxState.ConcentratedConcentrationFluxState
    :members:
    :special-members: __init__

    .. autoclasstoc::

ConcentratedForce
*****************

.. autoclass:: abaqus.Load.ConcentratedForce.ConcentratedForce
    :members:
    :special-members: __init__

    .. autoclasstoc::

ConcentratedForceState
**********************

.. autoclass:: abaqus.Load.ConcentratedForceState.ConcentratedForceState
    :members:
    :special-members: __init__

    .. autoclasstoc::

ConcentratedHeatFlux
********************

.. autoclass:: abaqus.Load.ConcentratedHeatFlux.ConcentratedHeatFlux
    :members:
    :special-members: __init__

    .. autoclasstoc::

ConcentratedHeatFluxState
*************************

.. autoclass:: abaqus.Load.ConcentratedHeatFluxState.ConcentratedHeatFluxState
    :members:
    :special-members: __init__

    .. autoclasstoc::

ConcentratedPoreFluidState
**************************

.. autoclass:: abaqus.Load.ConcentratedPoreFluidState.ConcentratedPoreFluidState
    :members:
    :special-members: __init__

    .. autoclasstoc::

ConcPoreFluid
*************

.. autoclass:: abaqus.Load.ConcPoreFluid.ConcPoreFluid
    :members:
    :special-members: __init__

    .. autoclasstoc::

ConnectorForce
**************

.. autoclass:: abaqus.Load.ConnectorForce.ConnectorForce
    :members:
    :special-members: __init__

    .. autoclasstoc::

ConnectorForceState
*******************

.. autoclass:: abaqus.Load.ConnectorForceState.ConnectorForceState
    :members:
    :special-members: __init__

    .. autoclasstoc::

ConnectorMoment
***************

.. autoclass:: abaqus.Load.ConnectorMoment.ConnectorMoment
    :members:
    :special-members: __init__

    .. autoclasstoc::

ConnectorMomentState
********************

.. autoclass:: abaqus.Load.ConnectorMomentState.ConnectorMomentState
    :members:
    :special-members: __init__

    .. autoclasstoc::

CoriolisForce
*************

.. autoclass:: abaqus.Load.CoriolisForce.CoriolisForce
    :members:
    :special-members: __init__

    .. autoclasstoc::

CoriolisForceState
******************

.. autoclass:: abaqus.Load.CoriolisForceState.CoriolisForceState
    :members:
    :special-members: __init__

    .. autoclasstoc::

Gravity
*******

.. autoclass:: abaqus.Load.Gravity.Gravity
    :members:
    :special-members: __init__

    .. autoclasstoc::

GravityState
************

.. autoclass:: abaqus.Load.GravityState.GravityState
    :members:
    :special-members: __init__

    .. autoclasstoc::

HydrostaticFluidFlowState
*************************

.. autoclass:: abaqus.Load.HydrostaticFluidFlowState.HydrostaticFluidFlowState
    :members:
    :special-members: __init__

    .. autoclasstoc::

InertiaRelief
*************

.. autoclass:: abaqus.Load.InertiaRelief.InertiaRelief
    :members:
    :special-members: __init__

    .. autoclasstoc::

InertiaReliefState
******************

.. autoclass:: abaqus.Load.InertiaReliefState.InertiaReliefState
    :members:
    :special-members: __init__

    .. autoclasstoc::

InwardVolAccel
**************

.. autoclass:: abaqus.Load.InwardVolAccel.InwardVolAccel
    :members:
    :special-members: __init__

    .. autoclasstoc::

InwardVolAccelState
*******************

.. autoclass:: abaqus.Load.InwardVolAccelState.InwardVolAccelState
    :members:
    :special-members: __init__

    .. autoclasstoc::

LineLoad
********

.. autoclass:: abaqus.Load.LineLoad.LineLoad
    :members:
    :special-members: __init__

    .. autoclasstoc::

LineLoadState
*************

.. autoclass:: abaqus.Load.LineLoadState.LineLoadState
    :members:
    :special-members: __init__

    .. autoclasstoc::

Moment
******

.. autoclass:: abaqus.Load.Moment.Moment
    :members:
    :special-members: __init__

    .. autoclasstoc::

MomentState
***********

.. autoclass:: abaqus.Load.MomentState.MomentState
    :members:
    :special-members: __init__

    .. autoclasstoc::

PEGLoad
*******

.. autoclass:: abaqus.Load.PEGLoad.PEGLoad
    :members:
    :special-members: __init__

    .. autoclasstoc::

PEGLoadState
************

.. autoclass:: abaqus.Load.PEGLoadState.PEGLoadState
    :members:
    :special-members: __init__

    .. autoclasstoc::

PipePressure
************

.. autoclass:: abaqus.Load.PipePressure.PipePressure
    :members:
    :special-members: __init__

    .. autoclasstoc::

PipePressureState
*****************

.. autoclass:: abaqus.Load.PipePressureState.PipePressureState
    :members:
    :special-members: __init__

    .. autoclasstoc::

Pressure
********

.. autoclass:: abaqus.Load.Pressure.Pressure
    :members:
    :special-members: __init__

    .. autoclasstoc::

PressureState
*************

.. autoclass:: abaqus.Load.PressureState.PressureState
    :members:
    :special-members: __init__

    .. autoclasstoc::

RotationalBodyForce
*******************

.. autoclass:: abaqus.Load.RotationalBodyForce.RotationalBodyForce
    :members:
    :special-members: __init__

    .. autoclasstoc::

RotationalBodyForceState
************************

.. autoclass:: abaqus.Load.RotationalBodyForceState.RotationalBodyForceState
    :members:
    :special-members: __init__

    .. autoclasstoc::

ShellEdgeLoad
*************

.. autoclass:: abaqus.Load.ShellEdgeLoad.ShellEdgeLoad
    :members:
    :special-members: __init__

    .. autoclasstoc::

ShellEdgeLoadState
******************

.. autoclass:: abaqus.Load.ShellEdgeLoadState.ShellEdgeLoadState
    :members:
    :special-members: __init__

    .. autoclasstoc::

SubmodelSB
**********

.. autoclass:: abaqus.Load.SubmodelSB.SubmodelSB
    :members:
    :special-members: __init__

    .. autoclasstoc::

SubmodelSBState
***************

.. autoclass:: abaqus.Load.SubmodelSBState.SubmodelSBState
    :members:
    :special-members: __init__

    .. autoclasstoc::

SubstructureLoad
****************

.. autoclass:: abaqus.Load.SubstructureLoad.SubstructureLoad
    :members:
    :special-members: __init__

    .. autoclasstoc::

SubstructureLoadState
*********************

.. autoclass:: abaqus.Load.SubstructureLoadState.SubstructureLoadState
    :members:
    :special-members: __init__

    .. autoclasstoc::

SurfaceCharge
*************

.. autoclass:: abaqus.Load.SurfaceCharge.SurfaceCharge
    :members:
    :special-members: __init__

    .. autoclasstoc::

SurfaceChargeState
******************

.. autoclass:: abaqus.Load.SurfaceChargeState.SurfaceChargeState
    :members:
    :special-members: __init__

    .. autoclasstoc::

SurfaceConcentrationFlux
************************

.. autoclass:: abaqus.Load.SurfaceConcentrationFlux.SurfaceConcentrationFlux
    :members:
    :special-members: __init__

    .. autoclasstoc::

SurfaceConcentrationFluxState
*****************************

.. autoclass:: abaqus.Load.SurfaceConcentrationFluxState.SurfaceConcentrationFluxState
    :members:
    :special-members: __init__

    .. autoclasstoc::

SurfaceCurrent
**************

.. autoclass:: abaqus.Load.SurfaceCurrent.SurfaceCurrent
    :members:
    :special-members: __init__

    .. autoclasstoc::

SurfaceCurrentDensity
*********************

.. autoclass:: abaqus.Load.SurfaceCurrentDensity.SurfaceCurrentDensity
    :members:
    :special-members: __init__

    .. autoclasstoc::

SurfaceCurrentState
*******************

.. autoclass:: abaqus.Load.SurfaceCurrentState.SurfaceCurrentState
    :members:
    :special-members: __init__

    .. autoclasstoc::

SurfaceHeatFlux
***************

.. autoclass:: abaqus.Load.SurfaceHeatFlux.SurfaceHeatFlux
    :members:
    :special-members: __init__

    .. autoclasstoc::

SurfaceHeatFluxState
********************

.. autoclass:: abaqus.Load.SurfaceHeatFluxState.SurfaceHeatFluxState
    :members:
    :special-members: __init__

    .. autoclasstoc::

SurfacePoreFluid
****************

.. autoclass:: abaqus.Load.SurfacePoreFluid.SurfacePoreFluid
    :members:
    :special-members: __init__

    .. autoclasstoc::

SurfacePoreFluidState
*********************

.. autoclass:: abaqus.Load.SurfacePoreFluidState.SurfacePoreFluidState
    :members:
    :special-members: __init__

    .. autoclasstoc::

SurfaceTraction
***************

.. autoclass:: abaqus.Load.SurfaceTraction.SurfaceTraction
    :members:
    :special-members: __init__

    .. autoclasstoc::

SurfaceTractionState
********************

.. autoclass:: abaqus.Load.SurfaceTractionState.SurfaceTractionState
    :members:
    :special-members: __init__

    .. autoclasstoc::


Load case
---------

The LoadCase object is used to define the loads and constraints comprising a particular loading condition and the linear response of a structure subjected to that loading condition.


Create load cases
~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Load.LoadStep.LoadStep
    :members:
    :special-members: __init__

    .. autoclasstoc::


Object features of load cases
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Load.LoadCase.LoadCase
    :members:
    :special-members: __init__

    .. autoclasstoc::