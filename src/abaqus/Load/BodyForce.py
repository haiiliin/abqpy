from typing import Union, Optional

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from .Load import Load
from ..Region.Region import Region
from ..UtilityAndView.abaqusConstants import SymbolicConstant, UNIFORM, UNSET


@abaqus_class_doc
class BodyForce(Load):
    """The BodyForce object defines a distributed load.
    The BodyForce object is derived from the Load object.

    .. note:: 
        This object can be accessed by::

            import load
            mdb.models[name].loads[name]

        The corresponding analysis keywords are:

        - DLOAD
    """

    #: A String specifying the load repository key.
    name: str = ""

    #: A SymbolicConstant specifying how the load is distributed spatially. Possible values are
    #: UNIFORM, USER_DEFINED, and FIELD. The default value is UNIFORM.
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
        field: str = "",
        distributionType: SymbolicConstant = UNIFORM,
        comp1: Optional[float] = None,
        comp2: Optional[float] = None,
        comp3: Optional[float] = None,
        amplitude: str = UNSET,
    ):
        """This method creates a BodyForce object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].BodyForce

        Parameters
        ----------
        name
            A String specifying the load repository key.
        createStepName
            A String specifying the name of the step in which the load is created.
        region
            A :py:class:`~abaqus.Region.Region.Region` object specifying the region to which the load is applied.
        field
            A String specifying the name of the AnalyticalField object associated with this load.
            The **field** argument applies only when **distributionType** = FIELD. The default value is an
            empty string.
        distributionType
            A SymbolicConstant specifying how the load is distributed spatially. Possible values are
            UNIFORM, USER_DEFINED, and FIELD. The default value is UNIFORM.
        comp1
            A Float or a Complex specifying the body force component in the
            1-direction.Note:Although **comp1**, **comp2**, and **comp3** are optional arguments, at least
            one of them must be nonzero unless **distributionType** = USER_DEFINED.
        comp2
            A Float or a Complex specifying the body force component in the 2-direction.
        comp3
            A Float or a Complex specifying the body force component in the 3-direction.
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
            UNSET should be used if the load has no amplitude reference. The default value is UNSET.
            You should provide the **amplitude** argument only if it is valid for the specified step.

        Returns
        -------
        BodyForce
            A :py:class:`~abaqus.Load.BodyForce.BodyForce` object.
        """
        super().__init__()

    @abaqus_method_doc
    def setValues(
        self,
        field: str = "",
        distributionType: SymbolicConstant = UNIFORM,
        comp1: Optional[float] = None,
        comp2: Optional[float] = None,
        comp3: Optional[float] = None,
        amplitude: str = UNSET,
    ):
        """This method modifies the data for an existing BodyForce object in the step where it is
        created.

        Parameters
        ----------
        field
            A String specifying the name of the AnalyticalField object associated with this load.
            The **field** argument applies only when **distributionType** = FIELD. The default value is an
            empty string.
        distributionType
            A SymbolicConstant specifying how the load is distributed spatially. Possible values are
            UNIFORM, USER_DEFINED, and FIELD. The default value is UNIFORM.
        comp1
            A Float or a Complex specifying the body force component in the
            1-direction.Note:Although **comp1**, **comp2**, and **comp3** are optional arguments, at least
            one of them must be nonzero unless **distributionType** = USER_DEFINED.
        comp2
            A Float or a Complex specifying the body force component in the 2-direction.
        comp3
            A Float or a Complex specifying the body force component in the 3-direction.
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
        comp1: Union[SymbolicConstant, float] = ...,
        comp2: Union[SymbolicConstant, float] = ...,
        comp3: Union[SymbolicConstant, float] = ...,
        amplitude: str = "",
    ):
        """This method modifies the propagating data for an existing BodyForce object in the
        specified step.

        Parameters
        ----------
        stepName
            A String specifying the name of the step in which the load is modified.
        comp1
            A Float, a Complex, or the SymbolicConstant UNCHANGED specifying the body force
            component in the 1-direction. UNCHANGED should be used if the body force component is
            propagated from the previous analysis step.
        comp2
            A Float, a Complex, or the SymbolicConstant UNCHANGED specifying the body force
            component in the 2-direction. UNCHANGED should be used if the body force component is
            propagated from the previous analysis step.
        comp3
            A Float, a Complex, or the SymbolicConstant UNCHANGED specifying the body force
            component in the 3-direction. UNCHANGED should be used if the body force component is
            propagated from the previous analysis step.
        amplitude
            A String or a SymbolicConstant specifying the name of the amplitude reference. Possible
            values for the SymbolicConstant are UNCHANGED and FREED. UNCHANGED should be used if the
            amplitude is propagated from the previous analysis step. FREED should be used if the
            load is changed to have no amplitude reference. You should provide the **amplitude**
            argument only if it is valid for the specified step.
        """
        ...
