from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from .Fastener import Fastener
from ..Region.Region import Region
from ..UtilityAndView.abaqusConstants import *


@abaqus_class_doc
class AssembledFastener(Fastener):
    """The AssembledFastener object defines an assembled fastener.
    The AssembledFastener object is derived from the Fastener object.

    .. note:: 
        This object can be accessed by::

            import part
            mdb.models[name].parts[name].engineeringFeatures.fasteners[name]
            import assembly
            mdb.models[name].rootAssembly.engineeringFeatures.fasteners[name]
    """

    #: A Boolean specifying whether the fastener is suppressed or not. The default value is
    #: OFF.
    suppressed: Boolean = OFF

    #: A String specifying the repository key.
    name: str

    #: A :py:class:`~abaqus.Region.Region.Region` object specifying the region of attachment points to which assembled fasteners
    #: are applied.
    region: Region

    #: A String specifying the name of the template model.
    templateModel: str

    #: A :py:class:`~abaqus.Region.Region.Region` object specifying the template model control point set. The set must contain a
    #: single node or vertex.
    controlSet: Region

    #: A sequence of Strings specifying the names of the template model surfaces that are
    #: referenced by tie or coupling constraints.
    templateSurfaces: tuple

    #: A sequence of Strings specifying the names of the master model surfaces that will be
    #: substituted for the template model constraint surfaces.
    assignedSurfaces: tuple

    #: A String specifying the name of the property prefix string. This string will be
    #: prepended to every property name as it is copied to the master model from the template
    #: model.
    propertyPrefix: str

    #: A SymbolicConstant specifying the method used to orient the virtual instances of the
    #: template model at each attachment point. Possible values are NORMALS and CSYS. The
    #: default value is NORMALS.
    orientMethod: SymbolicConstant = NORMALS

    #: None or a DatumCsys object specifying the local coordinate system. If **localCsys** = None,
    #: the global coordinate system is used. When this member is queried, it returns an Int.
    #: The default value is None.This argument applies only when **orientMethod** = CSYS.
    localCsys: int = None

    #: A String specifying the name of the property generation script. The default value is an
    #: empty string.
    scriptName: str = ""

    @abaqus_method_doc
    def __init__(
        self,
        name: str,
        region: Region,
        templateModel: str,
        controlSet: Region,
        templateSurfaces: tuple,
        assignedSurfaces: tuple,
        propertyPrefix: str,
        orientMethod: SymbolicConstant = NORMALS,
        localCsys: int = None,
        scriptName: str = "",
    ):
        """This method creates an AssembledFastener object. Although the constructor is available
        both for parts and for the assembly, AssembledFastener objects are currently supported
        only under the assembly.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].parts[name].engineeringFeatures.AssembledFastener
                mdb.models[name].rootAssembly.engineeringFeatures.AssembledFastener

        Parameters
        ----------
        name
            A String specifying the repository key.
        region
            A :py:class:`~abaqus.Region.Region.Region` object specifying the region of attachment points to which assembled fasteners
            are applied.
        templateModel
            A String specifying the name of the template model.
        controlSet
            A :py:class:`~abaqus.Region.Region.Region` object specifying the template model control point set. The set must contain a
            single node or vertex.
        templateSurfaces
            A sequence of Strings specifying the names of the template model surfaces that are
            referenced by tie or coupling constraints.
        assignedSurfaces
            A sequence of Strings specifying the names of the master model surfaces that will be
            substituted for the template model constraint surfaces.
        propertyPrefix
            A String specifying the name of the property prefix string. This string will be
            prepended to every property name as it is copied to the master model from the template
            model.
        orientMethod
            A SymbolicConstant specifying the method used to orient the virtual instances of the
            template model at each attachment point. Possible values are NORMALS and CSYS. The
            default value is NORMALS.
        localCsys
            None or a DatumCsys object specifying the local coordinate system. If **localCsys** = None,
            the global coordinate system is used. When this member is queried, it returns an Int.
            The default value is None.This argument applies only when **orientMethod** = CSYS.
        scriptName
            A String specifying the name of the property generation script. The default value is an
            empty string.

        Returns
        -------
        AssembledFastener
            An :py:class:`~abaqus.EngineeringFeature.AssembledFastener.AssembledFastener` object.
        """
        super().__init__()

    @abaqus_method_doc
    def setValues(
        self,
        orientMethod: SymbolicConstant = NORMALS,
        localCsys: int = None,
        scriptName: str = "",
    ):
        """This method modifies the AssembledFastener object.

        Parameters
        ----------
        orientMethod
            A SymbolicConstant specifying the method used to orient the virtual instances of the
            template model at each attachment point. Possible values are NORMALS and CSYS. The
            default value is NORMALS.
        localCsys
            None or a DatumCsys object specifying the local coordinate system. If **localCsys** = None,
            the global coordinate system is used. When this member is queried, it returns an Int.
            The default value is None.This argument applies only when **orientMethod** = CSYS.
        scriptName
            A String specifying the name of the property generation script. The default value is an
            empty string.
        """
        ...
