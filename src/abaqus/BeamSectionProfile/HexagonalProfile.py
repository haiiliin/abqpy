from .Profile import Profile


class HexagonalProfile(Profile):
    """The HexagonalProfile object defines the properties of a hexagonal profile.
    The HexagonalProfile object is derived from the Profile object.

    .. note:: 
        This object can be accessed by:

        .. code-block:: python

            import section
            mdb.models[name].profiles[name]
            import odbSection
            session.odbs[name].profiles[name]

        The corresponding analysis keywords are:

        - BEAM SECTION
    """

    #: A String specifying the repository key.
    name: str

    #: A positive Float specifying the **r** dimension (outer radius) of the hexagonal profile.
    #: For more information, see [Beam cross-section
    #: library](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEELMRefMap/simaelm-c-beamcrosssectlib.htm?ContextScope=all).
    r: float

    #: A positive Float specifying the **t** dimension (wall thickness) of the hexagonal profile,
    #: *t < (sqrt(3)/2)r*.
    t: float

    def __init__(self, name: str, r: float, t: float):
        """This method creates a HexagonalProfile object.

        .. note:: 
            This function can be accessed by:

            .. code-block:: python

                mdb.models[name].HexagonalProfile
                session.odbs[name].HexagonalProfile

        Parameters
        ----------
        name
            A String specifying the repository key.
        r
            A positive Float specifying the **r** dimension (outer radius) of the hexagonal profile.
            For more information, see [Beam cross-section
            library](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEELMRefMap/simaelm-c-beamcrosssectlib.htm?ContextScope=all).
        t
            A positive Float specifying the **t** dimension (wall thickness) of the hexagonal profile,
            *t < (sqrt(3)/2)r*.

        Returns
        -------
        HexagonalProfile
            A :py:class:`~abaqus.BeamSectionProfile.HexagonalProfile.HexagonalProfile` object.

        Raises
        ------
        RangeError

        """
        super().__init__()
        pass

    def setValues(self, *args, **kwargs):
        """This method modifies the HexagonalProfile object.

        Raises
        ------
        RangeError

        """
        pass
