import typing

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from .MeshFace import MeshFace


@abaqus_class_doc
class MeshFaceArray(typing.List[MeshFace]):
    """The MeshFaceArray is a sequence of MeshFace objects.

    .. note:: 
        This object can be accessed by::

            import part
            mdb.models[name].parts[name].elementFaces
            import assembly
            mdb.models[name].rootAssembly.allInstances[name].elementFaces
            mdb.models[name].rootAssembly.instances[name].elementFaces
    """

    @abaqus_method_doc
    def __init__(self, faces: typing.List[MeshFace]):
        """This method creates a MeshFaceArray object.

        .. note:: 
            This function can be accessed by::

                mesh.MeshFaceArray

        Parameters
        ----------
        faces
            A list of MeshFace objects.

        Returns
        -------
        MeshFaceArray
            A :py:class:`~abaqus.Mesh.MeshFaceArray.MeshFaceArray` object.
        """
        super().__init__()

    @abaqus_method_doc
    def getSequenceFromMask(self, mask: str):
        """This method returns the objects in the MeshFaceArray identified using the specified
        **mask**. When large number of objects are involved, this method is highly efficient.

        Parameters
        ----------
        mask
            A String specifying the object or objects.

        Returns
        -------
        MeshFaceArray
            A :py:class:`~abaqus.Mesh.MeshFaceArray.MeshFaceArray` object.

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
