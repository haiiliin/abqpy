from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from .Profile import Profile


@abaqus_class_doc
class RectangularProfile(Profile):
    """The RectangularProfile object defines the properties of a solid rectangular profile.
    The RectangularProfile object is derived from the Profile object.

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

    #: A positive Float specifying the **a** dimension of the rectangular profile. For more
    #: information, see [Beam cross-section
    #: library](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEELMRefMap/simaelm-c-beamcrosssectlib.htm?ContextScope=all).
    a: float

    #: A positive Float specifying the **b** dimension of the rectangular profile.
    b: float

    @abaqus_method_doc
    def __init__(self, name: str, a: float, b: float):
        """This method creates a RectangularProfile object.

        .. note::
            This function can be accessed by::

                mdb.models[name].RectangularProfile
                session.odbs[name].RectangularProfile

        Parameters
        ----------
        name
            A String specifying the repository key.
        a
            A positive Float specifying the **a** dimension of the rectangular profile. For more
            information, see [Beam cross-section
            library](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEELMRefMap/simaelm-c-beamcrosssectlib.htm?ContextScope=all).
        b
            A positive Float specifying the **b** dimension of the rectangular profile.

        Returns
        -------
        RectangularProfile
            A :py:class:`~abaqus.BeamSectionProfile.RectangularProfile.RectangularProfile` object.

        Raises
        ------
        RangeError

        """
        super().__init__()

    @abaqus_method_doc
    def setValues(self, *args, **kwargs):
        """This method modifies the RectangularProfile object.

        Raises
        ------
        RangeError

        """
        ...
