from __future__ import annotations

from typing import Union, List, Tuple, Sequence, Dict

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from .MeshNode import MeshNode


@abaqus_class_doc
class MeshNodeArray(List[MeshNode]):
    """The MeshNodeArray is a sequence of MeshNode objects.

    .. note::
        This object can be accessed by::

            import part
            mdb.models[name].parts[name].allInternalSets[name].nodes
            mdb.models[name].parts[name].allInternalSurfaces[name].nodes
            mdb.models[name].parts[name].allSets[name].nodes
            mdb.models[name].parts[name].allSurfaces[name].nodes
            mdb.models[name].parts[name].nodes
            mdb.models[name].parts[name].retainedNodes
            mdb.models[name].parts[name].sets[name].nodes
            mdb.models[name].parts[name].surfaces[name].nodes
            import assembly
            mdb.models[name].rootAssembly.allInstances[name].nodes
            mdb.models[name].rootAssembly.allInstances[name].sets[name].nodes
            mdb.models[name].rootAssembly.allInstances[name].surfaces[name].nodes
            mdb.models[name].rootAssembly.allInternalSets[name].nodes
            mdb.models[name].rootAssembly.allInternalSurfaces[name].nodes
            mdb.models[name].rootAssembly.allSets[name].nodes
            mdb.models[name].rootAssembly.allSurfaces[name].nodes
            mdb.models[name].rootAssembly.instances[name].nodes
            mdb.models[name].rootAssembly.instances[name].sets[name].nodes
            mdb.models[name].rootAssembly.instances[name].surfaces[name].nodes
            mdb.models[name].rootAssembly.modelInstances[i].nodes
            mdb.models[name].rootAssembly.modelInstances[i].sets[name].nodes
            mdb.models[name].rootAssembly.modelInstances[i].surfaces[name].nodes
            mdb.models[name].rootAssembly.nodes
            mdb.models[name].rootAssembly.sets[name].nodes
            mdb.models[name].rootAssembly.surfaces[name].nodes
    """

    @abaqus_method_doc
    def __init__(self, nodes: List[MeshNode]) -> None:
        """This method creates a MeshNodeArray object.

        .. note::
            This function can be accessed by::

                mesh.MeshNodeArray

        Parameters
        ----------
        nodes
            A list of MeshNode objects.

        Returns
        -------
        MeshNodeArray
            A :py:class:`~abaqus.Mesh.MeshNodeArray.MeshNodeArray` object.
        """
        super().__init__()

    @abaqus_method_doc
    def getFromLabel(self, label: int) -> MeshNode:
        """This method returns the object in the MeshNodeArray with the given label.

        Parameters
        ----------
        label
            An Int specifying the label of the object.

        Returns
        -------
        MeshNode
            A :py:class:`~abaqus.Mesh.MeshNode.MeshNode` object.
        """
        ...

    @abaqus_method_doc
    def getSequenceFromMask(self, mask: Union[str, Sequence[str]]) -> MeshNodeArray:
        """This method returns the objects in the MeshNodeArray identified using the specified
        **mask**. This command is generated when the JournalOptions are set to COMPRESSEDINDEX.
        When a large number of objects are involved, this method is highly efficient.

        Parameters
        ----------
        mask
            A String specifying the object or objects.

        Returns
        -------
        MeshNodeArray
            A :py:class:`~abaqus.Mesh.MeshNodeArray.MeshNodeArray` object.
        """
        ...

    @abaqus_method_doc
    def getMask(self) -> str:
        """This method returns a string specifying the object or objects.

        Returns
        -------
        str
            A String specifying the object or objects.
        """
        ...

    @abaqus_method_doc
    def getByBoundingBox(
        self,
        xMin: float = ...,
        yMin: float = ...,
        zMin: float = ...,
        xMax: float = ...,
        yMax: float = ...,
        zMax: float = ...,
    ) -> MeshNodeArray:
        """This method returns an array of nodes that lie within the specified bounding box.

        Parameters
        ----------
        xMin
            A float specifying the minimum X boundary of the bounding box.
        yMin
            A float specifying the minimum Y boundary of the bounding box.
        zMin
            A float specifying the minimum Z boundary of the bounding box.
        xMax
            A float specifying the maximum X boundary of the bounding box.
        yMax
            A float specifying the maximum Y boundary of the bounding box.
        zMax
            A float specifying the maximum Z boundary of the bounding box.

        Returns
        -------
        MeshNodeArray
            A :py:class:`~abaqus.Mesh.MeshNodeArray.MeshNodeArray` object, which is a sequence of MeshNode objects.
        """
        ...

    @abaqus_method_doc
    def getByBoundingCylinder(
        self,
        center1: Tuple[float, float, float],
        center2: Tuple[float, float, float],
        radius: float,
    ) -> MeshNodeArray:
        """This method returns an array of node objects that lie within the specified bounding
        cylinder.

        Parameters
        ----------
        center1
            A tuple of the X-, Y-, and Z-coordinates of the center of the first end of the cylinder.
        center2
            A tuple of the X-, Y-, and Z-coordinates of the center of the second end of the
            cylinder.
        radius
            A float specifying the radius of the cylinder.

        Returns
        -------
        MeshNodeArray
            A :py:class:`~abaqus.Mesh.MeshNodeArray.MeshNodeArray` object, which is a sequence of MeshNode objects.
        """
        ...

    @abaqus_method_doc
    def getByBoundingSphere(self, center: tuple, radius: str) -> MeshNodeArray:
        """This method returns an array of node objects that lie within the specified bounding
        sphere.

        Parameters
        ----------
        center
            A tuple of the X-, Y-, and Z-coordinates of the center of the sphere.
        radius
            A float specifying the radius of the sphere.

        Returns
        -------
        MeshNodeArray
            A :py:class:`~abaqus.Mesh.MeshNodeArray.MeshNodeArray` object, which is a sequence of MeshNode objects.
        """
        ...

    @abaqus_method_doc
    def getBoundingBox(self) -> Dict[str, Tuple[float, float, float]]:
        """This method returns a dictionary of two tuples representing minimum and maximum boundary
        values of the bounding box of the minimum size containing the node sequence.

        Returns
        -------
        Dict[str, Tuple[float, float, float]]
            A Dictionary object with the following items:

            - **low**: a tuple of three floats representing the minimum x, y and z boundary values of
              the bounding box.
            - **high**: a tuple of three floats representing the maximum x, y and z boundary values of
              the bounding box.

        Raises
        ------
        """
        ...

    @abaqus_method_doc
    def getClosest(
        self, coordinates: str, numToFind: int = 1, searchTolerance: float = ...
    ) -> Union[MeshNode, List[MeshNode]]:
        """This method returns the node or nodes closest to the given point or set of points.

        Parameters
        ----------
        coordinates
            A point defined by x, y, and z values or a list of such points.
        numToFind
            The number of nodes to find for each given point. For example, if **numToFind** is 2, then
            the 2 closest points, if available and within **searchTolerance**, will be returned in
            order of proximity for each input point. The default is 1.
        searchTolerance
            A float specifying a search radius for each point. By default, no search radius is
            defined, and all nodes in the sequence will be searched.

        Returns
        -------
        MeshNode | List[MeshNode]
            A MeshNode, or a list of MeshNode objects, or a list of lists of MeshNode objects,
            depending on the number of points given and the number of nodes requested.
        """
        ...

    @abaqus_method_doc
    def sequenceFromLabels(self, labels: Sequence[int]) -> MeshNodeArray:
        """This method returns the objects in the MeshNodeArray identified using the specified
        labels.

        Parameters
        ----------
        labels
            A sequence of Ints specifying the labels.

        Returns
        -------
        MeshNodeArray
            A :py:class:`~abaqus.Mesh.MeshNodeArray.MeshNodeArray` object.

        Raises
        ------
        Error: The mask results in an empty sequence
            An exception occurs if the resulting sequence is empty.
        """
        ...
