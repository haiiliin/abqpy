from __future__ import annotations

from typing_extensions import Self

from .constants import DEFAULT_SPACING
from .FXComposite import FXComposite
from .FXObject import FXObject
from .FXPacker import FXPacker


class AFXOptionTreeItem(FXPacker):
    """This class is a tree widget with check buttons."""

    #: Toggles display of frame with children.
    ID_TOGGLEEXPAND: int = hash("ID_TOGGLEEXPAND")

    #: Represents checked state of this object.
    ID_CHECKSTATE: int = hash("ID_CHECKSTATE")

    #: Container for the subtree.
    ID_SUBTREE: int = hash("ID_SUBTREE")

    #: Expands frame with children.
    ID_EXPAND: int = hash("ID_EXPAND")

    #: Collapses frame with children.
    ID_COLLAPSE: int = hash("ID_COLLAPSE")

    def __init__(
        self,
        p: FXComposite,
        label: str,
        tgt: FXObject | None = None,
        sel: int = 0,
        opts: int = 0,
        x: int = 0,
        y: int = 0,
        w: int = 0,
        h: int = 0,
        pl: int = DEFAULT_SPACING,
        pr: int = DEFAULT_SPACING,
        pt: int = DEFAULT_SPACING,
        pb: int = DEFAULT_SPACING,
        hs: int = DEFAULT_SPACING,
        vs: int = DEFAULT_SPACING,
    ):
        """Constructor creating a top-level (root) tree item.

        Parameters
        ----------
        p : FXComposite
            Parent widget.
        label : str
            Label text.
        tgt : FXObject | None
            Message target.
        sel : int
            Message ID.
        opts : int
            Options and hints.
        x : int
            X coordinate of origin.
        y : int
            Y coordinate of origin.
        w : int
            Width of the widget.
        h : int
            Height of the widget.
        pl : int
            Left padding.
        pr : int
            Right padding.
        pt : int
            Top padding.
        pb : int
            Bottom padding.
        hs : int
            Horizontal spacing.
        vs : int
            Vertical spacing.
        """

    def addItemAfter(self, label: str, tgt: FXObject | None = None, sel: int = 0):
        """Creates a new tree item as a sibling after (below) the tree item.

        Parameters
        ----------
        label : str
            Item label.
        tgt : FXObject | None
            Item target.
        sel : int
            Item selector.
        """

    def addItemBefore(self, label: str, tgt: FXObject | None = None, sel: int = 0):
        """Creates a new tree item as a sibling before (above) the tree item.

        Parameters
        ----------
        label : str
            Item label.
        tgt : FXObject | None
            Item target.
        sel : int
            Item selector.
        """

    def addItemFirst(self, label: str, tgt: FXObject | None = None, sel: int = 0):
        """Creates a new tree item as the first child of the tree item.

        Parameters
        ----------
        label : str
            Item label.
        tgt : FXObject | None
            Item target.
        sel : int
            Item selector.
        """

    def addItemLast(self, label: str, tgt: FXObject | None = None, sel: int = 0):
        """Creates a new tree item as the last child of the tree item.

        Parameters
        ----------
        label : str
            Item label.
        tgt : FXObject | None
            Item target.
        sel : int
            Item selector.
        """

    def childAtIndex(self, index: int):
        """Returns the child tree at the given index.

        Parameters
        ----------
        index : int
            Index.
        """

    def collapse(self):
        """Collapses (hides) the children."""

    def computeDefaultArrowSize(self):
        """Computes default size of the arrow button."""

    def containsChild(self, tree: Self):
        """Checks whether the given tree is a child of this object.

        Parameters
        ----------
        tree : Self
            Item.
        """

    def create(self):
        """Creates the tree item.

        Reimplemented from FXComposite.
        """

    def disable(self):
        """Disables the tree item.

        Reimplemented from FXWindow.
        """

    def enable(self):
        """Enables the tree item.

        Reimplemented from FXWindow.
        """

    def expand(self):
        """Expands (shows) the children."""

    def getArrowSize(self):
        """Returns the size of the arrow button."""

    def getCheck(self):
        """Returns the check state of the tree item."""

    def getDefaultWidth(self):
        """Returns the default width of the tree item.

        Reimplemented from FXPacker.
        """

    def getFirst(self):
        """Returns the first child tree.

        Reimplemented from FXWindow.
        """

    def getLast(self):
        """Returns the last child tree.

        Reimplemented from FXWindow.
        """

    def getNext(self):
        """Returns the next sibling tree.

        Reimplemented from FXWindow.
        """

    def getParent(self):
        """Returns the parent tree widget, or NULL if the tree item is the root.

        Reimplemented from FXWindow.
        """

    def getPrev(self):
        """Returns the previous sibling tree.

        Reimplemented from FXWindow.
        """

    def getText(self):
        """Returns the label text shown in the tree item's check button."""

    def hasVisibleChildren(self):
        """Checks whether the tree item has any visible children."""

    def hide(self):
        """Hides the tree item.

        Reimplemented from FXWindow.
        """

    def indexOfChild(self, tree: Self):
        """Returns the index of an immediate child tree, or -1 if not found.

        Parameters
        ----------
        tree : Self
            Item.
        """

    def isChildOf(self, tree: Self):
        """Checks whether this object is contained in the given tree.

        Parameters
        ----------
        tree : Self
            Item.
        """

    def isExpanded(self):
        """Checks whether the tree item shows its children."""

    def numChildren(self):
        """Returns the number of child trees.

        Reimplemented from FXWindow.
        """

    def setArrowSize(self, size: int):
        """Sets the size of the arrow button for this object and all its children.

        Parameters
        ----------
        size : int
            Size.
        """

    def setCheck(self, check: int = True):
        """Sets the check state of the tree item and its children.

        Parameters
        ----------
        check : int
            Check state.
        """

    def setText(self, txt: str):
        """Sets the label text shown in the tree item's check button.

        Parameters
        ----------
        txt : str
            Label text.
        """

    def show(self):
        """Shows the tree item.

        Reimplemented from FXWindow.
        """

    def updateCheck(self, notify: bool):
        """Updates the check state of the tree item and its ancestors.

        Parameters
        ----------
        notify : bool
            Notification flag.
        """
