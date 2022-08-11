from abaqusConstants import *
from .DesignResponse import DesignResponse


class CombinedTermDesignResponse(DesignResponse):
    """The CombinedTermDesignResponse object defines a combined-term design response.
    The CombinedTermDesignResponse object is derived from the DesignResponse object.

    .. note:: 
        This object can be accessed by:

        .. code-block:: python

            import optimization
            mdb.models[name].optimizationTasks[name].designResponses[name]
    """

    #: A String specifying the design response repository key.
    name: str

    #: A sequence of Strings specifying the names of the design responses to combine.
    terms: tuple

    #: None or a sequence of Floats specifying the maximum radius of influence used when
    #: **method** is FILTER. The default value is None.
    filterMaxRadius: str = None

    #: A Float specifying the exponent used when **method** is FILTER. The default value is 1.0.
    filterExponent: float = 1

    #: A Float specifying the reduction of the radius depending on surface bending, used when
    #: **method** is FILTER. The default value is 0.2.
    filterRadiusReduction: float = 0

    #: None or a sequence of Floats specifying the upper bound of the vector value used when
    #: **method** is CUT_OFF. All values greater than the **highCutOff** are set to the
    #: **highCutOff** value. The default value is None.
    highCutOff: str = None

    #: A Float specifying the lower bound of the vector value used when **method** is CUT_OFF.
    #: All values less than the **lowCutOff** are treated as 0. The default value is 0.0.
    lowCutOff: float = 0

    #: A SymbolicConstant specifying the method used to combine selected design responses.
    #: Possible values are:
    

    #: - ABSOLUTE_DIFFERENCE
    #: - ABSOLUTE_VALUE
    #: - ADD
    #: - COSINE
    #: - CUT_OFF
    #: - DELTA_OVER_1_ITERATION
    #: - DELTA_OVER_2_ITERATIONS
    #: - DELTA_OVER_3_ITERATIONS
    #: - DELTA_OVER_4_ITERATIONS
    #: - DELTA_OVER_5_ITERATIONS
    #: - DELTA_OVER_6_ITERATIONS
    #: - DIVIDE
    #: - EXPONENTIAL
    #: - FILTER
    #: - INTEGER
    #: - LOG
    #: - MAXIMUM
    #: - MINIMUM
    #: - MULTIPLY
    #: - NATURAL_LOG
    #: - NEAREST_INTEGER
    #: - NORM
    #: - NORM_FIRST
    #: - NTH_POWER
    #: - NTH_ROOT
    #: - SIGN
    #: - SINE
    #: - SQUARE_ROOT
    #: - SUBTRACT
    #: - TANGENT
    #: - WEIGHTED_ADD
    #: 
    #: The default value is ADD.
    method: SymbolicConstant = ADD

    #: A sequence of Floats specifying the weights to apply to the list of design responses
    #: used when **method** is WEIGHTED_ADD. The default value is an empty sequence.
    weights: tuple = ()

    def __init__(
        self,
        name: str,
        terms: tuple,
        filterMaxRadius: str = None,
        filterExponent: float = 1,
        filterRadiusReduction: float = 0,
        highCutOff: str = None,
        lowCutOff: float = 0,
        method: SymbolicConstant = ADD,
        weights: tuple = (),
    ):
        """This method creates a CombinedTermDesignResponse object.

        .. note:: 
            This function can be accessed by:

            .. code-block:: python

                mdb.models[name].optimizationTasks[name].CombinedTermDesignResponse

        Parameters
        ----------
        name
            A String specifying the design response repository key.
        terms
            A sequence of Strings specifying the names of the design responses to combine.
        filterMaxRadius
            None or a sequence of Floats specifying the maximum radius of influence used when
            **method** is FILTER. The default value is None.
        filterExponent
            A Float specifying the exponent used when **method** is FILTER. The default value is 1.0.
        filterRadiusReduction
            A Float specifying the reduction of the radius depending on surface bending, used when
            **method** is FILTER. The default value is 0.2.
        highCutOff
            None or a sequence of Floats specifying the upper bound of the vector value used when
            **method** is CUT_OFF. All values greater than the **highCutOff** are set to the
            **highCutOff** value. The default value is None.
        lowCutOff
            A Float specifying the lower bound of the vector value used when **method** is CUT_OFF.
            All values less than the **lowCutOff** are treated as 0. The default value is 0.0.
        method
            A SymbolicConstant specifying the method used to combine selected design responses.
            Possible values are:

            - ABSOLUTE_DIFFERENCE
            - ABSOLUTE_VALUE
            - ADD
            - COSINE
            - CUT_OFF
            - DELTA_OVER_1_ITERATION
            - DELTA_OVER_2_ITERATIONS
            - DELTA_OVER_3_ITERATIONS
            - DELTA_OVER_4_ITERATIONS
            - DELTA_OVER_5_ITERATIONS
            - DELTA_OVER_6_ITERATIONS
            - DIVIDE
            - EXPONENTIAL
            - FILTER
            - INTEGER
            - LOG
            - MAXIMUM
            - MINIMUM
            - MULTIPLY
            - NATURAL_LOG
            - NEAREST_INTEGER
            - NORM
            - NORM_FIRST
            - NTH_POWER
            - NTH_ROOT
            - SIGN
            - SINE
            - SQUARE_ROOT
            - SUBTRACT
            - TANGENT
            - WEIGHTED_ADD
            
            The default value is ADD.
        weights
            A sequence of Floats specifying the weights to apply to the list of design responses
            used when **method** is WEIGHTED_ADD. The default value is an empty sequence.

        Returns
        -------
        CombinedTermDesignResponse
            A :py:class:`~abaqus.Optimization.CombinedTermDesignResponse.CombinedTermDesignResponse` object.
        """
        super().__init__()

    def setValues(
        self,
        filterMaxRadius: str = None,
        filterExponent: float = 1,
        filterRadiusReduction: float = 0,
        highCutOff: str = None,
        lowCutOff: float = 0,
        method: SymbolicConstant = ADD,
        weights: tuple = (),
    ):
        """This method modifies the CombinedTermDesignResponse object.

        Parameters
        ----------
        filterMaxRadius
            None or a sequence of Floats specifying the maximum radius of influence used when
            **method** is FILTER. The default value is None.
        filterExponent
            A Float specifying the exponent used when **method** is FILTER. The default value is 1.0.
        filterRadiusReduction
            A Float specifying the reduction of the radius depending on surface bending, used when
            **method** is FILTER. The default value is 0.2.
        highCutOff
            None or a sequence of Floats specifying the upper bound of the vector value used when
            **method** is CUT_OFF. All values greater than the **highCutOff** are set to the
            **highCutOff** value. The default value is None.
        lowCutOff
            A Float specifying the lower bound of the vector value used when **method** is CUT_OFF.
            All values less than the **lowCutOff** are treated as 0. The default value is 0.0.
        method
            A SymbolicConstant specifying the method used to combine selected design responses.
            Possible values are:

            - ABSOLUTE_DIFFERENCE
            - ABSOLUTE_VALUE
            - ADD
            - COSINE
            - CUT_OFF
            - DELTA_OVER_1_ITERATION
            - DELTA_OVER_2_ITERATIONS
            - DELTA_OVER_3_ITERATIONS
            - DELTA_OVER_4_ITERATIONS
            - DELTA_OVER_5_ITERATIONS
            - DELTA_OVER_6_ITERATIONS
            - DIVIDE
            - EXPONENTIAL
            - FILTER
            - INTEGER
            - LOG
            - MAXIMUM
            - MINIMUM
            - MULTIPLY
            - NATURAL_LOG
            - NEAREST_INTEGER
            - NORM
            - NORM_FIRST
            - NTH_POWER
            - NTH_ROOT
            - SIGN
            - SINE
            - SQUARE_ROOT
            - SUBTRACT
            - TANGENT
            - WEIGHTED_ADD
            
            The default value is ADD.
        weights
            A sequence of Floats specifying the weights to apply to the list of design responses
            used when **method** is WEIGHTED_ADD. The default value is an empty sequence.
        """
        ...
