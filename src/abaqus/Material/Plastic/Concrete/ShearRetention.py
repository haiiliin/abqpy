from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from ....UtilityAndView.abaqusConstants import Boolean, OFF


@abaqus_class_doc
class ShearRetention:
    r"""The ShearRetention object defines the reduction of the shear modulus associated with
    crack surfaces in a Concrete model as a function of the tensile strain across the crack.

    .. note::
        This object can be accessed by::

            import material
            mdb.models[name].materials[name].concrete.shearRetention
            import odbMaterial
            session.odbs[name].materials[name].concrete.shearRetention

        The table data for this object are:

        - :math:`\varrho^{\text {close }} for dry concrete. The default value is 1.0`
        - :math:`\varepsilon^{\max }` for dry concrete. The default value is a very large number
          (full shear retention).
        - :math:`\varrho^{\text {close }} for wet concrete. The default value is 1.0`
        - :math:`\varepsilon^{\max }` for wet concrete. The default value is a very large number
          (full shear retention).
        - Temperature, if the data depend on temperature.
        - Value of the first field variable, if the data depend on field variables.
        - Value of the second field variable.
        - Etc.

        The corresponding analysis keywords are:

        - SHEAR RETENTION
    """

    @abaqus_method_doc
    def __init__(self, table: tuple, temperatureDependency: Boolean = OFF, dependencies: int = 0):
        """This method creates a ShearRetention object.

        .. note::
            This function can be accessed by::

                mdb.models[name].materials[name].concrete.ShearRetention
                session.odbs[name].materials[name].concrete.ShearRetention

        Parameters
        ----------
        table
            A sequence of sequences of Floats specifying the items described below.
        temperatureDependency
            A Boolean specifying whether the data depend on temperature. The default value is OFF.
        dependencies
            An Int specifying the number of field variable dependencies. The default value is 0.

        Returns
        -------
        ShearRetention
            A :py:class:`~abaqus.Material.Plastic.Concrete.ShearRetention.ShearRetention` object.

        Raises
        ------
        RangeError
        """
        ...

    @abaqus_method_doc
    def setValues(self, *args, **kwargs):
        """This method modifies the ShearRetention object.

        Raises
        ------
        RangeError
        """
        ...
