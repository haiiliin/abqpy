from __future__ import annotations

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from .Profile import Profile


@abaqus_class_doc
class ChannelProfile(Profile):
    """The ChannelProfile object defines the properties of a channel profile. The ChannelProfile object
    is derived from the Profile object.

    .. note::
        This object can be accessed by::

            import section
            mdb.models[name].profiles[name]
            import odbSection
            session.odbs[name].profiles[name]

        The corresponding analysis keywords are:

        - BEAM SECTION

    .. versionadded:: 2024
        The ``ChannelProfile`` class was added.
    """

    #: A String specifying the repository key.
    name: str

    #: A positive Float specifying the l dimension (offset of 1–axis from the bottom flange surface) of the Channel
    #: profile. For more information, see Beam Cross-Section Library.
    l: float

    #: A positive Float specifying the h dimension (height) of the Channel profile.
    h: float

    #: A positive Float specifying the b1 dimension (lower flange width) of the Channel profile.
    b1: float

    #: A positive Float specifying the b2 dimension (upper flange width) of the Channel profile.
    b2: float

    #: A positive Float specifying the t1 dimension (lower flange thickness) of the Channel profile.
    t1: float

    #: A positive Float specifying the t2 dimension (upper flange thickness) of the Channel profile.
    t2: float

    #: A positive Float specifying the t3 dimension (web thickness) of the Channel profile.
    t3: float

    #: A positive Float specifying the o dimension (offset of 2–axis from the left edge of web) of the Channel
    #: profile.
    o: float

    @abaqus_method_doc
    def __init__(
        self,
        name: str,
        l: float,
        h: float,
        b1: float,
        b2: float,
        t1: float,
        t2: float,
        t3: float,
        o: float,
    ):
        """This method creates a ChannelProfile object.

        .. note::
            This function can be accessed by::

                mdb.models[name].ChannelProfile
                session.odbs[name].ChannelProfile

        Parameters
        ----------
        name
            A String specifying the repository key.
        l
            A positive Float specifying the l dimension (offset of 1–axis from the bottom flange surface) of the Channel
            profile. For more information, see Beam Cross-Section Library.
        h
            A positive Float specifying the h dimension (height) of the Channel profile.
        b1
            A positive Float specifying the b1 dimension (lower flange width) of the Channel profile.
        b2
            A positive Float specifying the b2 dimension (upper flange width) of the Channel profile.
        t1
            A positive Float specifying the t1 dimension (lower flange thickness) of the Channel profile.
        t2
            A positive Float specifying the t2 dimension (upper flange thickness) of the Channel profile.
        t3
            A positive Float specifying the t3 dimension (web thickness) of the Channel profile.
        o
            A positive Float specifying the o dimension (offset of 2–axis from the left edge of web) of the Channel
            profile.

        Returns
        -------
        ChannelProfile
            An ChannelProfile object.

        Raises
        ------
        RangeError
        """
        super().__init__()

    @abaqus_method_doc
    def setValues(self, *args, **kwargs):
        """This method modifies the ChannelProfile object.

        Raises
        ------
        RangeError
        """
        ...
