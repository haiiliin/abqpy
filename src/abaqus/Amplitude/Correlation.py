from typing import Optional
from abqpy.decorators import abaqus_class_doc
from .Amplitude import Amplitude
from ..UtilityAndView.abaqusConstants import *


@abaqus_class_doc
class Correlation(Amplitude):
    """A Correlation is an object used to define the cross-correlation as part of the
    definition of random loading.
    The Correlation object is derived from the Amplitude object.

    .. note:: 
        This object can be accessed by::

            import load
            mdb.models[name].boundaryConditions[name].correlation[i]
    """

    #: A String specifying the repository key.
    name: str = ""

    #: A SymbolicConstant specifying the approach used in the correlation data representation.
    #: Possible values are CORRELATED, MOVING_NOISE, UNCORRELATED, and USER. The default value
    #: is CORRELATED.
    approach: SymbolicConstant = CORRELATED

    #: A tuple of tuples of Floats specifying the real and imaginary part of the scaling
    #: factor. If **approach** = MOVING_NOISE, then **data** represents the noise velocity components
    #: 1, 2, and 3.
    data: Optional[float] = None

    #: A SymbolicConstant specifying the time span of the amplitude. Possible values are STEP
    #: and TOTAL. The default value is STEP.
    timeSpan: SymbolicConstant = STEP
