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
    :show-inheritance:

    .. autoclasstoc::


Object features of loads
~~~~~~~~~~~~~~~~~~~~~~~~

Load
****

.. autoclass:: abaqus.Load.Load.Load
    :members:
    :special-members:
    :show-inheritance:

    .. autoclasstoc::

LoadState
*********

.. autoclass:: abaqus.Load.LoadState.LoadState
    :members:
    :special-members:
    :show-inheritance:

    .. autoclasstoc::

BodyCharge
**********

.. autoclass:: abaqus.Load.BodyCharge.BodyCharge
    :members:
    :special-members:
    :show-inheritance:

    .. autoclasstoc::

BodyChargeState
***************

.. autoclass:: abaqus.Load.BodyChargeState.BodyChargeState
    :members:
    :special-members:
    :show-inheritance:

    .. autoclasstoc::

BodyConcentrationFlux
*********************

.. autoclass:: abaqus.Load.BodyConcentrationFlux.BodyConcentrationFlux
    :members:
    :special-members:
    :show-inheritance:

    .. autoclasstoc::

BodyConcentrationFluxState
**************************

.. autoclass:: abaqus.Load.BodyConcentrationFluxState.BodyConcentrationFluxState
    :members:
    :special-members:
    :show-inheritance:

    .. autoclasstoc::

BodyCurrent
***********

.. autoclass:: abaqus.Load.BodyCurrent.BodyCurrent
    :members:
    :special-members:
    :show-inheritance:

    .. autoclasstoc::

BodyCurrentDensity
******************

.. autoclass:: abaqus.Load.BodyCurrentDensity.BodyCurrentDensity
    :members:
    :special-members:
    :show-inheritance:

    .. autoclasstoc::

BodyCurrentState
****************

.. autoclass:: abaqus.Load.BodyCurrentState.BodyCurrentState
    :members:
    :special-members:
    :show-inheritance:

    .. autoclasstoc::

BodyForce
*********

.. autoclass:: abaqus.Load.BodyForce.BodyForce
    :members:
    :special-members:
    :show-inheritance:

    .. autoclasstoc::

BodyForceState
**************

.. autoclass:: abaqus.Load.BodyForceState.BodyForceState
    :members:
    :special-members:
    :show-inheritance:

    .. autoclasstoc::

BodyHeatFlux
************

.. autoclass:: abaqus.Load.BodyHeatFlux.BodyHeatFlux
    :members:
    :special-members:
    :show-inheritance:

    .. autoclasstoc::

BodyHeatFluxState
*****************

.. autoclass:: abaqus.Load.BodyHeatFluxState.BodyHeatFluxState
    :members:
    :special-members:
    :show-inheritance:

    .. autoclasstoc::

BoltLoad
********

.. autoclass:: abaqus.Load.BoltLoad.BoltLoad
    :members:
    :special-members:
    :show-inheritance:

    .. autoclasstoc::

BoltLoadState
*************

.. autoclass:: abaqus.Load.BoltLoadState.BoltLoadState
    :members:
    :special-members:
    :show-inheritance:

    .. autoclasstoc::

ConcCharge
**********

.. autoclass:: abaqus.Load.ConcCharge.ConcCharge
    :members:
    :special-members:
    :show-inheritance:

    .. autoclasstoc::

ConcConcFlux
************

.. autoclass:: abaqus.Load.ConcConcFlux.ConcConcFlux
    :members:
    :special-members:
    :show-inheritance:

    .. autoclasstoc::

ConcCurrent
***********

.. autoclass:: abaqus.Load.ConcCurrent.ConcCurrent
    :members:
    :special-members:
    :show-inheritance:

    .. autoclasstoc::

ConcCurrentState
****************

.. autoclass:: abaqus.Load.ConcCurrentState.ConcCurrentState
    :members:
    :special-members:
    :show-inheritance:

    .. autoclasstoc::

ConcentratedChargeState
***********************

.. autoclass:: abaqus.Load.ConcentratedChargeState.ConcentratedChargeState
    :members:
    :special-members:
    :show-inheritance:

    .. autoclasstoc::

ConcentratedConcentrationFluxState
**********************************

.. autoclass:: abaqus.Load.ConcentratedConcentrationFluxState.ConcentratedConcentrationFluxState
    :members:
    :special-members:
    :show-inheritance:

    .. autoclasstoc::

ConcentratedForce
*****************

.. autoclass:: abaqus.Load.ConcentratedForce.ConcentratedForce
    :members:
    :special-members:
    :show-inheritance:

    .. autoclasstoc::

ConcentratedForceState
**********************

.. autoclass:: abaqus.Load.ConcentratedForceState.ConcentratedForceState
    :members:
    :special-members:
    :show-inheritance:

    .. autoclasstoc::

ConcentratedHeatFlux
********************

.. autoclass:: abaqus.Load.ConcentratedHeatFlux.ConcentratedHeatFlux
    :members:
    :special-members:
    :show-inheritance:

    .. autoclasstoc::

