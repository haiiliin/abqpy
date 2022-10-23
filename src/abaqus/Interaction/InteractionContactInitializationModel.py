from typing import Optional

from abqpy.decorators import abaqus_class_doc
from typing_extensions import Literal

from .StdInitialization import StdInitialization
from ..Model.ModelBase import ModelBase
from ..UtilityAndView.abaqusConstants import ADJUST
from ..UtilityAndView.abaqusConstants import abaqusConstants as C


@abaqus_class_doc
class InteractionContactInitializationModel(ModelBase):
    
    def StdInitialization(
        self,
        name: str,
        overclosureType: Literal[C.INTERFERENCE, C.ADJUST, C.CLEARANCE] = ADJUST,
        interferenceDistance: Optional[float] = None,
        clearanceDistance: Optional[float] = None,
        openingTolerance: Optional[float] = None,
        overclosureTolerance: Optional[float] = None,
    ) -> StdInitialization:
        """This method creates a StdInitialization object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].StdInitialization

        Parameters
        ----------
        name
            A String specifying the contact initialization repository key.
        overclosureType
            A SymbolicConstant specifying the type of overclosure to be defined. Possible values are
            ADJUST, INTERFERENCE, and CLEARANCE. The default value is ADJUST.
        interferenceDistance
            None or a Float specifying the interference distance. This argument is valid only when
            **overclosureType** = INTERFERENCE. The default value is None.
        clearanceDistance
            None or a Float specifying the initial clearance distance. This argument is valid only
            when **overclosureType** = CLEARANCE, and must be specified in that case. The default value
            is None.
        openingTolerance
            None or a Float specifying the distance tolerance within which initial openings will
            undergo strain-free adjustments. This argument is not valid when
            **overclosureType** = INTERFERENCE unless a value has been specified for
            **interferenceDistance**. The default value is None.
        overclosureTolerance
            None or a Float specifying the distance tolerance within which initial overclosures will
            undergo strain-free adjustments.. The default value is None.

        Returns
        -------
        StdInitialization
            A :py:class:`~abaqus.Interaction.StdInitialization.StdInitialization` object.

        Raises
        ------
        RangeError
        """
        self.contactInitializations[name] = contactInitialization = StdInitialization(
            name,
            overclosureType,
            interferenceDistance,
            clearanceDistance,
            openingTolerance,
            overclosureTolerance,
        )
        return contactInitialization
