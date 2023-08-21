from __future__ import annotations

from abaqus.DisplayGroup.Leaf import Leaf
from abaqus.DisplayGroup.LeafFromDisplayGroup import LeafFromDisplayGroup
from abaqus.DisplayGroup.LeafFromElementLabels import LeafFromElementLabels
from abaqus.DisplayGroup.LeafFromElementSets import LeafFromElementSets
from abaqus.DisplayGroup.LeafFromElementVarRange import LeafFromElementVarRange
from abaqus.DisplayGroup.LeafFromModelElemLabels import LeafFromModelElemLabels
from abaqus.DisplayGroup.LeafFromModelNodeLabels import LeafFromModelNodeLabels
from abaqus.DisplayGroup.LeafFromNodeLabels import LeafFromNodeLabels
from abaqus.DisplayGroup.LeafFromNodeSets import LeafFromNodeSets
from abaqus.DisplayGroup.LeafFromNodeVarRange import LeafFromNodeVarRange
from abaqus.DisplayGroup.LeafFromOdbEdgePick import LeafFromOdbEdgePick
from abaqus.DisplayGroup.LeafFromOdbElementLayups import LeafFromOdbElementLayups
from abaqus.DisplayGroup.LeafFromOdbElementMaterials import LeafFromOdbElementMaterials
from abaqus.DisplayGroup.LeafFromOdbElementPick import LeafFromOdbElementPick
from abaqus.DisplayGroup.LeafFromOdbElementPlies import LeafFromOdbElementPlies
from abaqus.DisplayGroup.LeafFromOdbElementSections import LeafFromOdbElementSections
from abaqus.DisplayGroup.LeafFromOdbElementTypes import LeafFromOdbElementTypes
from abaqus.DisplayGroup.LeafFromOdbNodePick import LeafFromOdbNodePick
from abaqus.DisplayGroup.LeafFromPartInstance import LeafFromPartInstance
from abaqus.DisplayGroup.LeafFromSurfaceSets import LeafFromSurfaceSets
from abaqus.DisplayGroup.LeafFromSurfaceVarRange import LeafFromSurfaceVarRange
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
    # "ConstraintLeafType",
    # "ConstraintNodeLeafType",
    # "CsysLeafType",
    "DEFAULT_MODEL",
    # "DGCommonOptionsType",
    # "DGContourOptionsType",
    # "DGOrientationOptionsType",
    # "DGSuperimposeOptionsType",
    # "DGSymbolOptionsType",
    # "DisplayGroupKnotType",
    # "DisplayGroupLeafType",
    # "DisplayGroupOdbInstanceType",
    # "DisplayGroupType",
    "EITHER",
    "EMPTY_LEAF",
    # "EdgePickLeafType",
    # "ElementLayupLeafType",
    # "ElementMaterialLeafType",
    # "ElementPickLeafType",
    # "ElementPlyLeafType",
    # "ElementSectionLeafType",
    # "ElementTypeLeafType",
    # "ElementVariableRangeLeafType",
    # "EnumerationLeafType",
    "INTERSECTION",
    "Leaf",
    # "LeafFromConstraintNodes",
    "LeafFromDisplayGroup",
    "LeafFromElementLabels",
    "LeafFromElementSets",
    "LeafFromElementVarRange",
    "LeafFromModelElemLabels",
    "LeafFromModelNodeLabels",
    "LeafFromNodeLabels",
    "LeafFromNodeSets",
    "LeafFromNodeVarRange",
    # "LeafFromOdbCoordSystem",
    "LeafFromOdbEdgePick",
    "LeafFromOdbElementLayups",
    "LeafFromOdbElementMaterials",
    "LeafFromOdbElementPick",
    "LeafFromOdbElementPlies",
    "LeafFromOdbElementSections",
    "LeafFromOdbElementTypes",
    "LeafFromOdbNodePick",
    # "LeafFromOdbSurfacePick",
    "LeafFromPartInstance",
    # "LeafFromPath",
    "LeafFromSurfaceSets",
    "LeafFromSurfaceVarRange",
    # "LeafFromUserCoordSystem",
    # "LeafType",
    # "ModelElementLabelLeafType",
    # "ModelNodeLabelLeafType",
    "NEGATE",
    # "NodePickLeafType",
    # "NodeVarRangeLeafType",
    # "ODB",
    # "OdbDisplayOptionsType",
    # "PART",
    # "PART_ASSEMBLY",
    # "PartElementLabelLeafType",
    # "PartElementSetLeafType",
    # "PartInstanceLeafType",
    # "PartNodeLabelLeafType",
    # "PartNodeSetLeafType",
    # "PartSurfaceSetLeafType",
    # "PathLeafType",
    "REMOVE",
    "REPLACE",
    # "SurfVariableRangeLeafType",
    # "SurfacePickLeafType",
    "__builtins__",
    "__doc__",
    "__name__",
    "__package__",
]