ConcentratedHeatFluxState
*************************

.. autoclass:: abaqus.Load.ConcentratedHeatFluxState.ConcentratedHeatFluxState
    :members:
    :special-members:
    :show-inheritance:

    .. autoclasstoc::

ConcentratedPoreFluidState
**************************

.. autoclass:: abaqus.Load.ConcentratedPoreFluidState.ConcentratedPoreFluidState
    :members:
    :special-members:
    :show-inheritance:

    .. autoclasstoc::

ConcPoreFluid
*************

.. autoclass:: abaqus.Load.ConcPoreFluid.ConcPoreFluid
    :members:
    :special-members:
    :show-inheritance:

    .. autoclasstoc::

ConnectorForce
**************

.. autoclass:: abaqus.Load.ConnectorForce.ConnectorForce
    :members:
    :special-members:
    :show-inheritance:

    .. autoclasstoc::

ConnectorForceState
*******************

.. autoclass:: abaqus.Load.ConnectorForceState.ConnectorForceState
    :members:
    :special-members:
    :show-inheritance:

    .. autoclasstoc::

ConnectorMoment
***************

.. autoclass:: abaqus.Load.ConnectorMoment.ConnectorMoment
    :members:
    :special-members:
    :show-inheritance:

    .. autoclasstoc::

ConnectorMomentState
********************

.. autoclass:: abaqus.Load.ConnectorMomentState.ConnectorMomentState
    :members:
    :special-members:
    :show-inheritance:

    .. autoclasstoc::

CoriolisForce
*************

.. autoclass:: abaqus.Load.CoriolisForce.CoriolisForce
    :members:
    :special-members:
    :show-inheritance:

    .. autoclasstoc::

CoriolisForceState
******************

.. autoclass:: abaqus.Load.CoriolisForceState.CoriolisForceState
    :members:
    :special-members:
    :show-inheritance:

    .. autoclasstoc::

Gravity
*******

.. autoclass:: abaqus.Load.Gravity.Gravity
    :members:
    :special-members:
    :show-inheritance:

    .. autoclasstoc::

GravityState
************

.. autoclass:: abaqus.Load.GravityState.GravityState
    :members:
    :special-members:
    :show-inheritance:

    .. autoclasstoc::

HydrostaticFluidFlowState
*************************

.. autoclass:: abaqus.Load.HydrostaticFluidFlowState.HydrostaticFluidFlowState
    :members:
    :special-members:
    :show-inheritance:

    .. autoclasstoc::

InertiaRelief
*************

.. autoclass:: abaqus.Load.InertiaRelief.InertiaRelief
    :members:
    :special-members:
    :show-inheritance:

    .. autoclasstoc::

InertiaReliefState
******************

.. autoclass:: abaqus.Load.InertiaReliefState.InertiaReliefState
    :members:
    :special-members:
    :show-inheritance:

    .. autoclasstoc::

InwardVolAccel
**************

.. autoclass:: abaqus.Load.InwardVolAccel.InwardVolAccel
    :members:
    :special-members:
    :show-inheritance:

    .. autoclasstoc::

InwardVolAccelState
*******************

.. autoclass:: abaqus.Load.InwardVolAccelState.InwardVolAccelState
    :members:
    :special-members:
    :show-inheritance:

    .. autoclasstoc::

LineLoad
********

.. autoclass:: abaqus.Load.LineLoad.LineLoad
    :members:
    :special-members:
    :show-inheritance:

    .. autoclasstoc::

LineLoadState
*************

.. autoclass:: abaqus.Load.LineLoadState.LineLoadState
    :members:
    :special-members:
    :show-inheritance:

    .. autoclasstoc::

Moment
******

.. autoclass:: abaqus.Load.Moment.Moment
    :members:
    :special-members:
    :show-inheritance:

    .. autoclasstoc::

MomentState
***********

.. autoclass:: abaqus.Load.MomentState.MomentState
    :members:
    :special-members:
    :show-inheritance:

    .. autoclasstoc::

PEGLoad
*******

.. autoclass:: abaqus.Load.PEGLoad.PEGLoad
    :members:
    :special-members:
    :show-inheritance:

    .. autoclasstoc::

PEGLoadState
************

.. autoclass:: abaqus.Load.PEGLoadState.PEGLoadState
    :members:
    :special-members:
    :show-inheritance:

    .. autoclasstoc::

PipePressure
************

.. autoclass:: abaqus.Load.PipePressure.PipePressure
    :members:
    :special-members:
    :show-inheritance:

    .. autoclasstoc::

PipePressureState
*****************

.. autoclass:: abaqus.Load.PipePressureState.PipePressureState
    :members:
    :special-members:
    :show-inheritance:

    .. autoclasstoc::

Pressure
********

.. autoclass:: abaqus.Load.Pressure.Pressure
    :members:
    :special-members:
    :show-inheritance:

    .. autoclasstoc::

PressureState
*************

.. autoclass:: abaqus.Load.PressureState.PressureState
    :members:
    :special-members:
    :show-inheritance:

    .. autoclasstoc::

