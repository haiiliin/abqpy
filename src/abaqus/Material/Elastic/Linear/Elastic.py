from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from typing_extensions import Literal

from .FailStrain import FailStrain
from .FailStress import FailStress
from ....UtilityAndView.abaqusConstants import Boolean, ISOTROPIC, LONG_TERM, OFF
from ....UtilityAndView.abaqusConstants import abaqusConstants as C


@abaqus_class_doc
class Elastic:
    r"""The Elastic object specifies elastic material properties.

    .. note::
        This object can be accessed by::

            import material
            mdb.models[name].materials[name].elastic
            import odbMaterial
            session.odbs[name].materials[name].elastic

        The table data for this object are:

        - If **type** = ISOTROPIC, the table data specify the following:

            - The Young's modulus, :math:`E`.
            - The Poisson's ratio, :math:`\nu`.
            - Temperature, if the data depend on temperature.
            - Value of the first field variable, if the data depend on field variables.
            - Value of the second field variable.
            - Etc.

        - If **type** = SHEAR, the table data specify the following:

            - The shear modulus, :math:`G`.
            - Temperature, if the data depend on temperature.
            - Value of the first field variable, if the data depend on field variables.
            - Value of the second field variable.
            - Etc.

        - If **type** = ENGINEERING_CONSTANTS, the table data specify the following:

            - :math:`E_{1}`.
            - :math:`E_{2}`.
            - :math:`E_{3}`.
            - :math:`\nu_{12}`.
            - :math:`\nu_{13}`.
            - :math:`\nu_{23}`.
            - :math:`G_{12}`.
            - :math:`G_{13}`.
            - :math:`G_{23}`.
            - Temperature, if the data depend on temperature.
            - Value of the first field variable, if the data depend on field variables.
            - Value of the second field variable.
            - Etc.

        - If **type** = LAMINA, the table data specify the following:

            - :math:`E_{1}`.
            - :math:`E_{2}`.
            - :math:`\nu_{12}`.
            - :math:`G_{12}`.
            - :math:`G_{13}`. This shear modulus is needed to define transverse shear behavior in shells.
            - :math:`G_{23}`. This shear modulus is needed to define transverse shear behavior in shells.
            - Temperature, if the data depend on temperature.
            - Value of the first field variable, if the data depend on field variables.
            - Value of the second field variable.
            - Etc.

        - If **type** = ORTHOTROPIC, the table data specify the following:

            - :math:`D_{1111}`
            - :math:`D_{1122}`
            - :math:`D_{2222}`
            - :math:`D_{1133}`
            - :math:`D_{2233}`
            - :math:`D_{3333}`
            - :math:`D_{1212}`
            - :math:`D_{1313}`
            - :math:`D_{2323}`
            - Temperature, if the data depend on temperature.
            - Value of the first field variable, if the data depend on field variables.
            - Value of the second field variable.
            - Etc.

        - If **type** = ANISOTROPIC, the table data specify the following:

            - :math:`D_{1111}`.
            - :math:`D_{1122}`.
            - :math:`D_{2222}`.
            - :math:`D_{1133}`.
            - :math:`D_{2233}`.
            - :math:`D_{3333}`.
            - :math:`D_{1112}`.
            - :math:`D_{2212}`.
            - :math:`D_{3312}`.
            - :math:`D_{1212}`.
            - :math:`D_{1113}`.
            - :math:`D_{2213}`.
            - :math:`D_{3313}`.
            - :math:`D_{1213}`.
            - :math:`D_{1313}`.
            - :math:`D_{1123}`.
            - :math:`D_{2223}`.
            - :math:`D_{3323}`.
            - :math:`D_{1223}`.
            - :math:`D_{1323}`.
            - :math:`D_{2323}`.
            - Temperature, if the data depend on temperature.
            - Value of the first field variable, if the data depend on field variables.
            - Value of the second field variable.
            - Etc.

        - If **type** = TRACTION, the table data specify the following:

            - :math:`E` for warping elements; :math:`E_{nn}` for cohesive elements.
            - :math:`G_1` for warping elements; :math:`E_{ss}` for cohesive elements.
            - :math:`G_2` for warping elements; :math:`E_{tt}` for cohesive elements.
            - Temperature, if the data depend on temperature.
            - Value of the first field variable, if the data depend on field variables.
            - Value of the second field variable.
            - Etc.

        - If **type** = BILAMINA, the table data specify the following:

            - :math:`E_{n n}`.
            - :math:`E_{s s}`.
            - :math:`E_{t t}`.
            - :math:`E_{n s}`.
            - :math:`E_{n t}`.
            - :math:`E_{s t}`.
            - Temperature, if the data depend on temperature.
            - Value of the first field variable, if the data depend on field variables.
            - Value of the second field variable.
            - Etc.

        - If **type** = SHORT_FIBER, there is no table data.

        The corresponding analysis keywords are:

        - ELASTIC
    """

    #: A :py:class:`~abaqus.Material.Elastic.Linear.FailStress.FailStress` object.
    failStress: FailStress = FailStress(((),))

    #: A :py:class:`~abaqus.Material.Elastic.Linear.FailStrain.FailStrain` object.
    failStrain: FailStrain = FailStrain(((),))

    @abaqus_method_doc
    def __init__(
        self,
        table: tuple,
        type: Literal[
            C.ENGINEERING_CONSTANTS,
            C.TRACTION,
            C.LAMINA,
            C.SHEAR,
            C.ANISOTROPIC,
            C.ORTHOTROPIC,
            C.SHORT_FIBER,
            C.BILAMINA,
            C.ISOTROPIC,
            C.COUPLED_TRACTION,
        ] = ISOTROPIC,
        noCompression: Boolean = OFF,
        noTension: Boolean = OFF,
        temperatureDependency: Boolean = OFF,
        dependencies: int = 0,
        moduli: Literal[C.INSTANTANEOUS, C.LONG_TERM] = LONG_TERM,
    ):
        """This method creates an Elastic object.

        .. note::
            This function can be accessed by::

                mdb.models[name].materials[name].Elastic
                session.odbs[name].materials[name].Elastic

        Parameters
        ----------
        table
            A sequence of sequences of Floats specifying the items described below.
        type
            A SymbolicConstant specifying the type of elasticity data provided. Possible values are:

            - ISOTROPIC
            - ORTHOTROPIC
            - ANISOTROPIC
            - ENGINEERING_CONSTANTS
            - LAMINA
            - TRACTION
            - COUPLED_TRACTION
            - SHORT_FIBER
            - SHEAR
            - BILAMINA

            The default value is ISOTROPIC.

            .. versionchanged:: 2022
                Add available value: BILAMINA.
        noCompression
            A Boolean specifying whether compressive stress is allowed. The default value is OFF.
        noTension
            A Boolean specifying whether tensile stress is allowed. The default value is OFF.
        temperatureDependency
            A Boolean specifying whether the data depend on temperature. The default value is OFF.
        dependencies
            An Int specifying the number of field variable dependencies. The default value is 0.
        moduli
            A SymbolicConstant specifying the time-dependence of the elastic material constants.
            Possible values are INSTANTANEOUS and LONG_TERM. The default value is LONG_TERM.

        Returns
        -------
        Elastic
            An :py:class:`~abaqus.Material.Elastic.Linear.Elastic.Elastic` object.

        Raises
        ------
        RangeError
        """
        ...

    @abaqus_method_doc
    def setValues(self, *args, **kwargs):
        """This method modifies the Elastic object.

        Raises
        ------
        RangeError
        """
        ...
