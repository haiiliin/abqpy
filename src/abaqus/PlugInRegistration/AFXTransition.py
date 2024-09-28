from __future__ import annotations

from .AFXIntTarget import AFXIntTarget
from .FXObject import FXObject


class AFXTransition(FXObject):
    """This class is designed for the finite state transition that the GUI (mostly the dialog boxes) can define
    to perform actions according to state changes.

    The first three arguments of the constructors (keyword, op, and refValue) define an expression
    (keyword.getValue() op refValue). The current value of the keyword is compared with the reference value.
    When the expression evaluates to True, a message with the given selector will be sent to the specified
    message target.
    """

    class Operator: ...

    #: Equal to.
    EQ: int = hash("EQ")

    #: Not equal to.
    NE: int = hash("NE")

    #: Less than.
    LT: int = hash("LT")

    #: Less than or equal to.
    LE: int = hash("LE")

    #: Greater than.
    GT: int = hash("GT")

    #: Greater than or equal to.
    GE: int = hash("GE")

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
        """Returns True and sends a message if the expression defined by the constructor arguments evaluates to
        True; returns False without performing any actions if otherwise.

        Parameters
        ----------
        sender : FXObject
            Message sender.
        """
