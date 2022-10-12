==================
Boundary Condition
==================

A specific type of boundary condition object and a specific type of boundary condition state object are designed for each type of boundary condition. A BoundaryCondition object stores the non-propagating data of a boundary condition as well as a number of instances of the corresponding BoundaryConditionState object, each of which stores the propagating data of the boundary condition in a single step. Instances of the BoundaryConditionState object are created and deleted internally by its corresponding BoundaryCondition object.


Create boundary conditions
--------------------------

.. autoclass:: abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::


Classes
-------

BoundaryCondition
~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.BoundaryCondition.BoundaryCondition
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::

BoundaryConditionState
~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.BoundaryConditionState.BoundaryConditionState
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::

AccelerationBaseMotionBC
~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.AccelerationBaseMotionBC.AccelerationBaseMotionBC
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::

AccelerationBaseMotionBCState
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.AccelerationBaseMotionBCState.AccelerationBaseMotionBCState
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::

AccelerationBC
~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.AccelerationBC.AccelerationBC
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::

AccelerationBCState
~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.AccelerationBCState.AccelerationBCState
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::

AcousticPressureBC
~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.AcousticPressureBC.AcousticPressureBC
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::

AcousticPressureBCState
~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.AcousticPressureBCState.AcousticPressureBCState
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::

ConcentrationBC
~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.ConcentrationBC.ConcentrationBC
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::

ConcentrationBCState
~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.ConcentrationBCState.ConcentrationBCState
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::

ConnAccelerationBC
~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.ConnAccelerationBC.ConnAccelerationBC
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::

ConnAccelerationBCState
~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.ConnAccelerationBCState.ConnAccelerationBCState
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::

ConnDisplacementBC
~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.ConnDisplacementBC.ConnDisplacementBC
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::

ConnDisplacementBCState
~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.ConnDisplacementBCState.ConnDisplacementBCState
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::

ConnVelocityBC
~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.ConnVelocityBC.ConnVelocityBC
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::

ConnVelocityBCState
~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.ConnVelocityBCState.ConnVelocityBCState
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::

DisplacementBaseMotionBC
~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.DisplacementBaseMotionBC.DisplacementBaseMotionBC
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::

DisplacementBaseMotionBCState
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.DisplacementBaseMotionBCState.DisplacementBaseMotionBCState
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::

DisplacementBC
~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.DisplacementBC.DisplacementBC
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::

DisplacementBCState
~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.DisplacementBCState.DisplacementBCState
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::

ElectricPotentialBC
~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.ElectricPotentialBC.ElectricPotentialBC
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::

ElectricPotentialBCState
~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.ElectricPotentialBCState.ElectricPotentialBCState
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::

EulerianBC
~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.EulerianBC.EulerianBC
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::

EulerianBCState
~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.EulerianBCState.EulerianBCState
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::

EulerianMotionBC
~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::

EulerianMotionBCState
~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.EulerianMotionBCState.EulerianMotionBCState
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::

FluidCavityPressureBC
~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.FluidCavityPressureBC.FluidCavityPressureBC
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::

FluidCavityPressureBCState
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.FluidCavityPressureBCState.FluidCavityPressureBCState
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::

MagneticVectorPotentialBC
~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.MagneticVectorPotentialBC.MagneticVectorPotentialBC
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::

MaterialFlowBC
~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.MaterialFlowBC.MaterialFlowBC
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::

MaterialFlowBCState
~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.MaterialFlowBCState.MaterialFlowBCState
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::

PorePressureBC
~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.PorePressureBC.PorePressureBC
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::

PorePressureBCState
~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.PorePressureBCState.PorePressureBCState
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::

RetainedNodalDofsBC
~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.RetainedNodalDofsBC.RetainedNodalDofsBC
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::

SecondaryBaseBC
~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.SecondaryBaseBC.SecondaryBaseBC
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::

SecondaryBaseBCState
~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.SecondaryBaseBCState.SecondaryBaseBCState
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::

SubmodelBC
~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.SubmodelBC.SubmodelBC
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::

SubmodelBCState
~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.SubmodelBCState.SubmodelBCState
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::

TemperatureBC
~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.TemperatureBC.TemperatureBC
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::

TemperatureBCState
~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.TemperatureBCState.TemperatureBCState
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::

TypeBC
~~~~~~

.. autoclass:: abaqus.BoundaryCondition.TypeBC.TypeBC
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::

TypeBCState
~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.TypeBCState.TypeBCState
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::

VelocityBaseMotionBC
~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.VelocityBaseMotionBC.VelocityBaseMotionBC
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::

VelocityBaseMotionBCState
~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.VelocityBaseMotionBCState.VelocityBaseMotionBCState
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::

VelocityBC
~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.VelocityBC.VelocityBC
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::

VelocityBCState
~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.VelocityBCState.VelocityBCState
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
