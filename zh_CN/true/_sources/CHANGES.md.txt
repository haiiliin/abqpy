# Abaqus API Changes

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
- {py:obj}`abaqus.Step.StepModel.ExplicitDynamicsStep.improvedDtMethod`: *added*: New in version 2018: The improvedDtMethod attribute was added.
- {py:obj}`abaqus.Step.StepModel.ExplicitDynamicsStep.setValues`: *added*: New in version 2018: The improvedDtMethod argument was added.

### {py:obj}`abaqus.Step.TempDisplacementDynamicsStep`

- {py:obj}`abaqus.Step.TempDisplacementDynamicsStep.TempDisplacementDynamicsStep`: *added*: New in version 2018: The improvedDtMethod argument was added.
- {py:obj}`abaqus.Step.TempDisplacementDynamicsStep.TempDisplacementDynamicsStep.improvedDtMethod`: *added*: New in version 2018: The improvedDtMethod attribute was added.
- {py:obj}`abaqus.Step.TempDisplacementDynamicsStep.TempDisplacementDynamicsStep.setValues`: *added*: New in version 2018: The improvedDtMethod argument was added.

### {py:obj}`abaqus.Session.SessionBase`

- {py:obj}`abaqus.Session.SessionBase.Drawing.setValues`: *added*: New in version 2018: The depthTest argument was added.

### {py:obj}`abaqus.OdbDisplay.OdbDisplay`

- {py:obj}`abaqus.OdbDisplay.OdbDisplay.ContourOptions.reversedContourLegendRange`: *added*: New in version 2018: The reversedContourLegendRange attribute was added.
- {py:obj}`abaqus.OdbDisplay.OdbDisplay.ContourOptions.setValues`: *added*: New in version 2018: The reversedContourLegendRange argument was added.

### {py:obj}`abaqus.OdbDisplay.ViewCut`

- {py:obj}`abaqus.OdbDisplay.ViewCut.ViewCut.crossSectionalArea`: *added*: New in version 2018: The crossSectionalArea attribute was added.

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


