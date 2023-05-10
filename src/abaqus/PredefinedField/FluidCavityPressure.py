from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from ..Region.Region import Region
from .PredefinedField import PredefinedField


@abaqus_class_doc
class FluidCavityPressure(PredefinedField):
    """The FluidCavityPressure object stores the data for initial fluid cavity pressures. The base class
    *region* argument can not be specifed with this object. The FluidCavityPressure object is derived from the
    PredefinedField object.

    .. note::
        This object can be accessed by::

            import load
            mdb.models[name].predefinedFields[name]

        The corresponding analysis keywords are:

        - INITIAL CONDITIONS
    """

    #: A Region object on which the **fluidCavity** interaction is specified.
    region: Region = Region()

    #: A String specifying the repository key.
    name: str

    #: A String specifying the name of a Fluid Cavity Interaction.
    fluidCavity: str

    #: A Float specifying the initial fluid pressure.
    fluidPressure: float

    @abaqus_method_doc
    def __init__(self, name: str, fluidCavity: str, fluidPressure: float):
        """This method creates a FluidCavityPressure object.

        .. note::
            This function can be accessed by::

                mdb.models[name].FluidCavityPressure

        Parameters
        ----------
        name
            A String specifying the repository key.
        fluidCavity
            A String specifying the name of a Fluid Cavity Interaction.
        fluidPressure
            A Float specifying the initial fluid pressure.

        Returns
        -------
        FluidCavityPressure
            A FluidCavityPressure object.
        """
        super().__init__()

    @abaqus_method_doc
    def setValues(self, *args, **kwargs):
        """This method modifies the FluidCavityPressure object."""
        ...
