from abaqusConstants import *
from .Crack import Crack
from ..Region.Region import Region


class XFEMCrack(Crack):
    """The XFEMCrack object defines the parameters needed to model crack initiation or crack
    growth using XFEM technology. Currently only assembly regions are supported.
    The XFEMCrack object is derived from the Crack object.

    Attributes
    ----------
    suppressed: Boolean
        A Boolean specifying whether the crack is suppressed or not. The default value is OFF.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import part
        mdb.models[name].parts[name].engineeringFeatures.cracks[name]
        import assembly
        mdb.models[name].rootAssembly.engineeringFeatures.cracks[name]

    The corresponding analysis keywords are:

    - ENRICHMENT
            - INITIAL CONDITIONS
    """

    # A Boolean specifying whether the crack is suppressed or not. The default value is OFF.
    suppressed: Boolean = OFF

    def __init__(
        self,
        name: str,
        crackDomain: Region,
        allowCrackGrowth: Boolean = ON,
        crackLocation: Region = None,
        singularityCalcRadius: float = None,
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

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            mdb.models[name].parts[name].engineeringFeatures.XFEMCrack
            mdb.models[name].rootAssembly.engineeringFeatures.XFEMCrack

        Parameters
        ----------
        name
            A String specifying the repository key.
        crackDomain
            A Region object specifying the region that contains the crack or is likely to contain
            the crack.
        allowCrackGrowth
            A Boolean specifying whether the crack is allowed to propagate (grow). The default value
            is ON.
        crackLocation
            A Region object specifying the initial crack location. This parameter is required when
            *allowCrackGrowth*=OFF.
        singularityCalcRadius
            None or a Float specifying the radius from the crack tips within which the elements are
            used for crack singularity calculations. This argument applies only when
            *allowCrackGrowth*=OFF. The default value is None.
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
            *crackFrontDist* values. A zero value indicates that *crackFrontDist* is not specified
            for the ith pair *elemId* and *nodeId*. This argument is used only by the input file
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
        A XFEMCrack object.
        """
        super().__init__()
        pass

    def setValues(
        self,
        allowCrackGrowth: Boolean = ON,
        crackLocation: Region = None,
        singularityCalcRadius: float = None,
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
            A Region object specifying the initial crack location. This parameter is required when
            *allowCrackGrowth*=OFF.
        singularityCalcRadius
            None or a Float specifying the radius from the crack tips within which the elements are
            used for crack singularity calculations. This argument applies only when
            *allowCrackGrowth*=OFF. The default value is None.
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
            *crackFrontDist* values. A zero value indicates that *crackFrontDist* is not specified
            for the ith pair *elemId* and *nodeId*. This argument is used only by the input file
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
        pass
