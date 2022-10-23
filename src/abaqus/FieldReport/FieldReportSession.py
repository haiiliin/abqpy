from typing import Optional

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from typing_extensions import Literal

from ..DisplayGroup.DisplayGroup import DisplayGroup
from ..Odb.Odb import Odb
from ..Session.SessionBase import SessionBase
from ..UtilityAndView.abaqusConstants import Boolean, SPECIFY
from ..UtilityAndView.abaqusConstants import abaqusConstants as C


@abaqus_class_doc
class FieldReportSession(SessionBase):
    @abaqus_method_doc
    def writeFieldReport(
        self,
        filename: str,
        append: Boolean,
        sortItem: str,
        odb: Odb,
        step: int,
        frame: int,
        outputPosition: Literal[
            C.ELEMENT_NODAL,
            C.ELEMENT_FACE,
            C.WHOLE_ELEMENT,
            C.NODAL,
            C.INTEGRATION_POINT,
            C.ELEMENT_CENTROID,
            C.WHOLE_MODEL,
            C.GENERAL_PARTICLE,
            C.WHOLE_PART_INSTANCE,
            C.WHOLE_REGION,
        ],
        displayGroup: DisplayGroup,
        variable: Literal[
            C.ELEMENT_FACE,
            C.ELEMENT_NODAL,
            C.SPOS,
            C.WHOLE_ELEMENT,
            C.NODAL,
            C.INTEGRATION_POINT,
            C.ELEMENT_CENTROID,
            C.WHOLE_MODEL,
            C.WHOLE_REGION,
            C.GENERAL_PARTICLE,
            C.WHOLE_PART_INSTANCE,
        ],
        numericForm: Optional[
            Literal[C.COMPLEX_PHASE, C.COMPLEX_MAG_AT_ANGLE, C.REAL, C.IMAGINARY, C.COMPLEX_MAGNITUDE]
        ] = None,
        complexAngle: Optional[float] = None,
        stepFrame: Literal[C.ALL, C.SPECIFY] = SPECIFY,
    ):
        """This method writes a FieldOutput object to a user-defined ASCII file.

        .. note::
            This function can be accessed by::

                session.writeFieldReport

        Parameters
        ----------
        filename
            A String specifying the name of the file to which field output will be written.
        append
            A Boolean specifying whether to append the field output to an existing file. The default
            value is ON.
        sortItem
            A String specifying the item by which to sort the tabular values.
        odb
            An :py:class:`~abaqus.Odb.Odb.Odb` object from which to obtain field output values.
        step
            An Int (or stepIndex) specifying the step from which to obtain field output values.
            Possible values are 0 ≤ **step** ≤ (*numSteps* − 1).
        frame
            An Int (or frameIndex) specifying the frame from which to obtain field output values.
            Possible values are 0 ≤ **frame** ≤ (*numFramesInStep* − 1).
        outputPosition
            A SymbolicConstant specifying the position from which to obtain data. Possible values
            are NODAL, INTEGRATION_POINT, ELEMENT_FACE, ELEMENT_NODAL, ELEMENT_CENTROID,
            WHOLE_ELEMENT, WHOLE_REGION, WHOLE_PART_INSTANCE, WHOLE_MODEL, and GENERAL_PARTICLE.
        displayGroup
            A :py:class:`~abaqus.DisplayGroup.DisplayGroup.DisplayGroup` object specifying the subset of the model for which to obtain data.
        variable
            A sequence of variable description sequences specifying one or more field output
            variables for which to obtain data. Each variable description sequence contains the
            following elements:

            - **element0**: A String specifying the name of the variable.
            - **element1**: A SymbolicConstant specifying the output position at which to report data.
              Possible values are ELEMENT_CENTROID, ELEMENT_FACE, ELEMENT_NODAL, GENERAL_PARTICLE,
              INTEGRATION_POINT, NODAL, WHOLE_ELEMENT, WHOLE_MODEL, WHOLE_PART_INSTANCE, and
              WHOLE_REGION.
            - **element2**: A Sequence of tuples each consisting of a SymbolicConstant specifying the
              refinement (COMPONENT or INVARIANT), followed by a String specifying the name of a
              component or invariant for which to obtain values.
              If this element is omitted, data are written for all components and invariants (if
              applicable). This element is required if **element3** (the following element in the tuple)
              is included.
            - **element3 (if applicable)**: A Dictionary with a String key and a String value
              specifying a single section point at which to report data. The key specifies a region in
              the model; the corresponding value specifies a section point within that region. For
              example::

                  {'shell < MAT > < 7 section points >': 'SPOS (fraction = 1.0)'}

              If this element is omitted, data are written for all section points (if applicable).
              If this element is omitted, data are written for all section points (if applicable).
        numericForm
            A SymbolicConstant specifying the numeric form in which to display results that contain
            complex numbers. Possible values are COMPLEX_MAGNITUDE, COMPLEX_PHASE, REAL, IMAGINARY,
            and COMPLEX_MAG_AT_ANGLE. The initial value is COMPLEX_MAGNITUDE.
        complexAngle
            A Float specifying the angle (in degrees) at which to display results that contain
            complex numbers when **numericForm** = COMPLEX_MAG_AT_ANGLE. The initial value is 0.
        stepFrame
            A SymbolicConstant indicating whether to obtain the values from the specified frame or
            from all active frames. Possible values are SPECIFY and ALL. The default value is
            SPECIFY.
        """
        ...

    @abaqus_method_doc
    def writeFreeBodyReport(
        self,
        fileName: str,
        append: Boolean,
        step: Optional[int] = None,
        frame: Optional[int] = None,
        stepFrame: Literal[C.ALL, C.SPECIFY] = SPECIFY,
        odb: Optional[Odb] = None,
    ):
        """This method writes a FreeBody object to a user-defined ASCII file.

        .. note::
            This function can be accessed by::

                session.writeFreeBodyReport

        Parameters
        ----------
        fileName
            A String specifying the name of the file to which the free body output will be written.
        append
            A Boolean specifying whether to append the free body output to an existing file. The
            default value is ON.
        step
            An Int identifying the step from which to obtain values. The default value is the
            current step.
        frame
            An Int identifying the frame from which to obtain values. The default value is the
            current frame.
        stepFrame
            A SymbolicConstant indicating whether to obtain the values from the specified frame or
            from all active frames. Possible values are SPECIFY and ALL. The default value is
            SPECIFY.
        odb
            An :py:class:`~abaqus.Odb.Odb.Odb` object specifying the output database from which data will be read.

        Returns
        -------

        Raises
        ------
        """
        ...
