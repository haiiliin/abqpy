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

    .. autoclasstoc::


Object features of loads
~~~~~~~~~~~~~~~~~~~~~~~~

Load
****

.. autoclass:: abaqus.Load.Load.Load
    :members:

    .. autoclasstoc::

LoadState
*********

.. autoclass:: abaqus.Load.LoadState.LoadState
    :members:

    .. autoclasstoc::

BodyCharge
**********

.. autoclass:: abaqus.Load.BodyCharge.BodyCharge
    :members:

    .. autoclasstoc::

BodyChargeState
***************

.. autoclass:: abaqus.Load.BodyChargeState.BodyChargeState
    :members:

    .. autoclasstoc::

BodyConcentrationFlux
*********************

.. autoclass:: abaqus.Load.BodyConcentrationFlux.BodyConcentrationFlux
    :members:

    .. autoclasstoc::

BodyConcentrationFluxState
**************************

.. autoclass:: abaqus.Load.BodyConcentrationFluxState.BodyConcentrationFluxState
    :members:

    .. autoclasstoc::

BodyCurrent
***********

.. autoclass:: abaqus.Load.BodyCurrent.BodyCurrent
    :members:

    .. autoclasstoc::

BodyCurrentDensity
******************

.. autoclass:: abaqus.Load.BodyCurrentDensity.BodyCurrentDensity
    :members:

    .. autoclasstoc::

BodyCurrentState
****************

.. autoclass:: abaqus.Load.BodyCurrentState.BodyCurrentState
    :members:

    .. autoclasstoc::

BodyForce
*********

.. autoclass:: abaqus.Load.BodyForce.BodyForce
    :members:

    .. autoclasstoc::

BodyForceState
**************

.. autoclass:: abaqus.Load.BodyForceState.BodyForceState
    :members:

    .. autoclasstoc::

BodyHeatFlux
************

.. autoclass:: abaqus.Load.BodyHeatFlux.BodyHeatFlux
    :members:

    .. autoclasstoc::

BodyHeatFluxState
*****************

.. autoclass:: abaqus.Load.BodyHeatFluxState.BodyHeatFluxState
    :members:

    .. autoclasstoc::

BoltLoad
********

.. autoclass:: abaqus.Load.BoltLoad.BoltLoad
    :members:

    .. autoclasstoc::

BoltLoadState
*************

.. autoclass:: abaqus.Load.BoltLoadState.BoltLoadState
    :members:

    .. autoclasstoc::

ConcCharge
**********

.. autoclass:: abaqus.Load.ConcCharge.ConcCharge
    :members:

    .. autoclasstoc::

ConcConcFlux
************

.. autoclass:: abaqus.Load.ConcConcFlux.ConcConcFlux
    :members:

    .. autoclasstoc::

ConcCurrent
***********

.. autoclass:: abaqus.Load.ConcCurrent.ConcCurrent
    :members:

    .. autoclasstoc::

ConcCurrentState
****************

.. autoclass:: abaqus.Load.ConcCurrentState.ConcCurrentState
    :members:

    .. autoclasstoc::

ConcentratedChargeState
***********************

.. autoclass:: abaqus.Load.ConcentratedChargeState.ConcentratedChargeState
    :members:

    .. autoclasstoc::

ConcentratedConcentrationFluxState
**********************************

.. autoclass:: abaqus.Load.ConcentratedConcentrationFluxState.ConcentratedConcentrationFluxState
    :members:

    .. autoclasstoc::

ConcentratedForce
*****************

.. autoclass:: abaqus.Load.ConcentratedForce.ConcentratedForce
    :members:

    .. autoclasstoc::

ConcentratedForceState
**********************

.. autoclass:: abaqus.Load.ConcentratedForceState.ConcentratedForceState
    :members:

    .. autoclasstoc::

ConcentratedHeatFlux
********************

.. autoclass:: abaqus.Load.ConcentratedHeatFlux.ConcentratedHeatFlux
    :members:

    .. autoclasstoc::

