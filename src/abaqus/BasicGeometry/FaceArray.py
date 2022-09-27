from __future__ import annotations
from typing import Union, Tuple, Dict, List

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from .Face import Face
from .EdgeArray import EdgeArray
from ..UtilityAndView.abaqusConstants import *


@abaqus_class_doc
class FaceArray(List[Face]):
    """The FaceArray is a sequence of Face objects. If the part is modified, then FaceArray
    must be updated for that part.

    .. note:: 
        This object can be accessed by::

            import part
            mdb.models[name].parts[name].allInternalSets[name].faces
            mdb.models[name].parts[name].allInternalSurfaces[name].faces
            mdb.models[name].parts[name].allSets[name].faces
            mdb.models[name].parts[name].allSurfaces[name].faces
            mdb.models[name].parts[name].faces
            mdb.models[name].parts[name].sets[name].faces
            mdb.models[name].parts[name].surfaces[name].faces
            import assembly
            mdb.models[name].rootAssembly.allInstances[name].faces
            mdb.models[name].rootAssembly.allInstances[name].sets[name].faces
            mdb.models[name].rootAssembly.allInstances[name].surfaces[name].faces
            mdb.models[name].rootAssembly.allInternalSets[name].faces
            mdb.models[name].rootAssembly.allInternalSurfaces[name].faces
            mdb.models[name].rootAssembly.allSets[name].faces
            mdb.models[name].rootAssembly.allSurfaces[name].faces
            mdb.models[name].rootAssembly.instances[name].faces
            mdb.models[name].rootAssembly.instances[name].sets[name].faces
            mdb.models[name].rootAssembly.instances[name].surfaces[name].faces
            mdb.models[name].rootAssembly.modelInstances[i].sets[name].faces
            mdb.models[name].rootAssembly.modelInstances[i].surfaces[name].faces
            mdb.models[name].rootAssembly.sets[name].faces
            mdb.models[name].rootAssembly.surfaces[name].faces
    """

    @abaqus_method_doc
    def __init__(self, faces: List[Face]) -> None:
        """This method creates a FaceArray object.

        .. note:: 
            This function can be accessed by::

                part.FaceArray

        Parameters
        ----------
        faces
            A list of Face objects.

        Returns
        -------
        FaceArray
            A :py:class:`~abaqus.BasicGeometry.FaceArray.FaceArray` object.

        """
        ...

    @abaqus_method_doc
    def findAt(
        self,
        coordinates: Union[
            Tuple[float, float, float], Tuple[Tuple[float, float, float],]
        ],
        normal: tuple = (),
        printWarning: Boolean = True,
    ) -> Union[Face, Tuple[Face, ...]]:
        """This method returns the object or objects in the FaceArray located at the given
        coordinates.
        findAt initially uses the ACIS tolerance of 1E-6. As a result, findAt returns any face
        that is at the arbitrary point specified or at a distance of less than 1E-6 from the
        arbitrary point. If nothing is found, findAt uses the tolerance for imprecise geometry
        (applicable only for imprecise geometric entities). The arbitrary point must not be
        shared by a second face. If two faces intersect or coincide at the arbitrary point,
        findAt chooses the first face that it encounters, and you should not rely on the return
        value being consistent.
        findAt will always try to find objects among all the faces in the part or assembly
        instance and will not restrict itself to a subset even if the FaceArray represents such
        subset.

        Parameters
        ----------
        coordinates
            A sequence of Floats specifying the **X**-, **Y**-, and **Z**-coordinates of the object to
            find. `findAt` returns either a Face object or a sequence of Face objects based on the type
            of input.
            
            * If **coordinates** is a sequence of Floats, findAt returns the Face object at that point.
            
            * If you omit the **coordinates** keyword argument, findAt accepts as arguments a
              sequence of pairs of sequences describing each face's coordinate and normal, and findAt
              returns a sequence of Face objects at the given locations. If you omit the **coordinates**
              keyword argument, you must also omit the **normal** argument::
            
                faces = f.findAt(((-16.438578, -41.835673, -24.19804), ), 
                                 ((25.210364, -35.689868, 1.860314), ), 
                                 ((26.727683, -38.207055, 4.164759), ))
        normal
            A sequence of Floats specifying the **X**-, **Y**-, and **Z**-components of a vector
            indicating the face normal.
        printWarning
            A Boolean specifying whether a message is to be printed to the CLI if no entity is found
            at the specified location. The default value is True.

        Returns
        -------
        Face
            A :py:class:`~abaqus.BasicGeometry.Face.Face` object.

        """
        ...

    @abaqus_method_doc
