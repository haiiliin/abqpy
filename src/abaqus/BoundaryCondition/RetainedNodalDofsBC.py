from typing import Optional

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from ..Region.Region import Region
from ..UtilityAndView.abaqusConstants import OFF, Boolean, SymbolicConstant
from .BoundaryCondition import BoundaryCondition


@abaqus_class_doc
class RetainedNodalDofsBC(BoundaryCondition):
    """The RetainedNodalDofsBC object stores the data for a retained nodal dofs boundary condition. The
    RetainedNodalDofsBC object is derived from the BoundaryCondition object.

    .. note::
        This object can be accessed by::

            import load
            mdb.models[name].boundaryConditions[name]
    """

    #: A String specifying the boundary condition repository key.
    name: str = ""

    #: A SymbolicConstant specifying the category of the boundary condition. Possible values
    #: are MECHANICAL and THERMAL.
    category: Optional[SymbolicConstant] = None

    #: A Region object specifying the region to which the boundary condition is applied.
    region: Region = Region()

    #: None or a DatumCsys object specifying the local coordinate system of the boundary
    #: condition's degrees of freedom. If **localCsys** = None, the degrees of freedom are defined
    #: in the global coordinate system. The default value is None.
    localCsys: Optional[str] = None

    @abaqus_method_doc
    def __init__(
        self,
        name: str,
        createStepName: str,
        region: Region,
        u1: Boolean = OFF,
        u2: Boolean = OFF,
        u3: Boolean = OFF,
        ur1: Boolean = OFF,
        ur2: Boolean = OFF,
        ur3: Boolean = OFF,
    ):
        """This method creates a RetainedNodalDofsBC object.

        .. note::
            This function can be accessed by::

                mdb.models[name].RetainedNodalDofsBC

        Parameters
        ----------
        name
            A String specifying the boundary condition repository key.
        createStepName
            A String specifying the name of the step in which the boundary condition is created.
        region
            A Region object specifying the region to which the boundary condition is applied.
        u1
            A Boolean specifying whether to retain the degree of freedom in the 1-direction. The
            default value is OFF indicating that the degree of freedom is not retained.
        u2
            A Boolean specifying whether to retain the degree of freedom in the 2-direction. The
            default value is OFF indicating that the degree of freedom is not retained.
        u3
            A Boolean specifying whether to retain the degree of freedom in the 3-direction. The
            default value is OFF indicating that the degree of freedom is not retained.
        ur1
            A Boolean specifying whether to retain the rotational degree of freedom about the
            1-direction. The default value is OFF indicating that the degree of freedom is not
            retained.
        ur2
            A Boolean specifying whether to retain the rotational degree of freedom about the
            2-direction. The default value is OFF indicating that the degree of freedom is not
            retained.
        ur3
            A Boolean specifying whether to retain the rotational degree of freedom about the
            3-direction. The default value is OFF indicating that the degree of freedom is not
            retained.

        Returns
        -------
        RetainedNodalDofsBC
            A RetainedNodalDofsBC object.
        """
        super().__init__()

    @abaqus_method_doc
    def setValues(
        self,
        u1: Boolean = OFF,
        u2: Boolean = OFF,
        u3: Boolean = OFF,
        ur1: Boolean = OFF,
        ur2: Boolean = OFF,
        ur3: Boolean = OFF,
    ):
        """This method modifies the data for an existing RetainedNodalDofsBC object in the step where it is
        created.

        Parameters
        ----------
        u1
            A Boolean specifying whether to retain the degree of freedom in the 1-direction. The
            default value is OFF indicating that the degree of freedom is not retained.
        u2
            A Boolean specifying whether to retain the degree of freedom in the 2-direction. The
            default value is OFF indicating that the degree of freedom is not retained.
        u3
            A Boolean specifying whether to retain the degree of freedom in the 3-direction. The
            default value is OFF indicating that the degree of freedom is not retained.
        ur1
            A Boolean specifying whether to retain the rotational degree of freedom about the
            1-direction. The default value is OFF indicating that the degree of freedom is not
            retained.
        ur2
            A Boolean specifying whether to retain the rotational degree of freedom about the
            2-direction. The default value is OFF indicating that the degree of freedom is not
            retained.
        ur3
            A Boolean specifying whether to retain the rotational degree of freedom about the
            3-direction. The default value is OFF indicating that the degree of freedom is not
            retained.
        """
        ...

    @abaqus_method_doc
    def setValuesInStep(
        self,
        stepName: str,
        u1: Boolean = OFF,
        u2: Boolean = OFF,
        u3: Boolean = OFF,
        ur1: Boolean = OFF,
        ur2: Boolean = OFF,
        ur3: Boolean = OFF,
    ):
        """This method modifies the propagating data for an existing RetainedNodalDofsBC object in the specified
        step.

        Parameters
        ----------
        stepName
            A String specifying the name of the step in which the boundary condition is modified.
        u1
            A Boolean specifying whether to retain the degree of freedom in the 1-direction.
        u2
            A Boolean specifying whether to retain the degree of freedom in the 2-direction.
        u3
            A Boolean specifying whether to retain the degree of freedom in the 3-direction.
        ur1
            A Boolean specifying whether to retain the rotational degree of freedom about the
            1-direction.
        ur2
            A Boolean specifying whether to retain the rotational degree of freedom about the
            2-direction.
        ur3
            A Boolean specifying whether to retain the rotational degree of freedom about the
            3-direction.
        """
        ...
