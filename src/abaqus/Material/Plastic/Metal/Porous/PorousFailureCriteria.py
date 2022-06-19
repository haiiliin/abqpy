class PorousFailureCriteria:
    """The PorousFailureCriteria object specifies the material failure criteria for a porous
    metal.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import material
        mdb.models[name].materials[name].porousMetalPlasticity.porousFailureCriteria
        import odbMaterial
        session.odbs[name].materials[name].porousMetalPlasticity.porousFailureCriteria

    The corresponding analysis keywords are:

    - POROUS FAILURE CRITERIA

    """

    def __init__(self, fraction: float = 1, criticalFraction: float = 1):
        """This method creates a PorousFailureCriteria object.

        Notes
        -----
            This function can be accessed by:
            
            .. code-block:: python
            
                mdb.models[name].materials[name].porousMetalPlasticity\
            - .PorousFailureCriteria
                session.odbs[name].materials[name].porousMetalPlasticity\
            - .PorousFailureCriteria
        
        Parameters
        ----------
        fraction
            A Float specifying the void volume fraction at total failure, fF>0. The default value is 
            1.0. 
        criticalFraction
            A Float specifying the critical void volume fraction, fc≥0. The default value is 1.0. 

        Returns
        -------
            A PorousFailureCriteria object. 

        Raises
        ------
        RangeError
        """
        pass

    def setValues(self):
        """This method modifies the PorousFailureCriteria object.

        Raises
        ------
        RangeError
        """
        pass
