from typing import Union, Optional

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from .Fastener import Fastener
from ..Region.Region import Region
from ..UtilityAndView.abaqusConstants import Boolean, CONTINUUM, OFF, ON, SymbolicConstant, UNIFORM


@abaqus_class_doc
class DiscreteFastener(Fastener):
    """The DiscreteFastener object defines a discrete fastener.
    The DiscreteFastener object is derived from the Fastener object.

    .. note:: 
        This object can be accessed by::

            import part
            mdb.models[name].parts[name].engineeringFeatures.fasteners[name]
            import assembly
            mdb.models[name].rootAssembly.engineeringFeatures.fasteners[name]

        The corresponding analysis keywords are:

        - COUPLING
    """

    #: A Boolean specifying whether the fastener is suppressed or not. The default value is
    #: OFF.
    suppressed: Boolean = OFF

    #: A String specifying the repository key.
    name: str

    #: A :py:class:`~abaqus.Region.Region.Region` object specifying the region to which the fastener is applied.
    region: Region

    #: The SymbolicConstant WHOLE_SURFACE or a Float specifying the coupling influence radius.
    influenceRadius: Union[SymbolicConstant, float]

    #: A Boolean specifying whether to constrain rotational displacement component about the
    #: 1-direction. The default value is ON.
    ur1: Boolean = ON

    #: A Boolean specifying whether to constrain rotational displacement component about the
    #: 2-direction. The default value is ON.
    ur2: Boolean = ON

    #: A Boolean specifying whether to constrain rotational displacement component about the
    #: 3-direction. The default value is ON.
    ur3: Boolean = ON

    #: A SymbolicConstant specifying the coupling method used to couple the displacement and
    #: rotation of each attachment point to the average motion of the surface nodes within the
    #: radius of influence from the fastening point. Possible values are CONTINUUM and
    #: STRUCTURAL. The default value is CONTINUUM.
    coupling: SymbolicConstant = CONTINUUM

    #: A SymbolicConstant specifying the weighting scheme to be used to weight the contribution
    #: of the displacements of the surface nodes within the radius of influence to the motion
    #: of the fastening point. UNIFORM, LINEAR, QUADRATIC, and CUBIC indicate uniform, linear
    #: decreasing, quadratic polynomial decreasing, and cubic polynomial monotonic decreasing
    #: weight distributions. Possible values are UNIFORM, LINEAR, QUADRATIC, and CUBIC. The
    #: default value is UNIFORM.
    weightingMethod: SymbolicConstant = UNIFORM

    #: None or a DatumCsys object specifying the local coordinate system of fastener couplings.
    #: If **localCsys** = None, couplings are defined in the global coordinate system. When this
    #: member is queried, it returns an Int. The default value is None.
    localCsys: Optional[int] = None

    @abaqus_method_doc
    def __init__(
        self,
        name: str,
        region: Region,
        influenceRadius: Union[SymbolicConstant, float],
        ur1: Boolean = ON,
        ur2: Boolean = ON,
        ur3: Boolean = ON,
        coupling: SymbolicConstant = CONTINUUM,
        weightingMethod: SymbolicConstant = UNIFORM,
        localCsys: Optional[int] = None,
    ):
        """This method creates a DiscreteFastener object. Although the constructor is available
        both for parts and for the assembly, DiscreteFastener objects are currently supported
        only under the assembly.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].parts[name].engineeringFeatures.DiscreteFastener
                mdb.models[name].rootAssembly.engineeringFeatures.DiscreteFastener

        Parameters
        ----------
        name
            A String specifying the repository key.
        region
            A :py:class:`~abaqus.Region.Region.Region` object specifying the region to which the fastener is applied.
        influenceRadius
            The SymbolicConstant WHOLE_SURFACE or a Float specifying the coupling influence radius.
        ur1
            A Boolean specifying whether to constrain rotational displacement component about the
            1-direction. The default value is ON.
        ur2
            A Boolean specifying whether to constrain rotational displacement component about the
            2-direction. The default value is ON.
        ur3
            A Boolean specifying whether to constrain rotational displacement component about the
            3-direction. The default value is ON.
        coupling
            A SymbolicConstant specifying the coupling method used to couple the displacement and
            rotation of each attachment point to the average motion of the surface nodes within the
            radius of influence from the fastening point. Possible values are CONTINUUM and
            STRUCTURAL. The default value is CONTINUUM.
        weightingMethod
            A SymbolicConstant specifying the weighting scheme to be used to weight the contribution
            of the displacements of the surface nodes within the radius of influence to the motion
            of the fastening point. UNIFORM, LINEAR, QUADRATIC, and CUBIC indicate uniform, linear
            decreasing, quadratic polynomial decreasing, and cubic polynomial monotonic decreasing
            weight distributions. Possible values are UNIFORM, LINEAR, QUADRATIC, and CUBIC. The
            default value is UNIFORM.
        localCsys
            None or a DatumCsys object specifying the local coordinate system of fastener couplings.
            If **localCsys** = None, couplings are defined in the global coordinate system. When this
            member is queried, it returns an Int. The default value is None.

        Returns
        -------
        DiscreteFastener
            A :py:class:`~abaqus.EngineeringFeature.DiscreteFastener.DiscreteFastener` object.
        """
        super().__init__()

    @abaqus_method_doc
    def setValues(
        self,
        ur1: Boolean = ON,
        ur2: Boolean = ON,
        ur3: Boolean = ON,
        coupling: SymbolicConstant = CONTINUUM,
        weightingMethod: SymbolicConstant = UNIFORM,
        localCsys: Optional[int] = None,
    ):
        """This method modifies the DiscreteFastener object.

        Parameters
        ----------
        ur1
            A Boolean specifying whether to constrain rotational displacement component about the
            1-direction. The default value is ON.
        ur2
            A Boolean specifying whether to constrain rotational displacement component about the
            2-direction. The default value is ON.
        ur3
            A Boolean specifying whether to constrain rotational displacement component about the
            3-direction. The default value is ON.
        coupling
            A SymbolicConstant specifying the coupling method used to couple the displacement and
            rotation of each attachment point to the average motion of the surface nodes within the
            radius of influence from the fastening point. Possible values are CONTINUUM and
            STRUCTURAL. The default value is CONTINUUM.
        weightingMethod
            A SymbolicConstant specifying the weighting scheme to be used to weight the contribution
            of the displacements of the surface nodes within the radius of influence to the motion
            of the fastening point. UNIFORM, LINEAR, QUADRATIC, and CUBIC indicate uniform, linear
            decreasing, quadratic polynomial decreasing, and cubic polynomial monotonic decreasing
            weight distributions. Possible values are UNIFORM, LINEAR, QUADRATIC, and CUBIC. The
            default value is UNIFORM.
        localCsys
            None or a DatumCsys object specifying the local coordinate system of fastener couplings.
            If **localCsys** = None, couplings are defined in the global coordinate system. When this
            member is queried, it returns an Int. The default value is None.
        """
        ...
