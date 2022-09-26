from __future__ import annotations
from typing import Union, List, Tuple, Dict

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from .IgnoredEdge import IgnoredEdge
from ..UtilityAndView.abaqusConstants import *


@abaqus_class_doc
class IgnoredEdgeArray(List[IgnoredEdge]):
    """The IgnoredEdgeArray is a sequence of IgnoredEdge objects. If the part is modified, then
    IgnoredEdgeArray must be updated for that part.

    .. note:: 
        This object can be accessed by::

            import part
            mdb.models[name].parts[name].ignoredEdges
            import assembly
            mdb.models[name].rootAssembly.allInstances[name].ignoredEdges
            mdb.models[name].rootAssembly.instances[name].ignoredEdges
    """

    @abaqus_method_doc
    def findAt(self, coordinates: tuple, printWarning: Boolean = True) -> Union[IgnoredEdge, List[IgnoredEdge]]:
        """This method returns the object or objects in the IgnoredEdgeArray located at the given
        coordinates.
        findAt initially uses the ACIS tolerance of 1E-6. As a result, findAt returns any
        IgnoredEdge that is at the arbitrary point specified or at a distance of less than 1E-6
        from the arbitrary point. If nothing is found, findAt uses the tolerance for imprecise
        geometry (applicable only for imprecise geometric entities). The arbitrary point must
        not be shared by a second IgnoredEdge. If two IgnoredEdge objects intersect or coincide
        at the arbitrary point, findAt chooses the first IgnoredEdge that it encounters, and you
        should not rely on the return value being consistent.
        findAt will always try to find objects among all the ignored edges in the part or
        assembly instance and will not restrict itself to a subset even if the IgnoredEdgeArray
        represents such subset.

        Parameters
        ----------
        coordinates
            A sequence of Floats specifying the **X**-, **Y**-, and **Z**- coordinates of the object to
            find.findAt returns either an IgnoredEdge object or a sequence of IgnoredEdge objects
            based on the type of input.If **coordinates** is a sequence of Floats, findAt returns the
            IgnoredEdge object at that point.If you omit the **coordinates** keyword argument, findAt
            accepts as arguments a sequence of sequence of floats in the following
            format::
            
                ignoredEdges = e.findAt(((20.19686, -169.513997, 27.798593), ),
                                        ((19.657627, -167.295749, 27.056402), ),
                                        ((18.274129, -157.144741, 25.15218), ))
        printWarning
            A Boolean specifying whether a message is to be printed to the CLI if no entity is found
            at the specified location. The default value is True.

        Returns
        -------
        IgnoredEdge
            An :py:class:`~abaqus.BasicGeometry.IgnoredEdge.IgnoredEdge` object or a sequence of IgnoredEdge objects.

        """
        return IgnoredEdge()

    @abaqus_method_doc
    def getSequenceFromMask(self, mask: str):
        """This method returns the object or objects in the IgnoredEdgeArray identified using the
        specified **mask**. This command is generated when the JournalOptions are set to
        COMPRESSEDINDEX. When large number of objects are involved, this method is highly
        efficient.

        Parameters
        ----------
        mask
            A String specifying the object or objects.

        Returns
        -------
        IgnoredEdge
            An :py:class:`~abaqus.BasicGeometry.IgnoredEdge.IgnoredEdge` object or a sequence of IgnoredEdge objects.

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
    def getClosest(self, coordinates: tuple, searchTolerance: str = "") -> Dict:
        """This method returns a object or objects in the IgnoredEdgeArray closest to the given set
        of points, where the given points need not lie on the edges in the IgnoredEdgeArray.

        Parameters
        ----------
        coordinates
            A sequence of a sequence of floats, where each sequence of floats describes the **X**-,
            **Y**-, and **Z**-coordinates of a point::
            
                >>> r=e.getClosest(coordinates=((20.0, 20.0, 10.0),(-1.0, -15.0, 15), ))
                >>> r.keys()
                [0, 1]
                >>> r[0]
                (mdb.models['Model-1'].parts['Part-1'].ignoredEdges[3], (15.7090625762939, 20.0, 10.0))
        searchTolerance
            A double specifying the distance within which the closest object must lie. The default
            value is half of the parent part/instance size.

        Returns
        -------
        dict
            This method returns a dictionary object. The key to the dictionary object is the
            position of the input point in the tuple specified in the **coordinates** starting at
            index 0. If a closest IgnoredEdge could be found then the value is a sequence consisting
            of two objects. The first object in the sequence is an IgnoredEdge that is close to the
            input point referred to by the key. The second object in the sequence, is a sequence of
            floats which specify the **X**-, **Y**-, and **Z**- location of the closest point on the
            IgnoredEdge to the given point. See program listing above.

        Raises
        ------
        Error: The mask results in an empty sequence
            An exception occurs if the resulting sequence is empty.
        """
        ...
