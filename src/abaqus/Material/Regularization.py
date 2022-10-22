from typing_extensions import Literal
from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from ..UtilityAndView.abaqusConstants import abaqusConstants as C
from ..UtilityAndView.abaqusConstants import LOGARITHMIC, SymbolicConstant


@abaqus_class_doc
class Regularization:
    """The Regularization object defines the tolerance to be used for regularizing material
    data.

    .. note:: 
        This object can be accessed by::

            import material
            mdb.models[name].materials[name].regularization
            import odbMaterial
            session.odbs[name].materials[name].regularization

        The corresponding analysis keywords are:

        - DASHPOT
    """

    #: A Float specifying the tolerance to be used for regularizing material data. The default
    #: value is 0.03.
    rtol: float = 0

    #: A SymbolicConstant specifying the form of regularization of strain-rate-dependent
    #: material data. Possible values are LOGARITHMIC and LINEAR. The default value is
    #: LOGARITHMIC.
    strainRateRegularization: SymbolicConstant = LOGARITHMIC

    @abaqus_method_doc
    def __init__(
        self, rtol: float = 0, strainRateRegularization: Literal[C.LINEAR, C.LOGARITHMIC] = LOGARITHMIC
    ):
        """This method creates a Regularization object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].materials[name].Regularization
                session.odbs[name].materials[name].Regularization

        Parameters
        ----------
        rtol
            A Float specifying the tolerance to be used for regularizing material data. The default
            value is 0.03.
        strainRateRegularization
            A SymbolicConstant specifying the form of regularization of strain-rate-dependent
            material data. Possible values are LOGARITHMIC and LINEAR. The default value is
            LOGARITHMIC.

        Returns
        -------
        Regularization
            A :py:class:`~abaqus.Material.Regularization.Regularization` object.

        Raises
        ------
        RangeError
        """
        ...

    @abaqus_method_doc
    def setValues(self, *args, **kwargs):
        """This method modifies the Regularization object.

        Raises
        ------
        RangeError
        """
        ...
