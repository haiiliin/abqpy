from ..Material.Material import Material
from ..Model.ModelBase import ModelBase


class MaterialModel(ModelBase):
    """Abaqus creates a Model object named `Model-1` when a session is started.

    .. note:: 
        This object can be accessed by:

        .. code-block:: python

            mdb.models[name]
    """

    def Material(self, name: str, description: str = "", materialIdentifier: str = ""):
        """This method creates a Material object.

        .. note:: 
            This function can be accessed by:

            .. code-block:: python

                mdb.models[name].Material

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
