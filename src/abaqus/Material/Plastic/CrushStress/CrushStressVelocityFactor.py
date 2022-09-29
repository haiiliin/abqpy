from typing import Tuple

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc


@abaqus_class_doc
class CrushStressVelocityFactor:
    """The CrushStressVelocityFactor object defines how the approach velocity at a crushing interface
    influences a material's resistance to crushing.

    .. note::
        This object can be accessed by::

            import material
            mdb.models[name].materials[name].crushStress.crushStressVelocityFactor
            import odbMaterial
            session.odbs[name].materials[name].crushStress.crushStressVelocityFactor

        The table data for this object are:

        - Scaling factor.
        - Relative velocity.

        The corresponding analysis keywords are:

        - CRUSH STRESS VELOCITY FACTOR

    .. versionadded:: 2022
        The `CrushStressVelocityFactor` class was added.
    """

    #: A sequence of sequences of Floats specifying the items described below.
    crushStressVelocityFactorTable: Tuple[Tuple[float, ...]]

    @abaqus_method_doc
    def __init__(self, crushStressVelocityFactorTable: Tuple[Tuple[float, ...]]):
        """This method creates a CrushStressVelocityFactor object.

        Parameters
        ----------
        crushStressVelocityFactorTable
            A sequence of sequences of Floats specifying the items described below.
        """
        self.crushStressVelocityFactorTable = crushStressVelocityFactorTable

    @abaqus_method_doc
    def setValues(self, crushStressVelocityFactorTable: Tuple[Tuple[float, ...]] = ()):
        """This method creates a CrushStressVelocityFactor object.

        Parameters
        ----------
        crushStressVelocityFactorTable
            A sequence of sequences of Floats specifying the items described below.
        """
        self.crushStressVelocityFactorTable = crushStressVelocityFactorTable
