from __future__ import annotations

from .FXObject import FXObject


class AFXTarget(FXObject):
    """This class is the base class for all target objects."""

    #: Unspecified.
    UNSPECIFIED: int = hash("UNSPECIFIED")

    #: Integer.
    INT: int = hash("INT")

    #: Float.
    FLOAT: int = hash("FLOAT")

    #: String.
    STRING: int = hash("STRING")

    def __init__(self):
        """Constructor."""

    def connect(self, value: int):
        """Associates the data with an integer variable.

        Parameters
        ----------
        value : int
            Variable to be associated with.
        """

    def getSelector(self):
        """Returns the message ID of this target object."""

    def getTarget(self):
        """Returns the target of this target object."""

    def getType(self):
        """Returns the target type; this method is deprecated in Abaqus 6.6, and its use should be replaced by
        getTypeName()."""

    def getTypeName(self):
        """Returns the name of the target type.

        Implemented in AFXFloatTarget, AFXIntTarget, and AFXStringTarget.
        """

    def setSelector(self, msgId: int):
        """Sets the message ID of this target object.

        Parameters
        ----------
        msgId : int
            Message ID.
        """

    def setTarget(self, target: FXObject):
        """Sets the target of this target object.

        Parameters
        ----------
        target : FXObject
            Target.
        """
