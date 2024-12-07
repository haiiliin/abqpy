from __future__ import annotations

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from ..UtilityAndView.abaqusConstants import OFF, Boolean
from .InteractionProperty import InteractionProperty


@abaqus_class_doc
class WearProperty(InteractionProperty):
    """The WearProperty object defines a wear interaction property.

    The WearProperty object is derived from the InteractionProperty object.

    .. note::
        This object can be accessed by::

            import interaction
            mdb.models[name].interactionProperties[name]

        The corresponding analysis keywords are:

        - FLUID INFLATOR ACTIVATION

    .. versionadded:: 2025
        The ``WearProperty`` class was added.
    """

    @abaqus_method_doc
    def __init__(
        self,
        name: str,
        fricCoefDependency: Boolean = OFF,
        unitlessWearCoefDependency: Boolean = OFF,
        referenceStress: float = 0.0,
        surfaceWearDistanceDependency: Boolean = OFF,
        temperatureDependency: Boolean = OFF,
        contactPressureDependency: Boolean = OFF,
        dependencies: int = 0,
    ):
        """This method creates an WearProperty object.

        .. note::
            This function can be accessed by::

                mdb.models[name].WearProperty

        Parameters
        ----------
        name
            A String specifying the interaction property repository key.
        fricCoefDependency
            A Boolean specifying whether the Archard's wear equation depends explicitly on the friction coefficient.
            The default value is OFF.
        unitlessWearCoefDependency
            A Boolean specifying whether the wear coefficient is dimensionless. The default value is OFF.
        referenceStress
            A Float specifying the value of the reference stress. This parameter is required if
            unitlessWearCoefDependency is ON.
        surfaceWearDistanceDependency
            A Boolean specifying whether the wear coefficient is dependent on the wear distance. The default value is
            OFF.
        temperatureDependency
            A Boolean specifying whether the wear coefficient is dependent on the surface temperature. The default
            value is OFF.
        contactPressureDependency
            A Boolean specifying whether the wear coefficient is dependent on the contact pressure. The default value
            is OFF.
        dependencies
            An Int specifying the number of field variable dependencies. The default value is 0.

        Returns
        -------
        WearProperty
            A WearProperty object.
        """
        super().__init__()
