from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from ....UtilityAndView.abaqusConstants import *


@abaqus_class_doc
class FailStress:
    r"""The FailStress object defines parameters for stress-based failure measures.

    .. note:: 
        This object can be accessed by::

            import material
            mdb.models[name].materials[name].elastic.failStress
            import odbMaterial
            session.odbs[name].materials[name].elastic.failStress

        The table data for this object are:
        
        - Tensile stress limit in fiber direction, :math:`X_{t}`.
        - Compressive stress limit in fiber direction, :math:`X_{c}`.
        - Tensile stress limit in transverse direction, :math:`Y_{t}`
        - Compressive stress limit in transverse direction, :math:`Y_{c}`.
        - Shear strength in the :math:`X - Y` plane, :math:`S`.
        - Cross product term coefficient, :math:`f^{*} (-1.0 \leq f^{*} \leq 1.0)`. 
          The default value is zero.
        - Biaxial stress limit, :math:`\sigma_{b i a x}`.
        - Temperature, if the data depend on temperature.
        - Value of the first field variable, if the data depend on field variables.
        - Value of the second field variable.
        - Etc.

        The corresponding analysis keywords are:

        - FAIL STRESS
    """

    @abaqus_method_doc
    def __init__(
        self, table: tuple, temperatureDependency: Boolean = OFF, dependencies: int = 0
    ):
        """This method creates a FailStress object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].materials[name].elastic.FailStress
                session.odbs[name].materials[name].elastic.FailStress

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
        FailStress
            A :py:class:`~abaqus.Material.Elastic.Linear.FailStress.FailStress` object.

        Raises
        ------
        RangeError
        """
        ...

    @abaqus_method_doc
    def setValues(self, *args, **kwargs):
        """This method modifies the FailStress object.

        Raises
        ------
        RangeError
        """
        ...
