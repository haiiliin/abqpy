from typing_extensions import Literal
from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from .DerivedComponent import DerivedComponent
from ..UtilityAndView.abaqusConstants import abaqusConstants as C
from ..UtilityAndView.abaqusConstants import ABS, COMPONENT_NUMBER, POSITIVE, SymbolicConstant


@abaqus_class_doc
class ConnectorPotential:
    """The ConnectorPotential object is used to define a restricted set of mathematical
    functions to represent yield or limiting surfaces in the space spanned by connector
    available components. It can be used only in conjunction with ConnectorDamage,
    ConnectorFriction, and ConnectorPlasticity objects. Because the ConnectorDamage object
    contains two separate ConnectorPotential repositories (one for damage initiation and one
    for damage evolution), there are two ConnectorPotential constructors associated with
    that behavior—IniPotential and EvoPotential.

    .. note:: 
        This object can be accessed by::

            import section
            mdb.models[name].sections[name].behaviorOptions[i].connectorPotentials[i]
            mdb.models[name].sections[name].behaviorOptions[i].evolutionPotentials[i]
            mdb.models[name].sections[name].behaviorOptions[i].initiationPotentials[i]
            import odbSection
            session.odbs[name].sections[name].behaviorOptions[i].connectorPotentials[i]
            session.odbs[name].sections[name].behaviorOptions[i].evolutionPotentials[i]
            session.odbs[name].sections[name].behaviorOptions[i].initiationPotentials[i]

        The corresponding analysis keywords are:

        - CONNECTOR POTENTIAL
    """

    #: A :py:class:`~abaqus.Connector.ConnectorBehaviorOption.DerivedComponent` object specifying the DerivedComponent used in the contribution. This
    #: argument is applicable only if **componentStyle** = DERIVED_COMPONENT.
    derivedComponent: DerivedComponent = DerivedComponent()

    #: A SymbolicConstant specifying whether a component number or the name of the
    #: DerivedComponent object will be used in the contribution. Possible values are
    #: COMPONENT_NUMBER and DERIVED_COMPONENT. The default value is COMPONENT_NUMBER.
    componentStyle: SymbolicConstant = COMPONENT_NUMBER

    #: An Int specifying the component number used in the contribution. This argument is
    #: applicable only if **componentStyle** = COMPONENT_NUMBER. Possible values are 1 ≤
    #: **componentNumber** ≤ 6. Only available components can be specified. The default value is
    #: 0.
    componentNumber: int = 0

    #: A SymbolicConstant specifying the sign of the contribution. Possible values are POSITIVE
    #: and NEGATIVE. The default value is POSITIVE.
    sign: SymbolicConstant = POSITIVE

    #: A Float specifying the scaling factor for the contribution. The default value is 1.0.
    scaleFactor: float = 1

    #: A Float specifying the positive exponent for the contribution. The default value is
    #: 2.0.This argument is ignored if the potential operator of the invoking behavior option
    #: is set to MAXIMUM.
    positiveExponent: float = 2

    #: A Float specifying the shift factor for the contribution. The default value is 0.0.
    shiftFactor: float = 0

    #: A SymbolicConstant specifying the H function of the contribution: either absolute value,
    #: Macauley bracket, or the identity function. Possible values are ABS, MACAULEY, and
    #: IDENTITY. The default value is ABS.The value of IDENTITY can be used only if
    #: **positiveExponent** = 1.0 and the potential exponent of the invoking behavior option is
    #: also 1.0 (i.e., the potential operator of the invoking behavior option must be SUM).
    hFunction: SymbolicConstant = ABS

    @abaqus_method_doc
    def __init__(
        self,
        componentStyle: Literal[C.COMPONENT_NUMBER, C.DERIVED_COMPONENT] = COMPONENT_NUMBER,
        componentNumber: int = 0,
        sign: Literal[C.POSITIVE, C.NEGATIVE] = POSITIVE,
        scaleFactor: float = 1,
        positiveExponent: float = 2,
        shiftFactor: float = 0,
        hFunction: Literal[C.MACAULEY, C.IDENTITY, C.ABS] = ABS,
    ):
        """This method creates a connector potential object to be used in conjunction with an
        allowable connector behavior option.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].sections[name].behaviorOptions[i].ConnectorPotential
                session.odbs[name].sections[name].behaviorOptions[i].ConnectorPotential
            
        Parameters
        ----------
        componentStyle
            A SymbolicConstant specifying whether a component number or the name of the 
            DerivedComponent object will be used in the contribution. Possible values are 
            COMPONENT_NUMBER and DERIVED_COMPONENT. The default value is COMPONENT_NUMBER. 
        componentNumber
            An Int specifying the component number used in the contribution. This argument is 
            applicable only if **componentStyle** = COMPONENT_NUMBER. Possible values are 1 ≤ 
            **componentNumber** ≤ 6. Only available components can be specified. The default value is 
            0. 
        sign
            A SymbolicConstant specifying the sign of the contribution. Possible values are POSITIVE 
            and NEGATIVE. The default value is POSITIVE. 
        scaleFactor
            A Float specifying the scaling factor for the contribution. The default value is 1.0. 
        positiveExponent
            A Float specifying the positive exponent for the contribution. The default value is 
            2.0.This argument is ignored if the potential operator of the invoking behavior option 
            is set to MAXIMUM. 
        shiftFactor
            A Float specifying the shift factor for the contribution. The default value is 0.0. 
        hFunction
            A SymbolicConstant specifying the H function of the contribution: either absolute value, 
            Macauley bracket, or the identity function. Possible values are ABS, MACAULEY, and 
            IDENTITY. The default value is ABS.The value of IDENTITY can be used only if 
            **positiveExponent** = 1.0 and the potential exponent of the invoking behavior option is 
            also 1.0 (i.e., the potential operator of the invoking behavior option must be SUM). 

        Returns
        -------
        ConnectorPotential
            A :py:class:`~abaqus.Connector.ConnectorPotential.ConnectorPotential` object. 

        Raises
        ------
        ValueError and TextError 
        """
        ...

    @abaqus_method_doc
    def setValues(self, *args, **kwargs):
        """This method modifies the ConnectorPotential object.

        Raises
        ------
        ValueError
        """
        ...

    @abaqus_method_doc
    def DerivedComponent(self) -> DerivedComponent:
        """This method creates a DerivedComponent object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].sections[name].behaviorOptions[i].ConnectorPotential
                session.odbs[name].sections[name].behaviorOptions[i].ConnectorPotential

        Returns
        -------
        DerivedComponent
            A :py:class:`~abaqus.Connector.ConnectorBehaviorOption.DerivedComponent` object.

        Raises
        ------
        ValueError and TextError
        """
        self.derivedComponent = derivedComponent = DerivedComponent()
        return derivedComponent
