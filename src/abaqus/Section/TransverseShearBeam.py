from typing import Union, Optional

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from ..UtilityAndView.abaqusConstants import SymbolicConstant


@abaqus_class_doc
class TransverseShearBeam:
    """The TransverseShearBeam object defines the transverse shear stiffness properties of a beam section.

    .. note:: 
        This object can be accessed by::

            import section
            mdb.models[name].sections[name].beamTransverseShear
            import odbSection
            session.odbs[name].sections[name].beamTransverseShear

        The corresponding analysis keywords are:

        - TRANSVERSE SHEAR STIFFNESS
    """

    #: A SymbolicConstant specifying how slenderness compensation factor of the section is
    #: given. Possible values are ANALYSIS_DEFAULT, COMPUTED, and VALUE.
    scfDefinition: SymbolicConstant

    #: None or a Float specifying the k23 shear stiffness of the section. The default value is
    #: None.
    k23: Optional[float] = None

    #: None or a Float specifying the k13 shear stiffness of the section. The default value is
    #: None.
    k13: Optional[float] = None

    #: The SymbolicConstant COMPUTED or a Float specifying the slenderness compensation factor
    #: of the section. The default value is 0.25.
    slendernessCompensation: Union[SymbolicConstant, float] = 0

    @abaqus_method_doc
    def __init__(
        self,
        scfDefinition: SymbolicConstant,
        k23: Optional[float] = None,
        k13: Optional[float] = None,
        slendernessCompensation: Union[SymbolicConstant, float] = 0,
    ):
        """This method creates a TransverseShearBeam object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].sections[name].TransverseShearBeam
                session.odbs[name].sections[name].TransverseShearBeam

        Parameters
        ----------
        scfDefinition
            A SymbolicConstant specifying how slenderness compensation factor of the section is
            given. Possible values are ANALYSIS_DEFAULT, COMPUTED, and VALUE.
        k23
            None or a Float specifying the k23 shear stiffness of the section. The default value is
            None.
        k13
            None or a Float specifying the k13 shear stiffness of the section. The default value is
            None.
        slendernessCompensation
            The SymbolicConstant COMPUTED or a Float specifying the slenderness compensation factor
            of the section. The default value is 0.25.

        Returns
        -------
        TransverseShearBeam
            A :py:class:`~abaqus.Section.TransverseShearBeam.TransverseShearBeam` object.
        """
        ...

    @abaqus_method_doc
    def setValues(self, *args, **kwargs):
        """This method modifies the TransverseShearBeam object."""
        ...
