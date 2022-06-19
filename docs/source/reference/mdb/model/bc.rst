==================
Boundary Condition
==================

A specific type of boundary condition object and a specific type of boundary condition state object are designed for each type of boundary condition. A BoundaryCondition object stores the non-propagating data of a boundary condition as well as a number of instances of the corresponding BoundaryConditionState object, each of which stores the propagating data of the boundary condition in a single step. Instances of the BoundaryConditionState object are created and deleted internally by its corresponding BoundaryCondition object.


Create boundary conditions
--------------------------

.. autoclass:: abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel
    :members:


Object features
---------------

BoundaryCondition
~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.BoundaryCondition.BoundaryCondition
    :members:

BoundaryConditionState
~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.BoundaryConditionState.BoundaryConditionState
    :members:

AccelerationBaseMotionBC
~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.AccelerationBaseMotionBC.AccelerationBaseMotionBC
    :members:

AccelerationBaseMotionBCState
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.AccelerationBaseMotionBCState.AccelerationBaseMotionBCState
    :members:

AccelerationBC
~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.AccelerationBC.AccelerationBC
    :members:

AccelerationBCState
~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.AccelerationBCState.AccelerationBCState
    :members:

AcousticPressureBC
~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.AcousticPressureBC.AcousticPressureBC
    :members:

AcousticPressureBCState
~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.AcousticPressureBCState.AcousticPressureBCState
    :members:

Calibration
~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.Calibration.Calibration
    :members:

ConcentrationBC
~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.ConcentrationBC.ConcentrationBC
    :members:

ConcentrationBCState
~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.ConcentrationBCState.ConcentrationBCState
    :members:

ConnAccelerationBC
~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.ConnAccelerationBC.ConnAccelerationBC
    :members:

ConnAccelerationBCState
~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.ConnAccelerationBCState.ConnAccelerationBCState
    :members:

ConnDisplacementBC
~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.ConnDisplacementBC.ConnDisplacementBC
    :members:

ConnDisplacementBCState
~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.ConnDisplacementBCState.ConnDisplacementBCState
    :members:

ConnVelocityBC
~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.ConnVelocityBC.ConnVelocityBC
    :members:

ConnVelocityBCState
~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.ConnVelocityBCState.ConnVelocityBCState
    :members:

DisplacementBaseMotionBC
~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.DisplacementBaseMotionBC.DisplacementBaseMotionBC
    :members:

DisplacementBaseMotionBCState
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.DisplacementBaseMotionBCState.DisplacementBaseMotionBCState
    :members:

DisplacementBC
~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.DisplacementBC.DisplacementBC
    :members:

DisplacementBCState
~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.DisplacementBCState.DisplacementBCState
    :members:

ElectricPotentialBC
~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.ElectricPotentialBC.ElectricPotentialBC
    :members:

ElectricPotentialBCState
~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.ElectricPotentialBCState.ElectricPotentialBCState
    :members:

EulerianBC
~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.EulerianBC.EulerianBC
    :members:

EulerianBCState
~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.EulerianBCState.EulerianBCState
    :members:

EulerianMotionBC
~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC
    :members:

EulerianMotionBCState
~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.EulerianMotionBCState.EulerianMotionBCState
    :members:

FluidCavityPressureBC
~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.FluidCavityPressureBC.FluidCavityPressureBC
    :members:

FluidCavityPressureBCState
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.FluidCavityPressureBCState.FluidCavityPressureBCState
    :members:

MagneticVectorPotentialBC
~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.MagneticVectorPotentialBC.MagneticVectorPotentialBC
    :members:

MaterialFlowBC
~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.MaterialFlowBC.MaterialFlowBC
    :members:

MaterialFlowBCState
~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.MaterialFlowBCState.MaterialFlowBCState
    :members:

PorePressureBC
~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.PorePressureBC.PorePressureBC
    :members:

PorePressureBCState
~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.PorePressureBCState.PorePressureBCState
    :members:

RetainedNodalDofsBC
~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.RetainedNodalDofsBC.RetainedNodalDofsBC
    :members:

SecondaryBaseBC
~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.SecondaryBaseBC.SecondaryBaseBC
    :members:

SecondaryBaseBCState
~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.SecondaryBaseBCState.SecondaryBaseBCState
    :members:

SubmodelBC
~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.SubmodelBC.SubmodelBC
    :members:

SubmodelBCState
~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.SubmodelBCState.SubmodelBCState
    :members:

TemperatureBC
~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.TemperatureBC.TemperatureBC
    :members:

TemperatureBCState
~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.TemperatureBCState.TemperatureBCState
    :members:

TypeBC
~~~~~~

.. autoclass:: abaqus.BoundaryCondition.TypeBC.TypeBC
    :members:

TypeBCState
~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.TypeBCState.TypeBCState
    :members:

VelocityBaseMotionBC
~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.VelocityBaseMotionBC.VelocityBaseMotionBC
    :members:

VelocityBaseMotionBCState
~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.VelocityBaseMotionBCState.VelocityBaseMotionBCState
    :members:

VelocityBC
~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.VelocityBC.VelocityBC
    :members:

VelocityBCState
~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.VelocityBCState.VelocityBCState
    :members:
