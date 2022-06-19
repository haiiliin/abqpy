import typing

from abaqusConstants import *
from .Fastener import Fastener
from ..Region.Region import Region


class DiscreteFastener(Fastener):
    """The DiscreteFastener object defines a discrete fastener.
    The DiscreteFastener object is derived from the Fastener object.

    Attributes
    ----------
    suppressed: Boolean
        A Boolean specifying whether the fastener is suppressed or not. The default value is
        OFF.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import part
        mdb.models[name].parts[name].engineeringFeatures.fasteners[name]
        import assembly
        mdb.models[name].rootAssembly.engineeringFeatures.fasteners[name]

    The corresponding analysis keywords are:

    - COUPLING

    """

    # A Boolean specifying whether the fastener is suppressed or not. The default value is
    # OFF.
    suppressed: Boolean = OFF

    def __init__(
        self,
        name: str,
        region: Region,
        influenceRadius: typing.Union[SymbolicConstant, float],
        ur1: Boolean = ON,
        ur2: Boolean = ON,
        ur3: Boolean = ON,
        coupling: SymbolicConstant = CONTINUUM,
        weightingMethod: SymbolicConstant = UNIFORM,
        localCsys: int = None,
    ):
        """This method creates a DiscreteFastener object. Although the constructor is available
        both for parts and for the assembly, DiscreteFastener objects are currently supported
        only under the assembly.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            mdb.models[name].parts[name].engineeringFeatures.DiscreteFastener
            mdb.models[name].rootAssembly.engineeringFeatures.DiscreteFastener

        Parameters
        ----------
        name
            A String specifying the repository key.
        region
            A Region object specifying the region to which the fastener is applied.
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
            If **localCsys**=None, couplings are defined in the global coordinate system. When this
            member is queried, it returns an Int. The default value is None.

        Returns
        -------
            A DiscreteFastener object.
        """
        super().__init__()
        pass

    def setValues(
        self,
        ur1: Boolean = ON,
        ur2: Boolean = ON,
        ur3: Boolean = ON,
        coupling: SymbolicConstant = CONTINUUM,
        weightingMethod: SymbolicConstant = UNIFORM,
        localCsys: int = None,
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
            If **localCsys**=None, couplings are defined in the global coordinate system. When this
            member is queried, it returns an Int. The default value is None.
        """
        pass
