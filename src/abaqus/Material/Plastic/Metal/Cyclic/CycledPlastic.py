from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from .....UtilityAndView.abaqusConstants import *


@abaqus_class_doc
class CycledPlastic:
    """The CycledPlastic object specifies cycled yield stress data for the ORNL constitutive
    model.

    .. note:: 
        This object can be accessed by::

            import material
            mdb.models[name].materials[name].Plastic.cycledPlastic
            import odbMaterial
            session.odbs[name].materials[name].Plastic.cycledPlastic

        The table data for this object are:

        - Yield stress.
        - Plastic strain.
        - Temperature, if the data depend on temperature.

        The corresponding analysis keywords are:

        - CYCLED PLASTIC
    """

    @abaqus_method_doc
    def __init__(self, table: tuple, temperatureDependency: Boolean = OFF):
        """This method creates a CycledPlastic object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].materials[name].Plastic.CycledPlastic
                session.odbs[name].materials[name].Plastic.CycledPlastic

        Parameters
        ----------
        table
            A sequence of sequences of Floats specifying the items described below.
        temperatureDependency
            A Boolean specifying whether the data depend on temperature. The default value is OFF.

        Returns
        -------
        CycledPlastic
            A :py:class:`~abaqus.Material.Plastic.Metal.Cyclic.CycledPlastic.CycledPlastic` object.
        """
        ...

    @abaqus_method_doc
    def setValues(self, *args, **kwargs):
        """This method modifies the CycledPlastic object."""
        ...
