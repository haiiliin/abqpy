from typing_extensions import Literal
from typing import Union, Optional

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from .Load import Load
from ..Region.Region import Region
from ..UtilityAndView.abaqusConstants import abaqusConstants as C
from ..UtilityAndView.abaqusConstants import GLOBAL, SymbolicConstant, UNIFORM, UNSET


@abaqus_class_doc
class LineLoad(Load):
    """The LineLoad object stores the data of an applied line load.
    The LineLoad object is derived from the Load object.

    .. note:: 
        This object can be accessed by::

            import load
            mdb.models[name].loads[name]
    """

    #: A String specifying the load repository key.
    name: str = ""

    #: A SymbolicConstant specifying how the load is distributed spatially. Possible values are
    #: UNIFORM, USER_DEFINED, and FIELD. The default value is UNIFORM.
    distributionType: SymbolicConstant = UNIFORM

    #: A SymbolicConstant specifying whether the load is applied in a global or the beam local
    #: frame of reference. Possible values are GLOBAL and LOCAL. The default value is GLOBAL.
    system: SymbolicConstant = GLOBAL

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
        distributionType: Literal[C.USER_DEFINED, C.FIELD, C.UNIFORM] = UNIFORM,
        field: str = "",
        comp1: Optional[float] = None,
        comp2: Optional[float] = None,
        comp3: Optional[float] = None,
        amplitude: str = UNSET,
        system: Literal[C.LOCAL, C.GLOBAL] = GLOBAL,
    ):
        """This method creates a LineLoad object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].LineLoad

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
            UNIFORM, USER_DEFINED, and FIELD. The default value is UNIFORM.
        field
            A String specifying the name of the AnalyticalField object associated with this load.
            The **field** argument applies only when **distributionType** = FIELD. The default value is an
            empty string.
        comp1
            A Float or a Complex specifying the component of the load in the global or the beam
            local 1-direction.Note:Although **comp1**, **comp2**, and **comp3** are optional arguments, at
            least one of them must be nonzero unless **distributionType** = USER_DEFINED.
        comp2
            A Float or a Complex specifying the component of the load in the global or the beam
            local 2-direction.
        comp3
            A Float or a Complex specifying the component of the load in the global 3-direction.
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
            UNSET should be used if the load has no amplitude reference. The default value is UNSET.
            You should provide the **amplitude** argument only if it is valid for the specified step.
        system
            A SymbolicConstant specifying whether the load is applied in a global or the beam local
            frame of reference. Possible values are GLOBAL and LOCAL. The default value is GLOBAL.

        Returns
        -------
        LineLoad
            A :py:class:`~abaqus.Load.LineLoad.LineLoad` object.
        """
        super().__init__()

    @abaqus_method_doc
    def setValues(
        self,
        distributionType: Literal[C.USER_DEFINED, C.FIELD, C.UNIFORM] = UNIFORM,
        field: str = "",
        comp1: Optional[float] = None,
        comp2: Optional[float] = None,
        comp3: Optional[float] = None,
        amplitude: str = UNSET,
        system: Literal[C.LOCAL, C.GLOBAL] = GLOBAL,
    ):
        """This method modifies the data for an existing LineLoad object in the step where it is
        created.

        Parameters
        ----------
        distributionType
            A SymbolicConstant specifying how the load is distributed spatially. Possible values are
            UNIFORM, USER_DEFINED, and FIELD. The default value is UNIFORM.
        field
            A String specifying the name of the AnalyticalField object associated with this load.
            The **field** argument applies only when **distributionType** = FIELD. The default value is an
            empty string.
        comp1
            A Float or a Complex specifying the component of the load in the global or the beam
            local 1-direction.Note:Although **comp1**, **comp2**, and **comp3** are optional arguments, at
            least one of them must be nonzero unless **distributionType** = USER_DEFINED.
        comp2
            A Float or a Complex specifying the component of the load in the global or the beam
            local 2-direction.
        comp3
            A Float or a Complex specifying the component of the load in the global 3-direction.
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
            UNSET should be used if the load has no amplitude reference. The default value is UNSET.
            You should provide the **amplitude** argument only if it is valid for the specified step.
        system
            A SymbolicConstant specifying whether the load is applied in a global or the beam local
            frame of reference. Possible values are GLOBAL and LOCAL. The default value is GLOBAL.
        """
        ...

    @abaqus_method_doc
    def setValuesInStep(
        self,
        stepName: str,
        comp1: Union[Literal[C.FREED, C.UNCHANGED], float] = ...,
        comp2: Union[SymbolicConstant, float] = ...,
        comp3: Union[SymbolicConstant, float] = ...,
        amplitude: str = "",
    ):
        """This method modifies the propagating data for an existing LineLoad object in the
        specified step.

        Parameters
        ----------
        stepName
            A String specifying the name of the step in which the load is modified.
        comp1
            A Float, a Complex, or a SymbolicConstant specifying the load component in the global or
            the beam local 1-direction. Possible values for the SymbolicConstant are UNCHANGED and
            FREED. UNCHANGED should be used if the load component is propagated from the previous
            static analysis step. Use FREED to remove a previously defined load component.
        comp2
            A Float, a Complex, or a SymbolicConstant specifying the load component in the global or
            the beam local 2-direction. For details see **comp1**.
        comp3
            A Float, a Complex, or a SymbolicConstant specifying the load component in the global
            3-direction. For details see **comp1**.
        amplitude
            A String or a SymbolicConstant specifying the name of the amplitude reference. Possible
            values for the SymbolicConstant are UNCHANGED and FREED. UNCHANGED should be used if the
            amplitude is propagated from the previous static analysis step. FREED should be used if
            the load is changed to have no amplitude reference. You should provide the **amplitude**
            argument only if it is valid for the specified step.
        """
        ...
