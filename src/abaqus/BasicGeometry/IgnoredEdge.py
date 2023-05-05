from typing import Optional, Tuple

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc


@abaqus_class_doc
class IgnoredEdge:
    """An IgnoredEdge object is a one-dimensional region of geometry that has been abstracted away by a virtual
    topology feature.

    .. note::
        This object can be accessed by::

            import part
            mdb.models[name].parts[name].ignoredEdges[i]
            import assembly
            mdb.models[name].rootAssembly.allInstances[name].ignoredEdges[i]
            mdb.models[name].rootAssembly.instances[name].ignoredEdges[i]
    """

    #: An Int specifying the index of the IgnoredEdge in the IgnoredEdgeArray.
    index: Optional[int] = None

    #: A tuple of Floats specifying the **X**, **Y**, and **Z** coordinates of a point located on
    #: the edge.
    pointOn: Optional[float] = None

    @abaqus_method_doc
    def getSize(self, printResults: str = True):
        """This method returns a Float indicating the length of the edge.

        Parameters
        ----------
        printResults
            A Bool specifying whether verbose output is printed. The default is True.

        Returns
        -------
        float
            A Float.
        """
        ...

    @abaqus_method_doc
    def getRadius(self):
        """This method returns the radius of a circular IgnoredEdge object.

        Returns
        -------
        float
            A Float specifying the radius.

        Raises
        ------
        The given IgnoredEdge object is not circular
        """
        ...

    @abaqus_method_doc
    def getCurvature(self, parameter: float, point: Tuple[float, float, float]):
        """This method returns curvature information at a location on the IgnoredEdge object.

        Parameters
        ----------
        parameter
            A Float specifying the normalized parameter location on the IgnoredEdge where the
            curvature is to be computed. This argument is mutually exclusive with the argument
            **point**.
        point
            A tuple of **X**, **Y**, and **Z** coordinates of a point at which the curvature is to be
            computed. If **point** does not lie on the IgnoredEdge an attempt is made to project it
            onto the IgnoredEdge and use the projected point.

        Returns
        -------
        dict
            A dictionary with keys 'evaluationPoint', 'curvature', 'radius', 'tangent'. Where
            'evaluationPoint' specifies the location at which the curvature was computed.
            'curvature' specifies the curvature vector at that location. 'radius' is the Radius of
            curvature and 'tangent' specifies the tangent to the IgnoredEdge at that location.

        Raises
        ------
        The given IgnoredEdge is straight
        """
        ...
