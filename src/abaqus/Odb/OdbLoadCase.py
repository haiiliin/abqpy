class OdbLoadCase:
    """The OdbLoadCase object describes a load case.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import odbAccess
        session.odbs[name].steps[name].frames[i].loadCase
        session.odbs[name].steps[name].historyRegions[name].loadCase
        session.odbs[name].steps[name].loadCases[name]
    """

    def __init__(self, name: str):
        """This method creates an OdbLoadCase object.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            session.odbs[*name*].steps[*name*].LoadCase

        Parameters
        ----------
        name
            A String specifying the name of the OdbLoadCase object.

        Returns
        -------
        An OdbLoadCase object.
        """
        pass
