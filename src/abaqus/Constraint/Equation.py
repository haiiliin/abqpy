from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from .Constraint import Constraint
from ..UtilityAndView.abaqusConstants import Boolean, OFF


@abaqus_class_doc
class Equation(Constraint):
    """The Equation object defines a linear multi-point constraint between a set of degrees of
    freedom.
    The Equation object is derived from the ConstrainedSketchConstraint object.

    .. note::
        This object can be accessed by::

            import interaction
            mdb.models[name].constraints[name]

        The corresponding analysis keywords are:

        - EQUATION
    """

    #: A Boolean specifying whether the constraint is suppressed or not. The default value is
    #: OFF.
    suppressed: Boolean = OFF

    #: A String specifying the constraint repository key.
    name: str

    #: A sequence of (Float, String, Int, Int) sequences specifying a coefficient, Set name,
    #: degree of freedom, and coordinate system ID. The coordinate system ID is optional.
    terms: tuple

    @abaqus_method_doc
    def __init__(self, name: str, terms: tuple):
        """This method creates an Equation object.

        .. note::
            This function can be accessed by::

                mdb.models[name].Equation

        Parameters
        ----------
        name
            A String specifying the constraint repository key.
        terms
            A sequence of (Float, String, Int, Int) sequences specifying a coefficient, Set name,
            degree of freedom, and coordinate system ID. The coordinate system ID is optional.

        Returns
        -------
        Equation
            An :py:class:`~abaqus.Constraint.Equation.Equation` object.

        Raises
        ------
        If **terms** does not contain more than one entry, Equation must have two or more terms.
        """
        super().__init__()

    @abaqus_method_doc
    def setValues(self, *args, **kwargs):
        """This method modifies the Equation object.

        Raises
        ------
        If **terms** does not contain more than one entry, Equation must have two or more terms.
        """
        ...
