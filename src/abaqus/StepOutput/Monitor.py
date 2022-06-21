from abaqusConstants import *


class Monitor:
    """The Monitor object defines a degree of freedom to monitor.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import step
        mdb.models[name].steps[name].monitor

    The corresponding analysis keywords are:

    - MONITOR
    """

    def __init__(self, node: str, dof: SymbolicConstant, frequency: int):
        """This method creates a request for a degree of freedom to be monitored in a general or
        modal procedure.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            mdb.models[name].steps[name].Monitor

        Parameters
        ----------
        node
            A String specifying the name of the region to be monitored.
        dof
            A SymbolicConstant specifying the degree of freedom to be monitored at the node.
            Possible values are:

            - U1
            - U2
            - U3
            - UR1
            - UR2
            - UR3
            - WARP
            - FLUID_PRESSURE
            - ELECTRICAL_POTENTIAL
            - NT11
            - NT30
            - NN11
            - NN30
            
            The NT identifiers are not available for mass diffusion. The NN identifiers are
            available only for mass diffusion.
        frequency
            An Int specifying the output frequency in increments. This argument is valid only for an
            Abaqus/Standard analysis.

        Returns
        -------
            A Monitor object.

        Raises
        ------
        RangeError
        """
        pass

    def setValues(self, *args, **kwargs):
        """This method modifies the Monitor object.

        Raises
        ------
        RangeError
        """
        pass
