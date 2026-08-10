# Abaqus API Changes

## Abaqus 2020

### {py:obj}`abaqus.Part.PartBase`

- {py:obj}`abaqus.Part.PartBase.AcisFile.openSolidworks`: *added*: New in version 2020: The openSolidworks method was added.

### {py:obj}`abaqus.Part.AcisMdb`

- {py:obj}`abaqus.Part.AcisMdb.AcisMdb.openSolidworks`: *added*: New in version 2020: The openSolidworks method was added.

### {py:obj}`abaqus.Odb.RebarOrientation`

- {py:obj}`abaqus.Odb.RebarOrientation.OdbSet.instances`: *added*: New in version 2020: The instances attribute was added.
- {py:obj}`abaqus.Odb.RebarOrientation.OdbSet.isInternal`: *added*: New in version 2020: The isInternal attribute was added.

### {py:obj}`abaqus.Canvas.ViewportBase`

- {py:obj}`abaqus.Canvas.ViewportBase.ViewportBase.animationController`: *added*: New in version 2020: The animationController attribute was added.

### {py:obj}`abaqus.TableCollection.TableCollectionAssembly`

- {py:obj}`abaqus.TableCollection.TableCollectionAssembly.TableCollectionAssembly`: *added*: New in version 2020: The TableCollectionAssembly class was added.
- {py:obj}`abaqus.TableCollection.TableCollectionAssembly.ElementProgressiveActivation`: *added*: New in version 2020: The ElementProgressiveActivation class was added.

### {py:obj}`abaqus.TableCollection.TableCollectionModel`

- {py:obj}`abaqus.TableCollection.TableCollectionModel.TableCollectionModel`: *added*: New in version 2020: The TableCollectionModel class was added.
- {py:obj}`abaqus.TableCollection.TableCollectionModel.EventSeries`: *added*: New in version 2020: The EventSeries class was added.
- {py:obj}`abaqus.TableCollection.TableCollectionModel.EventSeriesType`: *added*: New in version 2020: The EventSeriesType class was added.

### {py:obj}`abaqus.TableCollection.TableCollectionStep`

- {py:obj}`abaqus.TableCollection.TableCollectionStep.ActivateElements`: *added*: New in version 2020: The ActivateElements class was added.
- {py:obj}`abaqus.TableCollection.TableCollectionStep.TableCollectionStep`: *added*: New in version 2020: The TableCollectionStep class was added.

### {py:obj}`abaqus.TableCollection.TableCollection`

- {py:obj}`abaqus.TableCollection.TableCollection.DataTable`: *added*: New in version 2020: The DataTable class was added.
- {py:obj}`abaqus.TableCollection.TableCollection.ParameterTable`: *added*: New in version 2020: The ParameterTable class was added.
- {py:obj}`abaqus.TableCollection.TableCollection.PropertyTable`: *added*: New in version 2020: The PropertyTable class was added.
- {py:obj}`abaqus.TableCollection.TableCollection.TableCollection`: *added*: New in version 2020: The TableCollection class was added.

### {py:obj}`abaqus.TableCollection.ParameterTable`

- {py:obj}`abaqus.TableCollection.ParameterTable.ParameterColumn`: *added*: New in version 2020: The ParameterColumn class was added.

### {py:obj}`abaqus.TableCollection.PropertyTableData`

- {py:obj}`abaqus.TableCollection.PropertyTableData.PropertyTableData`: *added*: New in version 2020: The PropertyTableData class was added.

### {py:obj}`abaqus.Model.ModelBase`

- {py:obj}`abaqus.Model.ModelBase.ModelBase.eventSeriesDatas`: *added*: New in version 2020: The eventSeriesDatas attribute was added.
- {py:obj}`abaqus.Model.ModelBase.ModelBase.eventSeriesTypes`: *added*: New in version 2020: The eventSeriesTypes attribute was added.
- {py:obj}`abaqus.Model.ModelBase.ModelBase.tableCollections`: *added*: New in version 2020: The tableCollections attribute was added.

### {py:obj}`abaqus.Interaction.InteractionModel`

