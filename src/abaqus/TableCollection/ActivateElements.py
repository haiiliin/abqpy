class ActivateElements:
    """The ActivateElements object is used turn on progressive element activation within a step
    definition.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        mdb.models[name].steps[name].activateElements[key]

    The corresponding analysis keywords are:

    - ActivateElements
            - ElementProgressiveActivation
    """

    def __init__(
        self,
        tableCollection: str,
        activation: str,
        eigenTimeConst: str = "",
        expansionTimeConstant: str = "",
    ):
        """This method creates an ActivateElements object.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            mdb.models[name].ActivateElements

        Parameters
        ----------
        tableCollection
            A String specifying the name of the tableCollection object.
        activation
            A string specifying the name of progressive element activation.
        eigenTimeConst
            A Double specifying the time constant used to ramp up the eigenstrains at element
            activation.
        expansionTimeConstant
            A Double specifying the time constant used to ramp up the thermal strains at element
            activation.

        Returns
        -------
        An ActivateElements object.

        Raises
        ------
        RangeError
        """
        pass

    def setValues(self, *args, **kwargs):
        """This method modifies the ActivateElements object.

        Returns
        -------

        Raises
        ------
        RangeError
        """
        pass
