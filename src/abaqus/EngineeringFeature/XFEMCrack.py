from typing import Optional

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from .Crack import Crack
from ..Region.Region import Region
from ..UtilityAndView.abaqusConstants import Boolean, OFF, ON


@abaqus_class_doc
class XFEMCrack(Crack):
    """The XFEMCrack object defines the parameters needed to model crack initiation or crack
    growth using XFEM technology. Currently only assembly regions are supported.
    The XFEMCrack object is derived from the Crack object.

    .. note::
        This object can be accessed by::

            import part
            mdb.models[name].parts[name].engineeringFeatures.cracks[name]
            import assembly
            mdb.models[name].rootAssembly.engineeringFeatures.cracks[name]

        The corresponding analysis keywords are:

        - ENRICHMENT
        - INITIAL CONDITIONS
    """

    #: A Boolean specifying whether the crack is suppressed or not. The default value is OFF.
    suppressed: Boolean = OFF

    #: A String specifying the repository key.
    name: str

    #: A :py:class:`~abaqus.Region.Region.Region` object specifying the region that contains the crack or is likely to contain
    #: the crack.
    crackDomain: Region

    #: A Boolean specifying whether the crack is allowed to propagate (grow). The default value
    #: is ON.
    allowCrackGrowth: Boolean = ON

    #: A :py:class:`~abaqus.Region.Region.Region` object specifying the initial crack location. This parameter is required when
    #: **allowCrackGrowth** = OFF.
    crackLocation: Optional[Region] = None

    #: None or a Float specifying the radius from the crack tips within which the elements are
    #: used for crack singularity calculations. This argument applies only when
    #: **allowCrackGrowth** = OFF. The default value is None.
    singularityCalcRadius: Optional[float] = None

    #: A String specifying the name of the ContactProperty object that defines the contact
    #: properties for the crack surfaces. The default value is an empty string.
    interactionProperty: str = ""

    #: A sequence of Ints specifying the labels of the elements that are intersected by the
    #: initial crack location. This argument is used only by the input file reader.
    elemId: tuple = ()

    #: A sequence of Ints specifying the position of a node in the corresponding element
    #: connectivity. This argument is used only by the input file reader.
    nodeId: tuple = ()

    #: A sequence of Ints specifying the values indicating the inclusion/exclusion of the
    #: **crackFrontDist** values. A zero value indicates that **crackFrontDist** is not specified
    #: for the ith pair **elemId** and *nodeId*. This argument is used only by the input file
    #: reader.
    hasCrackFront: tuple = ()

    #: A sequence of Floats specifying the values of the first signed distance function. This
    #: argument is used by the input file reader.
    crackPlaneDist: tuple = ()

    #: A sequence of Floats specifying the values of the second signed distance function. This
    #: argument is used only by the input file reader.
    crackFrontDist: tuple = ()

    #: An integer specifying the number of element layers around the crack location, to which
    #: the crack domain is shrunk.
    autoDetectValue: str = ""

    @abaqus_method_doc
    def __init__(
        self,
        name: str,
        crackDomain: Region,
        allowCrackGrowth: Boolean = ON,
        crackLocation: Optional[Region] = None,
        singularityCalcRadius: Optional[float] = None,
        interactionProperty: str = "",
        elemId: tuple = (),
        nodeId: tuple = (),
        hasCrackFront: tuple = (),
        crackPlaneDist: tuple = (),
        crackFrontDist: tuple = (),
        autoDetectValue: str = "",
    ):
        """This method creates a XFEMCrack object. Although the constructor is available both for
        parts and for the assembly, XFEMCrack objects are currently supported only under the
        assembly.

        .. note::
            This function can be accessed by::

                mdb.models[name].parts[name].engineeringFeatures.XFEMCrack
                mdb.models[name].rootAssembly.engineeringFeatures.XFEMCrack

        Parameters
        ----------
        name
            A String specifying the repository key.
        crackDomain
            A :py:class:`~abaqus.Region.Region.Region` object specifying the region that contains the crack or is likely to contain
            the crack.
        allowCrackGrowth
            A Boolean specifying whether the crack is allowed to propagate (grow). The default value
            is ON.
        crackLocation
            A :py:class:`~abaqus.Region.Region.Region` object specifying the initial crack location. This parameter is required when
            **allowCrackGrowth** = OFF.
        singularityCalcRadius
            None or a Float specifying the radius from the crack tips within which the elements are
            used for crack singularity calculations. This argument applies only when
            **allowCrackGrowth** = OFF. The default value is None.
        interactionProperty
            A String specifying the name of the ContactProperty object that defines the contact
            properties for the crack surfaces. The default value is an empty string.
        elemId
            A sequence of Ints specifying the labels of the elements that are intersected by the
            initial crack location. This argument is used only by the input file reader.
        nodeId
            A sequence of Ints specifying the position of a node in the corresponding element
            connectivity. This argument is used only by the input file reader.
        hasCrackFront
            A sequence of Ints specifying the values indicating the inclusion/exclusion of the
            **crackFrontDist** values. A zero value indicates that **crackFrontDist** is not specified
            for the ith pair **elemId** and *nodeId*. This argument is used only by the input file
            reader.
        crackPlaneDist
            A sequence of Floats specifying the values of the first signed distance function. This
            argument is used by the input file reader.
        crackFrontDist
            A sequence of Floats specifying the values of the second signed distance function. This
            argument is used only by the input file reader.
        autoDetectValue
            An integer specifying the number of element layers around the crack location, to which
            the crack domain is shrunk.

        Returns
        -------
        XFEMCrack
            A :py:class:`~abaqus.EngineeringFeature.XFEMCrack.XFEMCrack` object.
        """
        super().__init__()

    @abaqus_method_doc
    def setValues(
        self,
        allowCrackGrowth: Boolean = ON,
        crackLocation: Optional[Region] = None,
        singularityCalcRadius: Optional[float] = None,
        interactionProperty: str = "",
        elemId: tuple = (),
        nodeId: tuple = (),
        hasCrackFront: tuple = (),
        crackPlaneDist: tuple = (),
        crackFrontDist: tuple = (),
        autoDetectValue: str = "",
    ):
        """This method modifies the XFEMCrack object.

        Parameters
        ----------
        allowCrackGrowth
            A Boolean specifying whether the crack is allowed to propagate (grow). The default value
            is ON.
        crackLocation
            A :py:class:`~abaqus.Region.Region.Region` object specifying the initial crack location. This parameter is required when
            **allowCrackGrowth** = OFF.
        singularityCalcRadius
            None or a Float specifying the radius from the crack tips within which the elements are
            used for crack singularity calculations. This argument applies only when
            **allowCrackGrowth** = OFF. The default value is None.
        interactionProperty
            A String specifying the name of the ContactProperty object that defines the contact
            properties for the crack surfaces. The default value is an empty string.
        elemId
            A sequence of Ints specifying the labels of the elements that are intersected by the
            initial crack location. This argument is used only by the input file reader.
        nodeId
            A sequence of Ints specifying the position of a node in the corresponding element
            connectivity. This argument is used only by the input file reader.
        hasCrackFront
            A sequence of Ints specifying the values indicating the inclusion/exclusion of the
            **crackFrontDist** values. A zero value indicates that **crackFrontDist** is not specified
            for the ith pair **elemId** and *nodeId*. This argument is used only by the input file
            reader.
        crackPlaneDist
            A sequence of Floats specifying the values of the first signed distance function. This
            argument is used by the input file reader.
        crackFrontDist
            A sequence of Floats specifying the values of the second signed distance function. This
            argument is used only by the input file reader.
        autoDetectValue
            An integer specifying the number of element layers around the crack location, to which
            the crack domain is shrunk.
        """
        ...
