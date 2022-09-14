from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from .LoadCase import LoadCase
from ..Step.StepBase import StepBase
from ..UtilityAndView.abaqusConstants import *


@abaqus_class_doc
class LoadStep(StepBase):
    @abaqus_method_doc
    def LoadCase(
        self,
        name: str,
        boundaryConditions: tuple = (),
        loads: tuple = (),
        includeActiveBaseStateBC: Boolean = ON,
    ) -> LoadCase:
        """This method creates a load case in a step.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].steps[name].LoadCase

        Parameters
        ----------
        name
            A String specifying the name of the object.
        boundaryConditions
            A sequence of (String, Float) sequences specifying the name of a BoundaryCondition
            followed by a nonzero Float scaling factor. The default value is an empty sequence.
        loads
            A sequence of (String, Float) sequences specifying the name of a Load followed by a
            nonzero Float specifying a scale factor. The default value is an empty sequence.
        includeActiveBaseStateBC
            A Boolean specifying whether to include all active boundary conditions propagated or
            modified from the base state. The default value is ON.

        Returns
        -------
        LoadCase
            A :py:class:`~abaqus.Load.LoadCase.LoadCase` object.

        Raises
        ------
        RangeError
        """
        self.loadCases[name] = loadCase = LoadCase(
            name, boundaryConditions, loads, includeActiveBaseStateBC
        )
        return loadCase
