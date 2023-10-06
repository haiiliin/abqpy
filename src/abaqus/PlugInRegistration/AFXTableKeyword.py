from __future__ import annotations

from .AFXComTableKeyword import AFXComTableKeyword
from .AFXGuiCommand import AFXGuiCommand


class AFXTableKeyword(AFXComTableKeyword):
    """This class is designed for command keywords that have table values."""

    def __init__(
        self,
        command: AFXGuiCommand,
        name: str,
        isRequired: bool = False,
        minLength: int = 0,
        maxLength: int = -1,
        opts: int = 0,
    ):
        """Constructor.

        Parameters
        ----------
        command : AFXGuiCommand
            Host command.
        name : str
            Keyword name.
        isRequired : bool
            True if this keyword is a required argument.
        minLength : int
            Minimum (and default) row length.
        maxLength : int
            Maximum row length (-1 => unlimited).
        opts : int
            Options.
        """

    def getTypeName(self):
        """Returns the name of the table keyword type.

        Reimplemented from AFXComTableKeyword.
        """
