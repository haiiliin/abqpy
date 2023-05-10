from __future__ import annotations

from typing import Dict, Optional, overload

from typing_extensions import Literal

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from ..UtilityAndView.abaqusConstants import SymbolicConstant
from ..UtilityAndView.abaqusConstants import abaqusConstants as C
from .HistoryOutput import HistoryOutput
from .HistoryPoint import HistoryPoint


@abaqus_class_doc
class HistoryRegion:
    """The HistoryRegion object contains history data for a single location in the model.

    .. note::
        This object can be accessed by::

            import odbAccess
            session.odbs[name].steps[name].historyRegions[name]
    """

    #: A SymbolicConstant specifying the position of the history output. Possible values are
    #: NODAL, INTEGRATION_POINT, WHOLE_ELEMENT, WHOLE_REGION, and WHOLE_MODEL.
    position: Optional[SymbolicConstant] = None

    #: A repository of HistoryOutput objects.
    historyOutputs: Dict[str, HistoryOutput] = {}

    #: A String specifying the name of the HistoryRegion object.
    name: str

    #: A String specifying the description of the HistoryRegion object.
    description: str

    #: A HistoryPoint object specifying the point to which the history data refer.
    point: HistoryPoint

    #: None or an OdbLoadCase object specifying the load case associated with the HistoryRegion
    #: object. The default value is None.
    loadCase: Optional[str] = None

    @abaqus_method_doc
    def __init__(
        self,
        name: str,
        description: str,
        point: HistoryPoint,
        loadCase: Optional[str] = None,
    ) -> None:
        """This method creates a HistoryRegion object.

        .. note::
            This function can be accessed by::

                session.odbs[name].steps[name].HistoryRegion

        Parameters
        ----------
        name
            A String specifying the name of the HistoryRegion object.
        description
            A String specifying the description of the HistoryRegion object.
        point
            A HistoryPoint object specifying the point to which the history data refer.
        loadCase
            None or an OdbLoadCase object specifying the load case associated with the HistoryRegion
            object. The default value is None.

        Returns
        -------
        HistoryRegion
            A HistoryRegion object.
        """
        ...

    @overload
    @abaqus_method_doc
    def getSubset(self, variableName: str) -> HistoryRegion:
        """This method returns a subset of the data in the HistoryRegion object.

        Parameters
        ----------
        variableName
            A String specifying the name of the output variable to return.

        Returns
        -------
        HistoryRegion
            A HistoryRegion object.
        """
        ...

    @overload
    @abaqus_method_doc
    def getSubset(self, start: float) -> HistoryRegion:
        """This method returns a subset of the data in the HistoryRegion object.

        Parameters
        ----------
        start
            A Float specifying the start of the subset. This is the same as the first item in the
            data array member of the HistoryOutput object.

        Returns
        -------
        HistoryRegion
            A HistoryRegion object.
        """
        ...

    @overload
    @abaqus_method_doc
    def getSubset(self, start: float, end: float) -> HistoryRegion:
        """This method returns a subset of the data in the HistoryRegion object.

        Parameters
        ----------
        start
            A Float specifying the start of the subset. This is the same as the first item in the
            data array member of the HistoryOutput object.
        end
            A Float specifying the end of the subset.

        Returns
        -------
        HistoryRegion
            A HistoryRegion object.
        """
        ...

    @abaqus_method_doc
    def getSubset(self, *args, **kwargs) -> HistoryRegion:
        ...

    def HistoryOutput(
        self,
        name: str,
        description: str,
        type: Literal[C.SCALAR],
        validInvariants: Optional[
            Literal[C.MISES, C.MAX_PRINCIPAL, C.MIN_PRINCIPAL, C.MID_PRINCIPAL, C.MAGNITUDE, C.TRESCA, C.INV3, C.PRESS]
        ] = None,
    ) -> HistoryOutput:
        """This method creates a HistoryOutput object.

        .. note::
            This function can be accessed by::

                session.odbs[name].steps[name].HistoryRegion

        Parameters
        ----------
        name
            A String specifying the output variable name.
        description
            A String specifying the output variable.
        type
            A SymbolicConstant specifying the output type. Only SCALAR is currently supported.
        validInvariants
            A sequence of SymbolicConstants specifying which invariants should be calculated for
            this field. Possible values are MAGNITUDE, MISES, TRESCA, PRESS, INV3, MAX_PRINCIPAL,
            MID_PRINCIPAL, and MIN_PRINCIPAL. The default value is an empty sequence.

        Returns
        -------
        HistoryOutput
            A HistoryOutput object.
        """
        self.historyOutputs[name] = historyOutput = HistoryOutput(name, description, type, validInvariants)
        return historyOutput
