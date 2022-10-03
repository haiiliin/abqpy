from typing import Dict

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc


# Prevent circular import
class ErrorIndicatorResult:
    ...


@abaqus_class_doc
class RuleResult:
    """The RuleResult object contains result information corresponding to a RemeshingRule
    object for an adaptivity iteration.

    .. note:: 
        This object can be accessed by::

            import job
            mdb.adaptivityProcesses[name].iterations[i].ruleResults[name]
    """

    #: A String specifying the name of the Remeshing Rule to which these results correspond.
    name: str

    #: A repository of ErrorIndicatorResult objects specifying the calculated results from the
    #: sizing function corresponding to the error indicator variables for the Remeshing Rule.
    indicatorResults: Dict[str, ErrorIndicatorResult]

    #: An Int specifying the number of elements before remeshing in the region of the Remeshing
    #: Rule.
    numElems: int

    #: An Int specifying the number of elements that were constrained to the minimum element
    #: size by the Remeshing Rule.
    minSizeElemCount: int

    #: A sequence of Strings specifying the error indicator variables that have satisfied the
    #: Remeshing Rule.
    satisfiedVars: tuple = ()

    @abaqus_method_doc
    def __init__(
        self,
        name: str,
        indicatorResults: Dict[str, ErrorIndicatorResult],
        numElems: int,
        minSizeElemCount: int,
        satisfiedVars: tuple = (),
    ):
        """This method creates a RuleResult with data for a RemeshingRule for a given adaptivity
        iteration.

        .. note:: 
            This function can be accessed by::

                mdb.adaptivityProcesses[name].iterations[i].RuleResult

        Parameters
        ----------
        name
            A String specifying the name of the Remeshing Rule to which these results correspond.
        indicatorResults
            A repository of ErrorIndicatorResult objects specifying the calculated results from the
            sizing function corresponding to the error indicator variables for the Remeshing Rule.
        numElems
            An Int specifying the number of elements before remeshing in the region of the Remeshing
            Rule.
        minSizeElemCount
            An Int specifying the number of elements that were constrained to the minimum element
            size by the Remeshing Rule.
        satisfiedVars
            A sequence of Strings specifying the error indicator variables that have satisfied the
            Remeshing Rule.

        Returns
        -------
        RuleResult
            A :py:class:`~abaqus.Adaptivity.RuleResult.RuleResult` object.

        Raises
        ------
        AbaqusException
        """
        ...
