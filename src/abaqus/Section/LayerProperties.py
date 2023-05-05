from abqpy.decorators import abaqus_class_doc, abaqus_method_doc


@abaqus_class_doc
class LayerProperties:
    """The LayerProperties object defines the properties of a layer of reinforcement for membrane, shell, and
    surface sections.

    .. note::
        This object can be accessed by::

            import section
            mdb.models[name].parts[name].compositeLayups[i].section.rebarLayers.layerTable[i]
            mdb.models[name].sections[name].rebarLayers.layerTable[i]
            import odbSection
            session.odbs[name].sections[name].rebarLayers.layerTable[i]

        The corresponding analysis keywords are:

        - REBAR LAYER
    """

    #: A Float specifying the area per bar.
    barArea: float

    #: A Float or a String specifying the orientation of the rebar. A Float specifies the
    #: angular orientation; a String specifies an orientation name.
    orientationAngle: float

    #: A String specifying the name of the rebar layer.
    layerName: str

    #: A String specifying the name of the rebar material.
    material: str

    #: A Float specifying the spacing of the rebar. This argument is only valid if the
    #: **rebarSpacing** argument on the parent RebarLayers object is set to CONSTANT. The default
    #: value is 0.0.
    barSpacing: float = 0

    #: A Float specifying the position of the rebar from the middle surface of the shell.
    #: **layerPosition** applies only for homogeneous shell sections and composite shell
    #: sections. The default value is 0.0.
    layerPosition: float = 0

    #: A Float specifying the spacing angle of the rebar. This argument is only valid if the
    #: **rebarSpacing** argument on the parent RebarLayers object is set to ANGULAR. The default
    #: value is 0.0.
    spacingAngle: float = 0

    #: A Float specifying the extension ratio for the rebar. This argument is only valid if the
    #: **rebarSpacing** argument on the parent RebarLayers object is set to LIFT_EQUATION. The
    #: default value is 0.0.
    extensionRatio: float = 0

    #: A Float specifying the radius of the rebar. This argument is only valid if the
    #: **rebarSpacing** argument on the parent RebarLayers object is set to LIFT_EQUATION. The
    #: default value is 0.0.
    radius: float = 0

    @abaqus_method_doc
    def __init__(
        self,
        barArea: float,
        orientationAngle: float,
        layerName: str,
        material: str,
        barSpacing: float = 0,
        layerPosition: float = 0,
        spacingAngle: float = 0,
        extensionRatio: float = 0,
        radius: float = 0,
    ):
        """This method creates a LayerProperties object.

        .. note::
            This function can be accessed by::

                section.LayerProperties
                odbSection.LayerProperties

        Parameters
        ----------
        barArea
            A Float specifying the area per bar.
        orientationAngle
            A Float or a String specifying the orientation of the rebar. A Float specifies the
            angular orientation; a String specifies an orientation name.
        layerName
            A String specifying the name of the rebar layer.
        material
            A String specifying the name of the rebar material.
        barSpacing
            A Float specifying the spacing of the rebar. This argument is only valid if the
            **rebarSpacing** argument on the parent RebarLayers object is set to CONSTANT. The default
            value is 0.0.
        layerPosition
            A Float specifying the position of the rebar from the middle surface of the shell.
            **layerPosition** applies only for homogeneous shell sections and composite shell
            sections. The default value is 0.0.
        spacingAngle
            A Float specifying the spacing angle of the rebar. This argument is only valid if the
            **rebarSpacing** argument on the parent RebarLayers object is set to ANGULAR. The default
            value is 0.0.
        extensionRatio
            A Float specifying the extension ratio for the rebar. This argument is only valid if the
            **rebarSpacing** argument on the parent RebarLayers object is set to LIFT_EQUATION. The
            default value is 0.0.
        radius
            A Float specifying the radius of the rebar. This argument is only valid if the
            **rebarSpacing** argument on the parent RebarLayers object is set to LIFT_EQUATION. The
            default value is 0.0.

        Returns
        -------
        LayerProperties
            A LayerProperties object.
        """
        ...
