from typing import Optional

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from ..UtilityAndView.abaqusConstants import Boolean, OFF


@abaqus_class_doc
class Cell:
    """Cells are volumetric regions of geometry.

    .. note::
        This object can be accessed by::

            import part
            mdb.models[name].parts[name].allInternalSets[name].cells[i]
            mdb.models[name].parts[name].allSets[name].cells[i]
            mdb.models[name].parts[name].cells[i]
            mdb.models[name].parts[name].sets[name].cells[i]
            import assembly
            mdb.models[name].rootAssembly.allInstances[name].cells[i]
            mdb.models[name].rootAssembly.allInstances[name].sets[name].cells[i]
            mdb.models[name].rootAssembly.allInternalSets[name].cells[i]
            mdb.models[name].rootAssembly.allSets[name].cells[i]
            mdb.models[name].rootAssembly.instances[name].cells[i]
            mdb.models[name].rootAssembly.instances[name].sets[name].cells[i]
            mdb.models[name].rootAssembly.modelInstances[i].sets[name].cells[i]
            mdb.models[name].rootAssembly.sets[name].cells[i]
    """

    #: An Int specifying the index of the cell in the CellArray.
    index: Optional[int] = None

    #: A Boolean specifying whether the cell belongs to the reference representation of the
    #: Part or Instance.
    isReferenceRep: Boolean = OFF

    #: A tuple of Floats specifying the **X**-, **Y**-, and **Z**-coordinates of a point located on
    #: the cell.
    pointOn: Optional[float] = None

    #: A tuple of Floats specifying the name of the feature that created this cell.
    featureName: Optional[float] = None

    #: A tuple of Floats specifying the name of the part instance for this cell (if
    #: applicable).
    instanceName: Optional[float] = None

    @abaqus_method_doc
    def getSize(self, printResults: Boolean = True):
        """This method returns a Float indicating the volume of the cell.

        Parameters
        ----------
        printResults
            A Boolean that determines whether a verbose output is to be printed. The default is
            True.

        Returns
        -------
        float
            A Float.

        """
        ...

    @abaqus_method_doc
    def getFaces(self):
        """This method returns a sequence consisting of the face IDs of the faces which bound the
        cell.

        Returns
        -------
        Sequence[int]
            A tuple of integers.

        """
        ...

    @abaqus_method_doc
    def getEdges(self):
        """This method returns a sequence consisting of the edge IDs of the edges on the cell.

        Returns
        -------
        Sequence[int]
            A tuple of integers.

        """
        ...

    @abaqus_method_doc
    def getVertices(self):
        """This method returns a sequence consisting of the vertex IDs of the vertices on the cell.

        Returns
        -------
        Sequence[int]
            A tuple of integers.

        """
        ...

    @abaqus_method_doc
    def getAdjacentCells(self):
        """This method returns an array of cell objects that share at least one face of the cell.

        Returns
        -------
        CellArray
            A :py:class:`~abaqus.BasicGeometry.CellArray.CellArray` object which is a sequence of Cell objects.

        """
        ...

    @abaqus_method_doc
    def getNodes(self):
        """This method returns an array of node objects that are associated with the cell.

        Returns
        -------
        MeshNodeArray
            A :py:class:`~abaqus.Mesh.MeshNodeArray.MeshNodeArray` object which is a sequence of MeshNode objects.

        """
        ...

    @abaqus_method_doc
    def getElements(self):
        """This method returns an array of element objects that are associated with the cell.

        Returns
        -------
        MeshElementArray
            A :py:class:`~abaqus.Mesh.MeshElementArray.MeshElementArray` object which is a sequence of MeshElement objects.

        """
        ...
