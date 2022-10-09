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
-------------

.. autoclass:: abaqus.Mdb.Mdb.Mdb
    :noindex:

    .. autoclasstoc::


Classes
-------

Model
~~~~~

.. autoclass:: abaqus.Model.Model.Model
    :members:

    .. autoclasstoc::

ModelBase
~~~~~~~~~

.. autoclass:: abaqus.Model.ModelBase.ModelBase
    :members:

    .. autoclasstoc::
