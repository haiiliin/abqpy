from typing import Union, Optional

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from typing_extensions import Literal

from .TransverseShearBeam import TransverseShearBeam
from .TransverseShearShell import TransverseShearShell
from ..Connector.ConnectorSection import ConnectorSection
from ..UtilityAndView.abaqusConstants import abaqusConstants as C


@abaqus_class_doc
class Section(ConnectorSection):
    @abaqus_method_doc
    def TransverseShearBeam(
        self,
        scfDefinition: Literal[C.VALUE, C.ANALYSIS_DEFAULT, C.COMPUTED],
        k23: Optional[float] = None,
        k13: Optional[float] = None,
        slendernessCompensation: Union[Literal[C.COMPUTED], float] = 0,
    ) -> TransverseShearBeam:
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
            A TransverseShearBeam object.
        """
        self.beamTransverseShear = transverseShearBeam = TransverseShearBeam(
            scfDefinition, k23, k13, slendernessCompensation
        )
        return transverseShearBeam

    @abaqus_method_doc
    def TransverseShearShell(self, k11: float, k22: float, k12: float) -> TransverseShearShell:
        """This method creates a TransverseShearShell object.

        .. note::
            This function can be accessed by::

                mdb.models[name].sections[name].TransverseShearShell
                session.odbs[name].sections[name].TransverseShearShell

        Parameters
        ----------
        k11
            A Float specifying the shear stiffness of the section in the first direction.
        k22
            A Float specifying the shear stiffness of the section in the second direction.
        k12
            A Float specifying the coupling term in the shear stiffness of the section.

        Returns
        -------
        TransverseShearShell
            A TransverseShearShell object.
        """
        self.transverseShear = transverseShearShell = TransverseShearShell(k11, k22, k12)
        return transverseShearShell
