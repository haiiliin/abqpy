from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

@abaqus_class_doc
class TieConstraint:
    """The TieConstraint object.

    .. note:: 
        This object can be accessed by::

            import visualization
            session.odbData[name].ties[i]
    """

    #: A String specifying the tie constraint name. This attribute is read-only.
    name: str = ""

    @abaqus_method_doc
    def constraintData(self):
        """This method returns constraint data if any are associated with the object

        Returns
        -------
        Tuple[float, ...]
            A tuple containing coordinates of the nodes pertaining to the constraint.
        """
        # TODO: Implement this method
        ...
