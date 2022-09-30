from typing import Optional

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from .Load import Load
from ..Datum.DatumAxis import DatumAxis
from ..Region.Region import Region
from ..UtilityAndView.abaqusConstants import APPLY_FORCE, SymbolicConstant, UNSET


@abaqus_class_doc
class BoltLoad(Load):
    """The BoltLoad object defines a bolt load.
    The BoltLoad object is derived from the Load object.

    .. note:: 
        This object can be accessed by::

            import load
            mdb.models[name].loads[name]

        The corresponding analysis keywords are:

        - PRE-TENSION SECTION
                - NODE
        - NSET
    """

    #: A String specifying the load repository key.
    name: str = ""

    #: A :py:class:`~abaqus.Datum.DatumAxis.DatumAxis` object specifying the orientation of the pre-tension section
    #: normal.Note:*datumAxis* is required only for Solid and Shell regions; it has no meaning
    #: for Wire regions.
    datumAxis: DatumAxis = DatumAxis()

    #: A :py:class:`~abaqus.Region.Region.Region` object specifying the region to which the load is applied.
    region: Region = Region()

    @abaqus_method_doc
    def __init__(
        self,
        name: str,
        createStepName: str,
        region: Region,
        magnitude: float,
        datumAxis: DatumAxis,
        boltMethod: SymbolicConstant = APPLY_FORCE,
        amplitude: str = UNSET,
    ):
        """This method creates a BoltLoad object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].BoltLoad

        Parameters
        ----------
        name
            A String specifying the load repository key.
        createStepName
            A String specifying the name of the step in which the load is created. This must be the
            first analysis step name.
        region
            A :py:class:`~abaqus.Region.Region.Region` object specifying the region to which the load is applied.
        magnitude
            A Float specifying the bolt load magnitude.
        datumAxis
            A :py:class:`~abaqus.Datum.DatumAxis.DatumAxis` object specifying the orientation of the pre-tension section normal.Note:
            **datumAxis** is applicable only for Solid and Shell regions; it has no meaning for Wire
            regions.
        boltMethod
            A SymbolicConstant specifying the method of applying the bolt load. Possible values are
            APPLY_FORCE and ADJUST_LENGTH. The default value is APPLY_FORCE.
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
            UNSET should be used if the load has no amplitude reference. The default value is UNSET.
            You should provide the **amplitude** argument only if it is valid for the specified step.

        Returns
        -------
        BoltLoad
            A :py:class:`~abaqus.Load.BoltLoad.BoltLoad` object.

        Raises
        ------
        TextError
        """
        super().__init__()

    @abaqus_method_doc
    def setValues(
        self,
        boltMethod: SymbolicConstant = APPLY_FORCE,
        datumAxis: Optional[DatumAxis] = None, 
        amplitude: str = UNSET,
    ):
        """This method modifies the data for an existing BoltLoad object in the step where it is
        created.

        Parameters
        ----------
        boltMethod
            A SymbolicConstant specifying the method of applying the bolt load. Possible values are
            APPLY_FORCE and ADJUST_LENGTH. The default value is APPLY_FORCE.
        datumAxis
            A :py:class:`~abaqus.Datum.DatumAxis.DatumAxis` object specifying the orientation of the pre-tension section normal.Note:
            **datumAxis** is applicable only for Solid and Shell regions; it has no meaning for Wire
            regions.
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
            UNSET should be used if the load has no amplitude reference. The default value is UNSET.
            You should provide the **amplitude** argument only if it is valid for the specified step.
        """
        ...

    @abaqus_method_doc
    def setValuesInStep(
        self,
        stepName: str,
        boltMethod: SymbolicConstant = APPLY_FORCE,
        magnitude: Optional[float] = None,
        amplitude: str = "",
    ):
        """This method modifies the propagating data for an existing BoltLoad object in the
        specified step.

        Parameters
        ----------
        stepName
            A String specifying the name of the step in which the load is modified.
        boltMethod
            A SymbolicConstant specifying the type of bolt load. Possible values are APPLY_FORCE,
            ADJUST_LENGTH, and FIX_LENGTH. The default is APPLY_FORCE.
        magnitude
            A Float specifying the bolt load magnitude.
        amplitude
            A String or a SymbolicConstant specifying the name of the amplitude reference. Possible
            values for the SymbolicConstant are UNCHANGED and FREED. UNCHANGED should be used if the
            amplitude is propagated from the previous analysis step. FREED should be used if the
            load is changed to have no amplitude reference. You should provide the **amplitude**
            argument only if it is valid for the specified step.
        """
        ...
