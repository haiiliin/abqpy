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
    :special-members:

    .. autoclasstoc::


Object features of loads
~~~~~~~~~~~~~~~~~~~~~~~~

Load
****

.. autoclass:: abaqus.Load.Load.Load
    :members:
    :special-members:

    .. autoclasstoc::

LoadState
*********

.. autoclass:: abaqus.Load.LoadState.LoadState
    :members:
    :special-members:

    .. autoclasstoc::

BodyCharge
**********

.. autoclass:: abaqus.Load.BodyCharge.BodyCharge
    :members:
    :special-members:

    .. autoclasstoc::

BodyChargeState
***************

.. autoclass:: abaqus.Load.BodyChargeState.BodyChargeState
    :members:
    :special-members:

    .. autoclasstoc::

BodyConcentrationFlux
*********************

.. autoclass:: abaqus.Load.BodyConcentrationFlux.BodyConcentrationFlux
    :members:
    :special-members:

    .. autoclasstoc::

BodyConcentrationFluxState
**************************

.. autoclass:: abaqus.Load.BodyConcentrationFluxState.BodyConcentrationFluxState
    :members:
    :special-members:

    .. autoclasstoc::

BodyCurrent
***********

.. autoclass:: abaqus.Load.BodyCurrent.BodyCurrent
    :members:
    :special-members:

    .. autoclasstoc::

BodyCurrentDensity
******************

.. autoclass:: abaqus.Load.BodyCurrentDensity.BodyCurrentDensity
    :members:
    :special-members:

    .. autoclasstoc::

BodyCurrentState
****************

.. autoclass:: abaqus.Load.BodyCurrentState.BodyCurrentState
    :members:
    :special-members:

    .. autoclasstoc::

BodyForce
*********

.. autoclass:: abaqus.Load.BodyForce.BodyForce
    :members:
    :special-members:

    .. autoclasstoc::

BodyForceState
**************

.. autoclass:: abaqus.Load.BodyForceState.BodyForceState
    :members:
    :special-members:

    .. autoclasstoc::

BodyHeatFlux
************

.. autoclass:: abaqus.Load.BodyHeatFlux.BodyHeatFlux
    :members:
    :special-members:

    .. autoclasstoc::

BodyHeatFluxState
*****************

.. autoclass:: abaqus.Load.BodyHeatFluxState.BodyHeatFluxState
    :members:
    :special-members:

    .. autoclasstoc::

BoltLoad
********

.. autoclass:: abaqus.Load.BoltLoad.BoltLoad
    :members:
    :special-members:

    .. autoclasstoc::

BoltLoadState
*************

.. autoclass:: abaqus.Load.BoltLoadState.BoltLoadState
    :members:
    :special-members:

    .. autoclasstoc::

ConcCharge
**********

.. autoclass:: abaqus.Load.ConcCharge.ConcCharge
    :members:
    :special-members:

    .. autoclasstoc::

ConcConcFlux
************

.. autoclass:: abaqus.Load.ConcConcFlux.ConcConcFlux
    :members:
    :special-members:

    .. autoclasstoc::

ConcCurrent
***********

.. autoclass:: abaqus.Load.ConcCurrent.ConcCurrent
    :members:
    :special-members:

    .. autoclasstoc::

ConcCurrentState
****************

.. autoclass:: abaqus.Load.ConcCurrentState.ConcCurrentState
    :members:
    :special-members:

    .. autoclasstoc::

ConcentratedChargeState
***********************

.. autoclass:: abaqus.Load.ConcentratedChargeState.ConcentratedChargeState
    :members:
    :special-members:

    .. autoclasstoc::

ConcentratedConcentrationFluxState
**********************************

.. autoclass:: abaqus.Load.ConcentratedConcentrationFluxState.ConcentratedConcentrationFluxState
    :members:
    :special-members:

    .. autoclasstoc::

ConcentratedForce
*****************

.. autoclass:: abaqus.Load.ConcentratedForce.ConcentratedForce
    :members:
    :special-members:

    .. autoclasstoc::

ConcentratedForceState
**********************

.. autoclass:: abaqus.Load.ConcentratedForceState.ConcentratedForceState
    :members:
    :special-members:

    .. autoclasstoc::

ConcentratedHeatFlux
********************

.. autoclass:: abaqus.Load.ConcentratedHeatFlux.ConcentratedHeatFlux
    :members:
    :special-members:

    .. autoclasstoc::

