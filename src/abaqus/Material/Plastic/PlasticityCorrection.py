from typing import Sequence

from typing_extensions import Literal

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from ...UtilityAndView.abaqusConstants import OFF, Boolean
from ...UtilityAndView.abaqusConstants import abaqusConstants as C


@abaqus_class_doc
class PlasticityCorrection:
    r"""The PlasticityCorrection object specifies the elastic-plastic response of the material with linear
    elasticity.

    .. note::
        This object can be accessed by::

            import material
            mdb.models[name].materials[name].plasticityCorrection

        The table data for this object are:

        - If type=RAMBERG_OSGOOD, the table specifies the following:

            - :math:`K`.
            - :math:`n`.
            - Temperature if the data depend on temperature.
            - Value of the first field variable if the data depend on field variables.
            - Value of the second field variable.
            - Etc.

        - If type=TABULAR, the table specifies the following:

            - Yield stress.
            - Plastic strain.
            - Temperature if the data depend on temperature.
            - Value of the first field variable if the data depend on field variables.
            - Value of the second field variable.
            - Etc.

        The corresponding analysis keywords are:

        - PLASTICITY CORRECTION

    .. versionadded:: 2023

        The ``PlasticityCorrection`` class was added.
    """

    #: Set type=RAMBERG_OSGOOD to specify the Ramberg-Osgood relationship.
    #: Set type=TABULAR to specify the tabular form.
    type: Literal[C.RAMBERG_OSGOOD, C.TABULAR]

    #: A sequence of sequences of Floats specifying the items described below.
    table: Sequence[Sequence[float]]

    #: A Boolean specifying whether the data depend on temperature. The default value is OFF.
    temperatureDependency: Boolean = OFF

    #: An Int specifying the number of field variable dependencies. The default value is 0.
    dependencies: int = 0

    @abaqus_method_doc
    def __init__(
        self,
        type: Literal[C.RAMBERG_OSGOOD, C.TABULAR],
        table: Sequence[Sequence[float]],
        temperatureDependency: Boolean = OFF,
        dependencies: int = 0,
    ):
        """This method creates a PlasticityCorrection object.

        .. note::
            This function can be accessed by::

                mdb.models[name].materials[name].PlasticityCorrection
                session.odbs[name].materials[name].PlasticityCorrection

        Parameters
        ----------
        type
            Set type=RAMBERG_OSGOOD to specify the Ramberg-Osgood relationship.
            Set type=TABULAR to specify the tabular form.
        table
            A sequence of sequences of Floats specifying the items described below.
        temperatureDependency
            A Boolean specifying whether the data depend on temperature. The default value is OFF.
        dependencies
            An Int specifying the number of field variable dependencies. The default value is 0.

        Returns
        -------
        PlasticityCorrection
            A PlasticityCorrection object.

        Raises
        ------
        RangeError
        """
        ...

    @abaqus_method_doc
    def setValues(self, *args, **kwargs):
        """This method modifies the PlasticityCorrection object.

        Raises
        ------
        RangeError
        """
        ...
