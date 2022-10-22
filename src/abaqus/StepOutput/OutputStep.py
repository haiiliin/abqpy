from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from .DiagnosticPrint import DiagnosticPrint
from .Monitor import Monitor
from .Restart import Restart
from ..Step.StepBase import StepBase
from ..UtilityAndView.abaqusConstants import Boolean, OFF, ON, SymbolicConstant


@abaqus_class_doc
class OutputStep(StepBase):
    """The Step object stores the parameters that determine the context of the step. The Step
    object is the abstract base type for other Step objects. The Step object has no explicit
    constructor. The methods and members of the Step object are common to all objects
    derived from the Step.

    .. note:: 
        This object can be accessed by::

            import step
            mdb.models[name].steps[name]
    """

    @abaqus_method_doc
    def DiagnosticPrint(
        self,
        allke: Boolean = ON,
        criticalElement: Boolean = ON,
        dmass: Boolean = OFF,
        etotal: Boolean = OFF,
        contact: Boolean = ON,
        modelChange: Boolean = OFF,
        plasticity: Boolean = OFF,
        residual: Boolean = ON,
        frequency: int = 1,
        solve: Boolean = ON,
        mass: Boolean = OFF,
    ) -> DiagnosticPrint:
        """This method creates a DiagnosticPrint object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].steps[name].DiagnosticPrint

        Parameters
        ----------
        allke
            A Boolean specifying a request for a column containing the total kinetic energy. This
            argument is valid only for an Abaqus/Explicit analysis. The default value is ON.
        criticalElement
            A Boolean specifying a request for a column containing the element that has the smallest
            stable time increment and a column listing the value. This argument is valid only for an
            Abaqus/Explicit analysis. The default value is ON.
        dmass
            A Boolean specifying a request for a column containing the percent change in total mass
            of the model as a result of mass scaling. This argument is valid only for an
            Abaqus/Explicit analysis. The default value is OFF unless mass scaling is present in the
            model.
        etotal
            A Boolean specifying a request for a column containing the energy balance of the model.
            This argument is valid only for an Abaqus/Explicit analysis. The default value is OFF.
        contact
            A Boolean specifying a request for detailed output of points that are contacting or
            separating in interface and gap problems. This argument is valid only for an
            Abaqus/Standard analysis. The default value is ON.
        modelChange
            A Boolean specifying a request for detailed output of which elements are being removed
            or reactivated in the step. This argument is valid only for an Abaqus/Standard analysis.
            The default value is OFF.
        plasticity
            A Boolean specifying a request for detailed output of element and integration point
            numbers for which the plasticity algorithms have failed to converge in the material
            routines. This argument is valid only for an Abaqus/Standard analysis. The default value
            is OFF.
        residual
            A Boolean specifying a request for output of equilibrium residuals during the
            equilibrium iterations. This argument is valid only for an Abaqus/Standard analysis. The
            default value is ON.
        frequency
            An Int specifying the frequency of output, in increments. The default value is 1.
        solve
            A Boolean specifying a request for information regarding the actual number of equations
            and the wavefront in each iteration. This argument is valid only for an Abaqus/Standard
            analysis. The default value is ON.
        mass
            A Boolean specifying a request for a column containing the total mass of the model as a
            result of mass scaling. This argument is valid only for an Abaqus/Explicit analysis. The
            default value is OFF.

        Returns
        -------
        diagnosticPrint: DiagnosticPrint
            A :py:class:`~abaqus.StepOutput.DiagnosticPrint.DiagnosticPrint` object
        """
        self.diagnosticPrint = diagnosticPrint = DiagnosticPrint(
            allke,
            criticalElement,
            dmass,
            etotal,
            contact,
            modelChange,
            plasticity,
            residual,
            frequency,
            solve,
            mass,
        )
        return diagnosticPrint

    @abaqus_method_doc
    def Monitor(self, node: str, dof: SymbolicConstant, frequency: int) -> Monitor:
        """This method creates a request for a degree of freedom to be monitored in a general or
        modal procedure.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].steps[name].Monitor

        Parameters
        ----------
        node
            A String specifying the name of the region to be monitored.
        dof
            A SymbolicConstant specifying the degree of freedom to be monitored at the node.
            Possible values are:
            
            - U1
            - U2
            - U3
            - UR1
            - UR2
            - UR3
            - WARP
            - FLUID_PRESSURE
            - ELECTRICAL_POTENTIAL
            - NT11
            - NT30
            - NN11
            - NN30
            
            The NT identifiers are not available for mass diffusion. The NN identifiers are
            available only for mass diffusion.
        frequency
            An Int specifying the output frequency in increments. This argument is valid only for an
            Abaqus/Standard analysis.

        Returns
        -------
        monitor: Monitor
            A :py:class:`~abaqus.StepOutput.Monitor.Monitor` object
        """
        self.monitor = monitor = Monitor(node, dof, frequency)
        return monitor

    @abaqus_method_doc
    def Restart(
        self,
        numberIntervals: int = 0,
        timeMarks: Boolean = OFF,
        overlay: Boolean = OFF,
        frequency: int = 0,
    ) -> Restart:
        """This method creates a restart request.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].steps[name].Restart

        Parameters
        ----------
        numberIntervals
            An Int specifying the number of intervals during the step at which restart information
            will be written. The default value is 0. The default value is 1.
        timeMarks
            A Boolean specifying whether to use exact time marks for writing during an analysis. The
            default value is OFF. The default value is OFF.
        overlay
            A Boolean specifying that only one increment per step should be retained on the restart
            file, thus minimizing the size of the restart file. The default value is OFF. The
            default value is ON.
        frequency
            An Int specifying the increments at which restart information will be written. The
            default value is 0. The default value is 0.This argument applies only to Abaqus/Standard
            analyses.

        Returns
        -------
        restart: Restart
            A :py:class:`~abaqus.StepOutput.Restart.Restart` object

        Raises
        ------
        RangeError
        """
        self.restart = restart = Restart(numberIntervals, timeMarks, overlay, frequency)
        return restart
