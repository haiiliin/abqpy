from abqpy.decorators import abaqus_function_doc
from ..DisplayGroup.DisplayGroup import DisplayGroup
from ..Odb.Odb import Odb
from ..UtilityAndView.abaqusConstants import *

"""This command writes a field output report to a file. 

"""


@abaqus_function_doc
def writeFieldReport(
    filename: str,
    append: Boolean,
    sortItem: str,
    odb: Odb,
    step: int,
    frame: int,
    outputPosition: SymbolicConstant,
    displayGroup: DisplayGroup,
    variable: SymbolicConstant,
    numericForm: SymbolicConstant = None,
    complexAngle: float = None,
):
    """This function writes a FieldOutput object to a user-defined ASCII file.

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
    """
    ...
