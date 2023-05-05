from abqpy.decorators import abaqus_class_doc, abaqus_method_doc


@abaqus_class_doc
class DamageStabilization:
    """The DamageStabilization object specifies the viscosity coefficients for the damage model for fiber-
    reinforced materials.

    .. note::
        This object can be accessed by::

            import material
            mdb.models[name].materials[name].ductileDamageInitiation.damageStabilization
            mdb.models[name].materials[name].fldDamageInitiation.damageStabilization
            mdb.models[name].materials[name].flsdDamageInitiation.damageStabilization
            mdb.models[name].materials[name].hashinDamageInitiation.damageStabilization
            mdb.models[name].materials[name].johnsonCookDamageInitiation.damageStabilization
            mdb.models[name].materials[name].maxeDamageInitiation.damageStabilization
            mdb.models[name].materials[name].maxpeDamageInitiation.damageStabilization
            mdb.models[name].materials[name].maxpsDamageInitiation.damageStabilization
            mdb.models[name].materials[name].maxsDamageInitiation.damageStabilization
            mdb.models[name].materials[name].mkDamageInitiation.damageStabilization
            mdb.models[name].materials[name].msfldDamageInitiation.damageStabilization
            mdb.models[name].materials[name].quadeDamageInitiation.damageStabilization
            mdb.models[name].materials[name].quadsDamageInitiation.damageStabilization
            mdb.models[name].materials[name].shearDamageInitiation.damageStabilization
            import odbMaterial
            session.odbs[name].materials[name].ductileDamageInitiation.damageStabilization
            session.odbs[name].materials[name].fldDamageInitiation.damageStabilization
            session.odbs[name].materials[name].flsdDamageInitiation.damageStabilization
            session.odbs[name].materials[name].hashinDamageInitiation.damageStabilization
            session.odbs[name].materials[name].johnsonCookDamageInitiation.damageStabilization
            session.odbs[name].materials[name].maxeDamageInitiation.damageStabilization
            session.odbs[name].materials[name].maxpeDamageInitiation.damageStabilization
            session.odbs[name].materials[name].maxpsDamageInitiation.damageStabilization
            session.odbs[name].materials[name].maxsDamageInitiation.damageStabilization
            session.odbs[name].materials[name].mkDamageInitiation.damageStabilization
            session.odbs[name].materials[name].msfldDamageInitiation.damageStabilization
            session.odbs[name].materials[name].quadeDamageInitiation.damageStabilization
            session.odbs[name].materials[name].quadsDamageInitiation.damageStabilization
            session.odbs[name].materials[name].shearDamageInitiation.damageStabilization

        The corresponding analysis keywords are:

        - DAMAGE STABILIZATION
    """

    @abaqus_method_doc
    def __init__(
        self,
        fiberTensileCoeff: float,
        fiberCompressiveCoeff: float,
        matrixTensileCoeff: float,
        matrixCompressiveCoeff: float,
    ):
        """This method creates a DamageStabilization object.

        .. note::
            This function can be accessed by::

                mdb.models[name].materials[name].ductileDamageInitiation.DamageStabilization
                mdb.models[name].materials[name].fldDamageInitiation.DamageStabilization
                mdb.models[name].materials[name].flsdDamageInitiation.DamageStabilization
                mdb.models[name].materials[name].hashinDamageInitiation.DamageStabilization
                mdb.models[name].materials[name].johnsonCookDamageInitiation.DamageStabilization
                mdb.models[name].materials[name].maxeDamageInitiation.DamageStabilization
                mdb.models[name].materials[name].maxpeDamageInitiation.DamageStabilization
                mdb.models[name].materials[name].maxpsDamageInitiation.DamageStabilization
                mdb.models[name].materials[name].maxsDamageInitiation.DamageStabilization
                mdb.models[name].materials[name].mkDamageInitiation.DamageStabilization
                mdb.models[name].materials[name].msfldDamageInitiation.DamageStabilization
                mdb.models[name].materials[name].quadeDamageInitiation.DamageStabilization
                mdb.models[name].materials[name].quadsDamageInitiation.DamageStabilization
                mdb.models[name].materials[name].shearDamageInitiation.DamageStabilization
                session.odbs[name].materials[name].ductileDamageInitiation.DamageStabilization
                session.odbs[name].materials[name].fldDamageInitiation.DamageStabilization
                session.odbs[name].materials[name].flsdDamageInitiation.DamageStabilization
                session.odbs[name].materials[name].hashinDamageInitiation.DamageStabilization
                session.odbs[name].materials[name].johnsonCookDamageInitiation.DamageStabilization
                session.odbs[name].materials[name].maxeDamageInitiation.DamageStabilization
                session.odbs[name].materials[name].maxpeDamageInitiation.DamageStabilization
                session.odbs[name].materials[name].maxpsDamageInitiation.DamageStabilization
                session.odbs[name].materials[name].maxsDamageInitiation.DamageStabilization
                session.odbs[name].materials[name].mkDamageInitiation.DamageStabilization
                session.odbs[name].materials[name].msfldDamageInitiation.DamageStabilization
                session.odbs[name].materials[name].quadeDamageInitiation.DamageStabilization
                session.odbs[name].materials[name].quadsDamageInitiation.DamageStabilization
                session.odbs[name].materials[name].shearDamageInitiation.DamageStabilization

        Parameters
        ----------
        fiberTensileCoeff
            A Float specifying the viscosity coefficient for the fiber tensile failure mode.
        fiberCompressiveCoeff
            A Float specifying the viscosity coefficient for the fiber compressive failure mode.
        matrixTensileCoeff
            A Float specifying the viscosity coefficient for the matrix tensile failure mode.
        matrixCompressiveCoeff
            A Float specifying the viscosity coefficient for the matrix compressive failure mode.

        Returns
        -------
        DamageStabilization
            A DamageStabilization object.

        Raises
        ------
        RangeError
        """
        ...

    @abaqus_method_doc
    def setValues(self, *args, **kwargs):
        """This method modifies the DamageStabilization object.

        Raises
        ------
        RangeError
        """
        ...
