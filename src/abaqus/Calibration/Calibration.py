from .Behavior import Behavior
from .DataSet import DataSet


class Calibration:
    """A Calibration object is the object used to specify a material calibration. The
    Calibration object stores the data that is used for specifying materials from test data.

    Attributes
    ----------
    dataSets: DataSet
        A :py:class:`~abaqus.Calibration.DataSet.DataSet` object.
    behaviors: Behavior
        A :py:class:`~abaqus.Calibration.Behavior.Behavior` object.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import calibration
        mdb.models[name].calibrations[name]

    """

    # A DataSet object.
    dataSets: DataSet = None

    # A Behavior object.
    behaviors: Behavior = None

    def __init__(self, name: str):
        """This method creates a Calibration object.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

                      mdb.models[name].Calibration

        Parameters
        ----------
        name
            A String specifying the name of the new calibration.

        Returns
        -------
            A Calibration object.
        """
        pass

    def Behavior(self, name: str, typeName: str) -> Behavior:
        """This method creates a Behavior object.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

                      mdb.models[name].Calibration

        Parameters
        ----------
        name
            A String specifying the name of the new behavior.
        typeName
            A String specifying the type of the new Behavior. Values can be "ElasIsoBehavior",
            "ElasPlasIsoBehavior", "FeFpBehavior", or a user plug-in behavior type.

        Returns
        -------
            A Behavior object.
        """
        self.behaviors = behavior = Behavior(name, typeName)
        return behavior

    def DataSet(
        self, name: str, data: tuple = (), type: str = "", form: str = ""
    ) -> DataSet:
        """This method creates a DataSet object.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

                      mdb.models[name].Calibration

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
            A DataSet object.
        """
        self.dataSets = dataSet = DataSet(name, data, type, form)
        return dataSet
