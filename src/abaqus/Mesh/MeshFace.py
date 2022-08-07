class MeshFace:
    """The MeshFace object refers to an element face. It has no constructor or members. A
    MeshFace object can be accessed via a MeshFaceArray or a repository on a part or part
    instance.

    .. note:: 
        This object can be accessed by:

        .. code-block:: python

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
    label: int = None

    #: An Int specifying a symbolic constant specifying the side of the element.
    face: int = None

    def getElemEdges(self):
        """This method returns a tuple of unique element edges on the element face.

        Returns
        -------
        edges: tuple[MeshEdge]
            A tuple of MeshEdge objects
        """
        pass

    def getElements(self):
        """This method returns a tuple of elements that share the element face.

        Returns
        -------
        elements: tuple[MeshElement]
            A tuple of MeshElement objects
        """
        pass

    def getNodes(self):
        """This method returns a tuple of nodes on the element face.

        Returns
        -------
        nodes: tuple[MeshNode]
            A tuple of MeshNode objects
        """
        pass

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
        pass

    def getNormal(self):
        """This method returns the normal direction for the element face.

        Returns
        -------
        normal: tuple[float, ...]
            A tuple of 3 floats representing the unit normal vector. If the element face is
            collapsed such that a normal cannot be computed, a zero-length vector is returned.
        """
        pass

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
        pass

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
        pass

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
        pass

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
        pass

    def getElementsViaTopology(self):
        """This method returns an array of mesh Element objects that are obtained by recursively
        finding adjacent elements via topology.

        Returns
        -------
        elements: MeshElementArray
            A :py:class:`~abaqus.Mesh.MeshElementArray.MeshElementArray` object, which is a sequence of MeshElement objects.
        """
        pass

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
        pass