<<<<<<< HEAD
    def getSequenceFromMask(self, mask: str):
=======
    def getExteriorEdges(self) -> EdgeArray:
        """This method returns the edges on the exterior of the faces in the FaceArray. That is, it
        returns the edges that are referenced by exactly one of the faces in the sequence.

        Returns
        -------
        EdgeArray
            An :py:class:`~abaqus.BasicGeometry.EdgeArray.EdgeArray` object specifying the exterior edges.

        """
        ...

    @abaqus_method_doc
    def getSequenceFromMask(self, mask: str) -> Face:
>>>>>>> 74234014 (Improve type hints (#1716))
        """This method returns the object or objects in the FaceArray identified using the
        specified **mask**. This command is generated when the JournalOptions are set to
        COMPRESSEDINDEX. When a large number of objects are involved, this method is highly
        efficient.

        Parameters
        ----------
        mask
            A String specifying the object or objects.

        Returns
        -------
        Face
            A :py:class:`~abaqus.BasicGeometry.Face.Face` object or a sequence of Face objects.

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
    ) -> FaceArray:
        """This method returns an array of face objects that lie within the specified bounding box.

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
        FaceArray
            A :py:class:`~abaqus.BasicGeometry.FaceArray.FaceArray` object, which is a sequence of Face objects.

        """
        ...

    @abaqus_method_doc
    def getByBoundingCylinder(
        self, center1: tuple, center2: tuple, radius: str
    ) -> FaceArray:
        """This method returns an array of face objects that lie within the specified bounding
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
        FaceArray
            A :py:class:`~abaqus.BasicGeometry.FaceArray.FaceArray` object, which is a sequence of Face objects.

        """
        ...

    @abaqus_method_doc
    def getByBoundingSphere(self, center: tuple, radius: str) -> FaceArray:
        """This method returns an array of face objects that lie within the specified bounding
        sphere.

        Parameters
        ----------
        center
            A tuple of the **X**-, **Y**-, and **Z**-coordinates of the center of the sphere.
        radius
            A float specifying the radius of the sphere.

        Returns
        -------
        FaceArray
            A :py:class:`~abaqus.BasicGeometry.FaceArray.FaceArray` object, which is a sequence of Face objects.

        """
        ...

    @abaqus_method_doc
    def getBoundingBox(self) -> Dict[str, Tuple[float, ...]]:
        """This method returns a dictionary of two tuples representing minimum and maximum boundary
        values of the bounding box of the minimum size containing the face sequence.

        Returns
        -------
        Dict[str, Tuple[float, ...]]
            A Dictionary object with the following items:
            
            - **low**: a tuple of three floats representing the minimum **X** -, **Y** -, and **Z**  -boundary
              values of the bounding box.
            - **high**: a tuple of three floats representing the maximum **X** -, **Y** -, and **Z**  -boundary
              values of the bounding box.
        """
        ...

    @abaqus_method_doc
    def getClosest(self, coordinates: tuple, searchTolerance: str = "") -> Dict:
        """This method returns an object or objects in the FaceArray closest to the given set of
        points, where the given points need not lie on the faces in the FaceArray.

        Parameters
        ----------
        coordinates
            A sequence of a sequence of floats, where each sequence of floats describes the **X**-,
            **Y**-, and **Z**-coordinates of a point::
            
                >>> r=f.getClosest(coordinates=((20.0, 20.0, 10.0), (-1.0, -15.0, 15), ))
                >>> r.keys()
                [0, 1]
                >>> r[0]
                (mdb.models['Model-1'].parts['Part-1'].faces[0], (15.7090625762939, 20.0, 10.0))
        searchTolerance
            A double specifying the distance within which the closest object must lie. The default
            value is half of the parent part/instance size.

        Returns
        -------
        dict
            This method returns a dictionary object. The key to the dictionary object is the
            position of the input point in the tuple specified in the **coordinates** starting at
            index 0. If a closest face could be found then the value is a sequence consisting of two
            objects. The first object in the sequence is a Face that is close to the input point
            referred to by the key. The second object in the sequence is a sequence of floats that
            specifies the **X**-, **Y**-, and **Z**- location of the closest point on the Face to the given
            point. See program listing above.

        Raises
        ------
        Error: The mask results in an empty sequence
            An exception occurs if the resulting sequence is empty.
        """
        ...