- {py:obj}`abaqus.Interaction.InteractionModel.InteractionModel.ContactExp`: *added*: New in version 2020: The polarityAssignments argument was added.
- {py:obj}`abaqus.Interaction.InteractionModel.ContactExp.polarityAssignments`: *added*: New in version 2020: The polarityAssignments attribute was added.

### {py:obj}`abaqus.Interaction.InteractionContactInitializationModel`

- {py:obj}`abaqus.Interaction.InteractionContactInitializationModel.InteractionContactInitializationModel.StdInitialization`: *added*: New in version 2020: The ExpInitialization method was added.
- {py:obj}`abaqus.Interaction.InteractionContactInitializationModel.ExpInitialization`: *added*: New in version 2020: The ExpInitialization class was added.

### {py:obj}`abaqus.Material.Material`

- {py:obj}`abaqus.Material.Material.Material.Creep`: *added*: New in version 2020: The options ANAND, DARVEAUX, DOUBLE_POWER, POWER_LAW, and TIME_POWER_LAW were added.
- {py:obj}`abaqus.Material.Material.Material.GapFlow`: *added*: New in version 2020: The options BINGHAM_PLASTIC and HERSCHEL-BULKLEY were added.
- {py:obj}`abaqus.Material.Material.Material.Viscous`: *added*: New in version 2020: The options ANAND, DARVEAUX, DOUBLE_POWER, POWER_LAW, and TIME_POWER_LAW were added.

### {py:obj}`abaqus.Material.Plastic.TensileFailure`

- {py:obj}`abaqus.Material.Plastic.TensileFailure.TensileFailure`: *added*: New in version 2020: The TensileFailure class was added.

### {py:obj}`abaqus.Assembly.AssemblyBase`

- {py:obj}`abaqus.Assembly.AssemblyBase.AssemblyBase.smoothNodes`: *changed*: Changed in version 2020: The coordinates arguments was removed, the nodes now replaces it.


## Abaqus 2019

### {py:obj}`abaqus.DisplayGroup.LeafFromConstraintNames`

- {py:obj}`abaqus.DisplayGroup.LeafFromConstraintNames.LeafFromConstraintNames`: *added*: New in version 2019: The LeafFromConstraintNames class was added.

### {py:obj}`abaqus.OdbDisplay.OdbDisplay`

- {py:obj}`abaqus.OdbDisplay.OdbDisplay.ContourOptions.setValues`: *added*: New in version 2019: The legendHideOutsideLimits argument was added.

### {py:obj}`abaqus.PlotOptions.BasicOptions`

- {py:obj}`abaqus.PlotOptions.BasicOptions.BasicOptions.numericForm`: *changed*: Changed in version 2019: Add possible values: COMPLEX_ENVELOPE_MAX_ABS, COMPLEX_ENVELOPE_MAX, and COMPLEX_ENVELOPE_MIN.
- {py:obj}`abaqus.PlotOptions.BasicOptions.BasicOptions.setValues`: *changed*: Changed in version 2019: Add possible values: COMPLEX_ENVELOPE_MAX_ABS, COMPLEX_ENVELOPE_MAX, and COMPLEX_ENVELOPE_MIN.

### {py:obj}`abaqus.Interaction.InteractionModel`

- {py:obj}`abaqus.Interaction.InteractionModel.InteractionModel.FluidInflator`: *added*: New in version 2019: The FluidInflator method was added.
- {py:obj}`abaqus.Interaction.InteractionModel.InteractionModel.SurfaceToSurfaceContactStd`: *added*: New in version 2019: The normalAdjustment argument was added.
- {py:obj}`abaqus.Interaction.InteractionModel.InteractionModel.SurfaceToSurfaceContactStd`: *added*: New in version 2019: The normalAdjustment argument was added.
- {py:obj}`abaqus.Interaction.InteractionModel.FluidInflator`: *added*: New in version 2019: The FluidInflator class was added.

### {py:obj}`abaqus.Interaction.InteractionPropertyModel`

- {py:obj}`abaqus.Interaction.InteractionPropertyModel.InteractionPropertyModel.FluidInflatorProperty`: *added*: New in version 2019: The FluidInflatorProperty method was added.
- {py:obj}`abaqus.Interaction.InteractionPropertyModel.FluidInflatorProperty`: *added*: New in version 2019: The FluidInflatorProperty class was added.

### {py:obj}`abaqus.Interaction.FluidInflatorState`

- {py:obj}`abaqus.Interaction.FluidInflatorState.FluidInflatorState`: *added*: New in version 2019: The FluidInflatorState class was added.

### {py:obj}`abaqus.Interaction.SurfaceToSurfaceContactStd`

- {py:obj}`abaqus.Interaction.SurfaceToSurfaceContactStd.SurfaceToSurfaceContactStd`: *added*: New in version 2019: The normalAdjustment argument was added.
- {py:obj}`abaqus.Interaction.SurfaceToSurfaceContactStd.SurfaceToSurfaceContactStd`: *added*: New in version 2019: The normalAdjustment argument was added.
- {py:obj}`abaqus.Interaction.SurfaceToSurfaceContactStd.SurfaceToSurfaceContactStd.handedness`: *added*: New in version 2019: The handedness attribute was added.
- {py:obj}`abaqus.Interaction.SurfaceToSurfaceContactStd.SurfaceToSurfaceContactStd.normalAdjustment`: *added*: New in version 2019: The normalAdjustment attribute was added.
- {py:obj}`abaqus.Interaction.SurfaceToSurfaceContactStd.SurfaceToSurfaceContactStd.setValues`: *added*: New in version 2019: The normalAdjustment argument was added.
- {py:obj}`abaqus.Interaction.SurfaceToSurfaceContactStd.SurfaceToSurfaceContactStd.setValues`: *added*: New in version 2019: The normalAdjustment argument was added.

### {py:obj}`abaqus.Mesh.MeshPart`

- {py:obj}`abaqus.Mesh.MeshPart.ElemType`: *added*: New in version 2019: The numFourierModes argument was added.
- {py:obj}`abaqus.Mesh.MeshPart.ElemType`: *added*: New in version 2019: The nodeOffset argument was added.
- {py:obj}`abaqus.Mesh.MeshPart.ElemType.nodeOffset`: *added*: New in version 2019: The nodeOffset attribute was added.
- {py:obj}`abaqus.Mesh.MeshPart.ElemType.numFourierModes`: *added*: New in version 2019: The numFourierModes attribute was added.

### {py:obj}`abaqus.Optimization.OptimizationTaskModel`

- {py:obj}`abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.BeadTask`: *added*: New in version 2019: The abaqusSensitivities argument was added.
- {py:obj}`abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask`: *added*: New in version 2019: The abaqusSensitivities argument was added.
- {py:obj}`abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.SizingTask`: *added*: New in version 2019: The abaqusSensitivities argument was added.
- {py:obj}`abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.TopologyTask`: *added*: New in version 2019: The abaqusSensitivities argument was added.
- {py:obj}`abaqus.Optimization.OptimizationTaskModel.BeadTask`: *added*: New in version 2019: The abaqusSensitivities argument was added.
- {py:obj}`abaqus.Optimization.OptimizationTaskModel.BeadTask.abaqusSensitivities`: *added*: New in version 2019: The abaqusSensitivities attribute was added.
- {py:obj}`abaqus.Optimization.OptimizationTaskModel.BeadTask.setValues`: *added*: New in version 2019: The abaqusSensitivities argument was added.

### {py:obj}`abaqus.Optimization.OptimizationTask`

- {py:obj}`abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyOverhangControl`: *added*: New in version 2019: The TopologyOverhangControl method was added.

### {py:obj}`abaqus.Optimization.TopologyOverhangControl`

- {py:obj}`abaqus.Optimization.TopologyOverhangControl.TopologyOverhangControl`: *added*: New in version 2019: The TopologyOverhangControl class was added.

### {py:obj}`abaqus.Optimization.ShapeTask`

- {py:obj}`abaqus.Optimization.ShapeTask.ShapeTask`: *added*: New in version 2019: The abaqusSensitivities argument was added.
- {py:obj}`abaqus.Optimization.ShapeTask.ShapeTask.abaqusSensitivities`: *added*: New in version 2019: The abaqusSensitivities attribute was added.
- {py:obj}`abaqus.Optimization.ShapeTask.ShapeTask.setValues`: *added*: New in version 2019: The abaqusSensitivities argument was added.

### {py:obj}`abaqus.Optimization.SizingTask`

- {py:obj}`abaqus.Optimization.SizingTask.SizingTask`: *added*: New in version 2019: The abaqusSensitivities argument was added.
- {py:obj}`abaqus.Optimization.SizingTask.SizingTask.abaqusSensitivities`: *added*: New in version 2019: The abaqusSensitivities attribute was added.
- {py:obj}`abaqus.Optimization.SizingTask.SizingTask.setValues`: *added*: New in version 2019: The abaqusSensitivities argument was added.

### {py:obj}`abaqus.Optimization.TopologyTask`

- {py:obj}`abaqus.Optimization.TopologyTask.TopologyTask`: *added*: New in version 2019: The abaqusSensitivities argument was added.
- {py:obj}`abaqus.Optimization.TopologyTask.TopologyTask.abaqusSensitivities`: *added*: New in version 2019: The abaqusSensitivities attribute was added.
- {py:obj}`abaqus.Optimization.TopologyTask.TopologyTask.setValues`: *added*: New in version 2019: The abaqusSensitivities argument was added.

### {py:obj}`abaqus.Assembly.ModelInstance`

- {py:obj}`abaqus.Assembly.ModelInstance.ModelInstance.replace`: *added*: New in version 2019: The replace method was added.


## Abaqus 2018

### {py:obj}`abaqus.Part.PartBase`

- {py:obj}`abaqus.Part.PartBase.PartBase.writeAcisFile`: *changed*: Changed in version 2018: Add description for thr file name's extension.
- {py:obj}`abaqus.Part.PartBase.AcisFile.writeAcisFile`: *changed*: Changed in version 2018: Add description for thr file name's extension.

### {py:obj}`abaqus.Region.RegionPart`

- {py:obj}`abaqus.Region.RegionPart.RegionPart.SetFromNodeLabels`: *added*: New in version 2018: The unsorted argument was added.

### {py:obj}`abaqus.Region.Set`

- {py:obj}`abaqus.Region.Set.Set.SetFromNodeLabels`: *added*: New in version 2018: The unsorted argument was added.

### {py:obj}`abaqus.PredefinedField.PredefinedFieldModel`

- {py:obj}`abaqus.PredefinedField.PredefinedFieldModel.PredefinedFieldModel.Field`: *added*: New in version 2018: The Field method was added.
- {py:obj}`abaqus.PredefinedField.PredefinedFieldModel.Field`: *added*: New in version 2018: The Field class was added.

### {py:obj}`abaqus.PredefinedField.FieldState`

- {py:obj}`abaqus.PredefinedField.FieldState.FieldState`: *added*: New in version 2018: The FieldState class was added.

### {py:obj}`abaqus.Section.SectionModel`

- {py:obj}`abaqus.Section.SectionModel.SectionModel.HomogeneousSolidSection`: *changed*: Changed in version 2018: The default value is now 1.0 instead of None.

### {py:obj}`abaqus.Section.SectionOdb`

- {py:obj}`abaqus.Section.SectionOdb.SectionOdb.HomogeneousSolidSection`: *changed*: Changed in version 2018: The default value is now 1.0 instead of None.
- {py:obj}`abaqus.Section.SectionOdb.HomogeneousSolidSection`: *changed*: Changed in version 2018: The default value is now 1.0 instead of None.
- {py:obj}`abaqus.Section.SectionOdb.HomogeneousSolidSection.thickness`: *changed*: Changed in version 2018: The default value is now 1.0 instead of None.

### {py:obj}`abaqus.Sketcher.SketchModel`

- {py:obj}`abaqus.Sketcher.SketchModel.ConstrainedSketch.writeAcisFile`: *changed*: Changed in version 2018: Add description for thr file name's extension.

### {py:obj}`abaqus.Step.StepModel`

- {py:obj}`abaqus.Step.StepModel.StepModel.ExplicitDynamicsStep`: *added*: New in version 2018: The improvedDtMethod argument was added.
- {py:obj}`abaqus.Step.StepModel.StepModel.TempDisplacementDynamicsStep`: *added*: New in version 2018: The improvedDtMethod argument was added.
- {py:obj}`abaqus.Step.StepModel.ExplicitDynamicsStep`: *added*: New in version 2018: The improvedDtMethod argument was added.
- {py:obj}`abaqus.Step.StepModel.ExplicitDynamicsStep.setValues`: *added*: New in version 2018: The improvedDtMethod argument was added.

### {py:obj}`abaqus.Step.TempDisplacementDynamicsStep`

- {py:obj}`abaqus.Step.TempDisplacementDynamicsStep.TempDisplacementDynamicsStep`: *added*: New in version 2018: The improvedDtMethod argument was added.
- {py:obj}`abaqus.Step.TempDisplacementDynamicsStep.TempDisplacementDynamicsStep.improvedDtMethod`: *added*: New in version 2018: The improvedDtMethod attribute was added.
- {py:obj}`abaqus.Step.TempDisplacementDynamicsStep.TempDisplacementDynamicsStep.setValues`: *added*: New in version 2018: The improvedDtMethod argument was added.

### {py:obj}`abaqus.Session.SessionBase`

- {py:obj}`abaqus.Session.SessionBase.Drawing.setValues`: *added*: New in version 2018: The depthTest argument was added.

### {py:obj}`abaqus.OdbDisplay.OdbDisplay`

- {py:obj}`abaqus.OdbDisplay.OdbDisplay.ContourOptions.setValues`: *added*: New in version 2018: The reversedContourLegendRange argument was added.

### {py:obj}`abaqus.XY.XYSession`

- {py:obj}`abaqus.XY.XYSession.XYSession.XYDataFromPath`: *added*: New in version 2018: The removeDuplicateXYPairs argument was added.
- {py:obj}`abaqus.XY.XYSession.XYSession.XYDataFromPath`: *added*: New in version 2018: The includeAllElements argument was added.

### {py:obj}`abaqus.XY.writeXYReport`

- {py:obj}`abaqus.XY.writeXYReport.XYData.XYDataFromPath`: *added*: New in version 2018: The removeDuplicateXYPairs argument was added.
- {py:obj}`abaqus.XY.writeXYReport.XYData.XYDataFromPath`: *added*: New in version 2018: The includeAllElements argument was added.

### {py:obj}`abaqus.Load.LoadModel`

- {py:obj}`abaqus.Load.LoadModel.LoadModel.BoltLoad`: *added*: New in version 2018: The preTenSecPartLevel argument was added.
- {py:obj}`abaqus.Load.LoadModel.BoltLoad`: *added*: New in version 2018: The preTenSecPartLevel argument was added.

### {py:obj}`abaqus.Material.Material`

- {py:obj}`abaqus.Material.Material.Material.MeanFieldHomogenization`: *added*: New in version 2018: The MeanFieldHomogenization method was added.

### {py:obj}`abaqus.Material.MaterialBase`

- {py:obj}`abaqus.Material.MaterialBase.MaterialBase.meanFieldHomogenization`: *added*: New in version 2018: The meanFieldHomogenization attribute was added.

### {py:obj}`abaqus.Material.Multiscale.MeanFieldHomogenization`

- {py:obj}`abaqus.Material.Multiscale.MeanFieldHomogenization.MeanFieldHomogenization`: *added*: New in version 2018: The MeanFieldHomogenization class was added.

### {py:obj}`abaqus.Material.Multiscale.MeanFieldInclusion`

- {py:obj}`abaqus.Material.Multiscale.MeanFieldInclusion.MeanFieldInclusion`: *added*: New in version 2018: The MeanFieldInclusion class was added.

### {py:obj}`abaqus.Material.Multiscale.MeanFieldMatrix`

- {py:obj}`abaqus.Material.Multiscale.MeanFieldMatrix.MeanFieldMatrix`: *added*: New in version 2018: The MeanFieldMatrix class was added.

### {py:obj}`abaqus.Material.Multiscale.MeanFieldVoid`

- {py:obj}`abaqus.Material.Multiscale.MeanFieldVoid.MeanFieldVoid`: *added*: New in version 2018: The MeanFieldMatrix class was added.

### {py:obj}`abaqus.Mesh.MeshElementArray`

