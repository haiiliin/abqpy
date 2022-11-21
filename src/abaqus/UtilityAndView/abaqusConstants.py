from typing import Union

from auto_all import start_all, end_all
from typing_extensions import Literal

start_all()

from .AbaqusBoolean import AbaqusBoolean
from .SymbolicConstant import SymbolicConstant, abaqusConstants

# Alias for methods type annotation
Boolean = Union[AbaqusBoolean, bool]

# Additional alias from original module `symbolicConstants.py`
BooleanType = bool
AbaqusBooleanType = AbaqusBoolean
SymbolicConstantType = SymbolicConstant

# Variables with simple values from original module `symbolicConstants.py`
TRUE = True
FALSE = False
ON = AbaqusBoolean(1)
OFF = AbaqusBoolean(0)

# Variables from original module `abaqusConstantsSupplement.py`
"""
abaqusConstantsSupplement.py

This module is included by abaqusConstants and contains SymbolicConstants
required by ABAQUS that are not defined in C++

"""
ALL_TYPES = abaqusConstants.ALL_TYPES
ALL_METHODS = abaqusConstants.ALL_METHODS
EARLIEST = abaqusConstants.EARLIEST
GUI = abaqusConstants.GUI
KERNEL = abaqusConstants.KERNEL
LATEST = abaqusConstants.LATEST

