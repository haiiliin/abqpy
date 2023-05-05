from abqpy.decorators import abaqus_class_doc, abaqus_method_doc


@abaqus_class_doc
class GapRadiation:
    """The GapRadiation object specifies radiative heat transfer between closely adjacent surfaces.

    .. note::
        This object can be accessed by::

            import material
            mdb.models[name].materials[name].gapRadiation
            import odbMaterial
            session.odbs[name].materials[name].gapRadiation

        The table data for this object are:

        - Effective view factor.
        - Gap clearance.
        - Repeat this data line as often as necessary to define the dependence of the view factor on gap clearance.

        The corresponding analysis keywords are:

        - GAP RADIATION

    .. versionadded:: 2021
        The ``GapRadiation`` class was added.
    """

    @abaqus_method_doc
    def __init__(
        self,
        masterSurfaceEmissivity: float,
        slaveSurfaceEmissivity: float,
        table: tuple,
    ):
        r"""This method creates a GapRadiation object.

        .. note::
            This function can be accessed by::

                mdb.models[name].materials[name].Gapradiation
                session.odbs[name].materials[name].Gapradiation

        Parameters
        ----------
        masterSurfaceEmissivity
            A Float specifying the Emissivity of master surface :math:`\varepsilon_A`.
        slaveSurfaceEmissivity
            A Float specifying the Emissivity of the slave surface :math:`\varepsilon_B`.
        table
            A sequence of sequences of Floats specifying the items described below.

        Returns
        -------
            A GapRadiation object.
        """
        ...

    @abaqus_method_doc
    def setValues(self):
        """This method modifies the GapRadiation object."""
        ...
