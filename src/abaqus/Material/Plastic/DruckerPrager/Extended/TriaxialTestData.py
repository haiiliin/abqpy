from typing import Optional
from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

@abaqus_class_doc
class TriaxialTestData:
    r"""The TriaxialTestData object provides triaxial test data.

    .. note:: 
        This object can be accessed by::

            import material
            mdb.models[name].materials[name].druckerPrager.triaxialTestData
            import odbMaterial
            session.odbs[name].materials[name].druckerPrager.triaxialTestData

        The table data for this object are:

        - Sign and magnitude of confining stress, :math:`\sigma_1=\sigma_2`.
        - Sign and magnitude of the stress in loading direction, :math:`\sigma_3`.

        The corresponding analysis keywords are:

        - TRIAXIAL TEST DATA
    """

    @abaqus_method_doc
    def __init__(
        self, table: tuple, a: Optional[float] = None, b: Optional[float] = None, pt: Optional[float] = None
    ):
        """This method creates a TriaxialTestData object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].materials[name].druckerPrager.TriaxialTestData
                session.odbs[name].materials[name].druckerPrager.TriaxialTestData

        Parameters
        ----------
        table
            A sequence of sequences of Floats specifying the items described below.
        a
            None or a Float specifying the value of the material constant aa. None is used when the
            value is unknown or it is not held fixed at the input value. The default value is None.
        b
            None or a Float specifying the value of the material constant bb. None is used when the
            value is unknown or it is not held fixed at the input value. The default value is None.
        pt
            None or a Float specifying the value of the material constant pt. None is used when the
            value is unknown or it is not held fixed at the input value. The default value is None.

        Returns
        -------
        TriaxialTestData
            A :py:class:`~abaqus.Material.Plastic.DruckerPrager.Extended.TriaxialTestData.TriaxialTestData` object.

        Raises
        ------
        RangeError
        """
        ...

    @abaqus_method_doc
    def setValues(self, *args, **kwargs):
        """This method modifies the TriaxialTestData object.

        Raises
        ------
        RangeError
        """
        ...
