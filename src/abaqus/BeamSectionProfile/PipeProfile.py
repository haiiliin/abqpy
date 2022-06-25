from .Profile import Profile


class PipeProfile(Profile):
    """The PipeProfile object defines the properties of a circular pipe profile.
    The PipeProfile object is derived from the Profile object.

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

    #: A Float specifying the outer radius of the pipe. For more information, see [Beam
    #: cross-section
    #: library](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEELMRefMap/simaelm-c-beamcrosssectlib.htm?ContextScope=all).
    r: float

    #: A Float specifying the wall thickness of the pipe.
    t: float

    def __init__(self, name: str, r: float, t: float):
        """This method creates a PipeProfile object.

        .. note:: 
            This function can be accessed by:

            .. code-block:: python

                mdb.models[name].PipeProfile
                session.odbs[name].PipeProfile

        Parameters
        ----------
        name
            A String specifying the repository key.
        r
            A Float specifying the outer radius of the pipe. For more information, see [Beam
            cross-section
            library](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEELMRefMap/simaelm-c-beamcrosssectlib.htm?ContextScope=all).
        t
            A Float specifying the wall thickness of the pipe.

        Returns
        -------
        PipeProfile
            A :py:class:`~abaqus.BeamSectionProfile.PipeProfile.PipeProfile` object.

        Raises
        ------
        RangeError

        """
        super().__init__()
        pass

    def setValues(self, *args, **kwargs):
        """This method modifies the PipeProfile object.

        Raises
        ------
        RangeError

        """
        pass
