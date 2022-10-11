=====
Field
=====

A Field object stores the non-propagating data of a field as well as a number of instances of the corresponding FieldState object. The FieldState object stores the propagating data of the field in a single step. A specific type of Field object and a specific type of FieldState object are designed for each type of predefined field. Instances of the FieldState object are created and deleted internally by its corresponding Field object.


Create fields
-------------

.. autoclass:: abaqus.Field.FieldModel.FieldModel
    :members:
    :special-members: __init__

    .. autoclasstoc::


Classes
-------

Field
~~~~~

.. autoclass:: abaqus.Field.Field.Field
    :members:
    :special-members: __init__

    .. autoclasstoc::

AnalyticalField
~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Field.AnalyticalField.AnalyticalField
    :members:
    :special-members: __init__

    .. autoclasstoc::

DataTable
~~~~~~~~~

.. autoclass:: abaqus.Field.DataTable.DataTable
    :members:
    :special-members: __init__

    .. autoclasstoc::

DataTableArray
~~~~~~~~~~~~~~

.. autoclass:: abaqus.Field.DataTableArray.DataTableArray
    :members:
    :special-members: __init__

    .. autoclasstoc::

DiscreteField
~~~~~~~~~~~~~

.. autoclass:: abaqus.Field.DiscreteField.DiscreteField
    :members:
    :special-members: __init__

    .. autoclasstoc::

ExpressionField
~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Field.ExpressionField.ExpressionField
    :members:
    :special-members: __init__

    .. autoclasstoc::

MappedField
~~~~~~~~~~~

.. autoclass:: abaqus.Field.MappedField.MappedField
    :members:
    :special-members: __init__

    .. autoclasstoc::

OdbMeshRegionData
~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Field.OdbMeshRegionData.OdbMeshRegionData
    :members:
    :special-members: __init__

    .. autoclasstoc::