RotationalBodyForce
*******************

.. autoclass:: abaqus.Load.RotationalBodyForce.RotationalBodyForce
    :members:
    :special-members:
    :show-inheritance:

    .. autoclasstoc::

RotationalBodyForceState
************************

.. autoclass:: abaqus.Load.RotationalBodyForceState.RotationalBodyForceState
    :members:
    :special-members:
    :show-inheritance:

    .. autoclasstoc::

ShellEdgeLoad
*************

.. autoclass:: abaqus.Load.ShellEdgeLoad.ShellEdgeLoad
    :members:
    :special-members:
    :show-inheritance:

    .. autoclasstoc::

ShellEdgeLoadState
******************

.. autoclass:: abaqus.Load.ShellEdgeLoadState.ShellEdgeLoadState
    :members:
    :special-members:
    :show-inheritance:

    .. autoclasstoc::

SubmodelSB
**********

.. autoclass:: abaqus.Load.SubmodelSB.SubmodelSB
    :members:
    :special-members:
    :show-inheritance:

    .. autoclasstoc::

SubmodelSBState
***************

.. autoclass:: abaqus.Load.SubmodelSBState.SubmodelSBState
    :members:
    :special-members:
    :show-inheritance:

    .. autoclasstoc::

SubstructureLoad
****************

.. autoclass:: abaqus.Load.SubstructureLoad.SubstructureLoad
    :members:
    :special-members:
    :show-inheritance:

    .. autoclasstoc::

SubstructureLoadState
*********************

.. autoclass:: abaqus.Load.SubstructureLoadState.SubstructureLoadState
    :members:
    :special-members:
    :show-inheritance:

    .. autoclasstoc::

SurfaceCharge
*************

.. autoclass:: abaqus.Load.SurfaceCharge.SurfaceCharge
    :members:
    :special-members:
    :show-inheritance:

    .. autoclasstoc::

SurfaceChargeState
******************

.. autoclass:: abaqus.Load.SurfaceChargeState.SurfaceChargeState
    :members:
    :special-members:
    :show-inheritance:

    .. autoclasstoc::

SurfaceConcentrationFlux
************************

.. autoclass:: abaqus.Load.SurfaceConcentrationFlux.SurfaceConcentrationFlux
    :members:
    :special-members:
    :show-inheritance:

    .. autoclasstoc::

SurfaceConcentrationFluxState
*****************************

.. autoclass:: abaqus.Load.SurfaceConcentrationFluxState.SurfaceConcentrationFluxState
    :members:
    :special-members:
    :show-inheritance:

    .. autoclasstoc::

SurfaceCurrent
**************

.. autoclass:: abaqus.Load.SurfaceCurrent.SurfaceCurrent
    :members:
    :special-members:
    :show-inheritance:

    .. autoclasstoc::

SurfaceCurrentDensity
*********************

.. autoclass:: abaqus.Load.SurfaceCurrentDensity.SurfaceCurrentDensity
    :members:
    :special-members:
    :show-inheritance:

    .. autoclasstoc::

SurfaceCurrentState
*******************

.. autoclass:: abaqus.Load.SurfaceCurrentState.SurfaceCurrentState
    :members:
    :special-members:
    :show-inheritance:

    .. autoclasstoc::

SurfaceHeatFlux
***************

.. autoclass:: abaqus.Load.SurfaceHeatFlux.SurfaceHeatFlux
    :members:
    :special-members:
    :show-inheritance:

    .. autoclasstoc::

SurfaceHeatFluxState
********************

.. autoclass:: abaqus.Load.SurfaceHeatFluxState.SurfaceHeatFluxState
    :members:
    :special-members:
    :show-inheritance:

    .. autoclasstoc::

SurfacePoreFluid
****************

.. autoclass:: abaqus.Load.SurfacePoreFluid.SurfacePoreFluid
    :members:
    :special-members:
    :show-inheritance:

    .. autoclasstoc::

SurfacePoreFluidState
*********************

.. autoclass:: abaqus.Load.SurfacePoreFluidState.SurfacePoreFluidState
    :members:
    :special-members:
    :show-inheritance:

    .. autoclasstoc::

SurfaceTraction
***************

.. autoclass:: abaqus.Load.SurfaceTraction.SurfaceTraction
    :members:
    :special-members:
    :show-inheritance:

    .. autoclasstoc::

SurfaceTractionState
********************

.. autoclass:: abaqus.Load.SurfaceTractionState.SurfaceTractionState
    :members:
    :special-members:
    :show-inheritance:

    .. autoclasstoc::


Load case
---------

The LoadCase object is used to define the loads and constraints comprising a particular loading condition and the linear response of a structure subjected to that loading condition.


Create load cases
~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Load.LoadStep.LoadStep
    :members:
    :special-members:
    :show-inheritance:

    .. autoclasstoc::


Object features of load cases
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Load.LoadCase.LoadCase
    :members:
    :special-members:
    :show-inheritance:

    .. autoclasstoc::