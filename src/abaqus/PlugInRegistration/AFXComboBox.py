from __future__ import annotations

from typing import Any

from .AFXDataComponent import AFXDataComponent
from .constants import DEFAULT_PAD
from .FXComposite import FXComposite
from .FXFont import FXFont
from .FXObject import FXObject
from .FXPacker import FXPacker

#: Use a check button instead of a label.
AFXCOMBOBOX_CHECKBUTTON: int = hash("AFXCOMBOBOX_CHECKBUTTON")

#: Use a radio button instead of a label.
AFXCOMBOBOX_RADIOBUTTON: int = hash("AFXCOMBOBOX_RADIOBUTTON")

#: Orient label or button above combo box.
AFXCOMBOBOX_VERTICAL: int = hash("AFXCOMBOBOX_VERTICAL")

#: Allow interaction with float keywords.
AFXCOMBOBOX_FLOAT: int = hash("AFXCOMBOBOX_FLOAT")

#: Configure combo box to the read-only state.
AFXCOMBOBOX_READONLY: int = hash("AFXCOMBOBOX_READONLY")

#: Include spinner buttons.
AFXCOMBOBOX_SPINNER: int = hash("AFXCOMBOBOX_SPINNER")


class AFXComboBox(FXPacker, AFXDataComponent):
    """This class implements a labeled combo box.

    It allows the user to select entries from a drop-down list. Each item has associated data set as
    integers as items are added.
    """

    #: Label or button ID.
    ID_BUTTON: int = hash("ID_BUTTON")

    #: Combo box ID.
    ID_COMBO: int = hash("ID_COMBO")

    #: Up arrow button ID.
    ID_INCREMENT: int = hash("ID_INCREMENT")

    #: Down arrow button ID.
    ID_DECREMENT: int = hash("ID_DECREMENT")

    def __init__(
        self,
        p: FXComposite,
        ncols: int,
        nvis: int,
        text: str,
        tgt: FXObject | None = None,
        sel: int = 0,
        opts: int = 0,
        x: int = 0,
        y: int = 0,
        w: int = 0,
        h: int = 0,
        pl: int = DEFAULT_PAD,
        pr: int = DEFAULT_PAD,
        pt: int = DEFAULT_PAD,
        pb: int = DEFAULT_PAD,
    ):
        """Constructor.

        Parameters
        ----------
        p : FXComposite
            Parent widget.
        ncols : int
            Number of columns in the combo box (use 0 for auto-sizing).
        nvis : int
            Number of visible items in the combo box's drop down list.
        text : str
            Label string.
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
            Left padding (margin).
        pr : int
            Right padding (margin).
        pt : int
            Top padding (margin).
        pb : int
            Bottom padding (margin).
        """

    def appendItem(self, text: str, sel: int = 0):
        """Adds an item to the end of the list.

        Parameters
        ----------
        text : str
            Text.
        sel : int
            Integer associated with this item.
        """

    def clearItems(self):
        """Removes all items from the list."""

    def create(self):
        """Creates the combo box.

        Reimplemented from FXComposite.
        """

    def disable(self):
        """Disables the combo box.

        Reimplemented from FXWindow.
        """

    def enable(self):
        """Enables the combo box.

        Reimplemented from FXWindow.
        """

    def getCheck(self):
        """Returns the state of the check button or the radio button."""

    def getCurrentItem(self):
        """Returns the index of the current item."""

    def getHelpText(self):
        """Returns the status line help text."""

    def getItemData(self, index: int):
        """Returns the data for the specified item.

        Parameters
        ----------
        index : int
            Index.
        """

    def getItemIndexForData(self, data: Any):
        """Returns the index of the first item with the associated data or -1 if not found.

        Parameters
        ----------
        data : Any
        """

    def getItemIndexForFloat(self, val: float):
        """Returns the index of the first item with the text evaluating to the given value.

        Parameters
        ----------
        val : float
        """

    def getItemProvider(self):
        """Returns the provider of the combo box's items."""

    def getItemText(self, index: int):
        """Returns the text for the specified item.

        Parameters
        ----------
        index : int
            Index.
        """

    def getLabelFont(self):
        """Returns the label font."""

    def getLabelText(self):
        """Returns the label string."""

    def getNumColumns(self):
        """Returns the number of columns."""

    def getNumItems(self):
        """Returns the number of items in the list."""

    def getNumVisible(self):
        """Returns the number of visible items."""

    def getText(self):
        """Returns the text displayed in input field."""

    def getTipText(self):
        """Returns the tool tip message."""

    def insertItem(self, index: int, text: str, sel: int = 0):
        """Inserts a new item at the specified index position.

        Parameters
        ----------
        index : int
            Index.
        text : str
            Text.
        sel : int
            Integer associated with this item
        """

    def isEditable(self):
        """Returns True if the text in the input field may be edited."""

    def isItemCurrent(self, index: int):
        """Returns True if the item at the specified index position is the current item.

        Parameters
        ----------
        index : int
            Index.
        """

    def isReadOnlyState(self):
        """Returns True if the combo box appears in the read-only state."""

    def removeItem(self, index: int):
        """Removes the item at the specified index position from the list.

        Parameters
        ----------
        index : int
            Index.
        """

    def replaceItem(self, index: int, text: str, sel: int = 0):
        """Replaces the item at the specified index position.

        Parameters
        ----------
        index : int
            Index.
        text : str
            Text.
        sel : int
            Integer associated with this item
        """

    def setCheck(self, state: bool):
        """Sets the state of the check button or the radio button.

        Parameters
        ----------
        state : bool
            Button state.
        """

    def setCheckButtonSelector(self, sel: int):
        """Sets the message ID of the check button or the radio button.

        Parameters
        ----------
        sel : int
            Selector.
        """

    def setCheckButtonTarget(self, tgt: FXObject, checkVal: bool = False):
        """Sets the message target of the check button or the radio button.

        Parameters
        ----------
        tgt : FXObject
            Target.
        checkVal : bool
            Value of check button.
        """

    def setCurrentItem(self, index: int):
        """Sets the current item (the index is zero-based).

        Parameters
        ----------
        index : int
            Index.
        """

    def setEditable(self, edit: bool = True):
        """Sets the editable state for the input field.

        Parameters
        ----------
        edit : bool
            Editable state.
        """

    def setFocusAndSelection(self):
        """Moves the focus to the input field and selects its contents if the combo box is editable."""

    def setFocusToCheckButton(self):
        """Moves the focus to the check button or the radio button (if existed) of the widget."""

    def setFocusToComboBox(self):
        """Moves the focus to the input field of the widget."""

    def setHelpText(self, text: str):
        """Sets the status line help text.

        Parameters
        ----------
        text : str
            Help text.
        """

    def setItemData(self, index: int, ptr: str):
        """Sets the data for the specified item.

        Parameters
        ----------
        index : int
            Index.
        ptr : str
            Data.
        """

    def setItemProvider(self, cp: FXObject):
        """Sets the provider of this object items.

        Parameters
        ----------
        cp : FXObject
            Item provider.
        """

    def setItemText(self, index: int, text: str):
        """Sets the text for the specified item.

        Parameters
        ----------
        index : int
            Index.
        text : str
            Text.
        """

    def setLabelFont(self, fnt: FXFont):
        """Sets the label font.

        Parameters
        ----------
        fnt : FXFont
            Label font.
        """

    def setLabelText(self, txt: str):
        """Sets the label string.

        Parameters
        ----------
        txt : str
            Label text.
        """

    def setMaxVisible(self, maxVis: int):
        """Sets the maximum number of visible items. The combo box will show up to the given maximum number of
        items in its list. If the combo box has more items, its list will show a scroll bar.

        Parameters
        ----------
        maxVis : int
            Maximum number of visible items.
        """

    def setNumColumns(self, cols: int):
        """Sets the number of columns in the combo box; passing zero will cause the combo box to always have the
        number of columns equal to the maximum item length.

        Parameters
        ----------
        cols : int
            Number of columns.
        """

    def setNumVisible(self, nvis: int):
        """Sets the number of visible items.

        Parameters
        ----------
        nvis : int
            Number of visible items.
        """

    def setReadOnlyState(self, readonly: bool = True):
        """Sets the read-only state of the combo box.

        Parameters
        ----------
        readonly : bool
            Read-only state.
        """

    def setText(self, txt: str):
        """Sets the text displayed in the input field.

        Parameters
        ----------
        txt : str
            Input field text.
        """

    def setTipText(self, text: str):
        """Sets the tool tip message.

        Parameters
        ----------
        text : str
            Tooltip text.
        """
