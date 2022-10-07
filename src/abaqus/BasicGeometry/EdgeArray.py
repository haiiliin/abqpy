from __future__ import annotations

from typing import Union, Tuple, Dict, List, overload

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from .Edge import Edge
from ..UtilityAndView.abaqusConstants import Boolean


@abaqus_class_doc
class EdgeArray(List[Edge]):
    """The EdgeArray is a sequence of Edge objects. If the part is modified, then EdgeArray
    must be updated for that part.

    .. note:: 
        This object can be accessed by::

            import part
            mdb.models[name].parts[name].allInternalSets[name].edges
            mdb.models[name].parts[name].allInternalSurfaces[name].edges
            mdb.models[name].parts[name].allSets[name].edges
            mdb.models[name].parts[name].allSurfaces[name].edges
            mdb.models[name].parts[name].edges
            mdb.models[name].parts[name].sets[name].edges
            mdb.models[name].parts[name].surfaces[name].edges
            import assembly
            mdb.models[name].rootAssembly.allInstances[name].edges
            mdb.models[name].rootAssembly.allInstances[name].sets[name].edges
            mdb.models[name].rootAssembly.allInstances[name].surfaces[name].edges
            mdb.models[name].rootAssembly.allInternalSets[name].edges
            mdb.models[name].rootAssembly.allInternalSurfaces[name].edges
            mdb.models[name].rootAssembly.allSets[name].edges
            mdb.models[name].rootAssembly.allSurfaces[name].edges
            mdb.models[name].rootAssembly.edges
            mdb.models[name].rootAssembly.instances[name].edges
            mdb.models[name].rootAssembly.instances[name].sets[name].edges
            mdb.models[name].rootAssembly.instances[name].surfaces[name].edges
            mdb.models[name].rootAssembly.modelInstances[i].edges
            mdb.models[name].rootAssembly.modelInstances[i].sets[name].edges
            mdb.models[name].rootAssembly.modelInstances[i].surfaces[name].edges
            mdb.models[name].rootAssembly.sets[name].edges
            mdb.models[name].rootAssembly.surfaces[name].edges
    """

    @abaqus_method_doc
    def __init__(self, edges: List[Edge]) -> None:
        """This method creates an EdgeArray object.

        .. note:: 
            This function can be accessed by::

                part.EdgeArray

        Parameters
        ----------
        edges
            A list of Edge objects.

        Returns
        -------
        EdgeArray
            A :py:class:`~abaqus.BasicGeometry.EdgeArray.EdgeArray` object.

        """
        ...

    @overload
    @abaqus_method_doc
    def findAt(
        self, *coordinates: Tuple[float, float, float], printWarning: Boolean = True
    ) -> Edge:
        ...

    @overload
    def findAt(
        self,
        *coordinates: Tuple[Tuple[float, float, float]],
        printWarning: Boolean = True
    ) -> List[Edge]:
        ...

    def findAt(
        self,
        *coordinates: Union[
            Tuple[float, float, float], Tuple[Tuple[float, float, float]]
        ],
        printWarning: Boolean = True
    ) -> Union[Edge, List[Edge]]:
        """This method returns the object or objects in the EdgeArray located at the given
        coordinates.
        findAt initially uses the ACIS tolerance of 1E-6. As a result, findAt returns any edge
        that is at the arbitrary point specified or at a distance of less than 1E-6 from the
        arbitrary point. If nothing is found, findAt uses the tolerance for imprecise geometry
        (applicable only for imprecise geometric entities). The arbitrary point must not be
        shared by a second edge. If two edges intersect or coincide at the arbitrary point,
        findAt chooses the first edge that it encounters, and you should not rely on the return
        value being consistent.
        findAt will always try to find objects among all the edges in the part or assembly
        instance and will not restrict itself to a subset even if the EdgeArray represents such
        subset.

        Parameters
        ----------
        coordinates
            A sequence of Floats specifying the **X**-, **Y**-, and **Z**-coordinates of the object to
            find. findAt returns either an Edge object or a sequence of Edge objects based on the
            type of input.

            * If **coordinates** is a sequence of Floats, findAt returns the Edge object at that point.
            * If you omit the **coordinates** keyword argument, findAt accepts as arguments a sequence
              of sequence of floats in the following format::
            
                edges = e.findAt(((20.19686, -169.513997, 27.798593), ), 
                                 ((19.657627, -167.295749, 27.056402), ), 
                                 ((18.274129, -157.144741, 25.15218), ))
        printWarning
            A Boolean specifying whether a message is to be printed to the CLI if no entity is found
            at the specified location. The default value is True.

        Returns
        -------
        Edge
            An :py:class:`~abaqus.BasicGeometry.Edge.Edge` object or a sequence of Edge objects.

        """
        return Edge()

    @abaqus_method_doc
    def getClosest(self, coordinates: tuple, searchTolerance: str = "") -> Dict:
        """This method returns an object or objects in the EdgeArray closest to the given set of
        points, where the given points need not lie on the edges in the EdgeArray.

        Parameters
        ----------
        coordinates
            A sequence of a sequence of floats, where each sequence of floats describes the **X**-,
            **Y**-, and **Z**- coordinates of a point::
            
                >>> r=e.getClosest(coordinates=((20.0, 20.0, 10.0), (-1.0, -15.0, 15), ))
                >>> r.keys()
                [0, 1]
                >>> r[0]
                (mdb.models['Model-1'].parts['Part-1'].edges[3], (15.7090625762939, 20.0, 10.0))
        searchTolerance
            A double specifying the distance within which the closest object must lie. The default
            value is half of the parent part/instance size.

        Returns
        -------
        dict
            This method returns a dictionary object. The key to the dictionary object is the
            position of the input point in the tuple specified in the **coordinates** starting at
            index 0. If a closest edge could be found then the value is a sequence consisting of two
            objects. The first object in the sequence is an Edge that is close to the input point
            referred to by the key. The second object in the sequence is a sequence of floats that
            specifies the **X**-, **Y**-, and **Z**- location of the closest point on the Edge to the given
            point. See program listing above.
        """
        ...

    @abaqus_method_doc
    def getSequenceFromMask(self, mask: str):
        """This method returns the object or objects in the EdgeArray identified using the
        specified **mask**. This command is generated when the JournalOptions are set to
        COMPRESSEDINDEX. When a large number of objects are involved, this method is highly
        efficient.

        Parameters
        ----------
        mask
            A String specifying the object or objects.

        Returns
        -------
        Edge
            An :py:class:`~abaqus.BasicGeometry.Edge.Edge` object or a sequence of Edge objects.

        Raises
        ------
        Error: The mask results in an empty sequence
            An exception occurs if the resulting sequence is empty.
        """
        ...

    @abaqus_method_doc
    def getMask(self):
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
    ) -> EdgeArray:
        """This method returns an array of edge objects that lie within the specified bounding box.

        Parameters
        ----------
        xMin
            A float specifying the minimum **X**-boundary of the bounding box.
        yMin
            A float specifying the minimum **Y**-boundary of the bounding box.
        zMin
            A float specifying the minimum **Z**-boundary of the bounding box.
        xMax
            A float specifying the maximum **X**-boundary of the bounding box.
        yMax
            A float specifying the maximum **Y**-boundary of the bounding box.
        zMax
            A float specifying the maximum **Z**-boundary of the bounding box.

        Returns
        -------
        EdgeArray
            An :py:class:`~abaqus.BasicGeometry.EdgeArray.EdgeArray` object, which is a sequence of Edge objects.

        """
        ...

    @abaqus_method_doc
    def getByBoundingCylinder(
        self,
        center1: Tuple[float, float, float],
        center2: Tuple[float, float, float],
        radius: float,
    ) -> EdgeArray:
        """This method returns an array of edge objects that lie within the specified bounding
        cylinder.

        Parameters
        ----------
        center1
            A tuple of the **X**-, **Y**-, and **Z**-coordinates of the center of the first end of the
            cylinder.
        center2
            A tuple of the **X**-, **Y**-, and **Z**-coordinates of the center of the second end of the
            cylinder.
        radius
            A float specifying the radius of the cylinder.

        Returns
        -------
        EdgeArray
            An :py:class:`~abaqus.BasicGeometry.EdgeArray.EdgeArray` object, which is a sequence of Edge objects.

        """
        ...

    @abaqus_method_doc
    def getByBoundingSphere(
        self, center: Tuple[float, float, float], radius: float,
    ) -> Dict[str, Tuple[float, float, float]]:
        """This method returns an array of edge objects that lie within the specified bounding
        sphere.

        Parameters
        ----------
        center
            A tuple of the **X**-, **Y**-, and **Z**-coordinates of the center of the sphere.
        radius
            A float specifying the radius of the sphere.

        Returns
        -------
        EdgeArray
            An :py:class:`~abaqus.BasicGeometry.EdgeArray.EdgeArray` object, which is a sequence of Edge objects.

        """
        ...

    @abaqus_method_doc
    def getBoundingBox(self) -> Dict[str, Tuple[float, float, float]]:
        """This method returns a dictionary of two tuples representing minimum and maximum boundary
        values of the bounding box of the minimum size containing the edge sequence.

        Returns
        -------
        Dict[str, Tuple[float, float, float]]
            A Dictionary object with the following items:
            
            - **low**: a tuple of three floats representing the minimum **X** -, **Y** -, and **Z** -boundary
              values of the bounding box.
            - **high**: a tuple of three floats representing the maximum **X** -, **Y** -, and **Z** -boundary
              values of the bounding box.
        """
        ...
