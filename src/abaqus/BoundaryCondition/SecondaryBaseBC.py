from typing import Optional
from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from .BoundaryCondition import BoundaryCondition
from ..Region.Region import Region
from ..Region.RegionArray import RegionArray
from ..UtilityAndView.abaqusConstants import *


@abaqus_class_doc
class SecondaryBaseBC(BoundaryCondition):
    """The SecondaryBaseBC object stores the data for a secondary base boundary condition.
    The SecondaryBaseBC object is derived from the BoundaryCondition object.

    .. note:: 
        This object can be accessed by::

            import load
            mdb.models[name].boundaryConditions[name]
    """

    #: A String specifying the boundary condition repository key.
    name: str = ""

    #: A tuple of tuples of Ints specifying the constrained degrees-of-freedom.
    dofs: Optional[int] = None

    #: A :py:class:`~abaqus.Region.RegionArray.RegionArray` object specifying the region to which the boundary condition is applied.
    #: Note that the usual **region** is ignored. The default value is MODEL.
    regions: RegionArray = MODEL

    #: A SymbolicConstant specifying the category of the boundary condition. Possible values
    #: are MECHANICAL and THERMAL.
    category: Optional[SymbolicConstant] = None

    #: A :py:class:`~abaqus.Region.Region.Region` object specifying the region to which the boundary condition is applied.
    region: Region = Region()

    #: None or a DatumCsys object specifying the local coordinate system of the boundary
    #: condition's degrees of freedom. If **localCsys** = None, the degrees of freedom are defined
    #: in the global coordinate system. The default value is None.
    localCsys: Optional[str] = None

    @abaqus_method_doc
    def __init__(
        self, name: str, createStepName: str, regions: RegionArray, dofs: tuple
    ):
        """This method creates a SecondaryBaseBC object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].SecondaryBaseBC

        Parameters
        ----------
        name
            A String specifying the boundary condition repository key.
        createStepName
            A String specifying the name of the step in which the boundary condition is created.
        regions
            A :py:class:`~abaqus.Region.RegionArray.RegionArray` object specifying the region to which the boundary condition is applied.
            Note that the usual **region** is ignored. The default value is MODEL.
        dofs
            A sequence of sequences of Ints specifying the constrained degrees-of-freedom.

        Returns
        -------
        SecondaryBaseBC
            A :py:class:`~abaqus.BoundaryCondition.SecondaryBaseBC.SecondaryBaseBC` object.
        """
        super().__init__()

    @abaqus_method_doc
    def setValues(self, *args, **kwargs):
        """This method modifies the data for an existing SecondaryBaseBC object in the step where
        it is created.
        """
        ...

    @abaqus_method_doc
    def setValuesInStep(self, stepName: str):
        """This method modifies the propagating data for an existing SecondaryBaseBC object in the
        specified step.

        Parameters
        ----------
        stepName
            A String specifying the name of the step in which the boundary condition is modified.
        """
        ...
