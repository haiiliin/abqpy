from __future__ import annotations

from typing import Any

from typing_extensions import Self

from .FXMetaClass import FXMetaClass
from .FXSelector import FXSelector


class FXObject:
    """Base of all FOX object."""

    def getClassName(self):
        """Get class name of some object."""

    def isMemberOf(self, metaclass: FXMetaClass):
        """Check if object is member of metaclass.

        Parameters
        ----------
        metaclass : FXMetaClass
        """

    def onDefault(self):
        """Called for unhandled messages.

        Reimplemented in FXDelegator, FXGLViewer, FXMDIChild, and FXMDIClient.
        """

    def handle(self, sender: Self, sel: FXSelector, ptr: Any):
        """Handles messages sent to this class.

        Parameters
        ----------
        sender : Self
            The sender of the message.
        sel : FXSelector
            The selector of the message.
        ptr : Any
            Associated data.
        """
