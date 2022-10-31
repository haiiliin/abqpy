from typing import Optional

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from typing_extensions import Literal

from .ConnectorBehaviorOption import ConnectorBehaviorOption
from ..UtilityAndView.abaqusConstants import ALL, SymbolicConstant
from ..UtilityAndView.abaqusConstants import abaqusConstants as C


@abaqus_class_doc
class ConnectorLock(ConnectorBehaviorOption):
    """The ConnectorLock object defines locking criteria for one or more available components
    of a connector's relative motion.
    The ConnectorLock object is derived from the ConnectorBehaviorOption object.

    .. note::
        This object can be accessed by::

            import section
            mdb.models[name].sections[name].behaviorOptions[i]
            import odbSection
            session.odbs[name].sections[name].behaviorOptions[i]

        The corresponding analysis keywords are:

        - CONNECTOR LOCK
    """

    #: The SymbolicConstant ALL or an Int specifying the motion components that are locked. If
    #: an Int is specified, only that motion component is locked when the locking criteria are
    #: satisfied. If **lockingComponent** = ALL, all motion components are locked. The default
    #: value is ALL.
    lockingComponent: SymbolicConstant = ALL

    #: None or a Float specifying the lower bound for the connector's relative position for all
    #: specified components, or no lower bound. The default value is None.
    minMotion: Optional[float] = None

    #: None or a Float specifying the upper bound for the connector's relative position for all
    #: specified components, or no upper bound. The default value is None.
    maxMotion: Optional[float] = None

    #: None or a Float specifying the lower bound of the force or moment in the directions of
    #: the specified components at which locking occurs, or no lower bound. The default value
    #: is None.
    minForce: Optional[float] = None

    #: None or a Float specifying the upper bound of the force or moment in the directions of
    #: the specified components at which locking occurs, or no upper bound. The default value
    #: is None.
    maxForce: Optional[float] = None

    #: A sequence of Ints specifying the components of relative motion for which the behavior
    #: is defined. Possible values are 1 ≤ **components** ≤ 6. Only available components can be
    #: specified. The default value is an empty sequence.
    components: tuple = ()

    @abaqus_method_doc
    def __init__(
        self,
        lockingComponent: Literal[C.ALL] = ALL,
        minMotion: Optional[float] = None,
        maxMotion: Optional[float] = None,
        minForce: Optional[float] = None,
        maxForce: Optional[float] = None,
        components: tuple = (),
    ):
        """This method creates a connector lock behavior option for a ConnectorSection.

        .. note::
            This function can be accessed by::

                import connectorBehavior
                connectorBehavior.ConnectorLock
                import odbConnectorBehavior
                odbConnectorBehavior.ConnectorLock

        Parameters
        ----------
        lockingComponent
            The SymbolicConstant ALL or an Int specifying the motion components that are locked. If
            an Int is specified, only that motion component is locked when the locking criteria are
            satisfied. If **lockingComponent** = ALL, all motion components are locked. The default
            value is ALL.
        minMotion
            None or a Float specifying the lower bound for the connector's relative position for all
            specified components, or no lower bound. The default value is None.
        maxMotion
            None or a Float specifying the upper bound for the connector's relative position for all
            specified components, or no upper bound. The default value is None.
        minForce
            None or a Float specifying the lower bound of the force or moment in the directions of
            the specified components at which locking occurs, or no lower bound. The default value
            is None.
        maxForce
            None or a Float specifying the upper bound of the force or moment in the directions of
            the specified components at which locking occurs, or no upper bound. The default value
            is None.
        components
            A sequence of Ints specifying the components of relative motion for which the behavior
            is defined. Possible values are 1 ≤ **components** ≤ 6. Only available components can be
            specified. The default value is an empty sequence.

        Returns
        -------
        ConnectorLock
            A ConnectorLock object.

        Raises
        ------
        ValueError and TextError
        """
        super().__init__()

    @abaqus_method_doc
    def setValues(self, *args, **kwargs):
        """This method modifies the ConnectorLock object.

        Raises
        ------
        ValueError
        """
        ...
