# Field

A Field object stores the non-propagating data of a field as well as a number of instances of the corresponding FieldState object. The FieldState object stores the propagating data of the field in a single step. A specific type of Field object and a specific type of FieldState object are designed for each type of predefined field. Instances of the FieldState object are created and deleted internally by its corresponding Field object.

## Create fields

```{eval-rst}
.. autoclass:: abaqus.Field.FieldModel.FieldModel

    .. autoclasstoc::

```

## Classes

```{eval-rst}

.. collapse:: Click here to Expand

    .. autoclass:: abaqus.Field.Field.Field

        .. autoclasstoc::
    ```

    ### AnalyticalField

    ```{eval-rst}
    .. autoclass:: abaqus.Field.AnalyticalField.AnalyticalField

        .. autoclasstoc::
    ```

    ### DataTable

    ```{eval-rst}
    .. autoclass:: abaqus.Field.DataTable.DataTable

        .. autoclasstoc::
    ```

    ### DataTableArray

    ```{eval-rst}
    .. autoclass:: abaqus.Field.DataTableArray.DataTableArray

        .. autoclasstoc::
    ```

    ### DiscreteField

    ```{eval-rst}
    .. autoclass:: abaqus.Field.DiscreteField.DiscreteField

        .. autoclasstoc::
    ```

    ### ExpressionField

    ```{eval-rst}
    .. autoclass:: abaqus.Field.ExpressionField.ExpressionField

        .. autoclasstoc::
    ```

    ### MappedField

    ```{eval-rst}
    .. autoclass:: abaqus.Field.MappedField.MappedField

        .. autoclasstoc::
    ```

    ### OdbMeshRegionData

    ```{eval-rst}
    .. autoclass:: abaqus.Field.OdbMeshRegionData.OdbMeshRegionData

        .. autoclasstoc::
```
