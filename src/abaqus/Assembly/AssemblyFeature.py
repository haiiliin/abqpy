from typing import Optional, Sequence

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from ..BasicGeometry.Face import Face
from ..Feature.Feature import Feature as FeatureBase
from ..Mesh.MeshFace import MeshFace
from ..UtilityAndView.abaqusConstants import (Boolean, OFF, PROJECT_BY_NUMBER, PROJECT_BY_PROXIMITY,
                                              SymbolicConstant)


@abaqus_class_doc
class AssemblyFeature(FeatureBase):
    """The following commands operate on Feature objects. For more information about the
    Feature object, see Feature object.

    .. note:: 
        This object can be accessed by::

            import assembly
    """

    @staticmethod
    @abaqus_method_doc
    def AttachmentLines(
        name: str,
        points: int,
        sourceFaces: Sequence[Face],
        sourceElementFaces: Sequence[MeshFace],
        targetFaces: Sequence[Face],
        targetElementFaces: Sequence[MeshFace],
        projectionMethod: SymbolicConstant = PROJECT_BY_PROXIMITY,
        projectionDirStartPt: Optional[float] = None,
        projectionDirEndPt: Optional[float] = None,
        sourceToTargetProjMethod: SymbolicConstant = PROJECT_BY_NUMBER,
        numProjections: str = "",
        projectionDistance: str = "",
        flipSourceToTargetDirection: Boolean = OFF,
        setName: str = "",
    ) -> "AssemblyFeature":
        """This method creates a Feature object by creating attachment lines between the given set
        of source and target faces. The given points are first projected onto the source faces
        using the specified projection method. The points are then projected normal to the
        source faces onto the target faces. The user can specify the number of projections or
        the length of projection vector for projection onto the target faces. The lines are then
        created between the source face and the closest target face. Subsequent lines are
        created between the target faces.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].rootAssembly.AttachmentLines

        Parameters
        ----------
        name
            A String specifying a unique Feature name.
        points
            A tuple of points. Each point can be a ConstrainedSketchVertex, Datum point, Reference point, an
            Attachment point, orphan mesh Node, or an Interesting point object.
        sourceFaces
            A sequence of Face objects specifying the geometry faces onto which the points are to be
            projected.
        sourceElementFaces
            A sequence of MeshFace objects specifying the orphan mesh element faces onto which the
            points are to be projected.
        targetFaces
            A sequence of Face objects specifying the geometry faces on which the attachment lines
            will terminate.
        targetElementFaces
            A sequence of MeshFace objects specifying the orphan mesh element faces on which the
            attachment lines will terminate.
        projectionMethod
            A SymbolicConstant specifying the method to be used to project onto source faces.
            Possible values are PROJECT_BY_PROXIMITY and PROJECT_BY_DIRECTION. The default value is
            PROJECT_BY_PROXIMITY.
        projectionDirStartPt
            A point specifying the start point of the projection direction to project onto source
            faces. The point can be a ConstrainedSketchVertex, Datum point, Reference point, Attachment point, orphan
            mesh Node, Interesting Point object, or a tuple of Floats representing the coordinates
            of a point.
        projectionDirEndPt
            A point specifying the end point of the projection direction to project onto source
            faces. The point can be a ConstrainedSketchVertex, Datum point, Reference point, Attachment point, orphan
            mesh Node, Interesting point object, or a tuple of Floats representing the coordinates
            of a point.
        sourceToTargetProjMethod
            A SymbolicConstant specifying the method to be used to project onto target faces.
            Possible values are PROJECT_BY_NUMBER and PROJECT_BY_DISTANCE. The default value is
            PROJECT_BY_NUMBER.
        numProjections
            An integer specifying the maximum number of layers each point should be projected onto
            when the source to target projection method is PROJECT_BY_NUMBER.
        projectionDistance
            A float specifying the maximum distance of the projection vector when the source to
            target projection method is PROJECT_BY_DISTANCE.
        flipSourceToTargetDirection
            A Boolean specifying whether the computed projection direction from the source to the
            target faces should be flipped.
        setName
            A String specifying a unique set name.

        Returns
        -------
        AssemblyFeature
            A :py:class:`~abaqus.Feature.Feature.Feature` object.
        """
        return AssemblyFeature()

    @staticmethod
    @abaqus_method_doc
    def Coaxial(movableAxis: str, fixedAxis: str, flip: Boolean) -> "AssemblyFeature":
        """This method moves an instance so that its selected face is coaxial with the selected
        face of a fixed instance.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].rootAssembly.AttachmentLines

        Parameters
        ----------
        movableAxis
            A cylindrical or conical Face on the part instance to be moved.
        fixedAxis
            A cylindrical or conical Face on the part instance that remains fixed.
        flip
            A Boolean specifying whether the axes are forward aligned (OFF) or reverse aligned (ON).

        Returns
        -------
        AssemblyFeature
            A :py:class:`~abaqus.Feature.Feature.Feature` object.

        Raises
        ------
        AbaqusException
        """
        return AssemblyFeature()

    @staticmethod
    @abaqus_method_doc
    def CoincidentPoint(movablePoint: str, fixedPoint: str) -> "AssemblyFeature":
        """This method moves an instance so that a specified point is coincident with a specified
        point of a fixed instance.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].rootAssembly.AttachmentLines

        Parameters
        ----------
        movablePoint
            A ConstrainedSketchVertex, a Datum point, or a ReferencePoint or a mesh node from an orphan mesh on the
            part instance to be moved.
        fixedPoint
            A ConstrainedSketchVertex, a Datum point, or a ReferencePoint or a mesh node from an orphan mesh on the
            part instance to remain fixed.

        Returns
        -------
        feature: AssemblyFeature
            A :py:class:`~abaqus.Feature.Feature.Feature` object
        """
        return AssemblyFeature()

    @staticmethod
    @abaqus_method_doc
    def EdgeToEdge(
        movableAxis: str, fixedAxis: str, flip: Boolean, clearance: float
    ) -> "AssemblyFeature":
        """This method moves an instance so that its edge is parallel to an edge of a fixed
        instance.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].rootAssembly.AttachmentLines

        Parameters
        ----------
        movableAxis
            A straight Edge, a Datum axis, or an element edge from an orphan mesh on the part
            instance to be moved.
        fixedAxis
            A straight Edge, a Datum axis, or an element edge from an orphan mesh on the part
            instance to remain fixed.
        flip
            A Boolean specifying whether the edges are forward aligned (OFF) or reverse aligned
            (ON).
        clearance
            A Float specifying the distance between the two edges (for two-dimensional and
            axisymmetric instances only).

        Returns
        -------
        AssemblyFeature
            A Feature Object.

        Raises
        ------
        AbaqusException
        """
        return AssemblyFeature()

    @staticmethod
    @abaqus_method_doc
    def FaceToFace(
        movablePlane: str, fixedPlane: str, flip: Boolean, clearance: float
    ) -> "AssemblyFeature":
        """This method moves an instance so that its face is coincident with a face of a fixed
        instance.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].rootAssembly.AttachmentLines

        Parameters
        ----------
        movablePlane
            A planar face, a Datum plane, or a face from an orphan mesh on the part instance to be
            moved.
        fixedPlane
            A planar face, a Datum plane, or a face from an orphan mesh on the part instance to
            remain fixed.
        flip
            A Boolean specifying whether the normals to the faces are forward aligned (OFF) or
            reverse aligned (ON).
        clearance
            A Float specifying the distance between the two faces.

        Returns
        -------
        AssemblyFeature
            A Feature Object.

        Raises
        ------
        AbaqusException
        """
        return AssemblyFeature()

    @staticmethod
    @abaqus_method_doc
    def ParallelCsys(movableCsys: str, fixedCsys: str) -> "AssemblyFeature":
        """This method moves an instance so that its Datum coordinate system is parallel to a Datum
        coordinate system of a fixed instance.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].rootAssembly.AttachmentLines

        Parameters
        ----------
        movableCsys
            A Datum coordinate system on the part instance to be moved.
        fixedCsys
            A Datum coordinate system on the part instance to remain fixed.

        Returns
        -------
        AssemblyFeature
            A :py:class:`~abaqus.Feature.Feature.Feature` object.

        Raises
        ------
        AbaqusException
        """
        return AssemblyFeature()

    @staticmethod
    @abaqus_method_doc
    def ParallelEdge(movableAxis: str, fixedAxis: str, flip: Boolean) -> "AssemblyFeature":
        """This method moves an instance so that its edge is parallel to an edge of a fixed
        instance.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].rootAssembly.AttachmentLines

        Parameters
        ----------
        movableAxis
            A straight Edge, a Datum axis, or an element edge from an orphan mesh on the part
            instance to be moved.
        fixedAxis
            A straight Edge, a Datum axis, or an element edge from an orphan mesh on the part
            instance to remain fixed.
        flip
            A Boolean specifying whether the edges are forward aligned (OFF) or reverse aligned
            (ON).

        Returns
        -------
        AssemblyFeature
            A :py:class:`~abaqus.Feature.Feature.Feature` object.

        Raises
        ------
        AbaqusException
        """
        return AssemblyFeature()

    @staticmethod
    @abaqus_method_doc
    def ParallelFace(movablePlane: str, fixedPlane: str, flip: Boolean) -> "AssemblyFeature":
        """This method moves an instance so that its face is parallel to a face of a fixed
        instance.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].rootAssembly.AttachmentLines

        Parameters
        ----------
        movablePlane
            A planar face, a Datum plane, or a face from an orphan mesh on the part instance to be
            moved.
        fixedPlane
            A planar face, a Datum plane, or a face from an orphan mesh on the part instance to
            remain fixed.
        flip
            A Boolean specifying whether the normals to the faces are forward aligned (OFF) or
            reverse aligned (ON).

        Returns
        -------
        AssemblyFeature
            A :py:class:`~abaqus.Feature.Feature.Feature` object.

        Raises
        ------
        AbaqusException
        """
        return AssemblyFeature()
