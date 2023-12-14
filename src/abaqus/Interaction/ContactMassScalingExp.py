from __future__ import annotations

from typing_extensions import Literal

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from ..Region.Region import Region
from ..UtilityAndView.abaqusConstants import SymbolicConstant
from ..UtilityAndView.abaqusConstants import abaqusConstants as C
from .Interaction import Interaction


@abaqus_class_doc
class ContactMassScalingExp(Interaction):
    """TThe ContactMassScalingExp object defines contact mass scaling during an Abaqus/Explicit analysis. The
    ContactMassScalingExp object is derived from the Interaction object.

    .. note::
        This object can be accessed by::

            import interaction
            mdb.models[name].interactions[name]

    .. versionadded:: 2024

        The ``ContactMassScalingExp`` class was added.
    """

    #: A String specifying the repository key.
    name: str

    #: A String specifying the name of the step in which the ContactMassScalingExp object is
    #: created.
    createStepName: str

    #: A SymbolicConstant specifying the location. Possible values are ELEMENT MASS SCALING
    #: (default), NONE, ALL CONTACT SURFACES, and SPECIFIED SURFACES.
    location: SymbolicConstant

    #: A tuple of Region objects specifying the surfaces when LOCATION=SPECIFIED SURFACES.
    surfaces: tuple[Region]

    @abaqus_method_doc
    def __init__(
        self,
        name: str,
        createStepName: str,
        location: Literal[
            C.ELEMENT_MASS_SCALING, C.NONE, C.ALL_CONTACT_SURFACES, C.SPECIFIED_SURFACES
        ] = C.ELEMENT_MASS_SCALING,
        surfaces: tuple = (),
    ):
        """This method creates an ContactMassScalingExp object.

        .. note::
            This function can be accessed by::

                mdb.models[name].ContactMassScalingExp

        Parameters
        ----------
        name
            A String specifying the repository key.
        createStepName
            A String specifying the name of the step in which the ContactMassScalingExp object is created.
        location
            A SymbolicConstant specifying the location. Possible values are ELEMENT MASS SCALING (default), NONE,
            ALL CONTACT SURFACES, and SPECIFIED SURFACES.
        surfaces
            A tuple of Region objects specifying the surfaces when LOCATION=SPECIFIED SURFACES.

        Returns
        -------
        ContactMassScalingExp
            An ContactMassScalingExp object.
        """
        super().__init__()

    @abaqus_method_doc
    def setValues(
        self,
        location: Literal[
            C.ELEMENT_MASS_SCALING, C.NONE, C.ALL_CONTACT_SURFACES, C.SPECIFIED_SURFACES
        ] = C.ELEMENT_MASS_SCALING,
        surfaces: tuple = (),
    ):
        """This method modifies the data for an existing ContactMassScalingExp object in the step where it is
        created.

        Parameters
        ----------
        location
            A SymbolicConstant specifying the location. Possible values are ELEMENT MASS SCALING (default), NONE,
            ALL CONTACT SURFACES, and SPECIFIED SURFACES.
        surfaces
            A tuple of Region objects specifying the surfaces when LOCATION=SPECIFIED SURFACES.
        """
        ...

    @abaqus_method_doc
    def setValuesInStep(
        self,
        stepName: str,
        location: Literal[
            C.ELEMENT_MASS_SCALING, C.NONE, C.ALL_CONTACT_SURFACES, C.SPECIFIED_SURFACES
        ] = C.ELEMENT_MASS_SCALING,
        surfaces: tuple = (),
    ):
        """This method modifies the propagating data for an existing ContactMassScalingExp object in the specified
        step.

        Parameters
        ----------
        stepName
            A String specifying the name of the step in which the interaction is modified.
        location
            A SymbolicConstant specifying the location. Possible values are ELEMENT MASS SCALING (default), NONE,
            ALL CONTACT SURFACES, and SPECIFIED SURFACES.
        surfaces
            A tuple of Region objects specifying the surfaces when LOCATION=SPECIFIED SURFACES.
        """
        ...
