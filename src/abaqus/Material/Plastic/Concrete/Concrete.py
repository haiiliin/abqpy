from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from .FailureRatios import FailureRatios
from .ShearRetention import ShearRetention
from .TensionStiffening import TensionStiffening
from ....UtilityAndView.abaqusConstants import Boolean, OFF


@abaqus_class_doc
class Concrete:
    """The Concrete object defines concrete properties beyond the elastic range.

    .. note:: 
        This object can be accessed by::

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

    #: A :py:class:`~abaqus.Material.Plastic.Concrete.FailureRatios.FailureRatios` object.
    failureRatios: FailureRatios = FailureRatios(((),))

    #: A :py:class:`~abaqus.Material.Plastic.Concrete.ShearRetention.ShearRetention` object.
    shearRetention: ShearRetention = ShearRetention(((),))

    #: A :py:class:`~abaqus.Material.Plastic.Concrete.TensionStiffening.TensionStiffening` object.
    tensionStiffening: TensionStiffening = TensionStiffening(((),))

    @abaqus_method_doc
    def __init__(
        self, table: tuple, temperatureDependency: Boolean = OFF, dependencies: int = 0
    ):
        """This method creates a Concrete object.

        .. note:: 
            This function can be accessed by::

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
        Concrete
            A :py:class:`~abaqus.Material.Plastic.Concrete.Concrete.Concrete` object.

        Raises
        ------
        RangeError
        """
        ...

    @abaqus_method_doc
    def setValues(self, *args, **kwargs):
        """This method modifies the Concrete object.

        Raises
        ------
        RangeError
        """
        ...
