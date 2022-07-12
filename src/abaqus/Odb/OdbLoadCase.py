class OdbLoadCase:
    """The OdbLoadCase object describes a load case.

    .. note:: 
        This object can be accessed by:

        .. code-block:: python

            import odbAccess
            session.odbs[name].steps[name].frames[i].loadCase
            session.odbs[name].steps[name].historyRegions[name].loadCase
            session.odbs[name].steps[name].loadCases[name]
    """

    #: A String specifying the name of the OdbLoadCase object.
    name: str

    def __init__(self, name: str):
        """This method creates an OdbLoadCase object.

        .. note:: 
            This function can be accessed by:

            .. code-block:: python

                session.odbs[name].steps[name].LoadCase

        Parameters
        ----------
        name
            A String specifying the name of the OdbLoadCase object.

        Returns
        -------
        OdbLoadCase
            An :py:class:`~abaqus.Odb.OdbLoadCase.OdbLoadCase` object.
        """
        pass
