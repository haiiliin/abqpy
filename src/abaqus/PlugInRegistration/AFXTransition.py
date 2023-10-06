from __future__ import annotations

from .AFXBoolKeyword import AFXBoolKeyword
from .AFXFloatKeyword import AFXFloatKeyword
from .AFXFloatTarget import AFXFloatTarget
from .AFXIntKeyword import AFXIntKeyword
from .AFXIntTarget import AFXIntTarget
from .AFXTogglableKeyword import AFXTogglableKeyword
from .FXObject import FXObject


class AFXTransition:
    """Abaqus"""

    def __init__(
        self, intTarget: AFXIntTarget, op: Operator, refValue: int, tgt: FXObject, sel: int, ptr: str = "None"
    ):
        """Constructor.

        Parameters
        ----------
        intTarget : AFXIntTarget
            Target.
        op : Operator
            Operator type.
        refValue : int
            Reference value.
        tgt : FXObject
            Message target.
        sel : int
            Message selector.
        ptr : str
            Message data.
        """

    def process(self, sender: FXObject):
        """Returns True and sends a message if the expression defined by the constructor arguments evaluates to True; returns False without performing any actions if otherwise.

        Parameters
        ----------
        sender : FXObject
            Message sender.
        """
