from .RuleResult import RuleResult


class ErrorIndicatorResult(RuleResult):
    """The ErrorIndicatorResult object contains result information corresponding to an error
    indicator variable in a RemeshingRule object for an adaptivity iteration.

    .. note:: 
        This object can be accessed by:

        .. code-block:: python

            import job
            mdb.adaptivityProcesses[name].iterations[i].ruleResults[name].indicatorResults[name]
    """

    #: A String specifying the name of the error indicator variable to which these results
    #: correspond.
    name: str

    #: A String-to-Float Dictionary specifying the calculated results from the sizing function
    #: corresponding to the error indicator variable represented by this ErrorIndicatorResult.
    results: str

    def __init__(self, name: str, results: str):
        """This method creates an ErrorIndicatorResult with data for an error indicator variable in
        a RemeshingRule for a given adaptivity iteration.

        .. note:: 
            This function can be accessed by:

            .. code-block:: python

                mdb.adaptivityProcesses[name].iterations[i].ruleResults[name].ErrorIndicatorResult

        Parameters
        ----------
        name
            A String specifying the name of the error indicator variable to which these results
            correspond.
        results
            A String-to-Float Dictionary specifying the calculated results from the sizing function
            corresponding to the error indicator variable represented by this ErrorIndicatorResult.

        Returns
        -------
        ErrorIndicatorResult
            An :py:class:`~abaqus.Adaptivity.ErrorIndicatorResult.ErrorIndicatorResult` object.

        Raises
        ------
        AbaqusException
        """
        pass
