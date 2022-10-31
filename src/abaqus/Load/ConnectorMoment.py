from typing import Union, Optional

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from typing_extensions import Literal

from .Load import Load
from ..Region.Region import Region
from ..UtilityAndView.abaqusConstants import UNSET
from ..UtilityAndView.abaqusConstants import abaqusConstants as C


@abaqus_class_doc
class ConnectorMoment(Load):
    """The ConnectorMoment object stores the data for a connector moment.
    The ConnectorMoment object is derived from the Load object.

    .. note::
        This object can be accessed by::

            import load
            mdb.models[name].loads[name]
    """

    #: A String specifying the load repository key.
    name: str = ""

    #: A String specifying the name of the assembled fastener to which the load will be
    #: applied. This argument is not valid when **region** is specified. When this argument is
    #: specified, **fastenerSetName** must also be specified. The default value is an empty
    #: string.
    fastenerName: str = ""

    #: A String specifying the assembled fastener template model set to which the load will be
    #: applied. This argument is not valid when **region** is specified. When this argument is
    #: specified, **fastenerName** must also be specified. The default value is an empty string.
    fastenerSetName: str = ""

    #: A Region object specifying the region to which the load is applied.
    region: Region = Region()

    @abaqus_method_doc
    def __init__(
        self,
        name: str,
        createStepName: str,
        region: str = "",
        fastenerName: str = "",
        fastenerSetName: str = "",
        m1: Optional[float] = None,
        m2: Optional[float] = None,
        m3: Optional[float] = None,
        amplitude: str = UNSET,
    ):
        """This method creates a ConnectorMoment object on a wire region. Alternatively, the load
        may also be applied to a wire set referenced from an assembled fastener template model.

        .. note::
            This function can be accessed by::

                mdb.models[name].ConnectorMoment

        Parameters
        ----------
        name
            A String specifying the load repository key.
        createStepName
            A String specifying the name of the step in which the load is created.
        region
            The wire region to which the load is applied. This argument is not valid when
            **fastenerName** and **fastenerSetName** are specified.
        fastenerName
            A String specifying the name of the assembled fastener to which the load will be
            applied. This argument is not valid when **region** is specified. When this argument is
            specified, **fastenerSetName** must also be specified. The default value is an empty
            string.
        fastenerSetName
            A String specifying the assembled fastener template model set to which the load will be
            applied. This argument is not valid when **region** is specified. When this argument is
            specified, **fastenerName** must also be specified. The default value is an empty string.
        m1
            A Float or a Complex specifying the moment component in the connector's local
            4-direction.
        m2
            A Float or a Complex specifying the moment component in the connector's local
            5-direction.
        m3
            A Float or a Complex specifying the moment component in the connector's local
            6-direction.
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
            UNSET should be used if the load has no amplitude reference. The default value is UNSET.
            You should provide the **amplitude** argument only if it is valid for the specified step.

        Returns
        -------
        ConnectorMoment
            A ConnectorMoment object.
        """
        super().__init__()

    @abaqus_method_doc
    def setValues(
        self,
        region: str = "",
        fastenerName: str = "",
        fastenerSetName: str = "",
        m1: Optional[float] = None,
        m2: Optional[float] = None,
        m3: Optional[float] = None,
        amplitude: str = UNSET,
    ):
        """This method modifies the data for an existing ConnectorMoment object in the step where
        it is created.

        Parameters
        ----------
        region
            The wire region to which the load is applied. This argument is not valid when
            **fastenerName** and **fastenerSetName** are specified.
        fastenerName
            A String specifying the name of the assembled fastener to which the load will be
            applied. This argument is not valid when **region** is specified. When this argument is
            specified, **fastenerSetName** must also be specified. The default value is an empty
            string.
        fastenerSetName
            A String specifying the assembled fastener template model set to which the load will be
            applied. This argument is not valid when **region** is specified. When this argument is
            specified, **fastenerName** must also be specified. The default value is an empty string.
        m1
            A Float or a Complex specifying the moment component in the connector's local
            4-direction.
        m2
            A Float or a Complex specifying the moment component in the connector's local
            5-direction.
        m3
            A Float or a Complex specifying the moment component in the connector's local
            6-direction.
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
        m1: Union[Literal[C.FREED, C.UNCHANGED], float] = ...,
        m2: Union[Literal[C.FREED, C.UNCHANGED], float] = ...,
        m3: Union[Literal[C.FREED, C.UNCHANGED], float] = ...,
        amplitude: str = "",
    ):
        """This method modifies the propagating data for an existing ConnectorMoment object in the
        specified step.

        Parameters
        ----------
        stepName
            A String specifying the name of the step in which the load is modified.
        m1
            A Float, a Complex, or a SymbolicConstant specifying the moment component in the
            connector's local 4-direction. Possible values for the SymbolicConstant are UNCHANGED
            and FREED. UNCHANGED should be used if the load component is propagated from the
            previous static analysis step. Use FREED to remove a previously defined load component.
        m2
            A Float, a Complex, or a SymbolicConstant specifying the moment component in the
            connector's local 5-direction. Possible values for the SymbolicConstant are UNCHANGED
            and FREED. UNCHANGED should be used if the load component is propagated from the
            previous static analysis step. Use FREED to remove a previously defined load component.
        m3
            A Float, a Complex, or a SymbolicConstant specifying the moment component in the
            connector's local 6-direction. Possible values for the SymbolicConstant are UNCHANGED
            and FREED. UNCHANGED should be used if the load component is propagated from the
            previous static analysis step. Use FREED to remove a previously defined load component.
        amplitude
            A String or a SymbolicConstant specifying the name of the amplitude reference. Possible
            values for the SymbolicConstant are UNCHANGED and FREED. UNCHANGED should be used if the
            amplitude is propagated from the previous static analysis step. FREED should be used if
            the load is changed to have no amplitude reference. You should provide the **amplitude**
            argument only if it is valid for the specified step.
        """
        ...
