from typing import Union, Optional

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from .AssembledFastener import AssembledFastener
from .ContourIntegral import ContourIntegral
from .DebondVCCT import DebondVCCT
from .DiscreteFastener import DiscreteFastener
from .EngineeringFeatureBase import EngineeringFeatureBase
from .HeatCapacitance import HeatCapacitance
from .NonstructuralMass import NonstructuralMass
from .PointFastener import PointFastener
from .PointMassInertia import PointMassInertia
from .SpringDashpotToGround import SpringDashpotToGround
from .TwoPointSpringDashpot import TwoPointSpringDashpot
from .XFEMCrack import XFEMCrack
from ..Region.Region import Region
from ..Region.RegionArray import RegionArray
from ..UtilityAndView.abaqusConstants import (ALL, AXIS_1, Boolean, CONNECTOR, CONTINUUM, DEFAULT,
                                              FACETOFACE, MASS_PROPORTIONAL, MODEL, NONE, NORMALS,
                                              OFF, ON, STEP, SymbolicConstant, UNIFORM)


@abaqus_class_doc
class EngineeringFeature(EngineeringFeatureBase):
    @abaqus_method_doc
    def AssembledFastener(
        self,
        name: str,
        region: Region,
        templateModel: str,
        controlSet: Region,
        templateSurfaces: tuple,
        assignedSurfaces: tuple,
        propertyPrefix: str,
        orientMethod: SymbolicConstant = NORMALS,
        localCsys: Optional[int] = None,
        scriptName: str = "",
    ) -> AssembledFastener:
        """This method creates an AssembledFastener object. Although the constructor is available
        both for parts and for the assembly, AssembledFastener objects are currently supported
        only under the assembly.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].parts[name].engineeringFeatures.AssembledFastener
                mdb.models[name].rootAssembly.engineeringFeatures.AssembledFastener

        Parameters
        ----------
        name
            A String specifying the repository key.
        region
            A :py:class:`~abaqus.Region.Region.Region` object specifying the region of attachment points to which assembled fasteners
            are applied.
        templateModel
            A String specifying the name of the template model.
        controlSet
            A :py:class:`~abaqus.Region.Region.Region` object specifying the template model control point set. The set must contain a
            single node or vertex.
        templateSurfaces
            A sequence of Strings specifying the names of the template model surfaces that are
            referenced by tie or coupling constraints.
        assignedSurfaces
            A sequence of Strings specifying the names of the main model surfaces that will be
            substituted for the template model constraint surfaces.
        propertyPrefix
            A String specifying the name of the property prefix string. This string will be
            prepended to every property name as it is copied to the main model from the template
            model.
        orientMethod
            A SymbolicConstant specifying the method used to orient the virtual instances of the
            template model at each attachment point. Possible values are NORMALS and CSYS. The
            default value is NORMALS.
        localCsys
            None or a DatumCsys object specifying the local coordinate system. If **localCsys** = None,
            the global coordinate system is used. When this member is queried, it returns an Int.
            The default value is None.This argument applies only when **orientMethod** = CSYS.
        scriptName
            A String specifying the name of the property generation script. The default value is an
            empty string.

        Returns
        -------
        AssembledFastener
            An :py:class:`~abaqus.EngineeringFeature.AssembledFastener.AssembledFastener` object.
        """
        self.fasteners[name] = assembledFastener = AssembledFastener(
            name,
            region,
            templateModel,
            controlSet,
            templateSurfaces,
            assignedSurfaces,
            propertyPrefix,
            orientMethod,
            localCsys,
            scriptName,
        )
        return assembledFastener

    @abaqus_method_doc
    def ContourIntegral(
        self,
        name: str,
        crackFront: RegionArray,
        crackTip: RegionArray,
        extensionDirectionMethod: SymbolicConstant,
        symmetric: Boolean = OFF,
        listOfRegions: Boolean = OFF,
        crackFrontName: str = "",
        crackTipName: str = "",
        crackNormal: tuple = (),
        qVectors: tuple = (),
        midNodePosition: float = 0,
        collapsedElementAtTip: SymbolicConstant = NONE,
    ) -> ContourIntegral:
        """This method creates a ContourIntegral object. Although the constructor is available both
        for parts and for the assembly, ContourIntegral objects are currently supported only
        under the assembly.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].parts[name].engineeringFeatures.ContourIntegral
                mdb.models[name].rootAssembly.engineeringFeatures.ContourIntegral

        Parameters
        ----------
        name
            A String specifying the repository key.
        crackFront
            A :py:class:`~abaqus.Region.RegionArray.RegionArray` object specifying the crack-front region to which the contour integral is
            applied. If the crack-front consists of a single region, a Region object may be
            specified instead of a sequence with a single item in it.
        crackTip
            A :py:class:`~abaqus.Region.RegionArray.RegionArray` object specifying the crack-tip region to which the contour integral is
            applied. If the crack-tip consists of a single region, a Region object may be specified
            instead of a sequence with a single item in it.
        extensionDirectionMethod
            A SymbolicConstant specifying how the virtual crack extension direction vectors are
            defined. Possible values are CRACK_NORMAL and Q_VECTORS.
        symmetric
            A Boolean specifying whether the crack is defined on a half model (about a symmetry
            plane) or whether it is defined on the whole model. The default value is OFF.
        listOfRegions
            A Boolean specifying whether the regions specified by **crackFront** and **crackTip** are
            specified using a single region or tuples of region objects. The default value is OFF.
        crackFrontName
            A String specifying the name of the crack-front region generated from the tuple of
            regions specifying the crack-front region. This argument is valid only when
            **listOfRegions** is ON. The default value is **name** + Front.
        crackTipName
            A String specifying the name of the crack-tip region generated from the tuple of regions
            specifying the crack-tip region. This parameter is valid only when **listOfRegions** = ON.
            The default value is **name** + Tip.
        crackNormal
            A sequence of sequences of Floats specifying the two points of the vector that describes
            the crack normal direction. Each point is defined by a tuple of two or three coordinates
            indicating its position. This argument is required only when
            **extensionDirectionMethod** = CRACK_NORMAL. The default value is an empty sequence.
        qVectors
            A sequence of sequences of sequences of Floats specifying the vectors that indicate the
            set of crack extension directions. Each vector is described by a tuple of two points,
            and each point is described by a tuple of two or three coordinates indicating its
            position. This argument is required only when **extensionDirectionMethod** = Q_VECTORS. The
            default value is an empty sequence.
        midNodePosition
            A Float specifying the position of the midside node along the edges of the second-order
            elements that radiate from the crack tip. Possible values are 0.0 < **midNodeParameter**
            < 1.0. The default value is 0.5.
        collapsedElementAtTip
            A SymbolicConstant specifying the crack-tip singularity. Possible values are NONE,
            SINGLE_NODE, and DUPLICATE_NODES. The default value is NONE.

        Returns
        -------
        ContourIntegral
            A :py:class:`~abaqus.EngineeringFeature.ContourIntegral.ContourIntegral` object.
        """
        self.cracks[name] = contourIntegral = ContourIntegral(
            name,
            crackFront,
            crackTip,
            extensionDirectionMethod,
            symmetric,
            listOfRegions,
            crackFrontName,
            crackTipName,
            crackNormal,
            qVectors,
            midNodePosition,
            collapsedElementAtTip,
        )
        return contourIntegral

    @abaqus_method_doc
    def DebondVCCT(
        self,
        name: str,
        initiationStep: str,
        surfToSurfInteraction: str,
        debondingForceAmplitude: SymbolicConstant = STEP,
        printToDATFrequency: int = 1,
    ) -> DebondVCCT:
        """This method creates a DebondVCCT object. Although the constructor is available both for
        parts and for the assembly, DebondVCCT objects are currently supported only under the
        assembly.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].parts[name].engineeringFeatures.DebondVCCT
                mdb.models[name].rootAssembly.engineeringFeatures.DebondVCCT

        Parameters
        ----------
        name
            A String specifying the repository key.
        initiationStep
            A String specifying the name of the step in which the DebondVCCT object is created.
        surfToSurfInteraction
            A String specifying the name of the SurfaceToSurfaceContactStd object that defines the
            surface to surface interaction for the crack surfaces.
        debondingForceAmplitude
            A SymbolicConstant specifying whether the debond force between the two surfaces at the
            crack tip is to be released immediately or gradually during the following increment
            after debonding. Possible values are STEP and RAMP. The default value is STEP.
        printToDATFrequency
            An Int specifying the frequency at which output will be printed to DAT file. The default
            value is 1.

        Returns
        -------
        DebondVCCT
            A :py:class:`~abaqus.EngineeringFeature.DebondVCCT.DebondVCCT` object.
        """
        self.cracks[name] = debondVCCT = DebondVCCT(
            name,
            initiationStep,
            surfToSurfInteraction,
            debondingForceAmplitude,
            printToDATFrequency,
        )
        return debondVCCT

    @abaqus_method_doc
    def DiscreteFastener(
        self,
        name: str,
        region: Region,
        influenceRadius: Union[SymbolicConstant, float],
        ur1: Boolean = ON,
        ur2: Boolean = ON,
        ur3: Boolean = ON,
        coupling: SymbolicConstant = CONTINUUM,
        weightingMethod: SymbolicConstant = UNIFORM,
        localCsys: Optional[int] = None,
    ) -> DiscreteFastener:
        """This method creates a DiscreteFastener object. Although the constructor is available
        both for parts and for the assembly, DiscreteFastener objects are currently supported
        only under the assembly.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].parts[name].engineeringFeatures.DiscreteFastener
                mdb.models[name].rootAssembly.engineeringFeatures.DiscreteFastener

        Parameters
        ----------
        name
            A String specifying the repository key.
        region
            A :py:class:`~abaqus.Region.Region.Region` object specifying the region to which the fastener is applied.
        influenceRadius
            The SymbolicConstant WHOLE_SURFACE or a Float specifying the coupling influence radius.
        ur1
            A Boolean specifying whether to constrain rotational displacement component about the
            1-direction. The default value is ON.
        ur2
            A Boolean specifying whether to constrain rotational displacement component about the
            2-direction. The default value is ON.
        ur3
            A Boolean specifying whether to constrain rotational displacement component about the
            3-direction. The default value is ON.
        coupling
            A SymbolicConstant specifying the coupling method used to couple the displacement and
            rotation of each attachment point to the average motion of the surface nodes within the
            radius of influence from the fastening point. Possible values are CONTINUUM and
            STRUCTURAL. The default value is CONTINUUM.
        weightingMethod
            A SymbolicConstant specifying the weighting scheme to be used to weight the contribution
            of the displacements of the surface nodes within the radius of influence to the motion
            of the fastening point. UNIFORM, LINEAR, QUADRATIC, and CUBIC indicate uniform, linear
            decreasing, quadratic polynomial decreasing, and cubic polynomial monotonic decreasing
            weight distributions. Possible values are UNIFORM, LINEAR, QUADRATIC, and CUBIC. The
            default value is UNIFORM.
        localCsys
            None or a DatumCsys object specifying the local coordinate system of fastener couplings.
            If **localCsys** = None, couplings are defined in the global coordinate system. When this
            member is queried, it returns an Int. The default value is None.

        Returns
        -------
        DiscreteFastener
            A :py:class:`~abaqus.EngineeringFeature.DiscreteFastener.DiscreteFastener` object.
        """
        self.fasteners[name] = discreteFastener = DiscreteFastener(
            name,
            region,
            influenceRadius,
            ur1,
            ur2,
            ur3,
            coupling,
            weightingMethod,
            localCsys,
        )
        return discreteFastener

    @abaqus_method_doc
    def HeatCapacitance(
        self,
        name: str,
        region: Region,
        table: tuple,
        temperatureDependency: Boolean = OFF,
        dependencies: int = 0,
    ) -> HeatCapacitance:
        """This method creates a HeatCapacitance object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].parts[name].engineeringFeatures.HeatCapacitance
                mdb.models[name].rootAssembly.engineeringFeatures.HeatCapacitance

        Parameters
        ----------
        name
            A String specifying the repository key.
        region
            A :py:class:`~abaqus.Region.Region.Region` object specifying the region to which the heat capacitance is applied.
        table
            A sequence of sequences of Floats specifying heat capacitance properties. The items in
            the table data are described below.
        temperatureDependency
            A Boolean specifying whether the data depend on temperature. The default value is OFF.
        dependencies
            An Int specifying the number of field variable dependencies. The default value is 0.

        Returns
        -------
        HeatCapacitance
            A :py:class:`~abaqus.EngineeringFeature.HeatCapacitance.HeatCapacitance` object.
        """
        self.inertias[name] = heatCapacitance = HeatCapacitance(
            name, region, table, temperatureDependency, dependencies
        )
        return heatCapacitance

    @abaqus_method_doc
    def NonstructuralMass(
        self,
        name: str,
        region: Region,
        units: SymbolicConstant,
        magnitude: float,
        distribution: SymbolicConstant = MASS_PROPORTIONAL,
    ) -> NonstructuralMass:
        """This method creates a NonstructuralMass object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].parts[name].engineeringFeatures.NonstructuralMass
                mdb.models[name].rootAssembly.engineeringFeatures.NonstructuralMass

        Parameters
        ----------
        name
            A String specifying the repository key.
        region
            A :py:class:`~abaqus.Region.Region.Region` object specifying the region to which the mass is applied.
        units
            A SymbolicConstant specifying the units used to specify the nonstructural mass. Possible
            values are TOTAL_MASS, MASS_PER_VOLUME, MASS_PER_AREA, and MASS_PER_LENGTH.
        magnitude
            A Float specifying the mass magnitude.
        distribution
            A SymbolicConstant specifying the distribution of the nonstructural mass. Possible
            values are MASS_PROPORTIONAL and VOLUME_PROPORTIONAL. The default value is
            MASS_PROPORTIONAL.The **distribution** argument applies only when **units** = TOTAL_MASS.

        Returns
        -------
        NonstructuralMass
            A :py:class:`~abaqus.EngineeringFeature.NonstructuralMass.NonstructuralMass` object.
        """
        self.inertias[name] = nonstructuralMass = NonstructuralMass(
            name, region, units, magnitude, distribution
        )
        return nonstructuralMass

    @abaqus_method_doc
    def PointFastener(
        self,
        name: str,
        region: Region,
        physicalRadius: float,
        directionVector: Optional[tuple] = None,
        targetSurfaces: RegionArray = MODEL,
        ur1: Boolean = ON,
        ur2: Boolean = ON,
        ur3: Boolean = ON,
        attachmentMethod: SymbolicConstant = FACETOFACE,
        influenceRadius: Union[SymbolicConstant, float] = DEFAULT,
        searchRadius: Union[SymbolicConstant, float] = DEFAULT,
        maximumLayers: SymbolicConstant = ALL,
        coupling: SymbolicConstant = CONTINUUM,
        weightingMethod: SymbolicConstant = UNIFORM,
        additionalMass: float = 0,
        adjustOrientation: Boolean = ON,
        localCsys: Optional[int] = None,
        connectionType: SymbolicConstant = CONNECTOR,
        sectionName: str = "",
        connectorOrientationLocalCsys1: Optional[int] = None,
        axis1: SymbolicConstant = AXIS_1,
        angle1: float = 0,
        orient2SameAs1: Boolean = ON,
        connectorOrientationLocalCsys2: Optional[int] = None,
        axis2: SymbolicConstant = AXIS_1,
        angle2: float = 0,
        unsorted: Boolean = OFF,
    ) -> PointFastener:
        """This method creates a PointFastener object. Although the constructor is available both
        for parts and for the assembly, PointFastener objects are currently supported only under
        the assembly.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].parts[name].engineeringFeatures.PointFastener
                mdb.models[name].rootAssembly.engineeringFeatures.PointFastener

        Parameters
        ----------
        name
            A String specifying the repository key.
        region
            A :py:class:`~abaqus.Region.Region.Region` object specifying the region to which fasteners are applied.
        physicalRadius
            A Float specifying the physical fastener radius.
        directionVector
            A :py:class:`~abaqus.BasicGeometry.VertexArray.VertexArray` object of length 2 specifying the direction of projection. Instead of
            through a ConstrainedSketchVertex, each point may be specified through a tuple of coordinates. The
            default value is None.
        targetSurfaces
            A :py:class:`~abaqus.Region.RegionArray.RegionArray` object specifying surfaces to be fastened. The default value is MODEL.
        ur1
            A Boolean specifying whether to constrain rotational displacement component about the
            1-direction. The default value is ON.
        ur2
            A Boolean specifying whether to constrain rotational displacement component about the
            2-direction. The default value is ON.
        ur3
            A Boolean specifying whether to constrain rotational displacement component about the
            3-direction. The default value is ON.
        attachmentMethod
            A SymbolicConstant specifying the method used to locate points for attaching fasteners.
            Possible values are FACETOFACE, EDGETOFACE, FACETOEDGE, and EDGETOEDGE. The default
            value is FACETOFACE.
        influenceRadius
            The SymbolicConstant DEFAULT or a Float specifying the maximum distance from the
            projection point on a connected surface within which the nodes on that surface must lie
            to contribute to the motion of the projection point. If the value is DEFAULT, a radius
            is computed from the fastener diameter and the surface facet lengths. The default value
            is DEFAULT.
        searchRadius
            The SymbolicConstant DEFAULT or a Float specifying the distance from the positioning
            points within which the connected points must lie. The default value is DEFAULT.
        maximumLayers
            The SymbolicConstant ALL or an Int specifying the maximum number of layers for each
            fastener. If the value is ALL, the maximum possible number of layers within the
            searchRadius will be used for each fastener. The default value is ALL.
        coupling
            A SymbolicConstant specifying the coupling method used to couple the displacement and
            rotation of each attachment point to the average motion of the surface nodes within the
            radius of influence from the fastener projection point. Possible values are CONTINUUM
            and STRUCTURAL. The default value is CONTINUUM.
        weightingMethod
            A SymbolicConstant specifying the weighting scheme to be used to weight the contribution
            of the displacements of the surface nodes within the radius of influence to the motion
            of the fastener projection point. UNIFORM, LINEAR, QUADRATIC, and CUBIC indicate
            uniform, linear decreasing, quadratic polynomial decreasing, and cubic polynomial
            monotonic decreasing weight distributions. Possible values are UNIFORM, LINEAR,
            QUADRATIC, and CUBIC. The default value is UNIFORM.
        additionalMass
            A Float specifying the mass that will be distributed to fastener attachment points. The
            default value is 0.0.
        adjustOrientation
            A Boolean specifying whether to adjust localCsys such that the local z-axis for each
            fastener is normal to the surface that is closest to the reference node for that
            fastener. The default value is ON.
        localCsys
            None or a DatumCsys object specifying the local coordinate system. If **localCsys** = None,
            the global coordinate system is used. When this member is queried, it returns an Int.
            The default value is None.
        connectionType
            A SymbolicConstant specifying the fastener connection type. Possible values are
            CONNECTOR and BEAM_MPC. The default value is CONNECTOR.
        sectionName
            A String specifying the connector section assigned to generated connectors. The default
            value is an empty string.
        connectorOrientationLocalCsys1
            None or a DatumCsys object specifying the local coordinate system of the first connector
            point in generated connectors. If **connectorOrientationLocalCsys1** = None, the degrees of
            freedom are defined in the global coordinate system. When this member is queried, it
            returns an Int. The default value is None.
        axis1
            A SymbolicConstant specifying the axis of a datum coordinate system about which an
            additional rotation is applied for the first point in generated connectors. Possible
            values are AXIS_1, AXIS_2, and AXIS_3. The default value is AXIS_1.
        angle1
            A Float specifying the angle of the additional rotation for the first point in generated
            connectors. The default value is 0.0.
        orient2SameAs1
            A Boolean specifying whether or not the second connector point in generated connectors
            is to use the same local coordinate system, axis, and angle as the first point. The
            default value is ON.
        connectorOrientationLocalCsys2
            None or a DatumCsys object specifying the local coordinate system of the second
            connector point in generated connectors. If **connectorOrientationLocalCsys2** = None, the
            degrees of freedom are defined in the global coordinate system. When this member is
            queried, it returns an Int. The default value is None.
        axis2
            A SymbolicConstant specifying the axis of a datum coordinate system about which an
            additional rotation is applied for the second point in generated connectors. Possible
            values are AXIS_1, AXIS_2, and AXIS_3. The default value is AXIS_1.
        angle2
            A Float specifying the angle of the additional rotation for the second point in
            generated connectors. The default value is 0.0.
        unsorted
            A Boolean specifying whether the analysis product should leave targetSurfaces in the
            given unsorted order, or sort them by proximity to determine the connectivity of
            fastening points. The default value is OFF.

        Returns
        -------
        PointFastener
            A :py:class:`~abaqus.EngineeringFeature.PointFastener.PointFastener` object.
        """
        self.fasteners[name] = pointFastener = PointFastener(
            name,
            region,
            physicalRadius,
            directionVector,
            targetSurfaces,
            ur1,
            ur2,
            ur3,
            attachmentMethod,
            influenceRadius,
            searchRadius,
            maximumLayers,
            coupling,
            weightingMethod,
            additionalMass,
            adjustOrientation,
            localCsys,
            connectionType,
            sectionName,
            connectorOrientationLocalCsys1,
            axis1,
            angle1,
            orient2SameAs1,
            connectorOrientationLocalCsys2,
            axis2,
            angle2,
            unsorted,
        )
        return pointFastener

    @abaqus_method_doc
    def PointMassInertia(
        self,
        name: str,
        region: Region,
        mass: float = 0,
        mass1: float = 0,
        mass2: float = 0,
        mass3: float = 0,
        i11: float = 0,
        i22: float = 0,
        i33: float = 0,
        i12: float = 0,
        i13: float = 0,
        i23: float = 0,
        localCsys: Optional[str] = None,
        alpha: float = 0,
        composite: float = 0,
    ) -> PointMassInertia:
        """This method creates a PointMassInertia object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].parts[name].engineeringFeatures.PointMassInertia
                mdb.models[name].rootAssembly.engineeringFeatures.PointMassInertia

        Parameters
        ----------
        name
            A String specifying the repository key.
        region
            A :py:class:`~abaqus.Region.Region.Region` object specifying the region to which the mass or rotary inertia is applied.
        mass
            A Float specifying the mass magnitude for isotropic mass. This parameter cannot be
            specified when anisotropic mass terms are specified. The default value is 0.0.
        mass1
            A Float specifying the mass in the 1-direction for anisotropic mass. This parameter
            cannot be specified when isotropic mass is also specified. The default value is 0.0.
        mass2
            A Float specifying the mass in the 2-direction for anisotropic mass. This parameter
            cannot be specified when isotropic mass is also specified. The default value is 0.0.
        mass3
            A Float specifying the mass in the 3-direction for anisotropic mass. This parameter
            cannot be specified when isotropic mass is also specified. The default value is 0.0.
        i11
            A Float specifying the rotary inertia about the local 1-axis, I11I11. The default value
            is 0.0.
        i22
            A Float specifying the rotary inertia about the local 2-axis, I22I22. The default value
            is 0.0.
        i33
            A Float specifying the rotary inertia about the local 3-axis, I33I33. The default value
            is 0.0.
        i12
            A Float specifying the product of inertia, I12I12. The default value is 0.0.
        i13
            A Float specifying the product of inertia, I13I13. The default value is 0.0.
        i23
            A Float specifying the product of inertia, I23I23. The default value is 0.0.
        localCsys
            None or a DatumCsys object specifying the local coordinate system for the anisotropic
            mass terms (when specified), and the rotary inertia (when specified). If
            **localCsys** = None, the anisotropic mass and rotary inertia data are defined in the global
            coordinate system. The default value is None.
        alpha
            A Float specifying the alpha damping magnitude. The default value is 0.0.This argument
            applies only to Abaqus/Standard analyses.
        composite
            A Float specifying the composite damping magnitude. The default value is 0.0.This
            argument applies only to Abaqus/Standard analyses.

        Returns
        -------
        PointMassInertia
            A :py:class:`~abaqus.EngineeringFeature.PointMassInertia.PointMassInertia` object.
        """
        self.inertias[name] = pointMassInertia = PointMassInertia(
            name,
            region,
            mass,
            mass1,
            mass2,
            mass3,
            i11,
            i22,
            i33,
            i12,
            i13,
            i23,
            localCsys,
            alpha,
            composite,
        )
        return pointMassInertia

    @abaqus_method_doc
    def SpringDashpotToGround(
        self,
        name: str,
        region: Region,
        dof: int,
        orientation: Optional[str] = None,
        springBehavior: Boolean = OFF,
        dashpotBehavior: Boolean = OFF,
        springStiffness: float = 0,
        dashpotCoefficient: float = 0,
    ) -> SpringDashpotToGround:
        """This method creates a SpringDashpotToGround object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].parts[name].engineeringFeatures.SpringDashpotToGround
                mdb.models[name].rootAssembly.engineeringFeatures.SpringDashpotToGround
            
        Parameters
        ----------
        name
            A String specifying the repository key.
        region
            A :py:class:`~abaqus.Region.Region.Region` object specifying the region to which the springs and/or dashpots are applied.
        dof
            An Int specifying the degree of freedom associated with the spring and dashpot
            behaviors.
        orientation
            None or a DatumCsys object specifying the local directions for the spring and/or
            dashpot. If **orientation** = None, the spring and/or dashpot data are defined in the global
            coordinate system. The default value is None.
        springBehavior
            A Boolean specifying whether to apply spring behavior to the selected points. The
            default value is OFF.At least one of the arguments **springBehavior** = ON or
            **dashpotBehavior** = ON must be specified.
        dashpotBehavior
            A Boolean specifying whether to apply dashpot behavior to the selected points. The
            default value is OFF.At least one of the arguments **springBehavior** = ON or
            **dashpotBehavior** = ON must be specified.
        springStiffness
            A Float specifying the force per relative displacement for the spring. The default value
            is 0.0.
        dashpotCoefficient
            A Float specifying the force per relative velocity for the dashpot. The default value is
            0.0.

        Returns
        -------
        SpringDashpotToGround
            A :py:class:`~abaqus.EngineeringFeature.SpringDashpotToGround.SpringDashpotToGround` object.
        """
        self.springDashpots[name] = springDashpotToGround = SpringDashpotToGround(
            name,
            region,
            dof,
            orientation,
            springBehavior,
            dashpotBehavior,
            springStiffness,
            dashpotCoefficient,
        )
        return springDashpotToGround

    @abaqus_method_doc
    def TwoPointSpringDashpot(
        self,
        name: str,
        regionPairs: tuple,
        axis: SymbolicConstant,
        dof1: int = 0,
        dof2: int = 0,
        orientation: Optional[str] = None,
        springBehavior: Boolean = OFF,
        dashpotBehavior: Boolean = OFF,
        springStiffness: float = 0,
        dashpotCoefficient: float = 0,
    ) -> TwoPointSpringDashpot:
        """This method creates a TwoPointSpringDashpot object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].parts[name].engineeringFeatures.TwoPointSpringDashpot
                mdb.models[name].rootAssembly.engineeringFeatures.TwoPointSpringDashpot
            
        Parameters
        ----------
        name
            A String specifying the repository key.
        regionPairs
            A sequence of pairs of Region objects specifying the points between which the springs
            and/or dashpots are applied.
        axis
            A SymbolicConstant specifying whether the axis of the springs and/or dashpots follows
            the rotation of the nodes or is in a specified direction. Possible values are NODAL_LINE
            and FIXED_DOF.
        dof1
            An Int specifying the degree of freedom with which the springs and/or dashpots are
            associated at their first points. The **dof1** argument applies only when
            **axis** = FIXED_DOFS. The default value is 0.
        dof2
            An Int specifying the degree of freedom with which the springs and/or dashpots are
            associated at their second points. The **dof2** argument applies only when
            **axis** = FIXED_DOFS. The default value is 0.
        orientation
            None or a DatumCsys object specifying the local directions for the spring and/or
            dashpot. If **orientation** = None, the spring and/or dashpot data are defined in the global
            coordinate system. The default value is None.The **orientation** argument applies only
            when **axis** = FIXED_DOFS.
        springBehavior
            A Boolean specifying whether to apply spring behavior to the selected point pairs. The
            default value is OFF.At least one of the arguments **springBehavior** = ON or
            **dashpotBehavior** = ON must be specified.
        dashpotBehavior
            A Boolean specifying whether to apply dashpot behavior to the selected point pairs. The
            default value is OFF.At least one of the arguments **springBehavior** = ON or
            **dashpotBehavior** = ON must be specified.
        springStiffness
            A Float specifying the force per relative displacement for the springs. The default
            value is 0.0.
        dashpotCoefficient
            A Float specifying the force per relative velocity for the dashpots. The default value
            is 0.0.

        Returns
        -------
        TwoPointSpringDashpot
            A :py:class:`~abaqus.EngineeringFeature.TwoPointSpringDashpot.TwoPointSpringDashpot` object.
        """
        self.springDashpots[name] = twoPointSpringDashpot = TwoPointSpringDashpot(
            name,
            regionPairs,
            axis,
            dof1,
            dof2,
            orientation,
            springBehavior,
            dashpotBehavior,
            springStiffness,
            dashpotCoefficient,
        )
        return twoPointSpringDashpot

    @abaqus_method_doc
    def XFEMCrack(
        self,
        name: str,
        crackDomain: Region,
        allowCrackGrowth: Boolean = ON,
        crackLocation: Optional[Region] = None,
        singularityCalcRadius: Optional[float] = None,
        interactionProperty: str = "",
        elemId: tuple = (),
        nodeId: tuple = (),
        hasCrackFront: tuple = (),
        crackPlaneDist: tuple = (),
        crackFrontDist: tuple = (),
        autoDetectValue: str = "",
    ) -> XFEMCrack:
        """This method creates a XFEMCrack object. Although the constructor is available both for
        parts and for the assembly, XFEMCrack objects are currently supported only under the
        assembly.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].parts[name].engineeringFeatures.XFEMCrack
                mdb.models[name].rootAssembly.engineeringFeatures.XFEMCrack

        Parameters
        ----------
        name
            A String specifying the repository key.
        crackDomain
            A :py:class:`~abaqus.Region.Region.Region` object specifying the region that contains the crack or is likely to contain
            the crack.
        allowCrackGrowth
            A Boolean specifying whether the crack is allowed to propagate (grow). The default value
            is ON.
        crackLocation
            A :py:class:`~abaqus.Region.Region.Region` object specifying the initial crack location. This parameter is required when
            **allowCrackGrowth** = OFF.
        singularityCalcRadius
            None or a Float specifying the radius from the crack tips within which the elements are
            used for crack singularity calculations. This argument applies only when
            **allowCrackGrowth** = OFF. The default value is None.
        interactionProperty
            A String specifying the name of the ContactProperty object that defines the contact
            properties for the crack surfaces. The default value is an empty string.
        elemId
            A sequence of Ints specifying the labels of the elements that are intersected by the
            initial crack location. This argument is used only by the input file reader.
        nodeId
            A sequence of Ints specifying the position of a node in the corresponding element
            connectivity. This argument is used only by the input file reader.
        hasCrackFront
            A sequence of Ints specifying the values indicating the inclusion/exclusion of the
            **crackFrontDist** values. A zero value indicates that **crackFrontDist** is not specified
            for the ith pair **elemId** and **nodeId**. This argument is used only by the input file
            reader.
        crackPlaneDist
            A sequence of Floats specifying the values of the first signed distance function. This
            argument is used by the input file reader.
        crackFrontDist
            A sequence of Floats specifying the values of the second signed distance function. This
            argument is used only by the input file reader.
        autoDetectValue
            An integer specifying the number of element layers around the crack location, to which
            the crack domain is shrunk.

        Returns
        -------
        XFEMCrack
            A :py:class:`~abaqus.EngineeringFeature.XFEMCrack.XFEMCrack` object.
        """
        self.cracks[name] = xFEMCrack = XFEMCrack(
            name,
            crackDomain,
            allowCrackGrowth,
            crackLocation,
            singularityCalcRadius,
            interactionProperty,
            elemId,
            nodeId,
            hasCrackFront,
            crackPlaneDist,
            crackFrontDist,
            autoDetectValue,
        )
        return xFEMCrack
