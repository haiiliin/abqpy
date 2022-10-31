from typing import Optional

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from typing_extensions import Literal

from .GeometricRestriction import GeometricRestriction
from ..Region.Region import Region
from ..UtilityAndView.abaqusConstants import AXIS_1, Boolean, OFF, SymbolicConstant
from ..UtilityAndView.abaqusConstants import abaqusConstants as C


@abaqus_class_doc
class SizingCyclicSymmetry(GeometricRestriction):
    """The SizingCyclicSymmetry object defines a sizing cyclic symmetry geometric restriction.
    The SizingCyclicSymmetry object is derived from the GeometricRestriction object.

    .. note::
        This object can be accessed by::

            import optimization
            mdb.models[name].optimizationTasks[name].geometricRestrictions[name]
    """

    #: A String specifying the geometric restriction repository key.
    name: str

    #: A Region object specifying the region to which the geometric restriction is applied.
    region: Region

    #: A Float specifying the translation distance.
    translation: float

    #: A SymbolicConstant specifying the translation direction defined along an axis positioned
    #: at the **csys** origin. Possible values are AXIS_1, AXIS_2, and AXIS_3. The default value
    #: is AXIS_1.
    axis: SymbolicConstant = AXIS_1

    #: None or a DatumCsys object specifying the local coordinate system. If **csys** = None, the
    #: global coordinate system is used. When this member is queried, it returns an Int. The
    #: default value is None.
    csys: Optional[int] = None

    #: A Boolean specifying whether to ignore frozen areas. The default value is OFF.
    ignoreFrozenArea: Boolean = OFF

    @abaqus_method_doc
    def __init__(
        self,
        name: str,
        region: Region,
        translation: float,
        axis: Literal[C.AXIS_1, C.AXIS_3, C.AXIS_2] = AXIS_1,
        csys: Optional[int] = None,
        ignoreFrozenArea: Boolean = OFF,
    ):
        """This method creates a SizingCyclicSymmetry object.

        .. note::
            This function can be accessed by::

                mdb.models[name].optimizationTasks[name].SizingCyclicSymmetry

        Parameters
        ----------
        name
            A String specifying the geometric restriction repository key.
        region
            A Region object specifying the region to which the geometric restriction is applied.
        translation
            A Float specifying the translation distance.
        axis
            A SymbolicConstant specifying the translation direction defined along an axis positioned
            at the **csys** origin. Possible values are AXIS_1, AXIS_2, and AXIS_3. The default value
            is AXIS_1.
        csys
            None or a DatumCsys object specifying the local coordinate system. If **csys** = None, the
            global coordinate system is used. When this member is queried, it returns an Int. The
            default value is None.
        ignoreFrozenArea
            A Boolean specifying whether to ignore frozen areas. The default value is OFF.

        Returns
        -------
        SizingCyclicSymmetry
            A SizingCyclicSymmetry object.
        """
        super().__init__()

    @abaqus_method_doc
    def setValues(
        self,
        axis: Literal[C.AXIS_1, C.AXIS_3, C.AXIS_2] = AXIS_1,
        csys: Optional[int] = None,
        ignoreFrozenArea: Boolean = OFF,
    ):
        """This method modifies the SizingCyclicSymmetry object.

        Parameters
        ----------
        axis
            A SymbolicConstant specifying the translation direction defined along an axis positioned
            at the **csys** origin. Possible values are AXIS_1, AXIS_2, and AXIS_3. The default value
            is AXIS_1.
        csys
            None or a DatumCsys object specifying the local coordinate system. If **csys** = None, the
            global coordinate system is used. When this member is queried, it returns an Int. The
            default value is None.
        ignoreFrozenArea
            A Boolean specifying whether to ignore frozen areas. The default value is OFF.
        """
        ...
