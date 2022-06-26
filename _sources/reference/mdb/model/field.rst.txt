=====
Field
=====

A Field object stores the non-propagating data of a field as well as a number of instances of the corresponding FieldState object. The FieldState object stores the propagating data of the field in a single step. A specific type of Field object and a specific type of FieldState object are designed for each type of predefined field. Instances of the FieldState object are created and deleted internally by its corresponding Field object.


Create fields
-------------

.. autoclass:: abaqus.Field.FieldModel.FieldModel
    :members:


Object features
---------------

Field
~~~~~

.. autoclass:: abaqus.Field.Field.Field
    :members:

    .. autoclassdoc::

AnalyticalField
~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Field.AnalyticalField.AnalyticalField
    :members:

    .. autoclassdoc::

DataTable
~~~~~~~~~

.. autoclass:: abaqus.Field.DataTable.DataTable
    :members:

    .. autoclassdoc::

DataTableArray
~~~~~~~~~~~~~~

.. autoclass:: abaqus.Field.DataTableArray.DataTableArray
    :members:

    .. autoclassdoc::

DiscreteField
~~~~~~~~~~~~~

.. autoclass:: abaqus.Field.DiscreteField.DiscreteField
    :members:

    .. autoclassdoc::

ExpressionField
~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Field.ExpressionField.ExpressionField
    :members:

    .. autoclassdoc::

MappedField
~~~~~~~~~~~

.. autoclass:: abaqus.Field.MappedField.MappedField
    :members:

    .. autoclassdoc::

OdbMeshRegionData
~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Field.OdbMeshRegionData.OdbMeshRegionData
    :members:

    .. autoclassdoc::

