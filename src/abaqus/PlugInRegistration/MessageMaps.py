"""Message maps are used by classes derived from FXObject (which includes most GUI classes) to route messages
sent to the object to a message handling method.

A typical use might be to route a message from a button in a dialog to one of the dialog's methods so that
some action is taken when the button is pressed.
"""

from __future__ import annotations

from typing import Callable

from .FXObject import FXObject


def FXMAPFUNC(object: FXObject, messageType: int, messageId: int, method: Callable):
    """Creates an entry in the object's message map that will route a message to a method.

    Parameters
    ----------
    object : FXObject
        An instance of the class in which the message map entry is to be made. Typically this is "self".
    messageType : int
        An integer flag specifying the message type (e.g. SEL_COMMAND).
    messageId : int
        An integer specifying the message ID.
    method : Callable
        The method to which the message is to be routed. This method must be specified by including the class name (e.g. MyDB.myMethod).
    """


def FXMAPFUNCS(object: FXObject, messageType: int, startMessageId: int, endMessageId: int, method: Callable):
    """Creates multiple entries in the object's message map that will route messages to a method.

    Parameters
    ----------
    object : FXObject
        An instance of the class in which the message map entry is to be made. Typically this is "self".
    messageType : int
        An integer flag specifying the message type (e.g. SEL_COMMAND).
    startMessageId : int
        An integer specifying the starting message ID.
    endMessageId : int
        An integer specifying the ending message ID.
    method : Callable
        The method to which the message is to be routed. This method must be specified by including the class name (e.g. MyDB.myMethod).
    """


def MKUINT(messageId: int, messageType: int):
    """Creates a message selector by combining a message ID and a message type.

    Parameters
    ----------
    messageId : int
        An integer specifying the message ID.
    messageType : int
        An integer flag specifying the message type (e.g. SEL_COMMAND).
    """


def SELID(selector: int):
    """Returns the message ID from a message selector.

    Parameters
    ----------
    selector : int
        A message selector.
    """


def SELTYPE(selector: int):
    """Returns the message type from a message selector.

    Parameters
    ----------
    selector : int
        A message selector.
    """
