from typing import Sequence, Union

from typing_extensions import Literal

from ..UtilityAndView.abaqusConstants import OFF, Boolean, R
from ..UtilityAndView.abaqusConstants import abaqusConstants as C
from .Imperfection import Imperfection


class DataImperfection(Imperfection):
    """The DataImperfection object defines geometric imperfection on an assembly region. The DataImperfection
    object is derived from the Imperfection object.

    .. note::
        This object can be accessed by::

            import assembly
            mdb.models[name].rootAssembly.engineeringFeatures.imperfections[name]

        The corresponding analysis keywords are:

        - IMPERFECTION

        The table data for this object are:

        - Node number.
        - Component of imperfection in the first coordinate direction.
        - Component of imperfection in the second coordinate direction.
        - Component of imperfection in the third coordinate direction.

    .. versionadded:: 2023
        The ``DataImperfection`` class was added.
    """

    #: A String specifying the repository key.
    name: str

    #: A sequence of sequences of Ints and Floats specifying the imperfection components at a given node. The
    #: items in the table data are described below.
    imperfectionTable: Sequence[Sequence[Union[int, float]]]

    #: A SymbolicConstant specifying the coordinate system. The imperfection values in the data lines would be
    #: treated as perturbation values of the respective coordinates. Possible values are R, C, and S. The default
    #: value is R.
    system: Literal[C.R, C.C, C.S] = R

    #: A Boolean specifying whether the imperfection is suppressed or not. The default value is OFF.
    suppressed: Boolean = OFF

    def __init__(
        self,
        name: str,
        imperfectionTable: Sequence[Sequence[Union[int, float]]],
        system: Literal[C.R, C.C, C.S] = R,
    ):
        """This method creates a DataImperfection object.

        .. note::
            This function can be accessed by::

                mdb.models[name].rootAssembly.engineeringFeatures.DataImperfection

        Parameters
        ----------
        name
            A String specifying the repository key.
        imperfectionTable: Sequence[Sequence[Union[int, float]]]
            A sequence of sequences of Ints and Floats specifying the imperfection components at a given node. The
            items in the table data are described below.
        system
            A SymbolicConstant specifying the coordinate system. The imperfection values in the data lines would be
            treated as perturbation values of the respective coordinates. Possible values are R, C, and S. The default
            value is R.

        Returns
        -------
        DataImperfection
            A DataImperfection object.
        """
        super().__init__(name)

    def setValues(
        self,
        imperfectionTable: Sequence[Sequence[Union[int, float]]],
        system: Literal[C.R, C.C, C.S] = R,
    ):
        """This method modifies the DataImperfection object.

        Parameters
        ----------
        imperfectionTable: Sequence[Sequence[Union[int, float]]]
            A sequence of sequences of Ints and Floats specifying the imperfection components at a given node. The
            items in the table data are described below.
        system
            A SymbolicConstant specifying the coordinate system. The imperfection values in the data lines would be
            treated as perturbation values of the respective coordinates. Possible values are R, C, and S. The default
            value is R.
        """
        ...
