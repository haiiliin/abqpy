# Abaqus API Changes

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


