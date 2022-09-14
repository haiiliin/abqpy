from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from .Behavior import Behavior
from .DataSet import DataSet


@abaqus_class_doc
class Calibration:
    """A :py:class:`~abaqus.Material.Calibration.Calibration` object is the object used to specify a material calibration. The
    Calibration object stores the data that is used for specifying materials from test data.

    .. note:: 
        This object can be accessed by::

            import calibration
            mdb.models[name].calibrations[name]
    """

    #: A :py:class:`~abaqus.Calibration.DataSet.DataSet` object.
    dataSets: DataSet = None

    #: A :py:class:`~abaqus.Calibration.Behavior.Behavior` object.
    behaviors: Behavior = None

    #: A String specifying the name of the new calibration.
    name: str

    @abaqus_method_doc
    def __init__(self, name: str):
        """This method creates a Calibration object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].Calibration

        Parameters
        ----------
        name
            A String specifying the name of the new calibration.

        Returns
        -------
        Calibration
            A :py:class:`~abaqus.Material.Calibration.Calibration` object.
        """
        ...

    @abaqus_method_doc
    def Behavior(self, name: str, typeName: str) -> Behavior:
        """This method creates a Behavior object.

        .. note:: 
            This function can be accessed by::

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
        Behavior
            A :py:class:`~abaqus.Calibration.Behavior.Behavior` object.
        """
        self.behaviors = behavior = Behavior(name, typeName)
        return behavior

    @abaqus_method_doc
    def DataSet(
        self, name: str, data: tuple = (), type: str = "", form: str = ""
    ) -> DataSet:
        """This method creates a DataSet object.

        .. note:: 
            This function can be accessed by::

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
        DataSet
            A :py:class:`~abaqus.Calibration.DataSet.DataSet` object.
        """
        self.dataSets = dataSet = DataSet(name, data, type, form)
        return dataSet
