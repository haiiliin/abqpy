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
    :members:

    .. autoclasstoc::


Object features
---------------

Model
~~~~~

.. autoclass:: abaqus.Model.Model.Model
    :members:
    :inherited-members:

    .. autoclasstoc::

ModelBase
~~~~~~~~~

.. autoclass:: abaqus.Model.ModelBase.ModelBase
    :members:

    .. autoclasstoc::

AdaptivityModel
~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Adaptivity.AdaptivityModel.AdaptivityModel
    :members:
    :inherited-members:

    .. autoclasstoc::

AmplitudeModel
~~~~~~~~~~~~~~

.. autoclass:: abaqus.Amplitude.AmplitudeModel.AmplitudeModel
    :members:
    :inherited-members:

    .. autoclasstoc::

AssemblyModel
~~~~~~~~~~~~~

.. autoclass:: abaqus.Assembly.AssemblyModel.AssemblyModel
    :members:
    :inherited-members:

    .. autoclasstoc::

BoundaryConditionModel
~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel
    :members:
    :inherited-members:

    .. autoclasstoc::

CalibrationModel
~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Calibration.CalibrationModel.CalibrationModel
    :members:
    :inherited-members:

    .. autoclasstoc::

ConstraintModel
~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Constraint.ConstraintModel.ConstraintModel
    :members:
    :inherited-members:

    .. autoclasstoc::

FilterModel
~~~~~~~~~~~

.. autoclass:: abaqus.Filter.FilterModel.FilterModel
    :members:
    :inherited-members:

    .. autoclasstoc::

InteractionModel
~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Interaction.InteractionModel.InteractionModel
    :members:
    :inherited-members:

    .. autoclasstoc::

LoadModel
~~~~~~~~~

.. autoclass:: abaqus.Load.LoadModel.LoadModel
    :members:
    :inherited-members:

    .. autoclasstoc::

MaterialModel
~~~~~~~~~~~~~

.. autoclass:: abaqus.Material.MaterialModel.MaterialModel
    :members:
    :inherited-members:

    .. autoclasstoc::

OptimizationTaskModel
~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel
    :members:
    :inherited-members:

    .. autoclasstoc::

PartModel
~~~~~~~~~

.. autoclass:: abaqus.Part.PartModel.PartModel
    :members:
    :inherited-members:

    .. autoclasstoc::

PredefinedFieldModel
~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.PredefinedField.PredefinedFieldModel.PredefinedFieldModel
    :members:
    :inherited-members:

    .. autoclasstoc::

BeamSectionProfileModel
~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BeamSectionProfile.BeamSectionProfileModel.BeamSectionProfileModel
    :members:
    :inherited-members:

    .. autoclasstoc::

OutputModel
~~~~~~~~~~~

.. autoclass:: StepOutput.StepOutput.OutputModel.OutputModel
    :members:
    :inherited-members:

    .. autoclasstoc::

SectionModel
~~~~~~~~~~~~

.. autoclass:: abaqus.Section.SectionModel.SectionModel
    :members:
    :inherited-members:

    .. autoclasstoc::

SketchModel
~~~~~~~~~~~

.. autoclass:: abaqus.Sketch.SketchModel.SketchModel
    :members:
    :inherited-members:

    .. autoclasstoc::

StepModel
~~~~~~~~~

.. autoclass:: abaqus.Step.StepModel.StepModel
    :members:
    :inherited-members:

    .. autoclasstoc::

KeywordBlock
~~~~~~~~~~~~

.. autoclass:: abaqus.Model.KeywordBlock.KeywordBlock
    :members:
