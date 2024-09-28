# Abaqus API Changes

## Abaqus 2024

### {py:obj}`abaqus.XY.XYSessionBase`

- {py:obj}`abaqus.XY.XYSessionBase.XYSessionBase.linearizeStress`: *added*: Added in version 2024: The argument useMaxStressValue was added.

### {py:obj}`abaqus.BeamSectionProfile.BeamSectionProfileModel`

- {py:obj}`abaqus.BeamSectionProfile.BeamSectionProfileModel.BeamSectionProfileModel.ChannelProfile`: *added*: Added in version 2024: The ChannelProfile method was added.
- {py:obj}`abaqus.BeamSectionProfile.BeamSectionProfileModel.BeamSectionProfileModel.HatProfile`: *added*: Added in version 2024: The HatProfile method was added.

### {py:obj}`abaqus.BeamSectionProfile.BeamSectionProfileOdb`

- {py:obj}`abaqus.BeamSectionProfile.BeamSectionProfileOdb.BeamSectionProfileOdb.ChannelProfile`: *added*: Added in version 2024: The ChannelProfile method was added.
- {py:obj}`abaqus.BeamSectionProfile.BeamSectionProfileOdb.BeamSectionProfileOdb.HatProfile`: *added*: Added in version 2024: The HatProfile method was added.

### {py:obj}`abaqus.BeamSectionProfile.ChannelProfile`

- {py:obj}`abaqus.BeamSectionProfile.ChannelProfile.ChannelProfile`: *added*: Added in version 2024: The ChannelProfile class was added.

### {py:obj}`abaqus.Section.SectionModel`

- {py:obj}`abaqus.Section.SectionModel.SectionModel.BeamSection`: *added*: Added in version 2024: The argument beamSectionOffset was added.

### {py:obj}`abaqus.Section.SectionOdb`

- {py:obj}`abaqus.Section.SectionOdb.SectionOdb.BeamSection`: *added*: Added in version 2024: The argument beamSectionOffset was added.
- {py:obj}`abaqus.Section.SectionOdb.BeamSection.beamSectionOffset`: *added*: Added in version 2024: The attribute beamSectionOffset was added.
- {py:obj}`abaqus.Section.SectionOdb.BeamSection.setValues`: *added*: Added in version 2024: The argument beamSectionOffset was added.

### {py:obj}`abaqus.Step.StepModel`

- {py:obj}`abaqus.Step.StepModel.StepModel.StaticLinearPerturbationStep`: *added*: Added in version 2024: The argument solutionTechnique was added.
- {py:obj}`abaqus.Step.StepModel.StepModel.StaticLinearPerturbationStep`: *added*: Added in version 2024: The argument gapDistance was added.
- {py:obj}`abaqus.Step.StepModel.StepModel.StaticLinearPerturbationStep`: *added*: Added in version 2024: The argument scaleFactor was added.
- {py:obj}`abaqus.Step.StepModel.StaticLinearPerturbationStep.gapDistance`: *added*: Added in version 2024: The attribute gapDistance was added.
- {py:obj}`abaqus.Step.StepModel.StaticLinearPerturbationStep.scaleFactor`: *added*: Added in version 2024: The attribute scaleFactor was added.
- {py:obj}`abaqus.Step.StepModel.StaticLinearPerturbationStep.setValues`: *added*: Added in version 2024: The argument solutionTechnique was added.
- {py:obj}`abaqus.Step.StepModel.StaticLinearPerturbationStep.setValues`: *added*: Added in version 2024: The argument gapDistance was added.
- {py:obj}`abaqus.Step.StepModel.StaticLinearPerturbationStep.setValues`: *added*: Added in version 2024: The argument scaleFactor was added.
- {py:obj}`abaqus.Step.StepModel.StaticLinearPerturbationStep.solutionTechnique`: *added*: Added in version 2024: The attribute solutionTechnique was added.

### {py:obj}`abaqus.Job.JobMdb`

- {py:obj}`abaqus.Job.JobMdb.JobMdb.OptimizationProcess`: *added*: Added in version 2024: The argument licenseType was added.

### {py:obj}`abaqus.Job.OptimizationProcess`

- {py:obj}`abaqus.Job.OptimizationProcess.OptimizationProcess.licenseType`: *added*: Added in version 2024: The argument licenseType was added.

### {py:obj}`abaqus.Constraint.ConstraintModel`

- {py:obj}`abaqus.Constraint.ConstraintModel.ConstraintModel.Coupling`: *added*: Added in version 2024: The rotationalCouplingType argument was added.

### {py:obj}`abaqus.Constraint.Coupling`

- {py:obj}`abaqus.Constraint.Coupling.Coupling.rotationalCouplingType`: *added*: Added in version 2024: The rotationalCouplingType attribute was added.

### {py:obj}`abaqus.Interaction.InteractionModel`

- {py:obj}`abaqus.Interaction.InteractionModel.InteractionModel.ContactMassScalingExp`: *added*: Added in version 2024: The ContactMassScalingExp method was added.
- {py:obj}`abaqus.Interaction.InteractionModel.ContactMassScalingExp`: *added*: Added in version 2024: The ContactMassScalingExp class was added.

### {py:obj}`abaqus.Optimization.OptimizationTask`

- {py:obj}`abaqus.Optimization.OptimizationTask.OptimizationTask.SingleTermDesignResponse`: *changed*: Changed in version 2024: The argument stepOperation was removed.

### {py:obj}`abaqus.Optimization.SingleTermDesignResponse`

- {py:obj}`abaqus.Optimization.SingleTermDesignResponse.SingleTermDesignResponse`: *changed*: Changed in version 2024: The attribute stepOperation was removed.

### {py:obj}`abaqus.EngineeringFeature.EngineeringFeature`

- {py:obj}`abaqus.EngineeringFeature.EngineeringFeature.EngineeringFeature.DiscreteFastener`: *added*: Added in version 2024: The argument rotationalCoupling was added.
- {py:obj}`abaqus.EngineeringFeature.EngineeringFeature.DiscreteFastener.setValues`: *added*: Added in version 2024: The argument rotationalCoupling was added.


## Abaqus 2023

### {py:obj}`abaqus.Job.JobMdb`

- {py:obj}`abaqus.Job.JobMdb.JobMdb.Job`: *changed*: Changed in version 2023: The parallelizationMethodExplicit argument was removed.
- {py:obj}`abaqus.Job.JobMdb.JobMdb.Job`: *changed*: Changed in version 2023: The docs for this argument were updated to reflect that the parallelizationMethodExplicit argument was removed in 2023.
- {py:obj}`abaqus.Job.JobMdb.JobFromInputFile`: *changed*: Changed in version 2023: The parallelizationMethodExplicit attribute was removed.
- {py:obj}`abaqus.Job.JobMdb.JobFromInputFile.numDomains`: *changed*: Changed in version 2023: The docs for this argument were updated to reflect that the parallelizationMethodExplicit argument was removed in 2023.
- {py:obj}`abaqus.Job.JobMdb.JobFromInputFile.setValues`: *changed*: Changed in version 2023: The parallelizationMethodExplicit argument was removed.
- {py:obj}`abaqus.Job.JobMdb.JobFromInputFile.setValues`: *changed*: Changed in version 2023: The docs for this argument were updated to reflect that the parallelizationMethodExplicit argument was removed in 2023.
- {py:obj}`abaqus.Job.JobMdb.JobMdb.Job`: *changed*: Changed in version 2023: The parallelizationMethodExplicit argument was removed.
- {py:obj}`abaqus.Job.JobMdb.JobMdb.Job`: *changed*: Changed in version 2023: The docs for this argument were updated to reflect that the parallelizationMethodExplicit argument was removed in 2023.
- {py:obj}`abaqus.Job.JobMdb.JobMdb.JobFromInputFile`: *changed*: Changed in version 2023: The parallelizationMethodExplicit argument was removed.
- {py:obj}`abaqus.Job.JobMdb.JobMdb.JobFromInputFile`: *changed*: Changed in version 2023: The docs for this argument were updated to reflect that the parallelizationMethodExplicit argument was removed in 2023.

### {py:obj}`abaqus.Job.ModelJob`

- {py:obj}`abaqus.Job.ModelJob.ModelJob`: *changed*: Changed in version 2023: The parallelizationMethodExplicit attribute was removed.
- {py:obj}`abaqus.Job.ModelJob.ModelJob.numDomains`: *changed*: Changed in version 2023: The docs for this argument were updated to reflect that the parallelizationMethodExplicit argument was removed in 2023.

### {py:obj}`abaqus.Interaction.SurfaceFeatureAssignment`

- {py:obj}`abaqus.Interaction.SurfaceFeatureAssignment.SurfaceFeatureAssignment.appendInStep`: *added*: Added in version 2023: The useDynFeatEdge argument was added.
- {py:obj}`abaqus.Interaction.SurfaceFeatureAssignment.SurfaceFeatureAssignment.changeValuesInStep`: *added*: Added in version 2023: The useDynFeatEdge argument was added.

### {py:obj}`abaqus.Material.Material`

- {py:obj}`abaqus.Material.Material.Material.PlasticityCorrection`: *added*: Added in version 2023: The PlasticityCorrection method was added.

### {py:obj}`abaqus.Material.Plastic.PlasticityCorrection`

- {py:obj}`abaqus.Material.Plastic.PlasticityCorrection.PlasticityCorrection`: *added*: Added in version 2023: The PlasticityCorrection class was added.

### {py:obj}`abaqus.Optimization.OptimizationTask`

- {py:obj}`abaqus.Optimization.OptimizationTask.OptimizationTask.BeadFilter`: *added*: Added in version 2023.
- {py:obj}`abaqus.Optimization.OptimizationTask.BeadFilter`: *added*: Added in version 2023: The BeadFilter class was added.

### {py:obj}`abaqus.Optimization.TopologyRibDesign`

- {py:obj}`abaqus.Optimization.TopologyRibDesign.TopologyRibDesign`: *added*: Added in version 2023: The TopologyRibDesign class was added.

### {py:obj}`abaqus.Assembly.AssemblyBase`

- {py:obj}`abaqus.Assembly.AssemblyBase.AssemblyBase.getCoordinates`: *added*: Added in version 2023: The csys argument was added.
- {py:obj}`abaqus.Assembly.AssemblyBase.AssemblyBase.getDistance`: *changed*: Changed in version 2023: The csys argument was removed.

### {py:obj}`abaqus.EngineeringFeature.EngineeringFeature`

- {py:obj}`abaqus.EngineeringFeature.EngineeringFeature.DataImperfection`: *added*: Added in version 2023: The DataImperfection class was added.

### {py:obj}`abaqus.EngineeringFeature.InputImperfection`

- {py:obj}`abaqus.EngineeringFeature.InputImperfection.Imperfection`: *added*: Added in version 2023: The Imperfection class was added.
- {py:obj}`abaqus.EngineeringFeature.InputImperfection.InputImperfection`: *added*: Added in version 2023: The InputImperfection class was added.

### {py:obj}`abaqus.EngineeringFeature.FileImperfection`

- {py:obj}`abaqus.EngineeringFeature.FileImperfection.FileImperfection`: *added*: Added in version 2023: The FileImperfection class was added.


## Abaqus 2022

### {py:obj}`abaqus.FieldReport.FieldReportOptions`

- {py:obj}`abaqus.FieldReport.FieldReportOptions.FieldReportOptions.setValues`: *added*: Added in version 2022: The printLocalCSYS argument was added.

### {py:obj}`abaqus.Session.SessionBase`

- {py:obj}`abaqus.Session.SessionBase.SessionBase.printToFile`: *changed*: Changed in version 2022: It is "only" valid to use this argument ...

### {py:obj}`abaqus.Part.PartBase`

- {py:obj}`abaqus.Part.PartBase.PartBase.getCoordinates`: *added*: Added in version 2022: The csys argument was added.

### {py:obj}`abaqus.Connector.ConnectorSection`

- {py:obj}`abaqus.Connector.ConnectorSection.ConnectorSection.ConnectorDamping`: *added*: Added in version 2022: The type argument was added.
- {py:obj}`abaqus.Connector.ConnectorSection.ConnectorDamping.type`: *added*: Added in version 2022: The type attribute was added.

### {py:obj}`abaqus.Odb.RebarOrientation`

- {py:obj}`abaqus.Odb.RebarOrientation.OdbDatumCsys.globalToLocal`: *added*: Added in version 2022: The globalToLocal method was added.
- {py:obj}`abaqus.Odb.RebarOrientation.OdbDatumCsys.localToGlobal`: *added*: Added in version 2022: The localToGlobal method was added.

### {py:obj}`abaqus.Job.JobMdb`

- {py:obj}`abaqus.Job.JobMdb.JobMdb.Job`: *changed*: Changed in version 2022: The licenseType argument was added.
- {py:obj}`abaqus.Job.JobMdb.JobFromInputFile.licenseType`: *added*: Added in version 2022: The licenseType attribute was added.
- {py:obj}`abaqus.Job.JobMdb.JobMdb.Job`: *changed*: Changed in version 2022: The licenseType argument was added.

### {py:obj}`abaqus.Job.Coexecution`

- {py:obj}`abaqus.Job.Coexecution.Coexecution.licenseType`: *added*: Added in version 2022: The licenseType attribute was added.
- {py:obj}`abaqus.Job.Coexecution.Coexecution.mainAnalysisProduct`: *changed*: Changed in version 2022: The masterAnalysisProduct attribute was changed to mainAnalysisProduct.
- {py:obj}`abaqus.Job.Coexecution.Coexecution.mainModel`: *changed*: Changed in version 2022: The masterModel attribute was changed to mainModel.
- {py:obj}`abaqus.Job.Coexecution.Coexecution.secondaryAnalysisProducts`: *changed*: Changed in version 2022: The slaveAnalysisProducts attribute was changed to secondaryAnalysisProducts.
- {py:obj}`abaqus.Job.Coexecution.Coexecution.secondaryModels`: *changed*: Changed in version 2022: The slaveModels attribute was changed to secondaryModels.

### {py:obj}`abaqus.Constraint.ConstraintModel`

- {py:obj}`abaqus.Constraint.ConstraintModel.ConstraintModel.Coupling`: *added*: Added in version 2022: The alpha argument was added.
- {py:obj}`abaqus.Constraint.ConstraintModel.ConstraintModel.Tie`: *changed*: Changed in version 2022: The master argument was renamed to main.
- {py:obj}`abaqus.Constraint.ConstraintModel.ConstraintModel.Tie`: *changed*: Changed in version 2022: The slave argument was renamed to secondary.

### {py:obj}`abaqus.Constraint.Coupling`

- {py:obj}`abaqus.Constraint.Coupling.Coupling.alpha`: *added*: Added in version 2022: The alpha attribute was added.

### {py:obj}`abaqus.Constraint.Tie`

- {py:obj}`abaqus.Constraint.Tie.Tie.main`: *changed*: Changed in version 2022: The master attribute was renamed to main.
- {py:obj}`abaqus.Constraint.Tie.Tie.secondary`: *changed*: Changed in version 2022: The slave attribute was renamed to secondary.

### {py:obj}`abaqus.Interaction.InteractionModel`

- {py:obj}`abaqus.Interaction.InteractionModel.InteractionModel.ContactExp`: *changed*: Changed in version 2022: The argument masterSlaveAssignments was renamed to mainSecondaryAssignments.
- {py:obj}`abaqus.Interaction.InteractionModel.InteractionModel.ContactStd`: *changed*: Changed in version 2022: The argument masterSlaveAssignments was renamed to mainSecondaryAssignments.
- {py:obj}`abaqus.Interaction.InteractionModel.InteractionModel.CyclicSymmetry`: *changed*: Changed in version 2022: The argument master was renamed to main.
- {py:obj}`abaqus.Interaction.InteractionModel.InteractionModel.CyclicSymmetry`: *changed*: Changed in version 2022: The argument slave was renamed to secondary.
- {py:obj}`abaqus.Interaction.InteractionModel.InteractionModel.PressurePenetration`: *changed*: Changed in version 2022: The argument masterPoints was renamed to mainPoints.
- {py:obj}`abaqus.Interaction.InteractionModel.InteractionModel.PressurePenetration`: *changed*: Changed in version 2022: The argument slavePoints was renamed to secondaryPoints.
- {py:obj}`abaqus.Interaction.InteractionModel.InteractionModel.SelfContactStd`: *changed*: Changed in version 2022: Rigid master surfaces was changed to rigid main surfaces.
- {py:obj}`abaqus.Interaction.InteractionModel.InteractionModel.SurfaceToSurfaceContactExp`: *changed*: Changed in version 2022: The argument master was renamed to main.
- {py:obj}`abaqus.Interaction.InteractionModel.InteractionModel.SurfaceToSurfaceContactExp`: *changed*: Changed in version 2022: The argument slave was renamed to secondary.
- {py:obj}`abaqus.Interaction.InteractionModel.InteractionModel.contactDetection`: *changed*: Changed in version 2022: The argument createUnionOfMasterSurfaces was renamed to createUnionOfMainSurfaces.
- {py:obj}`abaqus.Interaction.InteractionModel.InteractionModel.contactDetection`: *changed*: Changed in version 2022: The argument createUnionOfSlaveSurfaces was renamed to createUnionOfSecondarySurfaces.
- {py:obj}`abaqus.Interaction.InteractionModel.InteractionModel.contactDetection`: *changed*: Changed in version 2022: The argument createUnionOfMasterSlaveSurfaces was renamed to createUnionOfMainSecondarySurfaces.
- {py:obj}`abaqus.Interaction.InteractionModel.ContactExp.mainSecondaryAssignments`: *changed*: Changed in version 2022: The attribute masterSlaveAssignments was renamed to mainSecondaryAssignments.
- {py:obj}`abaqus.Interaction.InteractionModel.ContactStd.mainSecondaryAssignments`: *changed*: Changed in version 2022: The attribute masterSlaveAssignments was renamed to mainSecondaryAssignments.
- {py:obj}`abaqus.Interaction.InteractionModel.CyclicSymmetry.main`: *changed*: Changed in version 2022: The attribute master was renamed to main.
- {py:obj}`abaqus.Interaction.InteractionModel.CyclicSymmetry.secondary`: *changed*: Changed in version 2022: The attribute slave was renamed to secondary.

### {py:obj}`abaqus.Interaction.InteractionContactControlModel`

- {py:obj}`abaqus.Interaction.InteractionContactControlModel.InteractionContactControlModel.StdContactControl`: *changed*: Changed in version 2022: Slave node was changed to secondary node.

### {py:obj}`abaqus.Interaction.InteractionContactInitializationModel`

- {py:obj}`abaqus.Interaction.InteractionContactInitializationModel.InteractionContactInitializationModel.ExpInitialization`: *changed*: Changed in version 2022: The argument slaveNodesetName was renamed to secondaryNodesetName.
- {py:obj}`abaqus.Interaction.InteractionContactInitializationModel.ExpInitialization.secondaryNodesetName`: *changed*: Changed in version 2022: The attribute slaveNodesetName was renamed to secondaryNodesetName.
- {py:obj}`abaqus.Interaction.InteractionContactInitializationModel.ExpInitialization.setValues`: *changed*: Changed in version 2022: The argument slaveNodesetName was renamed to secondaryNodesetName.

### {py:obj}`abaqus.Interaction.InteractionPropertyModel`

- {py:obj}`abaqus.Interaction.InteractionPropertyModel.ContactProperty.HeatGeneration`: *changed*: Changed in version 2022: The argument slaveFraction was renamed to secondaryFraction.
- {py:obj}`abaqus.Interaction.InteractionPropertyModel.ContactProperty.Radiation`: *changed*: Changed in version 2022: The argument masterEmissivity was renamed to mainEmissivity.
- {py:obj}`abaqus.Interaction.InteractionPropertyModel.ContactProperty.Radiation`: *changed*: Changed in version 2022: The argument slaveEmissivity was renamed to secondaryEmissivity.

### {py:obj}`abaqus.Interaction.MainSecondaryAssignment`

- {py:obj}`abaqus.Interaction.MainSecondaryAssignment.MainSecondaryAssignment`: *changed*: Changed in version 2022: The MasterSlaveAssignment class was renamed to MainSecondaryAssignment.

### {py:obj}`abaqus.Interaction.PolarityAssignments`

- {py:obj}`abaqus.Interaction.PolarityAssignments.PolarityAssignments.changeValuesInStep`: *changed*: Changed in version 2022: Master-slave was changed to main-secondary.

### {py:obj}`abaqus.Interaction.GapHeatGeneration`

- {py:obj}`abaqus.Interaction.GapHeatGeneration.GapHeatGeneration.secondaryFraction`: *changed*: Changed in version 2022: The attribute slaveFraction was renamed to secondaryFraction.

### {py:obj}`abaqus.Interaction.Radiation`

- {py:obj}`abaqus.Interaction.Radiation.Radiation.mainEmissivity`: *changed*: Changed in version 2022: The attribute masterEmissivity was renamed to mainEmissivity.
- {py:obj}`abaqus.Interaction.Radiation.Radiation.secondaryEmissivity`: *changed*: Changed in version 2022: The attribute slaveEmissivity was renamed to secondaryEmissivity.

### {py:obj}`abaqus.Interaction.StdContactControl`

- {py:obj}`abaqus.Interaction.StdContactControl.StdContactControl.setValues`: *changed*: Changed in version 2022: Slave node was changed to secondary node.
- {py:obj}`abaqus.Interaction.StdContactControl.StdContactControl.uerrmx`: *changed*: Changed in version 2022: Slave node was changed to secondary node.

### {py:obj}`abaqus.Interaction.PressurePenetration`

- {py:obj}`abaqus.Interaction.PressurePenetration.PressurePenetration.mainPoints`: *changed*: Changed in version 2022: The attribute masterPoints was renamed to mainPoints.
- {py:obj}`abaqus.Interaction.PressurePenetration.PressurePenetration.secondaryPoints`: *changed*: Changed in version 2022: The attribute slavePoints was renamed to secondaryPoints.

### {py:obj}`abaqus.Interaction.SelfContactStd`

- {py:obj}`abaqus.Interaction.SelfContactStd.SelfContactStd.smooth`: *changed*: Changed in version 2022: Rigid master surfaces was changed to rigid main surfaces.

### {py:obj}`abaqus.Interaction.SurfaceToSurfaceContactExp`

- {py:obj}`abaqus.Interaction.SurfaceToSurfaceContactExp.SurfaceToSurfaceContactExp.main`: *changed*: Changed in version 2022: The attribute master was renamed to main.
- {py:obj}`abaqus.Interaction.SurfaceToSurfaceContactExp.SurfaceToSurfaceContactExp.secondary`: *changed*: Changed in version 2022: The attribute slave was renamed to secondary.
- {py:obj}`abaqus.Interaction.SurfaceToSurfaceContactExp.SurfaceToSurfaceContactExp.swapSurfaces`: *changed*: Changed in version 2022: Master and slave were changed to main and secondary.

### {py:obj}`abaqus.Interaction.SurfaceToSurfaceContactStd`

- {py:obj}`abaqus.Interaction.SurfaceToSurfaceContactStd.SurfaceToSurfaceContactStd.swapSurfaces`: *changed*: Changed in version 2022: Master and slave were changed to main and secondary.

### {py:obj}`abaqus.Material.Material`

- {py:obj}`abaqus.Material.Material.Material.CrushStress`: *added*: Added in version 2022: The CrushStress method was added.
- {py:obj}`abaqus.Material.Material.Material.Elastic`: *added*: Added in version 2022: The option BILAMINA was added.
- {py:obj}`abaqus.Material.Material.Material.Plastic`: *added*: Added in version 2022: The extrapolation argument was added.

### {py:obj}`abaqus.Material.Plastic.CrushStress.CrushStress`

- {py:obj}`abaqus.Material.Plastic.CrushStress.CrushStress.CrushStress`: *added*: Added in version 2022: The CrushStress class was added.

### {py:obj}`abaqus.Material.MaterialBase`

- {py:obj}`abaqus.Material.MaterialBase.MaterialBase.crushStress`: *added*: Added in version 2022: The crushStress attribute was added.

### {py:obj}`abaqus.Material.Plastic.CrushStress.CrushStressVelocityFactor`

- {py:obj}`abaqus.Material.Plastic.CrushStress.CrushStressVelocityFactor.CrushStressVelocityFactor`: *added*: Added in version 2022: The CrushStressVelocityFactor class was added.

### {py:obj}`abaqus.Mesh.MeshPart`

- {py:obj}`abaqus.Mesh.MeshPart.ElemType.initialGapOpening`: *added*: Added in version 2022: The initialGapOpening attribute was added.
- {py:obj}`abaqus.Mesh.MeshPart.ElemType.linearKinematicCtrl`: *added*: Added in version 2022: The linearKinematicCtrl attribute was added.

### {py:obj}`abaqus.Optimization.OptimizationTaskModel`

- {py:obj}`abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.BeadTask`: *added*: Added in version 2022: The groupOperator argument was added.
- {py:obj}`abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask`: *added*: Added in version 2022: The groupOperator argument was added.
- {py:obj}`abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.SizingTask`: *added*: Added in version 2022: The groupOperator argument was added.
- {py:obj}`abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.TopologyTask`: *added*: Added in version 2022: The groupOperator argument was added.
- {py:obj}`abaqus.Optimization.OptimizationTaskModel.BeadTask.groupOperator`: *added*: Added in version 2022: The groupSensitivities attribute was added.
- {py:obj}`abaqus.Optimization.OptimizationTaskModel.BeadTask.setValues`: *added*: Added in version 2022: The groupOperator argument was added.

### {py:obj}`abaqus.Optimization.OptimizationTask`

- {py:obj}`abaqus.Optimization.OptimizationTask.OptimizationTask.DesignDirection`: *changed*: Changed in version 2022: The argument masterPoint was renamed to mainPoint.
- {py:obj}`abaqus.Optimization.OptimizationTask.OptimizationTask.DesignDirection`: *changed*: Changed in version 2022: The argument masterPointDetermination was renamed to mainPointDetermination.
- {py:obj}`abaqus.Optimization.OptimizationTask.OptimizationTask.DrillControl`: *changed*: Changed in version 2022: The argument masterPoint was renamed to mainPoint.
- {py:obj}`abaqus.Optimization.OptimizationTask.OptimizationTask.DrillControl`: *changed*: Changed in version 2022: The argument masterPointDetermination was renamed to mainPointDetermination.
- {py:obj}`abaqus.Optimization.OptimizationTask.OptimizationTask.ShapeDemoldControl`: *changed*: Changed in version 2022: The argument masterPointDetermination was renamed to mainPointDetermination.
- {py:obj}`abaqus.Optimization.OptimizationTask.OptimizationTask.ShapeMemberSize`: *added*: Added in version 2022: The assignNodeGroupRegion argument was added.
- {py:obj}`abaqus.Optimization.OptimizationTask.OptimizationTask.ShapeMemberSize`: *added*: Added in version 2022: The nodeGroupRegion argument was added.
- {py:obj}`abaqus.Optimization.OptimizationTask.OptimizationTask.ShapePlanarSymmetry`: *changed*: Changed in version 2022: The argument masterPointDetermination was renamed to mainPointDetermination.
- {py:obj}`abaqus.Optimization.OptimizationTask.OptimizationTask.ShapePointSymmetry`: *changed*: Changed in version 2022: The argument masterPointDetermination was renamed to mainPointDetermination.
- {py:obj}`abaqus.Optimization.OptimizationTask.OptimizationTask.ShapeRotationalSymmetry`: *changed*: Changed in version 2022: The argument masterPoint was renamed to mainPoint.
- {py:obj}`abaqus.Optimization.OptimizationTask.OptimizationTask.ShapeRotationalSymmetry`: *changed*: Changed in version 2022: The argument masterPointDetermination was renamed to mainPointDetermination.
- {py:obj}`abaqus.Optimization.OptimizationTask.OptimizationTask.StampControl`: *changed*: Changed in version 2022: The argument masterPoint was renamed to mainPoint.
- {py:obj}`abaqus.Optimization.OptimizationTask.OptimizationTask.StampControl`: *changed*: Changed in version 2022: The argument masterPointDetermination was renamed to mainPointDetermination.
- {py:obj}`abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyMillingControl`: *added*: Added in version 2022: The TopologyMillingControl method was added.
- {py:obj}`abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyRibDesign`: *added*: Added in version 2022: The TopologyRibDesign method was added.
- {py:obj}`abaqus.Optimization.OptimizationTask.OptimizationTask.TurnControl`: *changed*: Changed in version 2022: The argument masterPoint was renamed to mainPoint.
- {py:obj}`abaqus.Optimization.OptimizationTask.OptimizationTask.TurnControl`: *changed*: Changed in version 2022: The argument masterPointDetermination was renamed to mainPointDetermination.
- {py:obj}`abaqus.Optimization.OptimizationTask.DesignDirection.mainPoint`: *changed*: Changed in version 2022: The attribute masterPoint was renamed to mainPoint.
- {py:obj}`abaqus.Optimization.OptimizationTask.DesignDirection.mainPointDetermination`: *changed*: Changed in version 2022: The attribute masterPointDetermination was renamed to mainPointDetermination.
- {py:obj}`abaqus.Optimization.OptimizationTask.DesignDirection.setValues`: *changed*: Changed in version 2022: The argument masterPoint was renamed to mainPoint.
- {py:obj}`abaqus.Optimization.OptimizationTask.DesignDirection.setValues`: *changed*: Changed in version 2022: The argument masterPointDetermination was renamed to mainPointDetermination.
- {py:obj}`abaqus.Optimization.OptimizationTask.DrillControl.mainPoint`: *changed*: Changed in version 2022: The attribute masterPoint was renamed to mainPoint.
- {py:obj}`abaqus.Optimization.OptimizationTask.DrillControl.mainPointDetermination`: *changed*: Changed in version 2022: The attribute masterPointDetermination was renamed to mainPointDetermination.
- {py:obj}`abaqus.Optimization.OptimizationTask.DrillControl.setValues`: *changed*: Changed in version 2022: The argument masterPoint was renamed to mainPoint.
- {py:obj}`abaqus.Optimization.OptimizationTask.DrillControl.setValues`: *changed*: Changed in version 2022: The argument masterPointDetermination was renamed to mainPointDetermination.

### {py:obj}`abaqus.Optimization.ShapeDemoldControl`

- {py:obj}`abaqus.Optimization.ShapeDemoldControl.ShapeDemoldControl.mainPointDetermination`: *changed*: Changed in version 2022: The attribute masterPointDetermination was renamed to mainPointDetermination.
- {py:obj}`abaqus.Optimization.ShapeDemoldControl.ShapeDemoldControl.setValues`: *changed*: Changed in version 2022: The argument masterPointDetermination was renamed to mainPointDetermination.

### {py:obj}`abaqus.Optimization.ShapeMemberSize`

- {py:obj}`abaqus.Optimization.ShapeMemberSize.ShapeMemberSize.assignNodeGroupRegion`: *added*: Added in version 2022: The assignNodeGroupRegion attribute was added.
- {py:obj}`abaqus.Optimization.ShapeMemberSize.ShapeMemberSize.nodeGroupRegion`: *added*: Added in version 2022: The nodeGroupRegion attribute was added.
- {py:obj}`abaqus.Optimization.ShapeMemberSize.ShapeMemberSize.setValues`: *added*: Added in version 2022: The assignNodeGroupRegion argument was added.
- {py:obj}`abaqus.Optimization.ShapeMemberSize.ShapeMemberSize.setValues`: *added*: Added in version 2022: The nodeGroupRegion argument was added.

### {py:obj}`abaqus.Optimization.ShapePointSymmetry`

- {py:obj}`abaqus.Optimization.ShapePointSymmetry.ShapePointSymmetry.mainPointDetermination`: *changed*: Changed in version 2022: The attribute masterPointDetermination was renamed to mainPointDetermination.
- {py:obj}`abaqus.Optimization.ShapePointSymmetry.ShapePointSymmetry.setValues`: *changed*: Changed in version 2022: The argument masterPointDetermination was renamed to mainPointDetermination.

### {py:obj}`abaqus.Optimization.ShapeRotationalSymmetry`

- {py:obj}`abaqus.Optimization.ShapeRotationalSymmetry.ShapeRotationalSymmetry.mainPoint`: *changed*: Changed in version 2022: The attribute masterPoint was renamed to mainPoint.
- {py:obj}`abaqus.Optimization.ShapeRotationalSymmetry.ShapeRotationalSymmetry.mainPointDetermination`: *changed*: Changed in version 2022: The attribute masterPointDetermination was renamed to mainPointDetermination.
- {py:obj}`abaqus.Optimization.ShapeRotationalSymmetry.ShapeRotationalSymmetry.setValues`: *changed*: Changed in version 2022: The argument masterPoint was renamed to mainPoint.
- {py:obj}`abaqus.Optimization.ShapeRotationalSymmetry.ShapeRotationalSymmetry.setValues`: *changed*: Changed in version 2022: The argument masterPointDetermination was renamed to mainPointDetermination.

### {py:obj}`abaqus.Optimization.StampControl`

- {py:obj}`abaqus.Optimization.StampControl.StampControl.mainPoint`: *changed*: Changed in version 2022: The attribute masterPoint was renamed to mainPoint.
- {py:obj}`abaqus.Optimization.StampControl.StampControl.mainPointDetermination`: *changed*: Changed in version 2022: The attribute masterPointDetermination was renamed to mainPointDetermination.
- {py:obj}`abaqus.Optimization.StampControl.StampControl.setValues`: *changed*: Changed in version 2022: The argument masterPoint was renamed to mainPoint.
- {py:obj}`abaqus.Optimization.StampControl.StampControl.setValues`: *changed*: Changed in version 2022: The argument masterPointDetermination was renamed to mainPointDetermination.

### {py:obj}`abaqus.Optimization.TopologyMillingControl`

- {py:obj}`abaqus.Optimization.TopologyMillingControl.TopologyMillingControl`: *added*: Added in version 2022: The TopologyMillingControl class was added.

### {py:obj}`abaqus.Optimization.TurnControl`

- {py:obj}`abaqus.Optimization.TurnControl.TurnControl.mainPoint`: *changed*: Changed in version 2022: The attribute masterPoint was renamed to mainPoint.
- {py:obj}`abaqus.Optimization.TurnControl.TurnControl.mainPointDetermination`: *changed*: Changed in version 2022: The attribute masterPointDetermination was renamed to mainPointDetermination.
- {py:obj}`abaqus.Optimization.TurnControl.TurnControl.setValues`: *changed*: Changed in version 2022: The argument masterPointDetermination was renamed to mainPointDetermination.

### {py:obj}`abaqus.Optimization.ShapeTask`

- {py:obj}`abaqus.Optimization.ShapeTask.ShapeTask.groupOperator`: *added*: Added in version 2022: The groupSensitivities attribute was added.
- {py:obj}`abaqus.Optimization.ShapeTask.ShapeTask.setValues`: *added*: Added in version 2022: The groupOperator argument was added.

### {py:obj}`abaqus.Optimization.SizingTask`

- {py:obj}`abaqus.Optimization.SizingTask.SizingTask.groupOperator`: *added*: Added in version 2022: The groupSensitivities attribute was added.
- {py:obj}`abaqus.Optimization.SizingTask.SizingTask.setValues`: *added*: Added in version 2022: The groupOperator argument was added.

### {py:obj}`abaqus.Optimization.TopologyTask`

- {py:obj}`abaqus.Optimization.TopologyTask.TopologyTask.groupOperator`: *added*: Added in version 2022: The groupSensitivities attribute was added.
- {py:obj}`abaqus.Optimization.TopologyTask.TopologyTask.setValues`: *added*: Added in version 2022: The groupOperator argument was added.

### {py:obj}`abaqus.StepOutput.OutputModel`

- {py:obj}`abaqus.StepOutput.OutputModel.FieldOutputRequest.setValuesInStep`: *changed*: Changed in version 2022: The argument timePoints was renamed to timePoint.

### {py:obj}`abaqus.Datum.DatumCsys`

- {py:obj}`abaqus.Datum.DatumCsys.DatumCsys.globalToLocal`: *added*: Added in version 2022: The globalToLocal method was added.
- {py:obj}`abaqus.Datum.DatumCsys.DatumCsys.localToGlobal`: *added*: Added in version 2022: The localToGlobal method was added.


## Abaqus 2021

### {py:obj}`abaqus.BoundaryCondition.BoundaryConditionModel`

- {py:obj}`abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.SubmodelBC`: *added*: Added in version 2021: The intersectionOnly argument was added.

### {py:obj}`abaqus.Interaction.InteractionModel`

- {py:obj}`abaqus.Interaction.InteractionModel.InteractionModel.ContactExp`: *added*: Added in version 2021: The surfaceCrushTriggerAssignments argument was added.
- {py:obj}`abaqus.Interaction.InteractionModel.InteractionModel.ContactExp`: *added*: Added in version 2021: The surfaceFrictionAssignments argument was added.
- {py:obj}`abaqus.Interaction.InteractionModel.InteractionModel.ContactStd`: *added*: Added in version 2021: The surfaceBeamSmoothingAssignments argument was added.
- {py:obj}`abaqus.Interaction.InteractionModel.InteractionModel.ContactStd`: *added*: Added in version 2021: The surfaceVertexCriteriaAssignments argument was added.
- {py:obj}`abaqus.Interaction.InteractionModel.InteractionModel.ContactStd`: *added*: Added in version 2021: The slidingFormulationAssignments argument was added.
- {py:obj}`abaqus.Interaction.InteractionModel.ContactPropertyAssignment.appendInStep`: *changed*: Changed in version 2021: Update descriptions of the three entries in the tuple.
- {py:obj}`abaqus.Interaction.InteractionModel.ContactPropertyAssignment.delete`: *changed*: Changed in version 2021: Update descriptions of the two entries in the tuple.

### {py:obj}`abaqus.Interaction.SurfaceCrushTriggerAssignment`

- {py:obj}`abaqus.Interaction.SurfaceCrushTriggerAssignment.SurfaceCrushTriggerAssignment`: *added*: Added in version 2021: The SurfaceCrushTriggerAssignment class was added.

### {py:obj}`abaqus.Interaction.SurfaceFrictionAssignment`

- {py:obj}`abaqus.Interaction.SurfaceFrictionAssignment.SurfaceFrictionAssignment`: *added*: Added in version 2021: The SurfaceFrictionAssignment class was added.

### {py:obj}`abaqus.Interaction.SurfaceOffsetAssignment`

- {py:obj}`abaqus.Interaction.SurfaceOffsetAssignment.SurfaceOffsetAssignment.appendInStep`: *changed*: Changed in version 2021: The first entry in the tuple can be a material object now.

### {py:obj}`abaqus.Interaction.SurfaceThicknessAssignment`

- {py:obj}`abaqus.Interaction.SurfaceThicknessAssignment.SurfaceThicknessAssignment.appendInStep`: *changed*: Changed in version 2021: The first entry in the tuple can be a material object now.

### {py:obj}`abaqus.Interaction.SlidingFormulationAssignment`

- {py:obj}`abaqus.Interaction.SlidingFormulationAssignment.SlidingFormulationAssignment`: *added*: Added in version 2021: The SlidingFormulationAssignment class was added.

### {py:obj}`abaqus.Interaction.SurfaceBeamSmoothingAssignment`

- {py:obj}`abaqus.Interaction.SurfaceBeamSmoothingAssignment.SurfaceBeamSmoothingAssignment`: *added*: Added in version 2021: The SurfaceBeamSmoothingAssignment class was added.

### {py:obj}`abaqus.Interaction.SurfaceVertexCriteriaAssignment`

- {py:obj}`abaqus.Interaction.SurfaceVertexCriteriaAssignment.SurfaceVertexCriteriaAssignment`: *added*: Added in version 2021: The SurfaceVertexCriteriaAssignment class was added.

### {py:obj}`abaqus.Material.Material`

- {py:obj}`abaqus.Material.Material.Material.GapConductance`: *added*: Added in version 2021: The GapConductance method was added.
- {py:obj}`abaqus.Material.Material.Material.GapConvection`: *added*: Added in version 2021: The GapConvection method was added.
- {py:obj}`abaqus.Material.Material.Material.GapRadiation`: *added*: Added in version 2021: The GapRadiation method was added.
- {py:obj}`abaqus.Material.Material.GapConductance`: *added*: Added in version 2021: The GapConductance class was added.
- {py:obj}`abaqus.Material.Material.GapConvection`: *added*: Added in version 2021: The GapConvection class was added.
- {py:obj}`abaqus.Material.Material.GapRadiation`: *added*: Added in version 2021: The GapRadiation class was added.

### {py:obj}`abaqus.Optimization.OptimizationTask`

- {py:obj}`abaqus.Optimization.OptimizationTask.OptimizationTask.ShapePlanarSymmetry`: *added*: Added in version 2021: The alloowNonSymmetricMesh argument was added.
- {py:obj}`abaqus.Optimization.OptimizationTask.OptimizationTask.ShapeRotationalSymmetry`: *added*: Added in version 2021: The alloowNonSymmetricMesh argument was added.

### {py:obj}`abaqus.Optimization.ShapePlanarSymmetry`

- {py:obj}`abaqus.Optimization.ShapePlanarSymmetry.ShapePlanarSymmetry.allowNonSymmetricMesh`: *added*: Added in version 2021: The allowNonSymmetricMesh attribute was added.

### {py:obj}`abaqus.Optimization.ShapeRotationalSymmetry`

- {py:obj}`abaqus.Optimization.ShapeRotationalSymmetry.ShapeRotationalSymmetry.allowNonSymmetricMesh`: *added*: Added in version 2021: The allowNonSymmetricMesh attribute was added.


## Abaqus 2020

### {py:obj}`abaqus.Part.PartBase`

- {py:obj}`abaqus.Part.PartBase.AcisFile.openSolidworks`: *added*: Added in version 2020: The openSolidworks method was added.

### {py:obj}`abaqus.Part.AcisMdb`

- {py:obj}`abaqus.Part.AcisMdb.AcisMdb.openSolidworks`: *added*: Added in version 2020: The openSolidworks method was added.

### {py:obj}`abaqus.Odb.RebarOrientation`

- {py:obj}`abaqus.Odb.RebarOrientation.OdbSet.instances`: *added*: Added in version 2020: The instances attribute was added.
- {py:obj}`abaqus.Odb.RebarOrientation.OdbSet.isInternal`: *added*: Added in version 2020: The isInternal attribute was added.

### {py:obj}`abaqus.Canvas.ViewportBase`

- {py:obj}`abaqus.Canvas.ViewportBase.ViewportBase.animationController`: *added*: Added in version 2020: The animationController attribute was added.

### {py:obj}`abaqus.Model.ModelBase`

- {py:obj}`abaqus.Model.ModelBase.ModelBase.eventSeriesDatas`: *added*: Added in version 2020: The eventSeriesDatas attribute was added.
- {py:obj}`abaqus.Model.ModelBase.ModelBase.eventSeriesTypes`: *added*: Added in version 2020: The eventSeriesTypes attribute was added.
- {py:obj}`abaqus.Model.ModelBase.ModelBase.tableCollections`: *added*: Added in version 2020: The tableCollections attribute was added.

### {py:obj}`abaqus.Interaction.InteractionModel`

- {py:obj}`abaqus.Interaction.InteractionModel.InteractionModel.ContactExp`: *added*: Added in version 2020: The polarityAssignments argument was added.
- {py:obj}`abaqus.Interaction.InteractionModel.ContactExp.polarityAssignments`: *added*: Added in version 2020: The polarityAssignments attribute was added.

### {py:obj}`abaqus.Interaction.InteractionContactInitializationModel`

- {py:obj}`abaqus.Interaction.InteractionContactInitializationModel.InteractionContactInitializationModel.StdInitialization`: *added*: Added in version 2020: The ExpInitialization method was added.
- {py:obj}`abaqus.Interaction.InteractionContactInitializationModel.ExpInitialization`: *added*: Added in version 2020: The ExpInitialization class was added.

### {py:obj}`abaqus.Material.Material`

- {py:obj}`abaqus.Material.Material.Material.Creep`: *added*: Added in version 2020: The options ANAND, DARVEAUX, DOUBLE_POWER, POWER_LAW, and TIME_POWER_LAW were added.
- {py:obj}`abaqus.Material.Material.Material.GapFlow`: *added*: Added in version 2020: The options BINGHAM_PLASTIC and HERSCHEL-BULKLEY were added.
- {py:obj}`abaqus.Material.Material.Material.Viscous`: *added*: Added in version 2020: The options ANAND, DARVEAUX, DOUBLE_POWER, POWER_LAW, and TIME_POWER_LAW were added.

### {py:obj}`abaqus.Material.Plastic.TensileFailure`

- {py:obj}`abaqus.Material.Plastic.TensileFailure.TensileFailure`: *added*: Added in version 2020: The TensileFailure class was added.

### {py:obj}`abaqus.Assembly.AssemblyBase`

- {py:obj}`abaqus.Assembly.AssemblyBase.AssemblyBase.smoothNodes`: *changed*: Changed in version 2020: The coordinates arguments was removed, the nodes now replaces it.

### {py:obj}`abaqus.TableCollection.TableCollectionAssembly`

- {py:obj}`abaqus.TableCollection.TableCollectionAssembly.TableCollectionAssembly`: *added*: Added in version 2020: The TableCollectionAssembly class was added.
- {py:obj}`abaqus.TableCollection.TableCollectionAssembly.ElementProgressiveActivation`: *added*: Added in version 2020: The ElementProgressiveActivation class was added.

### {py:obj}`abaqus.TableCollection.TableCollectionModel`

- {py:obj}`abaqus.TableCollection.TableCollectionModel.TableCollectionModel`: *added*: Added in version 2020: The TableCollectionModel class was added.
- {py:obj}`abaqus.TableCollection.TableCollectionModel.EventSeries`: *added*: Added in version 2020: The EventSeries class was added.
- {py:obj}`abaqus.TableCollection.TableCollectionModel.EventSeriesType`: *added*: Added in version 2020: The EventSeriesType class was added.

### {py:obj}`abaqus.TableCollection.TableCollectionStep`

- {py:obj}`abaqus.TableCollection.TableCollectionStep.ActivateElements`: *added*: Added in version 2020: The ActivateElements class was added.
- {py:obj}`abaqus.TableCollection.TableCollectionStep.TableCollectionStep`: *added*: Added in version 2020: The TableCollectionStep class was added.

### {py:obj}`abaqus.TableCollection.TableCollection`

- {py:obj}`abaqus.TableCollection.TableCollection.DataTable`: *added*: Added in version 2020: The DataTable class was added.
- {py:obj}`abaqus.TableCollection.TableCollection.ParameterTable`: *added*: Added in version 2020: The ParameterTable class was added.
- {py:obj}`abaqus.TableCollection.TableCollection.PropertyTable`: *added*: Added in version 2020: The PropertyTable class was added.
- {py:obj}`abaqus.TableCollection.TableCollection.TableCollection`: *added*: Added in version 2020: The TableCollection class was added.

### {py:obj}`abaqus.TableCollection.ParameterTable`

- {py:obj}`abaqus.TableCollection.ParameterTable.ParameterColumn`: *added*: Added in version 2020: The ParameterColumn class was added.

### {py:obj}`abaqus.TableCollection.PropertyTableData`

- {py:obj}`abaqus.TableCollection.PropertyTableData.PropertyTableData`: *added*: Added in version 2020: The PropertyTableData class was added.


## Abaqus 2019

### {py:obj}`abaqus.OdbDisplay.OdbDisplay`

- {py:obj}`abaqus.OdbDisplay.OdbDisplay.ContourOptions.setValues`: *added*: Added in version 2019: The legendHideOutsideLimits argument was added.

### {py:obj}`abaqus.PlotOptions.BasicOptions`

- {py:obj}`abaqus.PlotOptions.BasicOptions.BasicOptions.numericForm`: *changed*: Changed in version 2019: Add possible values: COMPLEX_ENVELOPE_MAX_ABS, COMPLEX_ENVELOPE_MAX, and COMPLEX_ENVELOPE_MIN.
- {py:obj}`abaqus.PlotOptions.BasicOptions.BasicOptions.setValues`: *changed*: Changed in version 2019: Add possible values: COMPLEX_ENVELOPE_MAX_ABS, COMPLEX_ENVELOPE_MAX, and COMPLEX_ENVELOPE_MIN.

### {py:obj}`abaqus.DisplayGroup.LeafFromConstraintNames`

- {py:obj}`abaqus.DisplayGroup.LeafFromConstraintNames.LeafFromConstraintNames`: *added*: Added in version 2019: The LeafFromConstraintNames class was added.

### {py:obj}`abaqus.Interaction.InteractionModel`

- {py:obj}`abaqus.Interaction.InteractionModel.InteractionModel.FluidInflator`: *added*: Added in version 2019: The FluidInflator method was added.
- {py:obj}`abaqus.Interaction.InteractionModel.InteractionModel.SurfaceToSurfaceContactStd`: *added*: Added in version 2019: The normalAdjustment argument was added.
- {py:obj}`abaqus.Interaction.InteractionModel.InteractionModel.SurfaceToSurfaceContactStd`: *added*: Added in version 2019: The normalAdjustment argument was added.
- {py:obj}`abaqus.Interaction.InteractionModel.FluidInflator`: *added*: Added in version 2019: The FluidInflator class was added.

### {py:obj}`abaqus.Interaction.InteractionPropertyModel`

- {py:obj}`abaqus.Interaction.InteractionPropertyModel.InteractionPropertyModel.FluidInflatorProperty`: *added*: Added in version 2019: The FluidInflatorProperty method was added.
- {py:obj}`abaqus.Interaction.InteractionPropertyModel.FluidInflatorProperty`: *added*: Added in version 2019: The FluidInflatorProperty class was added.

### {py:obj}`abaqus.Interaction.FluidInflatorState`

- {py:obj}`abaqus.Interaction.FluidInflatorState.FluidInflatorState`: *added*: Added in version 2019: The FluidInflatorState class was added.

### {py:obj}`abaqus.Interaction.SurfaceToSurfaceContactStd`

- {py:obj}`abaqus.Interaction.SurfaceToSurfaceContactStd.SurfaceToSurfaceContactStd.handedness`: *added*: Added in version 2019: The handedness attribute was added.
- {py:obj}`abaqus.Interaction.SurfaceToSurfaceContactStd.SurfaceToSurfaceContactStd.normalAdjustment`: *added*: Added in version 2019: The normalAdjustment attribute was added.
- {py:obj}`abaqus.Interaction.SurfaceToSurfaceContactStd.SurfaceToSurfaceContactStd.setValues`: *added*: Added in version 2019: The normalAdjustment argument was added.
- {py:obj}`abaqus.Interaction.SurfaceToSurfaceContactStd.SurfaceToSurfaceContactStd.setValues`: *added*: Added in version 2019: The normalAdjustment argument was added.

### {py:obj}`abaqus.Mesh.MeshPart`

- {py:obj}`abaqus.Mesh.MeshPart.ElemType.nodeOffset`: *added*: Added in version 2019: The nodeOffset attribute was added.
- {py:obj}`abaqus.Mesh.MeshPart.ElemType.numFourierModes`: *added*: Added in version 2019: The numFourierModes attribute was added.

### {py:obj}`abaqus.Optimization.OptimizationTaskModel`

- {py:obj}`abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.BeadTask`: *added*: Added in version 2019: The abaqusSensitivities argument was added.
- {py:obj}`abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask`: *added*: Added in version 2019: The abaqusSensitivities argument was added.
- {py:obj}`abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.SizingTask`: *added*: Added in version 2019: The abaqusSensitivities argument was added.
- {py:obj}`abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.TopologyTask`: *added*: Added in version 2019: The abaqusSensitivities argument was added.
- {py:obj}`abaqus.Optimization.OptimizationTaskModel.BeadTask.abaqusSensitivities`: *added*: Added in version 2019: The abaqusSensitivities attribute was added.
- {py:obj}`abaqus.Optimization.OptimizationTaskModel.BeadTask.setValues`: *added*: Added in version 2019: The abaqusSensitivities argument was added.

### {py:obj}`abaqus.Optimization.OptimizationTask`

- {py:obj}`abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyOverhangControl`: *added*: Added in version 2019: The TopologyOverhangControl method was added.

### {py:obj}`abaqus.Optimization.TopologyOverhangControl`

- {py:obj}`abaqus.Optimization.TopologyOverhangControl.TopologyOverhangControl`: *added*: Added in version 2019: The TopologyOverhangControl class was added.

### {py:obj}`abaqus.Optimization.ShapeTask`

- {py:obj}`abaqus.Optimization.ShapeTask.ShapeTask.abaqusSensitivities`: *added*: Added in version 2019: The abaqusSensitivities attribute was added.
- {py:obj}`abaqus.Optimization.ShapeTask.ShapeTask.setValues`: *added*: Added in version 2019: The abaqusSensitivities argument was added.

### {py:obj}`abaqus.Optimization.SizingTask`

- {py:obj}`abaqus.Optimization.SizingTask.SizingTask.abaqusSensitivities`: *added*: Added in version 2019: The abaqusSensitivities attribute was added.
- {py:obj}`abaqus.Optimization.SizingTask.SizingTask.setValues`: *added*: Added in version 2019: The abaqusSensitivities argument was added.

### {py:obj}`abaqus.Optimization.TopologyTask`

- {py:obj}`abaqus.Optimization.TopologyTask.TopologyTask.abaqusSensitivities`: *added*: Added in version 2019: The abaqusSensitivities attribute was added.
- {py:obj}`abaqus.Optimization.TopologyTask.TopologyTask.setValues`: *added*: Added in version 2019: The abaqusSensitivities argument was added.

### {py:obj}`abaqus.Assembly.ModelInstance`

- {py:obj}`abaqus.Assembly.ModelInstance.ModelInstance.replace`: *added*: Added in version 2019: The replace method was added.


## Abaqus 2018

### {py:obj}`abaqus.Session.SessionBase`

- {py:obj}`abaqus.Session.SessionBase.Drawing.setValues`: *added*: Added in version 2018: The depthTest argument was added.

### {py:obj}`abaqus.OdbDisplay.OdbDisplay`

- {py:obj}`abaqus.OdbDisplay.OdbDisplay.ContourOptions.setValues`: *added*: Added in version 2018: The reversedContourLegendRange argument was added.

### {py:obj}`abaqus.XY.XYSession`

- {py:obj}`abaqus.XY.XYSession.XYSession.XYDataFromPath`: *added*: Added in version 2018: The removeDuplicateXYPairs argument was added.
- {py:obj}`abaqus.XY.XYSession.XYSession.XYDataFromPath`: *added*: Added in version 2018: The includeAllElements argument was added.

