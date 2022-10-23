from abqpy.decorators import abaqus_class_doc, abaqus_method_doc


@abaqus_class_doc
class TransverseShearShell:
    """The TransverseShearShell object defines the transverse shear stiffness properties of a
    shell section.

    .. note::
        This object can be accessed by::

            import section
            mdb.models[name].sections[name].transverseShear
            import odbSection
            session.odbs[name].sections[name].transverseShear

        The corresponding analysis keywords are:

        - TRANSVERSE SHEAR STIFFNESS
    """

    #: A Float specifying the shear stiffness of the section in the first direction.
    k11: float

    #: A Float specifying the shear stiffness of the section in the second direction.
    k22: float

    #: A Float specifying the coupling term in the shear stiffness of the section.
    k12: float

    @abaqus_method_doc
    def __init__(self, k11: float, k22: float, k12: float):
        """This method creates a TransverseShearShell object.

        .. note::
            This function can be accessed by::

                mdb.models[name].sections[name].TransverseShearShell
                session.odbs[name].sections[name].TransverseShearShell

        Parameters
        ----------
        k11
            A Float specifying the shear stiffness of the section in the first direction.
        k22
            A Float specifying the shear stiffness of the section in the second direction.
        k12
            A Float specifying the coupling term in the shear stiffness of the section.

        Returns
        -------
        TransverseShearShell
            A :py:class:`~abaqus.Section.TransverseShearShell.TransverseShearShell` object.
        """
        ...

    @abaqus_method_doc
    def setValues(self, *args, **kwargs):
        """This method modifies the TransverseShearShell object."""
        ...
