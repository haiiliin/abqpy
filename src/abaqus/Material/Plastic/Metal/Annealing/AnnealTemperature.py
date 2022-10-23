from abqpy.decorators import abaqus_class_doc, abaqus_method_doc


@abaqus_class_doc
class AnnealTemperature:
    r"""The AnnealTemperature object specifies the material annealing temperature.

    .. note::
        This object can be accessed by::

            import material
            mdb.models[name].materials[name].Plastic.annealTemperature
            import odbMaterial
            session.odbs[name].materials[name].Plastic.annealTemperature

        The table data for this object are:

        - The annealing temperature, :math:`\theta`.
        - Temperature, if the data depend on temperature.
        - Value of the first field variable, if the data depend on field variables.
        - Value of the second field variable.
        - Etc.

        The corresponding analysis keywords are:

        - ANNEAL TEMPERATURE
    """

    @abaqus_method_doc
    def __init__(self, table: tuple, dependencies: int = 0):
        """This method creates an AnnealTemperature object.

        .. note::
            This function can be accessed by::

                mdb.models[name].materials[name].Plastic.AnnealTemperature
                session.odbs[name].materials[name].Plastic.AnnealTemperature

        Parameters
        ----------
        table
            A sequence of sequences of Floats specifying the items described below.
        dependencies
            An Int specifying the number of field variable dependencies. The default value is 0.

        Returns
        -------
        AnnealTemperature
            An :py:class:`~abaqus.Material.Plastic.Metal.Annealing.AnnealTemperature.AnnealTemperature` object.

        Raises
        ------
        RangeError
        """
        ...

    @abaqus_method_doc
    def setValues(self, *args, **kwargs):
        """This method modifies the AnnealTemperature object.

        Raises
        ------
        RangeError
        """
        ...
