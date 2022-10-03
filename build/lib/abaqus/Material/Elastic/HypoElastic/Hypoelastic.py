from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from ....UtilityAndView.abaqusConstants import Boolean, OFF


@abaqus_class_doc
class Hypoelastic:
    r"""The Hypoelastic object specifies hypoelastic material properties.

    .. note:: 
        This object can be accessed by::

            import material
            mdb.models[name].materials[name].hypoelastic
            import odbMaterial
            session.odbs[name].materials[name].hypoelastic

        The table data for this object are:

        - Instantaneous Young's modulus, :math:`E`.
        - Instantaneous Poisson's ratio, :math:`\nu`.
        - First strain invariant, :math:`I_1`.
        - Second strain invariant, :math:`I_2`.
        - Third strain invariant, :math:`I_3`.

        The corresponding analysis keywords are:

        - HYPOELASTIC
    """

    @abaqus_method_doc
    def __init__(self, table: tuple, user: Boolean = OFF):
        """This method creates a Hypoelastic object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].materials[name].Hypoelastic
                session.odbs[name].materials[name].Hypoelastic

        Parameters
        ----------
        table
            A sequence of sequences of Floats specifying the items described below.
        user
            A Boolean specifying that hypoelasticity is defined by user subroutine UHYPEL. The
            default value is OFF.

        Returns
        -------
        Hypoelastic
            A :py:class:`~abaqus.Material.Elastic.HypoElastic.Hypoelastic.Hypoelastic` object.
        """
        ...

    @abaqus_method_doc
    def setValues(self, *args, **kwargs):
        """This method modifies the Hypoelastic object."""
        ...
