from typing_extensions import Literal

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from ..Model.ModelBase import ModelBase
from ..Part.Part import Part
from ..UtilityAndView.SymbolicConstant import abaqusConstants as C
from ..UtilityAndView.abaqusConstants import (Boolean,
                                              OFF)


@abaqus_class_doc
class PartModel(ModelBase):
    """Abaqus creates a Model object named `Model-1` when a session is started.

    .. note:: 
        This object can be accessed by::

            mdb.models[name]
    """

    @abaqus_method_doc
    def Part(
        self,
        name: str,
        dimensionality: Literal[C.THREE_D, C.TWO_D_PLANAR, C.AXISYMMETRIC],
        type: Literal[
            C.DEFORMABLE_BODY, C.EULERIAN, C.DISCRETE_RIGID_SURFACE, C.ANALYTIC_RIGID_SURFACE
        ],
        twist: Boolean = OFF,
    ):
        """This method creates a Part object and places it in the parts repository.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].Part

        Parameters
        ----------
        name
            A String specifying the repository key.
        dimensionality
            A SymbolicConstant specifying the dimensionality of the part. Possible values are
            THREE_D, TWO_D_PLANAR, and AXISYMMETRIC.
        type
            A SymbolicConstant specifying the type of the part. Possible values are DEFORMABLE_BODY,
            EULERIAN, DISCRETE_RIGID_SURFACE, and ANALYTIC_RIGID_SURFACE.
        twist
            A Boolean specifying whether to include a twist DEGREE OF FREEDOM in the part (only
            available when **dimensionality** = AXISYMMETRIC and **type** = DEFORMABLE_BODY). The default
            value is OFF.

        Returns
        -------
        Part
            A :py:class:`~abaqus.Part.Part.Part` object.
        """
        self.parts[name] = part = Part(name, dimensionality, type, twist)
        return part
