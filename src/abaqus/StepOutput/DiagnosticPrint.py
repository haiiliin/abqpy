from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from ..UtilityAndView.abaqusConstants import *


@abaqus_class_doc
class DiagnosticPrint:
    """The DiagnosticPrint object is used to request detailed diagnostic output or to disable
    specific diagnostic checks

    .. note:: 
        This object can be accessed by::

            import step
            mdb.models[name].steps[name].diagnosticPrint

        The corresponding analysis keywords are:

        - DIAGNOSTICS
    """

    #: A Boolean specifying a request for a column containing the total kinetic energy. This
    #: argument is valid only for an Abaqus/Explicit analysis. The default value is ON.
    allke: Boolean = ON

    #: A Boolean specifying a request for a column containing the element that has the smallest
    #: stable time increment and a column listing the value. This argument is valid only for an
    #: Abaqus/Explicit analysis. The default value is ON.
    criticalElement: Boolean = ON

    #: A Boolean specifying a request for a column containing the percent change in total mass
    #: of the model as a result of mass scaling. This argument is valid only for an
    #: Abaqus/Explicit analysis. The default value is OFF unless mass scaling is present in the
    #: model.
    dmass: Boolean = OFF

    #: A Boolean specifying a request for a column containing the energy balance of the model.
    #: This argument is valid only for an Abaqus/Explicit analysis. The default value is OFF.
    etotal: Boolean = OFF

    #: A Boolean specifying a request for detailed output of points that are contacting or
    #: separating in interface and gap problems. This argument is valid only for an
    #: Abaqus/Standard analysis. The default value is ON.
    contact: Boolean = ON

    #: A Boolean specifying a request for detailed output of which elements are being removed
    #: or reactivated in the step. This argument is valid only for an Abaqus/Standard analysis.
    #: The default value is OFF.
    modelChange: Boolean = OFF

    #: A Boolean specifying a request for detailed output of element and integration point
    #: numbers for which the plasticity algorithms have failed to converge in the material
    #: routines. This argument is valid only for an Abaqus/Standard analysis. The default value
    #: is OFF.
    plasticity: Boolean = OFF

    #: A Boolean specifying a request for output of equilibrium residuals during the
    #: equilibrium iterations. This argument is valid only for an Abaqus/Standard analysis. The
    #: default value is ON.
    residual: Boolean = ON

    #: An Int specifying the frequency of output, in increments. The default value is 1.
    frequency: int = 1

    #: A Boolean specifying a request for information regarding the actual number of equations
    #: and the wavefront in each iteration. This argument is valid only for an Abaqus/Standard
    #: analysis. The default value is ON.
    

    #: A Boolean specifying a request for a column containing the total mass of the model as a
    #: result of mass scaling. This argument is valid only for an Abaqus/Explicit analysis. The
    #: default value is OFF.
    mass: Boolean = OFF

    @abaqus_method_doc
    def __init__(
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
    ):
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
        DiagnosticPrint
            A :py:class:`~abaqus.StepOutput.DiagnosticPrint.DiagnosticPrint` object.
        """
        ...

    @abaqus_method_doc
    def setValues(self, *args, **kwargs):
        """This method modifies the DiagnosticPrint object."""
        ...
