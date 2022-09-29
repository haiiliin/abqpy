from typing import Optional

from abqpy.decorators import abaqus_class_doc
from .OdbSet import OdbSet


@abaqus_class_doc
class OdbPretensionSection:
    """The pretension section object is used to define an assembly load. It associates a
    pretension node with a pretension section.

    .. note:: 
        This object can be accessed by::

            import odbAccess
            session.odbs[name].rootAssembly.pretensionSections[i]
    """

    #: An :py:class:`~abaqus.Odb.OdbSet.OdbSet` object specifying the node set containing the pretension node.
    node: OdbSet = OdbSet("set", ())

    #: An :py:class:`~abaqus.Odb.OdbSet.OdbSet` object specifying the element set that defines the pretension section.
    element: OdbSet = OdbSet("set", ())

    #: An :py:class:`~abaqus.Odb.OdbSet.OdbSet` object specifying the surface set that defines the pretension section.
    surface: OdbSet = OdbSet("set", ())

    #: A tuple of Floats specifying the components of the normal to the pretension section.
    normal: Optional[float] = None
