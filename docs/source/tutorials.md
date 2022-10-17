# Tutorials

```{note}
The abqpy is built in Python 3 but the Python interpreter of Abaqus is Python 2, so you must write codes that are compatible with Python 2 and Python 3.
```

For more examples, check [abqpy/examples at main · haiiliin/abqpy](https://github.com/haiiliin/abqpy/tree/main/examples).

Usually in Abaqus, we have several things to do:

- Build the model
- Submit and monitor the job
- Get the output data and visualize it

## Build an Abaqus model

The most convenient way to build an Abaqus model is to do it in Abaqus CAE. When we use the
Abaqus/CAE graphical user interface (GUI) to create a model and to visualize the results,
commands are issued internally by Abaqus/CAE after every operation. These commands reflect the
geometry you created along with the options and settings you selected from each dialog box.

Therefore, we can build our Abaqus model using Python script. We can totally use the Python
script to build our Abaqus model, although it is not an efficient way. Usually, we do
something in Abaqus/CAE, and check the Python script in the reply file (`.rpy`). And then copy
it to our script file, this works, but not nicely.

However, if type hints are provided in Python scripting of Abaqus, things will getting much
easier, and that is what `abqpy` does.

The example model described in the following is simple, there is a square structure, the vertical displacement of the bottom face is fixed, and there is a vertical pressure in the top surface, the Abaqus model is showed as follows:

```{image} images/model.png
:align: center
:width: 50%
```

### Header of the script

Usually, when we use Python script to build the model, we need to import the following modules:

```{eval-rst}
.. autolink-concat:: on
```

```Python
from abaqus import *
from abaqusConstants import *
from driverUtils import *
```

Module `abaqus` contains two most important variable `mdb` and `session` which control the model. Module `abaqusConstants` contains constant strings used in modelling, i.e., when we defines a part using the following code:

```{eval-rst}
.. autolink-concat:: on
```

```Python
mdb.models['Model-1'].Part(name='part', dimensionality=THREE_D, type=DEFORMABLE_BODY)
```

`THREE_D` indicates the part is a 3D part, `DEFORMABLE_BODY` indicates the part is deformable.

Module `driverUtils` contains an important function `executeOnCaeStartup`, this function will be execute each time we open the Abaqus, so we need to call this function in our Python script. Now, the header of our Python script would be like:

```{eval-rst}
.. autolink-concat:: on
```

```Python
from abaqus import *
from abaqusConstants import *
from driverUtils import *

executeOnCaeStartup()
```

### Create parts

First we need to create a sketch that will be used to create the part, we need to use {py:meth}`~abaqus.Sketcher.SketchModel.SketchModel.ConstrainedSketch` to create a sketch:

```{eval-rst}
.. autolink-concat:: on
```

```Python
model = mdb.models['Model-1']
sketch = model.ConstrainedSketch(name='sketch', sheetSize=1.0)
sketch.rectangle((0, 0), (1, 1))
```

In this code, we draw a sketch with a square. Now we can create a part using this sketch:

```{eval-rst}
.. autolink-concat:: on
```

```Python
part = model.Part(name='part', dimensionality=THREE_D, type=DEFORMABLE_BODY)
part.BaseSolidExtrude(sketch=sketch, depth=1)
```

The first line creates a 3D and deformable part. Then we use the {py:meth}`~abaqus.Part.PartFeature.PartFeature.BaseSolidExtrude` method to create a part using the sketch.

### Create some sets for boundary conditions and loads

Unlike building a model in Abaqus/CAE, we can just click the nodes/faces to create sets, when we use a Python script to build the model, we can use coordinates to find nodes/faces we need.

We can use {py:meth}`~abaqus.Region.RegionPart.RegionPart.Set` and {py:meth}`~abaqus.Region.RegionPart.RegionPart.Surface` to create sets and surfaces:

```{eval-rst}
.. autolink-concat:: on
```

```Python
part.Set(name='set-all', cells=part.cells.findAt(coordinates=((0.5, 0.5, 0.5), )))
part.Set(name='set-bottom', faces=part.faces.findAt(coordinates=((0.5, 0.5, 0.0), )))
part.Set(name='set-top', faces=part.faces.findAt(coordinates=((0.5, 0.5, 1.0), )))
part.Surface(name='surface-top',
             side1Faces=part.faces.findAt(coordinates=((0.5, 0.5, 1.0), )))
```

### Merge parts to assembly

We can use {py:meth}`~abaqus.Assembly.AssemblyBase.AssemblyBase.Instance` to create instances：

```{eval-rst}
.. autolink-concat:: on
```

```Python
model.rootAssembly.DatumCsysByDefault(CARTESIAN)
model.rootAssembly.Instance(name='instance', part=part, dependent=ON)
```

### Create materials and sections, and assign materials to sections

First we create a Material object using {py:meth}`~abaqus.Material.MaterialModel.MaterialModel.Material`:

```{eval-rst}
.. autolink-concat:: on
```

```Python
material = model.Material(name='material')
```

Then we assign some properties to the Material object, i.e., {py:meth}`~abaqus.Material.Material.Material.Elastic` and {py:meth}`~abaqus.Material.Material.Material.Density`:

```{eval-rst}
.. autolink-concat:: on
```

```Python
material.Elastic(table=((1000, 0.2), ))
material.Density(table=((2500, ), ))
```

Then we create a {py:meth}`~abaqus.Section.SectionModel.SectionModel.HomogeneousSolidSection` and assign the material to the section ({py:meth}`~abaqus.Property.PropertyPart.PropertyPart.SectionAssignment`):

```{eval-rst}
.. autolink-concat:: on
```

```Python
model.HomogeneousSolidSection(name='section', material='material', thickness=None)
part.SectionAssignment(region=part.sets['set-all'], sectionName='section')
```

### Create steps

It is easy to create a {py:meth}`~abaqus.Step.StepModel.StepModel.StaticStep`:

```{eval-rst}
.. autolink-concat:: on
```

```Python
step = model.StaticStep(name='Step-1', previous='Initial', description='',
                        timePeriod=1.0, timeIncrementationMethod=AUTOMATIC,
                        maxNumInc=100, initialInc=0.01, minInc=0.001, maxInc=0.1)
```

### Specify output requests

We can use the {py:meth}`~abaqus.StepOutput.OutputModel.OutputModel.FieldOutputRequest` and {py:meth}`~abaqus.StepOutput.OutputModel.OutputModel.HistoryOutputRequest` to specify field output and history output information.

```{eval-rst}
.. autolink-concat:: on
```

```Python
field = model.FieldOutputRequest('F-Output-1', createStepName='Step-1',
                                 variables=('S', 'E', 'U'))
```

### Create boundary conditions

We can use {py:meth}`~abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.DisplacementBC` to create a displacement boundary condition:

```{eval-rst}
.. autolink-concat:: on
```

```Python
bottom_instance = model.rootAssembly.instances['instance'].sets['set-bottom']
bc = model.DisplacementBC(name='BC-1', createStepName='Initial',
                          region=bottom_instance, u3=SET)
```

It should be noted that region of the boundary condition should be a region of the instances instead of parts, since sets created in parts are copied to the instance, we can use the sets in the parts that we defined before.

### Create loads

We can use {py:meth}`~abaqus.Load.LoadModel.LoadModel.Pressure` ro create a pressure:

```{eval-rst}
.. autolink-concat:: on
```

```Python
top_instance = model.rootAssembly.instances['instance'].surfaces['surface-top']
pressure = model.Pressure('pressure', createStepName='Step-1', region=top_instance,
                          magnitude=100)
```

### Mesh

To mesh the model, we have to set the {py:class}`~abaqus.Mesh.ElemType.ElemType`, which is defined in the `mesh` module, so we need to import `mesh` module:

```{eval-rst}
.. autolink-concat:: on
```

```Python
import mesh

elem1 = mesh.ElemType(elemCode=C3D8R)
elem2 = mesh.ElemType(elemCode=C3D6)
elem3 = mesh.ElemType(elemCode=C3D4)
part.setElementType(regions=(part.cells, ), elemTypes=(elem1, elem2, elem3))
part.seedPart(size=0.1)
part.generateMesh()
```

### Create jobs

We can use {py:meth}`~abaqus.Job.JobMdb.JobMdb.Job` to create a job:

```{eval-rst}
.. autolink-concat:: on
```

```Python
job = mdb.Job(name='Job-1', model='Model-1')
```

Then we can write the model to an input file (`.inp`):

```{eval-rst}
.. autolink-concat:: on
```

```Python
job.writeInput()
```

Then we can submit the job:

```{eval-rst}
.. autolink-concat:: on
```

```Python
job.submit()
job.waitForCompletion()
```

### Save the Abaqus model to a `.cae` file

We can use {py:class}`~abaqus.Mdb.MdbBase.MdbBase.saveAs` to save the Abaqus model to a `.cae` file:

```{eval-rst}
.. autolink-concat:: on
```

```Python
mdb.saveAs('compression.cae')
```

### How the model is submitted to Abaqus?

It should be noted that when we execute all the above codes, the Python script have to not be sent to the Python interpreter. Instead, we have to call the Abaqus kernel, using the command like this:

```{eval-rst}
.. autolink-concat:: on
```

```sh
abaqus cae noGUI=script.py
```

In order to make it simple, this has been done inside the {py:mod}`~abaqus` module, in the {py:meth}`~abqpy.abaqus.run` function:

```{eval-rst}
.. autolink-concat:: on
```

```Python
def run():
    abaqus = 'abaqus'
    if 'ABAQUS_BAT_PATH' in os.environ.keys():
        abaqus = os.environ['ABAQUS_BAT_PATH']

    filePath = os.path.abspath(__main__.__file__)
    args = " ".join(sys.argv[1:])

    os.system(f"{abaqus} cae noGUI={filePath} -- {args}")

    sys.exit(0)
```

This function is called when we import the {py:mod}`~abaqus` module, with the line `from abaqus import *`. So, we have to import the {py:mod}`~abaqus` module to submit the model when we use `abqpy` to build an Abaqus model. All the functions mentioned above are included in `abqpy`, however, nothing has been done inside this functions, they are just provided for type hints.

### The whole script

The whole script of this example is showed as follows:

```{eval-rst}
.. autolink-concat:: on
```

```{code-block} Python
:caption: compression.py

from abaqus import *
from abaqusConstants import *
from caeModules import *
from driverUtils import *

executeOnCaeStartup()

# Model
model = mdb.models['Model-1']

# Part
sketch = model.ConstrainedSketch(name='sketch', sheetSize=1.0)
sketch.rectangle((0, 0), (1, 1))
part = model.Part(name='part', dimensionality=THREE_D, type=DEFORMABLE_BODY)
part.BaseSolidExtrude(sketch=sketch, depth=1)

# Create sets
part.Set(name='set-all', cells=part.cells.findAt(coordinates=((0.5, 0.5, 0.5), )))
part.Set(name='set-bottom', faces=part.faces.findAt(coordinates=((0.5, 0.5, 0.0), )))
part.Set(name='set-top', faces=part.faces.findAt(coordinates=((0.5, 0.5, 1.0), )))
part.Surface(name='surface-top',
             side1Faces=part.faces.findAt(coordinates=((0.5, 0.5, 1.0), )))

# Assembly
model.rootAssembly.DatumCsysByDefault(CARTESIAN)
model.rootAssembly.Instance(name='instance', part=part, dependent=ON)

# Material
material = model.Material(name='material')
material.Elastic(table=((1000, 0.2), ))
material.Density(table=((2500, ), ))

# Section
model.HomogeneousSolidSection(name='section', material='material', thickness=None)
part.SectionAssignment(region=part.sets['set-all'], sectionName='section')

# Step
step = model.StaticStep(name='Step-1', previous='Initial', description='',
                        timePeriod=1.0, timeIncrementationMethod=AUTOMATIC,
                        maxNumInc=100, initialInc=0.01, minInc=0.001, maxInc=0.1)

# Output request
field = model.FieldOutputRequest('F-Output-1', createStepName='Step-1',
                                 variables=('S', 'E', 'U'))

# Boundary condition
bottom_instance = model.rootAssembly.instances['instance'].sets['set-bottom']
bc = model.DisplacementBC(name='BC-1', createStepName='Initial',
                          region=bottom_instance, u3=SET)

# Load
top_instance = model.rootAssembly.instances['instance'].surfaces['surface-top']
pressure = model.Pressure('pressure', createStepName='Step-1', region=top_instance,
                          magnitude=100)

# Mesh
elem1 = mesh.ElemType(elemCode=C3D8R)
elem2 = mesh.ElemType(elemCode=C3D6)
elem3 = mesh.ElemType(elemCode=C3D4)
part.setElementType(regions=(part.cells, ), elemTypes=(elem1, elem2, elem3))
part.seedPart(size=0.1)
part.generateMesh()

# Job
job = mdb.Job(name='Job-1', model='Model-1')
job.writeInput()

# Submit the job
# job.submit()
# job.waitForCompletion()

# Save abaqus model
mdb.saveAs('compression.cae')
```

## Extract output data

If we want to extract the output data, we have to write an output script.

### Header of the output script

Similarly, we have to import some modules:

```{eval-rst}
.. autolink-concat:: on
```

```Python
from abaqus import *
from abaqusConstants import *
from driverUtils import *

executeOnCaeStartup()
```

### Open the output database

We can use {py:meth}`~abaqus.Session.SessionBase.SessionBase.openOdb` to open the output database:

```{eval-rst}
.. autolink-concat:: on
```

```Python
import visualization
odb = session.openOdb('Job-1.odb')
session.viewports['Viewport: 1'].setValues(displayedObject=odb)
```

### Extract the data

We can use the {py:meth}`~abaqus.XY.XYSession.XYSession.xyDataListFromField` to extract the output data:

```{eval-rst}
.. autolink-concat:: on
```

```Python
dataList = session.xyDataListFromField(odb=odb, outputPosition=NODAL,
                                       variable=(('U', NODAL, ((COMPONENT, 'U3'),)),),
                                       nodeSets=('INSTANCE.SET-TOP', ))
```

`dataList` is a list of `XYData` objects. `XYData` is a data type defined in Abaqus, the data is stored in tuples of tuples, so we can simply save it to a file, i.e., using the `numpy` (`numpy` is installed in Python interpreter of Abaqus already):

```{eval-rst}
.. autolink-concat:: on
```

```Python
import numpy as np

data = np.array(dataList[0])
np.savetxt('data.csv', data, header='time,U3', delimiter=',', comments='')
```

### Results of above example

The distribution of `U3` of above model is showed as follows:

(output)=

```{image} /images/output.png
:align: center
:width: 70%
```

The distribution of the vertical displacement of a point in the top surface is showed as follows:

(compression)=

```{image} /images/compression.png
:align: center
:width: 70%
```

### The whole output script

The whole output script of this example is showed as follows:

```{eval-rst}
.. autolink-concat:: on
```

```{code-block} Python
:caption: compression-output.py

from abaqus import *
from abaqusConstants import *
from driverUtils import *
import visualization
import numpy as np

executeOnCaeStartup()

# Open output database
odb = session.openOdb('Job-1.odb')
session.viewports['Viewport: 1'].setValues(displayedObject=odb)

# Extract output data
dataList = session.xyDataListFromField(odb=odb, outputPosition=NODAL,
                                       variable=(('U', NODAL, ((COMPONENT, 'U3'),)),),
                                       nodeSets=('INSTANCE.SET-TOP', ))
data = np.array(dataList[0])
np.savetxt('data.csv', data, header='time,U3', delimiter=',', comments='')
```
