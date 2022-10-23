from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from .Profile import Profile


@abaqus_class_doc
class LProfile(Profile):
    """The LProfile object defines the properties of a L profile.
    The LProfile object is derived from the Profile object.

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

    #: A positive Float specifying the **a** dimension (flange length) of the L profile. For more
    #: information, see [Beam cross-section
    #: library](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEELMRefMap/simaelm-c-beamcrosssectlib.htm?ContextScope=all).
    a: float

    #: A positive Float specifying the **b** dimension (flange length) of the L profile.
    b: float

    #: A positive Float specifying the **t1** dimension (flange thickness) of the L profile (*t1
    #: < b*).
    t1: float

    #: A positive Float specifying the **t2** dimension (flange thickness) of the L profile (*t2<
    #: a*).
    t2: float

    @abaqus_method_doc
    def __init__(self, name: str, a: float, b: float, t1: float, t2: float):
        """This method creates a LProfile object.

        .. note::
            This function can be accessed by::

                mdb.models[name].LProfile
                session.odbs[name].LProfile

        Parameters
        ----------
        name
            A String specifying the repository key.
        a
            A positive Float specifying the **a** dimension (flange length) of the L profile. For more
            information, see [Beam cross-section
            library](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEELMRefMap/simaelm-c-beamcrosssectlib.htm?ContextScope=all).
        b
            A positive Float specifying the **b** dimension (flange length) of the L profile.
        t1
            A positive Float specifying the **t1** dimension (flange thickness) of the L profile (*t1
            < b*).
        t2
            A positive Float specifying the **t2** dimension (flange thickness) of the L profile (*t2<
            a*).

        Returns
        -------
        LProfile
            A :py:class:`~abaqus.BeamSectionProfile.LProfile.LProfile` object.

        Raises
        ------
        RangeError

        """
        super().__init__()

    @abaqus_method_doc
    def setValues(self, *args, **kwargs):
        """This method modifies the LProfile object.

        Raises
        ------
        RangeError

        """
        ...
