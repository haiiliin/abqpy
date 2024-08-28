from __future__ import annotations

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from .Profile import Profile


@abaqus_class_doc
class HatProfile(Profile):
    """The HatProfile object defines the properties of a hat profile. The HatProfile object
    is derived from the Profile object.

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

    #: A positive Float specifying the l dimension (offset of 1–axis from the bottom flange surface) of the Hat
    #: profile. For more information, see Beam Cross-Section Library.
    l: float

    #: A positive Float specifying the h dimension (height) of the Hat profile.
    h: float

    #: A positive Float specifying the b dimension (bottom width) of the Hat profile.
    b: float

    #: A positive Float specifying the b1 dimension (upper flange width) of the Hat profile.
    b1: float

    #: A positive Float specifying the b2 dimension (lower flange width) of the Hat profile.
    b2: float

    #: A positive Float specifying the t1 dimension (upper flange thickness) of the Hat profile.
    t1: float

    #: A positive Float specifying the t2 dimension (lower flange thickness) of the Hat profile.
    t2: float

    #: A positive Float specifying the t3 dimension (web thickness) of the Hat profile.
    t3: float

    @abaqus_method_doc
    def __init__(
        self,
        name: str,
        l: float,
        h: float,
        b: float,
        b1: float,
        b2: float,
        t1: float,
        t2: float,
        t3: float,
    ):
        """This method creates a HatProfile object.

        .. note::
            This function can be accessed by::

                mdb.models[name].HatProfile
                session.odbs[name].HatProfile

        .. versionadded:: 2024

            The ``HatProfile`` class was added.

        Parameters
        ----------
        name
            A String specifying the repository key.
        l
            A positive Float specifying the l dimension (offset of 1–axis from the bottom flange surface) of the Hat
            profile. For more information, see Beam Cross-Section Library.
        h
            A positive Float specifying the h dimension (height) of the Hat profile.
        b
            A positive Float specifying the b dimension (bottom width) of the Hat profile.
        b1
            A positive Float specifying the b1 dimension (upper flange width) of the Hat profile.
        b2
            A positive Float specifying the b2 dimension (lower flange width) of the Hat profile.
        t1
            A positive Float specifying the t1 dimension (upper flange thickness) of the Hat profile.
        t2
            A positive Float specifying the t2 dimension (lower flange thickness) of the Hat profile.
        t3
            A positive Float specifying the t3 dimension (web thickness) of the Hat profile.

        Returns
        -------
        HatProfile
            An HatProfile object.

        Raises
        ------
        RangeError
        """
        super().__init__()

    @abaqus_method_doc
    def setValues(self, *args, **kwargs):
        """This method modifies the HatProfile object.

        Raises
        ------
        RangeError
        """
        ...
