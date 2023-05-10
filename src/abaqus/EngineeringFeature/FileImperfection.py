from typing import Sequence

from ..Region.Region import Region
from ..UtilityAndView.abaqusConstants import OFF, Boolean
from .Imperfection import Imperfection


class FileImperfection(Imperfection):
    """The FileImperfection object defines geometric imperfection on an assembly region. The FileImperfection
    object is derived from the Imperfection object.

    .. note::
        This object can be accessed by::

            import assembly
            mdb.models[name].rootAssembly.engineeringFeatures.imperfections[name]

        The corresponding analysis keywords are:

        - IMPERFECTION

        The table data for this object are:

        - Mode Number.
        - Scaling factor for this mode.

    .. versionadded:: 2023
        The ``FileImperfection`` class was added.
    """

    #: A String specifying the repository key.
    name: str

    #: A String specifying the results file from a previous analysis from which the file imperfection is applied.
    file: str

    #: An Int specifying the step number (in the analysis whose file is being used as input to this option) from
    #: which the modal or displacement data are to be read.
    step: int

    #: A sequence of sequences of Integers and Floats specifying linearSuperpositions. The items in the table data
    #: are described below.
    linearSuperpositions: Sequence[Sequence[int]]

    #: A Region object specifying the region to which the file imperfection is applied. By default, the
    #: imperfection will be applied to all nodes in the model.
    region: Region = Region()

    #: An Int specifying the increment number (in the analysis whose file is being used as input to this option)
    #: from which the displacement data are to be read. By default, the data will be read from the last increment
    #: available for the specified step.
    increment: int = -1

    #: A Boolean specifying whether the imperfection is suppressed or not. The default value is OFF.
    suppressed: Boolean = OFF

    def __init__(
        self,
        name: str,
        file: str,
        step: int,
        linearSuperpositions: Sequence[Sequence[int]],
        region: Region = Region(),
        increment: int = -1,
    ):
        """This method creates a FileImperfection object.

        .. note::
            This function can be accessed by::

                mdb.models[name].rootAssembly.engineeringFeatures.FileImperfection

        Parameters
        ----------
        name
            A String specifying the repository key.
        file
            A String specifying the results file from a previous analysis from which the file imperfection is applied.
        step
            An Int specifying the step number (in the analysis whose file is being used as input to this option) from
            which the modal or displacement data are to be read.
        linearSuperpositions
            A sequence of sequences of Integers and Floats specifying linearSuperpositions. The items in the table data
            are described below.
        region
            A Region object specifying the region to which the file imperfection is applied. By default, the
            imperfection will be applied to all nodes in the model.
        increment
            An Int specifying the increment number (in the analysis whose file is being used as input to this option)
            from which the displacement data are to be read. By default, the data will be read from the last increment
            available for the specified step.

        Returns
        -------
        FileImperfection
            A FileImperfection object.
        """
        super().__init__(name)

    def setValues(
        self,
        file: str,
        step: int,
        linearSuperpositions: Sequence[Sequence[int]],
        region: Region = Region(),
        increment: int = -1,
    ):
        """This method modifies the FileImperfection object.

        Parameters
        ----------
        file
            A String specifying the results file from a previous analysis from which the file imperfection is applied.
        step
            An Int specifying the step number (in the analysis whose file is being used as input to this option) from
            which the modal or displacement data are to be read.
        linearSuperpositions
            A sequence of sequences of Integers and Floats specifying linearSuperpositions. The items in the table data
            are described below.
        region
            A Region object specifying the region to which the file imperfection is applied. By default, the
            imperfection will be applied to all nodes in the model.
        increment
            An Int specifying the increment number (in the analysis whose file is being used as input to this option)
            from which the displacement data are to be read. By default, the data will be read from the last increment
            available for the specified step.
        """
        ...
