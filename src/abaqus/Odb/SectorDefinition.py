from typing import Optional

from abqpy.decorators import abaqus_class_doc


@abaqus_class_doc
class SectorDefinition:
    """The SectorDefinition object describes the number of symmetry sectors and axis of symmetry for a cyclic
    symmetry model.

    .. note::
        This object can be accessed by::

            import odbAccess
            session.odbs[name].sectorDefinition
    """

    #: An Int specifying the number of sectors in the cyclic symmetry model.
    numSectors: Optional[int] = None

    #: A tuple of tuples of Floats specifying the coordinates of two points on the axis of
    #: symmetry.
    symmetryAxis: Optional[float] = None
