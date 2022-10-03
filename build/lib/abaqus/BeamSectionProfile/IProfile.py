from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from .Profile import Profile


@abaqus_class_doc
class IProfile(Profile):
    """The IProfile object defines the properties of an I profile.
    The IProfile object is derived from the Profile object.

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

    #: A Float specifying the **l** dimension (offset of 1-axis from the bottom flange surface)
    #: of the I profile. For more information, see [Beam cross-section
    #: library](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEELMRefMap/simaelm-c-beamcrosssectlib.htm?ContextScope=all).
    l: float

    #: A Float specifying the **h** dimension (height) of the I profile.
    h: float

    #: A Float specifying the **b1** dimension (bottom flange width) of the I profile.
    b1: float

    #: A Float specifying the **b2** dimension (top flange width) of the I profile.
    b2: float

    #: A Float specifying the **t1** dimension (bottom flange thickness) of the I profile.
    t1: float

    #: A Float specifying the **t2** dimension (top flange thickness) of the I profile.
    t2: float

    #: A Float specifying the **t3** dimension (web thickness) of the I profile.
    t3: float

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
    ):
        """This method creates an IProfile object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].IProfile
                session.odbs[name].IProfile

        Parameters
        ----------
        name
            A String specifying the repository key.
        l
            A Float specifying the **l** dimension (offset of 1-axis from the bottom flange surface)
            of the I profile. For more information, see [Beam cross-section
            library](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEELMRefMap/simaelm-c-beamcrosssectlib.htm?ContextScope=all).
        h
            A Float specifying the **h** dimension (height) of the I profile.
        b1
            A Float specifying the **b1** dimension (bottom flange width) of the I profile.
        b2
            A Float specifying the **b2** dimension (top flange width) of the I profile.
        t1
            A Float specifying the **t1** dimension (bottom flange thickness) of the I profile.
        t2
            A Float specifying the **t2** dimension (top flange thickness) of the I profile.
        t3
            A Float specifying the **t3** dimension (web thickness) of the I profile.

        Returns
        -------
        IProfile
            An :py:class:`~abaqus.BeamSectionProfile.IProfile.IProfile` object.

        Raises
        ------
        RangeError

        """
        super().__init__()

    @abaqus_method_doc
    def setValues(self, *args, **kwargs):
        """This method modifies the IProfile object.

        Raises
        ------
        RangeError

        """
        ...