ConcentratedHeatFluxState
*************************

.. autoclass:: abaqus.Load.ConcentratedHeatFluxState.ConcentratedHeatFluxState
    :members:
    :special-members:

    .. autoclasstoc::

ConcentratedPoreFluidState
**************************

.. autoclass:: abaqus.Load.ConcentratedPoreFluidState.ConcentratedPoreFluidState
    :members:
    :special-members:

    .. autoclasstoc::

ConcPoreFluid
*************

.. autoclass:: abaqus.Load.ConcPoreFluid.ConcPoreFluid
    :members:
    :special-members:

    .. autoclasstoc::

ConnectorForce
**************

.. autoclass:: abaqus.Load.ConnectorForce.ConnectorForce
    :members:
    :special-members:

    .. autoclasstoc::

ConnectorForceState
*******************

.. autoclass:: abaqus.Load.ConnectorForceState.ConnectorForceState
    :members:
    :special-members:

    .. autoclasstoc::

ConnectorMoment
***************

.. autoclass:: abaqus.Load.ConnectorMoment.ConnectorMoment
    :members:
    :special-members:

    .. autoclasstoc::

ConnectorMomentState
********************

.. autoclass:: abaqus.Load.ConnectorMomentState.ConnectorMomentState
    :members:
    :special-members:

    .. autoclasstoc::

CoriolisForce
*************

.. autoclass:: abaqus.Load.CoriolisForce.CoriolisForce
    :members:
    :special-members:

    .. autoclasstoc::

CoriolisForceState
******************

.. autoclass:: abaqus.Load.CoriolisForceState.CoriolisForceState
    :members:
    :special-members:

    .. autoclasstoc::

Gravity
*******

.. autoclass:: abaqus.Load.Gravity.Gravity
    :members:
    :special-members:

    .. autoclasstoc::

GravityState
************

.. autoclass:: abaqus.Load.GravityState.GravityState
    :members:
    :special-members:

    .. autoclasstoc::

HydrostaticFluidFlowState
*************************

.. autoclass:: abaqus.Load.HydrostaticFluidFlowState.HydrostaticFluidFlowState
    :members:
    :special-members:

    .. autoclasstoc::

InertiaRelief
*************

.. autoclass:: abaqus.Load.InertiaRelief.InertiaRelief
    :members:
    :special-members:

    .. autoclasstoc::

InertiaReliefState
******************

.. autoclass:: abaqus.Load.InertiaReliefState.InertiaReliefState
    :members:
    :special-members:

    .. autoclasstoc::

InwardVolAccel
**************

.. autoclass:: abaqus.Load.InwardVolAccel.InwardVolAccel
    :members:
    :special-members:

    .. autoclasstoc::

InwardVolAccelState
*******************

.. autoclass:: abaqus.Load.InwardVolAccelState.InwardVolAccelState
    :members:
    :special-members:

    .. autoclasstoc::

LineLoad
********

.. autoclass:: abaqus.Load.LineLoad.LineLoad
    :members:
    :special-members:

    .. autoclasstoc::

LineLoadState
*************

.. autoclass:: abaqus.Load.LineLoadState.LineLoadState
    :members:
    :special-members:

    .. autoclasstoc::

Moment
******

.. autoclass:: abaqus.Load.Moment.Moment
    :members:
    :special-members:

    .. autoclasstoc::

MomentState
***********

.. autoclass:: abaqus.Load.MomentState.MomentState
    :members:
    :special-members:

    .. autoclasstoc::

PEGLoad
*******

.. autoclass:: abaqus.Load.PEGLoad.PEGLoad
    :members:
    :special-members:

    .. autoclasstoc::

PEGLoadState
************

.. autoclass:: abaqus.Load.PEGLoadState.PEGLoadState
    :members:
    :special-members:

    .. autoclasstoc::

PipePressure
************

.. autoclass:: abaqus.Load.PipePressure.PipePressure
    :members:
    :special-members:

    .. autoclasstoc::

PipePressureState
*****************

.. autoclass:: abaqus.Load.PipePressureState.PipePressureState
    :members:
    :special-members:

    .. autoclasstoc::

Pressure
********

.. autoclass:: abaqus.Load.Pressure.Pressure
    :members:
    :special-members:

    .. autoclasstoc::

PressureState
*************

.. autoclass:: abaqus.Load.PressureState.PressureState
    :members:
    :special-members:

    .. autoclasstoc::

