from abaqusConstants import *


class AttributeColorMap:
    """The AttributeColorMap object is used to store values and attributes associated with
    AttributeColorMap type objects. AttributeColorMap objects can be modified using the
    methods described below. The methods accessed via the Viewport object cause the
    AttributeColorMap object to be updated in the session.viewports[name].colorMappings
    repository.

    Notes
    -----
    This object can be accessed by:

    .. code-block::

        session.viewports[name].colorMappings[name]
    """

    #: A SymbolicConstant specifying the type of AttributeColorMap . Possible values are
    #: MATERIAL_MAP, SECTION_MAP, PART_MAP, ELSET_MAP, AVERAGING_REGION_MAP, and ELTYPE_MAP.
    mapType: SymbolicConstant = None

    #: A Dictionary object specifying a color mapping. Each key is of String type and specifies
    #: an attribute in the map; the corresponding values specify the color definition to apply
    #: to that attribute in the form (0|1, wire color, edge color, face color). The 0|1 defines
    #: the active status for the attribute. For example:`overrides={
    #: 'Part-1':(1,'#00FF00', '#00CCFF',                        '#00FF00')}`
    overrides: dict = None

    #: A Dictionary object specifying a custom color mapping similar to overrides. For
    #: example:`defaultOverrides={                        'Copper':(1,''#00FF00', '#00CCFF',
    #:                     '#00FF00')}`The color mapping can contain keys that have not been
    #: created. When the key is created, it gets the appropriate values from this mapping.
    defaultOverrides: dict = None

    #: A Dictionary object specifying the color settings of each attribute as described in the
    #: [updateOverrides
    #: ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-attributecolormappyc.htm?ContextScope=all#simaker-attributecolormapupdateoverridespyc)method.
    attributeColors: dict = None

    def setDefaults(self):
        """This method resets the AttributeColorMap object to its default state."""
        pass

    def setValues(self, overrides: dict = None, defaultOverrides: dict = None):
        """This method modifies the AttributeColorMap object.

        Parameters
        ----------
        overrides
            A Dictionary object specifying a color mapping. Each key is of String type and specifies
            an attribute in the map; the corresponding values specify the color definition to apply
            to that attribute in the form (0|1, wire color, edge color, face color). The 0|1 defines
            the active status for the attribute. For example:`overrides={
            'Part-1':(1,'#00FF00', '#00CCFF',                        '#00FF00')}`
        defaultOverrides
            A Dictionary object specifying a custom color mapping similar to overrides. For
            example:`defaultOverrides={                        'Copper':(1,''#00FF00', '#00CCFF',
                                '#00FF00')}`The color mapping can contain keys that have not been
            created. When the key is created, it gets the appropriate values from this mapping.
        """
        pass

    def updateOverrides(self, overrides: dict = None, defaultOverrides: dict = None):
        """This method specifies additional overrides to be added to the current object definition.

        Parameters
        ----------
        overrides
            A Dictionary object specifying a color mapping. Each key is of String type and specifies
            an attribute in the map; the corresponding values specify the color definition to apply
            to that attribute in the form (0|1, wire color, edge color, face color). The 0|1 defines
            the active status for the attribute. For example:`overrides={
            'Part-1':(1,'#00FF00', '#00CCFF',                        '#00FF00')}`
        defaultOverrides
            A Dictionary object specifying a custom color mapping similar to overrides. For
            example:`defaultOverrides={                        'Copper':(1,''#00FF00', '#00CCFF',
                                '#00FF00')}`The color mapping can contain keys that have not been
            created. When the key is created, it gets the appropriate values from this mapping.
        """
        pass
