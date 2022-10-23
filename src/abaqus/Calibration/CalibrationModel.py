from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from ..Calibration.Calibration import Calibration
from ..Model.ModelBase import ModelBase


@abaqus_class_doc
class CalibrationModel(ModelBase):
    """Abaqus creates a Model object named `Model-1` when a session is started.

    .. note::
        This object can be accessed by::

            mdb.models[name]
    """

    @abaqus_method_doc
    def Calibration(self, name: str) -> Calibration:
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
        self.calibrations[name] = calibration = Calibration(name)
        return calibration
