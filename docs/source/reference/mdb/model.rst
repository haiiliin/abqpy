=====
Model
=====

Model commands are used to create Abaqus/CAE models. A finished model contains all the data that Abaqus/CAE needs to create and submit an analysis to Abaqus/Standard or Abaqus/Explicit. Models are stored in a model database.


.. toctree::
   :maxdepth: 1
   :caption: Objects in Model
   
   model/adaptivity
   model/amplitude
   model/bc
   model/calibration
   model/constraint
   model/field
   model/filter
   model/interaction
   model/load
   model/material
   model/mesh
   model/optimization
   model/output
   model/part_assembly
   model/predefined
   model/profile
   model/property
   model/section
   model/sketcher
   model/step


Create models
--------------

.. autoclass:: abaqus.Mdb.Mdb.Mdb
    :noindex:

    .. autoclasstoc::


Object features
---------------

Model
~~~~~

.. autoclass:: abaqus.Model.Model.Model
    :members:
    :special-members: __init__
    :inherited-members:

    .. autoclasstoc::

ModelBase
~~~~~~~~~

.. autoclass:: abaqus.Model.ModelBase.ModelBase
    :members:
    :special-members: __init__

    .. autoclasstoc::

AdaptivityModel
~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Adaptivity.AdaptivityModel.AdaptivityModel
    :members:
    :special-members: __init__
    :inherited-members:
    :noindex:

    .. autoclasstoc::

AmplitudeModel
~~~~~~~~~~~~~~

.. autoclass:: abaqus.Amplitude.AmplitudeModel.AmplitudeModel
    :members:
    :special-members: __init__
    :inherited-members:
    :noindex:

    .. autoclasstoc::

AssemblyModel
~~~~~~~~~~~~~

.. autoclass:: abaqus.Assembly.AssemblyModel.AssemblyModel
    :members:
    :special-members: __init__
    :inherited-members:
    :noindex:

    .. autoclasstoc::

BoundaryConditionModel
~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel
    :members:
    :special-members: __init__
    :inherited-members:
    :noindex:

    .. autoclasstoc::

CalibrationModel
~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Calibration.CalibrationModel.CalibrationModel
    :members:
    :special-members: __init__
    :inherited-members:
    :noindex:

    .. autoclasstoc::

ConstraintModel
~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Constraint.ConstraintModel.ConstraintModel
    :members:
    :special-members: __init__
    :inherited-members:
    :noindex:

    .. autoclasstoc::

FilterModel
~~~~~~~~~~~

.. autoclass:: abaqus.Filter.FilterModel.FilterModel
    :members:
    :special-members: __init__
    :inherited-members:
    :noindex:

    .. autoclasstoc::

InteractionModel
~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Interaction.InteractionModel.InteractionModel
    :members:
    :special-members: __init__
    :inherited-members:
    :noindex:

    .. autoclasstoc::

LoadModel
~~~~~~~~~

.. autoclass:: abaqus.Load.LoadModel.LoadModel
    :members:
    :special-members: __init__
    :inherited-members:
    :noindex:

    .. autoclasstoc::

MaterialModel
~~~~~~~~~~~~~

.. autoclass:: abaqus.Material.MaterialModel.MaterialModel
    :members:
    :special-members: __init__
    :inherited-members:
    :noindex:

    .. autoclasstoc::

OptimizationTaskModel
~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel
    :members:
    :special-members: __init__
    :inherited-members:
    :noindex:

    .. autoclasstoc::

PartModel
~~~~~~~~~

.. autoclass:: abaqus.Part.PartModel.PartModel
    :members:
    :special-members: __init__
    :inherited-members:
    :noindex:

    .. autoclasstoc::

PredefinedFieldModel
~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.PredefinedField.PredefinedFieldModel.PredefinedFieldModel
    :members:
    :special-members: __init__
    :inherited-members:
    :noindex:

    .. autoclasstoc::

BeamSectionProfileModel
~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BeamSectionProfile.BeamSectionProfileModel.BeamSectionProfileModel
    :members:
    :special-members: __init__
    :inherited-members:
    :noindex:

    .. autoclasstoc::

OutputModel
~~~~~~~~~~~

.. autoclass:: abaqus.StepOutput.OutputModel.OutputModel
    :members:
    :special-members: __init__
    :inherited-members:
    :noindex:

    .. autoclasstoc::

SectionModel
~~~~~~~~~~~~

.. autoclass:: abaqus.Section.SectionModel.SectionModel
    :members:
    :special-members: __init__
    :inherited-members:
    :noindex:

    .. autoclasstoc::

SketchModel
~~~~~~~~~~~

.. autoclass:: abaqus.Sketcher.SketchModel.SketchModel
    :members:
    :special-members: __init__
    :inherited-members:
    :noindex:

    .. autoclasstoc::

StepModel
~~~~~~~~~

.. autoclass:: abaqus.Step.StepModel.StepModel
    :members:
    :special-members: __init__
    :inherited-members:
    :noindex:

    .. autoclasstoc::

KeywordBlock
~~~~~~~~~~~~

.. autoclass:: abaqus.Model.KeywordBlock.KeywordBlock
    :members:
    :special-members: __init__
