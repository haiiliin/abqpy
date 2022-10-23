from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from .Profile import Profile


@abaqus_class_doc
class TProfile(Profile):
    """The TProfile object defines the properties of a T profile.
    The TProfile object is derived from the Profile object.

    .. note::
        This object can be accessed by::

            import section
            mdb.models[name].profiles[name]
            import odbSection
            session.odbs[name].profiles[name]

        The corresponding analysis keywords are:

        - BEAM SECTION
    """

    #: A String specifying the repository key.
    name: str

    #: A positive Float specifying the **b** dimension (flange width) of the T profile. For more
    #: information, see [Beam cross-section
    #: library](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEELMRefMap/simaelm-c-beamcrosssectlib.htm?ContextScope=all).
    b: float

    #: A positive Float specifying the **h** dimension (height) of the T profile.
    h: float

    #: A positive Float specifying the **l** dimension (offset of 1-axis from the edge of web) of
    #: the T profile.
    l: float

    #: A positive Float specifying the **tf** dimension (flange thickness) of the T profile (*tf
    #: < h*).
    tf: float

    #: A positive Float specifying the **tw** dimension (web thickness) of the T profile (*tw<
    #: b*).
    tw: float

    @abaqus_method_doc
    def __init__(self, name: str, b: float, h: float, l: float, tf: float, tw: float):
        """This method creates a TProfile object.

        .. note::
            This function can be accessed by::

                mdb.models[name].TProfile
                session.odbs[name].TProfile

        Parameters
        ----------
        name
            A String specifying the repository key.
        b
            A positive Float specifying the **b** dimension (flange width) of the T profile. For more
            information, see [Beam cross-section
            library](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEELMRefMap/simaelm-c-beamcrosssectlib.htm?ContextScope=all).
        h
            A positive Float specifying the **h** dimension (height) of the T profile.
        l
            A positive Float specifying the **l** dimension (offset of 1-axis from the edge of web) of
            the T profile.
        tf
            A positive Float specifying the **tf** dimension (flange thickness) of the T profile (*tf
            < h*).
        tw
            A positive Float specifying the **tw** dimension (web thickness) of the T profile (*tw<
            b*).

        Returns
        -------
        TProfile
            A :py:class:`~abaqus.BeamSectionProfile.TProfile.TProfile` object.

        Raises
        ------
        RangeError

        """
        super().__init__()

    @abaqus_method_doc
    def setValues(self, *args, **kwargs):
        """This method modifies the TProfile object.

        Raises
        ------
        RangeError

        """
        ...
