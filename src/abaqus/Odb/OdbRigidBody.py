from typing import Optional

from typing_extensions import Literal

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from ..UtilityAndView.abaqusConstants import INPUT, ON, Boolean, SymbolicConstant
from ..UtilityAndView.abaqusConstants import abaqusConstants as C
from .AnalyticSurface import AnalyticSurface
from .OdbSet import OdbSet


@abaqus_class_doc
class OdbRigidBody:
    """The Rigid body object is used to bind a set of elements and/or a set of nodes and/or an analytical
    surface with a reference node.

    .. note::
        This object can be accessed by::

            import odbAccess
            session.odbs[name].parts[name].rigidBodies[i]
            session.odbs[name].rootAssembly.instances[name].rigidBodies[i]
            session.odbs[name].rootAssembly.rigidBodies[i]
            session.odbs[name].steps[name].frames[i].fieldOutputs[name].values[i].instance.rigidBodies[i]
    """

    #: An OdbSet object specifying the reference node set associated with the rigid body.
    referenceNode: OdbSet

    #: A SymbolicConstant specifying the specific location of the OdbRigidBody reference node
    #: relative to the rest of the rigid body. Possible values are INPUT and CENTER_OF_MASS.
    #: The default value is INPUT.
    position: SymbolicConstant = INPUT

    #: A Boolean specifying specify whether the OdbRigidBody can have temperature gradients or
    #: be isothermal. This is used only for fully coupled thermal-stress analysis The default
    #: value is ON.
    isothermal: Boolean = ON

    #: An OdbSet object specifying the element set whose motion is governed by the motion of
    #: rigid body reference node.
    elements: OdbSet = OdbSet("set", ())

    #: An OdbSet object specifying the node set which have both translational and rotational
    #: degrees of freedom associated with the rigid body.
    tieNodes: OdbSet = OdbSet("set", ())

    #: An OdbSet object specifying the node set which have only translational degrees of
    #: freedom associated with the rigid body.
    pinNodes: OdbSet = OdbSet("set", ())

    #: An AnalyticSurface object specifying the analytic surface whose motion is governed by
    #: the motion of rigid body reference node.
    analyticSurface: Optional[AnalyticSurface] = None

    @abaqus_method_doc
    def __init__(
        self,
        referenceNode: OdbSet,
        position: Literal[C.INPUT, C.CENTER_OF_MASS] = INPUT,
        isothermal: Boolean = ON,
        elements: OdbSet = OdbSet("set", ()),
        tieNodes: OdbSet = OdbSet("set", ()),
        pinNodes: OdbSet = OdbSet("set", ()),
        analyticSurface: Optional[AnalyticSurface] = None,
    ):
        """This method creates a OdbRigidBody object.

        .. note::
            This function can be accessed by::

                session.odbs[name].rootAssembly.instances[name].RigidBody
                session.odbs[name].rootAssembly.RigidBody

        Parameters
        ----------
        referenceNode
            An OdbSet object specifying the reference node set associated with the rigid body.
        position
            A SymbolicConstant specifying the specific location of the OdbRigidBody reference node
            relative to the rest of the rigid body. Possible values are INPUT and CENTER_OF_MASS.
            The default value is INPUT.
        isothermal
            A Boolean specifying specify whether the OdbRigidBody can have temperature gradients or
            be isothermal. This is used only for fully coupled thermal-stress analysis The default
            value is ON.
        elements
            An OdbSet object specifying the element set whose motion is governed by the motion of
            rigid body reference node.
        tieNodes
            An OdbSet object specifying the node set which have both translational and rotational
            degrees of freedom associated with the rigid body.
        pinNodes
            An OdbSet object specifying the node set which have only translational degrees of
            freedom associated with the rigid body.
        analyticSurface
            An AnalyticSurface object specifying the analytic surface whose motion is governed by
            the motion of rigid body reference node.

        Returns
        -------
        OdbRigidBody
            An OdbRigidBody object.
        """
        ...
