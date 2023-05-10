from typing_extensions import Literal

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from ..Region.Region import Region
from ..UtilityAndView.abaqusConstants import UNIFORM, UNSET, SymbolicConstant
from ..UtilityAndView.abaqusConstants import abaqusConstants as C
from .Load import Load


@abaqus_class_doc
class SurfaceCurrentDensity(Load):
    """The SurfaceCurrentDensity object stores the data for a surface current. The SurfaceCurrentDensity object
    is derived from the Load object.

    .. note::
        This object can be accessed by::

            import load
            mdb.models[name].loads[name]
    """

    #: A String specifying the load repository key.
    name: str = ""

    #: A SymbolicConstant specifying how the load is distributed spatially. Possible values are
    #: UNIFORM and USER_DEFINED. The default value is UNIFORM.
    distributionType: SymbolicConstant = UNIFORM

    #: A Region object specifying the region to which the load is applied.
    region: Region = Region()

    @abaqus_method_doc
    def __init__(
        self,
        name: str,
        createStepName: str,
        region: Region,
        comp1: str,
        comp2: str,
        comp3: str,
        distributionType: Literal[C.USER_DEFINED, C.UNIFORM] = UNIFORM,
        amplitude: str = UNSET,
    ):
        """This method creates a SurfaceCurrentDensity object.

        .. note::
            This function can be accessed by::

                mdb.models[name].SurfaceCurrentDensity

        Parameters
        ----------
        name
            A String specifying the load repository key.
        createStepName
            A String specifying the name of the step in which the load is created. This must be the
            first analysis step name.
        region
            A Region object specifying the region to which the load is applied.
        comp1
            A Complex specifying the first component of the load.
        comp2
            A Complex specifying the second component of the load.
        comp3
            A Complex specifying the third component of the load.
        distributionType
            A SymbolicConstant specifying how the load is distributed spatially. Possible values are
            UNIFORM and USER_DEFINED. The default value is UNIFORM.
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
            UNSET should be used if the load has no amplitude reference. The default value is UNSET.
            You should provide the **amplitude** argument only if it is valid for the specified step.

        Returns
        -------
        SurfaceCurrentDensity
            A SurfaceCurrentDensity object.
        """
        super().__init__()

    @abaqus_method_doc
    def setValues(self, distributionType: Literal[C.USER_DEFINED, C.UNIFORM] = UNIFORM, amplitude: str = UNSET):
        """This method modifies the data for an existing SurfaceCurrentDensity object in the step where it is
        created.

        Parameters
        ----------
        distributionType
            A SymbolicConstant specifying how the load is distributed spatially. Possible values are
            UNIFORM and USER_DEFINED. The default value is UNIFORM.
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
        comp1: str = "",
        comp2: str = "",
        comp3: str = "",
        amplitude: str = "",
    ):
        """This method modifies the propagating data for an existing SurfaceCurrentDensity object in the
        specified step.

        Parameters
        ----------
        stepName
            A String specifying the name of the step in which the load is modified.
        comp1
            A Complex specifying the first component of the load.
        comp2
            A Complex specifying the second component of the load.
        comp3
            A Complex specifying the third component of the load.
        amplitude
            A String or a SymbolicConstant specifying the name of the amplitude reference. Possible
            values for the SymbolicConstant are UNCHANGED and FREED. UNCHANGED should be used if the
            amplitude is propagated from the previous static analysis step. FREED should be used if
            the load is changed to have no amplitude reference. You should provide the **amplitude**
            argument only if it is valid for the specified step.
        """
        ...
