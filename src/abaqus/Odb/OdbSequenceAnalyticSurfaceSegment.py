class OdbSequenceAnalyticSurfaceSegment:
    """A sequence of AnalyticSurfaceSegment describing an analytic surface profile.

    .. note:: 
        This object can be accessed by:

        .. code-block:: python

            import odbAccess
            session.odbs[name].parts[name].analyticSurface.segments
            session.odbs[name].rootAssembly.instances[name].analyticSurface.segments
            session.odbs[name].steps[name].frames[i].fieldOutputs[name].values[i].instance.analyticSurface.segments
    """

    def __init__(self):
        """This method creates a OdbSequenceAnalyticSurfaceSegment object.

        .. note:: 
            This function can be accessed by:

            .. code-block:: python

                odbAccess.AnalyticSurfaceProfile

        Returns
        -------
        OdbSequenceAnalyticSurfaceSegment
            An :py:class:`~abaqus.Odb.OdbSequenceAnalyticSurfaceSegment.OdbSequenceAnalyticSurfaceSegment` object.
        """
        pass

    def Start(self, origin: tuple):
        """This method adds a AnalyticSurfaceSegment describing the first segment of the surface
        profile.

        Parameters
        ----------
        origin
            A sequence of Floats specifying the coordinates of start point.
        """
        pass

    def Line(self, endPoint: tuple):
        """This method adds a AnalyticSurfaceSegment describing the line segment of the surface
        profile.

        Parameters
        ----------
        endPoint
            A sequence of Floats specifying the coordinates of end point.
        """
        pass

    def Circle(self, center: tuple, endPoint: tuple):
        """This method adds a AnalyticSurfaceSegment describing a circular segment of the surface
        profile.

        Parameters
        ----------
        center
            A sequence of Floats specifying the coordinates of center of the circular segment.
        endPoint
            A sequence of Floats specifying the coordinates of end point of the circular segment.
        """
        pass

    def Parabola(self, middlePoint: tuple, endPoint: tuple):
        """This method adds a AnalyticSurfaceSegment describing a parabolic segment of the surface
        profile.

        Parameters
        ----------
        middlePoint
            A sequence of Floats specifying the coordinates of middle point of the parabolic
            segment.
        endPoint
            A sequence of Floats specifying the coordinates of end point of the parabolic segment.
        """
        pass
