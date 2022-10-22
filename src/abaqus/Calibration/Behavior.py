from typing import Tuple

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from .DataSet import DataSet
from ..UtilityAndView.abaqusConstants import Boolean


@abaqus_class_doc
class Behavior:
    """The Behavior object specifies the method used for calibrating a material.

    .. note:: 
        This object can be accessed by::

            import calibration
            mdb.models[name].calibrations[name].behaviors[name]
    """

    #: A string specifying the name of the model to which the behavior belongs.
    modelName: str = ""

    #: A string specifying the name of calibration to which the behavior belongs.
    calibrationName: str = ""

    #: A String specifying the name of the dataset containing all the raw data in the test data
    #: file. Only valid if the behavior is of type FeFpBehavior
    biAxialAllName: str = ""

    #: A String specifying the name of the dataset containing all the raw data in the test data
    #: file. Only valid if the behavior is of type FeFpBehavior
    uniAxialAllName: str = ""

    #: A String specifying the name of the new behavior.
    name: str

    #: A String specifying the type of the new Behavior. Values can be "ElasIsoBehavior",
    #: "ElasPlasIsoBehavior", "FeFpBehavior", or a user plug-in behavior type.
    typeName: str

    @abaqus_method_doc
    def __init__(self, name: str, typeName: str):
        """This method creates a Behavior object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].calibrations[name].Behavior

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
        ...

    @abaqus_method_doc
    def setValues(
        self,
        E: str = "",
        nu: str = "",
        ds1Name: str = "",
        ds2Name: str = "",
        materialName: str = "",
        yieldPoint: str = "",
        ultimatePoint: str = "",
        plasticPoints: str = "",
        PoissonsRatio: str = "",
        elasticModulus: str = "",
        plasticPointsRange: str = "",
        name: str = "",
        uniaxialName: str = "",
        biaxialName: str = "",
        interpolation: str = "",
        uniWeight: str = "",
        biWeight: str = "",
        uMullinsReload: str = "",
        uMullinsUnload: str = "",
        uPYieldPoint: Tuple[float, float, float] = (),
        uPermSet: str = "",
        uPrimary: str = "",
        bMullinsReload: str = "",
        bMullinsUnload: str = "",
        bPYieldPoint: Tuple[float, float, float] = (),
        bPermSet: str = "",
        bPrimary: str = "",
    ):
        """This method modifies the data for an existing behavior object.

        Parameters
        ----------
        E
            Young's modulus. Only valid if the behavior type is ElasIsoBehavior.
        nu
            Poisson's ratio. Only valid if the behavior type is ElasIsoBehavior.
        ds1Name
            The name of the first data set. Only valid if the behavior type is ElasIsoBehavior or
            ElasPlasIsoBehavior
        ds2Name
            The name of the second data set. Only valid if the behavior type is ElasIsoBehavior or
            ElasPlasIsoBehavior
        materialName
            Material Name.
        yieldPoint
            Stress/strain value for the material yield point.Only valid if the behavior type is
            ElasPlasIsoBehavior
        ultimatePoint
            Stress/strain value for the material ultimate point.Only valid if the behavior type is
            ElasPlasIsoBehavior
        plasticPoints
            Stress/strain values for the Plastic portion of material curve. Only valid if the
            behavior type is ElasPlasIsoBehavior
        PoissonsRatio
            Poisson's Ratio. Only valid if the behavior type is ElasPlasIsoBehavior
        elasticModulus
            Young's Modulus for the elastic portion of the material curve. Only valid if the
            behavior type is ElasPlasIsoBehavior
        plasticPointsRange
            Extent of the material Plastic points. Only valid if the behavior type is
            ElasPlasIsoBehavior
        name
            Name of the behavior.
        uniaxialName
            Name of the uniaxial dataset. Only valid if the behavior type is FeFpBehavior
        biaxialName
            Name of the biaxial dataset. Only valid if the behavior type is FeFpBehavior
        interpolation
            'linear' specifies linear interpolation between data points, otherwise 'logarithmic'.
            Only valid if the behavior type is FeFpBehavior
        uniWeight
            Uniaxial weight factor, uniWeight + biWeight should equal 1.0. Only valid if the
            behavior type is FeFpBehavior
        biWeight
            Biaxial weight factor, uniWeight + biWeight should equal 1.0. Only valid if the behavior
            type is FeFpBehavior
        uMullinsReload
            A List of strings, specifying names of reloading DataSet objects obtained from uniaxial
            test data. Only valid if the behavior is of type FeFpBehavior
        uMullinsUnload
            A List of strings, specifying names of reloading DataSet objects obtained from uniaxial
            test data. Only valid if the behavior is of type FeFpBehavior
        uPYieldPoint
            A tuple specifying the coordinates of yield point of the permanent data set. Only valid
            if the behavior is of type FeFpBehavior
        uPermSet
            A List of strings, specifying names of permanent DataSet objects obtained from uniaxial
            test data. Only valid if the behavior is of type FeFpBehavior
        uPrimary
            A string specifying name of Primary DataSet object.Only valid if the behavior is of type
            FeFpBehavior
        bMullinsReload
            A List of strings, specifying names of reloading DataSet objects obtained from biaxial
            test data. Only valid if the behavior is of type FeFpBehavior
        bMullinsUnload
            A List of strings, specifying names of unloading DataSet objects obtained from biaxial
            test data. Only valid if the behavior is of type FeFpBehavior
        bPYieldPoint
            A tuple specifying the coordinates of yield point of the permanent data set. Only valid
            if the behavior is of type FeFpBehavior
        bPermSet
            A List of strings, specifying names of permanent DataSet objects obtained from biaxial
            test data. Only valid if the behavior is of type FeFpBehavior
        bPrimary
            A string specifying name of Primary DataSet object. Only valid if the behavior is of
            type FeFpBehavior
        """
        ...

    @abaqus_method_doc
    def mapToMaterial(self, materialName: str):
        """This method appends the calibration data obtained from the DataSet object to an existing
        material object. In the case of ElasIsoBehavior, it appends the young's modulus and
        poisson's ratio. For ElasPlasIsoBehavior it appends the young's modulus, poisson's ratio
        and Plastic points range and for FeFpBehavior it appends Plastic points range and
        Mullins effect properties.

        Parameters
        ----------
        materialName
            A String specifying the name of the existing material
        """
        ...

    @abaqus_method_doc
    def compute_E(self, dataSet: DataSet):
        """This method computes the value of young's modulus from the existing DataSet object. The
        method is only valid for ElasIsoBehavior type of behavior.

        Parameters
        ----------
        dataSet
            A :py:class:`~abaqus.Calibration.DataSet.DataSet` object.

        Returns
        -------
        Sequence[float]
            A tuple consisting of a and b values of the regression line(y = ax + b), coefficient of
            determination(r-squared) value and the start and end-points of the line.
        """
        ...

    @abaqus_method_doc
    def compute_nu(self, dataSet: DataSet):
        """This method computes the value of Poisson's Ratio from the existing DataSet object. The
        method is only valid for ElasIsoBehavior and ElasPlasIsoBehavior type of behavior.

        Parameters
        ----------
        dataSet
            A :py:class:`~abaqus.Calibration.DataSet.DataSet` object.

        Returns
        -------
        Sequence[float]
            A tuple consisting of a and b values of the regression line(y = ax + b), coefficient of
            determination(r-squared) value and the start and end-points of the line.
        """
        ...

    @abaqus_method_doc
    def compute_ultimatePoint(self, dataSet: DataSet):
        """This method computes the coordinates of the Ultimate point from the existing DataSet
        object. The method is only valid for ElasPlasIsoBehavior type of behavior.

        Parameters
        ----------
        dataSet
            A :py:class:`~abaqus.Calibration.DataSet.DataSet` object.

        Returns
        -------
        Sequence[float]
            Coordinates of the ultimate point.
        """
        ...

    @abaqus_method_doc
    def compute_elasticModulus(self, yieldPoint: tuple):
        """This method computes the value of the elastic modulus from the yieldpoint value. The
        method is only valid for ElasPlasIsoBehavior type of behavior.

        Parameters
        ----------
        yieldPoint
            A tuple consisting of coordinates of the yieldpoint.

        Returns
        -------
        float
            A float specifying the value of elastic modulus.
        """
        ...

    @abaqus_method_doc
    def compute_plasticPoints(
        self,
        dataSet: DataSet,
        slider_val: str,
        start_index: str,
        end_index: str,
        yp: str = "",
    ):
        """This method extracts the coordinates of the Plastic Points. The method is only valid for
        ElasPlasIsoBehavior type of behavior.

        Parameters
        ----------
        dataSet
            A :py:class:`~abaqus.Calibration.DataSet.DataSet` object.
        slider_val
            A float specifying the number of values to be taken.
        start_index
            A float specifying the lower limit of the range.
        end_index
            A float specifying the upper limit of the range.
        yp
            Coordinates of the yieldpoint. The default value is (0,0).

        Returns
        -------
        Sequence[Tuple[float]]
            A sequence of coordinates of the Plastic points..
        """
        ...

    @abaqus_method_doc
    def xyDataDissect(
        self, dsName: str, modelName: str, calibrationName: str, biaxial: Boolean = True
    ):
        """This method extracts primary, unload, reload and permanent DataSet objects from the
        existing DataSet object.The method is only valid for FeFpBehavior type of behavior.

        Parameters
        ----------
        dsName
            A string specifying the name of the uniaxial/biaxial test dataset.
        modelName
            A string specifying the name of the model to which the calibration behavior belongs.
        calibrationName
            A string specifying the name of the Calibration object to which the behavior belongs.
        biaxial
            A boolean specifying whether the test data is biaxial or uniaxial. The default value is
            True.

        Returns
        -------
        Sequence[str]
            A sequence of strings specifying names of the DataSet objects containing loading,
            unloading, reloading and primary datasets.
        """
        ...
