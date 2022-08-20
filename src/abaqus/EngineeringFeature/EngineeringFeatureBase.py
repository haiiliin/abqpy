import typing

from .Crack import Crack
from .Fastener import Fastener
from .Inertia import Inertia
from .SpringDashpot import SpringDashpot
from ..Region.Region import Region
from .._decorators import abaqus_class_doc, abaqus_method_doc


@abaqus_class_doc
class EngineeringFeatureBase:
    """The EngineeringFeature object is a container for various specific engineering feature
    repositories. The EngineeringFeature object has no explicit constructor or methods.

    .. note:: 
        This object can be accessed by:

        .. code-block:: python

            import part
            mdb.models[name].parts[name].engineeringFeatures
            import assembly
            mdb.models[name].rootAssembly.engineeringFeatures
    """

    #: A repository of Inertia objects.
    inertias: typing.Dict[str, Inertia] = {}

    #: A repository of Crack objects.
    cracks: typing.Dict[str, Crack] = {}

    #: A repository of Fastener objects.
    fasteners: typing.Dict[str, Fastener] = {}

    #: A repository of SpringDashpot objects.
    springDashpots: typing.Dict[str, SpringDashpot] = {}

    @abaqus_method_doc
    def assignSeam(self, regions: typing.Tuple[Region, ...]):
        """This method creates a seam crack along an edge or a face.

        Parameters
        ----------
        regions
            A sequence of Region objects specifying the domain of the seam crack. The Region objects
            must be faces or edges.
        """
        ...

    @abaqus_method_doc
    def deleteSeam(self, regions: typing.Tuple[Region, ...]):
        """This method deletes a seam crack.

        Parameters
        ----------
        regions
            A sequence of Region objects specifying the domain of the seam crack. The Region objects
            must be faces or edges.
        """
        ...
