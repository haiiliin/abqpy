# Section

The Section commands are used to create sections and profiles with their associated properties and behavior. The various section objects are all derived from the Section object. The various profile objects are all derived from the Profile object. See Property commands for the property assignment commands.

## Create sections

### In Mdb

```{eval-rst}
.. autoclass:: abaqus.Section.SectionModel.SectionModel
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::

```

### In Odb

```{eval-rst}
.. autoclass:: abaqus.Section.SectionOdb.SectionOdb
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::

```

## Other Classes

```{eval-rst}

.. toggle::

    .. autoclass:: abaqus.Section.Section.Section
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Section.SectionBase.SectionBase
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Section.AcousticInfiniteSection.AcousticInfiniteSection
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Section.AcousticInterfaceSection.AcousticInterfaceSection
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Section.BeamSection.BeamSection
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Section.CohesiveSection.CohesiveSection
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Section.CompositeShellSection.CompositeShellSection
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Section.CompositeSolidSection.CompositeSolidSection
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Section.ConnectorSection.ConnectorSection
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Section.EulerianSection.EulerianSection
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Section.GasketSection.GasketSection
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Section.GeneralStiffnessSection.GeneralStiffnessSection
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Section.GeometryShellSection.GeometryShellSection
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Section.HomogeneousShellSection.HomogeneousShellSection
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Section.HomogeneousSolidSection.HomogeneousSolidSection
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Section.LayerProperties.LayerProperties
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Section.LayerPropertiesArray.LayerPropertiesArray
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Section.MembraneSection.MembraneSection
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Section.MPCSection.MPCSection
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Section.PEGSection.PEGSection
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Section.RebarLayers.RebarLayers
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Section.SectionLayer.SectionLayer
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Section.SectionLayerArray.SectionLayerArray
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Section.ShellSection.ShellSection
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Section.SolidSection.SolidSection
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Section.SurfaceSection.SurfaceSection
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Section.TransverseShearBeam.TransverseShearBeam
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Section.TransverseShearShell.TransverseShearShell
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Section.TrussSection.TrussSection
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::
```

## Connector

A connector describes the relative motions between two points. A connector also describes the behavior associated with the relative motion.

### Create connectors

```{eval-rst}
.. autoclass:: abaqus.Connector.ConnectorSection.ConnectorSection
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::

```

### Other Classes

```{eval-rst}

.. toggle::

    .. autoclass:: abaqus.Connector.CDCTerm.CDCTerm
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Connector.CDCTermArray.CDCTermArray
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Connector.ConnectorBehaviorOption.ConnectorBehaviorOption
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Connector.ConnectorBehaviorOptionArray.ConnectorBehaviorOptionArray
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Connector.ConnectorDamage.ConnectorDamage
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Connector.ConnectorDamping.ConnectorDamping
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Connector.ConnectorElasticity.ConnectorElasticity
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Connector.ConnectorFailure.ConnectorFailure
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Connector.ConnectorFriction.ConnectorFriction
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Connector.ConnectorLock.ConnectorLock
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Connector.ConnectorOptions.ConnectorOptions
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Connector.ConnectorPlasticity.ConnectorPlasticity
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Connector.ConnectorPotential.ConnectorPotential
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Connector.ConnectorPotentialArray.ConnectorPotentialArray
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Connector.ConnectorStop.ConnectorStop
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Connector.DerivedComponent.DerivedComponent
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Connector.TangentialBehavior.TangentialBehavior
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Connector.CDCTerm.CDCTerm
        :noindex:

        .. autoclasstoc::

    .. autoclass:: abaqus.Connector.CDCTermArray.CDCTermArray
        :noindex:

        .. autoclasstoc::

    .. autoclass:: abaqus.Connector.ConnectorBehaviorOption.ConnectorBehaviorOption
        :noindex:

        .. autoclasstoc::

    .. autoclass:: abaqus.Connector.ConnectorBehaviorOptionArray.ConnectorBehaviorOptionArray
        :noindex:

        .. autoclasstoc::

    .. autoclass:: abaqus.Connector.ConnectorDamage.ConnectorDamage
        :noindex:

        .. autoclasstoc::

    .. autoclass:: abaqus.Connector.ConnectorDamping.ConnectorDamping
        :noindex:

        .. autoclasstoc::

    .. autoclass:: abaqus.Connector.ConnectorElasticity.ConnectorElasticity
        :noindex:

        .. autoclasstoc::

    .. autoclass:: abaqus.Connector.ConnectorFailure.ConnectorFailure
        :noindex:

        .. autoclasstoc::

    .. autoclass:: abaqus.Connector.ConnectorFriction.ConnectorFriction
        :noindex:

        .. autoclasstoc::

    .. autoclass:: abaqus.Connector.ConnectorLock.ConnectorLock
        :noindex:

        .. autoclasstoc::

    .. autoclass:: abaqus.Connector.ConnectorOptions.ConnectorOptions
        :noindex:

        .. autoclasstoc::

    .. autoclass:: abaqus.Connector.ConnectorPlasticity.ConnectorPlasticity
        :noindex:

        .. autoclasstoc::

    .. autoclass:: abaqus.Connector.ConnectorPotential.ConnectorPotential
        :noindex:

        .. autoclasstoc::

    .. autoclass:: abaqus.Connector.ConnectorPotentialArray.ConnectorPotentialArray
        :noindex:

        .. autoclasstoc::

    .. autoclass:: abaqus.Connector.ConnectorStop.ConnectorStop
        :noindex:

        .. autoclasstoc::

    .. autoclass:: abaqus.Connector.DerivedComponent.DerivedComponent
        :noindex:

        .. autoclasstoc::

    .. autoclass:: abaqus.Connector.TangentialBehavior.TangentialBehavior
        :noindex:

        .. autoclasstoc::
```
