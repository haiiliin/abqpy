from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from ..Assembly.AssemblyBase import AssemblyBase
from ..UtilityAndView.abaqusConstants import Boolean


@abaqus_class_doc
class RegionAssemblyBase(AssemblyBase):
    """The following commands operate on Assembly objects. For more information about the
    Assembly object, see Assembly object.

    .. note:: 
        This object can be accessed by::

            import regionToolset
    """

    @abaqus_method_doc
    def clashSets(self, arg1: str, arg2: str):
        """This command prints a message describing the relationship between the contents of two
        sets. Possible outcomes are:
        
        - Both sets are the same.
        - Set 2 is a subset of set 1.
        - Set 2 is a superset of set 1.
        - Set 2 intersects set 1.
        - Set 2 touches set 1 (their boundaries intersect).
        - Set 2 and set 1 are disjoint.
        
        This command accepts only positional arguments and has no keywords.

        Parameters
        ----------
        arg1
            A Set or Surface object specifying set 1.
        arg2
            A Set or Surface object specifying set 2.
        """
        ...

    @abaqus_method_doc
    def deleteSets(self, setNames: tuple):
        """This command deletes the given sets from the assembly.

        Parameters
        ----------
        setNames
            A sequence of Strings specifying the set names that will be deleted from the assembly.
        """
        ...

    @abaqus_method_doc
    def markSetInternal(self, setName: str, internalSet: Boolean):
        """This command marks the given Set as internal or external.

        Parameters
        ----------
        setName
            A string specifying the Set name.
        internalSet
            A Boolean specifying whether the Set should be marked as internal.
        """
        ...

    @abaqus_method_doc
    def markSurfaceInternal(self, setName: str, internalSurface: Boolean):
        """This command marks the given Surface as internal or external.

        Parameters
        ----------
        setName
            A string specifying the Surface name.
        internalSurface
            A Boolean specifying whether the Surface should be marked as internal.
        """
        ...

    @abaqus_method_doc
    def isSetInternal(self, setName: str):
        """This command returns a flag indicating whether the Set is Internal.

        Parameters
        ----------
        setName
            A string specifying the Set name.
        """
        ...

    @abaqus_method_doc
    def isSurfaceInternal(self, surfaceName: str):
        """This command returns a flag indicating whether the Surface is Internal.

        Parameters
        ----------
        surfaceName
            A string specifying the Surface name.
        """
        ...

    @abaqus_method_doc
    def deleteSurfaces(self, surfaceNames: tuple):
        """This command deletes the given surfaces from the assembly.

        Parameters
        ----------
        surfaceNames
            A sequence of Strings specifying the surface names that will be deleted from the
            assembly.
        """
        ...
