from abqpy.decorators import abaqus_class_doc

from ..Session.SessionBase import SessionBase
from .DisplayGroup import DisplayGroup
from .Leaf import Leaf


@abaqus_class_doc
class DisplayGroupSession(SessionBase):
    def DisplayGroup(self, name: str, leaf: Leaf) -> DisplayGroup:
        """This method creates a DisplayGroup object.

        .. note::
            This function can be accessed by::

                session.DisplayGroup

        Parameters
        ----------
        name
            A String specifying the repository key.
        leaf
            A Leaf object specifying the items in the display group.

        Returns
        -------
        DisplayGroup
            A DisplayGroup object.
        """
        self.displayGroups[name] = displayGroup = DisplayGroup(name, leaf)
        return displayGroup
