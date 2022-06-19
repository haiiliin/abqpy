from abaqusConstants import *


class SectionLayer:
    """The SectionLayer object defines the material layer in a composite shell.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import section
        mdb.models[name].parts[name].compositeLayups[i].section.layup[i]
        mdb.models[name].sections[name].layup[i]
        import odbSection
        session.odbs[name].sections[name].layup[i]

    The corresponding analysis keywords are:

    - SHELL SECTION
            - SHELL GENERAL SECTION

    """

    def __init__(
        self,
        thickness: float,
        material: str,
        orientAngle: float = 0,
        numIntPts: int = 3,
        axis: SymbolicConstant = AXIS_3,
        angle: float = 0,
        additionalRotationType: SymbolicConstant = ROTATION_NONE,
        thicknessType: SymbolicConstant = THICKNESS_MAGNITUDE,
        plyName: str = "",
        orientation: SymbolicConstant = None,
        additionalRotationField: str = "",
        thicknessField: str = "",
    ):
        """This method creates a SectionLayer object.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            section.SectionLayer
            odbSection.SectionLayer

        Parameters
        ----------
        thickness
            A Float specifying the thickness of the section layer.
        material
            A String specifying the name of the section layer material.
        orientAngle
            A Float or a String specifying the relative orientation of the section layer. A Float
            specifies the angular orientation; a String specifies a user-subroutine orientation
            name. If a String is specified, a user-subroutine orientation is used, otherwise the
            Float value is used as an angular orientation. The default value is 0.0.
        numIntPts
            An Int specifying the number of integration points to be used through the section. This
            argument is valid only if the **preIntegrate** argument on the parent
            CompositeShellSection object is set to ON. The default value is 3.
        axis
            A SymbolicConstant specifying the axis of a cylindrical or spherical datum coordinate
            system about which an additional rotation is applied. For shells this axis is also the
            shell normal. This only applies if a valid reference is provided for the orientation.
            Possible values are AXIS_1, AXIS_2, and AXIS_3. The default value is AXIS_3.
        angle
            A Float specifying the angle of the additional rotation. This only applies if a valid
            reference is provided for the orientation. The default value is 0.0.
        additionalRotationType
            A SymbolicConstant specifying the method used to describe the additional rotation when a
            valid orientation is specified. Possible values are ROTATION_NONE, ROTATION_ANGLE, and
            ROTATION_FIELD. The default value is ROTATION_NONE.
        thicknessType: SymbolicConstant
            A SymbolicConstant specifying the method used to describe the thickness. Possible values
            are THICKNESS_MAGNITUDE and THICKNESS_DISCRETE_FIELD. The default value is THICKNESS_MAGNITUDE.
        plyName
            A String specifying the ply identifier for this section layer. The default value is "".
        orientation
            The SymbolicConstant None or a DatumCsys object specifying a coordinate system reference
            for the relative orientation of this layer. If this reference is valid it is used as the
            relative orientation of the layer, otherwise the **orientAngle** is used as described. The
            default value is None.
        additionalRotationField
            A String specifying the name of the field specifying the additional rotation. The
            default value is "".
        thicknessField
            A String specifying the name of the field specifying the thickness The default value is "".

        Returns
        -------
            A SectionLayer object.
        """
        pass
