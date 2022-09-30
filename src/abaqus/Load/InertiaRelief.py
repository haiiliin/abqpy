from typing import Optional

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from .Load import Load
from ..Region.Region import Region
from ..UtilityAndView.abaqusConstants import Boolean, OFF


@abaqus_class_doc
class InertiaRelief(Load):
    """The InertiaRelief object defines an inertia relief load.
    The InertiaRelief object is derived from the Load object.

    .. note:: 
        This object can be accessed by::

            import load
            mdb.models[name].loads[name]
    """

    #: A String specifying the load repository key.
    name: str = ""

    #: None or a DatumCsys object specifying the local coordinate system of the rigid body
    #: degrees of freedom for the inertia relief load. If **localCoordinates** = None, the free
    #: directions are defined in the global coordinate system. When this member is queried, it
    #: returns an Int. The default value is None.
    localCoordinates: Optional[int] = None

    #: A :py:class:`~abaqus.Region.Region.Region` object specifying the region to which the load is applied.
    region: Region = Region()

    @abaqus_method_doc
    def __init__(
        self,
        name: str,
        createStepName: str,
        u1: Boolean = OFF,
        u2: Boolean = OFF,
        u3: Boolean = OFF,
        ur1: Boolean = OFF,
        ur2: Boolean = OFF,
        ur3: Boolean = OFF,
        referencePoint: tuple = (),
        localCoordinates: Optional[int] = None,
    ):
        """This method creates an InertiaRelief object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].InertiaRelief

        Parameters
        ----------
        name
            A String specifying the load repository key.
        createStepName
            A String specifying the name of the step in which the load is created.
        u1
            A Boolean specifying the 1-direction as a free direction.Note:Although **u1**, **u2**, **u3**,
            **ur1**, **ur2**, and **ur3** are optional arguments, at least one of them must be specified.
            Further, any specified set of free directions cannot include only two rotational degrees
            of freedom.
        u2
            A Boolean specifying the 2-direction as a free direction.
        u3
            A Boolean specifying the 3-direction as a free direction.
        ur1
            A Boolean specifying the rotation about the 1-direction as a free direction.
        ur2
            A Boolean specifying the rotation about the 2-direction as a free direction.
        ur3
            A Boolean specifying the rotation about the 3-direction as a free direction.
        referencePoint
            A sequence of Floats specifying the **X**, **Y** and **Z**-coordinates of a fixed rotation
            point or a point on the rotation axis or a point on the symmetry line, about which
            rotations are defined. Such a point must be specified only for certain combinations of
            free directions.
        localCoordinates
            None or a DatumCsys object specifying the local coordinate system of the rigid body
            degrees of freedom for the inertia relief load. If **localCoordinates** = None, the free
            directions are defined in the global coordinate system. When this member is queried, it
            returns an Int. The default value is None.

        Returns
        -------
        InertiaRelief
            An :py:class:`~abaqus.Load.InertiaRelief.InertiaRelief` object.
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
        referencePoint: tuple = (),
        localCoordinates: Optional[int] = None,
    ):
        """This method modifies the data for an existing InertiaRelief object in the step where it
        is created.

        Parameters
        ----------
        u1
            A Boolean specifying the 1-direction as a free direction.Note:Although **u1**, **u2**, **u3**,
            **ur1**, **ur2**, and **ur3** are optional arguments, at least one of them must be specified.
            Further, any specified set of free directions cannot include only two rotational degrees
            of freedom.
        u2
            A Boolean specifying the 2-direction as a free direction.
        u3
            A Boolean specifying the 3-direction as a free direction.
        ur1
            A Boolean specifying the rotation about the 1-direction as a free direction.
        ur2
            A Boolean specifying the rotation about the 2-direction as a free direction.
        ur3
            A Boolean specifying the rotation about the 3-direction as a free direction.
        referencePoint
            A sequence of Floats specifying the **X**, **Y** and **Z**-coordinates of a fixed rotation
            point or a point on the rotation axis or a point on the symmetry line, about which
            rotations are defined. Such a point must be specified only for certain combinations of
            free directions.
        localCoordinates
            None or a DatumCsys object specifying the local coordinate system of the rigid body
            degrees of freedom for the inertia relief load. If **localCoordinates** = None, the free
            directions are defined in the global coordinate system. When this member is queried, it
            returns an Int. The default value is None.
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
        referencePoint: tuple = (),
        fixed: Boolean = OFF,
    ):
        """This method modifies the propagating data for an existing InertiaRelief object in the
        specified step.

        Parameters
        ----------
        stepName
            A String specifying the name of the step in which the load is modified.
        u1
            A Boolean specifying the 1-direction as a free direction.
        u2
            A Boolean specifying the 2-direction as a free direction.
        u3
            A Boolean specifying the 3-direction as a free direction.
        ur1
            A Boolean specifying the rotation about the 1-direction as a free direction.
        ur2
            A Boolean specifying the rotation about the 2-direction as a free direction.
        ur3
            A Boolean specifying the rotation about the 3-direction as a free direction.
        referencePoint
            A sequence of Floats specifying the point about which rotations are defined. The point
            can be specified only for certain combinations of free directions. The **referencePoint**
            argument can be one of the following:
            
            - The **X**, **Y** and **Z**-coordinates of a fixed rotation point.
            - A point on the rotation axis.
            - A point on the symmetry line.
        fixed
            A Boolean specifying whether the inertia relief loading should remain fixed at the
            current loading at the start of the step. The default value is OFF.
        """
        ...
