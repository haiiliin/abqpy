class MpcConstraint:
    """The MpcConstraint object.

    .. note:: 
        This object can be accessed by:

        .. code-block:: python

            import visualization
            session.odbData[name].multiPointConstraints[i]
    """

    #: A String specifying the multipoint constraint name. This attribute is read-only.
    name: str = ""

    def constraintData(self):
        """This method returns constraint data if any are associated with the object.

        Returns
        -------
        tuple[float, ...]
            A tuple containing coordinates of the nodes pertaining to the constraint.
        """
        pass
