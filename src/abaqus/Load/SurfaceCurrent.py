from typing import Optional

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from typing_extensions import Literal

from .Load import Load
from ..Region.Region import Region
from ..UtilityAndView.abaqusConstants import SymbolicConstant, UNIFORM, UNSET
from ..UtilityAndView.abaqusConstants import abaqusConstants as C


@abaqus_class_doc
class SurfaceCurrent(Load):
    """The SurfaceCurrent object stores the data for a surface current.
    The SurfaceCurrent object is derived from the Load object.

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
        magnitude: float,
        distributionType: Literal[C.FIELD, C.UNIFORM] = UNIFORM,
        field: str = "",
        amplitude: str = UNSET,
    ):
        """This method creates a SurfaceCurrent object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].SurfaceCurrent

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
            A Float specifying the load magnitude.
        distributionType
            A SymbolicConstant specifying how the load is distributed spatially. Possible values are
            UNIFORM and FIELD. The default value is UNIFORM.
        field
            A String specifying the name of the AnalyticalField object associated with this load.
            The **field** argument applies only when **distributionType** = FIELD. The default value is an
            empty string.
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
            UNSET should be used if the load has no amplitude reference. The default value is UNSET.
            You should provide the **amplitude** argument only if it is valid for the specified step.

        Returns
        -------
        SurfaceCurrent
            A :py:class:`~abaqus.Load.SurfaceCurrent.SurfaceCurrent` object.
        """
        super().__init__()

    @abaqus_method_doc
    def setValues(
        self,
        distributionType: Literal[C.FIELD, C.UNIFORM] = UNIFORM,
        field: str = "",
        amplitude: str = UNSET,
    ):
        """This method modifies the data for an existing SurfaceCurrent object in the step where it
        is created.

        Parameters
        ----------
        distributionType
            A SymbolicConstant specifying how the load is distributed spatially. Possible values are
            UNIFORM and FIELD. The default value is UNIFORM.
        field
            A String specifying the name of the AnalyticalField object associated with this load.
            The **field** argument applies only when **distributionType** = FIELD. The default value is an
            empty string.
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
            UNSET should be used if the load has no amplitude reference. The default value is UNSET.
            You should provide the **amplitude** argument only if it is valid for the specified step.
        """
        ...

    @abaqus_method_doc
    def setValuesInStep(
        self, stepName: str, magnitude: Optional[float] = None, amplitude: str = ""
    ):
        """This method modifies the propagating data for an existing SurfaceCurrent object in the
        specified step.

        Parameters
        ----------
        stepName
            A String specifying the name of the step in which the load is modified.
        magnitude
            A Float specifying the load magnitude.
        amplitude
            A String or a SymbolicConstant specifying the name of the amplitude reference. Possible
            values for the SymbolicConstant are UNCHANGED and FREED. UNCHANGED should be used if the
            amplitude is propagated from the previous static analysis step. FREED should be used if
            the load is changed to have no amplitude reference. You should provide the **amplitude**
            argument only if it is valid for the specified step.
        """
        ...
