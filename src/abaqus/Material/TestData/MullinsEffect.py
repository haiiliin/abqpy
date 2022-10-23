from abqpy.decorators import abaqus_class_doc

from .BiaxialTestDataArray import BiaxialTestDataArray
from .PlanarTestDataArray import PlanarTestDataArray
from .UniaxialTestDataArray import UniaxialTestDataArray
from ...UtilityAndView.abaqusConstants import Boolean, CONSTANTS, OFF, SymbolicConstant


@abaqus_class_doc
class MullinsEffect:
    """The MullinsEffect specifies properties for mullins data.

    .. note::
        This object can be accessed by::

            import material
            mdb.models[name].materials[name].mullinsEffect
            import odbMaterial
            session.odbs[name].materials[name].mullinsEffect
    """

    #: A SymbolicConstant specifying the method of specifying the data. Possible values are
    #: USER, CONSTANTS, and TEST_DATA. The default value is CONSTANTS.
    definition: SymbolicConstant = CONSTANTS

    #: A Boolean specifying whether the data depend on temperature. The default value is OFF.
    temperatureDependency: Boolean = OFF

    #: An Int specifying the number of field variable dependencies. The default value is 0.
    dependencies: int = 0

    #: An Int specifying the number of property values needed as data for the user-defined
    #: hyperelastic material. The default value is 0.
    properties: int = 0

    #: A tuple of tuples of Floats specifying the items described below. The default value is
    #: an empty sequence.
    table: tuple = ()

    #: A :py:class:`~abaqus.Material.TestData.UniaxialTestDataArray.UniaxialTestDataArray` object.
    uniaxialTests: UniaxialTestDataArray = []

    #: A :py:class:`~abaqus.Material.TestData.BiaxialTestDataArray.BiaxialTestDataArray` object.
    biaxialTests: BiaxialTestDataArray = []

    #: A :py:class:`~abaqus.Material.TestData.PlanarTestDataArray.PlanarTestDataArray` object.
    planarTests: PlanarTestDataArray = []
