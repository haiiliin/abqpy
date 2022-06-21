from abaqusConstants import *
from .FailureRatios import FailureRatios
from .ShearRetention import ShearRetention
from .TensionStiffening import TensionStiffening


class Concrete:
    """The Concrete object defines concrete properties beyond the elastic range.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import material
        mdb.models[name].materials[name].concrete
        import odbMaterial
        session.odbs[name].materials[name].concrete

    The table data for this object are:

    - Absolute value of compressive stress.
    - Absolute value of Plastic strain.
    - Temperature, if the data depend on temperature.
    - Value of the first field variable, if the data depend on field variables.
    - Value of the second field variable.
    - Etc.

    The corresponding analysis keywords are:

    - CONCRETE
    """

    # A FailureRatios object.
    failureRatios: FailureRatios = FailureRatios(((),))

    # A ShearRetention object.
    shearRetention: ShearRetention = ShearRetention(((),))

    # A TensionStiffening object.
    tensionStiffening: TensionStiffening = TensionStiffening(((),))

    def __init__(
        self, table: tuple, temperatureDependency: Boolean = OFF, dependencies: int = 0
    ):
        """This method creates a Concrete object.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            mdb.models[name].materials[name].Concrete
            session.odbs[name].materials[name].Concrete

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
            A Concrete object.

        Raises
        ------
        RangeError
        """
        pass

    def setValues(self, *args, **kwargs):
        """This method modifies the Concrete object.

        Raises
        ------
        RangeError
        """
        pass
