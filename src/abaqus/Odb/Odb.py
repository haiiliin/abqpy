from typing_extensions import Literal

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from .OdbPart import OdbPart
from .OdbStep import OdbStep
from .SectionCategory import SectionCategory
from ..Amplitude.AmplitudeOdb import AmplitudeOdb
from ..BeamSectionProfile.BeamSectionProfileOdb import BeamSectionProfileOdb
from ..Canvas.Displayable import Displayable
from ..Filter.FilterOdb import FilterOdb
from ..Material.MaterialOdb import MaterialOdb
from ..UtilityAndView.SymbolicConstant import abaqusConstants as C


@abaqus_class_doc
class Odb(AmplitudeOdb, FilterOdb, MaterialOdb, BeamSectionProfileOdb, Displayable):
    """The Odb object is the in-memory representation of an output database (ODB) file.

    .. note:: 
        This object can be accessed by::

            import odbAccess
            session.odbs[name]
    """

    @abaqus_method_doc
    def Part(
        self,
        name: str,
        embeddedSpace: Literal[C.THREE_D, C.TWO_D_PLANAR, C.AXISYMMETRIC],
        type: Literal[C.DEFORMABLE_BODY, C.ANALYTIC_RIGID_SURFACE],
    ) -> OdbPart:
        """This method creates an OdbPart object. Nodes and elements are added to this object at a
        later stage.

        .. note:: 
            This function can be accessed by::

                session.odbs[name].Part

        Parameters
        ----------
        name
            A String specifying the part name.
        embeddedSpace
            A SymbolicConstant specifying the dimensionality of the Part object. Possible values are
            THREE_D, TWO_D_PLANAR, and AXISYMMETRIC.
        type
            A SymbolicConstant specifying the type of the Part object. Possible values are
            DEFORMABLE_BODY and ANALYTIC_RIGID_SURFACE.

        Returns
        -------
        OdbPart
            An :py:class:`~abaqus.Odb.OdbPart.OdbPart` object.
        """
        self.parts[name] = odbPart = OdbPart(name, embeddedSpace, type)
        return odbPart

    @abaqus_method_doc
    def Step(
        self,
        name: str,
        description: str,
        domain: Literal[C.TIME, C.FREQUENCY, C.ARC_LENGTH, C.MODAL],
        timePeriod: float = 0,
        previousStepName: str = "",
        procedure: str = "",
        totalTime: float = -1.0,
    ) -> OdbStep:
        """This method creates an OdbStep object.

        .. note:: 
            This function can be accessed by::

                session.odbs[name].Step

        Parameters
        ----------
        name
            A String specifying the repository key.
        description
            A String specifying the step description.
        domain
            A SymbolicConstant specifying the domain of the step. Possible values are TIME,
            FREQUENCY, ARC_LENGTH, and MODAL.The type of OdbFrame object that can be created for
            this step is based on the value of the **domain** argument.
        timePeriod
            A Float specifying the time period of the step. **timePeriod** is required if
            **domain** = TIME; otherwise, this argument is not applicable. The default value is 0.0.
        previousStepName
            A String specifying the preceding step. If **previousStepName** is the empty string, the
            last step in the repository is used. If **previousStepName** is not the last step, this
            will result in a change to the **previousStepName** member of the step that was in that
            position. A special value 'Initial' refers to the internal initial model step and may be
            used exclusively for inserting a new step at the first position before any other
            existing steps. The default value is an empty string.
        procedure
            A String specifying the step procedure. The default value is an empty string. The
            following is the list of valid procedures:
            
            - `*ANNEAL`
            - `*BUCKLE`
            - `*COMPLEX FREQUENCY`
            - `*COUPLED TEMPERATURE-DISPLACEMENT`
            - `*COUPLED TEMPERATURE-DISPLACEMENT, CETOL`
            - `*COUPLED TEMPERATURE-DISPLACEMENT, STEADY STATE`
            - `*COUPLED THERMAL-ELECTRICAL, STEADY STATE`
            - `*COUPLED THERMAL-ELECTRICAL`
            - `*COUPLED THERMAL-ELECTRICAL, DELTMX`
            - `*DYNAMIC`
            - `*DYNAMIC, DIRECT`
            - `*DYNAMIC, EXPLICIT`
            - `*DYNAMIC, SUBSPACE`
            - `*DYNAMIC TEMPERATURE-DISPLACEMENT, EXPLICT`
            - `*ELECTROMAGNETIC, HIGH FREQUENCY, TIME HARMONIC`
            - `*ELECTROMAGNETIC, LOW FREQUENCY, TIME DOMAIN`
            - `*ELECTROMAGNETIC, LOW FREQUENCY, TIME DOMAIN, DIRECT`
            - `*ELECTROMAGNETIC, LOW FREQUENCY, TIME HARMONIC`
            - `*FREQUENCY`
            - `*GEOSTATIC`
            - `*HEAT TRANSFER`
            - `*HEAT TRANSFER, DELTAMX=__`
            - `*HEAT TRANSFER, STEADY STATE`
            - `*MAGNETOSTATIC`
            - `*MAGNETOSTATIC, DIRECT`
            - `*MASS DIFFUSION`
            - `*MASS DIFFUSION, DCMAX=`
            - `*MASS DIFFUSION, STEADY STATE`
            - `*MODAL DYNAMIC`
            - `*RANDOM RESPONSE`
            - `*RESPONSE SPECTRUM`
            - `*SOILS`
            - `*SOILS, CETOL/UTOL`
            - `*SOILS, CONSOLIDATION`
            - `*SOILS, CONSOLIDATION, CETOL/UTOL`
            - `*STATIC`
            - `*STATIC, DIRECT`
            - `*STATIC, RIKS`
            - `*STEADY STATE DYNAMICS`
            - `*STEADY STATE TRANSPORT`
            - `*STEADY STATE TRANSPORT, DIRECT`
            - `*STEP PERTURBATION, *STATIC`
            - `*SUBSTRUCTURE GENERATE`
            - `*USA ADDDED MASS GENERATION`
            - `*VISCO`
        totalTime
            A Float specifying the analysis time spend in all the steps previous to this step. The
            default value is −1.0.

        Returns
        -------
        OdbStep
            An :py:class:`~abaqus.Odb.OdbStep.OdbStep` object.

        Raises
        ------
        ValueError: previousStepName is invalid
            If **previousStepName** is invalid.
        """
        self.steps[name] = odbStep = OdbStep(
            name,
            description,
            domain,
            timePeriod,
            previousStepName,
            procedure,
            totalTime,
        )
        return odbStep

    @abaqus_method_doc
    def SectionCategory(self, name: str, description: str) -> SectionCategory:
        """This method creates a SectionCategory object.

        .. note:: 
            This function can be accessed by::

                session.odbs[name].SectionCategory

        Parameters
        ----------
        name
            A String specifying the name of the category.
        description
            A String specifying the description of the category.

        Returns
        -------
        SectionCategory
            A :py:class:`~abaqus.Odb.SectionCategory.SectionCategory` object.
        """
        self.sectionCategories[name] = sectionCategory = SectionCategory(
            name, description
        )
        return sectionCategory
