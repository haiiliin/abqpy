from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

@abaqus_class_doc
class Interaction:
    """The Interaction object is the abstract base type for other Interaction objects. The
    Interaction object has no explicit constructor. Each of the Interaction objects has the
    following methods:
    - deactivate
    - move
    - reset
    - resume
    - suppress
    - delete
    The methods are described below.

    .. note:: 
        This object can be accessed by::

            import interaction
            mdb.models[name].interactions[name]
    """

    #: A String specifying the repository key.
    name: str = ""

    @abaqus_method_doc
    def deactivate(self, stepName: str):
        """This method deactivates the interaction in the specified step and all its subsequent
        steps.

        Parameters
        ----------
        stepName
            A String specifying the name of the step in which the interaction is deactivated.
        """
        ...

    @abaqus_method_doc
    def move(self, fromStepName: str, toStepName: str):
        """This method moves an interaction from one step to another.

        Parameters
        ----------
        fromStepName
            A String specifying the name of the step from which to move the interaction.
        toStepName
            A String specifying the name of the step to which to move the interaction.
        """
        ...

    @abaqus_method_doc
    def reset(self, stepName: str):
        """This method reactivates an interaction that was deactivated previously. The reset method
        is available during the step in which the interaction was deactivated originally.

        Parameters
        ----------
        stepName
            A String specifying the name of the step in which the interaction is reactivated.
        """
        ...

    @abaqus_method_doc
    def resume(self):
        """This method resumes an interaction that was previously suppressed."""
        ...

    @abaqus_method_doc
    def suppress(self):
        """This method suppresses an interaction."""
        ...

    @abaqus_method_doc
    def delete(self, indices: tuple):
        """This method allows you to delete existing interactions.

        Parameters
        ----------
        indices
            A sequence of Ints specifying the index of each interaction to delete.
        """
        ...
