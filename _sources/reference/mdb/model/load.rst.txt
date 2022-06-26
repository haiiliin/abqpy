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

    .. autoclassdoc::

LoadState
*********

.. autoclass:: abaqus.Load.LoadState.LoadState
    :members:

    .. autoclassdoc::

BodyCharge
**********

.. autoclass:: abaqus.Load.BodyCharge.BodyCharge
    :members:

    .. autoclassdoc::

BodyChargeState
***************

.. autoclass:: abaqus.Load.BodyChargeState.BodyChargeState
    :members:

    .. autoclassdoc::

BodyConcentrationFlux
*********************

.. autoclass:: abaqus.Load.BodyConcentrationFlux.BodyConcentrationFlux
    :members:

    .. autoclassdoc::

BodyConcentrationFluxState
**************************

.. autoclass:: abaqus.Load.BodyConcentrationFluxState.BodyConcentrationFluxState
    :members:

    .. autoclassdoc::

BodyCurrent
***********

.. autoclass:: abaqus.Load.BodyCurrent.BodyCurrent
    :members:

    .. autoclassdoc::

BodyCurrentDensity
******************

.. autoclass:: abaqus.Load.BodyCurrentDensity.BodyCurrentDensity
    :members:

    .. autoclassdoc::

BodyCurrentState
****************

.. autoclass:: abaqus.Load.BodyCurrentState.BodyCurrentState
    :members:

    .. autoclassdoc::

BodyForce
*********

.. autoclass:: abaqus.Load.BodyForce.BodyForce
    :members:

    .. autoclassdoc::

BodyForceState
**************

.. autoclass:: abaqus.Load.BodyForceState.BodyForceState
    :members:

    .. autoclassdoc::

BodyHeatFlux
************

.. autoclass:: abaqus.Load.BodyHeatFlux.BodyHeatFlux
    :members:

    .. autoclassdoc::

BodyHeatFluxState
*****************

.. autoclass:: abaqus.Load.BodyHeatFluxState.BodyHeatFluxState
    :members:

    .. autoclassdoc::

BoltLoad
********

.. autoclass:: abaqus.Load.BoltLoad.BoltLoad
    :members:

    .. autoclassdoc::

BoltLoadState
*************

.. autoclass:: abaqus.Load.BoltLoadState.BoltLoadState
    :members:

    .. autoclassdoc::

ConcCharge
**********

.. autoclass:: abaqus.Load.ConcCharge.ConcCharge
    :members:

    .. autoclassdoc::

ConcConcFlux
************

.. autoclass:: abaqus.Load.ConcConcFlux.ConcConcFlux
    :members:

    .. autoclassdoc::

ConcCurrent
***********

.. autoclass:: abaqus.Load.ConcCurrent.ConcCurrent
    :members:

    .. autoclassdoc::

ConcCurrentState
****************

.. autoclass:: abaqus.Load.ConcCurrentState.ConcCurrentState
    :members:

    .. autoclassdoc::

ConcentratedChargeState
***********************

.. autoclass:: abaqus.Load.ConcentratedChargeState.ConcentratedChargeState
    :members:

    .. autoclassdoc::

ConcentratedConcentrationFluxState
**********************************

.. autoclass:: abaqus.Load.ConcentratedConcentrationFluxState.ConcentratedConcentrationFluxState
    :members:

    .. autoclassdoc::

ConcentratedForce
*****************

.. autoclass:: abaqus.Load.ConcentratedForce.ConcentratedForce
    :members:

    .. autoclassdoc::

ConcentratedForceState
**********************

.. autoclass:: abaqus.Load.ConcentratedForceState.ConcentratedForceState
    :members:

    .. autoclassdoc::

ConcentratedHeatFlux
********************

.. autoclass:: abaqus.Load.ConcentratedHeatFlux.ConcentratedHeatFlux
    :members:

    .. autoclassdoc::

ConcentratedHeatFluxState
*************************

