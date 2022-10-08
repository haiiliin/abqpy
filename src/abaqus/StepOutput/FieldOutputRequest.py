from typing import Union, Optional, Sequence

from typing_extensions import Literal

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from ..Region.Region import Region
from ..UtilityAndView.SymbolicConstant import abaqusConstants as C
from ..UtilityAndView.abaqusConstants import (ALL, Boolean,
                                              DEFAULT, EVERY_TIME_INCREMENT, EXCLUDE,
                                              INTEGRATION_POINTS, MODEL,
                                              NODES, OFF, ON, PRESELECT, SPECIFIED)


@abaqus_class_doc
class FieldOutputRequest:
    """The FieldOutputRequest object defines a field output request.

    .. note:: 
        This object can be accessed by::

            import step
            mdb.models[name].fieldOutputRequests[name]

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

    #: A String specifying a bolt load from which output is requested.
    boltLoad: str = ""

    #: The SymbolicConstant MODEL or a Region object specifying the region from which output is
    #: requested. The SymbolicConstant MODEL represents the whole model. The default value is
    #: MODEL.
    region: Union[Literal[C.MODEL], Region] = MODEL

    #: None or a tuple of Strings specifying the interaction names. The default value is
    #: None.The sequence can contain only one String.
    interactions: Optional[tuple] = None

    @abaqus_method_doc
    def __init__(
        self,
        name: str,
        createStepName: str,
        region: Union[Literal[C.MODEL], Region] = MODEL,
        variables: Union[Sequence[str], Literal[C.PRESELECT, C.ALL]] = PRESELECT,
        frequency: Union[int, Literal[C.LAST_INCREMENT]] = 1,
        modes: Union[Literal[C.ALL], Sequence[int]] = ALL,
        timeInterval: Union[
            Literal[C.EVERY_TIME_INCREMENT], float
        ] = EVERY_TIME_INCREMENT,
        numIntervals: int = 20,
        timeMarks: Boolean = OFF,
        boltLoad: str = "",
        sectionPoints: Union[Sequence[int], Literal[C.DEFAULT]] = DEFAULT,
        interactions: Optional[str] = None,
        rebar: Literal[C.EXCLUDE, C.INCLUDE, C.ONLY] = EXCLUDE,
        filter: Union[Literal[C.ANTIALIASING], str, None] = None,
        directions: Boolean = ON,
        fasteners: str = "",
        assembledFastener: str = "",
        assembledFastenerSet: str = "",
        exteriorOnly: Boolean = OFF,
        layupNames: str = "",
        layupLocationMethod: str = SPECIFIED,
        outputAtPlyTop: Boolean = False,
        outputAtPlyMid: Boolean = True,
        outputAtPlyBottom: Boolean = False,
        position: Literal[
            C.INTEGRATION_POINTS, C.AVERAGED_AT_NODES, C.CENTROIDAL, C.NODES
        ] = INTEGRATION_POINTS,
    ) -> None:
        """This method creates a FieldOutputRequest object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].FieldOutputRequest

        Parameters
        ----------
        name
            A String specifying the repository key.
        createStepName
            A String specifying the name of the step in which the object is created.
        region
            The SymbolicConstant MODEL or a Region object specifying the region from which output is
            requested. The SymbolicConstant MODEL represents the whole model. The default value is
            MODEL.
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
        timeMarks
            A Boolean specifying when to write results to the output database. OFF indicates that
            output is written immediately after the time dictated by the specified number of
            intervals. ON indicates that output is written at the exact times dictated by the
            specified number of intervals. The default value is OFF.
        boltLoad
            A String specifying a bolt load from which output is requested.
        sectionPoints
            The SymbolicConstant DEFAULT or a sequence of Ints specifying the section points for
            which output requested. The default is DEFAULT.
        interactions
            None or a sequence of Strings specifying the interaction names. The default value is
            None.The sequence can contain only one String.
        rebar
            A SymbolicConstant specifying whether output is requested for rebar. Possible values are
            EXCLUDE, INCLUDE, and ONLY. The default value is EXCLUDE.
        filter
            The SymbolicConstant ANTIALIASING or a String specifying the name of an output filter
            object. The default value is None.
        directions
            A Boolean specifying whether to output directions of the local material coordinate
            system. The default value is ON.
        fasteners
            A String specifying the fastener name. The default value is an empty string.
        assembledFastener
            A String specifying the assembled fastener name. The default value is an empty string.
        assembledFastenerSet
            A String specifying the set name from the model referenced by the assembled fastener,
            **assembledFastener**. The default value is an empty string.
        exteriorOnly
            A Boolean specifying whether the output domain is restricted to the exterior of the
            model. This argument is only valid if **region** = MODEL. The default value is OFF.
        layupNames
            A List of Composite Layer Names.
        layupLocationMethod
            A Symbolic constant specifying the method used to indicate the output locations for
            composite layups. Possible values are ALL_LOCATIONS, SPECIFIED and TYPED_IN. The default
            value is SPECIFIED.
        outputAtPlyTop
            A Boolean specifying whether to output at the ply top section point. The default value
            is False.
        outputAtPlyMid
            A Boolean specifying whether to output at the ply mid section point. The default value
            is True.
        outputAtPlyBottom
            A Boolean specifying whether to output at the ply bottom section point. The default
            value is False.
        position
            A SymbolicConstant specifying the position on an element where output needs to be
            written. Possible values are INTEGRATION_POINTS, AVERAGED_AT_NODES, CENTROIDAL, and
            NODES. The default value is INTEGRATION_POINTS.
        """
        ...

    @abaqus_method_doc
    def deactivate(self, stepName: str) -> None:
        """This method deactivates the field output request in the specified step and all its
        subsequent steps.

        Parameters
        ----------
        stepName
            A String specifying the name of the step in which the field output request is
            deactivated.
        """
        ...

    @abaqus_method_doc
    def move(self, fromStepName: str, toStepName: str) -> None:
        """This method moves the field output request state object from one step to a different
        step.

        Parameters
        ----------
        fromStepName
            A String specifying the name of the step from which the field output request state is
            moved.
        toStepName
            A String specifying the name of the step to which the field output request state is
            moved.
        """
        ...

    @abaqus_method_doc
    def reset(self, stepName: str) -> None:
        """This method resets the field output request state of the specified step to the state of
        the previous step.

        Parameters
        ----------
        stepName
            A String specifying the name of the step in which the field output request state is
            reset.
        """
        ...

    @abaqus_method_doc
    def resume(self) -> None:
        """This method resumes the field output request that was previously suppressed."""
        ...

    @abaqus_method_doc
    def suppress(self) -> None:
        """This method suppresses the field output request."""
        ...

    @abaqus_method_doc
    def setValues(
        self,
        region: Union[Literal[C.MODEL], Region] = MODEL,
        variables: Union[Sequence[str], Literal[C.PRESELECT, C.ALL]] = PRESELECT,
        frequency: Union[int, Literal[C.LAST_INCREMENT]] = 1,
        modes: Union[Literal[C.ALL], int] = ALL,
        timeInterval: Union[
            Literal[C.EVERY_TIME_INCREMENT], float
        ] = EVERY_TIME_INCREMENT,
        numIntervals: int = 20,
        timeMarks: Boolean = OFF,
        boltLoad: str = "",
        sectionPoints: Union[int, Literal[C.DEFAULT]] = DEFAULT,
        interactions: Optional[str] = None,
        rebar: Literal[C.EXCLUDE, C.INCLUDE, C.ONLY] = EXCLUDE,
        filter: Union[Literal[C.ANTIALIASING], str, None] = None,
        directions: Boolean = ON,
        fasteners: str = "",
        assembledFastener: str = "",
        assembledFastenerSet: str = "",
        exteriorOnly: Boolean = OFF,
        layupNames: str = "",
        layupLocationMethod: str = SPECIFIED,
        outputAtPlyTop: Boolean = False,
        outputAtPlyMid: Boolean = True,
        outputAtPlyBottom: Boolean = False,
        position: Literal[
            C.INTEGRATION_POINTS, C.AVERAGED_AT_NODES, C.CENTROIDAL, NODES
        ] = INTEGRATION_POINTS,
    ) -> None:
        """This method modifies the data for an existing FieldOutputRequest object in the step
        where it is created.

        Parameters
        ----------
        region
            The SymbolicConstant MODEL or a Region object specifying the region from which output is
            requested. The SymbolicConstant MODEL represents the whole model. The default value is
            MODEL.
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
        timeMarks
            A Boolean specifying when to write results to the output database. OFF indicates that
            output is written immediately after the time dictated by the specified number of
            intervals. ON indicates that output is written at the exact times dictated by the
            specified number of intervals. The default value is OFF.
        boltLoad
            A String specifying a bolt load from which output is requested.
        sectionPoints
            The SymbolicConstant DEFAULT or a sequence of Ints specifying the section points for
            which output requested. The default is DEFAULT.
        interactions
            None or a sequence of Strings specifying the interaction names. The default value is
            None.The sequence can contain only one String.
        rebar
            A SymbolicConstant specifying whether output is requested for rebar. Possible values are
            EXCLUDE, INCLUDE, and ONLY. The default value is EXCLUDE.
        filter
            The SymbolicConstant ANTIALIASING or a String specifying the name of an output filter
            object. The default value is None.
        directions
            A Boolean specifying whether to output directions of the local material coordinate
            system. The default value is ON.
        fasteners
            A String specifying the fastener name. The default value is an empty string.
        assembledFastener
            A String specifying the assembled fastener name. The default value is an empty string.
        assembledFastenerSet
            A String specifying the set name from the model referenced by the assembled fastener,
            **assembledFastener**. The default value is an empty string.
        exteriorOnly
            A Boolean specifying whether the output domain is restricted to the exterior of the
            model. This argument is only valid if **region** = MODEL. The default value is OFF.
        layupNames
            A List of Composite Layer Names.
        layupLocationMethod
            A Symbolic constant specifying the method used to indicate the output locations for
            composite layups. Possible values are ALL_LOCATIONS, SPECIFIED and TYPED_IN. The default
            value is SPECIFIED.
        outputAtPlyTop
            A Boolean specifying whether to output at the ply top section point. The default value
            is False.
        outputAtPlyMid
            A Boolean specifying whether to output at the ply mid section point. The default value
            is True.
        outputAtPlyBottom
            A Boolean specifying whether to output at the ply bottom section point. The default
            value is False.
        position
            A SymbolicConstant specifying the position on an element where output needs to be
            written. Possible values are INTEGRATION_POINTS, AVERAGED_AT_NODES, CENTROIDAL, and
            NODES. The default value is INTEGRATION_POINTS.
        """
        ...

    @abaqus_method_doc
    def setValuesInStep(
        self,
        stepName: str,
        variables: Union[Sequence[str], Literal[C.PRESELECT, C.ALL], None] = None,
        frequency: Union[int, Literal[C.LAST_INCREMENT]] = 1,
        modes: Union[Literal[C.ALL], int] = ALL,
        timeInterval: Union[
            Literal[C.EVERY_TIME_INCREMENT], float
        ] = EVERY_TIME_INCREMENT,
        numIntervals: int = 20,
        timePoints: Optional[str] = None,
        timeMarks: Boolean = OFF,
    ) -> None:
        """This method modifies the propagating data for an existing FieldOutputRequest object in
        the specified step.

        Parameters
        ----------
        stepName
            A String specifying the name of the step in which the field output request is modified.
        variables
            A sequence of Strings specifying output request variable or component names, or the
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
            An Int equal to the number of intervals during the step at which output database states
            are to be written. The default value is 20.
        timePoints
            A String specifying the name of a time point object. The default value is equal to the
            number of intervals during the step at which output database states are to be written.
            The default value is None.
        timeMarks
            A Boolean specifying when to write results to the output database. The default value is
            OFF.
        """
        ...
