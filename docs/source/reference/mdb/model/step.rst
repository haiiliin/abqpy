====
Step
====

The Step commands described in this chapter are used to create and configure analysis steps. Step commands (output) describes the commands used to create and configure output requests and integrated output sections and the commands to configure diagnostic printing, monitoring, and restart. Step commands (miscellaneous) describes the commands used to configure controls, damping, and frequency tables.

.. toctree::
   :maxdepth: 1
   :caption: Objects in Step

   step/step_miscellaneous


Create steps
------------

.. autoclass:: abaqus.Step.StepModel.StepModel
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::

Classes
-------

Step
~~~~

.. autoclass:: abaqus.Step.Step.Step
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::

StepBase
~~~~~~~~

.. autoclass:: abaqus.Step.StepBase.StepBase
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::

AdaptivityStep
~~~~~~~~~~~~~~

.. autoclass:: abaqus.Adaptivity.AdaptivityStep.AdaptivityStep
    :members:
    :special-members: __init__
    :show-inheritance:
    :noindex:

    .. autoclasstoc::

OutputStep
~~~~~~~~~~

.. autoclass:: abaqus.StepOutput.OutputStep.OutputStep
    :members:
    :special-members: __init__
    :show-inheritance:
    :noindex:

    .. autoclasstoc::

AnalysisStep
~~~~~~~~~~~~

.. autoclass:: abaqus.Step.AnalysisStep.AnalysisStep
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::

AnnealStep
~~~~~~~~~~

.. autoclass:: abaqus.Step.AnnealStep.AnnealStep
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::

BuckleStep
~~~~~~~~~~

.. autoclass:: abaqus.Step.BuckleStep.BuckleStep
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::

ComplexFrequencyStep
~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Step.ComplexFrequencyStep.ComplexFrequencyStep
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::

CoupledTempDisplacementStep
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Step.CoupledTempDisplacementStep.CoupledTempDisplacementStep
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::

CoupledThermalElectricalStructuralStep
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Step.CoupledThermalElectricalStructuralStep.CoupledThermalElectricalStructuralStep
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::

CoupledThermalElectricStep
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Step.CoupledThermalElectricStep.CoupledThermalElectricStep
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::

DirectCyclicStep
~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Step.DirectCyclicStep.DirectCyclicStep
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::

EmagTimeHarmonicStep
~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Step.EmagTimeHarmonicStep.EmagTimeHarmonicStep
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::

ExplicitDynamicsStep
~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Step.ExplicitDynamicsStep.ExplicitDynamicsStep
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::

FrequencyStep
~~~~~~~~~~~~~

.. autoclass:: abaqus.Step.FrequencyStep.FrequencyStep
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::

GeostaticStep
~~~~~~~~~~~~~

.. autoclass:: abaqus.Step.GeostaticStep.GeostaticStep
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::

HeatTransferStep
~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Step.HeatTransferStep.HeatTransferStep
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::

ImplicitDynamicsStep
~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Step.ImplicitDynamicsStep.ImplicitDynamicsStep
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::

InitialStep
~~~~~~~~~~~

.. autoclass:: abaqus.Step.InitialStep.InitialStep
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::

MassDiffusionStep
~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Step.MassDiffusionStep.MassDiffusionStep
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::

ModalDynamicsStep
~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Step.ModalDynamicsStep.ModalDynamicsStep
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::

RandomResponseStep
~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Step.RandomResponseStep.RandomResponseStep
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::

ResponseSpectrumStep
~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Step.ResponseSpectrumStep.ResponseSpectrumStep
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::

SoilsStep
~~~~~~~~~

.. autoclass:: abaqus.Step.SoilsStep.SoilsStep
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::

StaticLinearPerturbationStep
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Step.StaticLinearPerturbationStep.StaticLinearPerturbationStep
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::

StaticRiksStep
~~~~~~~~~~~~~~

.. autoclass:: abaqus.Step.StaticRiksStep.StaticRiksStep
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::

StaticStep
~~~~~~~~~~

.. autoclass:: abaqus.Step.StaticStep.StaticStep
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::

SteadyStateDirectStep
~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Step.SteadyStateDirectStep.SteadyStateDirectStep
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::

SteadyStateModalStep
~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Step.SteadyStateModalStep.SteadyStateModalStep
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::

SteadyStateSubspaceStep
~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Step.SteadyStateSubspaceStep.SteadyStateSubspaceStep
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::

SubspaceDynamicsStep
~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Step.SubspaceDynamicsStep.SubspaceDynamicsStep
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::

SubstructureGenerateStep
~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Step.SubstructureGenerateStep.SubstructureGenerateStep
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::

TempDisplacementDynamicsStep
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Step.TempDisplacementDynamicsStep.TempDisplacementDynamicsStep
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::

ViscoStep
~~~~~~~~~

.. autoclass:: abaqus.Step.ViscoStep.ViscoStep
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