ConcentratedHeatFluxState
*************************

.. autoclass:: abaqus.Load.ConcentratedHeatFluxState.ConcentratedHeatFluxState
    :members:

    .. autoclasstoc::

ConcentratedPoreFluidState
**************************

.. autoclass:: abaqus.Load.ConcentratedPoreFluidState.ConcentratedPoreFluidState
    :members:

    .. autoclasstoc::

ConcPoreFluid
*************

.. autoclass:: abaqus.Load.ConcPoreFluid.ConcPoreFluid
    :members:

    .. autoclasstoc::

ConnectorForce
**************

.. autoclass:: abaqus.Load.ConnectorForce.ConnectorForce
    :members:

    .. autoclasstoc::

ConnectorForceState
*******************

.. autoclass:: abaqus.Load.ConnectorForceState.ConnectorForceState
    :members:

    .. autoclasstoc::

ConnectorMoment
***************

.. autoclass:: abaqus.Load.ConnectorMoment.ConnectorMoment
    :members:

    .. autoclasstoc::

ConnectorMomentState
********************

.. autoclass:: abaqus.Load.ConnectorMomentState.ConnectorMomentState
    :members:

    .. autoclasstoc::

CoriolisForce
*************

.. autoclass:: abaqus.Load.CoriolisForce.CoriolisForce
    :members:

    .. autoclasstoc::

CoriolisForceState
******************

.. autoclass:: abaqus.Load.CoriolisForceState.CoriolisForceState
    :members:

    .. autoclasstoc::

Gravity
*******

.. autoclass:: abaqus.Load.Gravity.Gravity
    :members:

    .. autoclasstoc::

GravityState
************

.. autoclass:: abaqus.Load.GravityState.GravityState
    :members:

    .. autoclasstoc::

HydrostaticFluidFlowState
*************************

.. autoclass:: abaqus.Load.HydrostaticFluidFlowState.HydrostaticFluidFlowState
    :members:

    .. autoclasstoc::

InertiaRelief
*************

.. autoclass:: abaqus.Load.InertiaRelief.InertiaRelief
    :members:

    .. autoclasstoc::

InertiaReliefState
******************

.. autoclass:: abaqus.Load.InertiaReliefState.InertiaReliefState
    :members:

    .. autoclasstoc::

InwardVolAccel
**************

.. autoclass:: abaqus.Load.InwardVolAccel.InwardVolAccel
    :members:

    .. autoclasstoc::

InwardVolAccelState
*******************

.. autoclass:: abaqus.Load.InwardVolAccelState.InwardVolAccelState
    :members:

    .. autoclasstoc::

LineLoad
********

.. autoclass:: abaqus.Load.LineLoad.LineLoad
    :members:

    .. autoclasstoc::

LineLoadState
*************

.. autoclass:: abaqus.Load.LineLoadState.LineLoadState
    :members:

    .. autoclasstoc::

Moment
******

.. autoclass:: abaqus.Load.Moment.Moment
    :members:

    .. autoclasstoc::

MomentState
***********

.. autoclass:: abaqus.Load.MomentState.MomentState
    :members:

    .. autoclasstoc::

PEGLoad
*******

.. autoclass:: abaqus.Load.PEGLoad.PEGLoad
    :members:

    .. autoclasstoc::

PEGLoadState
************

.. autoclass:: abaqus.Load.PEGLoadState.PEGLoadState
    :members:

    .. autoclasstoc::

PipePressure
************

.. autoclass:: abaqus.Load.PipePressure.PipePressure
    :members:

    .. autoclasstoc::

PipePressureState
*****************

.. autoclass:: abaqus.Load.PipePressureState.PipePressureState
    :members:

    .. autoclasstoc::

Pressure
********

.. autoclass:: abaqus.Load.Pressure.Pressure
    :members:

    .. autoclasstoc::

PressureState
*************

.. autoclass:: abaqus.Load.PressureState.PressureState
    :members:

    .. autoclasstoc::

RotationalBodyForce
*******************