# Variables from original module `abaqusConstants.py`
A0 = abaqusConstants.A0
A1 = abaqusConstants.A1
A2 = abaqusConstants.A2
A3 = abaqusConstants.A3
A4 = abaqusConstants.A4
A5 = abaqusConstants.A5
ABAQUS = abaqusConstants.ABAQUS
ABAQUS_AQUA = abaqusConstants.ABAQUS_AQUA
ABAQUS_BIORID = abaqusConstants.ABAQUS_BIORID
ABAQUS_CEL = abaqusConstants.ABAQUS_CEL
ABAQUS_CFD = abaqusConstants.ABAQUS_CFD
ABAQUS_DESIGN = abaqusConstants.ABAQUS_DESIGN
ABAQUS_EXPLICIT = abaqusConstants.ABAQUS_EXPLICIT
ABAQUS_STANDARD = abaqusConstants.ABAQUS_STANDARD
ABORTED = abaqusConstants.ABORTED
ABS = abaqusConstants.ABS
ABSCISSA = abaqusConstants.ABSCISSA
ABSOLUTE = abaqusConstants.ABSOLUTE
ABSOLUTE_DIFFERENCE = abaqusConstants.ABSOLUTE_DIFFERENCE
ABSOLUTE_DISTANCE = abaqusConstants.ABSOLUTE_DISTANCE
ABSOLUTE_EQUAL = abaqusConstants.ABSOLUTE_EQUAL
ABSOLUTE_GREATER_THAN_EQUAL = abaqusConstants.ABSOLUTE_GREATER_THAN_EQUAL
ABSOLUTE_GROWTH_MOVEMENT = abaqusConstants.ABSOLUTE_GROWTH_MOVEMENT
ABSOLUTE_LESS_THAN_EQUAL = abaqusConstants.ABSOLUTE_LESS_THAN_EQUAL
ABSOLUTE_SHRINK_MOVEMENT = abaqusConstants.ABSOLUTE_SHRINK_MOVEMENT
ABSOLUTE_VALUE = abaqusConstants.ABSOLUTE_VALUE
ABS_DEFAULT = abaqusConstants.ABS_DEFAULT
AC1D2 = abaqusConstants.AC1D2
AC1D3 = abaqusConstants.AC1D3
AC2D3 = abaqusConstants.AC2D3
AC2D4 = abaqusConstants.AC2D4
AC2D4R = abaqusConstants.AC2D4R
AC2D6 = abaqusConstants.AC2D6
AC2D8 = abaqusConstants.AC2D8
AC3D10 = abaqusConstants.AC3D10
AC3D15 = abaqusConstants.AC3D15
AC3D20 = abaqusConstants.AC3D20
AC3D4 = abaqusConstants.AC3D4
AC3D6 = abaqusConstants.AC3D6
AC3D8 = abaqusConstants.AC3D8
AC3D8R = abaqusConstants.AC3D8R
ACAX3 = abaqusConstants.ACAX3
ACAX4 = abaqusConstants.ACAX4
ACAX4R = abaqusConstants.ACAX4R
ACAX6 = abaqusConstants.ACAX6
ACAX8 = abaqusConstants.ACAX8
ACCELERATION = abaqusConstants.ACCELERATION
ACCELEROMETER = abaqusConstants.ACCELEROMETER
ACIN2D2 = abaqusConstants.ACIN2D2
ACIN2D3 = abaqusConstants.ACIN2D3
ACIN3D3 = abaqusConstants.ACIN3D3
ACIN3D4 = abaqusConstants.ACIN3D4
ACIN3D6 = abaqusConstants.ACIN3D6
ACIN3D8 = abaqusConstants.ACIN3D8
ACINAX2 = abaqusConstants.ACINAX2
ACINAX3 = abaqusConstants.ACINAX3
ACOUSTIC = abaqusConstants.ACOUSTIC
ACOUSTICS = abaqusConstants.ACOUSTICS
ACOUSTIC_INTENSITY = abaqusConstants.ACOUSTIC_INTENSITY
ACROSS = abaqusConstants.ACROSS
ACTIVE_CUT_RANGE = abaqusConstants.ACTIVE_CUT_RANGE
AC_OFF = abaqusConstants.AC_OFF
AC_ON = abaqusConstants.AC_ON
AC_PROJECTION = abaqusConstants.AC_PROJECTION
ADAPTIVE_MESHING = abaqusConstants.ADAPTIVE_MESHING
ADAPTIVE_MESH_SMOOTHING_FAILED = abaqusConstants.ADAPTIVE_MESH_SMOOTHING_FAILED
ADD = abaqusConstants.ADD
ADJUST = abaqusConstants.ADJUST
ADJUST_LENGTH = abaqusConstants.ADJUST_LENGTH
ADMITTANCE = abaqusConstants.ADMITTANCE
ADVANCING_FRONT = abaqusConstants.ADVANCING_FRONT
AFTER = abaqusConstants.AFTER
AGGRESSIVE = abaqusConstants.AGGRESSIVE
AIR_BLAST = abaqusConstants.AIR_BLAST
ALGORITHM = abaqusConstants.ALGORITHM
ALIGN = abaqusConstants.ALIGN
ALL = abaqusConstants.ALL
ALLISO = abaqusConstants.ALLISO
ALLOW_SUBCYCLING = abaqusConstants.ALLOW_SUBCYCLING
ALLSTAR = abaqusConstants.ALLSTAR
ALL_DAMAGE_STEPS = abaqusConstants.ALL_DAMAGE_STEPS
ALL_DATUMS = abaqusConstants.ALL_DATUMS
ALL_DIRECT = abaqusConstants.ALL_DIRECT
ALL_DIRECT_COMPONENTS = abaqusConstants.ALL_DIRECT_COMPONENTS
ALL_DISTRIB_CONTINUUM_COUPLING = abaqusConstants.ALL_DISTRIB_CONTINUUM_COUPLING
ALL_DISTRIB_COUPLING = abaqusConstants.ALL_DISTRIB_COUPLING
ALL_DISTRIB_STRUCTURAL_COUPLING = abaqusConstants.ALL_DISTRIB_STRUCTURAL_COUPLING
ALL_EDGES = abaqusConstants.ALL_EDGES
ALL_ELEMENTS = abaqusConstants.ALL_ELEMENTS
ALL_FRAMES = abaqusConstants.ALL_FRAMES
ALL_FREQUENCIES = abaqusConstants.ALL_FREQUENCIES
ALL_GEOMETRY = abaqusConstants.ALL_GEOMETRY
ALL_INCREMENTS = abaqusConstants.ALL_INCREMENTS
ALL_KINEM_COUPLING = abaqusConstants.ALL_KINEM_COUPLING
ALL_LOCATIONS = abaqusConstants.ALL_LOCATIONS
ALL_MODAL_STEPS = abaqusConstants.ALL_MODAL_STEPS
ALL_MPCS = abaqusConstants.ALL_MPCS
ALL_NODAL_DIAMETER = abaqusConstants.ALL_NODAL_DIAMETER
ALL_NODES = abaqusConstants.ALL_NODES
ALL_NONLINEAR_STEPS = abaqusConstants.ALL_NONLINEAR_STEPS
ALL_PRINCIPALS = abaqusConstants.ALL_PRINCIPALS
ALL_PRINCIPAL_COMPONENTS = abaqusConstants.ALL_PRINCIPAL_COMPONENTS
ALL_RIGID_BODY = abaqusConstants.ALL_RIGID_BODY
ALL_SHELL_SOLID_COUPLING = abaqusConstants.ALL_SHELL_SOLID_COUPLING
ALL_STATIC_STEPS = abaqusConstants.ALL_STATIC_STEPS
ALL_SURFACES = abaqusConstants.ALL_SURFACES
ALL_TIES = abaqusConstants.ALL_TIES
ALWAYS = abaqusConstants.ALWAYS
AMBIENT = abaqusConstants.AMBIENT
AMG = abaqusConstants.AMG
AMPLITUDE = abaqusConstants.AMPLITUDE
AMS = abaqusConstants.AMS
ANALYSIS = abaqusConstants.ANALYSIS
ANALYSIS_CHECKS = abaqusConstants.ANALYSIS_CHECKS
ANALYSIS_DEFAULT = abaqusConstants.ANALYSIS_DEFAULT
ANALYSIS_PRODUCT_DEFAULT = abaqusConstants.ANALYSIS_PRODUCT_DEFAULT
ANALYTICAL_FIELD = abaqusConstants.ANALYTICAL_FIELD
ANALYTIC_RIGID_SURFACE = abaqusConstants.ANALYTIC_RIGID_SURFACE
ANGLE = abaqusConstants.ANGLE
ANGLE_0 = abaqusConstants.ANGLE_0
ANGLE_45 = abaqusConstants.ANGLE_45
ANGLE_90 = abaqusConstants.ANGLE_90
ANGLE_NEG45 = abaqusConstants.ANGLE_NEG45
ANGULAR = abaqusConstants.ANGULAR
ANGULAR_DEVIATION = abaqusConstants.ANGULAR_DEVIATION
ANGULAR_MOMENTUM = abaqusConstants.ANGULAR_MOMENTUM
ANIMATION = abaqusConstants.ANIMATION
ANISOTROPIC = abaqusConstants.ANISOTROPIC
ANNEAL = abaqusConstants.ANNEAL
ANNEALING = abaqusConstants.ANNEALING
ANTIALIASING = abaqusConstants.ANTIALIASING
ANY_JOB = abaqusConstants.ANY_JOB
ANY_MESSAGE_TYPE = abaqusConstants.ANY_MESSAGE_TYPE
APPLY_FORCE = abaqusConstants.APPLY_FORCE
AQUA = abaqusConstants.AQUA
ARC = abaqusConstants.ARC
ARC_LENGTH = abaqusConstants.ARC_LENGTH
AREA = abaqusConstants.AREA
AREA_VELOCITY_SQUARED = abaqusConstants.AREA_VELOCITY_SQUARED
ARRAY = abaqusConstants.ARRAY
ARRAY_1D = abaqusConstants.ARRAY_1D
ARRHENIUS = abaqusConstants.ARRHENIUS
ARROW = abaqusConstants.ARROW
ARRUDA_BOYCE = abaqusConstants.ARRUDA_BOYCE
ASCENDING = abaqusConstants.ASCENDING
ASI2D2 = abaqusConstants.ASI2D2
ASI2D3 = abaqusConstants.ASI2D3
ASI3D3 = abaqusConstants.ASI3D3
ASI3D4 = abaqusConstants.ASI3D4
ASI3D6 = abaqusConstants.ASI3D6
ASI3D8 = abaqusConstants.ASI3D8
ASIAX2 = abaqusConstants.ASIAX2
ASIAX3 = abaqusConstants.ASIAX3
ASPECT_RATIO = abaqusConstants.ASPECT_RATIO
ASSEMBLY = abaqusConstants.ASSEMBLY
ASSEMBLY_LOAD = abaqusConstants.ASSEMBLY_LOAD
ASSEMBLY_MAP = abaqusConstants.ASSEMBLY_MAP
ASSEMBLY_MAP_COLORS = abaqusConstants.ASSEMBLY_MAP_COLORS
ASSEMBLY_SET = abaqusConstants.ASSEMBLY_SET
AS_DISPLAYED = abaqusConstants.AS_DISPLAYED
AS_IS = abaqusConstants.AS_IS
ATTACH_TO_POINT = abaqusConstants.ATTACH_TO_POINT
ATTACH_TO_REGION = abaqusConstants.ATTACH_TO_REGION
AT_BEGINNING = abaqusConstants.AT_BEGINNING
AUGMENTED_LAGRANGE = abaqusConstants.AUGMENTED_LAGRANGE
AUGMENTED_LAGRANGE_INCOMPATIBILITIES = abaqusConstants.AUGMENTED_LAGRANGE_INCOMPATIBILITIES
AUTO = abaqusConstants.AUTO
AUTOCAD = abaqusConstants.AUTOCAD
AUTOCOMPUTE = abaqusConstants.AUTOCOMPUTE
AUTOMATIC = abaqusConstants.AUTOMATIC
AUTOMATIC_EBE = abaqusConstants.AUTOMATIC_EBE
AUTOMATIC_GLOBAL = abaqusConstants.AUTOMATIC_GLOBAL
AUTO_ALIGN = abaqusConstants.AUTO_ALIGN
AUTO_FIT = abaqusConstants.AUTO_FIT
AUTO_FIT_PTS = abaqusConstants.AUTO_FIT_PTS
AUTO_INCREMENTATION = abaqusConstants.AUTO_INCREMENTATION
AUTO_TIGHT = abaqusConstants.AUTO_TIGHT
AVERAGE = abaqusConstants.AVERAGE
AVERAGE_EDGE_LENGTH = abaqusConstants.AVERAGE_EDGE_LENGTH
AVERAGE_SIZE = abaqusConstants.AVERAGE_SIZE
AVERAGE_STRAIN = abaqusConstants.AVERAGE_STRAIN
AVERAGE_TRANSLATION = abaqusConstants.AVERAGE_TRANSLATION
AVERAGING_REGION_MAP = abaqusConstants.AVERAGING_REGION_MAP
AVERAGING_REGION_MAP_COLORS = abaqusConstants.AVERAGING_REGION_MAP_COLORS
AVI = abaqusConstants.AVI
AXIAL = abaqusConstants.AXIAL
AXIAL_FORCE_CONSTRAINT = abaqusConstants.AXIAL_FORCE_CONSTRAINT
AXISYM = abaqusConstants.AXISYM
AXISYMMETRIC = abaqusConstants.AXISYMMETRIC
AXIS_1 = abaqusConstants.AXIS_1
AXIS_2 = abaqusConstants.AXIS_2
AXIS_3 = abaqusConstants.AXIS_3
B21 = abaqusConstants.B21
B21H = abaqusConstants.B21H
B22 = abaqusConstants.B22
B22H = abaqusConstants.B22H
B23 = abaqusConstants.B23
B23H = abaqusConstants.B23H
B31 = abaqusConstants.B31
B31H = abaqusConstants.B31H
B31OS = abaqusConstants.B31OS
B31OSH = abaqusConstants.B31OSH
B32 = abaqusConstants.B32
B32H = abaqusConstants.B32H
B32OS = abaqusConstants.B32OS
B32OSH = abaqusConstants.B32OSH
B33 = abaqusConstants.B33
B33H = abaqusConstants.B33H
BACKWARD_EULER = abaqusConstants.BACKWARD_EULER
BALANCED = abaqusConstants.BALANCED
BANDED = abaqusConstants.BANDED
BAR = abaqusConstants.BAR
BASE = abaqusConstants.BASE
BATCHPRE_PHASE = abaqusConstants.BATCHPRE_PHASE
BCGS = abaqusConstants.BCGS
BC_MAP = abaqusConstants.BC_MAP
BC_MAP_COLORS = abaqusConstants.BC_MAP_COLORS
BEAM = abaqusConstants.BEAM
BEAM_MPC = abaqusConstants.BEAM_MPC
BEFORE = abaqusConstants.BEFORE
BEFORE_ANALYSIS = abaqusConstants.BEFORE_ANALYSIS
BELOW_MIN = abaqusConstants.BELOW_MIN
BENDING = abaqusConstants.BENDING
BEST_FIT = abaqusConstants.BEST_FIT
BETWEEN_CAVITIES = abaqusConstants.BETWEEN_CAVITIES
BIASED = abaqusConstants.BIASED
BIAS_MAX_SIZE = abaqusConstants.BIAS_MAX_SIZE
BIAS_METHOD = abaqusConstants.BIAS_METHOD
BIAS_MIN_SIZE = abaqusConstants.BIAS_MIN_SIZE
BIAS_RATIO = abaqusConstants.BIAS_RATIO
BIAXIAL = abaqusConstants.BIAXIAL
BIDIRECTIONAL = abaqusConstants.BIDIRECTIONAL
BILINEAR = abaqusConstants.BILINEAR
BIMOMENT = abaqusConstants.BIMOMENT
BK = abaqusConstants.BK
BLACK_AND_WHITE = abaqusConstants.BLACK_AND_WHITE
BLACK_TO_WHITE = abaqusConstants.BLACK_TO_WHITE
BLEND = abaqusConstants.BLEND
BLOCKING_ALL = abaqusConstants.BLOCKING_ALL
BLUE_TO_RED = abaqusConstants.BLUE_TO_RED
BOLT = abaqusConstants.BOLT
BOOLEAN = abaqusConstants.BOOLEAN
BOTH = abaqusConstants.BOTH
BOTHSIDES = abaqusConstants.BOTHSIDES
BOTH_SIDES = abaqusConstants.BOTH_SIDES
BOTH_SURFACES = abaqusConstants.BOTH_SURFACES
BOTTOM = abaqusConstants.BOTTOM
BOTTOM_CENTER = abaqusConstants.BOTTOM_CENTER
BOTTOM_LEFT = abaqusConstants.BOTTOM_LEFT
BOTTOM_RIGHT = abaqusConstants.BOTTOM_RIGHT
BOTTOM_SURFACE = abaqusConstants.BOTTOM_SURFACE
BOTTOM_UP = abaqusConstants.BOTTOM_UP
BOUNDARY_CONDITION = abaqusConstants.BOUNDARY_CONDITION
BOUNDARY_ONLY = abaqusConstants.BOUNDARY_ONLY
BOX_OFF = abaqusConstants.BOX_OFF
BOX_ON = abaqusConstants.BOX_ON
BUCKLE = abaqusConstants.BUCKLE
BUCKLING_MODES = abaqusConstants.BUCKLING_MODES
BUILT_INTO_BASE_STATE = abaqusConstants.BUILT_INTO_BASE_STATE
BUILT_INTO_MODES = abaqusConstants.BUILT_INTO_MODES
BULK_VISCOSITY = abaqusConstants.BULK_VISCOSITY
BUSHING = abaqusConstants.BUSHING
BY_NUMBER = abaqusConstants.BY_NUMBER
BY_SPACING = abaqusConstants.BY_SPACING
C3D10 = abaqusConstants.C3D10
C3D10E = abaqusConstants.C3D10E
C3D10H = abaqusConstants.C3D10H
C3D10I = abaqusConstants.C3D10I
C3D10M = abaqusConstants.C3D10M
C3D10MH = abaqusConstants.C3D10MH
C3D10MHT = abaqusConstants.C3D10MHT
C3D10MP = abaqusConstants.C3D10MP
C3D10MPH = abaqusConstants.C3D10MPH
C3D10MPT = abaqusConstants.C3D10MPT
C3D10MT = abaqusConstants.C3D10MT
C3D15 = abaqusConstants.C3D15
C3D15E = abaqusConstants.C3D15E
C3D15H = abaqusConstants.C3D15H
C3D20 = abaqusConstants.C3D20
C3D20E = abaqusConstants.C3D20E
C3D20H = abaqusConstants.C3D20H
C3D20HT = abaqusConstants.C3D20HT
C3D20P = abaqusConstants.C3D20P
C3D20PH = abaqusConstants.C3D20PH
C3D20R = abaqusConstants.C3D20R
C3D20RE = abaqusConstants.C3D20RE
C3D20RH = abaqusConstants.C3D20RH
C3D20RHT = abaqusConstants.C3D20RHT
C3D20RP = abaqusConstants.C3D20RP
C3D20RPH = abaqusConstants.C3D20RPH
C3D20RT = abaqusConstants.C3D20RT
C3D20T = abaqusConstants.C3D20T
C3D4 = abaqusConstants.C3D4
C3D4E = abaqusConstants.C3D4E
C3D4H = abaqusConstants.C3D4H
C3D4P = abaqusConstants.C3D4P
C3D4T = abaqusConstants.C3D4T
C3D6 = abaqusConstants.C3D6
C3D6E = abaqusConstants.C3D6E
C3D6H = abaqusConstants.C3D6H
C3D6P = abaqusConstants.C3D6P
C3D6T = abaqusConstants.C3D6T
C3D8 = abaqusConstants.C3D8
C3D8E = abaqusConstants.C3D8E
C3D8H = abaqusConstants.C3D8H
C3D8HT = abaqusConstants.C3D8HT
C3D8I = abaqusConstants.C3D8I
C3D8IH = abaqusConstants.C3D8IH
C3D8P = abaqusConstants.C3D8P
C3D8PH = abaqusConstants.C3D8PH
C3D8PHT = abaqusConstants.C3D8PHT
C3D8PT = abaqusConstants.C3D8PT
C3D8R = abaqusConstants.C3D8R
C3D8RH = abaqusConstants.C3D8RH
C3D8RHT = abaqusConstants.C3D8RHT
C3D8RP = abaqusConstants.C3D8RP
C3D8RPH = abaqusConstants.C3D8RPH
C3D8RPHT = abaqusConstants.C3D8RPHT
C3D8RPT = abaqusConstants.C3D8RPT
C3D8RT = abaqusConstants.C3D8RT
C3D8T = abaqusConstants.C3D8T
CALCULATE = abaqusConstants.CALCULATE
CALCULATOR_PHASE = abaqusConstants.CALCULATOR_PHASE
CAMERA = abaqusConstants.CAMERA
CARDAN = abaqusConstants.CARDAN
CARMAN_KOZENY = abaqusConstants.CARMAN_KOZENY
CARTESIAN = abaqusConstants.CARTESIAN
CATEGORY_BASED = abaqusConstants.CATEGORY_BASED
CAVITY = abaqusConstants.CAVITY
CAVITY_RADIATION = abaqusConstants.CAVITY_RADIATION
CAVITY_RADIATION_EMMISIVITY_TOO_LARGE = abaqusConstants.CAVITY_RADIATION_EMMISIVITY_TOO_LARGE
CAVITY_RADIATION_PARALLEL_DECOMPOSITION = abaqusConstants.CAVITY_RADIATION_PARALLEL_DECOMPOSITION
CAX3 = abaqusConstants.CAX3
CAX3E = abaqusConstants.CAX3E
CAX3H = abaqusConstants.CAX3H
CAX3T = abaqusConstants.CAX3T
CAX4 = abaqusConstants.CAX4
CAX4E = abaqusConstants.CAX4E
CAX4H = abaqusConstants.CAX4H
CAX4HT = abaqusConstants.CAX4HT
CAX4I = abaqusConstants.CAX4I
CAX4IH = abaqusConstants.CAX4IH
CAX4P = abaqusConstants.CAX4P
CAX4PH = abaqusConstants.CAX4PH
CAX4R = abaqusConstants.CAX4R
CAX4RH = abaqusConstants.CAX4RH
CAX4RHT = abaqusConstants.CAX4RHT
CAX4RP = abaqusConstants.CAX4RP
CAX4RPH = abaqusConstants.CAX4RPH
CAX4RT = abaqusConstants.CAX4RT
CAX4T = abaqusConstants.CAX4T
CAX6 = abaqusConstants.CAX6
CAX6E = abaqusConstants.CAX6E
CAX6H = abaqusConstants.CAX6H
CAX6M = abaqusConstants.CAX6M
CAX6MH = abaqusConstants.CAX6MH
CAX6MHT = abaqusConstants.CAX6MHT
CAX6MP = abaqusConstants.CAX6MP
CAX6MPH = abaqusConstants.CAX6MPH
CAX6MT = abaqusConstants.CAX6MT
CAX8 = abaqusConstants.CAX8
CAX8E = abaqusConstants.CAX8E
CAX8H = abaqusConstants.CAX8H
CAX8HT = abaqusConstants.CAX8HT
CAX8P = abaqusConstants.CAX8P
CAX8PH = abaqusConstants.CAX8PH
CAX8R = abaqusConstants.CAX8R
CAX8RE = abaqusConstants.CAX8RE
CAX8RH = abaqusConstants.CAX8RH
CAX8RHT = abaqusConstants.CAX8RHT
CAX8RP = abaqusConstants.CAX8RP
CAX8RPH = abaqusConstants.CAX8RPH
CAX8RT = abaqusConstants.CAX8RT
CAX8T = abaqusConstants.CAX8T
CAXA41 = abaqusConstants.CAXA41
CAXA42 = abaqusConstants.CAXA42
CAXA43 = abaqusConstants.CAXA43
CAXA44 = abaqusConstants.CAXA44
CAXA4H1 = abaqusConstants.CAXA4H1
CAXA4H2 = abaqusConstants.CAXA4H2
CAXA4H3 = abaqusConstants.CAXA4H3
CAXA4H4 = abaqusConstants.CAXA4H4
CAXA4R1 = abaqusConstants.CAXA4R1
CAXA4R2 = abaqusConstants.CAXA4R2
CAXA4R3 = abaqusConstants.CAXA4R3
CAXA4R4 = abaqusConstants.CAXA4R4
CAXA4RH1 = abaqusConstants.CAXA4RH1
CAXA4RH2 = abaqusConstants.CAXA4RH2
CAXA4RH3 = abaqusConstants.CAXA4RH3
CAXA4RH4 = abaqusConstants.CAXA4RH4
CAXA81 = abaqusConstants.CAXA81
CAXA82 = abaqusConstants.CAXA82
CAXA83 = abaqusConstants.CAXA83
CAXA84 = abaqusConstants.CAXA84
CAXA8H1 = abaqusConstants.CAXA8H1
CAXA8H2 = abaqusConstants.CAXA8H2
CAXA8H3 = abaqusConstants.CAXA8H3
CAXA8H4 = abaqusConstants.CAXA8H4
CAXA8P1 = abaqusConstants.CAXA8P1
CAXA8P2 = abaqusConstants.CAXA8P2
CAXA8P3 = abaqusConstants.CAXA8P3
CAXA8P4 = abaqusConstants.CAXA8P4
CAXA8R1 = abaqusConstants.CAXA8R1
CAXA8R2 = abaqusConstants.CAXA8R2
CAXA8R3 = abaqusConstants.CAXA8R3
CAXA8R4 = abaqusConstants.CAXA8R4
CAXA8RH1 = abaqusConstants.CAXA8RH1
CAXA8RH2 = abaqusConstants.CAXA8RH2
CAXA8RH3 = abaqusConstants.CAXA8RH3
CAXA8RH4 = abaqusConstants.CAXA8RH4
CAXA8RP1 = abaqusConstants.CAXA8RP1
CAXA8RP2 = abaqusConstants.CAXA8RP2
CAXA8RP3 = abaqusConstants.CAXA8RP3
CAXA8RP4 = abaqusConstants.CAXA8RP4
CCL12 = abaqusConstants.CCL12
CCL12H = abaqusConstants.CCL12H
CCL18 = abaqusConstants.CCL18
CCL18H = abaqusConstants.CCL18H
CCL24 = abaqusConstants.CCL24
CCL24H = abaqusConstants.CCL24H
CCL24R = abaqusConstants.CCL24R
CCL24RH = abaqusConstants.CCL24RH
CCL9 = abaqusConstants.CCL9
CCL9H = abaqusConstants.CCL9H
CCW = abaqusConstants.CCW
CENTER = abaqusConstants.CENTER
CENTER_LEFT = abaqusConstants.CENTER_LEFT
CENTER_OF_MASS = abaqusConstants.CENTER_OF_MASS
CENTER_RIGHT = abaqusConstants.CENTER_RIGHT
CENTROID = abaqusConstants.CENTROID
CFD = abaqusConstants.CFD
CFD_ANALYSIS = abaqusConstants.CFD_ANALYSIS
CFD_PHASE = abaqusConstants.CFD_PHASE
CG = abaqusConstants.CG
CGAX3 = abaqusConstants.CGAX3
CGAX3H = abaqusConstants.CGAX3H
CGAX3HT = abaqusConstants.CGAX3HT
CGAX3T = abaqusConstants.CGAX3T
CGAX4 = abaqusConstants.CGAX4
CGAX4H = abaqusConstants.CGAX4H
CGAX4HT = abaqusConstants.CGAX4HT
CGAX4R = abaqusConstants.CGAX4R
CGAX4RH = abaqusConstants.CGAX4RH
CGAX4RHT = abaqusConstants.CGAX4RHT
CGAX4RT = abaqusConstants.CGAX4RT
CGAX4T = abaqusConstants.CGAX4T
CGAX6 = abaqusConstants.CGAX6
CGAX6H = abaqusConstants.CGAX6H
CGAX6M = abaqusConstants.CGAX6M
CGAX6MH = abaqusConstants.CGAX6MH
CGAX6MHT = abaqusConstants.CGAX6MHT
CGAX6MT = abaqusConstants.CGAX6MT
CGAX8 = abaqusConstants.CGAX8
CGAX8H = abaqusConstants.CGAX8H
CGAX8HT = abaqusConstants.CGAX8HT
CGAX8R = abaqusConstants.CGAX8R
CGAX8RH = abaqusConstants.CGAX8RH
CGAX8RHT = abaqusConstants.CGAX8RHT
CGAX8RT = abaqusConstants.CGAX8RT
CGAX8T = abaqusConstants.CGAX8T
CGPE10 = abaqusConstants.CGPE10
CGPE10H = abaqusConstants.CGPE10H
CGPE10R = abaqusConstants.CGPE10R
CGPE10RH = abaqusConstants.CGPE10RH
CGPE5 = abaqusConstants.CGPE5
CGPE5H = abaqusConstants.CGPE5H
CGPE6 = abaqusConstants.CGPE6
CGPE6H = abaqusConstants.CGPE6H
CGPE6I = abaqusConstants.CGPE6I
CGPE6IH = abaqusConstants.CGPE6IH
CGPE6MH = abaqusConstants.CGPE6MH
CGPE6R = abaqusConstants.CGPE6R
CGPE6RH = abaqusConstants.CGPE6RH
CGPE8 = abaqusConstants.CGPE8
CGPE8H = abaqusConstants.CGPE8H
CHEBYCHEV = abaqusConstants.CHEBYCHEV
CHECKER = abaqusConstants.CHECKER
CHECK_COMPLETED = abaqusConstants.CHECK_COMPLETED
CHECK_RUNNING = abaqusConstants.CHECK_RUNNING
CHECK_SUBMITTED = abaqusConstants.CHECK_SUBMITTED
CINAX4 = abaqusConstants.CINAX4
CINAX5R = abaqusConstants.CINAX5R
CINPE4 = abaqusConstants.CINPE4
CINPE5R = abaqusConstants.CINPE5R
CINPS4 = abaqusConstants.CINPS4
CINPS5R = abaqusConstants.CINPS5R
CIRCLE = abaqusConstants.CIRCLE
CIRCLE_RADIUS = abaqusConstants.CIRCLE_RADIUS
CIRCULAR = abaqusConstants.CIRCULAR
CIRCUM = abaqusConstants.CIRCUM
CIRCUMF = abaqusConstants.CIRCUMF
CIRCUMFERENTIAL = abaqusConstants.CIRCUMFERENTIAL
CIRC_MIRROR_RECT = abaqusConstants.CIRC_MIRROR_RECT
CIRC_RECT_MIRROR = abaqusConstants.CIRC_RECT_MIRROR
CLEARANCE = abaqusConstants.CLEARANCE
CLOCKWISE = abaqusConstants.CLOCKWISE
CLOSEST = abaqusConstants.CLOSEST
CLOSEST_POINT_FRACTION = abaqusConstants.CLOSEST_POINT_FRACTION
CLOSURE_VALUE = abaqusConstants.CLOSURE_VALUE
COARSE = abaqusConstants.COARSE
COD = abaqusConstants.COD
CODEC = abaqusConstants.CODEC
COEFFICIENT = abaqusConstants.COEFFICIENT
COEFFICIENTS = abaqusConstants.COEFFICIENTS
COH2D4 = abaqusConstants.COH2D4
COH2D4P = abaqusConstants.COH2D4P
COH3D6 = abaqusConstants.COH3D6
COH3D6P = abaqusConstants.COH3D6P
COH3D8 = abaqusConstants.COH3D8
COH3D8P = abaqusConstants.COH3D8P
COHAX4 = abaqusConstants.COHAX4
COHAX4P = abaqusConstants.COHAX4P
COLOR = abaqusConstants.COLOR
COMBINED = abaqusConstants.COMBINED
COMMA_SEPARATED_VALUES = abaqusConstants.COMMA_SEPARATED_VALUES
COMPLETED = abaqusConstants.COMPLETED
COMPLEX = abaqusConstants.COMPLEX
COMPLEX_EIGENSOLVER = abaqusConstants.COMPLEX_EIGENSOLVER
COMPLEX_FREQUENCY = abaqusConstants.COMPLEX_FREQUENCY
COMPLEX_MAGNITUDE = abaqusConstants.COMPLEX_MAGNITUDE
COMPLEX_PHASE = abaqusConstants.COMPLEX_PHASE
COMPLEX_VAL_AT_ANGLE = abaqusConstants.COMPLEX_VAL_AT_ANGLE
COMPONENT = abaqusConstants.COMPONENT
COMPONENT_NUMBER = abaqusConstants.COMPONENT_NUMBER
COMPRESSEDINDEX = abaqusConstants.COMPRESSEDINDEX
COMPRESSED_VRML = abaqusConstants.COMPRESSED_VRML
COMPRESSIBLE = abaqusConstants.COMPRESSIBLE
COMPRESSION = abaqusConstants.COMPRESSION
COMPUTE = abaqusConstants.COMPUTE
COMPUTED = abaqusConstants.COMPUTED
COMPUTED_TOLERANCE = abaqusConstants.COMPUTED_TOLERANCE
COMP_DEFAULT = abaqusConstants.COMP_DEFAULT
CONCENTRIC = abaqusConstants.CONCENTRIC
CONDITION_BASED_OPTIMIZATION = abaqusConstants.CONDITION_BASED_OPTIMIZATION
CONN2D2 = abaqusConstants.CONN2D2
CONN3D2 = abaqusConstants.CONN3D2
CONNECTOR = abaqusConstants.CONNECTOR
CONNECTOR_MAP = abaqusConstants.CONNECTOR_MAP
CONNECTOR_MAP_COLORS = abaqusConstants.CONNECTOR_MAP_COLORS
CONNECTOR_PROP_MAP = abaqusConstants.CONNECTOR_PROP_MAP
CONNECTOR_PROP_MAP_COLORS = abaqusConstants.CONNECTOR_PROP_MAP_COLORS
CONNECTOR_TYPE_MAP = abaqusConstants.CONNECTOR_TYPE_MAP
CONNECTOR_TYPE_MAP_COLORS = abaqusConstants.CONNECTOR_TYPE_MAP_COLORS
CONSERVATIVE = abaqusConstants.CONSERVATIVE
CONSOLIDATION = abaqusConstants.CONSOLIDATION
CONSTANT = abaqusConstants.CONSTANT
CONSTANTPRESSURE = abaqusConstants.CONSTANTPRESSURE
CONSTANTS = abaqusConstants.CONSTANTS
CONSTANTVOLUME = abaqusConstants.CONSTANTVOLUME
CONSTANT_RATIO = abaqusConstants.CONSTANT_RATIO
CONSTANT_THROUGH_THICKNESS = abaqusConstants.CONSTANT_THROUGH_THICKNESS
CONSTANT_VELOCITY = abaqusConstants.CONSTANT_VELOCITY
CONSTRAINED_LAPLACIAN = abaqusConstants.CONSTRAINED_LAPLACIAN
CONSTRAINT = abaqusConstants.CONSTRAINT
CONSTRAINT_MAP = abaqusConstants.CONSTRAINT_MAP
CONSTRAINT_MAP_COLORS = abaqusConstants.CONSTRAINT_MAP_COLORS
CONSTRAINT_TYPE_MAP = abaqusConstants.CONSTRAINT_TYPE_MAP
CONSTRAINT_TYPE_MAP_COLORS = abaqusConstants.CONSTRAINT_TYPE_MAP_COLORS
CONSTRUCTION = abaqusConstants.CONSTRUCTION
CONTACT = abaqusConstants.CONTACT
CONTACT_ALL = abaqusConstants.CONTACT_ALL
CONTACT_EXPLICIT = abaqusConstants.CONTACT_EXPLICIT
CONTACT_PRESELECT = abaqusConstants.CONTACT_PRESELECT
CONTACT_STANDARD = abaqusConstants.CONTACT_STANDARD
CONTINUE = abaqusConstants.CONTINUE
CONTINUOUS = abaqusConstants.CONTINUOUS
CONTINUUM = abaqusConstants.CONTINUUM
CONTINUUM_SHELL = abaqusConstants.CONTINUUM_SHELL
CONTOURS_ON_DEF = abaqusConstants.CONTOURS_ON_DEF
CONTOURS_ON_UNDEF = abaqusConstants.CONTOURS_ON_UNDEF
CONTROL_POINTS = abaqusConstants.CONTROL_POINTS
CONVERGENCE = abaqusConstants.CONVERGENCE
CONVERT_SDI_OFF = abaqusConstants.CONVERT_SDI_OFF
CONVERT_SDI_ON = abaqusConstants.CONVERT_SDI_ON
CONWEP = abaqusConstants.CONWEP
COORDINATE = abaqusConstants.COORDINATE
COPLANAR_EDGES = abaqusConstants.COPLANAR_EDGES
CORIOLIS_LOAD = abaqusConstants.CORIOLIS_LOAD
CORRECTION_ACCEPTED = abaqusConstants.CORRECTION_ACCEPTED
CORRECTION_ACCEPTED_ESTIMATED_CORRECTION = abaqusConstants.CORRECTION_ACCEPTED_ESTIMATED_CORRECTION
CORRECTION_ACCEPTED_SMALL_INCREMENT = abaqusConstants.CORRECTION_ACCEPTED_SMALL_INCREMENT
CORRECTION_NOT_ACCEPTED = abaqusConstants.CORRECTION_NOT_ACCEPTED
CORRELATED = abaqusConstants.CORRELATED
COSINE = abaqusConstants.COSINE
COUNT = abaqusConstants.COUNT
COUNTERCLOCKWISE = abaqusConstants.COUNTERCLOCKWISE
COUPLED = abaqusConstants.COUPLED
COUPLED_MOTION = abaqusConstants.COUPLED_MOTION
COUPLED_POSITION = abaqusConstants.COUPLED_POSITION
COUPLED_TEMP_DISPLACEMENT = abaqusConstants.COUPLED_TEMP_DISPLACEMENT
COUPLED_THERMAL_ELECTRIC = abaqusConstants.COUPLED_THERMAL_ELECTRIC
COUPLED_THERMAL_ELECTRICAL = abaqusConstants.COUPLED_THERMAL_ELECTRICAL
COUPLED_THERMAL_ELECTRICAL_STRUCTURAL = abaqusConstants.COUPLED_THERMAL_ELECTRICAL_STRUCTURAL
COUPLED_THERMAL_STRESS = abaqusConstants.COUPLED_THERMAL_STRESS
COUPLED_TRACTION = abaqusConstants.COUPLED_TRACTION
COUPLING_FORCE_CONSTRAINT = abaqusConstants.COUPLING_FORCE_CONSTRAINT
COUPLING_MOMENT_CONSTRAINT = abaqusConstants.COUPLING_MOMENT_CONSTRAINT
CPE3 = abaqusConstants.CPE3
CPE3E = abaqusConstants.CPE3E
CPE3H = abaqusConstants.CPE3H
CPE3T = abaqusConstants.CPE3T
CPE4 = abaqusConstants.CPE4
CPE4E = abaqusConstants.CPE4E
CPE4H = abaqusConstants.CPE4H
CPE4HT = abaqusConstants.CPE4HT
CPE4I = abaqusConstants.CPE4I
CPE4IH = abaqusConstants.CPE4IH
CPE4P = abaqusConstants.CPE4P
CPE4PH = abaqusConstants.CPE4PH
CPE4R = abaqusConstants.CPE4R
CPE4RH = abaqusConstants.CPE4RH
CPE4RHT = abaqusConstants.CPE4RHT
CPE4RP = abaqusConstants.CPE4RP
CPE4RPH = abaqusConstants.CPE4RPH
CPE4RT = abaqusConstants.CPE4RT
CPE4T = abaqusConstants.CPE4T
CPE6 = abaqusConstants.CPE6
CPE6E = abaqusConstants.CPE6E
CPE6H = abaqusConstants.CPE6H
CPE6M = abaqusConstants.CPE6M
CPE6MH = abaqusConstants.CPE6MH
CPE6MHT = abaqusConstants.CPE6MHT
CPE6MP = abaqusConstants.CPE6MP
CPE6MPH = abaqusConstants.CPE6MPH
CPE6MT = abaqusConstants.CPE6MT
CPE8 = abaqusConstants.CPE8
CPE8E = abaqusConstants.CPE8E
CPE8H = abaqusConstants.CPE8H
CPE8HT = abaqusConstants.CPE8HT
CPE8P = abaqusConstants.CPE8P
CPE8PH = abaqusConstants.CPE8PH
CPE8R = abaqusConstants.CPE8R
CPE8RE = abaqusConstants.CPE8RE
CPE8RH = abaqusConstants.CPE8RH
CPE8RHT = abaqusConstants.CPE8RHT
CPE8RP = abaqusConstants.CPE8RP
CPE8RPH = abaqusConstants.CPE8RPH
CPE8RT = abaqusConstants.CPE8RT
CPE8T = abaqusConstants.CPE8T
CPEG3 = abaqusConstants.CPEG3
CPEG3H = abaqusConstants.CPEG3H
CPEG3HT = abaqusConstants.CPEG3HT
CPEG3T = abaqusConstants.CPEG3T
CPEG4 = abaqusConstants.CPEG4
CPEG4H = abaqusConstants.CPEG4H
CPEG4HT = abaqusConstants.CPEG4HT
CPEG4I = abaqusConstants.CPEG4I
CPEG4IH = abaqusConstants.CPEG4IH
CPEG4R = abaqusConstants.CPEG4R
CPEG4RH = abaqusConstants.CPEG4RH
CPEG4RT = abaqusConstants.CPEG4RT
CPEG4RHT = abaqusConstants.CPEG4RHT
CPEG4T = abaqusConstants.CPEG4T
CPEG6 = abaqusConstants.CPEG6
CPEG6H = abaqusConstants.CPEG6H
CPEG6M = abaqusConstants.CPEG6M
CPEG6MH = abaqusConstants.CPEG6MH
CPEG6MHT = abaqusConstants.CPEG6MHT
CPEG6MT = abaqusConstants.CPEG6MT
CPEG8 = abaqusConstants.CPEG8
CPEG8H = abaqusConstants.CPEG8H
CPEG8HT = abaqusConstants.CPEG8HT
CPEG8R = abaqusConstants.CPEG8R
CPEG8RH = abaqusConstants.CPEG8RH
CPEG8RT = abaqusConstants.CPEG8RT
CPEG8RHT = abaqusConstants.CPEG8RHT
CPEG8T = abaqusConstants.CPEG8T
CPS3 = abaqusConstants.CPS3
CPS3E = abaqusConstants.CPS3E
CPS3T = abaqusConstants.CPS3T
CPS4 = abaqusConstants.CPS4
CPS4E = abaqusConstants.CPS4E
CPS4I = abaqusConstants.CPS4I
CPS4R = abaqusConstants.CPS4R
CPS4RT = abaqusConstants.CPS4RT
CPS4T = abaqusConstants.CPS4T
CPS6 = abaqusConstants.CPS6
CPS6E = abaqusConstants.CPS6E
CPS6M = abaqusConstants.CPS6M
CPS6MT = abaqusConstants.CPS6MT
CPS8 = abaqusConstants.CPS8
CPS8E = abaqusConstants.CPS8E
CPS8R = abaqusConstants.CPS8R
CPS8RE = abaqusConstants.CPS8RE
CPS8RT = abaqusConstants.CPS8RT
CPS8T = abaqusConstants.CPS8T
CPU_TIME_XPL = abaqusConstants.CPU_TIME_XPL
CQC = abaqusConstants.CQC
CRACKTIP = abaqusConstants.CRACKTIP
CRACK_GROWTH = abaqusConstants.CRACK_GROWTH
CRACK_LENGTH = abaqusConstants.CRACK_LENGTH
CRACK_NORMAL = abaqusConstants.CRACK_NORMAL
CREATED = abaqusConstants.CREATED
CREEP = abaqusConstants.CREEP
CREEP_OFF = abaqusConstants.CREEP_OFF
CREEP_TEST_DATA = abaqusConstants.CREEP_TEST_DATA
CRITICAL_DAMPING_FRACTION = abaqusConstants.CRITICAL_DAMPING_FRACTION
CRITICAL_STRESS = abaqusConstants.CRITICAL_STRESS
CROSS = abaqusConstants.CROSS
CROSSED_SURFACES = abaqusConstants.CROSSED_SURFACES
CROSSING_VALUE = abaqusConstants.CROSSING_VALUE
CRUSHABLE_FOAM = abaqusConstants.CRUSHABLE_FOAM
CSYS = abaqusConstants.CSYS
CUBIC = abaqusConstants.CUBIC
CUBIC_SPLINE = abaqusConstants.CUBIC_SPLINE
CURRENT = abaqusConstants.CURRENT
CURRENT_DISPLAY_GROUP = abaqusConstants.CURRENT_DISPLAY_GROUP
CURRENT_FRAME = abaqusConstants.CURRENT_FRAME
CURVATURE = abaqusConstants.CURVATURE
CURVATURE_BASED_BY_SIZE = abaqusConstants.CURVATURE_BASED_BY_SIZE
CURVE_LEGEND = abaqusConstants.CURVE_LEGEND
CURVE_NAME = abaqusConstants.CURVE_NAME
CURVE_NAME_LEGEND = abaqusConstants.CURVE_NAME_LEGEND
CUSTOM = abaqusConstants.CUSTOM
CUT = abaqusConstants.CUT
CUT_OFF = abaqusConstants.CUT_OFF
CVJOINT = abaqusConstants.CVJOINT
CW = abaqusConstants.CW
CYCLIC_SYMMETRY = abaqusConstants.CYCLIC_SYMMETRY
CYLINDER = abaqusConstants.CYLINDER
CYLINDRICAL = abaqusConstants.CYLINDRICAL
C_INTEGRAL = abaqusConstants.C_INTEGRAL
DAMAGE = abaqusConstants.DAMAGE
DAMAGE_CRITERION = abaqusConstants.DAMAGE_CRITERION
DAMPING_COEFFICIENT = abaqusConstants.DAMPING_COEFFICIENT
DAMPING_FACTOR = abaqusConstants.DAMPING_FACTOR
DASHED = abaqusConstants.DASHED
DASHPOT1 = abaqusConstants.DASHPOT1
DASHPOT2 = abaqusConstants.DASHPOT2
DASHPOTA = abaqusConstants.DASHPOTA
DATACHECK = abaqusConstants.DATACHECK
DATUM = abaqusConstants.DATUM
DB = abaqusConstants.DB
DB2 = abaqusConstants.DB2
DC1D2 = abaqusConstants.DC1D2
DC1D2E = abaqusConstants.DC1D2E
DC1D3 = abaqusConstants.DC1D3
DC1D3E = abaqusConstants.DC1D3E
DC2D3 = abaqusConstants.DC2D3
DC2D3E = abaqusConstants.DC2D3E
DC2D4 = abaqusConstants.DC2D4
DC2D4E = abaqusConstants.DC2D4E
DC2D6 = abaqusConstants.DC2D6
DC2D6E = abaqusConstants.DC2D6E
DC2D8 = abaqusConstants.DC2D8
DC2D8E = abaqusConstants.DC2D8E
DC3D10 = abaqusConstants.DC3D10
DC3D10E = abaqusConstants.DC3D10E
DC3D15 = abaqusConstants.DC3D15
DC3D15E = abaqusConstants.DC3D15E
DC3D20 = abaqusConstants.DC3D20
DC3D20E = abaqusConstants.DC3D20E
DC3D4 = abaqusConstants.DC3D4
DC3D4E = abaqusConstants.DC3D4E
DC3D6 = abaqusConstants.DC3D6
DC3D6E = abaqusConstants.DC3D6E
DC3D8 = abaqusConstants.DC3D8
DC3D8E = abaqusConstants.DC3D8E
DCAX3 = abaqusConstants.DCAX3
DCAX3E = abaqusConstants.DCAX3E
DCAX4 = abaqusConstants.DCAX4
DCAX4E = abaqusConstants.DCAX4E
DCAX6 = abaqusConstants.DCAX6
DCAX6E = abaqusConstants.DCAX6E
DCAX8 = abaqusConstants.DCAX8
DCAX8E = abaqusConstants.DCAX8E
DCC1D2 = abaqusConstants.DCC1D2
DCC1D2D = abaqusConstants.DCC1D2D
DCC2D4 = abaqusConstants.DCC2D4
DCC2D4D = abaqusConstants.DCC2D4D
DCC3D8 = abaqusConstants.DCC3D8
DCC3D8D = abaqusConstants.DCC3D8D
DCCAX2 = abaqusConstants.DCCAX2
DCCAX2D = abaqusConstants.DCCAX2D
DCCAX4 = abaqusConstants.DCCAX4
DCCAX4D = abaqusConstants.DCCAX4D
DCOUP2D = abaqusConstants.DCOUP2D
DCOUP3D = abaqusConstants.DCOUP3D
DDM_ITERATIVE = abaqusConstants.DDM_ITERATIVE
DEACTIVATED = abaqusConstants.DEACTIVATED
DEACTIVATED_FROM_BASE_STATE = abaqusConstants.DEACTIVATED_FROM_BASE_STATE
DEBONDING = abaqusConstants.DEBONDING
DECIMAL = abaqusConstants.DECIMAL
DEFAULT = abaqusConstants.DEFAULT
DEFAULTFORMAT = abaqusConstants.DEFAULTFORMAT
DEFAULT_COLORS = abaqusConstants.DEFAULT_COLORS
DEFAULT_LIMIT = abaqusConstants.DEFAULT_LIMIT
DEFAULT_MODEL = abaqusConstants.DEFAULT_MODEL
DEFAULT_SIZE = abaqusConstants.DEFAULT_SIZE
DEFINE = abaqusConstants.DEFINE
DEFORMABLE_BODY = abaqusConstants.DEFORMABLE_BODY
DEFORMED = abaqusConstants.DEFORMED
DELAYED = abaqusConstants.DELAYED
DELETE = abaqusConstants.DELETE
DELTA_OVER_1_ITERATION = abaqusConstants.DELTA_OVER_1_ITERATION
DELTA_OVER_2_ITERATIONS = abaqusConstants.DELTA_OVER_2_ITERATIONS
DELTA_OVER_3_ITERATIONS = abaqusConstants.DELTA_OVER_3_ITERATIONS
DELTA_OVER_4_ITERATIONS = abaqusConstants.DELTA_OVER_4_ITERATIONS
DELTA_OVER_5_ITERATIONS = abaqusConstants.DELTA_OVER_5_ITERATIONS
DELTA_OVER_6_ITERATIONS = abaqusConstants.DELTA_OVER_6_ITERATIONS
DEMOLD_REGION = abaqusConstants.DEMOLD_REGION
DENSITY = abaqusConstants.DENSITY
DENSITY_ROTATIONAL_ACCELERATION = abaqusConstants.DENSITY_ROTATIONAL_ACCELERATION
DERIVED_COMPONENT = abaqusConstants.DERIVED_COMPONENT
DESCENDING = abaqusConstants.DESCENDING
DESIGN_SENSITIVITY = abaqusConstants.DESIGN_SENSITIVITY
DEVIATION_FACTOR = abaqusConstants.DEVIATION_FACTOR
DGAP = abaqusConstants.DGAP
DIFFERENCE = abaqusConstants.DIFFERENCE
DIFFUSE = abaqusConstants.DIFFUSE
DIRECT = abaqusConstants.DIRECT
DIRECTION = abaqusConstants.DIRECTION
DIRECTIONAL = abaqusConstants.DIRECTIONAL
DIRECTION_COSINE = abaqusConstants.DIRECTION_COSINE
DIRECT_COMPONENT = abaqusConstants.DIRECT_COMPONENT
DIRECT_CYCLIC = abaqusConstants.DIRECT_CYCLIC
DIRECT_INCREMENTATION = abaqusConstants.DIRECT_INCREMENTATION
DIRECT_NO_STOP_INCREMENTATION = abaqusConstants.DIRECT_NO_STOP_INCREMENTATION
DIRECT_SOLVER = abaqusConstants.DIRECT_SOLVER
DIRECT_STEADY_STATE_DYNAMIC = abaqusConstants.DIRECT_STEADY_STATE_DYNAMIC
DIRECT_SYMMETRIC = abaqusConstants.DIRECT_SYMMETRIC
DIRECT_UNSYMMETRIC = abaqusConstants.DIRECT_UNSYMMETRIC
DISABLED_BY_SYSTEM = abaqusConstants.DISABLED_BY_SYSTEM
DISABLED_BY_USER = abaqusConstants.DISABLED_BY_USER
DISABLE_THROUGHOUT_STEP = abaqusConstants.DISABLE_THROUGHOUT_STEP
DISCONTINUITIES = abaqusConstants.DISCONTINUITIES
DISCRETE = abaqusConstants.DISCRETE
DISCRETE_FIELD = abaqusConstants.DISCRETE_FIELD
DISCRETE_RIGID_SURFACE = abaqusConstants.DISCRETE_RIGID_SURFACE
DISK = abaqusConstants.DISK
DISPLACEMENT = abaqusConstants.DISPLACEMENT
DISPLACEMENT_FIELD = abaqusConstants.DISPLACEMENT_FIELD
DISPLAY_GROUPS = abaqusConstants.DISPLAY_GROUPS
DISPLAY_GRP_MAP = abaqusConstants.DISPLAY_GRP_MAP
DISPLAY_GRP_MAP_COLORS = abaqusConstants.DISPLAY_GRP_MAP_COLORS
DISSIPATED_ENERGY_FRACTION = abaqusConstants.DISSIPATED_ENERGY_FRACTION
DISTRIBUTING = abaqusConstants.DISTRIBUTING
DISTRIBUTING_COUPLING = abaqusConstants.DISTRIBUTING_COUPLING
DIVIDE = abaqusConstants.DIVIDE
DMASS_XPL = abaqusConstants.DMASS_XPL
DOF_MODE = abaqusConstants.DOF_MODE
DOF_MODE_MPC = abaqusConstants.DOF_MODE_MPC
DOMAIN = abaqusConstants.DOMAIN
DOTTED = abaqusConstants.DOTTED
DOT_DASH = abaqusConstants.DOT_DASH
DOUBLE = abaqusConstants.DOUBLE
DOUBLE_CONSTRAINT_ONLY = abaqusConstants.DOUBLE_CONSTRAINT_ONLY
DOUBLE_PLUS_PACK = abaqusConstants.DOUBLE_PLUS_PACK
DOUBLE_PRECISION = abaqusConstants.DOUBLE_PRECISION
DOUBLE_SIDED = abaqusConstants.DOUBLE_SIDED
DPI_1200 = abaqusConstants.DPI_1200
DPI_150 = abaqusConstants.DPI_150
DPI_300 = abaqusConstants.DPI_300
DPI_450 = abaqusConstants.DPI_450
DPI_600 = abaqusConstants.DPI_600
DPI_75 = abaqusConstants.DPI_75
DRAG2D = abaqusConstants.DRAG2D
DRAG3D = abaqusConstants.DRAG3D
DS3 = abaqusConstants.DS3
DS4 = abaqusConstants.DS4
DS6 = abaqusConstants.DS6
DS8 = abaqusConstants.DS8
DSAX1 = abaqusConstants.DSAX1
DSAX2 = abaqusConstants.DSAX2
DSC = abaqusConstants.DSC
DUPLICATE_NODES = abaqusConstants.DUPLICATE_NODES
DURING_ANALYSIS = abaqusConstants.DURING_ANALYSIS
DYNAMIC = abaqusConstants.DYNAMIC
DYNAMIC_EXPLICIT = abaqusConstants.DYNAMIC_EXPLICIT
DYNAMIC_IMPLICIT = abaqusConstants.DYNAMIC_IMPLICIT
DYNAMIC_SUBSPACE = abaqusConstants.DYNAMIC_SUBSPACE
DYNAMIC_TEMP_DISPLACEMENT = abaqusConstants.DYNAMIC_TEMP_DISPLACEMENT
EC3D8R = abaqusConstants.EC3D8R
EC3D8RT = abaqusConstants.EC3D8RT
ECURRENT_AREA_TIME = abaqusConstants.ECURRENT_AREA_TIME
EDGE = abaqusConstants.EDGE
EDGE1 = abaqusConstants.EDGE1
EDGE2 = abaqusConstants.EDGE2
EDGE3 = abaqusConstants.EDGE3
EDGE4 = abaqusConstants.EDGE4
EDGES = abaqusConstants.EDGES
EDGETOEDGE = abaqusConstants.EDGETOEDGE
EDGETOFACE = abaqusConstants.EDGETOFACE
EDGE_LIST = abaqusConstants.EDGE_LIST
EDGE_SEEDING_METHOD = abaqusConstants.EDGE_SEEDING_METHOD
EIGENFREQUENCY = abaqusConstants.EIGENFREQUENCY
EIGENVALUE_BUCKLING = abaqusConstants.EIGENVALUE_BUCKLING
EITHER = abaqusConstants.EITHER
ELASTIC = abaqusConstants.ELASTIC
ELASTIC_PLASTIC = abaqusConstants.ELASTIC_PLASTIC
ELBOW31 = abaqusConstants.ELBOW31
ELBOW31B = abaqusConstants.ELBOW31B
ELBOW31C = abaqusConstants.ELBOW31C
ELBOW32 = abaqusConstants.ELBOW32
ELBOW_MPC = abaqusConstants.ELBOW_MPC
ELECTRICAL = abaqusConstants.ELECTRICAL
ELECTRICAL_CONTACT = abaqusConstants.ELECTRICAL_CONTACT
ELECTRICAL_POTENTIAL_FIELD = abaqusConstants.ELECTRICAL_POTENTIAL_FIELD
ELECTRIC_CHARGE = abaqusConstants.ELECTRIC_CHARGE
ELECTRIC_CURRENT = abaqusConstants.ELECTRIC_CURRENT
ELECTRIC_CURRENT_AREA = abaqusConstants.ELECTRIC_CURRENT_AREA
ELECTRIC_POTENTIAL = abaqusConstants.ELECTRIC_POTENTIAL
ELECTROMAGNETIC_TIME_HARMONIC = abaqusConstants.ELECTROMAGNETIC_TIME_HARMONIC
ELEMENT = abaqusConstants.ELEMENT
ELEMENTS = abaqusConstants.ELEMENTS
ELEMENT_ALL = abaqusConstants.ELEMENT_ALL
ELEMENT_BY_ELEMENT_INCREMENTATION = abaqusConstants.ELEMENT_BY_ELEMENT_INCREMENTATION
ELEMENT_CENTER_PROJECTION = abaqusConstants.ELEMENT_CENTER_PROJECTION
ELEMENT_CENTROID = abaqusConstants.ELEMENT_CENTROID
ELEMENT_FACE = abaqusConstants.ELEMENT_FACE
ELEMENT_FACE_INTEGRATION_POINT = abaqusConstants.ELEMENT_FACE_INTEGRATION_POINT
ELEMENT_NODAL = abaqusConstants.ELEMENT_NODAL
ELEMENT_NODES = abaqusConstants.ELEMENT_NODES
ELEMENT_PRESELECT = abaqusConstants.ELEMENT_PRESELECT
ELEMENT_SET = abaqusConstants.ELEMENT_SET
ELEM_SHAPE = abaqusConstants.ELEM_SHAPE
ELLIPSE = abaqusConstants.ELLIPSE
ELLIPTICAL = abaqusConstants.ELLIPTICAL
ELSET_MAP = abaqusConstants.ELSET_MAP
ELSET_MAP_COLORS = abaqusConstants.ELSET_MAP_COLORS
ELTYPE_MAP = abaqusConstants.ELTYPE_MAP
ELTYPE_MAP_COLORS = abaqusConstants.ELTYPE_MAP_COLORS
EMAG = abaqusConstants.EMAG
EMBEDDED_COEFF = abaqusConstants.EMBEDDED_COEFF
EMBEDDED_ELEMENT = abaqusConstants.EMBEDDED_ELEMENT
EMC2D3 = abaqusConstants.EMC2D3
EMC2D4 = abaqusConstants.EMC2D4
EMC3D4 = abaqusConstants.EMC3D4
EMC3D6 = abaqusConstants.EMC3D6
EMC3D8 = abaqusConstants.EMC3D8
EMF = abaqusConstants.EMF
EMPTY_FIELD = abaqusConstants.EMPTY_FIELD
EMPTY_LEAF = abaqusConstants.EMPTY_LEAF
ENABLED = abaqusConstants.ENABLED
ENCASTRE = abaqusConstants.ENCASTRE
END = abaqusConstants.END
END1 = abaqusConstants.END1
END2 = abaqusConstants.END2
END3 = abaqusConstants.END3
END_FRAME_TIME = abaqusConstants.END_FRAME_TIME
END_RELEASE = abaqusConstants.END_RELEASE
END_STEP = abaqusConstants.END_STEP
ENERGY = abaqusConstants.ENERGY
ENERGY_ALL = abaqusConstants.ENERGY_ALL
ENERGY_DENSITY = abaqusConstants.ENERGY_DENSITY
ENERGY_NONE = abaqusConstants.ENERGY_NONE
ENERGY_PRESELECT = abaqusConstants.ENERGY_PRESELECT
ENERGY_RELEASE_RATE = abaqusConstants.ENERGY_RELEASE_RATE
ENERGY_TYPE = abaqusConstants.ENERGY_TYPE
ENFORCEMENT_OFF = abaqusConstants.ENFORCEMENT_OFF
ENFORCEMENT_ON = abaqusConstants.ENFORCEMENT_ON
ENGINEERING = abaqusConstants.ENGINEERING
ENGINEERING_CONSTANTS = abaqusConstants.ENGINEERING_CONSTANTS
ENHANCED = abaqusConstants.ENHANCED
ENHANCED_VCCT = abaqusConstants.ENHANCED_VCCT
ENTEREDCOORD = abaqusConstants.ENTEREDCOORD
ENUMERATION = abaqusConstants.ENUMERATION
ENVELOPE = abaqusConstants.ENVELOPE
EPOTENTIAL_GRADIENT = abaqusConstants.EPOTENTIAL_GRADIENT
EPS = abaqusConstants.EPS
EQUAL = abaqusConstants.EQUAL
EQUALRADIUS = abaqusConstants.EQUALRADIUS
EQUATION = abaqusConstants.EQUATION
EQUILIBRIUM = abaqusConstants.EQUILIBRIUM
EQUIV_STRESS = abaqusConstants.EQUIV_STRESS
ERROR = abaqusConstants.ERROR
ETOTAL_XPL = abaqusConstants.ETOTAL_XPL
EULER = abaqusConstants.EULER
EULERIAN = abaqusConstants.EULERIAN
EVENT_ACCELERATION = abaqusConstants.EVENT_ACCELERATION
EVENT_DISPLACEMENT = abaqusConstants.EVENT_DISPLACEMENT
EVENT_GRAVITY = abaqusConstants.EVENT_GRAVITY
EVENT_VELOCITY = abaqusConstants.EVENT_VELOCITY
EVERY_CYCLE = abaqusConstants.EVERY_CYCLE
EVERY_NCYCLES = abaqusConstants.EVERY_NCYCLES
EVERY_TIME_INCREMENT = abaqusConstants.EVERY_TIME_INCREMENT
EXACT = abaqusConstants.EXACT
EXACT_TARGETS = abaqusConstants.EXACT_TARGETS
EXCESSIVE_DISTORTION = abaqusConstants.EXCESSIVE_DISTORTION
EXCESSIVE_ELEMENT_DISTORTION = abaqusConstants.EXCESSIVE_ELEMENT_DISTORTION
EXCESSIVE_STRAIN_INCREMENT = abaqusConstants.EXCESSIVE_STRAIN_INCREMENT
EXCLUDE = abaqusConstants.EXCLUDE
EXPLICIT = abaqusConstants.EXPLICIT
EXPLICIT_ANALYSIS = abaqusConstants.EXPLICIT_ANALYSIS
EXPLICIT_DYNAMIC = abaqusConstants.EXPLICIT_DYNAMIC
EXPLICIT_ONLY = abaqusConstants.EXPLICIT_ONLY
EXPLICIT_PHASE = abaqusConstants.EXPLICIT_PHASE
EXPONENTIAL = abaqusConstants.EXPONENTIAL
EXPONENTIAL_DECAY = abaqusConstants.EXPONENTIAL_DECAY
EXPONENTIAL_LAW = abaqusConstants.EXPONENTIAL_LAW
EXPORT_STEP_SIZE = abaqusConstants.EXPORT_STEP_SIZE
EXTERIOR = abaqusConstants.EXTERIOR
EXTERNAL = abaqusConstants.EXTERNAL
EXTRAPOLATE_AVERAGE_COMPUTE = abaqusConstants.EXTRAPOLATE_AVERAGE_COMPUTE
EXTRAPOLATE_COMPUTE = abaqusConstants.EXTRAPOLATE_COMPUTE
EXTRAPOLATE_COMPUTE_AVERAGE = abaqusConstants.EXTRAPOLATE_COMPUTE_AVERAGE
EXTRAPOLATE_COMPUTE_DISCONTINUITIES = abaqusConstants.EXTRAPOLATE_COMPUTE_DISCONTINUITIES
EXTRA_COARSE = abaqusConstants.EXTRA_COARSE
EXTRA_FINE = abaqusConstants.EXTRA_FINE
F2D2 = abaqusConstants.F2D2
F3D3 = abaqusConstants.F3D3
F3D4 = abaqusConstants.F3D4
FACE1 = abaqusConstants.FACE1
FACE2 = abaqusConstants.FACE2
FACE3 = abaqusConstants.FACE3
FACE4 = abaqusConstants.FACE4
FACE5 = abaqusConstants.FACE5
FACE6 = abaqusConstants.FACE6
FACETOEDGE = abaqusConstants.FACETOEDGE
FACETOFACE = abaqusConstants.FACETOFACE
FACETS = abaqusConstants.FACETS
FACE_CENTERED = abaqusConstants.FACE_CENTERED
FACE_UNKNOWN = abaqusConstants.FACE_UNKNOWN
FACTOR = abaqusConstants.FACTOR
FARTHEST_POINT_FRACTION = abaqusConstants.FARTHEST_POINT_FRACTION
FAST = abaqusConstants.FAST
FASTENER = abaqusConstants.FASTENER
FATIGUE = abaqusConstants.FATIGUE
FAX2 = abaqusConstants.FAX2
FC3D4 = abaqusConstants.FC3D4
FC3D5 = abaqusConstants.FC3D5
FC3D6 = abaqusConstants.FC3D6
FC3D8 = abaqusConstants.FC3D8
FEATURE = abaqusConstants.FEATURE
FE_SAFE = abaqusConstants.FE_SAFE
FGMRES = abaqusConstants.FGMRES
FICK = abaqusConstants.FICK
FIELD = abaqusConstants.FIELD
FIELDREPORTFORMAT = abaqusConstants.FIELDREPORTFORMAT
FIELD_OUTPUT = abaqusConstants.FIELD_OUTPUT
FIELD_THICKNESS = abaqusConstants.FIELD_THICKNESS
FILE = abaqusConstants.FILE
FILL = abaqusConstants.FILL
FILLED = abaqusConstants.FILLED
FILLED_ARROW = abaqusConstants.FILLED_ARROW
FILLED_CIRCLE = abaqusConstants.FILLED_CIRCLE
FILLED_DIAMOND = abaqusConstants.FILLED_DIAMOND
FILLED_SQUARE = abaqusConstants.FILLED_SQUARE
FILLED_TRI = abaqusConstants.FILLED_TRI
FILTER = abaqusConstants.FILTER
FINE = abaqusConstants.FINE
FINER = abaqusConstants.FINER
FINITE = abaqusConstants.FINITE
FIRST = abaqusConstants.FIRST
FIRST_AND_LAST = abaqusConstants.FIRST_AND_LAST
FIRST_CYCLE = abaqusConstants.FIRST_CYCLE
FIRST_FRAME = abaqusConstants.FIRST_FRAME
FIRST_ORDER_ADVECTION = abaqusConstants.FIRST_ORDER_ADVECTION
FIRST_STEP = abaqusConstants.FIRST_STEP
FITTED_VALUE = abaqusConstants.FITTED_VALUE
FIT_HEIGHT = abaqusConstants.FIT_HEIGHT
FIT_TO_PAGE = abaqusConstants.FIT_TO_PAGE
FIT_TO_VIEWPORT = abaqusConstants.FIT_TO_VIEWPORT
FIT_WIDTH = abaqusConstants.FIT_WIDTH
FIXED = abaqusConstants.FIXED
FIXED_CFL = abaqusConstants.FIXED_CFL
FIXED_DOF = abaqusConstants.FIXED_DOF
FIXED_EBE = abaqusConstants.FIXED_EBE
FIXED_INCREMENTATION = abaqusConstants.FIXED_INCREMENTATION
FIXED_TIME = abaqusConstants.FIXED_TIME
FIXED_USER_DEFINED_INC = abaqusConstants.FIXED_USER_DEFINED_INC
FIX_LENGTH = abaqusConstants.FIX_LENGTH
FIX_NONE = abaqusConstants.FIX_NONE
FLD = abaqusConstants.FLD
FLEXIBLE = abaqusConstants.FLEXIBLE
FLEXION_TORSION = abaqusConstants.FLEXION_TORSION
FLINK = abaqusConstants.FLINK
FLOAT = abaqusConstants.FLOAT
FLOW = abaqusConstants.FLOW
FLOW_CONVERTER = abaqusConstants.FLOW_CONVERTER
FLUID = abaqusConstants.FLUID
FLUID_PRESSURE_FIELD = abaqusConstants.FLUID_PRESSURE_FIELD
FOLLOW = abaqusConstants.FOLLOW
FONT = abaqusConstants.FONT
FORCE = abaqusConstants.FORCE
FORCE_SINGLE = abaqusConstants.FORCE_SINGLE
FORCE_VOLUME = abaqusConstants.FORCE_VOLUME
FORMULA = abaqusConstants.FORMULA
FORWARD = abaqusConstants.FORWARD
FRACTION = abaqusConstants.FRACTION
FRACTIONAL = abaqusConstants.FRACTIONAL
FRACTURE_MECHANICS = abaqusConstants.FRACTURE_MECHANICS
FRAME2D = abaqusConstants.FRAME2D
FRAME3D = abaqusConstants.FRAME3D
FRAME_BASED = abaqusConstants.FRAME_BASED
FRAME_VALUE = abaqusConstants.FRAME_VALUE
FREE = abaqusConstants.FREE
FREED = abaqusConstants.FREED
FREE_FORM = abaqusConstants.FREE_FORM
FREE_TASK_REGION_EQUIV_STRESS = abaqusConstants.FREE_TASK_REGION_EQUIV_STRESS
FREQUENCY = abaqusConstants.FREQUENCY
FREQUENCY_DATA = abaqusConstants.FREQUENCY_DATA
FREQUENCY_RANGE = abaqusConstants.FREQUENCY_RANGE
FRICTIONLESS = abaqusConstants.FRICTIONLESS
FROM_ASCII_FILE = abaqusConstants.FROM_ASCII_FILE
FROM_FILE = abaqusConstants.FROM_FILE
FROM_FILE_AND_USER_DEFINED = abaqusConstants.FROM_FILE_AND_USER_DEFINED
FROM_GEOMETRY = abaqusConstants.FROM_GEOMETRY
FROM_KEYBOARD = abaqusConstants.FROM_KEYBOARD
FROM_ODB = abaqusConstants.FROM_ODB
FROM_OPERATION = abaqusConstants.FROM_OPERATION
FROM_SECTION = abaqusConstants.FROM_SECTION
FROM_USER_DEFINED = abaqusConstants.FROM_USER_DEFINED
FULL = abaqusConstants.FULL
FULLY = abaqusConstants.FULLY
FULL_CYCLE = abaqusConstants.FULL_CYCLE
FULL_FIELD = abaqusConstants.FULL_FIELD
FULL_NEWTON = abaqusConstants.FULL_NEWTON
FUNG_ANISOTROPIC = abaqusConstants.FUNG_ANISOTROPIC
FUNG_ORTHOTROPIC = abaqusConstants.FUNG_ORTHOTROPIC
G = abaqusConstants.G
GALERKIN = abaqusConstants.GALERKIN
GAPCYL = abaqusConstants.GAPCYL
GAPSPHER = abaqusConstants.GAPSPHER
GAPUNI = abaqusConstants.GAPUNI
GAPUNIT = abaqusConstants.GAPUNIT
GASKET = abaqusConstants.GASKET
GAUSS = abaqusConstants.GAUSS
GAUSS_COUPLING = abaqusConstants.GAUSS_COUPLING
GENERAL = abaqusConstants.GENERAL
GENERALIZED = abaqusConstants.GENERALIZED
GENERALIZED_BEAM = abaqusConstants.GENERALIZED_BEAM
GENERALIZED_DECAY = abaqusConstants.GENERALIZED_DECAY
GENERALIZED_SHELL = abaqusConstants.GENERALIZED_SHELL
GENERAL_OPTIMIZATION = abaqusConstants.GENERAL_OPTIMIZATION
GENERAL_PARTICLE = abaqusConstants.GENERAL_PARTICLE
GEOMETRY = abaqusConstants.GEOMETRY
GEOMETRYFORMAT = abaqusConstants.GEOMETRYFORMAT
GEOMETRY_ENHANCED = abaqusConstants.GEOMETRY_ENHANCED
GEOM_DEVIATION_FACTOR = abaqusConstants.GEOM_DEVIATION_FACTOR
GEOSTATIC = abaqusConstants.GEOSTATIC
GFI = abaqusConstants.GFI
GIGA_BYTES = abaqusConstants.GIGA_BYTES
GK2D2 = abaqusConstants.GK2D2
GK2D2N = abaqusConstants.GK2D2N
GK3D12M = abaqusConstants.GK3D12M
GK3D12MN = abaqusConstants.GK3D12MN
GK3D18 = abaqusConstants.GK3D18
GK3D18N = abaqusConstants.GK3D18N
GK3D2 = abaqusConstants.GK3D2
GK3D2N = abaqusConstants.GK3D2N
GK3D4L = abaqusConstants.GK3D4L
GK3D4LN = abaqusConstants.GK3D4LN
GK3D6 = abaqusConstants.GK3D6
GK3D6L = abaqusConstants.GK3D6L
GK3D6LN = abaqusConstants.GK3D6LN
GK3D6N = abaqusConstants.GK3D6N
GK3D8 = abaqusConstants.GK3D8
GK3D8N = abaqusConstants.GK3D8N
GKAX2 = abaqusConstants.GKAX2
GKAX2N = abaqusConstants.GKAX2N
GKAX4 = abaqusConstants.GKAX4
GKAX4N = abaqusConstants.GKAX4N
GKAX6 = abaqusConstants.GKAX6
GKAX6N = abaqusConstants.GKAX6N
GKPE4 = abaqusConstants.GKPE4
GKPE6 = abaqusConstants.GKPE6
GKPS4 = abaqusConstants.GKPS4
GKPS4N = abaqusConstants.GKPS4N
GKPS6 = abaqusConstants.GKPS6
GKPS6N = abaqusConstants.GKPS6N
GLOBAL = abaqusConstants.GLOBAL
GLOBAL_NONE = abaqusConstants.GLOBAL_NONE
GLOBAL_X = abaqusConstants.GLOBAL_X
GLOBAL_Y = abaqusConstants.GLOBAL_Y
GLOBAL_Z = abaqusConstants.GLOBAL_Z
GOURAUD = abaqusConstants.GOURAUD
GRADED = abaqusConstants.GRADED
GRADIENT = abaqusConstants.GRADIENT
GRADIENTS = abaqusConstants.GRADIENTS
GRADIENTS_THROUGH_BEAM_CS = abaqusConstants.GRADIENTS_THROUGH_BEAM_CS
GRADIENTS_THROUGH_SHELL_CS = abaqusConstants.GRADIENTS_THROUGH_SHELL_CS
GRAVITY = abaqusConstants.GRAVITY
GREATER_THAN = abaqusConstants.GREATER_THAN
GREATER_THAN_EQUAL = abaqusConstants.GREATER_THAN_EQUAL
GREYSCALE = abaqusConstants.GREYSCALE
GRID = abaqusConstants.GRID
GROUND = abaqusConstants.GROUND
GROUP_BY_MATERIAL = abaqusConstants.GROUP_BY_MATERIAL
GROWTH_MOVEMENT = abaqusConstants.GROWTH_MOVEMENT
GRP = abaqusConstants.GRP
HALF = abaqusConstants.HALF
HALF_CYCLE = abaqusConstants.HALF_CYCLE
HALF_INDEX_SHIFT = abaqusConstants.HALF_INDEX_SHIFT
HALF_OF_AVERAGE = abaqusConstants.HALF_OF_AVERAGE
HARD = abaqusConstants.HARD
HARDWARE_OVERLAY = abaqusConstants.HARDWARE_OVERLAY
HARMONIC = abaqusConstants.HARMONIC
HEADING = abaqusConstants.HEADING
HEALER_TYPE = abaqusConstants.HEALER_TYPE
HEATCAP = abaqusConstants.HEATCAP
HEAT_FLUX = abaqusConstants.HEAT_FLUX
HEAT_FLUX_AREA = abaqusConstants.HEAT_FLUX_AREA
HEAT_FLUX_RATE = abaqusConstants.HEAT_FLUX_RATE
HEAT_FLUX_VOLUME = abaqusConstants.HEAT_FLUX_VOLUME
HEAT_TRANSFER = abaqusConstants.HEAT_TRANSFER
HEIGHT = abaqusConstants.HEIGHT
HEX = abaqusConstants.HEX
HEX20 = abaqusConstants.HEX20
HEX8 = abaqusConstants.HEX8
HEX_DOMINATED = abaqusConstants.HEX_DOMINATED
HIDDEN = abaqusConstants.HIDDEN
HIGH = abaqusConstants.HIGH
HINGE = abaqusConstants.HINGE
HISTORY = abaqusConstants.HISTORY
HOLLOW_CIRCLE = abaqusConstants.HOLLOW_CIRCLE
HOLLOW_DIAMOND = abaqusConstants.HOLLOW_DIAMOND
HOLLOW_SQUARE = abaqusConstants.HOLLOW_SQUARE
HOLLOW_TRI = abaqusConstants.HOLLOW_TRI
HOLZAPFEL = abaqusConstants.HOLZAPFEL
HOME = abaqusConstants.HOME
HORIZONTAL = abaqusConstants.HORIZONTAL
HYBRID = abaqusConstants.HYBRID
HYDRAULIC = abaqusConstants.HYDRAULIC
HYDROSTATIC = abaqusConstants.HYDROSTATIC
HYDROSTATIC_FLUID_MODELING = abaqusConstants.HYDROSTATIC_FLUID_MODELING
HYPERBOLIC = abaqusConstants.HYPERBOLIC
HYPERBOLIC_SINE = abaqusConstants.HYPERBOLIC_SINE
HYSTERESIS_INITIAL_GUESSES_EXHAUSTED = abaqusConstants.HYSTERESIS_INITIAL_GUESSES_EXHAUSTED
HYSTERESIS_JACOBIAN_CANNOT_BE_INVERTED = abaqusConstants.HYSTERESIS_JACOBIAN_CANNOT_BE_INVERTED
ICC = abaqusConstants.ICC
IDEALGAS = abaqusConstants.IDEALGAS
IDENTICAL = abaqusConstants.IDENTICAL
IDENTITY = abaqusConstants.IDENTITY
IGNITIONANDGROWTH = abaqusConstants.IGNITIONANDGROWTH
IMAGINARY = abaqusConstants.IMAGINARY
IMMEDIATE = abaqusConstants.IMMEDIATE
IMPEDANCE = abaqusConstants.IMPEDANCE
IMPERFECTION = abaqusConstants.IMPERFECTION
IMPLICIT = abaqusConstants.IMPLICIT
IMPLICIT_DYNAMIC = abaqusConstants.IMPLICIT_DYNAMIC
IMPLICIT_EXPLICIT = abaqusConstants.IMPLICIT_EXPLICIT
IMPORT = abaqusConstants.IMPORT
IMPORT_STEP_SIZE = abaqusConstants.IMPORT_STEP_SIZE
IMPRINT = abaqusConstants.IMPRINT
IMPROVED = abaqusConstants.IMPROVED
INCHES = abaqusConstants.INCHES
INCLUDE = abaqusConstants.INCLUDE
INCOMPRESSIBLE = abaqusConstants.INCOMPRESSIBLE
INCREMENT = abaqusConstants.INCREMENT
INCREMENTAL = abaqusConstants.INCREMENTAL
INCREMENTATION = abaqusConstants.INCREMENTATION
INCREMENTATION_ALL = abaqusConstants.INCREMENTATION_ALL
INCREMENTATION_PRESELECT = abaqusConstants.INCREMENTATION_PRESELECT
INC_SIZE = abaqusConstants.INC_SIZE
INDEPENDENT = abaqusConstants.INDEPENDENT
INDEX = abaqusConstants.INDEX
INERTIA_RELIEF = abaqusConstants.INERTIA_RELIEF
INFILTRATION = abaqusConstants.INFILTRATION
INFINITE = abaqusConstants.INFINITE
INFLOW = abaqusConstants.INFLOW
INITIAL = abaqusConstants.INITIAL
INITIAL_AND_LAST = abaqusConstants.INITIAL_AND_LAST
INITIAL_CONDITION = abaqusConstants.INITIAL_CONDITION
INITIAL_NODES = abaqusConstants.INITIAL_NODES
INITIAL_OPENINGS = abaqusConstants.INITIAL_OPENINGS
INITIAL_OVERCLOSURES = abaqusConstants.INITIAL_OVERCLOSURES
INITIAL_OVERCLOSURES_EXPLICIT = abaqusConstants.INITIAL_OVERCLOSURES_EXPLICIT
INPUT = abaqusConstants.INPUT
INPUT_FILE = abaqusConstants.INPUT_FILE
INSIDE = abaqusConstants.INSIDE
INSTANCE = abaqusConstants.INSTANCE
INSTANCE_FROM_INSTANCE = abaqusConstants.INSTANCE_FROM_INSTANCE
INSTANCE_FROM_PART = abaqusConstants.INSTANCE_FROM_PART
INSTANCE_MAP = abaqusConstants.INSTANCE_MAP
INSTANCE_MAP_COLORS = abaqusConstants.INSTANCE_MAP_COLORS
INSTANCE_NOT_APPLICABLE = abaqusConstants.INSTANCE_NOT_APPLICABLE
INSTANCE_TYPE_MAP = abaqusConstants.INSTANCE_TYPE_MAP
INSTANCE_TYPE_MAP_COLORS = abaqusConstants.INSTANCE_TYPE_MAP_COLORS
INSTANTANEOUS = abaqusConstants.INSTANTANEOUS
INTEGER = abaqusConstants.INTEGER
INTEGRATED_ALL = abaqusConstants.INTEGRATED_ALL
INTEGRATED_PRESELECT = abaqusConstants.INTEGRATED_PRESELECT
INTEGRATION_POINT = abaqusConstants.INTEGRATION_POINT
INTEGRATION_POINTS = abaqusConstants.INTEGRATION_POINTS
INTERACTION_MAP = abaqusConstants.INTERACTION_MAP
INTERACTION_MAP_COLORS = abaqusConstants.INTERACTION_MAP_COLORS
INTERACTION_PROP_MAP = abaqusConstants.INTERACTION_PROP_MAP
INTERACTION_PROP_MAP_COLORS = abaqusConstants.INTERACTION_PROP_MAP_COLORS
INTERACTION_TYPE_MAP = abaqusConstants.INTERACTION_TYPE_MAP
INTERACTION_TYPE_MAP_COLORS = abaqusConstants.INTERACTION_TYPE_MAP_COLORS
INTERFERENCE = abaqusConstants.INTERFERENCE
INTERNAL = abaqusConstants.INTERNAL
INTERNAL_SET_MAP = abaqusConstants.INTERNAL_SET_MAP
INTERNAL_SET_MAP_COLORS = abaqusConstants.INTERNAL_SET_MAP_COLORS
INTERNAL_SURFACE_MAP = abaqusConstants.INTERNAL_SURFACE_MAP
INTERNAL_SURFACE_MAP_COLORS = abaqusConstants.INTERNAL_SURFACE_MAP_COLORS
INTERPOLATED = abaqusConstants.INTERPOLATED
INTERPOLATE_OFF = abaqusConstants.INTERPOLATE_OFF
INTERPOLATE_ON = abaqusConstants.INTERPOLATE_ON
INTERRUPTED = abaqusConstants.INTERRUPTED
INTERSECTION = abaqusConstants.INTERSECTION
INTERSECTIONS = abaqusConstants.INTERSECTIONS
INV3 = abaqusConstants.INV3
INVALID = abaqusConstants.INVALID
INVALID_SURF = abaqusConstants.INVALID_SURF
INVARIANT = abaqusConstants.INVARIANT
INWARD = abaqusConstants.INWARD
ISL21A = abaqusConstants.ISL21A
ISL22A = abaqusConstants.ISL22A
ISOLINES = abaqusConstants.ISOLINES
ISOSURFACE = abaqusConstants.ISOSURFACE
ISOTROPIC = abaqusConstants.ISOTROPIC
ISOTROPIC_CFD = abaqusConstants.ISOTROPIC_CFD
ITERATION = abaqusConstants.ITERATION
ITERATIVE = abaqusConstants.ITERATIVE
ITERATIVE_SOLVER = abaqusConstants.ITERATIVE_SOLVER
ITSCYL = abaqusConstants.ITSCYL
ITSUNI = abaqusConstants.ITSUNI
ITT21 = abaqusConstants.ITT21
ITT31 = abaqusConstants.ITT31
JACOBI_COUPLING = abaqusConstants.JACOBI_COUPLING
JAMA = abaqusConstants.JAMA
JOB_ABORTED = abaqusConstants.JOB_ABORTED
JOB_COMPLETED = abaqusConstants.JOB_COMPLETED
JOB_INTERRUPTED = abaqusConstants.JOB_INTERRUPTED
JOB_STATUS_COMPLETED_SUCCESSFULLY = abaqusConstants.JOB_STATUS_COMPLETED_SUCCESSFULLY
JOB_STATUS_EXITED_WITH_ERROR = abaqusConstants.JOB_STATUS_EXITED_WITH_ERROR
JOB_STATUS_TERMINATED_BY_EXTERNAL_REQUEST = abaqusConstants.JOB_STATUS_TERMINATED_BY_EXTERNAL_REQUEST
JOB_STATUS_UNKNOWN = abaqusConstants.JOB_STATUS_UNKNOWN
JOB_SUBMITTED = abaqusConstants.JOB_SUBMITTED
JOHNSON_COOK = abaqusConstants.JOHNSON_COOK
JOIN = abaqusConstants.JOIN
JOINT2D = abaqusConstants.JOINT2D
JOINT3D = abaqusConstants.JOINT3D
JOINTC = abaqusConstants.JOINTC
JUSTIFY_LEFT = abaqusConstants.JUSTIFY_LEFT
JWL = abaqusConstants.JWL
J_INTEGRAL = abaqusConstants.J_INTEGRAL
KEPS_RNG = abaqusConstants.KEPS_RNG
KII0 = abaqusConstants.KII0
KINEMATIC = abaqusConstants.KINEMATIC
KINEMATIC_COUPLING = abaqusConstants.KINEMATIC_COUPLING
KINEMATIC_HARDENING = abaqusConstants.KINEMATIC_HARDENING
KINEMATIC_VIOLATIONS = abaqusConstants.KINEMATIC_VIOLATIONS
KINETIC_ENERGY_XPL = abaqusConstants.KINETIC_ENERGY_XPL
K_FACTORS = abaqusConstants.K_FACTORS
LAGRANGE = abaqusConstants.LAGRANGE
LAGRANGIAN = abaqusConstants.LAGRANGIAN
LAG_ANALYSIS = abaqusConstants.LAG_ANALYSIS
LAMINA = abaqusConstants.LAMINA
LANCZOS = abaqusConstants.LANCZOS
LANCZOS_EIGENSOLVER = abaqusConstants.LANCZOS_EIGENSOLVER
LANDSCAPE = abaqusConstants.LANDSCAPE
LARGE = abaqusConstants.LARGE
LARGE_ANGLE = abaqusConstants.LARGE_ANGLE
LARGE_ANGLE_QUAD_FACE = abaqusConstants.LARGE_ANGLE_QUAD_FACE
LARGE_ANGLE_TRI_FACE = abaqusConstants.LARGE_ANGLE_TRI_FACE
LARGE_STRAIN_INCREMENT = abaqusConstants.LARGE_STRAIN_INCREMENT
LAST = abaqusConstants.LAST
LAST_FRAME = abaqusConstants.LAST_FRAME
LAST_INCREMENT = abaqusConstants.LAST_INCREMENT
LAST_STEP = abaqusConstants.LAST_STEP
LATERAL_EXTENSION_RATIO_NOT_FOUND = abaqusConstants.LATERAL_EXTENSION_RATIO_NOT_FOUND
LATERAL_NOMINAL_STRAIN = abaqusConstants.LATERAL_NOMINAL_STRAIN
LAYUP = abaqusConstants.LAYUP
LAYUP_MAP = abaqusConstants.LAYUP_MAP
LAYUP_MAP_COLORS = abaqusConstants.LAYUP_MAP_COLORS
LAYUP_ORIENTATION = abaqusConstants.LAYUP_ORIENTATION
LEAD_ANALYSIS = abaqusConstants.LEAD_ANALYSIS
LEAF_COLORS = abaqusConstants.LEAF_COLORS
LEDGER = abaqusConstants.LEDGER
LEFT = abaqusConstants.LEFT
LEGAL = abaqusConstants.LEGAL
LENGTH = abaqusConstants.LENGTH
LESS_THAN = abaqusConstants.LESS_THAN
LESS_THAN_EQUAL = abaqusConstants.LESS_THAN_EQUAL
LETTER = abaqusConstants.LETTER
LETTERS = abaqusConstants.LETTERS
LICENSING = abaqusConstants.LICENSING
LIFT_EQUATION = abaqusConstants.LIFT_EQUATION
LINE = abaqusConstants.LINE
LINE2 = abaqusConstants.LINE2
LINE3 = abaqusConstants.LINE3
LINEAR = abaqusConstants.LINEAR
LINEAR_EXTRAPOLATION = abaqusConstants.LINEAR_EXTRAPOLATION
LINEAR_LEAST_SQUARES = abaqusConstants.LINEAR_LEAST_SQUARES
LINEAR_PRESSURE = abaqusConstants.LINEAR_PRESSURE
LINELINEDIST = abaqusConstants.LINELINEDIST
LINES = abaqusConstants.LINES
LINE_LOOP = abaqusConstants.LINE_LOOP
LINE_SEARCH = abaqusConstants.LINE_SEARCH
LINE_STRIP = abaqusConstants.LINE_STRIP
LINK = abaqusConstants.LINK
LINK_MPC = abaqusConstants.LINK_MPC
LINUX = abaqusConstants.LINUX
LIST_OF_MODES = abaqusConstants.LIST_OF_MODES
LOAD = abaqusConstants.LOAD
LOAD_CASE = abaqusConstants.LOAD_CASE
LOAD_MAP = abaqusConstants.LOAD_MAP
LOAD_MAP_COLORS = abaqusConstants.LOAD_MAP_COLORS
LOCAL = abaqusConstants.LOCAL
LOCAL_GRADIENT = abaqusConstants.LOCAL_GRADIENT
LOCKSTEP = abaqusConstants.LOCKSTEP
LOG = abaqusConstants.LOG
LOGARITHMIC = abaqusConstants.LOGARITHMIC
LONG = abaqusConstants.LONG
LONGEST_EDGE = abaqusConstants.LONGEST_EDGE
LONG_TERM = abaqusConstants.LONG_TERM
LOOP = abaqusConstants.LOOP
LOOP_BACKWARD = abaqusConstants.LOOP_BACKWARD
LOOSE_COUPLING = abaqusConstants.LOOSE_COUPLING
LOW = abaqusConstants.LOW
LS3S = abaqusConstants.LS3S
LS6 = abaqusConstants.LS6
LUMIN = abaqusConstants.LUMIN
M3D3 = abaqusConstants.M3D3
M3D4 = abaqusConstants.M3D4
M3D4R = abaqusConstants.M3D4R
M3D6 = abaqusConstants.M3D6
M3D8 = abaqusConstants.M3D8
M3D8R = abaqusConstants.M3D8R
MACAULEY = abaqusConstants.MACAULEY
MAGNITUDE = abaqusConstants.MAGNITUDE
MAGNITUDE_AND_PHASE = abaqusConstants.MAGNITUDE_AND_PHASE
MAINTAIN_CURRENT = abaqusConstants.MAINTAIN_CURRENT
MAIN_REGION = abaqusConstants.MAIN_REGION
MANUAL = abaqusConstants.MANUAL
MAP = abaqusConstants.MAP
MARLOW = abaqusConstants.MARLOW
MASS = abaqusConstants.MASS
MASS_DIFFUSION = abaqusConstants.MASS_DIFFUSION
MASS_FLOW_AREA = abaqusConstants.MASS_FLOW_AREA
MASS_FLOW_AREA_RATE = abaqusConstants.MASS_FLOW_AREA_RATE
MASS_FLOW_RATE = abaqusConstants.MASS_FLOW_RATE
MASS_FLUX = abaqusConstants.MASS_FLUX
MASS_PER_AREA = abaqusConstants.MASS_PER_AREA
MASS_PER_LENGTH = abaqusConstants.MASS_PER_LENGTH
MASS_PER_VOLUME = abaqusConstants.MASS_PER_VOLUME
MASS_PROPORTIONAL = abaqusConstants.MASS_PROPORTIONAL
MASS_RATE_LEAK = abaqusConstants.MASS_RATE_LEAK
MASS_SCALING = abaqusConstants.MASS_SCALING
MASTER = abaqusConstants.MASTER
MATCH = abaqusConstants.MATCH
MATERIAL = abaqusConstants.MATERIAL
MATERIAL_FLOW_FIELD = abaqusConstants.MATERIAL_FLOW_FIELD
MATERIAL_INSTABILITY = abaqusConstants.MATERIAL_INSTABILITY
MATERIAL_MAP = abaqusConstants.MATERIAL_MAP
MATERIAL_MAP_COLORS = abaqusConstants.MATERIAL_MAP_COLORS
MATERIAL_POINT_CALCULATIONS = abaqusConstants.MATERIAL_POINT_CALCULATIONS
MATRIX = abaqusConstants.MATRIX
MAX = abaqusConstants.MAX
MAX1 = abaqusConstants.MAX1
MAX2 = abaqusConstants.MAX2
MAXIMIZE = abaqusConstants.MAXIMIZE
MAXIMIZED = abaqusConstants.MAXIMIZED
MAXIMUM = abaqusConstants.MAXIMUM
MAXIMUM_NUMBER_OF_CONTACT_STRESS_AUGMENTATIONS = abaqusConstants.MAXIMUM_NUMBER_OF_CONTACT_STRESS_AUGMENTATIONS
MAXIMUM_NUMBER_OF_EQUILIBRIUM_ITERATIONS = abaqusConstants.MAXIMUM_NUMBER_OF_EQUILIBRIUM_ITERATIONS
MAXIMUM_NUMBER_OF_SEVERE_DISCONTINUITY_ITERATIONS = abaqusConstants.MAXIMUM_NUMBER_OF_SEVERE_DISCONTINUITY_ITERATIONS
MAXIMUM_SLIDE_DISTANCE_EXCEEDED = abaqusConstants.MAXIMUM_SLIDE_DISTANCE_EXCEEDED
MAX_ABS_VALUE = abaqusConstants.MAX_ABS_VALUE
MAX_CORRECTION = abaqusConstants.MAX_CORRECTION
MAX_EDGE = abaqusConstants.MAX_EDGE
MAX_ERROR = abaqusConstants.MAX_ERROR
MAX_ELASTOPLASTIC_STRAIN = abaqusConstants.MAX_ELASTOPLASTIC_STRAIN
MAX_FREQUENCY = abaqusConstants.MAX_FREQUENCY
MAX_INCREMENT = abaqusConstants.MAX_INCREMENT
MAX_INPLANE_PRINCIPAL = abaqusConstants.MAX_INPLANE_PRINCIPAL
MAX_PRINCIPAL = abaqusConstants.MAX_PRINCIPAL
MAX_RESIDUAL = abaqusConstants.MAX_RESIDUAL
MAX_SEPARATION = abaqusConstants.MAX_SEPARATION
MAX_SHEAR_STRAIN = abaqusConstants.MAX_SHEAR_STRAIN
MAX_STEP_SIZE = abaqusConstants.MAX_STEP_SIZE
MAX_STRESS = abaqusConstants.MAX_STRESS
MAX_VALUE = abaqusConstants.MAX_VALUE
MCL6 = abaqusConstants.MCL6
MCL9 = abaqusConstants.MCL9
MECHANICAL = abaqusConstants.MECHANICAL
MECHANICAL_CONTACT = abaqusConstants.MECHANICAL_CONTACT
MEDIAL_AXIS = abaqusConstants.MEDIAL_AXIS
MEDIUM = abaqusConstants.MEDIUM
MEGA_BYTES = abaqusConstants.MEGA_BYTES
MEMBRANE = abaqusConstants.MEMBRANE
MEMORY = abaqusConstants.MEMORY
MEMORY_ESTIMATE = abaqusConstants.MEMORY_ESTIMATE
MERGE = abaqusConstants.MERGE
MERR = abaqusConstants.MERR
MESH = abaqusConstants.MESH
MESHED_BEAM_SECTION = abaqusConstants.MESHED_BEAM_SECTION
MESH_MAP = abaqusConstants.MESH_MAP
MESH_MAP_COLORS = abaqusConstants.MESH_MAP_COLORS
MESH_TIE = abaqusConstants.MESH_TIE
MGAX1 = abaqusConstants.MGAX1
MGAX2 = abaqusConstants.MGAX2
MIDDLE = abaqusConstants.MIDDLE
MIDDLE_SURFACE = abaqusConstants.MIDDLE_SURFACE
MIDSIDE_ONLY = abaqusConstants.MIDSIDE_ONLY
MID_PRINCIPAL = abaqusConstants.MID_PRINCIPAL
MILLING_REGION = abaqusConstants.MILLING_REGION
MIN = abaqusConstants.MIN
MINIMIZE = abaqusConstants.MINIMIZE
MINIMIZED = abaqusConstants.MINIMIZED
MINIMIZE_MAXIMUM = abaqusConstants.MINIMIZE_MAXIMUM
MINIMUM = abaqusConstants.MINIMUM
MINIMUM_MAXIMUM = abaqusConstants.MINIMUM_MAXIMUM
MINIMUM_MOVE = abaqusConstants.MINIMUM_MOVE
MIN_EDGE = abaqusConstants.MIN_EDGE
MIN_INPLANE_PRINCIPAL = abaqusConstants.MIN_INPLANE_PRINCIPAL
MIN_MAX_EDGE = abaqusConstants.MIN_MAX_EDGE
MIN_MAX_LABEL = abaqusConstants.MIN_MAX_LABEL
MIN_PRINCIPAL = abaqusConstants.MIN_PRINCIPAL
MIN_PRINCIPAL_STRAIN = abaqusConstants.MIN_PRINCIPAL_STRAIN
MIN_SIZE_FACTOR = abaqusConstants.MIN_SIZE_FACTOR
MIN_STEP_SIZE = abaqusConstants.MIN_STEP_SIZE
MIN_TRANSITION = abaqusConstants.MIN_TRANSITION
MIN_VALUE = abaqusConstants.MIN_VALUE
MIRROR = abaqusConstants.MIRROR
MIRROR_CIRC_RECT = abaqusConstants.MIRROR_CIRC_RECT
MIRROR_RECT_CIRC = abaqusConstants.MIRROR_RECT_CIRC
MISES = abaqusConstants.MISES
MIXED = abaqusConstants.MIXED
MM = abaqusConstants.MM
MODAL = abaqusConstants.MODAL
MODAL_ALL = abaqusConstants.MODAL_ALL
MODAL_DYNAMICS = abaqusConstants.MODAL_DYNAMICS
MODEL = abaqusConstants.MODEL
MODEL_CHANGE = abaqusConstants.MODEL_CHANGE
MODEL_SIZE = abaqusConstants.MODEL_SIZE
MODERATE = abaqusConstants.MODERATE
MODERATE_DISSIPATION = abaqusConstants.MODERATE_DISSIPATION
MODES = abaqusConstants.MODES
MODE_BASED_DYNAMIC = abaqusConstants.MODE_BASED_DYNAMIC
MODE_BASED_STEADY_STATE_DYNAMIC = abaqusConstants.MODE_BASED_STEADY_STATE_DYNAMIC
MODE_INDEPENDENT = abaqusConstants.MODE_INDEPENDENT
MODE_NUMBER = abaqusConstants.MODE_NUMBER
MODE_RANGE = abaqusConstants.MODE_RANGE
MODIFIED = abaqusConstants.MODIFIED
MODIFIED_FROM_BASE_STATE = abaqusConstants.MODIFIED_FROM_BASE_STATE
MOMENT = abaqusConstants.MOMENT
MONITOR_DATA = abaqusConstants.MONITOR_DATA
MOONEY_RIVLIN = abaqusConstants.MOONEY_RIVLIN
MOTION = abaqusConstants.MOTION
MOTION_TYPE = abaqusConstants.MOTION_TYPE
MOVEMENT = abaqusConstants.MOVEMENT
MOVING_NOISE = abaqusConstants.MOVING_NOISE
MPC = abaqusConstants.MPC
MPI = abaqusConstants.MPI
MSBO = abaqusConstants.MSBO
MSFLD = abaqusConstants.MSFLD
MSPEI_XPL = abaqusConstants.MSPEI_XPL
MT = abaqusConstants.MT
MTS = abaqusConstants.MTS
MULTIPLE_DIRECTION_ABSOLUTE_SUM = abaqusConstants.MULTIPLE_DIRECTION_ABSOLUTE_SUM
MULTIPLE_DIRECTION_FORTY_PERCENT_RULE = abaqusConstants.MULTIPLE_DIRECTION_FORTY_PERCENT_RULE
MULTIPLE_DIRECTION_SRSS_SUM = abaqusConstants.MULTIPLE_DIRECTION_SRSS_SUM
MULTIPLE_DIRECTION_THIRTY_PERCENT_RULE = abaqusConstants.MULTIPLE_DIRECTION_THIRTY_PERCENT_RULE
MULTIPLE_SURFACE = abaqusConstants.MULTIPLE_SURFACE
MULTIPLICATIVE = abaqusConstants.MULTIPLICATIVE
MULTIPLY = abaqusConstants.MULTIPLY
N1 = abaqusConstants.N1
N1_COSINES = abaqusConstants.N1_COSINES
N2 = abaqusConstants.N2
NATURAL_FREQUENCY_EXTRACTION = abaqusConstants.NATURAL_FREQUENCY_EXTRACTION
NATURAL_LOG = abaqusConstants.NATURAL_LOG
NEAREST_INTEGER = abaqusConstants.NEAREST_INTEGER
NEGATE = abaqusConstants.NEGATE
NEGATIVE = abaqusConstants.NEGATIVE
NEO_HOOKE = abaqusConstants.NEO_HOOKE
NEVER = abaqusConstants.NEVER
NEWTONIAN = abaqusConstants.NEWTONIAN
NEW_CONTACT_PATCH = abaqusConstants.NEW_CONTACT_PATCH
NMORI = abaqusConstants.NMORI
NO = abaqusConstants.NO
NODAL = abaqusConstants.NODAL
NODAL_ANALYTICAL_FIELD = abaqusConstants.NODAL_ANALYTICAL_FIELD
NODAL_AVERAGE = abaqusConstants.NODAL_AVERAGE
NODAL_DISCRETE_FIELD = abaqusConstants.NODAL_DISCRETE_FIELD
NODAL_LINE = abaqusConstants.NODAL_LINE
NODE = abaqusConstants.NODE
NODES = abaqusConstants.NODES
NODE_ALL = abaqusConstants.NODE_ALL
NODE_CENTERED = abaqusConstants.NODE_CENTERED
NODE_LIST = abaqusConstants.NODE_LIST
NODE_MODE = abaqusConstants.NODE_MODE
NODE_MODE_MPC = abaqusConstants.NODE_MODE_MPC
NODE_PRESELECT = abaqusConstants.NODE_PRESELECT
NODE_TO_SURFACE = abaqusConstants.NODE_TO_SURFACE
NONACCUMULATEDENERGY = abaqusConstants.NONACCUMULATEDENERGY
NONE = abaqusConstants.NONE
NONLINEAR = abaqusConstants.NONLINEAR
NONREFLECTING = abaqusConstants.NONREFLECTING
NONUNIFORM = abaqusConstants.NONUNIFORM
NON_DEFAULT = abaqusConstants.NON_DEFAULT
NON_REFLECTING = abaqusConstants.NON_REFLECTING
NORM = abaqusConstants.NORM
NORMAL = abaqusConstants.NORMAL
NORMALIZED_CONCENTRATION_FIELD = abaqusConstants.NORMALIZED_CONCENTRATION_FIELD
NORMALS = abaqusConstants.NORMALS
NORMAL_ANNOTATED = abaqusConstants.NORMAL_ANNOTATED
NORMAL_TANGENTIAL = abaqusConstants.NORMAL_TANGENTIAL
NORMAL_VECTOR = abaqusConstants.NORMAL_VECTOR
NORM_DISTANCE = abaqusConstants.NORM_DISTANCE
NORM_FIRST = abaqusConstants.NORM_FIRST
NOT_ALLOWED = abaqusConstants.NOT_ALLOWED
NOT_APPLICABLE = abaqusConstants.NOT_APPLICABLE
NOT_SET = abaqusConstants.NOT_SET
NOT_YET_ACTIVE = abaqusConstants.NOT_YET_ACTIVE
NO_BLOCKING = abaqusConstants.NO_BLOCKING
NO_EXTRAPOLATION = abaqusConstants.NO_EXTRAPOLATION
NO_HEAD = abaqusConstants.NO_HEAD
NO_IDEALIZATION = abaqusConstants.NO_IDEALIZATION
NO_INDEPENDENT_COMPONENTS = abaqusConstants.NO_INDEPENDENT_COMPONENTS
NO_INITIAL_INTERSECTION = abaqusConstants.NO_INITIAL_INTERSECTION
NO_LIMIT = abaqusConstants.NO_LIMIT
NO_LINE = abaqusConstants.NO_LINE
NO_LONGER_ACTIVE = abaqusConstants.NO_LONGER_ACTIVE
NO_OUTPUT = abaqusConstants.NO_OUTPUT
NO_OUTPUT_VARIABLES = abaqusConstants.NO_OUTPUT_VARIABLES
NO_REFINEMENT = abaqusConstants.NO_REFINEMENT
NO_SIMPLIFICATION = abaqusConstants.NO_SIMPLIFICATION
NO_SLIP = abaqusConstants.NO_SLIP
NRL = abaqusConstants.NRL
NSET_MAP = abaqusConstants.NSET_MAP
NT = abaqusConstants.NT
NTH_POWER = abaqusConstants.NTH_POWER
NTH_ROOT = abaqusConstants.NTH_ROOT
NUMBER = abaqusConstants.NUMBER
NUMBERS = abaqusConstants.NUMBERS
NUMBER_INTERVALS = abaqusConstants.NUMBER_INTERVALS
NUMBER_OF_LAYERS = abaqusConstants.NUMBER_OF_LAYERS
NUMBER_OF_VALUES = abaqusConstants.NUMBER_OF_VALUES
NUMERICAL_PROBLEM = abaqusConstants.NUMERICAL_PROBLEM
NUM_ATTEMPTS = abaqusConstants.NUM_ATTEMPTS
NUM_DATA_TYPE = abaqusConstants.NUM_DATA_TYPE
NUM_ELEMENTS_EXCEEDING = abaqusConstants.NUM_ELEMENTS_EXCEEDING
NUM_EQI = abaqusConstants.NUM_EQI
NUM_ITERS = abaqusConstants.NUM_ITERS
NUM_PTS_ALONG_DIR = abaqusConstants.NUM_PTS_ALONG_DIR
NUM_PTS_BETWEEN_PTS = abaqusConstants.NUM_PTS_BETWEEN_PTS
NUM_SDI = abaqusConstants.NUM_SDI
OBLIQUE_DOWN = abaqusConstants.OBLIQUE_DOWN
OBLIQUE_UP = abaqusConstants.OBLIQUE_UP
ODB = abaqusConstants.ODB
ODB_FILE = abaqusConstants.ODB_FILE
ODB_FRAME = abaqusConstants.ODB_FRAME
ODB_REGIONS = abaqusConstants.ODB_REGIONS
ODB_VALUES = abaqusConstants.ODB_VALUES
OFFSET_FIELD = abaqusConstants.OFFSET_FIELD
OGDEN = abaqusConstants.OGDEN
OGDEN_N1 = abaqusConstants.OGDEN_N1
OGDEN_N2 = abaqusConstants.OGDEN_N2
OGDEN_N3 = abaqusConstants.OGDEN_N3
OGDEN_N4 = abaqusConstants.OGDEN_N4
OGDEN_N5 = abaqusConstants.OGDEN_N5
OGDEN_N6 = abaqusConstants.OGDEN_N6
OMIT = abaqusConstants.OMIT
ONE_CONFIG = abaqusConstants.ONE_CONFIG
ONLY = abaqusConstants.ONLY
OPENINGS = abaqusConstants.OPENINGS
OPEN_GL = abaqusConstants.OPEN_GL
OPTIMIZATION_DISPLACEMENT = abaqusConstants.OPTIMIZATION_DISPLACEMENT
OPT_DATASAVE_EVERY_CYCLE = abaqusConstants.OPT_DATASAVE_EVERY_CYCLE
OPT_DATASAVE_FIRST_AND_LAST_CYCLE = abaqusConstants.OPT_DATASAVE_FIRST_AND_LAST_CYCLE
OPT_DATASAVE_SPECIFY_CYCLE = abaqusConstants.OPT_DATASAVE_SPECIFY_CYCLE
OPT_EXTRACT_SMOOTH_ABAQUS_INPUT_FILE = abaqusConstants.OPT_EXTRACT_SMOOTH_ABAQUS_INPUT_FILE
OPT_EXTRACT_SMOOTH_NONE = abaqusConstants.OPT_EXTRACT_SMOOTH_NONE
OPT_EXTRACT_SMOOTH_STL = abaqusConstants.OPT_EXTRACT_SMOOTH_STL
ORDINATE = abaqusConstants.ORDINATE
ORIENTATION = abaqusConstants.ORIENTATION
ORIENT_FIELD = abaqusConstants.ORIENT_FIELD
ORIENT_ON_DEF = abaqusConstants.ORIENT_ON_DEF
ORIENT_ON_UNDEF = abaqusConstants.ORIENT_ON_UNDEF
ORIGINAL = abaqusConstants.ORIGINAL
ORIGINAL_MODEL = abaqusConstants.ORIGINAL_MODEL
ORIGIN_AXIS = abaqusConstants.ORIGIN_AXIS
ORTHOGONAL = abaqusConstants.ORTHOGONAL
ORTHOTROPIC = abaqusConstants.ORTHOTROPIC
OTHER = abaqusConstants.OTHER
OTHER_BC = abaqusConstants.OTHER_BC
OUTFLOW = abaqusConstants.OUTFLOW
OUTOFPLANE_PRINCIPAL = abaqusConstants.OUTOFPLANE_PRINCIPAL
OUTPUT = abaqusConstants.OUTPUT
OUTSIDE = abaqusConstants.OUTSIDE
OUTWARD = abaqusConstants.OUTWARD
OUT_OF_PLANE_EXTENSION_RATIO_NOT_FOUND = abaqusConstants.OUT_OF_PLANE_EXTENSION_RATIO_NOT_FOUND
OVERCLOSED = abaqusConstants.OVERCLOSED
OVERCLOSURES = abaqusConstants.OVERCLOSURES
OVERCONSTRAINT = abaqusConstants.OVERCONSTRAINT
OVERHANG_REGION = abaqusConstants.OVERHANG_REGION
OVERLAY = abaqusConstants.OVERLAY
OVERWRITE = abaqusConstants.OVERWRITE
PACKAGER_PHASE = abaqusConstants.PACKAGER_PHASE
PARABOLA = abaqusConstants.PARABOLA
PARABOLIC = abaqusConstants.PARABOLIC
PARABOLIC_EXTRAPOLATION = abaqusConstants.PARABOLIC_EXTRAPOLATION
PARALLEL = abaqusConstants.PARALLEL
PARAMETERS = abaqusConstants.PARAMETERS
PARAMETRIC_DATA = abaqusConstants.PARAMETRIC_DATA
PART = abaqusConstants.PART
PARTIAL_BLOCKING = abaqusConstants.PARTIAL_BLOCKING
PARTIAL_FIELD = abaqusConstants.PARTIAL_FIELD
PART_ASSEMBLY = abaqusConstants.PART_ASSEMBLY
PART_GEOM_MAP = abaqusConstants.PART_GEOM_MAP
PART_GEOM_MAP_COLORS = abaqusConstants.PART_GEOM_MAP_COLORS
PART_MAP = abaqusConstants.PART_MAP
PART_MAP_COLORS = abaqusConstants.PART_MAP_COLORS
PATH = abaqusConstants.PATH
PATH_POINTS = abaqusConstants.PATH_POINTS
PATH_X = abaqusConstants.PATH_X
PATH_Y = abaqusConstants.PATH_Y
PATH_Z = abaqusConstants.PATH_Z
PATTERN_ALONG_DIRECTION = abaqusConstants.PATTERN_ALONG_DIRECTION
PATTERN_INVALID = abaqusConstants.PATTERN_INVALID
PATTERN_ORTHOGONALLY = abaqusConstants.PATTERN_ORTHOGONALLY
PENALTY = abaqusConstants.PENALTY
PENETRATION_TOLERANCE_EXCEEDED = abaqusConstants.PENETRATION_TOLERANCE_EXCEEDED
PERCENTAGE = abaqusConstants.PERCENTAGE
PERIMETER = abaqusConstants.PERIMETER
PERIOD = abaqusConstants.PERIOD
PERP = abaqusConstants.PERP
PERPENDICULAR = abaqusConstants.PERPENDICULAR
PERSPECTIVE = abaqusConstants.PERSPECTIVE
PERTURBATION_AND_BUCKLING = abaqusConstants.PERTURBATION_AND_BUCKLING
PHASE = abaqusConstants.PHASE
PHONG = abaqusConstants.PHONG
PICKED = abaqusConstants.PICKED
PICKEDPOINTS = abaqusConstants.PICKEDPOINTS
PIEZOELECTRIC = abaqusConstants.PIEZOELECTRIC
PIEZO_ELECTRICAL_POTENTIAL_FIELD = abaqusConstants.PIEZO_ELECTRICAL_POTENTIAL_FIELD
PINNED = abaqusConstants.PINNED
PIN_MPC = abaqusConstants.PIN_MPC
PIPE21 = abaqusConstants.PIPE21
PIPE21H = abaqusConstants.PIPE21H
PIPE22 = abaqusConstants.PIPE22
PIPE22H = abaqusConstants.PIPE22H
PIPE31 = abaqusConstants.PIPE31
PIPE31H = abaqusConstants.PIPE31H
PIPE32 = abaqusConstants.PIPE32
PIPE32H = abaqusConstants.PIPE32H
PLANAR = abaqusConstants.PLANAR
PLANE = abaqusConstants.PLANE
PLANE12 = abaqusConstants.PLANE12
PLANE13 = abaqusConstants.PLANE13
PLANE21 = abaqusConstants.PLANE21
PLANE23 = abaqusConstants.PLANE23
PLANE31 = abaqusConstants.PLANE31
PLANE32 = abaqusConstants.PLANE32
PLASTIC_MOTION = abaqusConstants.PLASTIC_MOTION
PLAY = abaqusConstants.PLAY
PLAY_ONCE = abaqusConstants.PLAY_ONCE
PLOT_MAP = abaqusConstants.PLOT_MAP
PLOT_MAP_COLORS = abaqusConstants.PLOT_MAP_COLORS
PLOT_OPTIONS = abaqusConstants.PLOT_OPTIONS
PLOT_STATE = abaqusConstants.PLOT_STATE
PLY = abaqusConstants.PLY
PLY_BASED = abaqusConstants.PLY_BASED
PLY_MAP = abaqusConstants.PLY_MAP
PLY_MAP_COLORS = abaqusConstants.PLY_MAP_COLORS
PNEUMATIC = abaqusConstants.PNEUMATIC
PNG = abaqusConstants.PNG
POINT = abaqusConstants.POINT
POINTLINEDIST = abaqusConstants.POINTLINEDIST
POINTPOINTDIST = abaqusConstants.POINTPOINTDIST
POINTS = abaqusConstants.POINTS
POINTS_NOW_SLIPPING = abaqusConstants.POINTS_NOW_SLIPPING
POINTS_NOW_STICKING = abaqusConstants.POINTS_NOW_STICKING
POINTS_THROUGH_SECTION = abaqusConstants.POINTS_THROUGH_SECTION
POINTWISE = abaqusConstants.POINTWISE
POINT_ARC = abaqusConstants.POINT_ARC
POINT_LIST = abaqusConstants.POINT_LIST
POISSON = abaqusConstants.POISSON
POISSON_RATIO = abaqusConstants.POISSON_RATIO
POLAR = abaqusConstants.POLAR
POLYNOMIAL = abaqusConstants.POLYNOMIAL
POLY_N1 = abaqusConstants.POLY_N1
POLY_N2 = abaqusConstants.POLY_N2
POLY_N3 = abaqusConstants.POLY_N3
POLY_N4 = abaqusConstants.POLY_N4
POLY_N5 = abaqusConstants.POLY_N5
POLY_N6 = abaqusConstants.POLY_N6
PORE_FLUID_CONTACT = abaqusConstants.PORE_FLUID_CONTACT
PORE_FLUID_DIFFUSION = abaqusConstants.PORE_FLUID_DIFFUSION
PORE_LIQUID_PRESSURE_FIELD = abaqusConstants.PORE_LIQUID_PRESSURE_FIELD
PORTRAIT = abaqusConstants.PORTRAIT
POSITION = abaqusConstants.POSITION
POSITIONS = abaqusConstants.POSITIONS
POSITIVE = abaqusConstants.POSITIVE
POWER = abaqusConstants.POWER
POWER_LAW = abaqusConstants.POWER_LAW
PREDEFINED = abaqusConstants.PREDEFINED
PREDEFINED_FIELD = abaqusConstants.PREDEFINED_FIELD
PREDEFINED_PATH = abaqusConstants.PREDEFINED_PATH
PRESCRIBEDCONDITION_DOF = abaqusConstants.PRESCRIBEDCONDITION_DOF
PRESELECT = abaqusConstants.PRESELECT
PRESERVE_SECTION = abaqusConstants.PRESERVE_SECTION
PRESS = abaqusConstants.PRESS
PRESSURE = abaqusConstants.PRESSURE
PRESSURE_GRADIENT = abaqusConstants.PRESSURE_GRADIENT
PRESSURE_PENETRATION = abaqusConstants.PRESSURE_PENETRATION
PRESSURE_STRESS_CONSTRAINT = abaqusConstants.PRESSURE_STRESS_CONSTRAINT
PREVIOUS = abaqusConstants.PREVIOUS
PREVIOUS_STEP = abaqusConstants.PREVIOUS_STEP
PRIMARY_VECTOR = abaqusConstants.PRIMARY_VECTOR
PRINCIPAL = abaqusConstants.PRINCIPAL
PRINCIPAL_COMPONENT = abaqusConstants.PRINCIPAL_COMPONENT
PRINTER = abaqusConstants.PRINTER
PROJECTION_CARTESIAN = abaqusConstants.PROJECTION_CARTESIAN
PROJECTION_FLEXION_TORSION = abaqusConstants.PROJECTION_FLEXION_TORSION
PROJECT_BY_DIRECTION = abaqusConstants.PROJECT_BY_DIRECTION
PROJECT_BY_DISTANCE = abaqusConstants.PROJECT_BY_DISTANCE
PROJECT_BY_NUMBER = abaqusConstants.PROJECT_BY_NUMBER
PROJECT_BY_PROXIMITY = abaqusConstants.PROJECT_BY_PROXIMITY
PROLATE = abaqusConstants.PROLATE
PRONY = abaqusConstants.PRONY
PROPAGATED = abaqusConstants.PROPAGATED
PROPAGATED_FROM_BASE_STATE = abaqusConstants.PROPAGATED_FROM_BASE_STATE
PROPAGATED_FROM_COMPUTED = abaqusConstants.PROPAGATED_FROM_COMPUTED
PROPAGATED_FROM_FREQUENCY = abaqusConstants.PROPAGATED_FROM_FREQUENCY
PROPERTY_CHANGE = abaqusConstants.PROPERTY_CHANGE
PROPERTY_MAP = abaqusConstants.PROPERTY_MAP
PROPERTY_MAP_COLORS = abaqusConstants.PROPERTY_MAP_COLORS
PROPERTY_REF = abaqusConstants.PROPERTY_REF
PS = abaqusConstants.PS
PSI24 = abaqusConstants.PSI24
PSI26 = abaqusConstants.PSI26
PSI34 = abaqusConstants.PSI34
PSI36 = abaqusConstants.PSI36
PS_ALWAYS = abaqusConstants.PS_ALWAYS
PS_IF_AVAILABLE = abaqusConstants.PS_IF_AVAILABLE
PYR5 = abaqusConstants.PYR5
Q3D10M = abaqusConstants.Q3D10M
Q3D10MH = abaqusConstants.Q3D10MH
Q3D20 = abaqusConstants.Q3D20
Q3D20H = abaqusConstants.Q3D20H
Q3D20R = abaqusConstants.Q3D20R
Q3D20RH = abaqusConstants.Q3D20RH
Q3D4 = abaqusConstants.Q3D4
Q3D6 = abaqusConstants.Q3D6
Q3D8 = abaqusConstants.Q3D8
Q3D8H = abaqusConstants.Q3D8H
Q3D8R = abaqusConstants.Q3D8R
Q3D8RH = abaqusConstants.Q3D8RH
QUAD = abaqusConstants.QUAD
QUAD4 = abaqusConstants.QUAD4
QUAD8 = abaqusConstants.QUAD8
QUADRATIC = abaqusConstants.QUADRATIC
QUADS = abaqusConstants.QUADS
QUAD_DOMINATED = abaqusConstants.QUAD_DOMINATED
QUAD_SEPARATION = abaqusConstants.QUAD_SEPARATION
QUAD_STRIP = abaqusConstants.QUAD_STRIP
QUAD_TRACTION = abaqusConstants.QUAD_TRACTION
QUASI_NEWTON = abaqusConstants.QUASI_NEWTON
QUASI_NEWTON_METHOD = abaqusConstants.QUASI_NEWTON_METHOD
QUASI_STATIC = abaqusConstants.QUASI_STATIC
QUATERNION_2D = abaqusConstants.QUATERNION_2D
QUATERNION_3D = abaqusConstants.QUATERNION_3D
QUICKTIME = abaqusConstants.QUICKTIME
QUILT = abaqusConstants.QUILT
QUINTIC = abaqusConstants.QUINTIC
Q_VECTORS = abaqusConstants.Q_VECTORS
R2D2 = abaqusConstants.R2D2
R3D3 = abaqusConstants.R3D3
R3D4 = abaqusConstants.R3D4
RADIAL = abaqusConstants.RADIAL
RADIAL_THRUST = abaqusConstants.RADIAL_THRUST
RADIATION_ALL = abaqusConstants.RADIATION_ALL
RADIUS = abaqusConstants.RADIUS
RAINBOW = abaqusConstants.RAINBOW
RAMP = abaqusConstants.RAMP
RANDOM_RESPONSE = abaqusConstants.RANDOM_RESPONSE
RANGE = abaqusConstants.RANGE
RASTER = abaqusConstants.RASTER
RATE = abaqusConstants.RATE
RATE_OF_CONVERGENCE_IS_SLOW = abaqusConstants.RATE_OF_CONVERGENCE_IS_SLOW
RAW24 = abaqusConstants.RAW24
RAW32 = abaqusConstants.RAW32
RAW8 = abaqusConstants.RAW8
RAW_DATA = abaqusConstants.RAW_DATA
RAX2 = abaqusConstants.RAX2
RB2D2 = abaqusConstants.RB2D2
RB3D2 = abaqusConstants.RB3D2
REAL = abaqusConstants.REAL
REAL_AND_IMAGINARY = abaqusConstants.REAL_AND_IMAGINARY
REAL_ONLY = abaqusConstants.REAL_ONLY
REBAR = abaqusConstants.REBAR
RECIEVE_PREDICTION = abaqusConstants.RECIEVE_PREDICTION
RECOMPUTE_EACH_FRAME = abaqusConstants.RECOMPUTE_EACH_FRAME
RECOMPUTE_GEOMETRY = abaqusConstants.RECOMPUTE_GEOMETRY
RECOVER = abaqusConstants.RECOVER
RECT_CIRC_MIRROR = abaqusConstants.RECT_CIRC_MIRROR
RECT_MIRROR_CIRC = abaqusConstants.RECT_MIRROR_CIRC
RECURSIVE = abaqusConstants.RECURSIVE
REDUCED_POLYNOMIAL = abaqusConstants.REDUCED_POLYNOMIAL
REDUCED_POLYNOMIAL_ALL = abaqusConstants.REDUCED_POLYNOMIAL_ALL
REDUCED_POLYNOMIAL_N1 = abaqusConstants.REDUCED_POLYNOMIAL_N1
REDUCED_POLYNOMIAL_N2 = abaqusConstants.REDUCED_POLYNOMIAL_N2
REDUCED_POLYNOMIAL_N3 = abaqusConstants.REDUCED_POLYNOMIAL_N3
REDUCED_POLYNOMIAL_N4 = abaqusConstants.REDUCED_POLYNOMIAL_N4
REDUCED_POLYNOMIAL_N5 = abaqusConstants.REDUCED_POLYNOMIAL_N5
REDUCED_POLYNOMIAL_N6 = abaqusConstants.REDUCED_POLYNOMIAL_N6
RED_TO_BLUE = abaqusConstants.RED_TO_BLUE
REEDER = abaqusConstants.REEDER
REFERENCE = abaqusConstants.REFERENCE
REGION = abaqusConstants.REGION
REGULAR = abaqusConstants.REGULAR
REGULAR_BEAM = abaqusConstants.REGULAR_BEAM
REGULAR_SHELL = abaqusConstants.REGULAR_SHELL
REINFORCEMENT = abaqusConstants.REINFORCEMENT
REINITIALIZE = abaqusConstants.REINITIALIZE
RELATIVE = abaqusConstants.RELATIVE
RELATIVE_EQUAL = abaqusConstants.RELATIVE_EQUAL
RELATIVE_GREATER_THAN_EQUAL = abaqusConstants.RELATIVE_GREATER_THAN_EQUAL
RELATIVE_LESS_THAN_EQUAL = abaqusConstants.RELATIVE_LESS_THAN_EQUAL
RELATIVE_SLOPE_DROP = abaqusConstants.RELATIVE_SLOPE_DROP
RELATIVE_VALUE = abaqusConstants.RELATIVE_VALUE
RELAXATION = abaqusConstants.RELAXATION
RELAXATION_TEST_DATA = abaqusConstants.RELAXATION_TEST_DATA
RELAX_STIFFNESS = abaqusConstants.RELAX_STIFFNESS
REMOVE = abaqusConstants.REMOVE
REPETITIVE_SDI_PATTERN = abaqusConstants.REPETITIVE_SDI_PATTERN
REPLACE = abaqusConstants.REPLACE
RESET_TO_INITIAL = abaqusConstants.RESET_TO_INITIAL
RESIDUAL_ACCEPTED = abaqusConstants.RESIDUAL_ACCEPTED
RESIDUAL_NOT_ACCEPTED = abaqusConstants.RESIDUAL_NOT_ACCEPTED
RESPONSE_SPECTRUM = abaqusConstants.RESPONSE_SPECTRUM
RESTART = abaqusConstants.RESTART
RESTRICTED_TASK_REGION_EQUIV_STRESS = abaqusConstants.RESTRICTED_TASK_REGION_EQUIV_STRESS
RESULTANT = abaqusConstants.RESULTANT
RETENTION_FACTOR = abaqusConstants.RETENTION_FACTOR
RETRACTOR = abaqusConstants.RETRACTOR
REVERSE = abaqusConstants.REVERSE
REVERSED_RAINBOW = abaqusConstants.REVERSED_RAINBOW
REVERSE_MIRROR = abaqusConstants.REVERSE_MIRROR
REVOLUTE = abaqusConstants.REVOLUTE
REVOLUTION = abaqusConstants.REVOLUTION
RIGHT = abaqusConstants.RIGHT
RIGID = abaqusConstants.RIGID
RIGID_BODY = abaqusConstants.RIGID_BODY
RIGID_SPRING_RIGID = abaqusConstants.RIGID_SPRING_RIGID
RIKS = abaqusConstants.RIKS
RLE24 = abaqusConstants.RLE24
RLE8 = abaqusConstants.RLE8
ROLLING = abaqusConstants.ROLLING
ROTARYI = abaqusConstants.ROTARYI
ROTARY_INERTIA = abaqusConstants.ROTARY_INERTIA
ROTATE = abaqusConstants.ROTATE
ROTATION = abaqusConstants.ROTATION
ROTATIONAL_ACCELERATION = abaqusConstants.ROTATIONAL_ACCELERATION
ROTATIONAL_VELOCITY = abaqusConstants.ROTATIONAL_VELOCITY
ROTATION_ACCELEROMETER = abaqusConstants.ROTATION_ACCELEROMETER
ROTATION_ANGLE = abaqusConstants.ROTATION_ANGLE
ROTATION_FIELD = abaqusConstants.ROTATION_FIELD
ROTATION_NONE = abaqusConstants.ROTATION_NONE
ROUGH = abaqusConstants.ROUGH
RSH = abaqusConstants.RSH
RSS = abaqusConstants.RSS
RUNNING = abaqusConstants.RUNNING
S1 = abaqusConstants.S1
S2 = abaqusConstants.S2
S3 = abaqusConstants.S3
S3R = abaqusConstants.S3R
S3RS = abaqusConstants.S3RS
S3RT = abaqusConstants.S3RT
S3T = abaqusConstants.S3T
S4 = abaqusConstants.S4
S4R = abaqusConstants.S4R
S4R5 = abaqusConstants.S4R5
S4RS = abaqusConstants.S4RS
S4RSW = abaqusConstants.S4RSW
S4RT = abaqusConstants.S4RT
S4T = abaqusConstants.S4T
S5 = abaqusConstants.S5
S6 = abaqusConstants.S6
S8R = abaqusConstants.S8R
S8R5 = abaqusConstants.S8R5
S8RT = abaqusConstants.S8RT
SAX1 = abaqusConstants.SAX1
SAX2 = abaqusConstants.SAX2
SAX2T = abaqusConstants.SAX2T
SAXA11 = abaqusConstants.SAXA11
SAXA12 = abaqusConstants.SAXA12
SAXA13 = abaqusConstants.SAXA13
SAXA14 = abaqusConstants.SAXA14
SAXA21 = abaqusConstants.SAXA21
SAXA22 = abaqusConstants.SAXA22
SAXA23 = abaqusConstants.SAXA23
SAXA24 = abaqusConstants.SAXA24
SC6R = abaqusConstants.SC6R
SC6RT = abaqusConstants.SC6RT
SC8R = abaqusConstants.SC8R
SC8RT = abaqusConstants.SC8RT
SCALAR = abaqusConstants.SCALAR
SCALE = abaqusConstants.SCALE
SCALE_FACTOR = abaqusConstants.SCALE_FACTOR
SCATTERED = abaqusConstants.SCATTERED
SCIENTIFIC = abaqusConstants.SCIENTIFIC
SCREEN = abaqusConstants.SCREEN
SCREEN_SIZE = abaqusConstants.SCREEN_SIZE
SECOND = abaqusConstants.SECOND
SECOND_ORDER_ADVECTION = abaqusConstants.SECOND_ORDER_ADVECTION
SECTION = abaqusConstants.SECTION
SECTION_MAP = abaqusConstants.SECTION_MAP
SECTION_MAP_COLORS = abaqusConstants.SECTION_MAP_COLORS
SECTION_PTS = abaqusConstants.SECTION_PTS
SEGMENTS = abaqusConstants.SEGMENTS
SELECTED = abaqusConstants.SELECTED
SELECTION_GRP_MAP = abaqusConstants.SELECTION_GRP_MAP
SELECTION_GRP_MAP_COLORS = abaqusConstants.SELECTION_GRP_MAP_COLORS
SELECTIVE = abaqusConstants.SELECTIVE
SELECT_ALL = abaqusConstants.SELECT_ALL
SELECT_BY_ANGLE = abaqusConstants.SELECT_BY_ANGLE
SELECT_BY_NUMBER = abaqusConstants.SELECT_BY_NUMBER
SELF = abaqusConstants.SELF
SEMI_AUTOMATIC = abaqusConstants.SEMI_AUTOMATIC
SEND_PREDICTION = abaqusConstants.SEND_PREDICTION
SEPARATE = abaqusConstants.SEPARATE
SEPARATED = abaqusConstants.SEPARATED
SEPARATED_SOLUTION = abaqusConstants.SEPARATED_SOLUTION
SEPARATE_TABLES = abaqusConstants.SEPARATE_TABLES
SEQUENTIAL_THERMAL_STRESS = abaqusConstants.SEQUENTIAL_THERMAL_STRESS
SEQ_ID = abaqusConstants.SEQ_ID
SET = abaqusConstants.SET
SET_EQUAL_DT = abaqusConstants.SET_EQUAL_DT
SET_MAP = abaqusConstants.SET_MAP
SET_MAP_COLORS = abaqusConstants.SET_MAP_COLORS
SEVERE_CONTACT_OVERCLOSURES = abaqusConstants.SEVERE_CONTACT_OVERCLOSURES
SEVERE_OVERCLOSURES = abaqusConstants.SEVERE_OVERCLOSURES
SFM3D3 = abaqusConstants.SFM3D3
SFM3D4 = abaqusConstants.SFM3D4
SFM3D4R = abaqusConstants.SFM3D4R
SFM3D6 = abaqusConstants.SFM3D6
SFM3D8 = abaqusConstants.SFM3D8
SFM3D8R = abaqusConstants.SFM3D8R
SFMAX1 = abaqusConstants.SFMAX1
SFMAX2 = abaqusConstants.SFMAX2
SFMCL6 = abaqusConstants.SFMCL6
SFMCL9 = abaqusConstants.SFMCL9
SFMGAX1 = abaqusConstants.SFMGAX1
SFMGAX2 = abaqusConstants.SFMGAX2
SHADED = abaqusConstants.SHADED
SHAPE_FACTOR = abaqusConstants.SHAPE_FACTOR
SHARED_LM_PRESSURE_FIELD = abaqusConstants.SHARED_LM_PRESSURE_FIELD
SHARED_LM_VOLUME_FIELD = abaqusConstants.SHARED_LM_VOLUME_FIELD
SHEAR = abaqusConstants.SHEAR
SHEARCREEP = abaqusConstants.SHEARCREEP
SHEARRELAXATION = abaqusConstants.SHEARRELAXATION
SHELL = abaqusConstants.SHELL
SHELL_TO_SOLID_COUPLING = abaqusConstants.SHELL_TO_SOLID_COUPLING
SHORT = abaqusConstants.SHORT
SHORTEST_EDGE = abaqusConstants.SHORTEST_EDGE
SHORTEST_PATH = abaqusConstants.SHORTEST_PATH
SHORT_FIBER = abaqusConstants.SHORT_FIBER
SHRINK_FIT = abaqusConstants.SHRINK_FIT
SHRINK_MOVEMENT = abaqusConstants.SHRINK_MOVEMENT
SIDE1 = abaqusConstants.SIDE1
SIDE2 = abaqusConstants.SIDE2
SIGCONT = abaqusConstants.SIGCONT
SIGINT = abaqusConstants.SIGINT
SIGN = abaqusConstants.SIGN
SIGTERM = abaqusConstants.SIGTERM
SIGTSTP = abaqusConstants.SIGTSTP
SIGUSR1 = abaqusConstants.SIGUSR1
SIGUSR2 = abaqusConstants.SIGUSR2
SIM = abaqusConstants.SIM
SIMP = abaqusConstants.SIMP
SIMPLE = abaqusConstants.SIMPLE
SIMPLESHEAR = abaqusConstants.SIMPLESHEAR
SIMPSON = abaqusConstants.SIMPSON
SIMULATION_ABORTED = abaqusConstants.SIMULATION_ABORTED
SIMULATION_COMPLETED = abaqusConstants.SIMULATION_COMPLETED
SIMULATION_INTERRUPTED = abaqusConstants.SIMULATION_INTERRUPTED
SIMULATION_STARTED = abaqusConstants.SIMULATION_STARTED
SINE = abaqusConstants.SINE
SINGHM = abaqusConstants.SINGHM
SINGLE = abaqusConstants.SINGLE
SINGLE_DIRECTION = abaqusConstants.SINGLE_DIRECTION
SINGLE_NODE = abaqusConstants.SINGLE_NODE
SINGLE_PRECISION = abaqusConstants.SINGLE_PRECISION
SINGLE_TABLE = abaqusConstants.SINGLE_TABLE
SINGLE_VALUE = abaqusConstants.SINGLE_VALUE
SIZE = abaqusConstants.SIZE
SIZE_ON_SCREEN = abaqusConstants.SIZE_ON_SCREEN
SKINS = abaqusConstants.SKINS
SKIN_MAP = abaqusConstants.SKIN_MAP
SKIN_MAP_COLORS = abaqusConstants.SKIN_MAP_COLORS
SLASH = abaqusConstants.SLASH
SLAVE = abaqusConstants.SLAVE
SLIDE_DISTANCE_EXCEEDED = abaqusConstants.SLIDE_DISTANCE_EXCEEDED
SLIDE_PLANE = abaqusConstants.SLIDE_PLANE
SLIDING = abaqusConstants.SLIDING
SLIPPED_OFF_PATCH = abaqusConstants.SLIPPED_OFF_PATCH
SLIPRING = abaqusConstants.SLIPRING
SLOT = abaqusConstants.SLOT
SMALL = abaqusConstants.SMALL
SMALLEST_ELEM_AT_CENTER = abaqusConstants.SMALLEST_ELEM_AT_CENTER
SMALLEST_ELEM_AT_ENDS = abaqusConstants.SMALLEST_ELEM_AT_ENDS
SMALLEST_ELEM_LOCATION = abaqusConstants.SMALLEST_ELEM_LOCATION
SMALL_ANGLE = abaqusConstants.SMALL_ANGLE
SMALL_ANGLE_QUAD_FACE = abaqusConstants.SMALL_ANGLE_QUAD_FACE
SMALL_ANGLE_TRI_FACE = abaqusConstants.SMALL_ANGLE_TRI_FACE
SMEAR_ABOUT_CORE = abaqusConstants.SMEAR_ABOUT_CORE
SMEAR_ALL_LAYERS = abaqusConstants.SMEAR_ALL_LAYERS
SMOOTHING_AS_IS = abaqusConstants.SMOOTHING_AS_IS
SMOOTHING_OFF = abaqusConstants.SMOOTHING_OFF
SMOOTHING_ON = abaqusConstants.SMOOTHING_ON
SNEG = abaqusConstants.SNEG
SOFTWARE_OVERLAY = abaqusConstants.SOFTWARE_OVERLAY
SOFT_CONTACT_INCOMPATIBILITIES = abaqusConstants.SOFT_CONTACT_INCOMPATIBILITIES
SOILS = abaqusConstants.SOILS
SOLID = abaqusConstants.SOLID
SOLIDWORKS = abaqusConstants.SOLIDWORKS
SOLUTION_APPEARS_TO_BE_DIVERGING = abaqusConstants.SOLUTION_APPEARS_TO_BE_DIVERGING
SOLVER_DEFAULT = abaqusConstants.SOLVER_DEFAULT
SPALART = abaqusConstants.SPALART
SPECIFIED = abaqusConstants.SPECIFIED
SPECIFIED_LIMIT = abaqusConstants.SPECIFIED_LIMIT
SPECIFIED_MODES = abaqusConstants.SPECIFIED_MODES
SPECIFIED_NODAL_DIAMETER = abaqusConstants.SPECIFIED_NODAL_DIAMETER
SPECIFY = abaqusConstants.SPECIFY
SPECIFY_NUM_PTS = abaqusConstants.SPECIFY_NUM_PTS
SPECIFY_ORIENT = abaqusConstants.SPECIFY_ORIENT
SPECIFY_PATH = abaqusConstants.SPECIFY_PATH
SPECIFY_STEP_SIZE = abaqusConstants.SPECIFY_STEP_SIZE
SPECIFY_THICKNESS = abaqusConstants.SPECIFY_THICKNESS
SPECIFY_TOLERANCE = abaqusConstants.SPECIFY_TOLERANCE
SPECTRUM = abaqusConstants.SPECTRUM
SPHERE = abaqusConstants.SPHERE
SPHERICAL = abaqusConstants.SPHERICAL
SPIN = abaqusConstants.SPIN
SPLINE = abaqusConstants.SPLINE
SPLINE_APPROXIMATION = abaqusConstants.SPLINE_APPROXIMATION
SPLINE_INTERPOLATION = abaqusConstants.SPLINE_INTERPOLATION
SPOS = abaqusConstants.SPOS
SPOT_WELD_CONTACT = abaqusConstants.SPOT_WELD_CONTACT
SPRING1 = abaqusConstants.SPRING1
SPRING2 = abaqusConstants.SPRING2
SPRINGA = abaqusConstants.SPRINGA
SPRING_RIGID_SPRING = abaqusConstants.SPRING_RIGID_SPRING
SQUARE_ROOT = abaqusConstants.SQUARE_ROOT
SRSS = abaqusConstants.SRSS
SSH = abaqusConstants.SSH
SSOR = abaqusConstants.SSOR
STABILIZATION = abaqusConstants.STABILIZATION
STABILIZED = abaqusConstants.STABILIZED
STABLE_INC_XPL = abaqusConstants.STABLE_INC_XPL
STABLE_TIME_INCREMENT = abaqusConstants.STABLE_TIME_INCREMENT
STACK_1 = abaqusConstants.STACK_1
STACK_2 = abaqusConstants.STACK_2
STACK_3 = abaqusConstants.STACK_3
STACK_ORIENTATION = abaqusConstants.STACK_ORIENTATION
STAGNATION = abaqusConstants.STAGNATION
STAMP = abaqusConstants.STAMP
STANDALONE = abaqusConstants.STANDALONE
STANDALONENOSHOW = abaqusConstants.STANDALONENOSHOW
STANDARD = abaqusConstants.STANDARD
STANDARD_ANALYSIS = abaqusConstants.STANDARD_ANALYSIS
STANDARD_EXPLICIT = abaqusConstants.STANDARD_EXPLICIT
STANDARD_PHASE = abaqusConstants.STANDARD_PHASE
START = abaqusConstants.START
STARTED = abaqusConstants.STARTED
STATE_FRAME = abaqusConstants.STATE_FRAME
STATIC = abaqusConstants.STATIC
STATIC_GENERAL = abaqusConstants.STATIC_GENERAL
STATIC_LINEAR_PERTURBATION = abaqusConstants.STATIC_LINEAR_PERTURBATION
STATIC_PERTURBATION = abaqusConstants.STATIC_PERTURBATION
STATIC_RIKS = abaqusConstants.STATIC_RIKS
STATUS = abaqusConstants.STATUS
STEADY_STATE = abaqusConstants.STEADY_STATE
STEADY_STATE_DIRECT = abaqusConstants.STEADY_STATE_DIRECT
STEADY_STATE_MODAL = abaqusConstants.STEADY_STATE_MODAL
STEADY_STATE_SUBSPACE = abaqusConstants.STEADY_STATE_SUBSPACE
STEADY_STATE_TRANSPORT = abaqusConstants.STEADY_STATE_TRANSPORT
STEP = abaqusConstants.STEP
STEP_END = abaqusConstants.STEP_END
STEP_START = abaqusConstants.STEP_START
STEP_TIME = abaqusConstants.STEP_TIME
STEP_TIME_XPL = abaqusConstants.STEP_TIME_XPL
STIFFNESS = abaqusConstants.STIFFNESS
STIFFNESS_OPTIMIZATION = abaqusConstants.STIFFNESS_OPTIMIZATION
STIPPLED = abaqusConstants.STIPPLED
STOP = abaqusConstants.STOP
STRAIN = abaqusConstants.STRAIN
STRAIN_FREE_CORRECTIONS = abaqusConstants.STRAIN_FREE_CORRECTIONS
STRAIN_RATE = abaqusConstants.STRAIN_RATE
STRESS = abaqusConstants.STRESS
STRESS_INTENS_FACTOR = abaqusConstants.STRESS_INTENS_FACTOR
STRESS_PERTURBATION = abaqusConstants.STRESS_PERTURBATION
STRI3 = abaqusConstants.STRI3
STRI65 = abaqusConstants.STRI65
STRINGERS = abaqusConstants.STRINGERS
STRINGER_MAP = abaqusConstants.STRINGER_MAP
STRINGER_MAP_COLORS = abaqusConstants.STRINGER_MAP_COLORS
STRUCTURAL = abaqusConstants.STRUCTURAL
STRUCTURED = abaqusConstants.STRUCTURED
SUBMISSION_ABORTED = abaqusConstants.SUBMISSION_ABORTED
SUBMITTED = abaqusConstants.SUBMITTED
SUBMODELING = abaqusConstants.SUBMODELING
SUBSPACE = abaqusConstants.SUBSPACE
SUBSPACE_DYNAMIC = abaqusConstants.SUBSPACE_DYNAMIC
SUBSPACE_EIGENSOLVER = abaqusConstants.SUBSPACE_EIGENSOLVER
SUBSPACE_STEADY_STATE_DYNAMIC = abaqusConstants.SUBSPACE_STEADY_STATE_DYNAMIC
SUBSTANCE = abaqusConstants.SUBSTANCE
SUBSTRUCTURE_GENERATE = abaqusConstants.SUBSTRUCTURE_GENERATE
SUBSTRUCTURING = abaqusConstants.SUBSTRUCTURING
SUBTRACT = abaqusConstants.SUBTRACT
SUM = abaqusConstants.SUM
SUPERIMPOSE = abaqusConstants.SUPERIMPOSE
SUPPRESS = abaqusConstants.SUPPRESS
SURFACE = abaqusConstants.SURFACE
SURFACE_BLAST = abaqusConstants.SURFACE_BLAST
SURFACE_INTEGRATION_POINT = abaqusConstants.SURFACE_INTEGRATION_POINT
SURFACE_MAP = abaqusConstants.SURFACE_MAP
SURFACE_MAP_COLORS = abaqusConstants.SURFACE_MAP_COLORS
SURFACE_NODAL = abaqusConstants.SURFACE_NODAL
SURFACE_POINT_EQUIV_STRESS = abaqusConstants.SURFACE_POINT_EQUIV_STRESS
SURFACE_TO_SURFACE = abaqusConstants.SURFACE_TO_SURFACE
SVG = abaqusConstants.SVG
SWEEP = abaqusConstants.SWEEP
SWING = abaqusConstants.SWING
SYMBOL = abaqusConstants.SYMBOL
SYMBOLS_ON_DEF = abaqusConstants.SYMBOLS_ON_DEF
SYMBOLS_ON_UNDEF = abaqusConstants.SYMBOLS_ON_UNDEF
SYMMETRIC = abaqusConstants.SYMMETRIC
SYMMETRIC_MODEL_GENERATION = abaqusConstants.SYMMETRIC_MODEL_GENERATION
SYNTAXCHECK = abaqusConstants.SYNTAXCHECK
SYSTEM = abaqusConstants.SYSTEM
SYSTEM_ASSIGN = abaqusConstants.SYSTEM_ASSIGN
SYSTEM_DEFINED = abaqusConstants.SYSTEM_DEFINED
T2D2 = abaqusConstants.T2D2
T2D2E = abaqusConstants.T2D2E
T2D2H = abaqusConstants.T2D2H
T2D2T = abaqusConstants.T2D2T
T2D3 = abaqusConstants.T2D3
T2D3E = abaqusConstants.T2D3E
T2D3H = abaqusConstants.T2D3H
T2D3T = abaqusConstants.T2D3T
T3D2 = abaqusConstants.T3D2
T3D2E = abaqusConstants.T3D2E
T3D2H = abaqusConstants.T3D2H
T3D2T = abaqusConstants.T3D2T
T3D3 = abaqusConstants.T3D3
T3D3E = abaqusConstants.T3D3E
T3D3H = abaqusConstants.T3D3H
T3D3T = abaqusConstants.T3D3T
TABULAR = abaqusConstants.TABULAR
TANGENT = abaqusConstants.TANGENT
TANGENTIAL = abaqusConstants.TANGENTIAL
TAPERED = abaqusConstants.TAPERED
TASK_REGION_EQUIV_STRESS = abaqusConstants.TASK_REGION_EQUIV_STRESS
TASK_REGION_LAYERS = abaqusConstants.TASK_REGION_LAYERS
TECHNIQUE = abaqusConstants.TECHNIQUE
TEMPERATURE = abaqusConstants.TEMPERATURE
TEMPERATURE_FALLEN_BELOW_ABSOLUTE_ZERO = abaqusConstants.TEMPERATURE_FALLEN_BELOW_ABSOLUTE_ZERO
TEMPERATURE_FIELD = abaqusConstants.TEMPERATURE_FIELD
TENP = abaqusConstants.TENP
TENSION = abaqusConstants.TENSION
TENSOR = abaqusConstants.TENSOR
TENSOR_2D_PLANAR = abaqusConstants.TENSOR_2D_PLANAR
TENSOR_2D_SURFACE = abaqusConstants.TENSOR_2D_SURFACE
TENSOR_3D_FULL = abaqusConstants.TENSOR_3D_FULL
TENSOR_3D_PLANAR = abaqusConstants.TENSOR_3D_PLANAR
TENSOR_3D_SURFACE = abaqusConstants.TENSOR_3D_SURFACE
TERMINATED = abaqusConstants.TERMINATED
TESSELLATED = abaqusConstants.TESSELLATED
TEST_DATA = abaqusConstants.TEST_DATA
TET = abaqusConstants.TET
TET10 = abaqusConstants.TET10
TET4 = abaqusConstants.TET4
TEXTURE_MAPPED = abaqusConstants.TEXTURE_MAPPED
THERMAL = abaqusConstants.THERMAL
THERMAL_CONTACT = abaqusConstants.THERMAL_CONTACT
THERMOMECHANICAL = abaqusConstants.THERMOMECHANICAL
THICK = abaqusConstants.THICK
THICKNESS = abaqusConstants.THICKNESS
THICKNESS_DISCRETE_FIELD = abaqusConstants.THICKNESS_DISCRETE_FIELD
THICKNESS_MAGNITUDE = abaqusConstants.THICKNESS_MAGNITUDE
THICK_WALL = abaqusConstants.THICK_WALL
THIN = abaqusConstants.THIN
THINNING = abaqusConstants.THINNING
THIN_WALL = abaqusConstants.THIN_WALL
THREADS = abaqusConstants.THREADS
THREED_DATA = abaqusConstants.THREED_DATA
THREE_D = abaqusConstants.THREE_D
THROUGHOUT_STEP = abaqusConstants.THROUGHOUT_STEP
TIE = abaqusConstants.TIE
TIE_MPC = abaqusConstants.TIE_MPC
TIFF = abaqusConstants.TIFF
TIGHTEN_GAPS = abaqusConstants.TIGHTEN_GAPS
TIME = abaqusConstants.TIME
TIME_AVERAGE = abaqusConstants.TIME_AVERAGE
TIME_BASED = abaqusConstants.TIME_BASED
TIME_HEAT_FLUX = abaqusConstants.TIME_HEAT_FLUX
TIME_HEAT_FLUX_AREA = abaqusConstants.TIME_HEAT_FLUX_AREA
TIME_HISTORY = abaqusConstants.TIME_HISTORY
TIME_INCREMENT = abaqusConstants.TIME_INCREMENT
TIME_INTEGRATION = abaqusConstants.TIME_INTEGRATION
TIME_INTEGRATION_ACCURACY_LIMIT_EXCEEDED = abaqusConstants.TIME_INTEGRATION_ACCURACY_LIMIT_EXCEEDED
TIME_INTEGRATION_STABILITY_LIMIT_EXCEEDED = abaqusConstants.TIME_INTEGRATION_STABILITY_LIMIT_EXCEEDED
TIME_INTERVAL = abaqusConstants.TIME_INTERVAL
TIME_INTERVAL_VALUE = abaqusConstants.TIME_INTERVAL_VALUE
TIME_POINT = abaqusConstants.TIME_POINT
TIME_VOLUME = abaqusConstants.TIME_VOLUME
TIME_VOLUME_FLUX = abaqusConstants.TIME_VOLUME_FLUX
TMORI = abaqusConstants.TMORI
TOLERANCE = abaqusConstants.TOLERANCE
TOP = abaqusConstants.TOP
TOP_AND_BOTTOM = abaqusConstants.TOP_AND_BOTTOM
TOP_CENTER = abaqusConstants.TOP_CENTER
TOP_LEFT = abaqusConstants.TOP_LEFT
TOP_RIGHT = abaqusConstants.TOP_RIGHT
TOP_SURFACE = abaqusConstants.TOP_SURFACE
TOROIDAL = abaqusConstants.TOROIDAL
TOTAL = abaqusConstants.TOTAL
TOTAL_ABSOLUTE_MOVEMENT = abaqusConstants.TOTAL_ABSOLUTE_MOVEMENT
TOTAL_FORCE = abaqusConstants.TOTAL_FORCE
TOTAL_MASS = abaqusConstants.TOTAL_MASS
TOTAL_MASS_XPL = abaqusConstants.TOTAL_MASS_XPL
TOTAL_NUM = abaqusConstants.TOTAL_NUM
TOTAL_NUMBER = abaqusConstants.TOTAL_NUMBER
TOTAL_TIME_XPL = abaqusConstants.TOTAL_TIME_XPL
TO_ENVIRONMENT = abaqusConstants.TO_ENVIRONMENT
TRACTION = abaqusConstants.TRACTION
TRACTION_SEPARATION = abaqusConstants.TRACTION_SEPARATION
TRANSFORMATION = abaqusConstants.TRANSFORMATION
TRANSIENT = abaqusConstants.TRANSIENT
TRANSIENT_FIDELITY = abaqusConstants.TRANSIENT_FIDELITY
TRANSLATE = abaqusConstants.TRANSLATE
TRANSLATOR = abaqusConstants.TRANSLATOR
TRANSPARENT = abaqusConstants.TRANSPARENT
TRANSVERSE = abaqusConstants.TRANSVERSE
TRANSVERSE_SHEAR_FORCE_CONSTRAINT = abaqusConstants.TRANSVERSE_SHEAR_FORCE_CONSTRAINT
TRAPEZOID = abaqusConstants.TRAPEZOID
TRESCA = abaqusConstants.TRESCA
TRI = abaqusConstants.TRI
TRIGGER = abaqusConstants.TRIGGER
TRI3 = abaqusConstants.TRI3
TRI6 = abaqusConstants.TRI6
TRIANGLES = abaqusConstants.TRIANGLES
TRIANGLE_FAN = abaqusConstants.TRIANGLE_FAN
TRIANGLE_STRIP = abaqusConstants.TRIANGLE_STRIP
TRIDIRECTIONAL = abaqusConstants.TRIDIRECTIONAL
TRUE_DISTANCE = abaqusConstants.TRUE_DISTANCE
TRUE_DISTANCE_X = abaqusConstants.TRUE_DISTANCE_X
TRUE_DISTANCE_Y = abaqusConstants.TRUE_DISTANCE_Y
TRUE_DISTANCE_Z = abaqusConstants.TRUE_DISTANCE_Z
TRUSS = abaqusConstants.TRUSS
TURB_NONE = abaqusConstants.TURB_NONE
TURN = abaqusConstants.TURN
TWIST = abaqusConstants.TWIST
TWO_CONFIG = abaqusConstants.TWO_CONFIG
TWO_D_PLANAR = abaqusConstants.TWO_D_PLANAR
TYPED_IN = abaqusConstants.TYPED_IN
TYPE_NOT_APPLICABLE = abaqusConstants.TYPE_NOT_APPLICABLE
T_STRESS = abaqusConstants.T_STRESS
U1 = abaqusConstants.U1
U2 = abaqusConstants.U2
U3 = abaqusConstants.U3
UJOINT = abaqusConstants.UJOINT
UNCHANGED = abaqusConstants.UNCHANGED
UNCONVERGED_CAP_PLASTICITY = abaqusConstants.UNCONVERGED_CAP_PLASTICITY
UNCONVERGED_CLAY_PLASTICITY = abaqusConstants.UNCONVERGED_CLAY_PLASTICITY
UNCONVERGED_CONCRETE_PLASTICITY = abaqusConstants.UNCONVERGED_CONCRETE_PLASTICITY
UNCONVERGED_CREEP_PLASTICITY = abaqusConstants.UNCONVERGED_CREEP_PLASTICITY
UNCONVERGED_DRUCKER_PRAGER_PLASTICITY = abaqusConstants.UNCONVERGED_DRUCKER_PRAGER_PLASTICITY
UNCONVERGED_FOAM_PLASTICITY = abaqusConstants.UNCONVERGED_FOAM_PLASTICITY
UNCONVERGED_HYPERELASTICITY = abaqusConstants.UNCONVERGED_HYPERELASTICITY
UNCONVERGED_METAL_PLASTICITY = abaqusConstants.UNCONVERGED_METAL_PLASTICITY
UNCONVERGED_MOHR_COULOMB_PLASTICITY = abaqusConstants.UNCONVERGED_MOHR_COULOMB_PLASTICITY
UNCORRELATED = abaqusConstants.UNCORRELATED
UNCOUPLED = abaqusConstants.UNCOUPLED
UNDEFINED_ANALYSIS = abaqusConstants.UNDEFINED_ANALYSIS
UNDEFINED_INVARIANT = abaqusConstants.UNDEFINED_INVARIANT
UNDEFINED_POSITION = abaqusConstants.UNDEFINED_POSITION
UNDEFORMED = abaqusConstants.UNDEFORMED
UNDEX = abaqusConstants.UNDEX
UNDEX_CHARGE = abaqusConstants.UNDEX_CHARGE
UNIAXIAL = abaqusConstants.UNIAXIAL
UNIAXIAL_VOLUMETRIC = abaqusConstants.UNIAXIAL_VOLUMETRIC
UNIDIRECTIONAL = abaqusConstants.UNIDIRECTIONAL
UNIFORM = abaqusConstants.UNIFORM
UNIFORM_BY_NUMBER = abaqusConstants.UNIFORM_BY_NUMBER
UNIFORM_BY_SIZE = abaqusConstants.UNIFORM_BY_SIZE
UNIFORM_ERROR = abaqusConstants.UNIFORM_ERROR
UNIFORM_SPACING = abaqusConstants.UNIFORM_SPACING
UNION = abaqusConstants.UNION
UNIVERSAL = abaqusConstants.UNIVERSAL
UNIX = abaqusConstants.UNIX
UNKNOWN = abaqusConstants.UNKNOWN
UNKNOWNAXIS = abaqusConstants.UNKNOWNAXIS
UNKNOWNPLANE = abaqusConstants.UNKNOWNPLANE
UNKNOWN_ANALYSIS_CODE = abaqusConstants.UNKNOWN_ANALYSIS_CODE
UNKNOWN_DIMENSION = abaqusConstants.UNKNOWN_DIMENSION
UNKNOWN_HEX = abaqusConstants.UNKNOWN_HEX
UNKNOWN_HOURGLASS_CONTROL = abaqusConstants.UNKNOWN_HOURGLASS_CONTROL
UNKNOWN_KINEMATIC_SPLIT = abaqusConstants.UNKNOWN_KINEMATIC_SPLIT
UNKNOWN_PHASE = abaqusConstants.UNKNOWN_PHASE
UNKNOWN_QUAD = abaqusConstants.UNKNOWN_QUAD
UNKNOWN_SHAPE = abaqusConstants.UNKNOWN_SHAPE
UNKNOWN_STRESS_RATE = abaqusConstants.UNKNOWN_STRESS_RATE
UNKNOWN_TET = abaqusConstants.UNKNOWN_TET
UNKNOWN_TRI = abaqusConstants.UNKNOWN_TRI
UNKNOWN_WEDGE = abaqusConstants.UNKNOWN_WEDGE
UNLIMITED = abaqusConstants.UNLIMITED
UNMESHABLE = abaqusConstants.UNMESHABLE
UNRESOLVED_INITIAL_OVERCLOSURES = abaqusConstants.UNRESOLVED_INITIAL_OVERCLOSURES
UNSET = abaqusConstants.UNSET
UNSPECIFIED = abaqusConstants.UNSPECIFIED
UNSYMMETRIC = abaqusConstants.UNSYMMETRIC
UR1 = abaqusConstants.UR1
UR2 = abaqusConstants.UR2
UR3 = abaqusConstants.UR3
USA_ADDED_MASS_GENERATION = abaqusConstants.USA_ADDED_MASS_GENERATION
USER = abaqusConstants.USER
USER_CUSTOMIZED = abaqusConstants.USER_CUSTOMIZED
USER_DEFINED = abaqusConstants.USER_DEFINED
USER_MPC = abaqusConstants.USER_MPC
USER_SPECIFIED = abaqusConstants.USER_SPECIFIED
USER_SUB = abaqusConstants.USER_SUB
USER_SUBROUTINE = abaqusConstants.USER_SUBROUTINE
USER_SUBROUTINE_REQUEST = abaqusConstants.USER_SUBROUTINE_REQUEST
USE_BOTTOM = abaqusConstants.USE_BOTTOM
USE_BOTTOM_AND_TOP = abaqusConstants.USE_BOTTOM_AND_TOP
USE_ENVELOPE = abaqusConstants.USE_ENVELOPE
USE_GEOMETRY = abaqusConstants.USE_GEOMETRY
USE_MESH = abaqusConstants.USE_MESH
USE_TOP = abaqusConstants.USE_TOP
USUP = abaqusConstants.USUP
VALUE = abaqusConstants.VALUE
VALUES = abaqusConstants.VALUES
VALUES_AND_HISTORY = abaqusConstants.VALUES_AND_HISTORY
VAN_DER_WAALS = abaqusConstants.VAN_DER_WAALS
VAN_DER_WALLS_STRETCHES_LOCKING = abaqusConstants.VAN_DER_WALLS_STRETCHES_LOCKING
VARIABLE_RATIO = abaqusConstants.VARIABLE_RATIO
VCCT = abaqusConstants.VCCT
VECTOR = abaqusConstants.VECTOR
VECTOR_COMPONENT = abaqusConstants.VECTOR_COMPONENT
VELOCITY = abaqusConstants.VELOCITY
VELOCITY_PARABOLIC = abaqusConstants.VELOCITY_PARABOLIC
VELOCITY_SQUARED = abaqusConstants.VELOCITY_SQUARED
VERTEX_ADJ_TO_SMALLEST_ELEM = abaqusConstants.VERTEX_ADJ_TO_SMALLEST_ELEM
VERTICAL = abaqusConstants.VERTICAL
VERY_SMALL = abaqusConstants.VERY_SMALL
VERY_THIN = abaqusConstants.VERY_THIN
VIEW_MANIP = abaqusConstants.VIEW_MANIP
VISCO = abaqusConstants.VISCO
VISCOUS = abaqusConstants.VISCOUS
VMS = abaqusConstants.VMS
VOID = abaqusConstants.VOID
VOLUME = abaqusConstants.VOLUME
VOLUMETRIC = abaqusConstants.VOLUMETRIC
VOLUMETRICCREEP = abaqusConstants.VOLUMETRICCREEP
VOLUMETRICRELAXATION = abaqusConstants.VOLUMETRICRELAXATION
VOLUMETRIC_DATA = abaqusConstants.VOLUMETRIC_DATA
VOLUME_COMPRESSION = abaqusConstants.VOLUME_COMPRESSION
VOLUME_FLUX = abaqusConstants.VOLUME_FLUX
VOLUME_FLUX_AREA = abaqusConstants.VOLUME_FLUX_AREA
VOLUME_FRACTION = abaqusConstants.VOLUME_FRACTION
VOLUME_PROPORTIONAL = abaqusConstants.VOLUME_PROPORTIONAL
VOL_FLUX = abaqusConstants.VOL_FLUX
VOL_RATE_LEAK = abaqusConstants.VOL_RATE_LEAK
VRML = abaqusConstants.VRML
WARNING = abaqusConstants.WARNING
WARP2D3 = abaqusConstants.WARP2D3
WARP2D4 = abaqusConstants.WARP2D4
WEDGE = abaqusConstants.WEDGE
WEDGE15 = abaqusConstants.WEDGE15
WEDGE6 = abaqusConstants.WEDGE6
WEIGHTED = abaqusConstants.WEIGHTED
WEIGHTED_ADD = abaqusConstants.WEIGHTED_ADD
WELD = abaqusConstants.WELD
WHITE_TO_BLACK = abaqusConstants.WHITE_TO_BLACK
WHOLE_ELEMENT = abaqusConstants.WHOLE_ELEMENT
WHOLE_MODEL = abaqusConstants.WHOLE_MODEL
WHOLE_PART_INSTANCE = abaqusConstants.WHOLE_PART_INSTANCE
WHOLE_REGION = abaqusConstants.WHOLE_REGION
WHOLE_SURFACE = abaqusConstants.WHOLE_SURFACE
WIDTH = abaqusConstants.WIDTH
WINDOWS = abaqusConstants.WINDOWS
WIRE = abaqusConstants.WIRE
WIREFRAME = abaqusConstants.WIREFRAME
WLF = abaqusConstants.WLF
WRAP_AROUND = abaqusConstants.WRAP_AROUND
X11 = abaqusConstants.X11
XASYMM = abaqusConstants.XASYMM
XAXIS = abaqusConstants.XAXIS
XMARKER = abaqusConstants.XMARKER
XOR = abaqusConstants.XOR
XSYMM = abaqusConstants.XSYMM
XYPLANE = abaqusConstants.XYPLANE
XYZ = abaqusConstants.XYZ
XZPLANE = abaqusConstants.XZPLANE
YASYMM = abaqusConstants.YASYMM
YAXIS = abaqusConstants.YAXIS
YEOH = abaqusConstants.YEOH
YES = abaqusConstants.YES
YIELD_RATIO = abaqusConstants.YIELD_RATIO
YSYMM = abaqusConstants.YSYMM
YZPLANE = abaqusConstants.YZPLANE
ZASYMM = abaqusConstants.ZASYMM
ZAXIS = abaqusConstants.ZAXIS
ZERO = abaqusConstants.ZERO
ZERO_PRESSURE = abaqusConstants.ZERO_PRESSURE
ZSYMM = abaqusConstants.ZSYMM
X_COORDINATE = abaqusConstants.X_COORDINATE
Y_COORDINATE = abaqusConstants.Y_COORDINATE
Z_COORDINATE = abaqusConstants.Z_COORDINATE
AVERAGED_AT_NODES = abaqusConstants.AVERAGED_AT_NODES
CENTROIDAL = abaqusConstants.CENTROIDAL
K110 = abaqusConstants.K110
UNARY_NEGATIVE = abaqusConstants.UNARY_NEGATIVE
HYPERBOLIC_COSINE = abaqusConstants.HYPERBOLIC_COSINE
INVERSE_COSINE = abaqusConstants.INVERSE_COSINE
INVERSE_SINE = abaqusConstants.INVERSE_SINE
HYPERBOLIC_TANGENT = abaqusConstants.HYPERBOLIC_TANGENT
INVERSE_TANGENT = abaqusConstants.INVERSE_TANGENT
NORMALIZE = abaqusConstants.NORMALIZE
DEG2RAD = abaqusConstants.DEG2RAD
RAD2DEG = abaqusConstants.RAD2DEG
SMOOTH = abaqusConstants.SMOOTH
SWAP = abaqusConstants.SWAP
AVERAGE_ALL = abaqusConstants.AVERAGE_ALL
MAXIMUM_ENVELOPE = abaqusConstants.MAXIMUM_ENVELOPE
MINIMUM_ENVELOPE = abaqusConstants.MINIMUM_ENVELOPE
RANGE_ALL = abaqusConstants.RANGE_ALL
SS = abaqusConstants.SS
TOKEN = abaqusConstants.TOKEN
CREDIT = abaqusConstants.CREDIT
REUSS = abaqusConstants.REUSS
VOIGT = abaqusConstants.VOIGT
INVERSED_MT = abaqusConstants.INVERSED_MT
EISO = abaqusConstants.EISO
PISO = abaqusConstants.PISO
IGES = abaqusConstants.IGES
ANALYTICAL_FIELD_THICKNESS = abaqusConstants.ANALYTICAL_FIELD_THICKNESS
NORMAL_DATUM = abaqusConstants.NORMAL_DATUM
PRIMARY_DATUM = abaqusConstants.PRIMARY_DATUM
COMPLEX_MAG_AT_ANGLE = abaqusConstants.COMPLEX_MAG_AT_ANGLE
VALANIS_LANDEL = abaqusConstants.VALANIS_LANDEL
ELLIPTIC_CYLINDER = abaqusConstants.ELLIPTIC_CYLINDER
OBLATE = abaqusConstants.OBLATE
PENNY = abaqusConstants.PENNY
ORIENTATION_TENSOR = abaqusConstants.ORIENTATION_TENSOR
RANDOM3D = abaqusConstants.RANDOM3D
UMAT = abaqusConstants.UMAT
BRITTLE = abaqusConstants.BRITTLE
DUCTILE = abaqusConstants.DUCTILE
NT11 = abaqusConstants.NT11
FLUID_PRESSURE = abaqusConstants.FLUID_PRESSURE
WARP = abaqusConstants.WARP
ELECTRICAL_POTENTIAL = abaqusConstants.ELECTRICAL_POTENTIAL
NN30 = abaqusConstants.NN30
NN11 = abaqusConstants.NN11
NT30 = abaqusConstants.NT30
STRING = abaqusConstants.STRING
ELECTROMAGNETIC = abaqusConstants.ELECTROMAGNETIC
JUSTIFY_CENTER = abaqusConstants.JUSTIFY_CENTER
JUSTIFY_RIGHT = abaqusConstants.JUSTIFY_RIGHT
TWO_SIDED = abaqusConstants.TWO_SIDED
SMALL_SLIDING = abaqusConstants.SMALL_SLIDING
NO_CRUSH = abaqusConstants.NO_CRUSH
NO_TRIGGER = abaqusConstants.NO_TRIGGER
LOCATION = abaqusConstants.LOCATION
DEPENDENT = abaqusConstants.DEPENDENT
MAIN = abaqusConstants.MAIN
SECONDARY = abaqusConstants.SECONDARY
ELEMENT_ORDER_SMOOTHING = abaqusConstants.ELEMENT_ORDER_SMOOTHING
LINEAR_SMOOTHING = abaqusConstants.LINEAR_SMOOTHING
QUADRATIC_SMOOTHING = abaqusConstants.QUADRATIC_SMOOTHING
NO_VERTICES = abaqusConstants.NO_VERTICES
ALL_VERTICES = abaqusConstants.ALL_VERTICES
SIMULATION_SUBMITTED = abaqusConstants.SIMULATION_SUBMITTED
HEALER_JOB = abaqusConstants.HEALER_JOB
COMPLEX_ENVELOPE_MAX_ABS = abaqusConstants.COMPLEX_ENVELOPE_MAX_ABS
COMPLEX_ENVELOPE_MIN = abaqusConstants.COMPLEX_ENVELOPE_MIN
COMPLEX_ENVELOPE_MAX = abaqusConstants.COMPLEX_ENVELOPE_MAX
TRANSFORM = abaqusConstants.TRANSFORM
WIRE_FRAME = abaqusConstants.WIRE_FRAME
FIELD_ANALYTICAL = abaqusConstants.FIELD_ANALYTICAL
EXTRA = abaqusConstants.EXTRA
API = abaqusConstants.API
ALLOW = abaqusConstants.ALLOW
BYPASS = abaqusConstants.BYPASS
FACET = abaqusConstants.FACET
S11 = abaqusConstants.S11
STEEL = abaqusConstants.STEEL
S22 = abaqusConstants.S22
# okay decompiling abaqusConstants.pyc

