from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from typing_extensions import Literal

from ..Region.Region import Region
from ..UtilityAndView.abaqusConstants import Boolean, NONE, OFF, SymbolicConstant
from ..UtilityAndView.abaqusConstants import abaqusConstants as C


@abaqus_class_doc
class ElementProgressiveActivation:
    """The ElementProgressiveActivation object is used to specify elements that can be
    activated during an analysis.

    .. note::
        This object can be accessed by::

            mdb.models[name].rootAssembly.elementProgressiveActivations[name]

        The corresponding analysis keywords are:

        - ELEMENT PROGRESSIVE ACTIVATION

    .. versionadded:: 2020
        The `ElementProgressiveActivation` class was added.
    """

    #: A String specifying the key of the repository.
    name: str

    #: A :py:class:`~abaqus.Region.Region.Region` object specifying the region containing the elements that will be activated
    #: during the analysis.
    elset: Region

    #: A Boolean value specifying whether the elements that have not yet been activated will
    #: follow the deformations of the active elements. Set **deformation** = ON when the
    #: deformation of the active elements is excessive. The default value is OFF.
    deformation: Boolean = OFF

    #: A SymbolicConstant specifying the exposed areas of the element facets that are active
    #: for convection or radiation boundary conditions to be applied. Possible values are NONE
    #: and FACET. If **freeSurfaceType** = FACET, user subroutine UEPACTIVATIONFACET will be called
    #: at the start of the increment for each element. If **freeSurfaceType** = NONE, all the
    #: exposed areas of the element facets are considered. The default value is NONE.
    freeSurfaceType: SymbolicConstant = NONE

    @abaqus_method_doc
    def __init__(
        self,
        name: str,
        elset: Region,
        deformation: Boolean = OFF,
        freeSurfaceType: Literal[C.FACET, C.NONE] = NONE,
    ):
        """This method creates an ElementProgressiveActivation object and places it in the
        elementProgressiveActivation repository.

        .. note::
            This function can be accessed by::

                mdb.models[name].rootAssembly.ElementProgressiveActivation

        Parameters
        ----------
        name
            A String specifying the key of the repository.
        elset
            A :py:class:`~abaqus.Region.Region.Region` object specifying the region containing the elements that will be activated
            during the analysis.
        deformation
            A Boolean value specifying whether the elements that have not yet been activated will
            follow the deformations of the active elements. Set **deformation** = ON when the
            deformation of the active elements is excessive. The default value is OFF.
        freeSurfaceType
            A SymbolicConstant specifying the exposed areas of the element facets that are active
            for convection or radiation boundary conditions to be applied. Possible values are NONE
            and FACET. If **freeSurfaceType** = FACET, user subroutine UEPACTIVATIONFACET will be called
            at the start of the increment for each element. If **freeSurfaceType** = NONE, all the
            exposed areas of the element facets are considered. The default value is NONE.

        Returns
        -------
        ElementProgressiveActivation
            An :py:class:`~abaqus.TableCollection.ElementProgressiveActivation.ElementProgressiveActivation` object.

        Raises
        ------
        AbaqusException
            If the region does not contain only elements.
        """
        ...

    @abaqus_method_doc
    def setValue(self):
        """The method modifies the ElementProgressiveActivation object.

        Returns
        -------

        Raises
        ------
        """
        ...
