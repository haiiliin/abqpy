from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from .Profile import Profile


@abaqus_class_doc
class TrapezoidalProfile(Profile):
    """The TrapezoidalProfile object defines the properties of a trapezoidal profile.
    The TrapezoidalProfile object is derived from the Profile object.

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

    #: A positive Float specifying the **a** dimension of the Trapezoidal profile. For more
    #: information, see [Beam cross-section
    #: library](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEELMRefMap/simaelm-c-beamcrosssectlib.htm?ContextScope=all).
    a: float

    #: A positive Float specifying the **b** dimension of the Trapezoidal profile.
    b: float

    #: A positive Float specifying the **c** dimension of the Trapezoidal profile.
    c: float

    #: A Float specifying the **d** dimension of the Trapezoidal profile.
    d: float

    @abaqus_method_doc
    def __init__(self, name: str, a: float, b: float, c: float, d: float):
        """This method creates a TrapezoidalProfile object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].TrapezoidalProfile
                session.odbs[name].TrapezoidalProfile

        Parameters
        ----------
        name
            A String specifying the repository key.
        a
            A positive Float specifying the **a** dimension of the Trapezoidal profile. For more
            information, see [Beam cross-section
            library](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEELMRefMap/simaelm-c-beamcrosssectlib.htm?ContextScope=all).
        b
            A positive Float specifying the **b** dimension of the Trapezoidal profile.
        c
            A positive Float specifying the **c** dimension of the Trapezoidal profile.
        d
            A Float specifying the **d** dimension of the Trapezoidal profile.

        Returns
        -------
        TrapezoidalProfile
            A :py:class:`~abaqus.BeamSectionProfile.TrapezoidalProfile.TrapezoidalProfile` object.

        Raises
        ------
        RangeError

        """
        super().__init__()

    @abaqus_method_doc
    def setValues(self, *args, **kwargs):
        """This method modifies the TrapezoidalProfile object.

        Raises
        ------
        RangeError

        """
        ...
