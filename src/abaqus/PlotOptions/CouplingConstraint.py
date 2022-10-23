from abqpy.decorators import abaqus_class_doc, abaqus_method_doc


@abaqus_class_doc
class CouplingConstraint:
    """The CouplingConstraint object.

    .. note::
        This object can be accessed by::

            import visualization
            session.odbData[name].kinematicCouplings[i]
            session.odbData[name].distributingCouplings[i]
            session.odbData[name].shellSolidCouplings[i]
    """

    #: A String specifying the coupling name. This attribute is read-only.
    name: str = ""

    #: A String specifying the type of coupling. This attribute is read-only.
    type: str = ""

    @abaqus_method_doc
    def constraintData(self):
        """This method returns node numbers of the surface being controlled by the control point.

        Returns
        -------
        Tuple-of-Ints Dictionary specifying the node numbers on the controlled surface.
        """
        # TODO: Implement this method
        ...
