from typing_extensions import Literal

from ..UtilityAndView.abaqusConstants import OFF, Boolean, R
from ..UtilityAndView.abaqusConstants import abaqusConstants as C
from .Imperfection import Imperfection


class InputImperfection(Imperfection):
    """The InputImperfection object defines geometric imperfection on an assembly region. The InputImperfection
    object is derived from the Imperfection object.

    .. note::
        This object can be accessed by::

            import assembly
            mdb.models[name].rootAssembly.engineeringFeatures.imperfections[name]

        The corresponding analysis keywords are:

        - IMPERFECTION

    .. versionadded:: 2023
        The ``InputImperfection`` class was added.
    """

    #: A String specifying the repository key.
    name: str

    #: A String specifying the name of the alternate input file containing the imperfection data.
    file: str

    #: A SymbolicConstant specifying the coordinate system. The imperfection values in the alternate input file
    #: being used as input to this option would be treated as perturbation values of respective coordinates.
    #: Possible values are R, C and S. The default value is R.
    system: Literal[C.R, C.C, C.S] = R

    #: A Boolean specifying whether the imperfection is suppressed or not. The default value is OFF.
    suppressed: Boolean = OFF

    def __init__(
        self,
        name: str,
        file: str,
        system: Literal[C.R, C.C, C.S] = R,
    ):
        """This method creates a InputImperfection object.

        .. note::
            This function can be accessed by::

                mdb.models[name].rootAssembly.engineeringFeatures.InputImperfection

        Parameters
        ----------
        name
            A String specifying the repository key.
        file
            A String specifying the name of the alternate input file containing the imperfection data.
        system
            A SymbolicConstant specifying the coordinate system. The imperfection values in the alternate input file
            being used as input to this option would be treated as perturbation values of respective coordinates.
            Possible values are R, C and S. The default value is R.

        Returns
        -------
        InputImperfection
            A InputImperfection object.
        """
        super().__init__(name)

    def setValues(
        self,
        file: str,
        system: Literal[C.R, C.C, C.S] = R,
    ):
        """This method modifies the InputImperfection object.

        Parameters
        ----------
        file
            A String specifying the name of the alternate input file containing the imperfection data.
        system
            A SymbolicConstant specifying the coordinate system. The imperfection values in the alternate input file
            being used as input to this option would be treated as perturbation values of respective coordinates.
            Possible values are R, C and S. The default value is R.
        """
        ...
