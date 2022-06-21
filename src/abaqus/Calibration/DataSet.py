class DataSet:
    """The DataSetobject specifies material test data.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import calibration
        mdb.models[name].calibrations[name].dataSets[name]
    """

    def __init__(self, name: str, data: tuple = (), type: str = "", form: str = ""):
        """This method creates a DataSet object.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

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
        A :py:class:`~abaqus.Calibration.DataSet.DataSet` object.
        """
        pass

    def setValues(self, data: tuple = ()):
        """This method modifies the data for an existing DataSet object.

        Parameters
        ----------
        data
            A sequence of pairs of Floats specifying data set type pairs.
        """
        pass