.. autoclass:: abaqus.Load.ConcentratedHeatFluxState.ConcentratedHeatFluxState
    :members:

    .. autoclassdoc::

ConcentratedPoreFluidState
**************************

.. autoclass:: abaqus.Load.ConcentratedPoreFluidState.ConcentratedPoreFluidState
    :members:

    .. autoclassdoc::

ConcPoreFluid
*************

.. autoclass:: abaqus.Load.ConcPoreFluid.ConcPoreFluid
    :members:

    .. autoclassdoc::

ConnectorForce
**************

.. autoclass:: abaqus.Load.ConnectorForce.ConnectorForce
    :members:

    .. autoclassdoc::

ConnectorForceState
*******************

.. autoclass:: abaqus.Load.ConnectorForceState.ConnectorForceState
    :members:

    .. autoclassdoc::

ConnectorMoment
***************

.. autoclass:: abaqus.Load.ConnectorMoment.ConnectorMoment
    :members:

    .. autoclassdoc::

ConnectorMomentState
********************

.. autoclass:: abaqus.Load.ConnectorMomentState.ConnectorMomentState
    :members:

    .. autoclassdoc::

CoriolisForce
*************

.. autoclass:: abaqus.Load.CoriolisForce.CoriolisForce
    :members:

    .. autoclassdoc::

CoriolisForceState
******************

.. autoclass:: abaqus.Load.CoriolisForceState.CoriolisForceState
    :members:

    .. autoclassdoc::

Gravity
*******

.. autoclass:: abaqus.Load.Gravity.Gravity
    :members:

    .. autoclassdoc::

GravityState
************

.. autoclass:: abaqus.Load.GravityState.GravityState
    :members:

    .. autoclassdoc::

HydrostaticFluidFlowState
*************************

.. autoclass:: abaqus.Load.HydrostaticFluidFlowState.HydrostaticFluidFlowState
    :members:

    .. autoclassdoc::

InertiaRelief
*************

.. autoclass:: abaqus.Load.InertiaRelief.InertiaRelief
    :members:

    .. autoclassdoc::

InertiaReliefState
******************

.. autoclass:: abaqus.Load.InertiaReliefState.InertiaReliefState
    :members:

    .. autoclassdoc::

InwardVolAccel
**************

.. autoclass:: abaqus.Load.InwardVolAccel.InwardVolAccel
    :members:

    .. autoclassdoc::

InwardVolAccelState
*******************

.. autoclass:: abaqus.Load.InwardVolAccelState.InwardVolAccelState
    :members:

    .. autoclassdoc::

LineLoad
********

.. autoclass:: abaqus.Load.LineLoad.LineLoad
    :members:

    .. autoclassdoc::

LineLoadState
*************

.. autoclass:: abaqus.Load.LineLoadState.LineLoadState
    :members:

    .. autoclassdoc::

LoadStep
********

.. autoclass:: abaqus.Load.LoadStep.LoadStep
    :members:

    .. autoclassdoc::

Moment
******

.. autoclass:: abaqus.Load.Moment.Moment
    :members:

    .. autoclassdoc::

MomentState
***********

.. autoclass:: abaqus.Load.MomentState.MomentState
    :members:

    .. autoclassdoc::

PEGLoad
*******

.. autoclass:: abaqus.Load.PEGLoad.PEGLoad
    :members:

    .. autoclassdoc::

PEGLoadState
************

.. autoclass:: abaqus.Load.PEGLoadState.PEGLoadState
    :members:

    .. autoclassdoc::

PipePressure
************

.. autoclass:: abaqus.Load.PipePressure.PipePressure
    :members:

    .. autoclassdoc::

PipePressureState
*****************

.. autoclass:: abaqus.Load.PipePressureState.PipePressureState
    :members:

    .. autoclassdoc::

Pressure
********

.. autoclass:: abaqus.Load.Pressure.Pressure
    :members:

    .. autoclassdoc::

PressureState
*************

.. autoclass:: abaqus.Load.PressureState.PressureState
    :members:

    .. autoclassdoc::

