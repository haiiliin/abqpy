from typing import Optional, Union

from typing_extensions import Literal

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from ..Datum.DatumCsys import DatumCsys
from ..Region.Region import Region
from ..UtilityAndView.abaqusConstants import (
    INDEPENDENT,
    MECHANICAL,
    UNSET,
    SymbolicConstant,
)
from ..UtilityAndView.abaqusConstants import abaqusConstants as C
from .AdaptiveMeshConstraint import AdaptiveMeshConstraint


@abaqus_class_doc
class DisplacementAdaptiveMeshConstraint(AdaptiveMeshConstraint):
    """The AdaptivityProcess object defines a series of jobs that will be submitted for analysis. Abaqus
    performs adaptive remeshing between each job.

    .. note::
        This object can be accessed by::

            import step
            mdb.models[name].adaptiveMeshConstraints[name]
    """

    #: A String specifying the adaptive mesh constraint repository key.
    name: str = ""

    #: A SymbolicConstant specifying the category of the adaptive mesh constraint. Possible
    #: values are MECHANICAL and THERMAL.
    category: Optional[SymbolicConstant] = None

    #: A Region object specifying the region to which the adaptive mesh constraint is applied.
    region: Region = Region()

    #: None or a DatumCsys object specifying the local coordinate system of the adaptive mesh
    #: constraint's degrees of freedom. If **localCsys** = None, the degrees of freedom are defined
    #: in the global coordinate system. The default value is None.
    localCsys: Optional[str] = None

    @abaqus_method_doc
    def __init__(
        self,
        name: str,
        createStepName: str,
        region: Region,
        u1: Union[Literal[C.SET, C.UNSET], float] = UNSET,
        u2: Union[Literal[C.SET, C.UNSET], float] = UNSET,
        u3: Union[Literal[C.SET, C.UNSET], float] = UNSET,
        ur1: Union[Literal[C.SET, C.UNSET], float] = UNSET,
        ur2: Union[Literal[C.SET, C.UNSET], float] = UNSET,
        ur3: Union[Literal[C.SET, C.UNSET], float] = UNSET,
        amplitude: str = UNSET,
        motionType: Literal[C.USER_DEFINED, C.INDEPENDENT, C.FOLLOW] = INDEPENDENT,
        localCsys: Optional[DatumCsys] = None,
    ):
        """This method creates a DisplacementAdaptiveMeshConstraint object.

        .. note::
            This function can be accessed by::

                mdb.models[name].DisplacementAdaptiveMeshConstraint

        Parameters
        ----------
        name
            A String specifying the adaptive mesh constraint repository key.
        createStepName
            A String specifying the name of the step in which the adaptive mesh constraint is
            created.
        region
            A Region object specifying the region to which the adaptive mesh constraint is applied.
        u1
            A Float or a SymbolicConstant specifying the displacement component in the 1-direction.
            Possible values for the SymbolicConstant are UNSET and SET. The default value is
            UNSET. Note: Although **u1**, **u2**, **u3**, **ur1**, **ur2**, and **ur3** are optional arguments, at
            least one of them must be specified.
        u2
            A Float or a SymbolicConstant specifying the displacement component in the 2-direction.
            Possible values for the SymbolicConstant are UNSET and SET. The default value is UNSET.
        u3
            A Float or a SymbolicConstant specifying the displacement component in the 3-direction.
            Possible values for the SymbolicConstant are UNSET and SET. The default value is UNSET.
        ur1
            A Float or a SymbolicConstant specifying the rotational displacement component about the
            1-direction. Possible values for the SymbolicConstant are UNSET and SET. The default
            value is UNSET.
        ur2
            A Float or a SymbolicConstant specifying the rotational displacement component about the
            2-direction. Possible values for the SymbolicConstant are UNSET and SET. The default
            value is UNSET.
        ur3
            A Float or a SymbolicConstant specifying the rotational displacement component about the
            3-direction. Possible values for the SymbolicConstant are UNSET and SET. The default
            value is UNSET.
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
            UNSET should be used if the adaptive mesh constraint has no amplitude reference. The
            default value is UNSET. You should provide the **amplitude** argument only if it is valid
            for the specified step.
        motionType
            A SymbolicConstant specifying the mesh motion in relation to the underlying material.
            Possible values are INDEPENDENT, FOLLOW and USER_DEFINED. The default value is
            INDEPENDENT.
        localCsys
            None or a DatumCsys object specifying the local coordinate system of the adaptive mesh
            constraint's degrees of freedom. If **localCsys** = None, the degrees of freedom are defined
            in the global coordinate system. The default value is None.

        Returns
        -------
        DisplacementAdaptiveMeshConstraint
            A DisplacementAdaptiveMeshConstraint object.
        """
        super().__init__(name, region=region, category=MECHANICAL, localCsys=localCsys)

    @abaqus_method_doc
    def setValues(
        self,
        u1: Union[Literal[C.SET, C.UNSET], float] = UNSET,
        u2: Union[Literal[C.SET, C.UNSET], float] = UNSET,
        u3: Union[Literal[C.SET, C.UNSET], float] = UNSET,
        ur1: Union[Literal[C.SET, C.UNSET], float] = UNSET,
        ur2: Union[Literal[C.SET, C.UNSET], float] = UNSET,
        ur3: Union[Literal[C.SET, C.UNSET], float] = UNSET,
        amplitude: str = UNSET,
        motionType: Literal[C.USER_DEFINED, C.INDEPENDENT, C.FOLLOW] = INDEPENDENT,
        localCsys: Optional[str] = None,
    ):
        """This method modifies the data for an existing DisplacementAdaptiveMeshConstraint object in the step
        where it is created.

        Parameters
        ----------
        u1
            A Float or a SymbolicConstant specifying the displacement component in the 1-direction.
            Possible values for the SymbolicConstant are UNSET and SET. The default value is
            UNSET. Note: Although **u1**, **u2**, **u3**, **ur1**, **ur2**, and **ur3** are optional arguments, at
            least one of them must be specified.
        u2
            A Float or a SymbolicConstant specifying the displacement component in the 2-direction.
            Possible values for the SymbolicConstant are UNSET and SET. The default value is UNSET.
        u3
            A Float or a SymbolicConstant specifying the displacement component in the 3-direction.
            Possible values for the SymbolicConstant are UNSET and SET. The default value is UNSET.
        ur1
            A Float or a SymbolicConstant specifying the rotational displacement component about the
            1-direction. Possible values for the SymbolicConstant are UNSET and SET. The default
            value is UNSET.
        ur2
            A Float or a SymbolicConstant specifying the rotational displacement component about the
            2-direction. Possible values for the SymbolicConstant are UNSET and SET. The default
            value is UNSET.
        ur3
            A Float or a SymbolicConstant specifying the rotational displacement component about the
            3-direction. Possible values for the SymbolicConstant are UNSET and SET. The default
            value is UNSET.
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
            UNSET should be used if the adaptive mesh constraint has no amplitude reference. The
            default value is UNSET. You should provide the **amplitude** argument only if it is valid
            for the specified step.
        motionType
            A SymbolicConstant specifying the mesh motion in relation to the underlying material.
            Possible values are INDEPENDENT, FOLLOW and USER_DEFINED. The default value is
            INDEPENDENT.
        localCsys
            None or a DatumCsys object specifying the local coordinate system of the adaptive mesh
            constraint's degrees of freedom. If **localCsys** = None, the degrees of freedom are defined
            in the global coordinate system. The default value is None.
        """
        ...

    @abaqus_method_doc
    def setValuesInStep(
        self,
        stepName: str,
        u1: Union[Literal[C.SET, C.FREED, C.UNCHANGED], float, None] = None,
        u2: Union[Literal[C.SET, C.FREED, C.UNCHANGED], float, None] = None,
        u3: Union[Literal[C.SET, C.FREED, C.UNCHANGED], float, None] = None,
        ur1: Union[Literal[C.SET, C.FREED, C.UNCHANGED], float, None] = None,
        ur2: Union[Literal[C.SET, C.FREED, C.UNCHANGED], float, None] = None,
        ur3: Union[Literal[C.SET, C.FREED, C.UNCHANGED], float, None] = None,
        amplitude: str = "",
    ):
        """This method modifies the propagating data for an existing DisplacementAdaptiveMeshConstraint object
        in the specified step.

        Parameters
        ----------
        stepName
            A String specifying the name of the step in which the adaptive mesh constraint is
            modified.
        u1
            A Float or a SymbolicConstant specifying the displacement component in the 1-direction.
            Possible values for the SymbolicConstant are SET, UNCHANGED, and FREED.
        u2
            A Float or a SymbolicConstant specifying the displacement component in the 2-direction.
            Possible values for the SymbolicConstant are SET, UNCHANGED, and FREED.
        u3
            A Float or a SymbolicConstant specifying the displacement component in the 3-direction.
            Possible values for the SymbolicConstant are SET, UNCHANGED, and FREED.
        ur1
            A Float or a SymbolicConstant specifying the rotational displacement component about the
            1-direction. Possible values for the SymbolicConstant are SET, UNCHANGED, and FREED.
        ur2
            A Float or a SymbolicConstant specifying the rotational displacement component about the
            2-direction. Possible values for the SymbolicConstant are SET, UNCHANGED, and FREED.
        ur3
            A Float or a SymbolicConstant specifying the rotational displacement component about the
            3-direction. Possible values for the SymbolicConstant are SET, UNCHANGED, and FREED.
        amplitude
            A String or a SymbolicConstant specifying the name of the amplitude reference. Possible
            values for the SymbolicConstant are UNCHANGED and FREED. UNCHANGED should be used if the
            amplitude is propagated from the previous analysis step. FREED should be used if the
            adaptive mesh constraint is changed to have no amplitude reference. You should provide
            the **amplitude** argument only if it is valid for the specified step.
        """
        ...
