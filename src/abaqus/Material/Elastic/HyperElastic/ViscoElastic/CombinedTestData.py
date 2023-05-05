from typing import Optional

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc


@abaqus_class_doc
class CombinedTestData:
    r"""The CombinedTestData object specifies simultaneously the normalized shear and bulk compliances or
    relaxation moduli as functions of time.

    .. note::
        This object can be accessed by::

            import material
            mdb.models[name].materials[name].viscoelastic.combinedTestData
            import odbMaterial
            session.odbs[name].materials[name].viscoelastic.combinedTestData

        The table data for this object are:

        If **time** = RELAXATION_TEST_DATA, the table data specify the following:

        - Normalized shear modulus, :math:`g_R(t)` (:math:`0\le g_R(t)\le 1`).
        - Normalized volumetric (bulk) modulus, :math:`k_R(t)` (:math:`0\le k_R(t)\le 1`).
        - Time :math:`t` (:math:`t>0`).

        If **time** = CREEP_TEST_DATA, the table data specify the following:

        - Normalized shear compliance, :math:`j_S(t)` (:math:`j_S(t)\ge 1`).
        - Normalized volumetric (bulk) compliance, :math:`j_K(t)` (:math:`j_K(t)\ge 1`).
        - Time :math:`t` (:math:`t>0`).

        The corresponding analysis keywords are:

        - COMBINED TEST DATA
    """

    @abaqus_method_doc
    def __init__(self, table: tuple, volinf: Optional[float] = None, shrinf: Optional[float] = None):
        r"""This method creates a CombinedTestData object.

        .. note::
            This function can be accessed by::

                mdb.models[name].materials[name].viscoelastic.CombinedTestData
                session.odbs[name].materials[name].viscoelastic.CombinedTestData

        Parameters
        ----------
        table
            A sequence of sequences of Floats specifying the items described below. The values of
            the table data depend on the value of the **time** member of the Viscoelastic object.
        volinf
            None or a Float specifying a normalized volume. The value of **volinf** depends on the
            value of the **time** member of the Viscoelastic object. The default value is None.
            If **time** = RELAXATION_TEST_DATA, **volinf** specifies the value of the long-term normalized
            volumetric modulus, :math:`k_R(\infty)`.
            If **time** = CREEP_TEST_DATA, **volinf** specifies the value of the long-term normalized
            volumetric compliance, :math:`j_K(\infty)`.
        shrinf
            None or a Float specifying a normalized shear. The value of **shrinf** depends on the
            value of the **time** member of the Viscoelastic object. The default value is None.
            If **time** = RELAXATION_TEST_DATA, **shrinf** specifies the value of the long-term normalized
            shear modulus, :math:`g_R(\infty)`
            If **time** = CREEP_TEST_DATA, **shrinf** specifies the value of the long-term normalized
            shear compliance, :math:`j_S(\infty)`.

        Returns
        -------
        CombinedTestData
            A CombinedTestData object.
        """
        ...

    @abaqus_method_doc
    def setValues(self, *args, **kwargs):
        """This method modifies the CombinedTestData object."""
        ...
