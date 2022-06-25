from .DisplayGroup import DisplayGroup
from .Leaf import Leaf
from ..Session.SessionBase import SessionBase


class DisplayGroupSession(SessionBase):
    def DisplayGroup(self, name: str, leaf: Leaf) -> DisplayGroup:
        """This method creates a DisplayGroup object.

        .. note:: 
            This function can be accessed by:

            .. code-block:: python

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
        self.displayGroups[name] = displayGroup = DisplayGroup(name, leaf)
        return displayGroup