RotationalBodyForce
*******************

.. autoclass:: abaqus.Load.RotationalBodyForce.RotationalBodyForce
    :members:
    :special-members:

    .. autoclasstoc::

RotationalBodyForceState
************************

.. autoclass:: abaqus.Load.RotationalBodyForceState.RotationalBodyForceState
    :members:
    :special-members:

    .. autoclasstoc::

ShellEdgeLoad
*************

.. autoclass:: abaqus.Load.ShellEdgeLoad.ShellEdgeLoad
    :members:
    :special-members:

    .. autoclasstoc::

ShellEdgeLoadState
******************

.. autoclass:: abaqus.Load.ShellEdgeLoadState.ShellEdgeLoadState
    :members:
    :special-members:

    .. autoclasstoc::

SubmodelSB
**********

.. autoclass:: abaqus.Load.SubmodelSB.SubmodelSB
    :members:
    :special-members:

    .. autoclasstoc::

SubmodelSBState
***************

.. autoclass:: abaqus.Load.SubmodelSBState.SubmodelSBState
    :members:
    :special-members:

    .. autoclasstoc::

SubstructureLoad
****************

.. autoclass:: abaqus.Load.SubstructureLoad.SubstructureLoad
    :members:
    :special-members:

    .. autoclasstoc::

SubstructureLoadState
*********************

.. autoclass:: abaqus.Load.SubstructureLoadState.SubstructureLoadState
    :members:
    :special-members:

    .. autoclasstoc::

SurfaceCharge
*************

.. autoclass:: abaqus.Load.SurfaceCharge.SurfaceCharge
    :members:
    :special-members:

    .. autoclasstoc::

SurfaceChargeState
******************

.. autoclass:: abaqus.Load.SurfaceChargeState.SurfaceChargeState
    :members:
    :special-members:

    .. autoclasstoc::

SurfaceConcentrationFlux
************************

.. autoclass:: abaqus.Load.SurfaceConcentrationFlux.SurfaceConcentrationFlux
    :members:
    :special-members:

    .. autoclasstoc::

SurfaceConcentrationFluxState
*****************************

.. autoclass:: abaqus.Load.SurfaceConcentrationFluxState.SurfaceConcentrationFluxState
    :members:
    :special-members:

    .. autoclasstoc::

SurfaceCurrent
**************

.. autoclass:: abaqus.Load.SurfaceCurrent.SurfaceCurrent
    :members:
    :special-members:

    .. autoclasstoc::

SurfaceCurrentDensity
*********************

.. autoclass:: abaqus.Load.SurfaceCurrentDensity.SurfaceCurrentDensity
    :members:
    :special-members:

    .. autoclasstoc::

SurfaceCurrentState
*******************

.. autoclass:: abaqus.Load.SurfaceCurrentState.SurfaceCurrentState
    :members:
    :special-members:

    .. autoclasstoc::

SurfaceHeatFlux
***************

.. autoclass:: abaqus.Load.SurfaceHeatFlux.SurfaceHeatFlux
    :members:
    :special-members:

    .. autoclasstoc::

SurfaceHeatFluxState
********************

.. autoclass:: abaqus.Load.SurfaceHeatFluxState.SurfaceHeatFluxState
    :members:
    :special-members:

    .. autoclasstoc::

SurfacePoreFluid
****************

.. autoclass:: abaqus.Load.SurfacePoreFluid.SurfacePoreFluid
    :members:
    :special-members:

    .. autoclasstoc::

SurfacePoreFluidState
*********************

.. autoclass:: abaqus.Load.SurfacePoreFluidState.SurfacePoreFluidState
    :members:
    :special-members:

    .. autoclasstoc::

SurfaceTraction
***************

.. autoclass:: abaqus.Load.SurfaceTraction.SurfaceTraction
    :members:
    :special-members:

    .. autoclasstoc::

SurfaceTractionState
********************

.. autoclass:: abaqus.Load.SurfaceTractionState.SurfaceTractionState
    :members:
    :special-members:

    .. autoclasstoc::


Load case
---------

The LoadCase object is used to define the loads and constraints comprising a particular loading condition and the linear response of a structure subjected to that loading condition.


Create load cases
~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Load.LoadStep.LoadStep
    :members:
    :special-members:

    .. autoclasstoc::


Object features of load cases
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Load.LoadCase.LoadCase
    :members:
    :special-members:

    .. autoclasstoc::