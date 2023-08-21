from __future__ import annotations

from abaqus.DisplayGroup.Leaf import Leaf
from abaqus.DisplayGroup.LeafFromDatums import LeafFromDatums
from abaqus.DisplayGroup.LeafFromDisplayGroup import LeafFromDisplayGroup
from abaqus.DisplayGroup.LeafFromGeometry import LeafFromGeometry
from abaqus.DisplayGroup.LeafFromInstance import LeafFromInstance
from abaqus.DisplayGroup.LeafFromInstanceElementLabels import (
    LeafFromInstanceElementLabels,
)
from abaqus.DisplayGroup.LeafFromInstanceNodeLabels import LeafFromInstanceNodeLabels
from abaqus.DisplayGroup.LeafFromMeshElementLabels import LeafFromMeshElementLabels
from abaqus.DisplayGroup.LeafFromMeshNodeLabels import LeafFromMeshNodeLabels
from abaqus.DisplayGroup.LeafFromMeshSurfaceSets import LeafFromMeshSurfaceSets
from abaqus.DisplayGroup.LeafFromPartElementLabels import LeafFromPartElementLabels
from abaqus.DisplayGroup.LeafFromPartNodeLabels import LeafFromPartNodeLabels
from abaqus.DisplayGroup.LeafFromReferencePoint import LeafFromReferencePoint
from abaqus.DisplayGroup.LeafFromSets import LeafFromSets
from abaqus.UtilityAndView.abaqusConstants import (
    ADD,
    ALL,
    ALL_DATUMS,
    ALL_DISTRIB_CONTINUUM_COUPLING,
    ALL_DISTRIB_COUPLING,
    ALL_DISTRIB_STRUCTURAL_COUPLING,
    ALL_ELEMENTS,
    ALL_GEOMETRY,
    ALL_KINEM_COUPLING,
    ALL_MPCS,
    ALL_NODES,
    ALL_RIGID_BODY,
    ALL_SHELL_SOLID_COUPLING,
    ALL_SURFACES,
    ALL_TIES,
    ASSEMBLY,
    DEFAULT_MODEL,
    EITHER,
    EMPTY_LEAF,
    INTERSECTION,
    NEGATE,
    REMOVE,
    REPLACE,
)

# Inspected from Abaqus 2021
__all__ = [
    "ADD",
    "ALL",
    "ALL_DATUMS",
    "ALL_DISTRIB_CONTINUUM_COUPLING",
    "ALL_DISTRIB_COUPLING",
    "ALL_DISTRIB_STRUCTURAL_COUPLING",
    "ALL_ELEMENTS",
    "ALL_GEOMETRY",
    "ALL_KINEM_COUPLING",
    "ALL_MPCS",
    "ALL_NODES",
    "ALL_RIGID_BODY",
    "ALL_SHELL_SOLID_COUPLING",
    "ALL_SURFACES",
    "ALL_TIES",
    "ASSEMBLY",
    "DEFAULT_MODEL",
    # "DatumsLeafType",
    # "DisplayGroupKnotType",
    # "DisplayGroupLeafType",
    # "DisplayGroupMdbInstanceType",
    # "DisplayGroupType",
    "EITHER",
    "EMPTY_LEAF",
    # "ElementLabelLeafType",
    # "EnumerationLeafType",
    # "GeometryLeafType",
    "INTERSECTION",
    "Leaf",
    "LeafFromDatums",
    "LeafFromDisplayGroup",
    "LeafFromGeometry",
    "LeafFromInstance",
    "LeafFromInstanceElementLabels",
    "LeafFromInstanceNodeLabels",
    "LeafFromMeshElementLabels",
    "LeafFromMeshNodeLabels",
    "LeafFromMeshSurfaceSets",
    "LeafFromPartElementLabels",
    "LeafFromPartNodeLabels",
    "LeafFromReferencePoint",
    "LeafFromSets",
    # "LeafType",
    "NEGATE",
    # "NodeLabelLeafType",
    # "ODB",
    # "PART",
    # "PART_ASSEMBLY",
    # "PickingExpressionMdbType",
    "REMOVE",
    "REPLACE",
    # "RefPtLeafType",
    # "SetsLeafType",
    # "SurfaceSetsLeafType",
    "__builtins__",
    "__doc__",
    "__name__",
    "__package__",
]
