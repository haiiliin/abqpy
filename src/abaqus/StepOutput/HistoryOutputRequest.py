from typing import Union, Optional, Tuple

from typing_extensions import Literal

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from ..Region.Region import Region
from ..UtilityAndView.SymbolicConstant import abaqusConstants as C
from ..UtilityAndView.abaqusConstants import (ALL, Boolean, DEFAULT,
                                              EVERY_TIME_INCREMENT, EXCLUDE, J_INTEGRAL,
                                              MODEL, MTS,
                                              OFF, PRESELECT, SymbolicConstant)


@abaqus_class_doc
class HistoryOutputRequest:
    """The HistoryOutputRequest object defines a history output request.

    .. note:: 
        This object can be accessed by::

            import step
            mdb.models[name].historyOutputRequests[name]

        The corresponding analysis keywords are:

        - CONTACT OUTPUT
        - ELEMENT OUTPUT
        - ENERGY OUTPUT
        - CONTACT OUTPUT
        - ELEMENT OUTPUT
        - ENERGY OUTPUT        
        - MODAL OUTPUT
        - CONTACT OUTPUT
        - ELEMENT OUTPUT
        - OUTPUT
        - RADIATION OUTPUT
    """

    #: A String specifying a bolt load from which output is requested. The default value is an
    #: empty string.
    boltLoad: str = ""

    #: The SymbolicConstant MODEL or a Region object specifying the region from which output is
    #: requested. The SymbolicConstant MODEL represents the whole model. The default value is
    #: MODEL.If the region is a surface region, the surface must lie within the general contact
    #: surface domain.
    region: Union[Literal[C.MODEL], Region] = MODEL

    #: The SymbolicConstant DEFAULT or a tuple of Ints specifying the section points for which
    #: output is requested. The default value is DEFAULT.
    sectionPoints: Union[Literal[C.DEFAULT], Tuple[int, ...]] = DEFAULT

    #: None or a tuple of Strings specifying the interaction names. The default value is
    #: None.The sequence can contain only one String.
    interactions: Optional[tuple] = None

    @abaqus_method_doc
    def __init__(
        self,
        name: str,
        createStepName: str,
        region: Union[Literal[C.MODEL], Region] = MODEL,
        variables: Union[Tuple[str, ...], Literal[C.PRESELECT, C.ALL]] = PRESELECT,
        frequency: Union[int, Literal[C.LAST_INCREMENT]] = 1,
        modes: Union[Literal[C.ALL], Tuple[int, ...]] = ALL,
        timeInterval: Union[
            Literal[C.EVERY_TIME_INCREMENT], float
        ] = EVERY_TIME_INCREMENT,
        numIntervals: int = 20,
        boltLoad: str = "",
        sectionPoints: Union[Literal[C.DEFAULT], Tuple[int, ...]] = DEFAULT,
        stepName: str = "",
        interactions: Optional[str] = None,
        contourIntegral: Optional[str] = None,
        numberOfContours: int = 0,
        stressInitializationStep: Optional[str] = None,
        contourType: Literal[C.J_INTEGRAL, C.C_INTEGRAL, C.T_STRESS, C.K_FACTORS] = J_INTEGRAL,
        kFactorDirection: Literal[C.MTS, C.MERR, C.K110] = MTS,
        rebar: Literal[C.EXCLUDE, C.INCLUDE, C.ONLY] = EXCLUDE,
        integratedOutputSection: str = "",
        springs: Optional[tuple] = None,
        filter: Optional[SymbolicConstant] = None,
        fasteners: str = "",
        assembledFastener: str = "",
        assembledFastenerSet: str = "",
        sensor: Boolean = OFF,
        useGlobal: Boolean = True,
    ) -> None:
        """This method creates a HistoryOutputRequest object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].HistoryOutputRequest

        Parameters
        ----------
        name
            A String specifying the repository key.
        createStepName
            A String specifying the name of the step in which the object is created.
        region
            The SymbolicConstant MODEL or a Region object specifying the region from which output is
            requested. The SymbolicConstant MODEL represents the whole model. The default value is
            MODEL.If the region is a surface region, the surface must lie within the general contact
            surface domain.
        variables
            A sequence of Strings specifying output request variable or component names, or the
            SymbolicConstant PRESELECT or ALL. PRESELECT represents all default output variables for
            the given step. ALL represents all valid output variables. The default value is
            PRESELECT.
        frequency
            The SymbolicConstant LAST_INCREMENT or an Int specifying the output frequency in
            increments. The default value is 1.
        modes
            The SymbolicConstant ALL or a sequence of Ints specifying a list of eigenmodes for which
            output is desired. The default value is ALL.
        timeInterval
            The SymbolicConstant EVERY_TIME_INCREMENT or a Float specifying the time interval at
            which the output states are to be written. The default value is EVERY_TIME_INCREMENT.
        numIntervals
            An Int specifying the number of intervals during the step at which output database
            states are to be written. The default value is 20.
        boltLoad
            A String specifying a bolt load from which output is requested. The default value is an
            empty string.
        sectionPoints
            The SymbolicConstant DEFAULT or a sequence of Ints specifying the section points for
            which output is requested. The default value is DEFAULT.
        stepName
            A String specifying the name of the step. The default value is an empty string.
        interactions
            None or a sequence of Strings specifying the interaction names. The default value is
            None.The sequence can contain only one String.
        contourIntegral
            A String specifying the contour integral name. The default value is None.
        numberOfContours
            An Int specifying the number of contour integrals to output for the contour integral
            object. The default value is 0.
        stressInitializationStep
            A String specifying the name of the stress initialization step. The default value is
            None.
        contourType
            A SymbolicConstant specifying the type of contour integral. Possible values are
            J_INTEGRAL, C_INTEGRAL, T_STRESS, and K_FACTORS. The default value is J_INTEGRAL.
        kFactorDirection
            A SymbolicConstant specifying the stress intensity factor direction. Possible values are
            MTS, MERR, and K110. The **kFactorDirection** argument is valid only if
            **contourType** = K_FACTORS. The default value is MTS.
        rebar
            A SymbolicConstant specifying whether output is requested for rebar. Possible values are
            EXCLUDE, INCLUDE, and ONLY. The default value is EXCLUDE.
        integratedOutputSection
            A String specifying the integrated output section. The default value is an empty string.
        springs
            A sequence of Strings specifying the springs/dashpots names. The default value is None.
            The sequence can contain only one String.
        filter
            The SymbolicConstant ANTIALIASING or a String specifying the name of an output filter
            object. The default value is None.
        fasteners
            A String specifying the fastener name. The default value is an empty string.
        assembledFastener
            A String specifying the assembled fastener name. The default value is an empty string.
        assembledFastenerSet
            A String specifying the set name from the model referenced by the assembled fastener,
            **assembledFastener**. The default value is an empty string.
        sensor
            A Boolean specifying whether to associate the output request with a sensor definition.
            The default value is OFF.
        useGlobal
            A Boolean specifying whether to output vector-valued nodal variables in the global
            directions. The default value is True.
        """
        ...

    @abaqus_method_doc
    def deactivate(self, stepName: str) -> None:
        """This method deactivates the history output request in the specified step and all
        subsequent steps.

        Parameters
        ----------
        stepName
            A String specifying the name of the step in which the history output request is
            deactivated.
        """
        ...

    @abaqus_method_doc
    def move(self, fromStepName: str, toStepName: str) -> None:
        """This method moves the history output request state object from one step to a different
        step.

        Parameters
        ----------
        fromStepName
            A String specifying the name of the step from which the history output request state is
            moved.
        toStepName
            A String specifying the name of the step to which the history output request state is
            moved.
        """
        ...

    @abaqus_method_doc
    def reset(self, stepName: str) -> None:
        """This method resets the history output request state of the specified step to the state
        of the previous step.

        Parameters
        ----------
        stepName
            A String specifying the name of the step in which the history output request state is
            reset.
        """
        ...

    @abaqus_method_doc
    def resume(self) -> None:
        """This method resumes the history output request that was previously suppressed."""
        ...

    @abaqus_method_doc
    def suppress(self) -> None:
        """This method suppresses the history output request."""
        ...

    @abaqus_method_doc
    def setValues(
        self,
        region: Union[Literal[C.MODEL], Region] = MODEL,
        variables: Union[Tuple[str, ...], Literal[C.PRESELECT, C.ALL]] = PRESELECT,
        frequency: Union[int, Literal[C.LAST_INCREMENT]] = 1,
        modes: Union[Literal[C.ALL], Tuple[int, ...]] = ALL,
        timeInterval: Union[
            Literal[C.EVERY_TIME_INCREMENT], float
        ] = EVERY_TIME_INCREMENT,
        numIntervals: int = 20,
        boltLoad: str = "",
        sectionPoints: Union[Literal[C.DEFAULT], Tuple[int, ...]] = DEFAULT,
        stepName: str = "",
        interactions: Optional[str] = None,
        contourIntegral: Optional[str] = None,
        numberOfContours: int = 0,
        stressInitializationStep: Optional[str] = None,
        contourType: Literal[C.J_INTEGRAL, C.C_INTEGRAL, C.T_STRESS, C.K_FACTORS] = J_INTEGRAL,
        kFactorDirection: Literal[C.MTS, C.MERR, C.K110] = MTS,
        rebar: Literal[C.EXCLUDE, C.INCLUDE, C.ONLY] = EXCLUDE,
        integratedOutputSection: str = "",
        springs: Optional[tuple] = None,
        filter: Optional[SymbolicConstant] = None,
        fasteners: str = "",
        assembledFastener: str = "",
        assembledFastenerSet: str = "",
        sensor: Boolean = OFF,
        useGlobal: Boolean = True,
    ) -> None:
        """This method modifies the data for an existing HistoryOutputRequest object in the step
        where it is created.

        Parameters
        ----------
        region
            The SymbolicConstant MODEL or a Region object specifying the region from which output is
            requested. The SymbolicConstant MODEL represents the whole model. The default value is
            MODEL.If the region is a surface region, the surface must lie within the general contact
            surface domain.
        variables
            A sequence of Strings specifying output request variable or component names, or the
            SymbolicConstant PRESELECT or ALL. PRESELECT represents all default output variables for
            the given step. ALL represents all valid output variables. The default value is
            PRESELECT.
        frequency
            The SymbolicConstant LAST_INCREMENT or an Int specifying the output frequency in
            increments. The default value is 1.
        modes
            The SymbolicConstant ALL or a sequence of Ints specifying a list of eigenmodes for which
            output is desired. The default value is ALL.
        timeInterval
            The SymbolicConstant EVERY_TIME_INCREMENT or a Float specifying the time interval at
            which the output states are to be written. The default value is EVERY_TIME_INCREMENT.
        numIntervals
            An Int specifying the number of intervals during the step at which output database
            states are to be written. The default value is 20.
        boltLoad
            A String specifying a bolt load from which output is requested. The default value is an
            empty string.
        sectionPoints
            The SymbolicConstant DEFAULT or a sequence of Ints specifying the section points for
            which output is requested. The default value is DEFAULT.
        stepName
            A String specifying the name of the step. The default value is an empty string.
        interactions
            None or a sequence of Strings specifying the interaction names. The default value is
            None.The sequence can contain only one String.
        contourIntegral
            A String specifying the contour integral name. The default value is None.
        numberOfContours
            An Int specifying the number of contour integrals to output for the contour integral
            object. The default value is 0.
        stressInitializationStep
            A String specifying the name of the stress initialization step. The default value is
            None.
        contourType
            A SymbolicConstant specifying the type of contour integral. Possible values are
            J_INTEGRAL, C_INTEGRAL, T_STRESS, and K_FACTORS. The default value is J_INTEGRAL.
        kFactorDirection
            A SymbolicConstant specifying the stress intensity factor direction. Possible values are
            MTS, MERR, and K110. The **kFactorDirection** argument is valid only if
            **contourType** = K_FACTORS. The default value is MTS.
        rebar
            A SymbolicConstant specifying whether output is requested for rebar. Possible values are
            EXCLUDE, INCLUDE, and ONLY. The default value is EXCLUDE.
        integratedOutputSection
            A String specifying the integrated output section. The default value is an empty string.
        springs
            A sequence of Strings specifying the springs/dashpots names. The default value is None.
            The sequence can contain only one String.
        filter
            The SymbolicConstant ANTIALIASING or a String specifying the name of an output filter
            object. The default value is None.
        fasteners
            A String specifying the fastener name. The default value is an empty string.
        assembledFastener
            A String specifying the assembled fastener name. The default value is an empty string.
        assembledFastenerSet
            A String specifying the set name from the model referenced by the assembled fastener,
            **assembledFastener**. The default value is an empty string.
        sensor
            A Boolean specifying whether to associate the output request with a sensor definition.
            The default value is OFF.
        useGlobal
            A Boolean specifying whether to output vector-valued nodal variables in the global
            directions. The default value is True.
        """
        ...

    @abaqus_method_doc
    def setValuesInStep(
        self,
        stepName: str,
        variables: Union[Tuple[str, ...], Literal[C.PRESELECT, C.ALL]] = ...,
        frequency: Union[int, Literal[C.LAST_INCREMENT]] = 1,
        modes: Union[Literal[C.ALL], Tuple[int, ...]] = ALL,
        timeInterval: Union[
            Literal[C.EVERY_TIME_INCREMENT], float
        ] = EVERY_TIME_INCREMENT,
        numIntervals: int = 20,
        timePoints: Optional[str] = None,
    ) -> None:
        """This method modifies the propagating data for an existing HistoryOutputRequest object in
        the specified step.

        Parameters
        ----------
        stepName
            A String specifying the name of the step in which the history output request is
            modified.
        variables
            A sequence of Strings specifying output request variable or component names or the
            SymbolicConstant PRESELECT or ALL. PRESELECT represents all default output variables for
            the given step. ALL represents all valid output variables.
        frequency
            The SymbolicConstant LAST_INCREMENT or an Int specifying the output frequency in
            increments. The default value is 1.
        modes
            The SymbolicConstant ALL or a sequence of Ints specifying a list of eigenmodes for which
            output is desired. The default value is ALL.
        timeInterval
            The SymbolicConstant EVERY_TIME_INCREMENT or a Float specifying the time interval at
            which the output states are to be written. The default value is EVERY_TIME_INCREMENT.
        numIntervals
            An Int specifying the number of intervals during the step at which output database
            states are to be written. The default value is 20.
        timePoints
            A String specifying the name of a time point object. The default value is equal to the
            number of intervals during the step at which output database states are to be written.
            The default value is None.
        """
        ...
