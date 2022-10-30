# Abaqus Output Database

The Python ODB API commands are used to read and write data from an output database (.odb) file. The path to the Odb object can be via the session.odbs repository or via a variable. In this chapter the Access and Path statements refer to a variable called odb that represents an existing Odb object.

## Classes

### Odb

```{eval-rst}
.. autoclass:: abaqus.Odb.Odb.Odb
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### Other Classes

```{eval-rst}

.. toggle::

    .. autoclass:: abaqus.Odb.OdbBase.OdbBase
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb
        :members:
        :special-members: __init__
        :show-inheritance:
        :noindex:

        .. autoclasstoc::

    .. autoclass:: abaqus.Filter.FilterOdb.FilterOdb
        :members:
        :special-members: __init__
        :show-inheritance:
        :noindex:

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.MaterialOdb.MaterialOdb
        :members:
        :special-members: __init__
        :show-inheritance:
        :noindex:

        .. autoclasstoc::

    .. autoclass:: abaqus.BeamSectionProfile.BeamSectionProfileOdb.BeamSectionProfileOdb
        :members:
        :special-members: __init__
        :show-inheritance:
        :noindex:

        .. autoclasstoc::

    .. autoclass:: abaqus.Odb.AnalyticSurface.AnalyticSurface
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Odb.AnalyticSurfaceSegment.AnalyticSurfaceSegment
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Odb.BeamOrientation.BeamOrientation
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Odb.BeamOrientationArray.BeamOrientationArray
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Odb.FieldBulkData.FieldBulkData
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Odb.FieldLocation.FieldLocation
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Odb.FieldLocationArray.FieldLocationArray
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Odb.FieldOutput.FieldOutput
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Odb.FieldValue.FieldValue
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Odb.FieldValueArray.FieldValueArray
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Odb.HistoryOutput.HistoryOutput
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Odb.HistoryPoint.HistoryPoint
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Odb.HistoryRegion.HistoryRegion
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Odb.JobData.JobData
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Odb.OdbAssembly.OdbAssembly
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Odb.OdbAssemblyBase.OdbAssemblyBase
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. automodule:: abaqus.Odb.OdbCommands
        :members:
        :special-members: __init__
        :show-inheritance:

    .. autoclass:: abaqus.Odb.OdbDatumCsys.OdbDatumCsys
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Odb.OdbFrame.OdbFrame
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Odb.OdbFrameArray.OdbFrameArray
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Odb.OdbInstance.OdbInstance
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Odb.OdbInstanceBase.OdbInstanceBase
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Odb.OdbLoadCase.OdbLoadCase
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Odb.OdbMeshElement.OdbMeshElement
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Odb.OdbMeshElementArray.OdbMeshElementArray
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Odb.OdbMeshNode.OdbMeshNode
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Odb.OdbMeshNodeArray.OdbMeshNodeArray
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Odb.OdbPart.OdbPart
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Odb.OdbPartBase.OdbPartBase
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Odb.OdbPretensionSection.OdbPretensionSection
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Odb.OdbPretensionSectionArray.OdbPretensionSectionArray
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Odb.OdbRigidBody.OdbRigidBody
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Odb.OdbRigidBodyArray.OdbRigidBodyArray
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Odb.OdbSequenceAnalyticSurfaceSegment.OdbSequenceAnalyticSurfaceSegment
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Odb.OdbSession.OdbSession
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Odb.OdbSet.OdbSet
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Odb.OdbStep.OdbStep
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Odb.OdbStepBase.OdbStepBase
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Odb.RebarOrientation.RebarOrientation
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Odb.RebarOrientationArray.RebarOrientationArray
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Odb.ScratchOdb.ScratchOdb
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Odb.SectionCategory.SectionCategory
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Odb.SectionPoint.SectionPoint
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Odb.SectionPointArray.SectionPointArray
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Odb.SectorDefinition.SectorDefinition
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Odb.UserData.UserData
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Odb.UserDataBase.UserDataBase
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::
```
