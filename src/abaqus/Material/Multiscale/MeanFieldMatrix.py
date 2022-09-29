import typing
from abqpy.decorators import abaqus_class_doc, abaqus_method_doc


@abaqus_class_doc
class MeanFieldMatrix:
    """The MeanFieldMatrix object specifies the matrix property.

    .. note::
        This object can be accessed by::

            import material
            mdb.models[name].materials[name].constituents[name]
            import odbMaterial
            session.odbs[name].materials[name].constituents[name]

        The corresponding analysis keywords are:

        - CONSTITUENT

    .. versionadded:: 2018
        The `MeanFieldMatrix` class was added.
    """

    @abaqus_method_doc
    def __init__(
        self, name: str, material: str = "", isotropizationCoefficient: typing.Optional[float] = None
    ):
        """This method creates a MeanFieldMatrix object.

        .. note::
            This function can be accessed by::

                mdb.models[name].materials[name].meanFieldHomogenization.MeanFieldMatrix
                session.odbs[name].materials[name].meanFieldHomogenization.MeanFieldMatrix

        Parameters
        ----------
        name
            A String specifying the constituent repository key.
        material
            A String specifying the name of the material.
        isotropizationCoefficient
            A Float specifying the factor used for scaling the Plastic strain of the constituent
            when calculating the isotropic part of the tangent.

        Returns
        -------
            A MeanFieldMatrix object.

        Raises
        ------
        RangeError
        """
        ...

    @abaqus_method_doc
    def setValues(self):
        """This method modifies the MeanFieldMatrix object.

        Raises
        ------
        RangeError
        """
        ...