### {py:obj}`abaqus.XY.writeXYReport`

- {py:obj}`abaqus.XY.writeXYReport.XYData.XYDataFromPath`: *added*: Added in version 2018: The removeDuplicateXYPairs argument was added.
- {py:obj}`abaqus.XY.writeXYReport.XYData.XYDataFromPath`: *added*: Added in version 2018: The includeAllElements argument was added.

### {py:obj}`abaqus.XY.XYDataCommands`

- {py:obj}`abaqus.XY.XYDataCommands.XYDataFromPath`: *added*: Added in version 2018: The removeDuplicateXYPairs argument was added.
- {py:obj}`abaqus.XY.XYDataCommands.XYDataFromPath`: *added*: Added in version 2018: The includeAllElements argument was added.

### {py:obj}`abaqus.Part.PartBase`

- {py:obj}`abaqus.Part.PartBase.PartBase.writeAcisFile`: *changed*: Changed in version 2018: Add description for thr file name's extension.
- {py:obj}`abaqus.Part.PartBase.AcisFile.writeAcisFile`: *changed*: Changed in version 2018: Add description for thr file name's extension.

### {py:obj}`abaqus.Region.RegionPart`

- {py:obj}`abaqus.Region.RegionPart.RegionPart.SetFromNodeLabels`: *added*: Added in version 2018: The unsorted argument was added.

### {py:obj}`abaqus.Region.Set`

- {py:obj}`abaqus.Region.Set.Set.SetFromNodeLabels`: *added*: Added in version 2018: The unsorted argument was added.

### {py:obj}`abaqus.PredefinedField.PredefinedFieldModel`

- {py:obj}`abaqus.PredefinedField.PredefinedFieldModel.PredefinedFieldModel.Field`: *added*: Added in version 2018: The Field method was added.
- {py:obj}`abaqus.PredefinedField.PredefinedFieldModel.Field`: *added*: Added in version 2018: The Field class was added.

### {py:obj}`abaqus.PredefinedField.FieldState`

- {py:obj}`abaqus.PredefinedField.FieldState.FieldState`: *added*: Added in version 2018: The FieldState class was added.

### {py:obj}`abaqus.Section.SectionModel`

- {py:obj}`abaqus.Section.SectionModel.SectionModel.HomogeneousSolidSection`: *changed*: Changed in version 2018: The default value is now 1.0 instead of None.

### {py:obj}`abaqus.Section.SectionOdb`

- {py:obj}`abaqus.Section.SectionOdb.SectionOdb.HomogeneousSolidSection`: *changed*: Changed in version 2018: The default value is now 1.0 instead of None.
- {py:obj}`abaqus.Section.SectionOdb.HomogeneousSolidSection.thickness`: *changed*: Changed in version 2018: The default value is now 1.0 instead of None.

### {py:obj}`abaqus.Sketcher.SketchModel`

- {py:obj}`abaqus.Sketcher.SketchModel.ConstrainedSketch.writeAcisFile`: *changed*: Changed in version 2018: Add description for thr file name's extension.

### {py:obj}`abaqus.Step.StepModel`

- {py:obj}`abaqus.Step.StepModel.StepModel.ExplicitDynamicsStep`: *added*: Added in version 2018: The improvedDtMethod argument was added.
- {py:obj}`abaqus.Step.StepModel.StepModel.TempDisplacementDynamicsStep`: *added*: Added in version 2018: The improvedDtMethod argument was added.
- {py:obj}`abaqus.Step.StepModel.ExplicitDynamicsStep.setValues`: *added*: Added in version 2018: The improvedDtMethod argument was added.

### {py:obj}`abaqus.Step.TempDisplacementDynamicsStep`

- {py:obj}`abaqus.Step.TempDisplacementDynamicsStep.TempDisplacementDynamicsStep.improvedDtMethod`: *added*: Added in version 2018: The improvedDtMethod attribute was added.
- {py:obj}`abaqus.Step.TempDisplacementDynamicsStep.TempDisplacementDynamicsStep.setValues`: *added*: Added in version 2018: The improvedDtMethod argument was added.

### {py:obj}`abaqus.Load.LoadModel`

- {py:obj}`abaqus.Load.LoadModel.LoadModel.BoltLoad`: *added*: Added in version 2018: The preTenSecPartLevel argument was added.

### {py:obj}`abaqus.Material.Material`

- {py:obj}`abaqus.Material.Material.Material.MeanFieldHomogenization`: *added*: Added in version 2018: The MeanFieldHomogenization method was added.

### {py:obj}`abaqus.Material.MaterialBase`

- {py:obj}`abaqus.Material.MaterialBase.MaterialBase.meanFieldHomogenization`: *added*: Added in version 2018: The meanFieldHomogenization attribute was added.

### {py:obj}`abaqus.Material.Multiscale.MeanFieldHomogenization`

- {py:obj}`abaqus.Material.Multiscale.MeanFieldHomogenization.MeanFieldHomogenization`: *added*: Added in version 2018: The MeanFieldHomogenization class was added.

### {py:obj}`abaqus.Material.Multiscale.MeanFieldInclusion`

- {py:obj}`abaqus.Material.Multiscale.MeanFieldInclusion.MeanFieldInclusion`: *added*: Added in version 2018: The MeanFieldInclusion class was added.

### {py:obj}`abaqus.Material.Multiscale.MeanFieldMatrix`

- {py:obj}`abaqus.Material.Multiscale.MeanFieldMatrix.MeanFieldMatrix`: *added*: Added in version 2018: The MeanFieldMatrix class was added.

### {py:obj}`abaqus.Material.Multiscale.MeanFieldVoid`

- {py:obj}`abaqus.Material.Multiscale.MeanFieldVoid.MeanFieldVoid`: *added*: Added in version 2018: The MeanFieldMatrix class was added.

### {py:obj}`abaqus.Mesh.MeshElementArray`

- {py:obj}`abaqus.Mesh.MeshElementArray.MeshElementArray.getExteriorEdges`: *added*: Added in version 2018: The getExteriorEdges method was added.
- {py:obj}`abaqus.Mesh.MeshElementArray.MeshElementArray.getExteriorFaces`: *added*: Added in version 2018: The getExteriorFaces method was added.

### {py:obj}`abaqus.Mesh.MesherOptions`

- {py:obj}`abaqus.Mesh.MesherOptions.MesherOptions.setValues`: *added*: Added in version 2018: The guiPreferredElements argument was added.


## Abaqus 2017

### {py:obj}`abaqus.PredefinedField.PredefinedFieldModel`

- {py:obj}`abaqus.PredefinedField.PredefinedFieldModel.PredefinedFieldModel.Stress`: *added*: Added in version 2017: The Stress method was added.

### {py:obj}`abaqus.PredefinedField.Stress`

- {py:obj}`abaqus.PredefinedField.Stress.Stress`: *added*: Added in version 2017: The Stress class was added.

### {py:obj}`abaqus.Section.SectionLayerArray`

- {py:obj}`abaqus.Section.SectionLayerArray.SectionLayer`: *changed*: Changed in version 2017: The thicknessType attribute and thicknessField attribute were removed.

### {py:obj}`abaqus.Step.StepModel`

- {py:obj}`abaqus.Step.StepModel.StepModel.GeostaticStep`: *added*: Added in version 2017: The maxNumInc attribute was added to the GeostaticStep class.
- {py:obj}`abaqus.Step.StepModel.GeostaticStep.maxNumInc`: *added*: Added in version 2017: The maxNumInc attribute was added to the GeostaticStep class.

### {py:obj}`abaqus.Odb.OdbSet`

- {py:obj}`abaqus.Odb.OdbSet.OdbMeshElement.getNormal`: *added*: Added in version 2017: The getNormal method was added.

### {py:obj}`abaqus.Field.OdbMeshRegionData`

- {py:obj}`abaqus.Field.OdbMeshRegionData.OdbMeshRegionData`: *changed*: Changed in version 2017: The transformationType attribute was moved.


