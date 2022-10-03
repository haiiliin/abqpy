from typing import Optional

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from .Leaf import Leaf
from ..UtilityAndView.abaqusConstants import Boolean, OFF, SymbolicConstant


@abaqus_class_doc
class DisplayGroup:
    """DisplayGroup objects are used to select a subset of the entities displayed in the
    viewport.

    .. note:: 
        This object can be accessed by::

            session.displayGroups[name]
            import assembly
            session.viewports[name].assemblyDisplay.displayGroup
            session.viewports[name].layers[name].assemblyDisplay.displayGroup
            import visualization
            session.viewports[name].layers[name].odbDisplay.displayGroup
            import part
            session.viewports[name].layers[name].partDisplay.displayGroup
            session.viewports[name].odbDisplay.displayGroup
            session.viewports[name].partDisplay.displayGroup
    """

    #: A Boolean specifying whether Undo is possible or not.
    canUndo: Boolean = OFF

    #: A Boolean specifying whether Redo is possible or not.
    canRedo: Boolean = OFF

    #: A String specifying the repository key.
    name: str = ""

    #: A SymbolicConstant specifying the module in which the display group has been created.
    #: The possible values are PART, ASSEMBLY, PART_ASSEMBLY, ODB, and ALL.
    module: Optional[SymbolicConstant] = None

    #: A String specifying the name of the model to which the display group belongs when the
    #: module is part- or assembly-based.
    modelName: str = ""

    #: A String specifying the name of the part to which the display group belongs when the
    #: module is part-based.
    partName: str = ""

    @abaqus_method_doc
    def __init__(self, name: str, leaf: Leaf):
        """This method creates a DisplayGroup object.

        .. note:: 
            This function can be accessed by::

                session.DisplayGroup

        Parameters
        ----------
        name
            A String specifying the repository key.
        leaf
            A :py:class:`~abaqus.DisplayGroup.Leaf.Leaf` object specifying the items in the display group.

        Returns
        -------
        DisplayGroup
            A :py:class:`~abaqus.DisplayGroup.DisplayGroup.DisplayGroup` object.
        """
        ...

    @abaqus_method_doc
    def add(self, leaf: Leaf):
        """This method adds the specified items to the display group.

        Parameters
        ----------
        leaf
            A :py:class:`~abaqus.DisplayGroup.Leaf.Leaf` object specifying the items to add to the display group.
        """
        ...

    @abaqus_method_doc
    def either(self, leaf: Leaf):
        """This method redefines the display group to be only those items that are not shared by
        the **leaf** argument and by the display group.

        Parameters
        ----------
        leaf
            A :py:class:`~abaqus.DisplayGroup.Leaf.Leaf` object specifying the items to be excluded from the display group.
        """
        ...

    @abaqus_method_doc
    def intersect(self, leaf: Leaf):
        """This method redefines the display group to be only those items that are shared by the
        **leaf** argument and the display group.

        Parameters
        ----------
        leaf
            A :py:class:`~abaqus.DisplayGroup.Leaf.Leaf` object specifying the items to be included in the display group.
        """
        ...

    @abaqus_method_doc
    def redoLast(self):
        """This method redoes the last undone operation on the display group."""
        ...

    @abaqus_method_doc
    def remove(self, leaf: Leaf):
        """This method removes the specified items from the display group.

        Parameters
        ----------
        leaf
            A :py:class:`~abaqus.DisplayGroup.Leaf.Leaf` object specifying the items to remove from the display group.
        """
        ...

    @abaqus_method_doc
    def replace(self, leaf: Leaf):
        """This method replaces the contents of the display group with the specified items.

        Parameters
        ----------
        leaf
            A :py:class:`~abaqus.DisplayGroup.Leaf.Leaf` object specifying the items with which to replace the current display group
            contents.
        """
        ...

    @abaqus_method_doc
    def undoLast(self):
        """This method undoes the last operation performed on the display group."""
        ...
