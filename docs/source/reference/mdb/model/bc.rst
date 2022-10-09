==================
Boundary Condition
==================

A specific type of boundary condition object and a specific type of boundary condition state object are designed for each type of boundary condition. A BoundaryCondition object stores the non-propagating data of a boundary condition as well as a number of instances of the corresponding BoundaryConditionState object, each of which stores the propagating data of the boundary condition in a single step. Instances of the BoundaryConditionState object are created and deleted internally by its corresponding BoundaryCondition object.


Create boundary conditions
--------------------------

.. autoclass:: abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel
    :members:

    .. autoclasstoc::


Classes
-------

BoundaryCondition
~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.BoundaryCondition.BoundaryCondition
    :members:

    .. autoclasstoc::

BoundaryConditionState
~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.BoundaryConditionState.BoundaryConditionState
    :members:

    .. autoclasstoc::

AccelerationBaseMotionBC
~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.AccelerationBaseMotionBC.AccelerationBaseMotionBC
    :members:

    .. autoclasstoc::

AccelerationBaseMotionBCState
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.AccelerationBaseMotionBCState.AccelerationBaseMotionBCState
    :members:

    .. autoclasstoc::

AccelerationBC
~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.AccelerationBC.AccelerationBC
    :members:

    .. autoclasstoc::

AccelerationBCState
~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.AccelerationBCState.AccelerationBCState
    :members:

    .. autoclasstoc::

AcousticPressureBC
~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.AcousticPressureBC.AcousticPressureBC
    :members:

    .. autoclasstoc::

AcousticPressureBCState
~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.AcousticPressureBCState.AcousticPressureBCState
    :members:

    .. autoclasstoc::

ConcentrationBC
~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.ConcentrationBC.ConcentrationBC
    :members:

    .. autoclasstoc::

ConcentrationBCState
~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.ConcentrationBCState.ConcentrationBCState
    :members:

    .. autoclasstoc::

ConnAccelerationBC
~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.ConnAccelerationBC.ConnAccelerationBC
    :members:

    .. autoclasstoc::

ConnAccelerationBCState
~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.ConnAccelerationBCState.ConnAccelerationBCState
    :members:

    .. autoclasstoc::

ConnDisplacementBC
~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.ConnDisplacementBC.ConnDisplacementBC
    :members:

    .. autoclasstoc::

ConnDisplacementBCState
~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.ConnDisplacementBCState.ConnDisplacementBCState
    :members:

    .. autoclasstoc::

ConnVelocityBC
~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.ConnVelocityBC.ConnVelocityBC
    :members:

    .. autoclasstoc::

ConnVelocityBCState
~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.ConnVelocityBCState.ConnVelocityBCState
    :members:

    .. autoclasstoc::

DisplacementBaseMotionBC
~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.DisplacementBaseMotionBC.DisplacementBaseMotionBC
    :members:

    .. autoclasstoc::

DisplacementBaseMotionBCState
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.DisplacementBaseMotionBCState.DisplacementBaseMotionBCState
    :members:

    .. autoclasstoc::

DisplacementBC
~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.DisplacementBC.DisplacementBC
    :members:

    .. autoclasstoc::

DisplacementBCState
~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.DisplacementBCState.DisplacementBCState
    :members:

    .. autoclasstoc::

ElectricPotentialBC
~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.ElectricPotentialBC.ElectricPotentialBC
    :members:

    .. autoclasstoc::

ElectricPotentialBCState
~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.ElectricPotentialBCState.ElectricPotentialBCState
    :members:

    .. autoclasstoc::

EulerianBC
~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.EulerianBC.EulerianBC
    :members:

    .. autoclasstoc::

EulerianBCState
~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.EulerianBCState.EulerianBCState
    :members:

    .. autoclasstoc::

EulerianMotionBC
~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC
    :members:

    .. autoclasstoc::

EulerianMotionBCState
~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.EulerianMotionBCState.EulerianMotionBCState
    :members:

    .. autoclasstoc::

FluidCavityPressureBC
~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.FluidCavityPressureBC.FluidCavityPressureBC
    :members:

    .. autoclasstoc::

FluidCavityPressureBCState
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.FluidCavityPressureBCState.FluidCavityPressureBCState
    :members:

    .. autoclasstoc::

MagneticVectorPotentialBC
~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.MagneticVectorPotentialBC.MagneticVectorPotentialBC
    :members:

    .. autoclasstoc::

MaterialFlowBC
~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.MaterialFlowBC.MaterialFlowBC
    :members:

    .. autoclasstoc::

MaterialFlowBCState
~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.MaterialFlowBCState.MaterialFlowBCState
    :members:

    .. autoclasstoc::

PorePressureBC
~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.PorePressureBC.PorePressureBC
    :members:

    .. autoclasstoc::

PorePressureBCState
~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.PorePressureBCState.PorePressureBCState
    :members:

    .. autoclasstoc::

RetainedNodalDofsBC
~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.RetainedNodalDofsBC.RetainedNodalDofsBC
    :members:

    .. autoclasstoc::

SecondaryBaseBC
~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.SecondaryBaseBC.SecondaryBaseBC
    :members:

    .. autoclasstoc::

SecondaryBaseBCState
~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.SecondaryBaseBCState.SecondaryBaseBCState
    :members:

    .. autoclasstoc::

SubmodelBC
~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.SubmodelBC.SubmodelBC
    :members:

    .. autoclasstoc::

SubmodelBCState
~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.SubmodelBCState.SubmodelBCState
    :members:

    .. autoclasstoc::

TemperatureBC
~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.TemperatureBC.TemperatureBC
    :members:

    .. autoclasstoc::

TemperatureBCState
~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.TemperatureBCState.TemperatureBCState
    :members:

    .. autoclasstoc::

TypeBC
~~~~~~

.. autoclass:: abaqus.BoundaryCondition.TypeBC.TypeBC
    :members:

    .. autoclasstoc::

TypeBCState
~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.TypeBCState.TypeBCState
    :members:

    .. autoclasstoc::

VelocityBaseMotionBC
~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.VelocityBaseMotionBC.VelocityBaseMotionBC
    :members:

    .. autoclasstoc::

VelocityBaseMotionBCState
~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.VelocityBaseMotionBCState.VelocityBaseMotionBCState
    :members:

    .. autoclasstoc::

VelocityBC
~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.VelocityBC.VelocityBC
    :members:

    .. autoclasstoc::

VelocityBCState
~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.VelocityBCState.VelocityBCState
    :members:

    .. autoclasstoc::
