from abqpy.decorators import abaqus_class_doc


@abaqus_class_doc
class MpcConstraint:
    """The MpcConstraint object.

    .. note::
        This object can be accessed by::

            import visualization
            session.odbData[name].multiPointConstraints[i]
    """

    #: A String specifying the multipoint constraint name. This attribute is read-only.
    name: str = ""

    def constraintData(self):
        """This method returns constraint data if any are associated with the object.

        Returns
        -------
        Sequence[float]
            A tuple containing coordinates of the nodes pertaining to the constraint.
        """
        # TODO: Implement this method
        ...
