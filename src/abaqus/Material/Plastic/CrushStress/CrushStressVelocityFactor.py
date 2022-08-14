import typing

class CrushStressVelocityFactor:
    """The CrushStressVelocityFactor object defines how the approach velocity at a crushing interface
    influences a material's resistance to crushing.

    .. note::
        This object can be accessed by:

        .. code-block:: python

            import material
            mdb.models[name].materials[name].crushStress.crushStressVelocityFactor
            import odbMaterial
            session.odbs[name].materials[name].crushStress.crushStressVelocityFactor

        The table data for this object are:

        - Scaling factor.
        - Relative velocity.

        The corresponding analysis keywords are:

        - CRUSH STRESS VELOCITY FACTOR
    """

    #: A sequence of sequences of Floats specifying the items described below.
    crushStressVelocityFactorTable: typing.Tuple[typing.Tuple[float, ...]]

    def __init__(self, crushStressVelocityFactorTable: typing.Tuple[typing.Tuple[float, ...]]):
        """This method creates a CrushStressVelocityFactor object.

        Parameters
        ----------
        crushStressVelocityFactorTable
            A sequence of sequences of Floats specifying the items described below.
        """
        self.crushStressVelocityFactorTable = crushStressVelocityFactorTable

    def setValues(self, crushStressVelocityFactorTable: typing.Tuple[typing.Tuple[float, ...]] = ()):
        """This method creates a CrushStressVelocityFactor object.

        Parameters
        ----------
        crushStressVelocityFactorTable
            A sequence of sequences of Floats specifying the items described below.
        """
        self.crushStressVelocityFactorTable = crushStressVelocityFactorTable
