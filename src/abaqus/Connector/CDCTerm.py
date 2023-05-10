from typing_extensions import Literal

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from ..UtilityAndView.abaqusConstants import (
    CONSTANT,
    LINEAR,
    OFF,
    ON,
    POSITION,
    POSITIVE,
    RSS,
    Boolean,
    SymbolicConstant,
)
from ..UtilityAndView.abaqusConstants import abaqusConstants as C
from .ConnectorOptions import ConnectorOptions


@abaqus_class_doc
class CDCTerm:
    """The CDCTerm object is used to create contributing terms for a DerivedComponent object.

    .. note::
        This object can be accessed by::

            import section
            mdb.models[name].sections[name].behaviorOptions[i].connectorPotentials[i].derivedComponent.cdcTerms[i]
            mdb.models[name].sections[name].behaviorOptions[i].derivedComponent.cdcTerms[i]
            mdb.models[name].sections[name].behaviorOptions[i].evolutionPotentials[i].derivedComponent.cdcTerms[i]
            mdb.models[name].sections[name].behaviorOptions[i].initiationPotentials[i].derivedComponent.cdcTerms[i]
            import odbSection
            session.odbs[name].sections[name].behaviorOptions[i].connectorPotentials[i].derivedComponent.cdcTerms[i]
            session.odbs[name].sections[name].behaviorOptions[i].derivedComponent.cdcTerms[i]
            session.odbs[name].sections[name].behaviorOptions[i].evolutionPotentials[i].derivedComponent.cdcTerms[i]
            session.odbs[name].sections[name].behaviorOptions[i].initiationPotentials[i].derivedComponent.cdcTerms[i]
    """

    #: A ConnectorOptions object specifying the ConnectorOptions used to define tabular options
    #: for this ConnectorBehaviorOption.
    options: ConnectorOptions = ConnectorOptions()

    #: A sequence of Ints specifying the components of relative motion for which the
    #: contributing term is defined. Possible values are 1 ≤ **intrinsicComponents** ≤ 6. Only
    #: available components can be specified if the DerivedComponent object is being referenced
    #: by a Potential object. This is not the case if the DerivedComponent object is referenced
    #: by a ConnectorFriction object directly. The default value is an empty sequence.
    intrinsicComponents: tuple

    #: A sequence of sequences of Floats specifying components numbers and temperature and
    #: field values. Each sequence of the table data specifies:The first intrinsic component
    #: number.If applicable, the second intrinsic component number.Etc.If applicable, the first
    #: independent component number.If applicable, the second independent component
    #: number.Etc.If applicable, the temperature value.If applicable, the value of the first
    #: field variable.If applicable, the value of the second field variable.Etc.The default
    #: value is an empty sequence.
    table: tuple

    #: A SymbolicConstant specifying the method for combining contributing terms: square root
    #: of a sum of the squares, direct sum, or Macauley sum. Possible values are RSS, SUM, and
    #: MACAULEY. The default value is RSS.
    termOperator: SymbolicConstant = RSS

    #: A SymbolicConstant specifying the overall sign for the contributing term. Possible
    #: values are POSITIVE and NEGATIVE. The default value is POSITIVE.
    termSign: SymbolicConstant = POSITIVE

    #: A Boolean specifying whether the table data depend on either components of relative
    #: position or components of constitutive relative motion. The default value is OFF.
    localDependency: Boolean = OFF

    #: A SymbolicConstant specifying whether localDependency refers to components of relative
    #: position or components of constitutive relative motion. Possible values are POSITION and
    #: MOTION. The default value is POSITION.The **indepCompType** argument applies only if
    #: **localDependency** = ON.
    indepCompType: SymbolicConstant = POSITION

    #: A sequence of Ints specifying the independent components included in the derived
    #: component definition. Possible values are 1 ≤ **indepComponents** ≤ 6. Only available
    #: components can be specified. The **indepComponents** argument applies only if
    #: **localDependency** = ON. The default value is an empty sequence.
    indepComponents: tuple = ()

    #: A Boolean specifying whether the table data depend on temperature. The default value is
    #: OFF.
    tempDependency: Boolean = OFF

    #: An Int specifying the number of field variable dependencies. The default value is 0.
    fieldDependencies: int = 0

    @abaqus_method_doc
    def __init__(
        self,
        intrinsicComponents: tuple,
        table: tuple,
        termOperator: Literal[C.SUM, C.RSS, C.MACAULEY] = RSS,
        termSign: Literal[C.POSITIVE, C.NEGATIVE] = POSITIVE,
        localDependency: Boolean = OFF,
        indepCompType: Literal[C.POSITION, C.MOTION] = POSITION,
        indepComponents: tuple = (),
        tempDependency: Boolean = OFF,
        fieldDependencies: int = 0,
    ):
        """This method creates a CDCTerm object.

        .. note::
            This function can be accessed by::

                mdb.models[name].sections[name].behaviorOptions[i].connectorPotentials[i].derivedComponent.CDCTerm
                mdb.models[name].sections[name].behaviorOptions[i].derivedComponent.CDCTerm
                mdb.models[name].sections[name].behaviorOptions[i].evolutionPotentials[i].derivedComponent.CDCTerm
                mdb.models[name].sections[name].behaviorOptions[i].initiationPotentials[i].derivedComponent.CDCTerm
                session.odbs[name].sections[name].behaviorOptions[i].connectorPotentials[i].derivedComponent.CDCTerm
                session.odbs[name].sections[name].behaviorOptions[i].derivedComponent.CDCTerm
                session.odbs[name].sections[name].behaviorOptions[i].evolutionPotentials[i].derivedComponent.CDCTerm
                session.odbs[name].sections[name].behaviorOptions[i].initiationPotentials[i].derivedComponent.CDCTerm

        Parameters
        ----------
        intrinsicComponents
            A sequence of Ints specifying the components of relative motion for which the
            contributing term is defined. Possible values are 1 ≤ **intrinsicComponents** ≤ 6. Only
            available components can be specified if the DerivedComponent object is being referenced
            by a Potential object. This is not the case if the DerivedComponent object is referenced
            by a ConnectorFriction object directly. The default value is an empty sequence.
        table
            A sequence of sequences of Floats specifying components numbers and temperature and
            field values. Each sequence of the table data specifies:The first intrinsic component
            number.If applicable, the second intrinsic component number.Etc.If applicable, the first
            independent component number.If applicable, the second independent component
            number.Etc.If applicable, the temperature value.If applicable, the value of the first
            field variable.If applicable, the value of the second field variable.Etc.The default
            value is an empty sequence.
        termOperator
            A SymbolicConstant specifying the method for combining contributing terms: square root
            of a sum of the squares, direct sum, or Macauley sum. Possible values are RSS, SUM, and
            MACAULEY. The default value is RSS.
        termSign
            A SymbolicConstant specifying the overall sign for the contributing term. Possible
            values are POSITIVE and NEGATIVE. The default value is POSITIVE.
        localDependency
            A Boolean specifying whether the table data depend on either components of relative
            position or components of constitutive relative motion. The default value is OFF.
        indepCompType
            A SymbolicConstant specifying whether localDependency refers to components of relative
            position or components of constitutive relative motion. Possible values are POSITION and
            MOTION. The default value is POSITION.The **indepCompType** argument applies only if
            **localDependency** = ON.
        indepComponents
            A sequence of Ints specifying the independent components included in the derived
            component definition. Possible values are 1 ≤ **indepComponents** ≤ 6. Only available
            components can be specified. The **indepComponents** argument applies only if
            **localDependency** = ON. The default value is an empty sequence.
        tempDependency
            A Boolean specifying whether the table data depend on temperature. The default value is
            OFF.
        fieldDependencies
            An Int specifying the number of field variable dependencies. The default value is 0.

        Returns
        -------
        CDCTerm
            A CDCTerm object.

        Raises
        ------
        ValueError and TextError
        """
        ...

    @abaqus_method_doc
    def setValues(self, *args, **kwargs):
        """This method modifies the CDCTerm object.

        Raises
        ------
        ValueError
        """
        ...

    @abaqus_method_doc
    def ConnectorOptions(
        self,
        useBehRegSettings: Boolean = ON,
        regularize: Boolean = ON,
        defaultTolerance: Boolean = ON,
        regularization: float = 0,
        defaultRateFactor: Boolean = ON,
        rateFactor: float = 0,
        interpolation: Literal[C.LOGARITHMIC, C.LINEAR] = LINEAR,
        useBehExtSettings: Boolean = ON,
        extrapolation: Literal[C.CONSTANT, C.LINEAR] = CONSTANT,
    ) -> ConnectorOptions:
        """This method creates a connector options object to be used in conjunction with an allowable connector
        behavior option, derived component term, or connector section.

        .. note::
            This function can be accessed by::

                mdb.models[name].sections[name].behaviorOptions[i].connectorPotentials[i].derivedComponent.CDCTerm
                mdb.models[name].sections[name].behaviorOptions[i].derivedComponent.CDCTerm
                mdb.models[name].sections[name].behaviorOptions[i].evolutionPotentials[i].derivedComponent.CDCTerm
                mdb.models[name].sections[name].behaviorOptions[i].initiationPotentials[i].derivedComponent.CDCTerm
                session.odbs[name].sections[name].behaviorOptions[i].connectorPotentials[i].derivedComponent.CDCTerm
                session.odbs[name].sections[name].behaviorOptions[i].derivedComponent.CDCTerm
                session.odbs[name].sections[name].behaviorOptions[i].evolutionPotentials[i].derivedComponent.CDCTerm
                session.odbs[name].sections[name].behaviorOptions[i].initiationPotentials[i].derivedComponent.CDCTerm

        Parameters
        ----------
        useBehRegSettings
            A Boolean specifying whether or not to use the behavior-level settings for
            regularization options. This argument is applicable only for an Abaqus/Explicit
            analysis. The default value is ON.
        regularize
            A Boolean specifying whether or not the tabular data will be regularized. This argument
            is applicable only for an Abaqus/Explicit analysis and only if **useBehRegSettings** = OFF.
            The default value is ON.
        defaultTolerance
            A Boolean specifying whether or not the analysis default regularization tolerance will
            be used. This argument is applicable only for an Abaqus/Explicit analysis and only if
            **useBehRegSettings** = OFF and **regularize** = ON. The default value is ON.
        regularization
            A Float specifying the regularization increment to be used. This argument is applicable
            only for an Abaqus/Explicit analysis and only if **useBehRegSettings** = OFF,
            **regularize** = ON, and **defaultTolerance** = OFF. The default value is 0.03.
        defaultRateFactor
            A Boolean specifying whether or not the analysis default rate filter factor will be
            used. This argument is applicable only for an Abaqus/Explicit analysis that includes
            isotropic hardening with tabular definition or damage initiation with Plastic motion
            criteria. The default value is ON.
        rateFactor
            A Float specifying the rate filter factor to be used. This argument is applicable only
            for an Abaqus/Explicit analysis that includes isotropic hardening with tabular
            definition or damage initiation with Plastic motion criteria. This argument is also
            applicable only if **defaultRateFactor** = OFF. The default value is 0.9.
        interpolation
            A SymbolicConstant specifying the type of interpolation increment to be used on
            rate-dependent tabular data. This argument is applicable only for an Abaqus/Explicit
            analysis that includes isotropic hardening with tabular definition or damage initiation
            with Plastic motion criteria. Possible values are LINEAR and LOGARITHMIC. The default
            value is LINEAR.
        useBehExtSettings
            A Boolean specifying whether or not to use the behavior-level settings for extrapolation
            options. The default value is ON.
        extrapolation
            A SymbolicConstant specifying the extrapolation technique to be used. This argument is
            applicable only if **useBehExtSettings** = OFF. Possible values are CONSTANT and LINEAR. The
            default value is CONSTANT.

        Returns
        -------
        ConnectorOptions
            A ConnectorOptions object.

        Raises
        ------
        ValueError and TextError
        """
        self.options = connectorOptions = ConnectorOptions(
            useBehRegSettings,
            regularize,
            defaultTolerance,
            regularization,
            defaultRateFactor,
            rateFactor,
            interpolation,
            useBehExtSettings,
            extrapolation,
        )
        return connectorOptions
