from __future__ import annotations

from .FXComposite import FXComposite
from .FXIcon import FXIcon
from .FXObject import FXObject


class AFXToolButton:
    """|"""

    def __init__(
        self,
        p: FXComposite,
        label: str,
        icon: FXIcon | None = None,
        tgt: FXObject | None = None,
        sel: int = 0,
        asToggle: bool = True,
    ):
        """Constructor.

        Parameters
        ----------
        p : FXComposite
            Parent widget.
        label : str
            Label for the button.
        icon : FXIcon | None
            Icon for the button.
        tgt : FXObject | None
            Message target.
        sel : int
            Message ID.
        asToggle : bool
            Allow toggle off behavior.
        """
