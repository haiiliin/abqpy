from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from ....UtilityAndView.abaqusConstants import Boolean, OFF


@abaqus_class_doc
class FailureRatios:
    """The FailureRatios object specifies the shape of the failure surface for a Concrete
    model.

    .. note:: 
        This object can be accessed by::

            import material
            mdb.models[name].materials[name].concrete.failureRatios
            import odbMaterial
            session.odbs[name].materials[name].concrete.failureRatios

        The table data for this object are:

        - Ratio of the ultimate biaxial compressive stress to the uniaxial compressive ultimate
          stress. The default value is 1.16.
        - Absolute value of the ratio of the uniaxial tensile stress at failure to the uniaxial 
          compressive stress at failure. The default value is 0.09.
        - Ratio of the magnitude of a principal component of Plastic strain at ultimate stress in 
          biaxial compression to the Plastic strain at ultimate stress in uniaxial compression. 
          The default value is 1.28.
        - Ratio of the tensile principal stress value at shear in plane stress, when the other 
          nonzero principal stress component is at the ultimate compressive stress value, to the 
          tensile cracking stress under uniaxial tension. The default value is 1/3.
        - Temperature, if the data depend on temperature.
        - Value of the first field variable, if the data depend on field variables.
        - Value of the second field variable.
        - Etc.

        The corresponding analysis keywords are:

        - FAILURE RATIOS
    """

    @abaqus_method_doc
    def __init__(
        self, table: tuple, temperatureDependency: Boolean = OFF, dependencies: int = 0
    ):
        """This method creates a FailureRatios object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].materials[name].concrete.FailureRatios
                session.odbs[name].materials[name].concrete.FailureRatios

        Parameters
        ----------
        table
            A sequence of sequences of Floats specifying the items described below.
        temperatureDependency
            A Boolean specifying whether the data depend on temperature. The default value is OFF.
        dependencies
            An Int specifying the number of field variable dependencies. The default value is 0.

        Returns
        -------
        FailureRatios
            A :py:class:`~abaqus.Material.Plastic.Concrete.FailureRatios.FailureRatios` object.

        Raises
        ------
        RangeError
        """
        ...

    @abaqus_method_doc
    def setValues(self, *args, **kwargs):
        """This method modifies the FailureRatios object.

        Raises
        ------
        RangeError
        """
        ...