- {py:obj}`abaqus.Mesh.MeshElementArray.MeshElementArray.getExteriorEdges`: *added*: New in version 2018: The getExteriorEdges method was added.
- {py:obj}`abaqus.Mesh.MeshElementArray.MeshElementArray.getExteriorFaces`: *added*: New in version 2018: The getExteriorFaces method was added.

### {py:obj}`abaqus.Mesh.MesherOptions`

- {py:obj}`abaqus.Mesh.MesherOptions.MesherOptions.setValues`: *added*: New in version 2018: The guiPreferredElements argument was added.


## Abaqus 2017

### {py:obj}`abaqus.PredefinedField.PredefinedFieldModel`

- {py:obj}`abaqus.PredefinedField.PredefinedFieldModel.PredefinedFieldModel.Stress`: *added*: New in version 2017: The Stress method was added.

### {py:obj}`abaqus.PredefinedField.Stress`

- {py:obj}`abaqus.PredefinedField.Stress.Stress`: *added*: New in version 2017: The Stress class was added.

### {py:obj}`abaqus.Section.SectionLayerArray`

- {py:obj}`abaqus.Section.SectionLayerArray.SectionLayer`: *changed*: Changed in version 2017: The thicknessType attribute and thicknessField attribute were removed.
- {py:obj}`abaqus.Section.SectionLayerArray.SectionLayer`: *changed*: Changed in version 2017: The thicknessType argument and thicknessField argument were removed.

### {py:obj}`abaqus.Sketcher.ConstrainedSketchDimension.DistanceDimension`

- {py:obj}`abaqus.Sketcher.ConstrainedSketchDimension.DistanceDimension.DistanceDimension`: *changed*: Changed in version 2017: The vertex2 argument was renamed to entity2.

### {py:obj}`abaqus.Sketcher.ConstrainedSketchGeometry.ArcByCenterEnds`

- {py:obj}`abaqus.Sketcher.ConstrainedSketchGeometry.ArcByCenterEnds.ArcByCenterEnds`: *added*: New in version 2017: The direction argument was added.

### {py:obj}`abaqus.Step.StepModel`

- {py:obj}`abaqus.Step.StepModel.StepModel.GeostaticStep`: *added*: New in version 2017: The maxNumInc attribute was added to the GeostaticStep class.
- {py:obj}`abaqus.Step.StepModel.GeostaticStep`: *added*: New in version 2017: The maxNumInc attribute was added to the GeostaticStep class.
- {py:obj}`abaqus.Step.StepModel.GeostaticStep.maxNumInc`: *added*: New in version 2017: The maxNumInc attribute was added to the GeostaticStep class.

### {py:obj}`abaqus.Odb.OdbSet`

- {py:obj}`abaqus.Odb.OdbSet.OdbMeshElement.getNormal`: *added*: New in version 2017: The getNormal method was added.

### {py:obj}`abaqus.Job.JobMdb`

- {py:obj}`abaqus.Job.JobMdb.JobFromInputFile`: *changed*: Changed in version 2017: The default value for parallelizationMethodExplicit is now DOMAIN
- {py:obj}`abaqus.Job.JobMdb.JobFromInputFile.parallelizationMethodExplicit`: *changed*: Changed in version 2017: The default value for parallelizationMethodExplicit is now DOMAIN
- {py:obj}`abaqus.Job.JobMdb.JobFromInputFile.setValues`: *changed*: Changed in version 2017: The default value for parallelizationMethodExplicit is now DOMAIN

### {py:obj}`abaqus.Job.ModelJob`

- {py:obj}`abaqus.Job.ModelJob.ModelJob`: *changed*: Changed in version 2017: The default value for parallelizationMethodExplicit is now DOMAIN
- {py:obj}`abaqus.Job.ModelJob.ModelJob.parallelizationMethodExplicit`: *changed*: Changed in version 2017: The default value for parallelizationMethodExplicit is now DOMAIN

### {py:obj}`abaqus.Field.OdbMeshRegionData`

- {py:obj}`abaqus.Field.OdbMeshRegionData.OdbMeshRegionData`: *changed*: Changed in version 2017: The transformationType attribute was moved.
- {py:obj}`abaqus.Field.OdbMeshRegionData.OdbMeshRegionData`: *changed*: Changed in version 2017: The transformationType argument was moved.


