=====
Field
=====

A Field object stores the non-propagating data of a field as well as a number of instances of the corresponding FieldState object. The FieldState object stores the propagating data of the field in a single step. A specific type of Field object and a specific type of FieldState object are designed for each type of predefined field. Instances of the FieldState object are created and deleted internally by its corresponding Field object.


Create fields
-------------

.. autoclass:: abaqus.Field.FieldModel.FieldModel
    :noindex:

    .. autoclasstoc::