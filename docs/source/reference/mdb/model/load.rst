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


Object features of loads
~~~~~~~~~~~~~~~~~~~~~~~~

Load
****

.. autoclass:: abaqus.Load.Load.Load
    :members:

LoadState
*********

.. autoclass:: abaqus.Load.LoadState.LoadState
    :members:

BodyCharge
**********

.. autoclass:: abaqus.Load.BodyCharge.BodyCharge
    :members:

BodyChargeState
***************

.. autoclass:: abaqus.Load.BodyChargeState.BodyChargeState
    :members:

BodyConcentrationFlux
*********************

.. autoclass:: abaqus.Load.BodyConcentrationFlux.BodyConcentrationFlux
    :members:

BodyConcentrationFluxState
**************************

.. autoclass:: abaqus.Load.BodyConcentrationFluxState.BodyConcentrationFluxState
    :members:

BodyCurrent
***********

.. autoclass:: abaqus.Load.BodyCurrent.BodyCurrent
    :members:

BodyCurrentDensity
******************

.. autoclass:: abaqus.Load.BodyCurrentDensity.BodyCurrentDensity
    :members:

BodyCurrentState
****************

.. autoclass:: abaqus.Load.BodyCurrentState.BodyCurrentState
    :members:

BodyForce
*********

.. autoclass:: abaqus.Load.BodyForce.BodyForce
    :members:

BodyForceState
**************

.. autoclass:: abaqus.Load.BodyForceState.BodyForceState
    :members:

BodyHeatFlux
************

.. autoclass:: abaqus.Load.BodyHeatFlux.BodyHeatFlux
    :members:

BodyHeatFluxState
*****************

.. autoclass:: abaqus.Load.BodyHeatFluxState.BodyHeatFluxState
    :members:

BoltLoad
********

.. autoclass:: abaqus.Load.BoltLoad.BoltLoad
    :members:

BoltLoadState
*************

.. autoclass:: abaqus.Load.BoltLoadState.BoltLoadState
    :members:

ConcCharge
**********

.. autoclass:: abaqus.Load.ConcCharge.ConcCharge
    :members:

ConcConcFlux
************

.. autoclass:: abaqus.Load.ConcConcFlux.ConcConcFlux
    :members:

ConcCurrent
***********

.. autoclass:: abaqus.Load.ConcCurrent.ConcCurrent
    :members:

ConcCurrentState
****************

.. autoclass:: abaqus.Load.ConcCurrentState.ConcCurrentState
    :members:

ConcentratedChargeState
***********************

.. autoclass:: abaqus.Load.ConcentratedChargeState.ConcentratedChargeState
    :members:

ConcentratedConcentrationFluxState
**********************************

.. autoclass:: abaqus.Load.ConcentratedConcentrationFluxState.ConcentratedConcentrationFluxState
    :members:

ConcentratedForce
*****************

.. autoclass:: abaqus.Load.ConcentratedForce.ConcentratedForce
    :members:

ConcentratedForceState
**********************

.. autoclass:: abaqus.Load.ConcentratedForceState.ConcentratedForceState
    :members:

ConcentratedHeatFlux
********************

.. autoclass:: abaqus.Load.ConcentratedHeatFlux.ConcentratedHeatFlux
    :members:

ConcentratedHeatFluxState
*************************

.. autoclass:: abaqus.Load.ConcentratedHeatFluxState.ConcentratedHeatFluxState
    :members:

ConcentratedPoreFluidState
**************************

.. autoclass:: abaqus.Load.ConcentratedPoreFluidState.ConcentratedPoreFluidState
    :members:

ConcPoreFluid
*************

.. autoclass:: abaqus.Load.ConcPoreFluid.ConcPoreFluid
    :members:

ConnectorForce
**************

.. autoclass:: abaqus.Load.ConnectorForce.ConnectorForce
    :members:

ConnectorForceState
*******************

.. autoclass:: abaqus.Load.ConnectorForceState.ConnectorForceState
    :members:

ConnectorMoment
***************

.. autoclass:: abaqus.Load.ConnectorMoment.ConnectorMoment
    :members:

ConnectorMomentState
********************

.. autoclass:: abaqus.Load.ConnectorMomentState.ConnectorMomentState
    :members:

CoriolisForce
*************

.. autoclass:: abaqus.Load.CoriolisForce.CoriolisForce
    :members:

CoriolisForceState
******************

.. autoclass:: abaqus.Load.CoriolisForceState.CoriolisForceState
    :members:

Gravity
*******

.. autoclass:: abaqus.Load.Gravity.Gravity
    :members:

GravityState
************

.. autoclass:: abaqus.Load.GravityState.GravityState
    :members:

HydrostaticFluidFlowState
*************************

.. autoclass:: abaqus.Load.HydrostaticFluidFlowState.HydrostaticFluidFlowState
    :members:

InertiaRelief
*************

