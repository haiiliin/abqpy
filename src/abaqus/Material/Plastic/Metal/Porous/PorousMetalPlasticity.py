from typing import Optional

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from .PorousFailureCriteria import PorousFailureCriteria
from .VoidNucleation import VoidNucleation
from .....UtilityAndView.abaqusConstants import Boolean, OFF


@abaqus_class_doc
class PorousMetalPlasticity:
    """The PorousMetalPlasticity object specifies a porous metal plasticity model.

    .. note:: 
        This object can be accessed by::

            import material
            mdb.models[name].materials[name].porousMetalPlasticity
            import odbMaterial
            session.odbs[name].materials[name].porousMetalPlasticity

        The table data for this object are:

        - :math:`q_1`.
        - :math:`q_2`.
        - :math:`q_3`.
        - Temperature, if the data depend on temperature.
        - Value of the first field variable, if the data depend on field variables.
        - Value of the second field variable.
        - Etc.

        The corresponding analysis keywords are:

        - POROUS METAL PLASTICITY
    """

    #: A :py:class:`~abaqus.Material.Plastic.Metal.Porous.PorousFailureCriteria.PorousFailureCriteria` object.
    porousFailureCriteria: PorousFailureCriteria = PorousFailureCriteria()

    #: A :py:class:`~abaqus.Material.Plastic.Metal.Porous.VoidNucleation.VoidNucleation` object.
    voidNucleation: VoidNucleation = VoidNucleation(((),))

    @abaqus_method_doc
    def __init__(
        self,
        table: tuple,
        relativeDensity: Optional[float] = None,
        temperatureDependency: Boolean = OFF,
        dependencies: int = 0,
    ):
        """This method creates a PorousMetalPlasticity object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].materials[name].PorousMetalPlasticity
                session.odbs[name].materials[name].PorousMetalPlasticity

        Parameters
        ----------
        table
            A sequence of sequences of Floats specifying the items described below.
        relativeDensity
            None or a Float specifying the initial relative density of the material, r0. The default
            value is None.
        temperatureDependency
            A Boolean specifying whether the data depend on temperature. The default value is OFF.
        dependencies
            An Int specifying the number of field variable dependencies. The default value is 0.

        Returns
        -------
        PorousMetalPlasticity
            A :py:class:`~abaqus.Material.Plastic.Metal.Porous.PorousMetalPlasticity.PorousMetalPlasticity` object.

        Raises
        ------
        RangeError
        """
        ...

    @abaqus_method_doc
    def setValues(self, *args, **kwargs):
        """This method modifies the PorousMetalPlasticity object.

        Raises
        ------
        RangeError
        """
        ...
