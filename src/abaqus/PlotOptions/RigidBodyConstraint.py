from abqpy.decorators import abaqus_class_doc, abaqus_method_doc


@abaqus_class_doc
class RigidBodyConstraint:
    """The RigidBodyConstraint object.

    .. note::
        This object can be accessed by::

            import visualization
            session.odbData[name].rigidbodies[i]
    """

    #: A String specifying the rigidbody constraint name. This attribute is read-only.
    name: str = ""

    @abaqus_method_doc
    def constraintData(self):
        """This method returns constraint data if any are associated with the object.

        Returns
        -------
        str
            A String Value: NONE in the absence of constraint data.
        """
        # TODO: Implement this method
        ...
