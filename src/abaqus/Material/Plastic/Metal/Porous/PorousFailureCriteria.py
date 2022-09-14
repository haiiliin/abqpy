from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

@abaqus_class_doc
class PorousFailureCriteria:
    """The PorousFailureCriteria object specifies the material failure criteria for a porous
    metal.

    .. note:: 
        This object can be accessed by::

            import material
            mdb.models[name].materials[name].porousMetalPlasticity.porousFailureCriteria
            import odbMaterial
            session.odbs[name].materials[name].porousMetalPlasticity.porousFailureCriteria

        The corresponding analysis keywords are:

        - POROUS FAILURE CRITERIA
    """

    @abaqus_method_doc
    def __init__(self, fraction: float = 1, criticalFraction: float = 1):
        """This method creates a PorousFailureCriteria object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].materials[name].porousMetalPlasticity.PorousFailureCriteria.PorousFailureCriteriaaterials[name].porousMetalPlasticity.PorousFailureCriteria
            
        Parameters
        ----------
        fraction
            A Float specifying the void volume fraction at total failure, fF>0. The default value is 
            1.0. 
        criticalFraction
            A Float specifying the critical void volume fraction, fc≥0. The default value is 1.0. 

        Returns
        -------
        PorousFailureCriteria
            A :py:class:`~abaqus.Material.Plastic.Metal.Porous.PorousFailureCriteria.PorousFailureCriteria` object. 

        Raises
        ------
        RangeError
        """
        ...

    @abaqus_method_doc
    def setValues(self, *args, **kwargs):
        """This method modifies the PorousFailureCriteria object.

        Raises
        ------
        RangeError
        """
        ...
