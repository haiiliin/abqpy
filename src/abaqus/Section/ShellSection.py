from typing import Optional

from abqpy.decorators import abaqus_class_doc

from .Section import Section
from .TransverseShearShell import TransverseShearShell


@abaqus_class_doc
class ShellSection(Section):
    """The ShellSection object defines the properties of a shell section. The ShellSection
    object is derived from the Section object. The ShellSection object has no explicit
    constructor and no methods or members.
    The ShellSection object is derived from the Section object.

    .. note::
        This object can be accessed by::

            import section
            mdb.models[name].sections[name]
            import odbSection
            session.odbs[name].sections[name]
    """

    #: A String specifying the repository key.
    name: str = ""

    #: A :py:class:`~abaqus.Section.TransverseShearShell.TransverseShearShell` object specifying the transverse shear stiffness properties.
    transverseShear: Optional[TransverseShearShell] = None
