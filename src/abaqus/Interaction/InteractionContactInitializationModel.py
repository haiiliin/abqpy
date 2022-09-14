from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from .StdInitialization import StdInitialization
from ..Model.ModelBase import ModelBase
from ..UtilityAndView.abaqusConstants import *


@abaqus_class_doc
class InteractionContactInitializationModel(ModelBase):

    @abaqus_method_doc
    def StdInitialization(
        self,
        name: str,
        overclosureType: SymbolicConstant = ADJUST,
        interferenceDistance: float = None,
        clearanceDistance: float = None,
        openingTolerance: float = None,
        overclosureTolerance: float = None,
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
