from abqpy.decorators import abaqus_class_doc, abaqus_method_doc


@abaqus_class_doc
class DataSet:
    """The DataSetobject specifies material test data.

    .. note::
        This object can be accessed by::

            import calibration
            mdb.models[name].calibrations[name].dataSets[name]
    """

    #: A String specifying the name of the new dataset.
    name: str

    #: A sequence of pairs of Floats specifying data set type pairs. Possible values are for
    #: stress/strain, force/displacement, or transverse strain/axial strain pairs.
    data: tuple = ()

    #: A String specifying the type of the new dataset. Values can be "STRESS/STRAIN",
    #: "FORCE/DISPLACEMENT", or "AXIALSTRAIN/TRANSVERSESTRAIN". The default value is
    #: "STRESS/STRAIN".
    type: str = ""

    #: A String specifying the form of the new dataset. Values can be "NOMINAL" or "TRUE". The
    #: default value is "NOMINAl".
    form: str = ""

    @abaqus_method_doc
    def __init__(self, name: str, data: tuple = (), type: str = "", form: str = ""):
        """This method creates a DataSet object.

        .. note::
            This function can be accessed by::

                mdb.models[name].calibrations[name].DataSet

        Parameters
        ----------
        name
            A String specifying the name of the new dataset.
        data
            A sequence of pairs of Floats specifying data set type pairs. Possible values are for
            stress/strain, force/displacement, or transverse strain/axial strain pairs.
        type
            A String specifying the type of the new dataset. Values can be "STRESS/STRAIN",
            "FORCE/DISPLACEMENT", or "AXIALSTRAIN/TRANSVERSESTRAIN". The default value is
            "STRESS/STRAIN".
        form
            A String specifying the form of the new dataset. Values can be "NOMINAL" or "TRUE". The
            default value is "NOMINAl".

        Returns
        -------
        DataSet
            A :py:class:`~abaqus.Calibration.DataSet.DataSet` object.
        """
        ...

    @abaqus_method_doc
    def setValues(self, data: tuple = ()):
        """This method modifies the data for an existing DataSet object.

        Parameters
        ----------
        data
            A sequence of pairs of Floats specifying data set type pairs.
        """
        ...
