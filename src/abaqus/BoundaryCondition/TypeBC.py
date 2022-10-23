from typing import Optional

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from typing_extensions import Literal

from .BoundaryCondition import BoundaryCondition
from ..Region.Region import Region
from ..UtilityAndView.abaqusConstants import NOT_APPLICABLE, SymbolicConstant
from ..UtilityAndView.abaqusConstants import abaqusConstants as C


@abaqus_class_doc
class TypeBC(BoundaryCondition):
    """The TypeBC object stores the data for several types of predefined boundary conditions
    that are commonly used in stress/displacement analyses.
    The TypeBC object is derived from the BoundaryCondition object.

    .. note:: 
        This object can be accessed by::

            import load
            mdb.models[name].boundaryConditions[name]
    """

    #: A String specifying the boundary condition repository key.
    name: str = ""

    #: A SymbolicConstant specifying how the boundary condition is defined in a BUCKLE
    #: analysis. Possible values are NOT_APPLICABLE, STRESS_PERTURBATION, BUCKLING_MODES, and
    #: PERTURBATION_AND_BUCKLING. The default value is NOT_APPLICABLE.
    buckleCase: SymbolicConstant = NOT_APPLICABLE

    #: A SymbolicConstant specifying the category of the boundary condition. Possible values
    #: are MECHANICAL and THERMAL.
    category: Optional[SymbolicConstant] = None

    #: A :py:class:`~abaqus.Region.Region.Region` object specifying the region to which the boundary condition is applied.
    region: Region = Region()

    #: None or a DatumCsys object specifying the local coordinate system of the boundary
    #: condition's degrees of freedom. If **localCsys** = None, the degrees of freedom are defined
    #: in the global coordinate system. The default value is None.
    localCsys: Optional[str] = None

    @abaqus_method_doc
    def __init__(
        self,
        name: str,
        createStepName: str,
        region: Region,
        buckleCase: Literal[C.STRESS_PERTURBATION, C.NOT_APPLICABLE, C.BUCKLING_MODES, C.BUCKLE, C.PERTURBATION_AND_BUCKLING] = NOT_APPLICABLE,
        localCsys: Optional[str] = None,
    ) -> None:
        """This method creates an TypeBC object.
        
        .. note:: 
            This function can be accessed by::

                mdb.models[name].EncastreBC
                mdb.models[name].PinnedBC
                mdb.models[name].XsymmBC
                mdb.models[name].YsymmBC
                mdb.models[name].ZsymmBC
                mdb.models[name].XasymmBC
                mdb.models[name].YasymmBC
                mdb.models[name].ZasymmBC

        Parameters
        ----------
        name
            A String specifying the boundary condition repository key.
        createStepName
            A String specifying the name of the step in which the boundary condition is created.
        region
            A :py:class:`~abaqus.Region.Region.Region` object specifying the region to which the boundary condition is applied.
        buckleCase
            A SymbolicConstant specifying how the boundary condition is defined in a BUCKLE
            analysis. Possible values are NOT_APPLICABLE, STRESS_PERTURBATION, BUCKLING_MODES, and
            PERTURBATION_AND_BUCKLING. The default value is NOT_APPLICABLE.
        localCsys
            None or a DatumCsys object specifying the local coordinate system of the boundary
            condition's degrees of freedom. If **localCsys** = None, the degrees of freedom are defined
            in the global coordinate system. The default value is None.
        """
        super().__init__()
        self.name = name
        self.buckleCase = buckleCase
        self.region = region
        self.localCsys = localCsys

    @staticmethod
    @abaqus_method_doc
    def EncastreBC(
        name: str,
        createStepName: str,
        region: Region,
        buckleCase: SymbolicConstant = NOT_APPLICABLE,
        localCsys: Optional[str] = None,
    ) -> "TypeBC":
        """This method creates an encastre TypeBC object.
        
        .. note:: 
            This function can be accessed by::

                mdb.models[name].EncastreBC

        Parameters
        ----------
        name
            A String specifying the boundary condition repository key.
        createStepName
            A String specifying the name of the step in which the boundary condition is created.
        region
            A :py:class:`~abaqus.Region.Region.Region` object specifying the region to which the boundary condition is applied.
        buckleCase
            A SymbolicConstant specifying how the boundary condition is defined in a BUCKLE
            analysis. Possible values are NOT_APPLICABLE, STRESS_PERTURBATION, BUCKLING_MODES, and
            PERTURBATION_AND_BUCKLING. The default value is NOT_APPLICABLE.
        localCsys
            None or a DatumCsys object specifying the local coordinate system of the boundary
            condition's degrees of freedom. If **localCsys** = None, the degrees of freedom are defined
            in the global coordinate system. The default value is None.

        Returns
        -------
        TypeBC
            A :py:class:`~abaqus.BoundaryCondition.TypeBC.TypeBC` object.
        """
        return TypeBC(name, createStepName, region, buckleCase, localCsys)

    @staticmethod
    @abaqus_method_doc
    def PinnedBC(
        name: str,
        createStepName: str,
        region: Region,
        buckleCase: SymbolicConstant = NOT_APPLICABLE,
        localCsys: Optional[str] = None,
    ) -> "TypeBC":
        """This method creates a pinned TypeBC object.
        
        .. note:: 
            This function can be accessed by::

                mdb.models[name].PinnedBC

        Parameters
        ----------
        name
            A String specifying the boundary condition repository key.
        createStepName
            A String specifying the name of the step in which the boundary condition is created.
        region
            A :py:class:`~abaqus.Region.Region.Region` object specifying the region to which the boundary condition is applied.
        buckleCase
            A SymbolicConstant specifying how the boundary condition is defined in a BUCKLE
            analysis. Possible values are NOT_APPLICABLE, STRESS_PERTURBATION, BUCKLING_MODES, and
            PERTURBATION_AND_BUCKLING. The default value is NOT_APPLICABLE.
        localCsys
            None or a DatumCsys object specifying the local coordinate system of the boundary
            condition's degrees of freedom. If **localCsys** = None, the degrees of freedom are defined
            in the global coordinate system. The default value is None.

        Returns
        -------
        TypeBC
            A :py:class:`~abaqus.BoundaryCondition.TypeBC.TypeBC` object.
        """
        return TypeBC(name, createStepName, region, buckleCase, localCsys)

    @staticmethod
    @abaqus_method_doc
    def XsymmBC(
        name: str,
        createStepName: str,
        region: Region,
        buckleCase: SymbolicConstant = NOT_APPLICABLE,
        localCsys: Optional[str] = None,
    ) -> "TypeBC":
        """This method creates a TypeBC object that specifies symmetry about the **X**-axis.
        
        .. note:: 
            This function can be accessed by::

                mdb.models[name].XsymmBC

        Parameters
        ----------
        name
            A String specifying the boundary condition repository key.
        createStepName
            A String specifying the name of the step in which the boundary condition is created.
        region
            A :py:class:`~abaqus.Region.Region.Region` object specifying the region to which the boundary condition is applied.
        buckleCase
            A SymbolicConstant specifying how the boundary condition is defined in a BUCKLE
            analysis. Possible values are NOT_APPLICABLE, STRESS_PERTURBATION, BUCKLING_MODES, and
            PERTURBATION_AND_BUCKLING. The default value is NOT_APPLICABLE.
        localCsys
            None or a DatumCsys object specifying the local coordinate system of the boundary
            condition's degrees of freedom. If **localCsys** = None, the degrees of freedom are defined
            in the global coordinate system. The default value is None.

        Returns
        -------
        TypeBC
            A :py:class:`~abaqus.BoundaryCondition.TypeBC.TypeBC` object.
        """
        return TypeBC(name, createStepName, region, buckleCase, localCsys)

    @staticmethod
    @abaqus_method_doc
    def YsymmBC(
        name: str,
        createStepName: str,
        region: Region,
        buckleCase: SymbolicConstant = NOT_APPLICABLE,
        localCsys: Optional[str] = None,
    ) -> "TypeBC":
        """This method creates a TypeBC object that specifies symmetry about the **Y**-axis.
        
        .. note:: 
            This function can be accessed by::

                mdb.models[name].YsymmBC

        Parameters
        ----------
        name
            A String specifying the boundary condition repository key.
        createStepName
            A String specifying the name of the step in which the boundary condition is created.
        region
            A :py:class:`~abaqus.Region.Region.Region` object specifying the region to which the boundary condition is applied.
        buckleCase
            A SymbolicConstant specifying how the boundary condition is defined in a BUCKLE
            analysis. Possible values are NOT_APPLICABLE, STRESS_PERTURBATION, BUCKLING_MODES, and
            PERTURBATION_AND_BUCKLING. The default value is NOT_APPLICABLE.
        localCsys
            None or a DatumCsys object specifying the local coordinate system of the boundary
            condition's degrees of freedom. If **localCsys** = None, the degrees of freedom are defined
            in the global coordinate system. The default value is None.

        Returns
        -------
        TypeBC
            A :py:class:`~abaqus.BoundaryCondition.TypeBC.TypeBC` object.
        """
        return TypeBC(name, createStepName, region, buckleCase, localCsys)

    @staticmethod
    @abaqus_method_doc
    def ZsymmBC(
        name: str,
        createStepName: str,
        region: Region,
        buckleCase: SymbolicConstant = NOT_APPLICABLE,
        localCsys: Optional[str] = None,
    ) -> "TypeBC":
        """This method creates a TypeBC object that specifies symmetry about the **Z**-axis.
        
        .. note:: 
            This function can be accessed by::

                mdb.models[name].ZsymmBC

        Parameters
        ----------
        name
            A String specifying the boundary condition repository key.
        createStepName
            A String specifying the name of the step in which the boundary condition is created.
        region
            A :py:class:`~abaqus.Region.Region.Region` object specifying the region to which the boundary condition is applied.
        buckleCase
            A SymbolicConstant specifying how the boundary condition is defined in a BUCKLE
            analysis. Possible values are NOT_APPLICABLE, STRESS_PERTURBATION, BUCKLING_MODES, and
            PERTURBATION_AND_BUCKLING. The default value is NOT_APPLICABLE.
        localCsys
            None or a DatumCsys object specifying the local coordinate system of the boundary
            condition's degrees of freedom. If **localCsys** = None, the degrees of freedom are defined
            in the global coordinate system. The default value is None.

        Returns
        -------
        TypeBC
            A :py:class:`~abaqus.BoundaryCondition.TypeBC.TypeBC` object.
        """
        return TypeBC(name, createStepName, region, buckleCase, localCsys)

    @staticmethod
    @abaqus_method_doc
    def XasymmBC(
        name: str,
        createStepName: str,
        region: Region,
        buckleCase: SymbolicConstant = NOT_APPLICABLE,
        localCsys: Optional[str] = None,
    ) -> "TypeBC":
        """This method creates a TypeBC object that specifies antisymmetry about the **X**-axis.
        
        .. note:: 
            This function can be accessed by::

                mdb.models[name].XasymmBC

        Parameters
        ----------
        name
            A String specifying the boundary condition repository key.
        createStepName
            A String specifying the name of the step in which the boundary condition is created.
        region
            A :py:class:`~abaqus.Region.Region.Region` object specifying the region to which the boundary condition is applied.
        buckleCase
            A SymbolicConstant specifying how the boundary condition is defined in a BUCKLE
            analysis. Possible values are NOT_APPLICABLE, STRESS_PERTURBATION, BUCKLING_MODES, and
            PERTURBATION_AND_BUCKLING. The default value is NOT_APPLICABLE.
        localCsys
            None or a DatumCsys object specifying the local coordinate system of the boundary
            condition's degrees of freedom. If **localCsys** = None, the degrees of freedom are defined
            in the global coordinate system. The default value is None.

        Returns
        -------
        TypeBC
            A :py:class:`~abaqus.BoundaryCondition.TypeBC.TypeBC` object.
        """
        return TypeBC(name, createStepName, region, buckleCase, localCsys)

    @staticmethod
    @abaqus_method_doc
    def YasymmBC(
        name: str,
        createStepName: str,
        region: Region,
        buckleCase: SymbolicConstant = NOT_APPLICABLE,
        localCsys: Optional[str] = None,
    ) -> "TypeBC":
        """This method creates a TypeBC object that specifies antisymmetry about the **Y**-axis.
        
        .. note:: 
            This function can be accessed by::

                mdb.models[name].YasymmBC

        Parameters
        ----------
        name
            A String specifying the boundary condition repository key.
        createStepName
            A String specifying the name of the step in which the boundary condition is created.
        region
            A :py:class:`~abaqus.Region.Region.Region` object specifying the region to which the boundary condition is applied.
        buckleCase
            A SymbolicConstant specifying how the boundary condition is defined in a BUCKLE
            analysis. Possible values are NOT_APPLICABLE, STRESS_PERTURBATION, BUCKLING_MODES, and
            PERTURBATION_AND_BUCKLING. The default value is NOT_APPLICABLE.
        localCsys
            None or a DatumCsys object specifying the local coordinate system of the boundary
            condition's degrees of freedom. If **localCsys** = None, the degrees of freedom are defined
            in the global coordinate system. The default value is None.

        Returns
        -------
        TypeBC
            A :py:class:`~abaqus.BoundaryCondition.TypeBC.TypeBC` object.
        """
        return TypeBC(name, createStepName, region, buckleCase, localCsys)

    @staticmethod
    @abaqus_method_doc
    def ZasymmBC(
        name: str,
        createStepName: str,
        region: Region,
        buckleCase: SymbolicConstant = NOT_APPLICABLE,
        localCsys: Optional[str] = None,
    ) -> "TypeBC":
        """This method creates a TypeBC object that specifies antisymmetry about the **Z**-axis.
        
        .. note:: 
            This function can be accessed by::

                mdb.models[name].ZasymmBC

        Parameters
        ----------
        name
            A String specifying the boundary condition repository key.
        createStepName
            A String specifying the name of the step in which the boundary condition is created.
        region
            A :py:class:`~abaqus.Region.Region.Region` object specifying the region to which the boundary condition is applied.
        buckleCase
            A SymbolicConstant specifying how the boundary condition is defined in a BUCKLE
            analysis. Possible values are NOT_APPLICABLE, STRESS_PERTURBATION, BUCKLING_MODES, and
            PERTURBATION_AND_BUCKLING. The default value is NOT_APPLICABLE.
        localCsys
            None or a DatumCsys object specifying the local coordinate system of the boundary
            condition's degrees of freedom. If **localCsys** = None, the degrees of freedom are defined
            in the global coordinate system. The default value is None.

        Returns
        -------
        TypeBC
            A :py:class:`~abaqus.BoundaryCondition.TypeBC.TypeBC` object.
        """
        return TypeBC(name, createStepName, region, buckleCase, localCsys)

    @abaqus_method_doc
    def setValues(
        self,
        region: Region,
        typeName: Optional[Literal[C.YASYMM, C.ENCASTRE, C.ZASYMM, C.ZSYMM, C.YSYMM, C.XSYMM, C.PINNED, C.XASYMM]] = None,
        buckleCase: Literal[C.STRESS_PERTURBATION, C.NOT_APPLICABLE, C.BUCKLING_MODES, C.BUCKLE, C.PERTURBATION_AND_BUCKLING] = NOT_APPLICABLE,
        localCsys: Optional[str] = None,
    ):
        """This method modifies the data for an existing TypeBC object in the step where it is
        created.
        
        Parameters
        ----------
        region
            A :py:class:`~abaqus.Region.Region.Region` object specifying the region to which the boundary condition is applied.
        typeName
            A SymbolicConstant specifying the predefined boundary condition type. Possible values
            are XSYMM, YSYMM, ZSYMM, XASYMM, YASYMM, ZASYMM, PINNED, and ENCASTRE.
        buckleCase
            A SymbolicConstant specifying how the boundary condition is defined in a BUCKLE
            analysis. Possible values are NOT_APPLICABLE, STRESS_PERTURBATION, BUCKLING_MODES, and
            PERTURBATION_AND_BUCKLING. The default value is NOT_APPLICABLE.
        localCsys
            None or a DatumCsys object specifying the local coordinate system of the boundary
            condition's degrees of freedom. If **localCsys** = None, the degrees of freedom are defined
            in the global coordinate system. The default value is None.
        """
        ...

    @abaqus_method_doc
    def setValuesInStep(self, stepName: str, typeName: Optional[Literal[C.YASYMM, C.ENCASTRE, C.ZASYMM, C.ZSYMM, C.YSYMM, C.XSYMM, C.PINNED, C.XASYMM]] = None):
        """This method always returns a value error for a TypeBC; it is inherited from the
        BoundaryCondition object.

        Parameters
        ----------
        stepName
            A String specifying the name of the step in which the boundary condition is modified.
        typeName
            A SymbolicConstant specifying the predefined boundary condition type. Possible values
            are XSYMM, YSYMM, ZSYMM, XASYMM, YASYMM, ZASYMM, PINNED, and ENCASTRE.

        Raises
        ------
        Value Error
            A Symmetry/Antisymmetry/Encastre BC cannot be edited in a propagated step.
        """
        ...
