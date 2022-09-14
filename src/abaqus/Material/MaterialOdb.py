from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from .Material import Material
from ..Odb.OdbBase import OdbBase


@abaqus_class_doc
class MaterialOdb(OdbBase):
    """The Odb object is the in-memory representation of an output database (ODB) file.

    .. note:: 
        This object can be accessed by::

            import odbAccess
            session.odbs[name]
    """

    @abaqus_method_doc
    def Material(self, name: str, description: str = "", materialIdentifier: str = ""):
        """This method creates a Material object.

        .. note:: 
            This function can be accessed by::

                session.odbs[name].Material

        Parameters
        ----------
        name
            A String specifying the name of the new material.
        description
            A String specifying user description of the material. The default value is an empty
            string.
        materialIdentifier
            A String specifying material identifier for customer use. The default value is an empty
            string.

        Returns
        -------
        Material
            A :py:class:`~abaqus.Material.Material.Material` object.
        """
        self.materials[name] = material = Material(
            name, description, materialIdentifier
        )
        return material
