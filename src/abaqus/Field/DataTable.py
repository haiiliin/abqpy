from abqpy.decorators import abaqus_class_doc


@abaqus_class_doc
class DataTable:
    """A DataTable is an object used to define the domain and data for a DiscreteField.

    .. note:: 
        This object can be accessed by::

            import field
            mdb.models[name].discreteFields[name].data[i]
    """

    #: An Int specifying the width of the data. Valid widths are 1, 6, 21, corresponding to
    #: scalar data, orientations and 4D tensors.
    dataWidth: int = None

    #: A String specifying the index.
    name: str = ""

    #: A String specifying the instance name.
    instanceName: str = ""

    #: A tuple of Ints specifying the domain node, element or integration point identifiers.
    domain: int = None

    #: A tuple of Floats specifying the data within the domain.
    table: float = None
