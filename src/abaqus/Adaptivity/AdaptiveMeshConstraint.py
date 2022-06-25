from abaqusConstants import *
from ..Datum.DatumCsys import DatumCsys
from ..Region.Region import Region


class AdaptiveMeshConstraint:
    """The AdaptiveMeshConstraint object is the abstract base type for other Arbitrary
    Lagrangian Eularian (ALE) style AdaptiveMeshConstraint objects. The
    AdaptiveMeshConstraint object has no explicit constructor. The methods and members of
    the AdaptiveMeshConstraint object are common to all objects derived from the
    AdaptiveMeshConstraint object.

    .. note:: 
        This object can be accessed by:

        .. code-block:: python

            import step
            mdb.models[name].adaptiveMeshConstraints[name]
    """

    #: A String specifying the adaptive mesh constraint repository key.
    name: str = ""

    #: A SymbolicConstant specifying the category of the adaptive mesh constraint. Possible
    #: values are MECHANICAL and THERMAL.
    category: SymbolicConstant = None

    #: A :py:class:`~abaqus.Region.Region.Region` object specifying the region to which the adaptive mesh constraint is applied.
    region: Region = Region()

    #: None or a DatumCsys object specifying the local coordinate system of the adaptive mesh
    #: constraint's degrees of freedom. If **localCsys** = None, the degrees of freedom are defined
    #: in the global coordinate system. The default value is None.
    localCsys: DatumCsys = None

    def __init__(
        self,
        name: str,
        category: SymbolicConstant,
        region: Region,
        localCsys: DatumCsys = None,
    ):
        """The AdaptiveMeshConstraint object is the abstract base type for other Arbitrary
        Lagrangian Eularian (ALE) style AdaptiveMeshConstraint objects. The
        AdaptiveMeshConstraint object has no explicit constructor. The methods and members of
        the AdaptiveMeshConstraint object are common to all objects derived from the
        AdaptiveMeshConstraint object.

        .. note:: 
            This function can be accessed by:

            .. code-block:: python

                mdb.models[name].AdaptiveMeshConstraint

        Parameters
        ----------
        name
            A String specifying the adaptive mesh constraint repository key.
        category
            A SymbolicConstant specifying the category of the adaptive mesh constraint. Possible values are MECHANICAL and THERMAL.
        region
            A :py:class:`~abaqus.Region.Region.Region` object specifying the region to which the adaptive mesh constraint is applied.
        localCsys
            None or a DatumCsys object specifying the local coordinate system of the adaptive mesh  constraint's
            degrees of freedom. If **localCsys** = None, the degrees of freedom are defined  in the global coordinate
            system. The default value is None.
        """
        pass

    def deactivate(self, stepName: str):
        """This method deactivates the adaptive mesh constraint in the specified step and all
        subsequent steps.

        Parameters
        ----------
        stepName
            A String specifying the name of the step in which the adaptive mesh constraint is
            deactivated.

        Raises
        ------
        TextError
        """
        pass

    def move(self, fromStepName: str, toStepName: str):
        """This method moves the adaptive mesh constraint state from one step to a different step.

        Parameters
        ----------
        fromStepName
            A String specifying the name of the step from which the adaptive mesh constraint state
            is moved.
        toStepName
            A String specifying the name of the step to which the adaptive mesh constraint state is
            moved.

        Raises
        ------
        TextError
        """
        pass

    def reset(self, stepName: str):
        """This method resets the adaptive mesh constraint state of the specified step to the state
        of the previous analysis step.

        Parameters
        ----------
        stepName
            A String specifying the name of the step in which the adaptive mesh constraint state is
            reset.

        Raises
        ------
        TextError
        """
        pass

    def resume(self):
        """This method resumes the adaptive mesh constraint that was previously suppressed."""
        pass

    def suppress(self):
        """This method suppresses the adaptive mesh constraint."""
        pass

    def delete(self, indices: tuple):
        """This method allows you to delete existing adaptive mesh constraints.

        Parameters
        ----------
        indices
            A sequence of Ints specifying the index of each adaptive mesh constraint to delete.
        """
        pass