.. autoclass:: abaqus.Load.InertiaRelief.InertiaRelief
    :members:

InertiaReliefState
******************

.. autoclass:: abaqus.Load.InertiaReliefState.InertiaReliefState
    :members:

InwardVolAccel
**************

.. autoclass:: abaqus.Load.InwardVolAccel.InwardVolAccel
    :members:

InwardVolAccelState
*******************

.. autoclass:: abaqus.Load.InwardVolAccelState.InwardVolAccelState
    :members:

LineLoad
********

.. autoclass:: abaqus.Load.LineLoad.LineLoad
    :members:

LineLoadState
*************

.. autoclass:: abaqus.Load.LineLoadState.LineLoadState
    :members:

LoadStep
********

.. autoclass:: abaqus.Load.LoadStep.LoadStep
    :members:

Moment
******

.. autoclass:: abaqus.Load.Moment.Moment
    :members:

MomentState
***********

.. autoclass:: abaqus.Load.MomentState.MomentState
    :members:

PEGLoad
*******

.. autoclass:: abaqus.Load.PEGLoad.PEGLoad
    :members:

PEGLoadState
************

.. autoclass:: abaqus.Load.PEGLoadState.PEGLoadState
    :members:

PipePressure
************

.. autoclass:: abaqus.Load.PipePressure.PipePressure
    :members:

PipePressureState
*****************

.. autoclass:: abaqus.Load.PipePressureState.PipePressureState
    :members:

Pressure
********

.. autoclass:: abaqus.Load.Pressure.Pressure
    :members:

PressureState
*************

.. autoclass:: abaqus.Load.PressureState.PressureState
    :members:

RotationalBodyForce
*******************

.. autoclass:: abaqus.Load.RotationalBodyForce.RotationalBodyForce
    :members:

RotationalBodyForceState
************************

.. autoclass:: abaqus.Load.RotationalBodyForceState.RotationalBodyForceState
    :members:

ShellEdgeLoad
*************

.. autoclass:: abaqus.Load.ShellEdgeLoad.ShellEdgeLoad
    :members:

ShellEdgeLoadState
******************

.. autoclass:: abaqus.Load.ShellEdgeLoadState.ShellEdgeLoadState
    :members:

SubmodelSB
**********

.. autoclass:: abaqus.Load.SubmodelSB.SubmodelSB
    :members:

SubmodelSBState
***************

.. autoclass:: abaqus.Load.SubmodelSBState.SubmodelSBState
    :members:

SubstructureLoad
****************

.. autoclass:: abaqus.Load.SubstructureLoad.SubstructureLoad
    :members:

SubstructureLoadState
*********************

.. autoclass:: abaqus.Load.SubstructureLoadState.SubstructureLoadState
    :members:

SurfaceCharge
*************

.. autoclass:: abaqus.Load.SurfaceCharge.SurfaceCharge
    :members:

SurfaceChargeState
******************

.. autoclass:: abaqus.Load.SurfaceChargeState.SurfaceChargeState
    :members:

SurfaceConcentrationFlux
************************

.. autoclass:: abaqus.Load.SurfaceConcentrationFlux.SurfaceConcentrationFlux
    :members:

SurfaceConcentrationFluxState
*****************************

.. autoclass:: abaqus.Load.SurfaceConcentrationFluxState.SurfaceConcentrationFluxState
    :members:

SurfaceCurrent
**************

.. autoclass:: abaqus.Load.SurfaceCurrent.SurfaceCurrent
    :members:

SurfaceCurrentDensity
*********************

.. autoclass:: abaqus.Load.SurfaceCurrentDensity.SurfaceCurrentDensity
    :members:

SurfaceCurrentState
*******************

.. autoclass:: abaqus.Load.SurfaceCurrentState.SurfaceCurrentState
    :members:

SurfaceHeatFlux
***************

.. autoclass:: abaqus.Load.SurfaceHeatFlux.SurfaceHeatFlux
    :members:

SurfaceHeatFluxState
********************

.. autoclass:: abaqus.Load.SurfaceHeatFluxState.SurfaceHeatFluxState
    :members:

SurfacePoreFluid
****************

.. autoclass:: abaqus.Load.SurfacePoreFluid.SurfacePoreFluid
    :members:

SurfacePoreFluidState
*********************

.. autoclass:: abaqus.Load.SurfacePoreFluidState.SurfacePoreFluidState
    :members:

SurfaceTraction
***************

.. autoclass:: abaqus.Load.SurfaceTraction.SurfaceTraction
    :members:

SurfaceTractionState
********************

.. autoclass:: abaqus.Load.SurfaceTractionState.SurfaceTractionState
    :members:


Load case
---------

The LoadCase object is used to define the loads and constraints comprising a particular loading condition and the linear response of a structure subjected to that loading condition.


Create load cases
~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Load.LoadStep.LoadStep
    :members:


Object features of load cases
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Load.LoadCase.LoadCase
    :members: