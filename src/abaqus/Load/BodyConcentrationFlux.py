from typing import Optional

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from .Load import Load
from ..Region.Region import Region
from ..UtilityAndView.abaqusConstants import SymbolicConstant, UNIFORM, UNSET


@abaqus_class_doc
class BodyConcentrationFlux(Load):
    """The BodyConcentrationFlux object defines body concentration flux from a region or into a
    region.
    The BodyConcentrationFlux object is derived from the Load object.

    .. note:: 
        This object can be accessed by::

            import load
            mdb.models[name].loads[name]
    """

    #: A String specifying the load repository key.
    name: str = ""

    #: A SymbolicConstant specifying how the body concentration flux is distributed spatially.
    #: Possible values are UNIFORM, USER_DEFINED, and FIELD. The default value is UNIFORM.
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
        field: str = "",
        distributionType: SymbolicConstant = UNIFORM,
        amplitude: str = UNSET,
    ):
        """This method creates a BodyConcentrationFlux object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].BodyConcentrationFlux

        Parameters
        ----------
        name
            A String specifying the load repository key.
        createStepName
            A String specifying the name of the step in which the load is created.
        region
            A :py:class:`~abaqus.Region.Region.Region` object specifying the region to which the load is applied.
        magnitude
            A Float specifying the body concentration flux magnitude. **magnitude** is optional if
            **distributionType** = USER_DEFINED.
        field
            A String specifying the name of the AnalyticalField object associated with this load.
            The **field** argument applies only when **distributionType** = FIELD. The default value is an
            empty string.
        distributionType
            A SymbolicConstant specifying how the body concentration flux is distributed spatially.
            Possible values are UNIFORM, USER_DEFINED, and FIELD. The default value is UNIFORM.
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
            UNSET should be used if the load has no amplitude reference. The default value is UNSET.
            You should provide the **amplitude** argument only if it is valid for the specified step.

        Returns
        -------
        BodyConcentrationFlux
            A :py:class:`~abaqus.Load.BodyConcentrationFlux.BodyConcentrationFlux` object.
        """
        super().__init__()

    @abaqus_method_doc
    def setValues(
        self,
        field: str = "",
        distributionType: SymbolicConstant = UNIFORM,
        amplitude: str = UNSET,
    ):
        """This method modifies the data for an existing BodyConcentrationFlux object in the step
        where it is created.

        Parameters
        ----------
        field
            A String specifying the name of the AnalyticalField object associated with this load.
            The **field** argument applies only when **distributionType** = FIELD. The default value is an
            empty string.
        distributionType
            A SymbolicConstant specifying how the body concentration flux is distributed spatially.
            Possible values are UNIFORM, USER_DEFINED, and FIELD. The default value is UNIFORM.
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
        """This method modifies the propagating data for an existing BodyConcentrationFlux object
        in the specified step.

        Parameters
        ----------
        stepName
            A String specifying the name of the step in which the Body heat flux is modified.
        magnitude
            A Float specifying the Body concentration flux magnitude.
        amplitude
            A String or a SymbolicConstant specifying the name of the amplitude reference. Possible
            values for the SymbolicConstant are UNCHANGED and FREED. UNCHANGED should be used if the
            amplitude is propagated from the previous analysis step. FREED should be used if the
            load has no amplitude reference. You should provide the **amplitude** argument only if it
            is valid for the specified step.
        """
        ...
