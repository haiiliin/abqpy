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

    .. autoclassdoc::

BoundaryConditionState
~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.BoundaryConditionState.BoundaryConditionState
    :members:

    .. autoclassdoc::

AccelerationBaseMotionBC
~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.AccelerationBaseMotionBC.AccelerationBaseMotionBC
    :members:

    .. autoclassdoc::

AccelerationBaseMotionBCState
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.AccelerationBaseMotionBCState.AccelerationBaseMotionBCState
    :members:

    .. autoclassdoc::

AccelerationBC
~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.AccelerationBC.AccelerationBC
    :members:

    .. autoclassdoc::

AccelerationBCState
~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.AccelerationBCState.AccelerationBCState
    :members:

    .. autoclassdoc::

AcousticPressureBC
~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.AcousticPressureBC.AcousticPressureBC
    :members:

    .. autoclassdoc::

AcousticPressureBCState
~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.AcousticPressureBCState.AcousticPressureBCState
    :members:

    .. autoclassdoc::

Calibration
~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.Calibration.Calibration
    :members:

    .. autoclassdoc::

ConcentrationBC
~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.ConcentrationBC.ConcentrationBC
    :members:

    .. autoclassdoc::

ConcentrationBCState
~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.ConcentrationBCState.ConcentrationBCState
    :members:

    .. autoclassdoc::

ConnAccelerationBC
~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.ConnAccelerationBC.ConnAccelerationBC
    :members:

    .. autoclassdoc::

ConnAccelerationBCState
~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.ConnAccelerationBCState.ConnAccelerationBCState
    :members:

    .. autoclassdoc::

ConnDisplacementBC
~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.ConnDisplacementBC.ConnDisplacementBC
    :members:

    .. autoclassdoc::

ConnDisplacementBCState
~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.ConnDisplacementBCState.ConnDisplacementBCState
    :members:

    .. autoclassdoc::

ConnVelocityBC
~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.ConnVelocityBC.ConnVelocityBC
    :members:

    .. autoclassdoc::

ConnVelocityBCState
~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.ConnVelocityBCState.ConnVelocityBCState
    :members:

    .. autoclassdoc::

DisplacementBaseMotionBC
~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.DisplacementBaseMotionBC.DisplacementBaseMotionBC
    :members:

    .. autoclassdoc::

DisplacementBaseMotionBCState
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.DisplacementBaseMotionBCState.DisplacementBaseMotionBCState
    :members:

    .. autoclassdoc::

DisplacementBC
~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.DisplacementBC.DisplacementBC
    :members:

    .. autoclassdoc::

DisplacementBCState
~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.DisplacementBCState.DisplacementBCState
    :members:

    .. autoclassdoc::

ElectricPotentialBC
~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.ElectricPotentialBC.ElectricPotentialBC
    :members:

    .. autoclassdoc::

ElectricPotentialBCState
~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.ElectricPotentialBCState.ElectricPotentialBCState
    :members:

    .. autoclassdoc::

EulerianBC
~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.EulerianBC.EulerianBC
    :members:

    .. autoclassdoc::

EulerianBCState
~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.EulerianBCState.EulerianBCState
    :members:

    .. autoclassdoc::

EulerianMotionBC
~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC
    :members:

    .. autoclassdoc::

EulerianMotionBCState
~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.EulerianMotionBCState.EulerianMotionBCState
    :members:

    .. autoclassdoc::

FluidCavityPressureBC
~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.FluidCavityPressureBC.FluidCavityPressureBC
    :members:

    .. autoclassdoc::

FluidCavityPressureBCState
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.FluidCavityPressureBCState.FluidCavityPressureBCState
    :members:

    .. autoclassdoc::

MagneticVectorPotentialBC
~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.MagneticVectorPotentialBC.MagneticVectorPotentialBC
    :members:

    .. autoclassdoc::

MaterialFlowBC
~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.MaterialFlowBC.MaterialFlowBC
    :members:

    .. autoclassdoc::

MaterialFlowBCState
~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.MaterialFlowBCState.MaterialFlowBCState
    :members:

    .. autoclassdoc::

PorePressureBC
~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.PorePressureBC.PorePressureBC
    :members:

    .. autoclassdoc::

PorePressureBCState
~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.PorePressureBCState.PorePressureBCState
    :members:

    .. autoclassdoc::

RetainedNodalDofsBC
~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.RetainedNodalDofsBC.RetainedNodalDofsBC
    :members:

    .. autoclassdoc::

SecondaryBaseBC
~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.SecondaryBaseBC.SecondaryBaseBC
    :members:

    .. autoclassdoc::

SecondaryBaseBCState
~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.SecondaryBaseBCState.SecondaryBaseBCState
    :members:

    .. autoclassdoc::

SubmodelBC
~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.SubmodelBC.SubmodelBC
    :members:

    .. autoclassdoc::

SubmodelBCState
~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.SubmodelBCState.SubmodelBCState
    :members:

    .. autoclassdoc::

TemperatureBC
~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.TemperatureBC.TemperatureBC
    :members:

    .. autoclassdoc::

TemperatureBCState
~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.TemperatureBCState.TemperatureBCState
    :members:

    .. autoclassdoc::

TypeBC
~~~~~~

.. autoclass:: abaqus.BoundaryCondition.TypeBC.TypeBC
    :members:

    .. autoclassdoc::

TypeBCState
~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.TypeBCState.TypeBCState
    :members:

    .. autoclassdoc::

VelocityBaseMotionBC
~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.VelocityBaseMotionBC.VelocityBaseMotionBC
    :members:

    .. autoclassdoc::

VelocityBaseMotionBCState
~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.VelocityBaseMotionBCState.VelocityBaseMotionBCState
    :members:

    .. autoclassdoc::

VelocityBC
~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.VelocityBC.VelocityBC
    :members:

    .. autoclassdoc::

VelocityBCState
~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.VelocityBCState.VelocityBCState
    :members:

    .. autoclassdoc::
