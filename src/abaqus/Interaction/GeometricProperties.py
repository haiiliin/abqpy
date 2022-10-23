from typing import Optional

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from ..UtilityAndView.abaqusConstants import Boolean, OFF, SymbolicConstant


@abaqus_class_doc
class GeometricProperties:
    """The GeometricProperties object specifies surface interaction properties.

    .. note::
        This object can be accessed by::

            import interaction
            mdb.models[name].interactionProperties[name].geometricProperties

        The corresponding analysis keywords are:

        - SURFACE INTERACTION
    """

    #: A Float specifying the out-of-plane thickness of the surface for a two-dimensional model
    #: or cross-sectional area for every node in the node-based surface. The default value is
    #: 1.0.
    contactArea: float = 1

    #: None or a Float specifying the thickness of an interfacial layer between the contacting
    #: surfaces. If **padThickness** = None, there is no interfacial layer. The default value is
    #: None.
    padThickness: Optional[float] = None

    #: None or a Float specifying the thickness that determines the contacting surfaces to be
    #: tracked. The input value for this parameter cannot be negative. An internal default
    #: value is used if a zero value is input or if the parameter is omitted.
    trackingThickness: Optional[float] = None

    #: An Int specifying the number of state-dependent variables. The default value is 0. This
    #: argument is applicable only if **modelType** = MODELTYPE_USER or
    #: **modelType** = MODELTYPE_USER_INTERACTION.
    dependentVariables: int = 0

    #: An Int specifying the number of property values required. The default value is 0. This
    #: argument is applicable only if **modelType** = MODELTYPE_USER or
    #: **modelType** = MODELTYPE_USER_INTERACTION.
    numProperties: int = 0

    #: A Boolean specifying whether to use unsymmetric equation solution procedures. This
    #: argument is applicable only if **modelType** = MODELTYPE_USER or
    #: **modelType** = MODELTYPE_USER_INTERACTION.
    useUnsymmetricEqunProcedure: Boolean = OFF

    #: A SymbolicConstant specifying the surface interaction model type.
    modelType: Optional[SymbolicConstant] = None

    @abaqus_method_doc
    def __init__(
        self,
        contactArea: float = 1,
        padThickness: Optional[float] = None,
        trackingThickness: Optional[float] = None,
        dependentVariables: int = 0,
        numProperties: int = 0,
        useUnsymmetricEqunProcedure: Boolean = OFF,
        modelType: Optional[SymbolicConstant] = None,
    ):
        """This method creates a GeometricProperties object.

        .. note::
            This function can be accessed by::

                mdb.models[name].interactionProperties[name].GeometricProperties

        Parameters
        ----------
        contactArea
            A Float specifying the out-of-plane thickness of the surface for a two-dimensional model
            or cross-sectional area for every node in the node-based surface. The default value is
            1.0.
        padThickness
            None or a Float specifying the thickness of an interfacial layer between the contacting
            surfaces. If **padThickness** = None, there is no interfacial layer. The default value is
            None.
        trackingThickness
            None or a Float specifying the thickness that determines the contacting surfaces to be
            tracked. The input value for this parameter cannot be negative. An internal default
            value is used if a zero value is input or if the parameter is omitted.
        dependentVariables
            An Int specifying the number of state-dependent variables. The default value is 0. This
            argument is applicable only if **modelType** = MODELTYPE_USER or
            **modelType** = MODELTYPE_USER_INTERACTION.
        numProperties
            An Int specifying the number of property values required. The default value is 0. This
            argument is applicable only if **modelType** = MODELTYPE_USER or
            **modelType** = MODELTYPE_USER_INTERACTION.
        useUnsymmetricEqunProcedure
            A Boolean specifying whether to use unsymmetric equation solution procedures. This
            argument is applicable only if **modelType** = MODELTYPE_USER or
            **modelType** = MODELTYPE_USER_INTERACTION.
        modelType
            A SymbolicConstant specifying the surface interaction model type.

        Returns
        -------
        GeometricProperties
            A :py:class:`~abaqus.Interaction.GeometricProperties.GeometricProperties` object.
        """
        ...

    @abaqus_method_doc
    def setValues(self, *args, **kwargs):
        """This method modifies the GeometricProperties object."""
        ...
