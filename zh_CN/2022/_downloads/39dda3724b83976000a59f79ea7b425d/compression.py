"""
Compression Model
=================

A simple example to establish a compression model.

.. figure:: /images/model.png
    :width: 50%
    :align: center

    A simple compression model.
"""

from abaqus import *
from abaqusConstants import *
from caeModules import *
from driverUtils import *

executeOnCaeStartup()

# Model
model = mdb.models["Model-1"]

# Part
sketch = model.ConstrainedSketch(name="sketch", sheetSize=1.0)
sketch.rectangle((0, 0), (1, 1))
part = model.Part(name="part", dimensionality=THREE_D, type=DEFORMABLE_BODY)
part.BaseSolidExtrude(sketch=sketch, depth=1)

# Create sets
part.Set(name="set-all", cells=part.cells.findAt(coordinates=((0.5, 0.5, 0.5),)))
part.Set(name="set-bottom", faces=part.faces.findAt(coordinates=((0.5, 0.5, 0.0),)))
part.Set(name="set-top", faces=part.faces.findAt(coordinates=((0.5, 0.5, 1.0),)))
part.Surface(name="surface-top", side1Faces=part.faces.findAt(coordinates=((0.5, 0.5, 1.0),)))

# Assembly
model.rootAssembly.DatumCsysByDefault(CARTESIAN)
model.rootAssembly.Instance(name="instance", part=part, dependent=ON)

# Material
material = model.Material(name="material")
material.Elastic(table=((1000, 0.2),))
material.Density(table=((2500,),))

# Section
model.HomogeneousSolidSection(name="section", material="material", thickness=None)
part.SectionAssignment(region=part.sets["set-all"], sectionName="section")

# Step
step = model.StaticStep(
    name="Step-1",
    previous="Initial",
    description="",
    timePeriod=1.0,
    timeIncrementationMethod=AUTOMATIC,
    maxNumInc=100,
    initialInc=0.01,
    minInc=0.001,
    maxInc=0.1,
)

# Output request
field = model.FieldOutputRequest("F-Output-1", createStepName="Step-1", variables=("S", "E", "U"))

# Boundary condition
bottom_instance = model.rootAssembly.instances["instance"].sets["set-bottom"]
bc = model.DisplacementBC(
    name="BC-1", createStepName="Initial", region=bottom_instance, u1=SET, u2=SET, u3=SET, ur1=SET, ur2=SET, ur3=SET
)

# Load
top_instance = model.rootAssembly.instances["instance"].surfaces["surface-top"]
pressure = model.Pressure("pressure", createStepName="Step-1", region=top_instance, magnitude=100)

# Mesh
elem1 = mesh.ElemType(elemCode=C3D8R)
elem2 = mesh.ElemType(elemCode=C3D6)
elem3 = mesh.ElemType(elemCode=C3D4)
part.setElementType(regions=(part.cells,), elemTypes=(elem1, elem2, elem3))
part.seedPart(size=0.1)
part.generateMesh()

# Job
job = mdb.Job(name="Job-1", model="Model-1")
job.writeInput()

# Submit the job
job.submit()
job.waitForCompletion()

# Save abaqus model
mdb.saveAs("compression.cae")
