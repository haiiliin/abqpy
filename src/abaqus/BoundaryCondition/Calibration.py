from ..Calibration.Behavior import Behavior
from ..Calibration.DataSet import DataSet


class Calibration:
    """A :py:class:`~abaqus.BoundaryCondition.Calibration.Calibration` object is the object used to specify a material calibration. The
    Calibration object stores the data that is used for specifying materials from test data.

    .. note:: 
        This object can be accessed by:

        .. code-block:: python

            import calibration
            mdb.models[name].calibrations[name]
    """

    #: A :py:class:`~abaqus.Calibration.DataSet.DataSet` object.
    dataSets: DataSet = None

    #: A :py:class:`~abaqus.Calibration.Behavior.Behavior` object.
    behaviors: Behavior = None

    #: A String specifying the name of the new calibration.
    name: str

    def __init__(self, name: str):
        """This method creates a Calibration object.

        .. note:: 
            This function can be accessed by:

            .. code-block:: python

                mdb.models[name].Calibration

        Parameters
        ----------
        name
            A String specifying the name of the new calibration.

        Returns
        -------
        Calibration
            A :py:class:`~abaqus.BoundaryCondition.Calibration.Calibration` object.
        """
        pass
