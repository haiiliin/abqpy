from __future__ import annotations

from typing import List, Tuple, Sequence, Dict, Union

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from .MeshElement import MeshElement


@abaqus_class_doc
class MeshElementArray(List[MeshElement]):
    """The MeshElementArray is a sequence of MeshElement objects.

    .. note::
        This object can be accessed by::

            import part
            mdb.models[name].parts[name].allInternalSets[name].elements
            mdb.models[name].parts[name].allInternalSurfaces[name].elements
            mdb.models[name].parts[name].allSets[name].elements
            mdb.models[name].parts[name].allSurfaces[name].elements
            mdb.models[name].parts[name].elements
            mdb.models[name].parts[name].sets[name].elements
            mdb.models[name].parts[name].surfaces[name].elements
            import assembly
            mdb.models[name].rootAssembly.allInstances[name].elements
            mdb.models[name].rootAssembly.allInstances[name].sets[name].elements
            mdb.models[name].rootAssembly.allInstances[name].surfaces[name].elements
            mdb.models[name].rootAssembly.allInternalSets[name].elements
            mdb.models[name].rootAssembly.allInternalSurfaces[name].elements
            mdb.models[name].rootAssembly.allSets[name].elements
            mdb.models[name].rootAssembly.allSurfaces[name].elements
            mdb.models[name].rootAssembly.elements
            mdb.models[name].rootAssembly.instances[name].elements
            mdb.models[name].rootAssembly.instances[name].sets[name].elements
            mdb.models[name].rootAssembly.instances[name].surfaces[name].elements
            mdb.models[name].rootAssembly.modelInstances[i].elements
            mdb.models[name].rootAssembly.modelInstances[i].sets[name].elements
            mdb.models[name].rootAssembly.modelInstances[i].surfaces[name].elements
            mdb.models[name].rootAssembly.sets[name].elements
            mdb.models[name].rootAssembly.surfaces[name].elements
    """

    @abaqus_method_doc
    def __init__(self, elements: List[MeshElement]) -> None:
        """This method creates a MeshElementArray object.

        .. note::
            This function can be accessed by::

                mesh.MeshElementArray

        Parameters
        ----------
        elements
            A list of MeshElement objects.

        Returns
        -------
        MeshElementArray
            A MeshElementArray object.
        """
        super().__init__()

    @abaqus_method_doc
    def getFromLabel(self, label: int) -> MeshElement:
        """This method returns the object in the MeshElementArray with the given label.

        Parameters
        ----------
        label
            An Int specifying the label of the object.

        Returns
        -------
        MeshElement
            A MeshElement object.
        """
        ...

    @abaqus_method_doc
    def getSequenceFromMask(self, mask: Union[str, Sequence[str]]) -> MeshElementArray:
        """This method returns the objects in the MeshElementArray identified using the specified
        **mask**. This command is generated when the JournalOptions are set to COMPRESSEDINDEX.
        When a large number of objects are involved, this method is highly efficient.

        Parameters
        ----------
        mask
            A String specifying the object or objects.

        Returns
        -------
        MeshElementArray
            A MeshElementArray object.
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
    ) -> MeshElementArray:
        """This method returns an array of element objects that lie within the specified bounding
        box.

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
        MeshElementArray
            A MeshElementArray object, which is a sequence of MeshElement objects.
        """
        ...

    @abaqus_method_doc
    def getByBoundingCylinder(self, center1: tuple, center2: tuple, radius: str) -> MeshElementArray:
        """This method returns an array of element objects that lie within the specified bounding
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
        MeshElementArray
            A MeshElementArray object, which is a sequence of MeshElement objects.
        """
        ...

    @abaqus_method_doc
    def getByBoundingSphere(self, center: Tuple[float, float, float], radius: float) -> MeshElementArray:
        """This method returns an array of element objects that lie within the specified bounding
        sphere.

        Parameters
        ----------
        center
            A tuple of the X-, Y-, and Z-coordinates of the center of the sphere.
        radius
            A float specifying the radius of the sphere.

        Returns
        -------
        MeshElementArray
            A MeshElementArray object, which is a sequence of MeshElement objects.
        """
        ...

    @abaqus_method_doc
    def getBoundingBox(self) -> Dict[str, Tuple[float, float, float]]:
        """This method returns a dictionary of two tuples representing minimum and maximum boundary
        values of the bounding box of the minimum size containing the element sequence.

        Returns
        -------
        Dict[str, Tuple[float, float, float]]
            A Dictionary object with the following items:

            - **low**: a tuple of three floats representing the minimum x, y, and z boundary values of
              the bounding box.
            - **high**: a tuple of three floats representing the maximum x, y, and z boundary values of
              the bounding box.
        """
        ...

    @abaqus_method_doc
    def sequenceFromLabels(self, labels: Sequence[int]) -> MeshElementArray:
        """This method returns the objects in the MeshElementArray identified using the specified
        labels.

        Parameters
        ----------
        labels
            A sequence of Ints specifying the labels.

        Returns
        -------
        MeshElementArray
            A MeshElementArray object.

        Raises
        ------
        Error: The mask results in an empty sequence
            An exception occurs if the resulting sequence is empty.
        """
        ...
