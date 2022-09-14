import typing

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from .Load import Load
from ..Region.Region import Region
from ..UtilityAndView.abaqusConstants import *


@abaqus_class_doc
class ConcentratedForce(Load):
    """The ConcentratedForce object defines a concentrated force.
    The ConcentratedForce object is derived from the Load object.

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

    #: A Boolean specifying whether the direction of the force rotates with the rotation at
    #: each node of the region. You should provide the **follower** argument only if it is valid
    #: for the specified step. The default value is OFF.
    follower: Boolean = OFF

    #: None or a DatumCsys object specifying the local coordinate system of the load's degrees
    #: of freedom. If **localCsys** = None, the degrees of freedom are defined in the global
    #: coordinate system. When this member is queried, it returns an Int. The default value is
    #: None.
    localCsys: int = None

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
        cf1: float = None,
        cf2: float = None,
        cf3: float = None,
        amplitude: str = UNSET,
        follower: Boolean = OFF,
        localCsys: int = None,
    ):
        """This method creates a ConcentratedForce object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].ConcentratedForce

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
        cf1
            A Float or a Complex specifying the concentrated force component in the 1-direction.
            Although **cf1**, **cf2**, and **cf3** are optional arguments, at least one of them must be
            nonzero.
        cf2
            A Float or a Complex specifying the concentrated force component in the 2-direction.
        cf3
            A Float or a Complex specifying the concentrated force component in the 3-direction.
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
            UNSET should be used if the load has no amplitude reference. The default value is UNSET.
            You should provide the **amplitude** argument only if it is valid for the specified step.
        follower
            A Boolean specifying whether the direction of the force rotates with the rotation at
            each node of the region. You should provide the **follower** argument only if it is valid
            for the specified step. The default value is OFF.
        localCsys
            None or a DatumCsys object specifying the local coordinate system of the load's degrees
            of freedom. If **localCsys** = None, the degrees of freedom are defined in the global
            coordinate system. When this member is queried, it returns an Int. The default value is
            None.

        Returns
        -------
        ConcentratedForce
            A :py:class:`~abaqus.Load.ConcentratedForce.ConcentratedForce` object.
        """
        super().__init__()

    @abaqus_method_doc
    def setValues(
        self,
        distributionType: SymbolicConstant = UNIFORM,
        field: str = "",
        cf1: float = None,
        cf2: float = None,
        cf3: float = None,
        amplitude: str = UNSET,
        follower: Boolean = OFF,
        localCsys: int = None,
    ):
        """This method modifies the data for an existing ConcentratedForce object in the step where
        it is created.

        Parameters
        ----------
        distributionType
            A SymbolicConstant specifying how the load is distributed spatially. Possible values are
            UNIFORM and FIELD. The default value is UNIFORM.
        field
            A String specifying the name of the AnalyticalField object associated with this load.
            The **field** argument applies only when **distributionType** = FIELD. The default value is an
            empty string.
        cf1
            A Float or a Complex specifying the concentrated force component in the 1-direction.
            Although **cf1**, **cf2**, and **cf3** are optional arguments, at least one of them must be
            nonzero.
        cf2
            A Float or a Complex specifying the concentrated force component in the 2-direction.
        cf3
            A Float or a Complex specifying the concentrated force component in the 3-direction.
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
            UNSET should be used if the load has no amplitude reference. The default value is UNSET.
            You should provide the **amplitude** argument only if it is valid for the specified step.
        follower
            A Boolean specifying whether the direction of the force rotates with the rotation at
            each node of the region. You should provide the **follower** argument only if it is valid
            for the specified step. The default value is OFF.
        localCsys
            None or a DatumCsys object specifying the local coordinate system of the load's degrees
            of freedom. If **localCsys** = None, the degrees of freedom are defined in the global
            coordinate system. When this member is queried, it returns an Int. The default value is
            None.
        """
        ...

    @abaqus_method_doc
    def setValuesInStep(
        self,
        stepName: str,
        cf1: typing.Union[SymbolicConstant, float] = None,
        cf2: typing.Union[SymbolicConstant, float] = None,
        cf3: typing.Union[SymbolicConstant, float] = None,
        amplitude: str = "",
    ):
        """This method modifies the propagating data for an existing ConcentratedForce object in
        the specified step.

        Parameters
        ----------
        stepName
            A String specifying the name of the step in which the load is modified.
        cf1
            A Float, a Complex, or the SymbolicConstant UNCHANGED specifying the concentrated force
            component in the 1-direction. UNCHANGED should be used if the concentrated force
            component is propagated from the previous analysis step.
        cf2
            A Float, a Complex, or the SymbolicConstant UNCHANGED specifying the concentrated force
            component in the 2-direction. UNCHANGED should be used if the concentrated force
            component is propagated from the previous analysis step.
        cf3
            A Float, a Complex, or the SymbolicConstant UNCHANGED specifying the concentrated force
            component in the 3-direction. UNCHANGED should be used if the concentrated force
            component is propagated from the previous analysis step.
        amplitude
            A String or a SymbolicConstant specifying the name of the amplitude reference. Possible
            values for the SymbolicConstant are UNCHANGED and FREED. UNCHANGED should be used if the
            amplitude is propagated from the previous analysis step. FREED should be used if the
            load is changed to have no amplitude reference. You should provide the **amplitude**
            argument only if it is valid for the specified step.
        """
        ...
