from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from .Profile import Profile


@abaqus_class_doc
class GeneralizedProfile(Profile):
    """The GeneralizedProfile object defines the properties of a profile via its area, moment
    of inertia, etc.
    The GeneralizedProfile object is derived from the Profile object.

    .. note::
        This object can be accessed by::

            import section
            mdb.models[name].profiles[name]
            import odbSection
            session.odbs[name].profiles[name]

        The corresponding analysis keywords are:

        - BEAM GENERAL SECTION
    """

    #: A String specifying the repository key.
    name: str

    #: A Float specifying the cross-sectional area for the profile.
    area: float

    #: A Float specifying the moment of inertia for bending about the 1-axis, I11I11.
    i11: float

    #: A Float specifying the moment of inertia for cross bending, I12I12.
    i12: float

    #: A Float specifying the moment of inertia for bending about the 2-axis, I22I22.
    i22: float

    #: A Float specifying the torsional constant, JJ.
    j: float

    #: A Float specifying the sectorial moment, Γ0Γ0.
    gammaO: float

    #: A Float specifying the warping constant, ΓWΓW.
    gammaW: float

    @abaqus_method_doc
    def __init__(
        self,
        name: str,
        area: float,
        i11: float,
        i12: float,
        i22: float,
        j: float,
        gammaO: float,
        gammaW: float,
    ):
        """This method creates a GeneralizedProfile object.

        .. note::
            This function can be accessed by::

                mdb.models[name].GeneralizedProfile
                session.odbs[name].GeneralizedProfile

        Parameters
        ----------
        name
            A String specifying the repository key.
        area
            A Float specifying the cross-sectional area for the profile.
        i11
            A Float specifying the moment of inertia for bending about the 1-axis, I11I11.
        i12
            A Float specifying the moment of inertia for cross bending, I12I12.
        i22
            A Float specifying the moment of inertia for bending about the 2-axis, I22I22.
        j
            A Float specifying the torsional constant, JJ.
        gammaO
            A Float specifying the sectorial moment, Γ0Γ0.
        gammaW
            A Float specifying the warping constant, ΓWΓW.

        Returns
        -------
        GeneralizedProfile
            A :py:class:`~abaqus.BeamSectionProfile.GeneralizedProfile.GeneralizedProfile` object.

        Raises
        ------
        RangeError

        """
        super().__init__()

    @abaqus_method_doc
    def setValues(self, *args, **kwargs):
        """This method modifies the GeneralizedProfile object.

        Raises
        ------
        RangeError

        """
        ...
