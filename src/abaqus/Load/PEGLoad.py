from typing import Optional

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from .Load import Load
from ..Region.Region import Region
from ..UtilityAndView.abaqusConstants import *


@abaqus_class_doc
class PEGLoad(Load):
    """The PEGLoad object stores the data for a PEG load.
    The PEGLoad object is derived from the Load object.

    .. note:: 
        This object can be accessed by::

            import load
            mdb.models[name].loads[name]
    """

    #: A String specifying the load repository key.
    name: str = ""

    #: A SymbolicConstant specifying how the load is distributed spatially. Possible values are
    #: UNIFORM and FIELD. The default value is UNIFORM.
    distributionType: SymbolicConstant = UNIFORM

    #: A String specifying the name of the AnalyticalField object associated with this load.
    #: The **field** argument applies only when **distributionType** = FIELD. The default value is an
    #: empty string.
    field: str = ""

    #: A :py:class:`~abaqus.Region.Region.Region` object specifying the region to which the load is applied.
    region: Region = Region()

    @abaqus_method_doc
    def __init__(
        self,
        name: str,
        createStepName: str,
        region: Region,
        distributionType: SymbolicConstant = UNIFORM,
        field: str = "",
        comp1: Optional[float] = None,
        comp2: Optional[float] = None,
        comp3: Optional[float] = None,
        amplitude: str = UNSET,
    ):
        """This method creates a PEGLoad object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].PEGLoad

        Parameters
        ----------
        name
            A String specifying the load repository key.
        createStepName
            A String specifying the name of the step in which the load is created.
        region
            A :py:class:`~abaqus.Region.Region.Region` object specifying the region to which the load is applied.
        distributionType
            A SymbolicConstant specifying how the load is distributed spatially. Possible values are
            UNIFORM and FIELD. The default value is UNIFORM.
        field
            A String specifying the name of the AnalyticalField object associated with this load.
            The **field** argument applies only when **distributionType** = FIELD. The default value is an
            empty string.
        comp1
            A Float or a Complex specifying the load component at dof 1 of reference node
            1.Note:Although **comp1**, **comp2**, and **comp3** are optional arguments, at least one of
            them must be nonzero.
        comp2
            A Float or a Complex specifying the load component at dof 1 of reference node 2.
        comp3
            A Float or a Complex specifying the load component at dof 2 of reference node 2.
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
            UNSET should be used if the load has no amplitude reference. The default value is UNSET.
            You should provide the **amplitude** argument only if it is valid for the specified step.

        Returns
        -------
        PEGLoad
            A :py:class:`~abaqus.Load.PEGLoad.PEGLoad` object.
        """
        super().__init__()

    @abaqus_method_doc
    def setValues(
        self,
        distributionType: SymbolicConstant = UNIFORM,
        field: str = "",
        comp1: Optional[float] = None,
        comp2: Optional[float] = None,
        comp3: Optional[float] = None,
        amplitude: str = UNSET,
    ):
        """This method modifies the data for an existing PEGLoad object in the step where it is
        created.

        Parameters
        ----------
        distributionType
            A SymbolicConstant specifying how the load is distributed spatially. Possible values are
            UNIFORM and FIELD. The default value is UNIFORM.
        field
            A String specifying the name of the AnalyticalField object associated with this load.
            The **field** argument applies only when **distributionType** = FIELD. The default value is an
            empty string.
        comp1
            A Float or a Complex specifying the load component at dof 1 of reference node
            1.Note:Although **comp1**, **comp2**, and **comp3** are optional arguments, at least one of
            them must be nonzero.
        comp2
            A Float or a Complex specifying the load component at dof 1 of reference node 2.
        comp3
            A Float or a Complex specifying the load component at dof 2 of reference node 2.
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
        comp1: Union[SymbolicConstant, float] = None,
        comp2: Union[SymbolicConstant, float] = None,
        comp3: Union[SymbolicConstant, float] = None,
        amplitude: str = "",
    ):
        """This method modifies the propagating data for an existing PEGLoad object in the
        specified step.

        Parameters
        ----------
        stepName
            A String specifying the name of the step in which the load is modified.
        comp1
            A Float, a Complex, or a SymbolicConstant specifying the load component at dof 1 of
            reference node 1. Possible values for the SymbolicConstant are UNCHANGED and FREED.
            UNCHANGED should be used if the load component is propagated from the previous static
            analysis step. Use FREED to remove a previously defined load component.
        comp2
            A Float, a Complex, or a SymbolicConstant specifying the load component at dof 1 of
            reference node 2. For details see **comp1**.
        comp3
            A Float, a Complex, or a SymbolicConstant specifying the load component at dof 2 of
            reference node 2. For details see **comp1**.
        amplitude
            A String or a SymbolicConstant specifying the name of the amplitude reference. Possible
            values for the SymbolicConstant are UNCHANGED and FREED. UNCHANGED should be used if the
            amplitude is propagated from the previous static analysis step. FREED should be used if
            the load is changed to have no amplitude reference. You should provide the **amplitude**
            argument only if it is valid for the specified step.
        """
        ...
