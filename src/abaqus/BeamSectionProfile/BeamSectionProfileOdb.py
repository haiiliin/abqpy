from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from .ArbitraryProfile import ArbitraryProfile
from .BoxProfile import BoxProfile
from .CircularProfile import CircularProfile
from .GeneralizedProfile import GeneralizedProfile
from .HexagonalProfile import HexagonalProfile
from .IProfile import IProfile
from .LProfile import LProfile
from .PipeProfile import PipeProfile
from .RectangularProfile import RectangularProfile
from .TProfile import TProfile
from .TrapezoidalProfile import TrapezoidalProfile
from ..Odb.OdbBase import OdbBase
from ..UtilityAndView.abaqusConstants import Boolean


@abaqus_class_doc
class BeamSectionProfileOdb(OdbBase):
    """The Odb object is the in-memory representation of an output database (ODB) file.

    .. note::
        This object can be accessed by::

            import odbAccess
            session.odbs[name]
    """

    @abaqus_method_doc
    def ArbitraryProfile(self, name: str, table: tuple) -> ArbitraryProfile:
        """This method creates a ArbitraryProfile object.

        .. note::
            This function can be accessed by::

                mdb.models[name].ArbitraryProfile
                session.odbs[name].ArbitraryProfile

        Parameters
        ----------
        name
            A String specifying the repository key.
        table
            A sequence of sequences of Floats specifying the items described below.

        Returns
        -------
        ArbitraryProfile
            An :py:class:`~abaqus.BeamSectionProfile.ArbitraryProfile.ArbitraryProfile` object.

        Raises
        ------
        RangeError
        """
        self.profiles[name] = arbitraryProfile = ArbitraryProfile(name, table)
        return arbitraryProfile

    @abaqus_method_doc
    def BoxProfile(
        self,
        name: str,
        a: float,
        b: float,
        uniformThickness: Boolean,
        t1: float,
        t2: float = 0,
        t3: float = 0,
        t4: float = 0,
    ) -> BoxProfile:
        """This method creates a BoxProfile object.

        .. note::
            This function can be accessed by::

                mdb.models[name].BoxProfile
                session.odbs[name].BoxProfile

        Parameters
        ----------
        name
            A String specifying the repository key.
        a
            A Float specifying the **a** dimension of the box profile. For more information, see [Beam
            cross-section
            library](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEELMRefMap/simaelm-c-beamcrosssectlib.htm?ContextScope=all).
        b
            A Float specifying the **b** dimension of the box profile.
        uniformThickness
            A Boolean specifying whether the thickness is uniform.
        t1
            A Float specifying the uniform wall thickness if **uniformThickness** = ON, and the wall
            thickness of the first segment if **uniformThickness** = OFF.
        t2
            A Float specifying the wall thickness of the second segment. **t2** is required only when
            **uniformThickness** = OFF. The default value is 0.0.
        t3
            A Float specifying the wall thickness of the third segment. **t3** is required only when
            **uniformThickness** = OFF. The default value is 0.0.
        t4
            A Float specifying the wall thickness of the fourth segment. **t4** is required only when
            **uniformThickness** = OFF. The default value is 0.0.

        Returns
        -------
        BoxProfile
            A :py:class:`~abaqus.BeamSectionProfile.BoxProfile.BoxProfile` object.

        Raises
        ------
        RangeError
        """
        self.profiles[name] = boxProfile = BoxProfile(name, a, b, uniformThickness, t1, t2, t3, t4)
        return boxProfile

    @abaqus_method_doc
    def CircularProfile(self, name: str, r: float) -> CircularProfile:
        """This method creates a CircularProfile object.

        .. note::
            This function can be accessed by::

                mdb.models[name].CircularProfile
                session.odbs[name].CircularProfile

        Parameters
        ----------
        name
            A String specifying the repository key.
        r
            A positive Float specifying the **r** dimension (outer radius) of the circular profile.
            For more information, see [Beam cross-section
            library](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEELMRefMap/simaelm-c-beamcrosssectlib.htm?ContextScope=all).

        Returns
        -------
        CircularProfile
            A :py:class:`~abaqus.BeamSectionProfile.CircularProfile.CircularProfile` object.

        Raises
        ------
        RangeError
        """
        self.profiles[name] = circularProfile = CircularProfile(name, r)
        return circularProfile

    @abaqus_method_doc
    def GeneralizedProfile(
        self,
        name: str,
        area: float,
        i11: float,
        i12: float,
        i22: float,
        j: float,
        gammaO: float,
        gammaW: float,
    ) -> GeneralizedProfile:
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
        self.profiles[name] = generalizedProfile = GeneralizedProfile(name, area, i11, i12, i22, j, gammaO, gammaW)
        return generalizedProfile

    @abaqus_method_doc
    def HexagonalProfile(self, name: str, r: float, t: float) -> HexagonalProfile:
        """This method creates a HexagonalProfile object.

        .. note::
            This function can be accessed by::

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
        self.profiles[name] = hexagonalProfile = HexagonalProfile(name, r, t)
        return hexagonalProfile

    @abaqus_method_doc
    def IProfile(
        self,
        name: str,
        l: float,
        h: float,
        b1: float,
        b2: float,
        t1: float,
        t2: float,
        t3: float,
    ) -> IProfile:
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
        self.profiles[name] = iProfile = IProfile(name, l, h, b1, b2, t1, t2, t3)
        return iProfile

    @abaqus_method_doc
    def LProfile(self, name: str, a: float, b: float, t1: float, t2: float) -> LProfile:
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
        self.profiles[name] = lProfile = LProfile(name, a, b, t1, t2)
        return lProfile

    @abaqus_method_doc
    def PipeProfile(self, name: str, r: float, t: float) -> PipeProfile:
        """This method creates a PipeProfile object.

        .. note::
            This function can be accessed by::

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
        self.profiles[name] = pipeProfile = PipeProfile(name, r, t)
        return pipeProfile

    @abaqus_method_doc
    def RectangularProfile(self, name: str, a: float, b: float) -> RectangularProfile:
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
        self.profiles[name] = rectangularProfile = RectangularProfile(name, a, b)
        return rectangularProfile

    @abaqus_method_doc
    def TProfile(self, name: str, b: float, h: float, l: float, tf: float, tw: float) -> TProfile:
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
        self.profiles[name] = tProfile = TProfile(name, b, h, l, tf, tw)
        return tProfile

    @abaqus_method_doc
    def TrapezoidalProfile(self, name: str, a: float, b: float, c: float, d: float) -> TrapezoidalProfile:
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
        self.profiles[name] = trapezoidalProfile = TrapezoidalProfile(name, a, b, c, d)
        return trapezoidalProfile
