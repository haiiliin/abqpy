from .Crack import Crack
from .Fastener import Fastener
from .Inertia import Inertia
from .SpringDashpot import SpringDashpot
from ..Region.Region import Region


class EngineeringFeatureBase:
    """The EngineeringFeature object is a container for various specific engineering feature
    repositories. The EngineeringFeature object has no explicit constructor or methods.

    Attributes
    ----------
    inertias: dict[str, Inertia]
        A repository of :py:class:`~abaqus.EngineeringFeature.Inertia.Inertia` objects.
    cracks: dict[str, Crack]
        A repository of :py:class:`~abaqus.EngineeringFeature.Crack.Crack` objects.
    fasteners: dict[str, Fastener]
        A repository of :py:class:`~abaqus.EngineeringFeature.Fastener.Fastener` objects.
    springDashpots: dict[str, SpringDashpot]
        A repository of :py:class:`~abaqus.EngineeringFeature.SpringDashpot.SpringDashpot` objects.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import part
        mdb.models[name].parts[name].engineeringFeatures
        import assembly
        mdb.models[name].rootAssembly.engineeringFeatures
    """

    #: A repository of Inertia objects.
    inertias: dict[str, Inertia] = dict[str, Inertia]()

    #: A repository of Crack objects.
    cracks: dict[str, Crack] = dict[str, Crack]()

    #: A repository of Fastener objects.
    fasteners: dict[str, Fastener] = dict[str, Fastener]()

    #: A repository of SpringDashpot objects.
    springDashpots: dict[str, SpringDashpot] = dict[str, SpringDashpot]()

    def assignSeam(self, regions: tuple[Region]):
        """This method creates a seam crack along an edge or a face.

        Parameters
        ----------
        regions
            A sequence of Region objects specifying the domain of the seam crack. The Region objects
            must be faces or edges.
        """
        pass

    def deleteSeam(self, regions: tuple[Region]):
        """This method deletes a seam crack.

        Parameters
        ----------
        regions
            A sequence of Region objects specifying the domain of the seam crack. The Region objects
            must be faces or edges.
        """
        pass