CODE = Literal[
    abaqusConstants.AC1D2,
    abaqusConstants.AC1D3,
    abaqusConstants.AC2D3,
    abaqusConstants.AC2D4,
    abaqusConstants.AC2D6,
    abaqusConstants.AC2D8,
    abaqusConstants.AC3D4,
    abaqusConstants.AC3D6,
    abaqusConstants.AC3D8,
    abaqusConstants.AC3D10,
    abaqusConstants.AC3D15,
    abaqusConstants.AC3D20,
    abaqusConstants.ACAX3,
    abaqusConstants.ACAX4,
    abaqusConstants.ACAX6,
    abaqusConstants.ACAX8,
    abaqusConstants.ACIN2D2,
    abaqusConstants.ACIN2D3,
    abaqusConstants.ACIN3D3,
    abaqusConstants.ACIN3D4,
    abaqusConstants.ACIN3D6,
    abaqusConstants.ACIN3D8,
    abaqusConstants.ACINAX2,
    abaqusConstants.ACINAX3,
    abaqusConstants.ASI2D2,
    abaqusConstants.ASI2D3,
    abaqusConstants.ASI3D3,
    abaqusConstants.ASI3D4,
    abaqusConstants.ASI3D6,
    abaqusConstants.ASI3D8,
    abaqusConstants.ASIAX2,
    abaqusConstants.ASIAX3,
    abaqusConstants.B21,
    abaqusConstants.B21H,
    abaqusConstants.B22,
    abaqusConstants.B22H,
    abaqusConstants.B23,
    abaqusConstants.B23H,
    abaqusConstants.B31,
    abaqusConstants.B31H,
    abaqusConstants.B31OS,
    abaqusConstants.B31OSH,
    abaqusConstants.B32,
    abaqusConstants.B32H,
    abaqusConstants.B32OS,
    abaqusConstants.B32OSH,
    abaqusConstants.B33,
    abaqusConstants.B33H,
    abaqusConstants.C3D4,
    abaqusConstants.C3D4E,
    abaqusConstants.C3D4H,
    abaqusConstants.C3D4P,
    abaqusConstants.C3D4T,
    abaqusConstants.C3D6,
    abaqusConstants.C3D6E,
    abaqusConstants.C3D6H,
    abaqusConstants.C3D6P,
    abaqusConstants.C3D6T,
    abaqusConstants.C3D8,
    abaqusConstants.C3D8E,
    abaqusConstants.C3D8H,
    abaqusConstants.C3D8HT,
    abaqusConstants.C3D8I,
    abaqusConstants.C3D8IH,
    abaqusConstants.C3D8P,
    abaqusConstants.C3D8PH,
    abaqusConstants.C3D8PHT,
    abaqusConstants.C3D8PT,
    abaqusConstants.C3D8R,
    abaqusConstants.C3D8RH,
    abaqusConstants.C3D8RHT,
    abaqusConstants.C3D8RP,
    abaqusConstants.C3D8RPH,
    abaqusConstants.C3D8RPHT,
    abaqusConstants.C3D8RPT,
    abaqusConstants.C3D8RT,
    abaqusConstants.C3D8T,
    abaqusConstants.C3D10,
    abaqusConstants.C3D10E,
    abaqusConstants.C3D10H,
    abaqusConstants.C3D10M,
    abaqusConstants.C3D10MH,
    abaqusConstants.C3D10MHT,
    abaqusConstants.C3D10MP,
    abaqusConstants.C3D10MPH,
    abaqusConstants.C3D10MPT,
    abaqusConstants.C3D10MT,
    abaqusConstants.C3D15,
    abaqusConstants.C3D15E,
    abaqusConstants.C3D15H,
    abaqusConstants.C3D20,
    abaqusConstants.C3D20E,
    abaqusConstants.C3D20H,
    abaqusConstants.C3D20HT,
    abaqusConstants.C3D20P,
    abaqusConstants.C3D20PH,
    abaqusConstants.C3D20R,
    abaqusConstants.C3D20RE,
    abaqusConstants.C3D20RH,
    abaqusConstants.C3D20RHT,
    abaqusConstants.C3D20RP,
    abaqusConstants.C3D20RPH,
    abaqusConstants.C3D20RT,
    abaqusConstants.C3D20T,
    abaqusConstants.CAX3,
    abaqusConstants.CAX3E,
    abaqusConstants.CAX3H,
    abaqusConstants.CAX3T,
    abaqusConstants.CAX4,
    abaqusConstants.CAX4E,
    abaqusConstants.CAX4H,
    abaqusConstants.CAX4HT,
    abaqusConstants.CAX4I,
    abaqusConstants.CAX4IH,
    abaqusConstants.CAX4P,
    abaqusConstants.CAX4PH,
    abaqusConstants.CAX4R,
    abaqusConstants.CAX4RH,
    abaqusConstants.CAX4RHT,
    abaqusConstants.CAX4RP,
    abaqusConstants.CAX4RPH,
    abaqusConstants.CAX4RT,
    abaqusConstants.CAX4T,
    abaqusConstants.CAX6,
    abaqusConstants.CAX6E,
    abaqusConstants.CAX6H,
    abaqusConstants.CAX6M,
    abaqusConstants.CAX6MH,
    abaqusConstants.CAX6MHT,
    abaqusConstants.CAX6MP,
    abaqusConstants.CAX6MPH,
    abaqusConstants.CAX6MT,
    abaqusConstants.CAX8,
    abaqusConstants.CAX8E,
    abaqusConstants.CAX8H,
    abaqusConstants.CAX8HT,
    abaqusConstants.CAX8P,
    abaqusConstants.CAX8PH,
    abaqusConstants.CAX8R,
    abaqusConstants.CAX8RE,
    abaqusConstants.CAX8RH,
    abaqusConstants.CAX8RHT,
    abaqusConstants.CAX8RP,
    abaqusConstants.CAX8RPH,
    abaqusConstants.CAX8RT,
    abaqusConstants.CAX8T,
    abaqusConstants.CCL9,
    abaqusConstants.CCL9H,
    abaqusConstants.CCL12,
    abaqusConstants.CCL12H,
    abaqusConstants.CCL18,
    abaqusConstants.CCL18H,
    abaqusConstants.CCL24,
    abaqusConstants.CCL24H,
    abaqusConstants.CCL24R,
    abaqusConstants.CCL24RH,
    abaqusConstants.CGAX3,
    abaqusConstants.CGAX3H,
    abaqusConstants.CGAX3HT,
    abaqusConstants.CGAX3T,
    abaqusConstants.CGAX4,
    abaqusConstants.CGAX4H,
    abaqusConstants.CGAX4HT,
    abaqusConstants.CGAX4R,
    abaqusConstants.CGAX4RH,
    abaqusConstants.CGAX4RHT,
    abaqusConstants.CGAX4RT,
    abaqusConstants.CGAX4T,
    abaqusConstants.CGAX6,
    abaqusConstants.CGAX6H,
    abaqusConstants.CGAX6M,
    abaqusConstants.CGAX6MH,
    abaqusConstants.CGAX6MHT,
    abaqusConstants.CGAX6MT,
    abaqusConstants.CGAX8,
    abaqusConstants.CGAX8H,
    abaqusConstants.CGAX8HT,
    abaqusConstants.CGAX8R,
    abaqusConstants.CGAX8RH,
    abaqusConstants.CGAX8RHT,
    abaqusConstants.CGAX8RT,
    abaqusConstants.CGAX8T,
    abaqusConstants.CINAX4,
    abaqusConstants.CINAX5R,
    abaqusConstants.CINPE4,
    abaqusConstants.CINPE5R,
    abaqusConstants.CINPS4,
    abaqusConstants.CINPS5R,
    abaqusConstants.COH2D4,
    abaqusConstants.COH2D4P,
    abaqusConstants.COH3D6,
    abaqusConstants.COH3D6P,
    abaqusConstants.COH3D8,
    abaqusConstants.COH3D8P,
    abaqusConstants.COHAX4,
    abaqusConstants.COHAX4P,
    abaqusConstants.CONN2D2,
    abaqusConstants.CONN3D2,
    abaqusConstants.CPE3,
    abaqusConstants.CPE3E,
    abaqusConstants.CPE3H,
    abaqusConstants.CPE3T,
    abaqusConstants.CPE4,
    abaqusConstants.CPE4E,
    abaqusConstants.CPE4H,
    abaqusConstants.CPE4HT,
    abaqusConstants.CPE4I,
    abaqusConstants.CPE4IH,
    abaqusConstants.CPE4P,
    abaqusConstants.CPE4PH,
    abaqusConstants.CPE4R,
    abaqusConstants.CPE4RH,
    abaqusConstants.CPE4RHT,
    abaqusConstants.CPE4RP,
    abaqusConstants.CPE4RPH,
    abaqusConstants.CPE4RT,
    abaqusConstants.CPE4T,
    abaqusConstants.CPE6,
    abaqusConstants.CPE6E,
    abaqusConstants.CPE6H,
    abaqusConstants.CPE6M,
    abaqusConstants.CPE6MH,
    abaqusConstants.CPE6MHT,
    abaqusConstants.CPE6MP,
    abaqusConstants.CPE6MPH,
    abaqusConstants.CPE6MT,
    abaqusConstants.CPE8,
    abaqusConstants.CPE8E,
    abaqusConstants.CPE8H,
    abaqusConstants.CPE8HT,
    abaqusConstants.CPE8P,
    abaqusConstants.CPE8PH,
    abaqusConstants.CPE8R,
    abaqusConstants.CPE8RE,
    abaqusConstants.CPE8RH,
    abaqusConstants.CPE8RHT,
    abaqusConstants.CPE8RP,
    abaqusConstants.CPE8RPH,
    abaqusConstants.CPE8RT,
    abaqusConstants.CPE8T,
    abaqusConstants.CPEG3,
    abaqusConstants.CPEG3H,
    abaqusConstants.CPEG3HT,
    abaqusConstants.CPEG3T,
    abaqusConstants.CPEG4,
    abaqusConstants.CPEG4H,
    abaqusConstants.CPEG4HT,
    abaqusConstants.CPEG4I,
    abaqusConstants.CPEG4IH,
    abaqusConstants.CPEG4R,
    abaqusConstants.CPEG4RH,
    abaqusConstants.CPEG4RHT,
    abaqusConstants.CPEG4RT,
    abaqusConstants.CPEG4T,
    abaqusConstants.CPEG6,
    abaqusConstants.CPEG6H,
    abaqusConstants.CPEG6M,
    abaqusConstants.CPEG6MH,
    abaqusConstants.CPEG6MHT,
    abaqusConstants.CPEG6MT,
    abaqusConstants.CPEG8,
    abaqusConstants.CPEG8H,
    abaqusConstants.CPEG8HT,
    abaqusConstants.CPEG8R,
    abaqusConstants.CPEG8RH,
    abaqusConstants.CPEG8RHT,
    abaqusConstants.CPEG8T,
    abaqusConstants.CPS3,
    abaqusConstants.CPS3E,
    abaqusConstants.CPS3T,
    abaqusConstants.CPS4,
    abaqusConstants.CPS4E,
    abaqusConstants.CPS4I,
    abaqusConstants.CPS4R,
    abaqusConstants.CPS4RT,
    abaqusConstants.CPS4T,
    abaqusConstants.CPS6,
    abaqusConstants.CPS6E,
    abaqusConstants.CPS6M,
    abaqusConstants.CPS6MT,
    abaqusConstants.CPS8,
    abaqusConstants.CPS8E,
    abaqusConstants.CPS8R,
    abaqusConstants.CPS8RE,
    abaqusConstants.CPS8RT,
    abaqusConstants.CPS8T,
    abaqusConstants.DASHPOT1,
    abaqusConstants.DASHPOT2,
    abaqusConstants.DASHPOTA,
    abaqusConstants.DC1D2,
    abaqusConstants.DC1D2E,
    abaqusConstants.DC1D3,
    abaqusConstants.DC1D3E,
    abaqusConstants.DC2D3,
    abaqusConstants.DC2D3E,
    abaqusConstants.DC2D4,
    abaqusConstants.DC2D4E,
    abaqusConstants.DC2D6,
    abaqusConstants.DC2D6E,
    abaqusConstants.DC2D8,
    abaqusConstants.DC2D8E,
    abaqusConstants.DC3D4,
    abaqusConstants.DC3D4E,
    abaqusConstants.DC3D6,
    abaqusConstants.DC3D6E,
    abaqusConstants.DC3D8,
    abaqusConstants.DC3D8E,
    abaqusConstants.DC3D10,
    abaqusConstants.DC3D10E,
    abaqusConstants.DC3D15,
    abaqusConstants.DC3D15E,
    abaqusConstants.DC3D20,
    abaqusConstants.DC3D20E,
    abaqusConstants.DCAX3,
    abaqusConstants.DCAX3E,
    abaqusConstants.DCAX4,
    abaqusConstants.DCAX4E,
    abaqusConstants.DCAX6,
    abaqusConstants.DCAX6E,
    abaqusConstants.DCAX8,
    abaqusConstants.DCAX8E,
    abaqusConstants.DCC1D2,
    abaqusConstants.DCC1D2D,
    abaqusConstants.DCC2D4,
    abaqusConstants.DCC2D4D,
    abaqusConstants.DCC3D8,
    abaqusConstants.DCC3D8D,
    abaqusConstants.DCCAX2,
    abaqusConstants.DCCAX2D,
    abaqusConstants.DCCAX4,
    abaqusConstants.DCCAX4D,
    abaqusConstants.DCOUP2D,
    abaqusConstants.DCOUP3D,
    abaqusConstants.DGAP,
    abaqusConstants.DRAG2D,
    abaqusConstants.DRAG3D,
    abaqusConstants.DS3,
    abaqusConstants.DS4,
    abaqusConstants.DS6,
    abaqusConstants.DS8,
    abaqusConstants.DSAX1,
    abaqusConstants.DSAX2,
    abaqusConstants.ELBOW31,
    abaqusConstants.ELBOW31B,
    abaqusConstants.ELBOW31C,
    abaqusConstants.ELBOW32,
    abaqusConstants.EMC2D3,
    abaqusConstants.EMC2D4,
    abaqusConstants.EMC3D4,
    abaqusConstants.EMC3D6,
    abaqusConstants.EMC3D8,
    abaqusConstants.FRAME2D,
    abaqusConstants.FRAME3D,
    abaqusConstants.GAPCYL,
    abaqusConstants.GAPSPHER,
    abaqusConstants.GAPUNI,
    abaqusConstants.GAPUNIT,
    abaqusConstants.GK2D2,
    abaqusConstants.GK2D2N,
    abaqusConstants.GK3D2,
    abaqusConstants.GK3D2N,
    abaqusConstants.GK3D4L,
    abaqusConstants.GK3D4LN,
    abaqusConstants.GK3D6L,
    abaqusConstants.GK3D6LN,
    abaqusConstants.GK3D6,
    abaqusConstants.GK3D6N,
    abaqusConstants.GK3D8,
    abaqusConstants.GK3D8N,
    abaqusConstants.GK3D12M,
    abaqusConstants.GK3D12MN,
    abaqusConstants.GK3D18,
    abaqusConstants.GK3D18N,
    abaqusConstants.GKAX2,
    abaqusConstants.GKAX2N,
    abaqusConstants.GKAX4,
    abaqusConstants.GKAX4N,
    abaqusConstants.GKAX6,
    abaqusConstants.GKAX6N,
    abaqusConstants.GKPE4,
    abaqusConstants.GKPE6,
    abaqusConstants.GKPS4,
    abaqusConstants.GKPS4N,
    abaqusConstants.GKPS6,
    abaqusConstants.GKPS6N,
    abaqusConstants.HEATCAP,
    abaqusConstants.ISL21A,
    abaqusConstants.ISL22A,
    abaqusConstants.ITSCYL,
    abaqusConstants.ITSUNI,
    abaqusConstants.ITT21,
    abaqusConstants.ITT31,
    abaqusConstants.JOINT2D,
    abaqusConstants.JOINT3D,
    abaqusConstants.JOINTC,
    abaqusConstants.LS3S,
    abaqusConstants.LS6,
    abaqusConstants.M3D3,
    abaqusConstants.M3D4,
    abaqusConstants.M3D4R,
    abaqusConstants.M3D6,
    abaqusConstants.M3D8,
    abaqusConstants.M3D8R,
    abaqusConstants.MASS,
    abaqusConstants.MAX1,
    abaqusConstants.MAX2,
    abaqusConstants.MCL6,
    abaqusConstants.MCL9,
    abaqusConstants.MGAX1,
    abaqusConstants.MGAX2,
    abaqusConstants.PIPE21,
    abaqusConstants.PIPE21H,
    abaqusConstants.PIPE22,
    abaqusConstants.PIPE22H,
    abaqusConstants.PIPE31,
    abaqusConstants.PIPE31H,
    abaqusConstants.PIPE32,
    abaqusConstants.PIPE32H,
    abaqusConstants.PSI24,
    abaqusConstants.PSI26,
    abaqusConstants.PSI34,
    abaqusConstants.PSI36,
    abaqusConstants.Q3D4,
    abaqusConstants.Q3D6,
    abaqusConstants.Q3D8,
    abaqusConstants.Q3D8H,
    abaqusConstants.Q3D8R,
    abaqusConstants.Q3D8RH,
    abaqusConstants.Q3D10M,
    abaqusConstants.Q3D10MH,
    abaqusConstants.Q3D20,
    abaqusConstants.Q3D20H,
    abaqusConstants.Q3D20R,
    abaqusConstants.Q3D20RH,
    abaqusConstants.R2D2,
    abaqusConstants.R3D3,
    abaqusConstants.R3D4,
    abaqusConstants.RAX2,
    abaqusConstants.RB2D2,
    abaqusConstants.RB3D2,
    abaqusConstants.ROTARYI,
    abaqusConstants.S3,
    abaqusConstants.S3T,
    abaqusConstants.S3R,
    abaqusConstants.S3RT,
    abaqusConstants.S4,
    abaqusConstants.S4T,
    abaqusConstants.S4R,
    abaqusConstants.S4RT,
    abaqusConstants.S4R5,
    abaqusConstants.S8R,
    abaqusConstants.S8R5,
    abaqusConstants.S8RT,
    abaqusConstants.SAX1,
    abaqusConstants.SAX2,
    abaqusConstants.SAX2T,
    abaqusConstants.SC6R,
    abaqusConstants.SC8R,
    abaqusConstants.SC6RT,
    abaqusConstants.SC8RT,
    abaqusConstants.SFM3D3,
    abaqusConstants.SFM3D4,
    abaqusConstants.SFM3D4R,
    abaqusConstants.SFM3D6,
    abaqusConstants.SFM3D8,
    abaqusConstants.SFM3D8R,
    abaqusConstants.SFMAX1,
    abaqusConstants.SFMAX2,
    abaqusConstants.SFMCL6,
    abaqusConstants.SFMCL9,
    abaqusConstants.SFMGAX1,
    abaqusConstants.SFMGAX2,
    abaqusConstants.SPRING1,
    abaqusConstants.SPRING2,
    abaqusConstants.SPRINGA,
    abaqusConstants.STRI3,
    abaqusConstants.STRI65,
    abaqusConstants.T2D2,
    abaqusConstants.T2D2E,
    abaqusConstants.T2D2H,
    abaqusConstants.T2D2T,
    abaqusConstants.T2D3,
    abaqusConstants.T2D3E,
    abaqusConstants.T2D3H,
    abaqusConstants.T2D3T,
    abaqusConstants.T3D2,
    abaqusConstants.T3D2E,
    abaqusConstants.T3D2H,
    abaqusConstants.T3D2T,
    abaqusConstants.T3D3,
    abaqusConstants.T3D3E,
    abaqusConstants.T3D3H,
    abaqusConstants.T3D3T,
    abaqusConstants.WARP2D3,
    abaqusConstants.WARP2D4,
    abaqusConstants.AC2D3,
    abaqusConstants.AC2D4R,
    abaqusConstants.AC3D4,
    abaqusConstants.AC3D6,
    abaqusConstants.AC3D8R,
    abaqusConstants.ACAX3,
    abaqusConstants.ACAX4R,
    abaqusConstants.ACIN2D2,
    abaqusConstants.ACIN3D3,
    abaqusConstants.ACIN3D4,
    abaqusConstants.ACINAX2,
    abaqusConstants.B21,
    abaqusConstants.B22,
    abaqusConstants.B31,
    abaqusConstants.B32,
    abaqusConstants.C3D4,
    abaqusConstants.C3D4H,
    abaqusConstants.C3D4T,
    abaqusConstants.C3D6,
    abaqusConstants.C3D6T,
    abaqusConstants.C3D8,
    abaqusConstants.C3D8I,
    abaqusConstants.C3D8R,
    abaqusConstants.C3D8T,
    abaqusConstants.C3D8RT,
    abaqusConstants.C3D10,
    abaqusConstants.C3D10M,
    abaqusConstants.C3D10MT,
    abaqusConstants.CAX3,
    abaqusConstants.CAX3T,
    abaqusConstants.CAX4R,
    abaqusConstants.CAX4RT,
    abaqusConstants.CAX6M,
    abaqusConstants.CAX6MT,
    abaqusConstants.CINAX4,
    abaqusConstants.CINPE4,
    abaqusConstants.CINPS4,
    abaqusConstants.COHAX4,
    abaqusConstants.COH2D4,
    abaqusConstants.COH3D6,
    abaqusConstants.COH3D8,
    abaqusConstants.CONN2D2,
    abaqusConstants.CONN3D2,
    abaqusConstants.CPE3,
    abaqusConstants.CPE3T,
    abaqusConstants.CPE4R,
    abaqusConstants.CPE4RT,
    abaqusConstants.CPE6M,
    abaqusConstants.CPE6MT,
    abaqusConstants.CPS3,
    abaqusConstants.CPS3T,
    abaqusConstants.CPS4R,
    abaqusConstants.CPS4RT,
    abaqusConstants.CPS6M,
    abaqusConstants.CPS6MT,
    abaqusConstants.DASHPOTA,
    abaqusConstants.EC3D8R,
    abaqusConstants.EC3D8RT,
    abaqusConstants.HEATCAP,
    abaqusConstants.M3D3,
    abaqusConstants.M3D4,
    abaqusConstants.M3D4R,
    abaqusConstants.MASS,
    abaqusConstants.PIPE21,
    abaqusConstants.PIPE31,
    abaqusConstants.R2D2,
    abaqusConstants.R3D3,
    abaqusConstants.R3D4,
    abaqusConstants.RAX2,
    abaqusConstants.ROTARYI,
    abaqusConstants.S3R,
    abaqusConstants.S3RS,
    abaqusConstants.S3RT,
    abaqusConstants.S4,
    abaqusConstants.S4R,
    abaqusConstants.S4RS,
    abaqusConstants.S4RSW,
    abaqusConstants.S4RT,
    abaqusConstants.SAX1,
    abaqusConstants.SC6R,
    abaqusConstants.SC8R,
    abaqusConstants.SC6RT,
    abaqusConstants.SC8RT,
    abaqusConstants.SFM3D3,
    abaqusConstants.SFM3D4R,
    abaqusConstants.SPRINGA,
    abaqusConstants.T2D2,
    abaqusConstants.T3D2,
]

end_all()
