from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from ..PlotOptions.OdbDisplayOptions import OdbDisplayOptions
from ..UtilityAndView.abaqusConstants import Boolean, OFF


@abaqus_class_doc
class DisplayGroupInstance:
    """A :py:class:`~abaqus.DisplayGroup.DisplayGroupInstance.DisplayGroupInstance` object stores the IDs of the entities displayed in a viewport.
    The DisplayGroupInstance object has no constructor. When you set a display group to be
    plotted in a viewport, Abaqus/CAE creates a DisplayGroupInstance object for each display
    group and places it in the DisplayGroupInstanceRepository object.

    .. note:: 
        This object can be accessed by::

            import assembly
            session.viewports[name].assemblyDisplay.displayGroupInstances[name]
            session.viewports[name].layers[name].assemblyDisplay.displayGroupInstances[name]
            import visualization
            session.viewports[name].layers[name].odbDisplay.displayGroupInstances[name]
            import part
            session.viewports[name].layers[name].partDisplay.displayGroupInstances[name]
            session.viewports[name].odbDisplay.displayGroupInstances[name]
            session.viewports[name].partDisplay.displayGroupInstances[name]
    """

    #: A String specifying the repository key.
    name: str = ""

    #: A Boolean specifying whether the display options stored on the DisplayGroupInstance
    #: object should be synchronized with changes to the viewport display options. This member
    #: is available only for DisplayGroupInstance objects that are members of the
    #: DisplayGroupInstance repository member of the OdbDisplay object. The default value is
    #: OFF.
    lockOptions: Boolean = OFF

    #: An :py:class:`~abaqus.PlotOptions.OdbDisplayOptions.OdbDisplayOptions` object specifying this member is available only for
    #: DisplayGroupInstance objects that are members of the DisplayGroupInstance repository
    #: member of the OdbDisplay object.
    odbDisplayOptions: OdbDisplayOptions = OdbDisplayOptions()

    @abaqus_method_doc
    def nodes(self):
        """This method is used to obtain the list of nodes present in the DisplayGroupInstance
        object. It returns a Dictionary object keyed by part instance names, the value of which
        is a list of user node labels belonging to the part instance and contained in the
        DisplayGroupInstance object. This method is available only for DisplayGroupInstance
        objects that are members of the DisplayGroupInstance repository member of OdbDisplay
        object.

        Returns
        -------
        dict
            A Dictionary object.
        """
        ...

    @abaqus_method_doc
    def elements(self):
        """This method returns the list of elements present in the DisplayGroupInstance object. The
        elements method returns a Dictionary object that uses part instance names for the keys.
        The value of the items in the Dictionary object is a List of user element labels that
        belong to the part instance and are contained in the DisplayGroupInstance object. This
        method is available only for DisplayGroupInstance objects that are members of the
        DisplayGroupInstance repository member of the OdbDisplay object.

        Returns
        -------
        dict
            A Dictionary object.
        """
        ...

    @abaqus_method_doc
    def setValues(self, lockOptions: Boolean = OFF):
        """This method modifies the DisplayGroupInstance object. The setValues method is available
        only for DisplayGroupInstance objects that are members of the DisplayGroupInstance
        repository member of the OdbDisplay object.

        Parameters
        ----------
        lockOptions
            A Boolean specifying whether the display options stored on the DisplayGroupInstance
            object should be synchronized with changes to the viewport display options. This member
            is available only for DisplayGroupInstance objects that are members of the
            DisplayGroupInstance repository member of the OdbDisplay object. The default value is
            OFF.
        """
        ...
