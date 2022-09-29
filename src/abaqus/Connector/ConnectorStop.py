from typing import Optional

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from .ConnectorBehaviorOption import ConnectorBehaviorOption


@abaqus_class_doc
class ConnectorStop(ConnectorBehaviorOption):
    """The ConnectorStop object defines connector stops for one or more components of a
    connector's relative motion.
    The ConnectorStop object is derived from the ConnectorBehaviorOption object.

    .. note:: 
        This object can be accessed by::

            import section
            mdb.models[name].sections[name].behaviorOptions[i]
            import odbSection
            session.odbs[name].sections[name].behaviorOptions[i]

        The corresponding analysis keywords are:

        - CONNECTOR STOP
    """

    #: None or a Float specifying the lower bound for the connector's relative position for all
    #: specified components, or no lower bound. The default value is None.
    minMotion: Optional[float] = None

    #: None or a Float specifying the upper bound for the connector's relative position for all
    #: specified components, or no upper bound. The default value is None.
    maxMotion: Optional[float] = None

    #: A sequence of Ints specifying the components of relative motion for which the behavior
    #: is defined. Possible values are 1 ≤ **components** ≤ 6. Only available components can be
    #: specified. The default value is an empty sequence.
    components: tuple = ()

    @abaqus_method_doc
    def __init__(
        self, minMotion: Optional[float] = None, maxMotion: Optional[float] = None, components: tuple = ()
    ):
        """This method creates a connector stop behavior option for a ConnectorSection object.

        .. note:: 
            This function can be accessed by::

                import connectorBehavior
                connectorBehavior.ConnectorStop
                import odbConnectorBehavior
                odbConnectorBehavior.ConnectorStop

        Parameters
        ----------
        minMotion
            None or a Float specifying the lower bound for the connector's relative position for all
            specified components, or no lower bound. The default value is None.
        maxMotion
            None or a Float specifying the upper bound for the connector's relative position for all
            specified components, or no upper bound. The default value is None.
        components
            A sequence of Ints specifying the components of relative motion for which the behavior
            is defined. Possible values are 1 ≤ **components** ≤ 6. Only available components can be
            specified. The default value is an empty sequence.

        Returns
        -------
        ConnectorStop
            A :py:class:`~abaqus.Connector.ConnectorStop.ConnectorStop` object.

        Raises
        ------
        ValueError and TextError
        """
        super().__init__()

    @abaqus_method_doc
    def setValues(self, *args, **kwargs):
        """This method modifies the ConnectorStop object.

        Raises
        ------
        ValueError
        """
        ...
