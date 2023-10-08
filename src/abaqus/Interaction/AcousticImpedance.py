from typing_extensions import Literal

from abqpy.decorators import abaqus_class_doc

from ..Region.Region import Region
from ..UtilityAndView.abaqusConstants import PLANE, TABULAR, SymbolicConstant
from ..UtilityAndView.abaqusConstants import abaqusConstants as C
from .Interaction import Interaction


@abaqus_class_doc
class AcousticImpedance(Interaction):
    """The AcousticImpedance object defines surface impedance information or nonreflecting boundaries for
    acoustic and coupled acoustic-structural analyses. The AcousticImpedance object is derived from the
    Interaction object.

    .. note::
        This object can be accessed by::

            import interaction
            mdb.models[name].interactions[name]

        The corresponding analysis keywords are:

        - SIMPEDANCE
    """

    #: A String specifying the repository key.
    name: str

    #: A String specifying the name of the step in which the AcousticImpedance object is
    #: created.
    createStepName: str

    #: A Region object specifying the acoustic boundary surface.
    surface: Region

    #: A SymbolicConstant specifying the type of acoustic impedance to be defined. Possible
    #: values are TABULAR and NONREFLECTING. The default value is TABULAR.
    definition: SymbolicConstant = TABULAR

    #: A String specifying the AcousticImpedanceProp object associated with this interaction.
    interactionProperty: str = ""

    #: A SymbolicConstant specifying the type of nonreflecting geometry to be defined. Possible
    #: values are PLANE, IMPROVED, CIRCULAR, SPHERICAL, ELLIPTICAL, and PROLATE. The default
    #: value is PLANE.This argument is valid only when **definition** = NONREFLECTING.
    nonreflectingType: SymbolicConstant = PLANE

    #: A Float specifying the radius of the circle or sphere defining the boundary surface. The
    #: default value is 1.0.This argument is valid only when **definition** = NONREFLECTING, and
    #: **nonreflectingType** = CIRCULAR or SPHERICAL.
    radius: float = 1

    #: A Float specifying the semimajor axis length of the ellipse or prolate spheroid defining
    #: the boundary surface. The default value is 1.0.This argument is valid only when
    #: **definition** = NONREFLECTING, and **nonreflectingType** = ELLIPTICAL or PROLATE.
    semimajorAxis: float = 1

    #: A Float specifying the eccentricity of the ellipse or prolate spheroid defining the
    #: boundary surface. The default value is 0.0.This argument is valid only when
    #: **definition** = NONREFLECTING, and **nonreflectingType** = ELLIPTICAL or PROLATE.
    eccentricity: float = 0

    #: A sequence of three Floats specifying the X, Y, and Z coordinates of the center of the
    #: ellipse or prolate spheroid defining the boundary surface. The default value is (0, 0,
    #: 0).This argument is valid only when **definition** = NONREFLECTING, and
    #: **nonreflectingType** = ELLIPTICAL or PROLATE.
    centerCoordinates: tuple = ()

    #: A sequence of three Floats specifying the X, Y, and Z components of the direction cosine
    #: of the major axis of the ellipse or prolate spheroid defining the boundary surface. The
    #: default value is (0, 0, 1).This argument is valid only when **definition** = NONREFLECTING,
    #: and **nonreflectingType** = ELLIPTICAL or PROLATE.
    directionCosine: tuple = ()

    def __init__(
        self,
        name: str,
        createStepName: str,
        surface: Region,
        definition: Literal[C.TABULAR, C.NONREFLECTING] = TABULAR,
        interactionProperty: str = "",
        nonreflectingType: Literal[
            C.PLANE, C.ELLIPTICAL, C.IMPROVED, C.SPHERICAL, C.PROLATE, C.CIRCULAR, C.NONREFLECTING
        ] = PLANE,
        radius: float = 1,
        semimajorAxis: float = 1,
        eccentricity: float = 0,
        centerCoordinates: tuple = (),
        directionCosine: tuple = (),
    ):
        """This method creates an AcousticImpedance object.

        .. note::
            This function can be accessed by::

                mdb.models[name].AcousticImpedance

        Parameters
        ----------
        name
            A String specifying the repository key.
        createStepName
            A String specifying the name of the step in which the AcousticImpedance object is
            created.
        surface
            A Region object specifying the acoustic boundary surface.
        definition
            A SymbolicConstant specifying the type of acoustic impedance to be defined. Possible
            values are TABULAR and NONREFLECTING. The default value is TABULAR.
        interactionProperty
            A String specifying the AcousticImpedanceProp object associated with this interaction.
        nonreflectingType
            A SymbolicConstant specifying the type of nonreflecting geometry to be defined. Possible
            values are PLANE, IMPROVED, CIRCULAR, SPHERICAL, ELLIPTICAL, and PROLATE. The default
            value is PLANE.This argument is valid only when **definition** = NONREFLECTING.
        radius
            A Float specifying the radius of the circle or sphere defining the boundary surface. The
            default value is 1.0.This argument is valid only when **definition** = NONREFLECTING, and
            **nonreflectingType** = CIRCULAR or SPHERICAL.
        semimajorAxis
            A Float specifying the semimajor axis length of the ellipse or prolate spheroid defining
            the boundary surface. The default value is 1.0.This argument is valid only when
            **definition** = NONREFLECTING, and **nonreflectingType** = ELLIPTICAL or PROLATE.
        eccentricity
            A Float specifying the eccentricity of the ellipse or prolate spheroid defining the
            boundary surface. The default value is 0.0.This argument is valid only when
            **definition** = NONREFLECTING, and **nonreflectingType** = ELLIPTICAL or PROLATE.
        centerCoordinates
            A sequence of three Floats specifying the X, Y, and Z coordinates of the center of the
            ellipse or prolate spheroid defining the boundary surface. The default value is (0, 0,
            0).This argument is valid only when **definition** = NONREFLECTING, and
            **nonreflectingType** = ELLIPTICAL or PROLATE.
        directionCosine
            A sequence of three Floats specifying the X, Y, and Z components of the direction cosine
            of the major axis of the ellipse or prolate spheroid defining the boundary surface. The
            default value is (0, 0, 1).This argument is valid only when **definition** = NONREFLECTING,
            and **nonreflectingType** = ELLIPTICAL or PROLATE.

        Returns
        -------
        AcousticImpedance
            An AcousticImpedance object.
        """
        super().__init__()

    def setValues(
        self,
        definition: Literal[C.TABULAR, C.NONREFLECTING] = TABULAR,
        interactionProperty: str = "",
        nonreflectingType: Literal[
            C.PLANE, C.ELLIPTICAL, C.IMPROVED, C.SPHERICAL, C.PROLATE, C.CIRCULAR, C.NONREFLECTING
        ] = PLANE,
        radius: float = 1,
        semimajorAxis: float = 1,
        eccentricity: float = 0,
        centerCoordinates: tuple = (),
        directionCosine: tuple = (),
    ):
        """This method modifies the data for an existing AcousticImpedance object in the step where it is
        created.

        Parameters
        ----------
        definition
            A SymbolicConstant specifying the type of acoustic impedance to be defined. Possible
            values are TABULAR and NONREFLECTING. The default value is TABULAR.
        interactionProperty
            A String specifying the AcousticImpedanceProp object associated with this interaction.
        nonreflectingType
            A SymbolicConstant specifying the type of nonreflecting geometry to be defined. Possible
            values are PLANE, IMPROVED, CIRCULAR, SPHERICAL, ELLIPTICAL, and PROLATE. The default
            value is PLANE.This argument is valid only when **definition** = NONREFLECTING.
        radius
            A Float specifying the radius of the circle or sphere defining the boundary surface. The
            default value is 1.0.This argument is valid only when **definition** = NONREFLECTING, and
            **nonreflectingType** = CIRCULAR or SPHERICAL.
        semimajorAxis
            A Float specifying the semimajor axis length of the ellipse or prolate spheroid defining
            the boundary surface. The default value is 1.0.This argument is valid only when
            **definition** = NONREFLECTING, and **nonreflectingType** = ELLIPTICAL or PROLATE.
        eccentricity
            A Float specifying the eccentricity of the ellipse or prolate spheroid defining the
            boundary surface. The default value is 0.0.This argument is valid only when
            **definition** = NONREFLECTING, and **nonreflectingType** = ELLIPTICAL or PROLATE.
        centerCoordinates
            A sequence of three Floats specifying the X, Y, and Z coordinates of the center of the
            ellipse or prolate spheroid defining the boundary surface. The default value is (0, 0,
            0).This argument is valid only when **definition** = NONREFLECTING, and
            **nonreflectingType** = ELLIPTICAL or PROLATE.
        directionCosine
            A sequence of three Floats specifying the X, Y, and Z components of the direction cosine
            of the major axis of the ellipse or prolate spheroid defining the boundary surface. The
            default value is (0, 0, 1).This argument is valid only when **definition** = NONREFLECTING,
            and **nonreflectingType** = ELLIPTICAL or PROLATE.
        """
        ...

    def setValuesInStep(self, stepName: str, interactionProperty: str = ""):
        """This method modifies the propagating data for an existing AcousticImpedance object in the specified
        step.

        Parameters
        ----------
        stepName
            A String specifying the name of the step in which the interaction is modified.
        interactionProperty
            A String specifying the AcousticImpedanceProp object associated with this interaction.
        """
        ...