.. autoclass:: abaqus.Load.RotationalBodyForce.RotationalBodyForce
    :members:

    .. autoclasstoc::

RotationalBodyForceState
************************

.. autoclass:: abaqus.Load.RotationalBodyForceState.RotationalBodyForceState
    :members:

    .. autoclasstoc::

ShellEdgeLoad
*************

.. autoclass:: abaqus.Load.ShellEdgeLoad.ShellEdgeLoad
    :members:

    .. autoclasstoc::

ShellEdgeLoadState
******************

.. autoclass:: abaqus.Load.ShellEdgeLoadState.ShellEdgeLoadState
    :members:

    .. autoclasstoc::

SubmodelSB
**********

.. autoclass:: abaqus.Load.SubmodelSB.SubmodelSB
    :members:

    .. autoclasstoc::

SubmodelSBState
***************

.. autoclass:: abaqus.Load.SubmodelSBState.SubmodelSBState
    :members:

    .. autoclasstoc::

SubstructureLoad
****************

.. autoclass:: abaqus.Load.SubstructureLoad.SubstructureLoad
    :members:

    .. autoclasstoc::

SubstructureLoadState
*********************

.. autoclass:: abaqus.Load.SubstructureLoadState.SubstructureLoadState
    :members:

    .. autoclasstoc::

SurfaceCharge
*************

.. autoclass:: abaqus.Load.SurfaceCharge.SurfaceCharge
    :members:

    .. autoclasstoc::

SurfaceChargeState
******************

.. autoclass:: abaqus.Load.SurfaceChargeState.SurfaceChargeState
    :members:

    .. autoclasstoc::

SurfaceConcentrationFlux
************************

.. autoclass:: abaqus.Load.SurfaceConcentrationFlux.SurfaceConcentrationFlux
    :members:

    .. autoclasstoc::

SurfaceConcentrationFluxState
*****************************

.. autoclass:: abaqus.Load.SurfaceConcentrationFluxState.SurfaceConcentrationFluxState
    :members:

    .. autoclasstoc::

SurfaceCurrent
**************

.. autoclass:: abaqus.Load.SurfaceCurrent.SurfaceCurrent
    :members:

    .. autoclasstoc::

SurfaceCurrentDensity
*********************

.. autoclass:: abaqus.Load.SurfaceCurrentDensity.SurfaceCurrentDensity
    :members:

    .. autoclasstoc::

SurfaceCurrentState
*******************

.. autoclass:: abaqus.Load.SurfaceCurrentState.SurfaceCurrentState
    :members:

    .. autoclasstoc::

SurfaceHeatFlux
***************

.. autoclass:: abaqus.Load.SurfaceHeatFlux.SurfaceHeatFlux
    :members:

    .. autoclasstoc::

SurfaceHeatFluxState
********************

.. autoclass:: abaqus.Load.SurfaceHeatFluxState.SurfaceHeatFluxState
    :members:

    .. autoclasstoc::

SurfacePoreFluid
****************

.. autoclass:: abaqus.Load.SurfacePoreFluid.SurfacePoreFluid
    :members:

    .. autoclasstoc::

SurfacePoreFluidState
*********************

.. autoclass:: abaqus.Load.SurfacePoreFluidState.SurfacePoreFluidState
    :members:

    .. autoclasstoc::

SurfaceTraction
***************

.. autoclass:: abaqus.Load.SurfaceTraction.SurfaceTraction
    :members:

    .. autoclasstoc::

SurfaceTractionState
********************

.. autoclass:: abaqus.Load.SurfaceTractionState.SurfaceTractionState
    :members:

    .. autoclasstoc::


Load case
---------

The LoadCase object is used to define the loads and constraints comprising a particular loading condition and the linear response of a structure subjected to that loading condition.


Create load cases
~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Load.LoadStep.LoadStep
    :members:

    .. autoclasstoc::


Object features of load cases
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Load.LoadCase.LoadCase
    :members:

    .. autoclasstoc::