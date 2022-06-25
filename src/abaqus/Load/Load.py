from ..Region.Region import Region


class Load:
    """The Load object is the abstract base type for other Load objects. The Load object has no
    explicit constructor. The methods and members of the Load object are common to all
    objects derived from Load.

    .. note:: 
        This object can be accessed by:

        .. code-block:: python

            import load
            mdb.models[name].loads[name]
    """

    #: A String specifying the load repository key.
    name: str = ""

    #: A :py:class:`~abaqus.Region.Region.Region` object specifying the region to which the load is applied.
    region: Region = Region()

    def deactivate(self, stepName: str):
        """This method deactivates the load in the specified step and all its subsequent steps.

        Parameters
        ----------
        stepName
            A String specifying the name of the step in which the load is deactivated.
        """
        pass

    def move(self, fromStepName: str, toStepName: str):
        """This method moves the load state object from one step to a different step.

        Parameters
        ----------
        fromStepName
            A String specifying the name of the step from which the load state is moved.
        toStepName
            A String specifying the name of the step to which the load state is moved.
        """
        pass

    def reset(self, stepName: str):
        """This method resets the load state of the specified step to the state of the previous
        general analysis step.

        Parameters
        ----------
        stepName
            A String specifying the name of the step in which the load state is reset.
        """
        pass

    def resume(self):
        """This method resumes the load that was previously suppressed."""
        pass

    def suppress(self):
        """This method suppresses the load."""
        pass

    def delete(self, indices: tuple):
        """This method allows you to delete existing loads.

        Parameters
        ----------
        indices
            A sequence of Ints specifying the index of each load to delete.
        """
        pass