RotationalBodyForce
*******************

.. autoclass:: abaqus.Load.RotationalBodyForce.RotationalBodyForce
    :members:

    .. autoclassdoc::

RotationalBodyForceState
************************

.. autoclass:: abaqus.Load.RotationalBodyForceState.RotationalBodyForceState
    :members:

    .. autoclassdoc::

ShellEdgeLoad
*************

.. autoclass:: abaqus.Load.ShellEdgeLoad.ShellEdgeLoad
    :members:

    .. autoclassdoc::

ShellEdgeLoadState
******************

.. autoclass:: abaqus.Load.ShellEdgeLoadState.ShellEdgeLoadState
    :members:

    .. autoclassdoc::

SubmodelSB
**********

.. autoclass:: abaqus.Load.SubmodelSB.SubmodelSB
    :members:

    .. autoclassdoc::

SubmodelSBState
***************

.. autoclass:: abaqus.Load.SubmodelSBState.SubmodelSBState
    :members:

    .. autoclassdoc::

SubstructureLoad
****************

.. autoclass:: abaqus.Load.SubstructureLoad.SubstructureLoad
    :members:

    .. autoclassdoc::

SubstructureLoadState
*********************

.. autoclass:: abaqus.Load.SubstructureLoadState.SubstructureLoadState
    :members:

    .. autoclassdoc::

SurfaceCharge
*************

.. autoclass:: abaqus.Load.SurfaceCharge.SurfaceCharge
    :members:

    .. autoclassdoc::

SurfaceChargeState
******************

.. autoclass:: abaqus.Load.SurfaceChargeState.SurfaceChargeState
    :members:

    .. autoclassdoc::

SurfaceConcentrationFlux
************************

.. autoclass:: abaqus.Load.SurfaceConcentrationFlux.SurfaceConcentrationFlux
    :members:

    .. autoclassdoc::

SurfaceConcentrationFluxState
*****************************

.. autoclass:: abaqus.Load.SurfaceConcentrationFluxState.SurfaceConcentrationFluxState
    :members:

    .. autoclassdoc::

SurfaceCurrent
**************

.. autoclass:: abaqus.Load.SurfaceCurrent.SurfaceCurrent
    :members:

    .. autoclassdoc::

SurfaceCurrentDensity
*********************

.. autoclass:: abaqus.Load.SurfaceCurrentDensity.SurfaceCurrentDensity
    :members:

    .. autoclassdoc::

SurfaceCurrentState
*******************

.. autoclass:: abaqus.Load.SurfaceCurrentState.SurfaceCurrentState
    :members:

    .. autoclassdoc::

SurfaceHeatFlux
***************

.. autoclass:: abaqus.Load.SurfaceHeatFlux.SurfaceHeatFlux
    :members:

    .. autoclassdoc::

SurfaceHeatFluxState
********************

.. autoclass:: abaqus.Load.SurfaceHeatFluxState.SurfaceHeatFluxState
    :members:

    .. autoclassdoc::

SurfacePoreFluid
****************

.. autoclass:: abaqus.Load.SurfacePoreFluid.SurfacePoreFluid
    :members:

    .. autoclassdoc::

SurfacePoreFluidState
*********************

.. autoclass:: abaqus.Load.SurfacePoreFluidState.SurfacePoreFluidState
    :members:

    .. autoclassdoc::

SurfaceTraction
***************

.. autoclass:: abaqus.Load.SurfaceTraction.SurfaceTraction
    :members:

    .. autoclassdoc::

SurfaceTractionState
********************

.. autoclass:: abaqus.Load.SurfaceTractionState.SurfaceTractionState
    :members:

    .. autoclassdoc::


Load case
---------

The LoadCase object is used to define the loads and constraints comprising a particular loading condition and the linear response of a structure subjected to that loading condition.


Create load cases
~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Load.LoadStep.LoadStep
    :members:

    .. autoclassdoc::


Object features of load cases
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Load.LoadCase.LoadCase
    :members:

    .. autoclassdoc::