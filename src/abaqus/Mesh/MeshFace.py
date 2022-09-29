from typing import Optional

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc


@abaqus_class_doc
class MeshFace:
    """The MeshFace object refers to an element face. It has no constructor or members. A
    MeshFace object can be accessed via a MeshFaceArray or a repository on a part or part
    instance.

    .. note:: 
        This object can be accessed by::

            import part
            mdb.models[name].parts[name].elementFaces[i]
            mdb.models[name].parts[name].elemFaces[i]
            import assembly
            mdb.models[name].rootAssembly.allInstances[name].elementFaces[i]
            mdb.models[name].rootAssembly.allInstances[name].elemFaces[i]
            mdb.models[name].rootAssembly.instances[name].elementFaces[i]
            mdb.models[name].rootAssembly.instances[name].elemFaces[i]
    """

    #: An Int specifying an Int specifying the element label.
    label: Optional[int] = None

    #: An Int specifying a symbolic constant specifying the side of the element.
    face: Optional[int] = None

    @abaqus_method_doc
    def getElemEdges(self):
        """This method returns a tuple of unique element edges on the element face.

        Returns
        -------
        edges: Tuple[MeshEdge, ...]
            A tuple of MeshEdge objects
        """
        ...

    @abaqus_method_doc
    def getElements(self):
        """This method returns a tuple of elements that share the element face.

        Returns
        -------
        elements: Tuple[MeshElement, ...]
            A tuple of MeshElement objects
        """
        ...

    @abaqus_method_doc
    def getNodes(self):
        """This method returns a tuple of nodes on the element face.

        Returns
        -------
        nodes: Tuple[MeshNode, ...]
            A tuple of MeshNode objects
        """
        ...

    @abaqus_method_doc
    def getNodesByFaceAngle(self, angle: str):
        """This method returns an array of mesh node objects that are obtained by recursively
        finding adjacent element faces that are at an angle of less than or equal to the
        specified angle.

        Parameters
        ----------
        angle
            A float specifying the value of the face angle.

        Returns
        -------
        nodes: MeshNodeArray
            A :py:class:`~abaqus.Mesh.MeshNodeArray.MeshNodeArray` object, which is a sequence of MeshNode objects
        """
        ...

    @abaqus_method_doc
    def getNormal(self):
        """This method returns the normal direction for the element face.

        Returns
        -------
        normal: Tuple[float, ...]
            A tuple of 3 floats representing the unit normal vector. If the element face is
            collapsed such that a normal cannot be computed, a zero-length vector is returned.
        """
        ...

    @abaqus_method_doc
    def getElemFacesByFaceAngle(self, angle: str):
        """This method returns an array of element face objects that are obtained by recursively
        finding adjacent element faces that are at an angle of less than or equal to the
        specified angle.

        Parameters
        ----------
        angle
            A float specifying the value of the face angle.

        Returns
        -------
        faces: MeshFaceArray
            A :py:class:`~abaqus.Mesh.MeshFaceArray.MeshFaceArray` object, which is a sequence of MeshFace objects.
        """
        ...

    @abaqus_method_doc
    def getElemEdgesByFaceAngle(self, angle: str):
        """This method returns an array of element edge objects that are obtained by recursively
        finding adjacent element edges that are at an angle of less than or equal to the
        specified face angle.

        Parameters
        ----------
        angle
            A float specifying the value of the face angle in degrees.

        Returns
        -------
        edges: MeshEdgeArray
            A :py:class:`~abaqus.Mesh.MeshEdgeArray.MeshEdgeArray` object, which is a sequence of MeshEdge objects.
        """
        ...

    @abaqus_method_doc
    def getElementsByFaceAngle(self, angle: str):
        """This method returns an array of mesh Element objects that are obtained by recursively
        finding adjacent element faces that are at an angle of less than or equal to the
        specified angle.

        Parameters
        ----------
        angle
            A float specifying the value of the face angle.

        Returns
        -------
        elements: MeshElementArray
            A :py:class:`~abaqus.Mesh.MeshElementArray.MeshElementArray` object, which is a sequence of MeshElement objects.
        """
        ...

    @abaqus_method_doc
    def getElemFacesByLimitingAngle(self, angle: str):
        """This method returns an array of element edge objects that are obtained by recursively
        finding adjacent element faces that are at an angle of less than or equal to the
        specified face angle with the seed face.

        Parameters
        ----------
        angle
            A float specifying the value of the face angle in degrees.

        Returns
        -------
        faces: MeshFaceArray
            A :py:class:`~abaqus.Mesh.MeshFaceArray.MeshFaceArray` object, which is a sequence of MeshFace objects.
        """
        ...

    @abaqus_method_doc
    def getElementsViaTopology(self):
        """This method returns an array of mesh Element objects that are obtained by recursively
        finding adjacent elements via topology.

        Returns
        -------
        elements: MeshElementArray
            A :py:class:`~abaqus.Mesh.MeshElementArray.MeshElementArray` object, which is a sequence of MeshElement objects.
        """
        ...

    @abaqus_method_doc
    def getElemFacesByLayer(self, numLayers: str):
        """This method returns an array of element face objects, obtained by traversing shell
        elements or the exterior of a solid mesh, and recursively finding adjacent element faces
        by layer.

        Parameters
        ----------
        numLayers
            A int specifying the value of the number of layers.

        Returns
        -------
        faces: MeshFaceArray
            A :py:class:`~abaqus.Mesh.MeshFaceArray.MeshFaceArray` object, which is a sequence of MeshFace objects.
        """
        ...
