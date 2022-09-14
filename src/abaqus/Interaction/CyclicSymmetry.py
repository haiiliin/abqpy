from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from .Interaction import Interaction
from ..Region.Region import Region
from ..UtilityAndView.abaqusConstants import *


@abaqus_class_doc
class CyclicSymmetry(Interaction):
    """The CyclicSymmetry object defines a cyclic symmetry analysis.
    The CyclicSymmetry object is derived from the Interaction object.

    .. note:: 
        This object can be accessed by::

            import interaction
            mdb.models[name].interactions[name]

        The corresponding analysis keywords are:

        - CLOAD
        - CYCLIC SYMMETRY MODEL
        - DLOAD        - CLOAD        - CYCLIC SYMMETRY MODEL
        - DLOAD        - SELECT CYCLIC SYMMETRY MODES
        - TIE
    """

    #: A String specifying the repository key.
    name: str

    #: A String specifying the name of the step in which the cyclic symmetry interaction should
    #: be created.
    createStepName: str

    #: A :py:class:`~abaqus.Region.Region.Region` object specifying the master surface.
    master: Region

    #: A :py:class:`~abaqus.Region.Region.Region` object specifying the slave surface.
    slave: Region

    #: An Int specifying the total number of sectors in the cyclic symmetric model.
    repetitiveSectors: int

    #: A :py:class:`~abaqus.Region.Region.Region` object specifying the first point of the axis of symmetry. The region should
    #: contain exactly one mesh node, vertex, interesting point, reference point, or datum
    #: point. In a two-dimensional model **axisPoint1** is the only point used to define the axis
    #: of symmetry.
    axisPoint1: Region

    #: A :py:class:`~abaqus.Region.Region.Region` object specifying the second point of the axis of symmetry. The region should
    #: contain exactly one mesh node, vertex, interesting point, reference point, or datum
    #: point. This point is ignored in a two-dimensional model.
    axisPoint2: Region

    #: A SymbolicConstant specifying whether Abaqus should extract all possible nodal diameters
    #: or the nodal diameters between the user-specified values for **lowestNodalDiameter** and
    #: **highestNodalDiameter**. Possible values are ALL_NODAL_DIAMETER and
    #: SPECIFIED_NODAL_DIAMETER. The default value is ALL_NODAL_DIAMETER.
    extractedNodalDiameter: SymbolicConstant = ALL_NODAL_DIAMETER

    #: An Int specifying the lowest nodal diameter to be used in the eigenfrequency analysis.
    #: The default value is 0.
    lowestNodalDiameter: int = 0

    #: An Int specifying the highest nodal diameter to be used in the eigenfrequency analysis.
    #: This argument value should be less than or equal to the half of the total number of
    #: sectors (as specified in the **repetitiveSectors** parameter). The default value is 0.
    highestNodalDiameter: int = 0

    #: An Int specifying the nodal diameter for which the modal-based steady-state dynamic
    #: analysis will be performed. This value should be greater than or equal to the lowest
    #: nodal diameter (specified in the **lowestNodalDiameter** parameter), and less than or
    #: equal to the highest nodal diameter (specified in the **highestNodalDiameter** parameter).
    #: The default value is 0.
    excitationNodalDiameter: int = 0

    #: A Boolean specifying whether or not to adjust the slave surface of the cyclic
    #: symmetry to tie it to the master surface. The default value is ON.
    adjustTie: Boolean = ON

    #: A Float specifying the position tolerance. The*positionTolerance* argument applies only
    #: when **positionToleranceMethod** = SPECIFY_TOLERANCE. The default value is 0.0.
    positionTolerance: float = 0

    #: A SymbolicConstant specifying the method used to determine the position tolerance.
    #: Possible values are COMPUTED_TOLERANCE and SPECIFY_TOLERANCE. The default value is
    #: COMPUTED_TOLERANCE.
    positionToleranceMethod: SymbolicConstant = COMPUTED_TOLERANCE

    @abaqus_method_doc
    def __init__(
        self,
        name: str,
        createStepName: str,
        master: Region,
        slave: Region,
        repetitiveSectors: int,
        axisPoint1: Region,
        axisPoint2: Region,
        extractedNodalDiameter: SymbolicConstant = ALL_NODAL_DIAMETER,
        lowestNodalDiameter: int = 0,
        highestNodalDiameter: int = 0,
        excitationNodalDiameter: int = 0,
        adjustTie: Boolean = ON,
        positionTolerance: float = 0,
        positionToleranceMethod: SymbolicConstant = COMPUTED_TOLERANCE,
    ):
        """This method creates a CyclicSymmetry object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].CyclicSymmetry

        Parameters
        ----------
        name
            A String specifying the repository key.
        createStepName
            A String specifying the name of the step in which the cyclic symmetry interaction should
            be created.
        master
            A :py:class:`~abaqus.Region.Region.Region` object specifying the master surface.
        slave
            A :py:class:`~abaqus.Region.Region.Region` object specifying the slave surface.
        repetitiveSectors
            An Int specifying the total number of sectors in the cyclic symmetric model.
        axisPoint1
            A :py:class:`~abaqus.Region.Region.Region` object specifying the first point of the axis of symmetry. The region should
            contain exactly one mesh node, vertex, interesting point, reference point, or datum
            point. In a two-dimensional model **axisPoint1** is the only point used to define the axis
            of symmetry.
        axisPoint2
            A :py:class:`~abaqus.Region.Region.Region` object specifying the second point of the axis of symmetry. The region should
            contain exactly one mesh node, vertex, interesting point, reference point, or datum
            point. This point is ignored in a two-dimensional model.
        extractedNodalDiameter
            A SymbolicConstant specifying whether Abaqus should extract all possible nodal diameters
            or the nodal diameters between the user-specified values for **lowestNodalDiameter** and
            **highestNodalDiameter**. Possible values are ALL_NODAL_DIAMETER and
            SPECIFIED_NODAL_DIAMETER. The default value is ALL_NODAL_DIAMETER.
        lowestNodalDiameter
            An Int specifying the lowest nodal diameter to be used in the eigenfrequency analysis.
            The default value is 0.
        highestNodalDiameter
            An Int specifying the highest nodal diameter to be used in the eigenfrequency analysis.
            This argument value should be less than or equal to the half of the total number of
            sectors (as specified in the **repetitiveSectors** parameter). The default value is 0.
        excitationNodalDiameter
            An Int specifying the nodal diameter for which the modal-based steady-state dynamic
            analysis will be performed. This value should be greater than or equal to the lowest
            nodal diameter (specified in the **lowestNodalDiameter** parameter), and less than or
            equal to the highest nodal diameter (specified in the **highestNodalDiameter** parameter).
            The default value is 0.
        adjustTie
            A Boolean specifying whether or not to adjust the slave surface of the cyclic
            symmetry to tie it to the master surface. The default value is ON.
        positionTolerance
            A Float specifying the position tolerance. The*positionTolerance* argument applies only
            when **positionToleranceMethod** = SPECIFY_TOLERANCE. The default value is 0.0.
        positionToleranceMethod
            A SymbolicConstant specifying the method used to determine the position tolerance.
            Possible values are COMPUTED_TOLERANCE and SPECIFY_TOLERANCE. The default value is
            COMPUTED_TOLERANCE.

        Returns
        -------
        CyclicSymmetry
            A :py:class:`~abaqus.Interaction.CyclicSymmetry.CyclicSymmetry` object.
        """
        super().__init__()

    @abaqus_method_doc
    def swapSurfaces(self):
        """This method switches the master and slave surfaces of a cyclic symmetry interaction.
        This command is valid only during the step in which the interaction is created.
        """
        ...

    @abaqus_method_doc
    def setValues(
        self,
        extractedNodalDiameter: SymbolicConstant = ALL_NODAL_DIAMETER,
        lowestNodalDiameter: int = 0,
        highestNodalDiameter: int = 0,
        excitationNodalDiameter: int = 0,
        adjustTie: Boolean = ON,
        positionTolerance: float = 0,
        positionToleranceMethod: SymbolicConstant = COMPUTED_TOLERANCE,
    ):
        """This method modifies the data for an existing CyclicSymmetry object in the step where it
        is created.

        Parameters
        ----------
        extractedNodalDiameter
            A SymbolicConstant specifying whether Abaqus should extract all possible nodal diameters
            or the nodal diameters between the user-specified values for **lowestNodalDiameter** and
            **highestNodalDiameter**. Possible values are ALL_NODAL_DIAMETER and
            SPECIFIED_NODAL_DIAMETER. The default value is ALL_NODAL_DIAMETER.
        lowestNodalDiameter
            An Int specifying the lowest nodal diameter to be used in the eigenfrequency analysis.
            The default value is 0.
        highestNodalDiameter
            An Int specifying the highest nodal diameter to be used in the eigenfrequency analysis.
            This argument value should be less than or equal to the half of the total number of
            sectors (as specified in the **repetitiveSectors** parameter). The default value is 0.
        excitationNodalDiameter
            An Int specifying the nodal diameter for which the modal-based steady-state dynamic
            analysis will be performed. This value should be greater than or equal to the lowest
            nodal diameter (specified in the **lowestNodalDiameter** parameter), and less than or
            equal to the highest nodal diameter (specified in the **highestNodalDiameter** parameter).
            The default value is 0.
        adjustTie
            A Boolean specifying whether or not to adjust the slave surface of the cyclic
            symmetry to tie it to the master surface. The default value is ON.
        positionTolerance
            A Float specifying the position tolerance. The*positionTolerance* argument applies only
            when **positionToleranceMethod** = SPECIFY_TOLERANCE. The default value is 0.0.
        positionToleranceMethod
            A SymbolicConstant specifying the method used to determine the position tolerance.
            Possible values are COMPUTED_TOLERANCE and SPECIFY_TOLERANCE. The default value is
            COMPUTED_TOLERANCE.
        """
        ...

    @abaqus_method_doc
    def setValuesInStep(
        self,
        stepName: str,
        extractedNodalDiameter: SymbolicConstant = ALL_NODAL_DIAMETER,
        lowestNodalDiameter: int = 0,
        highestNodalDiameter: int = 0,
        excitationNodalDiameter: int = 0,
    ):
        """This method modifies the propagating data of an existing CyclicSymmetry object in the
        specified step.

        Parameters
        ----------
        stepName
            A String specifying the name of the step in which the interaction is modified.
        extractedNodalDiameter
            A SymbolicConstant specifying whether Abaqus should extract all possible nodal diameters
            or the nodal diameters between the user-specified values for **lowestNodalDiameter** and
            **highestNodalDiameter**. Possible values are ALL_NODAL_DIAMETER and
            SPECIFIED_NODAL_DIAMETER. The default value is ALL_NODAL_DIAMETER.
        lowestNodalDiameter
            An Int specifying the lowest nodal diameter to be used in the eigenfrequency analysis.
            The default value is 0.
        highestNodalDiameter
            An Int specifying the highest nodal diameter to be used in the eigenfrequency analysis.
            This argument value should be less than or equal to the half of the total number of
            sectors (as specified in the **repetitiveSectors** parameter). The default value is 0.
        excitationNodalDiameter
            An Int specifying the nodal diameter for which the modal-based steady-state dynamic
            analysis will be performed. This value should be greater than or equal to the lowest
            nodal diameter (specified in the **lowestNodalDiameter** parameter), and less than or
            equal to the highest nodal diameter (specified in the **highestNodalDiameter** parameter).
            The default value is 0.
        """
        ...
