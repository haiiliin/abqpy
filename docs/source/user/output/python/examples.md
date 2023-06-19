# Example scripts that access data from an output database

The following examples illustrate how you use the output database commands to access data from an output database.

In addition, the Abaqus Scripting Interface examples, {doc}`/user/about/examples/read-output` and {doc}`/user/examples/index` illustrate how to read data from an output database.

## Finding the maximum value of von Mises stress

This example illustrates how you can iterate through an output database and search for the maximum value of von Mises stress. The script opens the output database specified by the first argument on the command line and iterates through the following:

- Each step.
- Each frame in each step.
- Each value of von Mises stress in each frame.

In addition, you can supply an optional assembly element set argument from the command line, in which case the script searches only the element set for the maximum value of von Mises stress.

The following illustrates how you can run the example script from the system prompt. The script will search the element set ALL ELEMENTS in the viewer tutorial output database for the maximum value of von Mises stress:

```sh
abaqus python odbMaxMises.py -odb viewer_tutorial.odb
    -elset "ALL ELEMENTS"
```

```{note}
If a command line argument is a String that contains spaces, some systems will interpret the String correctly only if it is enclosed in double quotation marks. For example, `"ALL ELEMENTS"`.
```

You can also run the example with only the **-help** parameter for a summary of the usage.

Use the following commands to retrieve the example script and the viewer tutorial output database:

```python2
# abaqus fetch job=odbMaxMises.py
# abaqus fetch job=viewer_tutorial
"""
odbMaxMises.py
Code to determine the location and value of the maximum
von-mises stress in an output database.
Usage: abaqus python odbMaxMises.py -odb odbName
    -elset(optional) elsetName
Requirements:
1. -odb   : Name of the output database.
2. -elset : Name of the assembly level element set.
            Search will be done only for element belonging
            to this set. If this parameter is not provided,
            search will be performed over the entire model.
3. -help  : Print usage
"""

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from odbAccess import *
from sys import argv,exit
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def rightTrim(input,suffix):
    if (input.find(suffix) == -1):
        input = input + suffix
    return input
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def getMaxMises(odbName,elsetName):
    """ Print max mises location and value given odbName
        and elset(optional)
    """
    elset = elemset = None
    region = "over the entire model"
    """ Open the output database """
    odb = openOdb(odbName)
    assembly = odb.rootAssembly

    """ Check to see if the element set exists
        in the assembly
    """
    if elsetName:
        try:
            elemset = assembly.elementSets[elsetName]
            region = " in the element set : " + elsetName;
        except KeyError:
            print 'An assembly level elset named %s does'
                'not exist in the output database %s' \
                % (elsetName, odbName)
            odb.close()
            exit(0)

    """ Initialize maximum values """
    maxMises = -0.1
    maxElem = 0
    maxStep = "_None_"
    maxFrame = -1
    Stress = 'S'
    isStressPresent = 0
    for step in odb.steps.values():
        print 'Processing Step:', step.name
        for frame in step.frames:
            allFields = frame.fieldOutputs
            if (allFields.has_key(Stress)):
                isStressPresent = 1
                stressSet = allFields[Stress]
                if elemset:
                    stressSet = stressSet.getSubset(
                        region=elemset)
                for stressValue in stressSet.values:
                    if (stressValue.mises > maxMises):
                        maxMises = stressValue.mises
                        maxElem = stressValue.elementLabel
                        maxStep = step.name
                        maxFrame = frame.incrementNumber
    if(isStressPresent):
        print 'Maximum von Mises stress %s is %f in element %d'%(
            region, maxMises, maxElem)
        print 'Location: frame # %d  step:  %s '%(maxFrame,maxStep)
    else:
        print 'Stress output is not available in' \
            'the output database : %s\n' %(odb.name)

    """ Close the output database before exiting the program """
    odb.close()

#==================================================================
# S T A R T
#
if __name__ == '__main__':

    odbName = None
    elsetName = None
    argList = argv
    argc = len(argList)
    i=0
    while (i < argc):
        if (argList[i][:2] == "-o"):
            i += 1
            name = argList[i]
            odbName = rightTrim(name,".odb")
        elif (argList[i][:2] == "-e"):
            i += 1
            elsetName = argList[i]
        elif (argList[i][:2] == "-h"):
            print __doc__
            exit(0)
        i += 1
    if not (odbName):
        print ' **ERROR** output database name is not provided'
        print __doc__
        exit(1)
    getMaxMises(odbName,elsetName)
```

(creating-an-output-database)=

## Creating an output database

The following example illustrates how you can use the Abaqus Scripting Interface commands to do the following:

1. Create a new output database.
2. Add model data.
3. Add field data.
4. Add history data.
5. Read history data.
6. Save the output database.

Use the following command to retrieve the example script:

```python2
abaqus fetch job=odbWrite
"""odbWrite.py
Script to create an output database and add model,
field, and history data. The script also reads
history data, performs an operation on the data, and writes
the result back to the output database.
usage: abaqus python odbWrite.py
"""
from odbAccess import *
from odbMaterial import *
from odbSection import *
from abaqusConstants import *

def createODB():

    # Create an ODB (which also creates the rootAssembly)
    odb = Odb(name='simpleModel',
        analysisTitle='ODB created with Python ODB API',
        description='example illustrating Python ODB API ',
        path='odbWritePython.odb')

    # create few materials
    materialName = "Elastic Material"
    material_1 = odb.Material(name=materialName)
    material_1.Elastic(type=ISOTROPIC,
        temperatureDependency=OFF, dependencies=0,
        noCompression=OFF, noTension=OFF,
        moduli=LONG_TERM, table=((12000,0.3),))

    # create few sections
    sectionName = 'Homogeneous Shell Section'
    section_1 = odb.HomogeneousShellSection(name=sectionName,
        material=materialName, thickness=2.0)
    #  Model data:

    # Set up the section categories.
    sCat = odb.SectionCategory(name='S5',
        description='Five-Layered Shell')
    spBot = sCat.SectionPoint(number=1,
        description='Bottom')
    spMid = sCat.SectionPoint(number=3,
        description='Middle')
    spTop = sCat.SectionPoint(number=5,
        description='Top')

    #  Create a 2-element shell model,
    #  4 integration points, 5 section points.

    part1 = odb.Part(name='part-1', embeddedSpace=THREE_D,
        type=DEFORMABLE_BODY)
    nodeData = (
        (1, 1,0,0),
        (2, 2,0,0),
        (3, 2,1,0.1),
        (4, 1,1,0.1),
        (5, 2,-1,-0.1),
        (6, 1,-1,-0.1),
        )
    part1.addNodes(nodeData=nodeData,
        nodeSetName='nset-1')

    elementData = (
        (1, 1,2,3,4),
        (2, 6,5,2,1),
        )
    part1.addElements(elementData=elementData, type='S4',
        elementSetName='eset-1', sectionCategory=sCat)

    #  Instance the part.
    instance1 = odb.rootAssembly.Instance(name='part-1-1',
        object=part1)
    # create instance level sets for section assignment
    elLabels = (1,2)
    elset_1 = odb.rootAssembly.instances['part-1-1'].ElementSetFromElementLabels(name=materialName, elementLabels=elLabels)
    instance1.assignSection(region=elset_1, section=section_1)

    #  Field data:

    #  Create a step and a frame.

    step1 = odb.Step(name='step-1',
        description='first analysis step',
        domain=TIME, timePeriod=1.0)
    analysisTime=0.1
    frame1 = step1.Frame(incrementNumber=1,
        frameValue=analysisTime,
        description=\
            'results frame for time '+str(analysisTime))


    #  Write nodal displacements.

    uField = frame1.FieldOutput(name='U',
        description='Displacements', type=VECTOR)

    nodeLabelData = (1, 2, 3, 4, 5, 6)
    dispData = (
        (1,2,3),
        (4,5,6),
        (7,8,9),
        (10,11,12),
        (13, 14, 15),
        (16,17,18)
        )

    uField.addData(position=NODAL, instance=instance1,
        labels=nodeLabelData,
        data=dispData)

    #  Make this the default deformed field for visualization.

    step1.setDefaultDeformedField(uField)

    """ Write stress tensors
    (output only available at top/bottom section points)
    The element defined above (S4) has 4 integration points.
    Hence, there are 4 stress tensors per element.
    Each Field constructor refers to only one layer of section
    points.
    """

    elementLabelData = (1, 2)
    topData = (
        (1.,2.,3.,4.),
        (1.,2.,3.,4.),
        (1.,2.,3.,4.),
        (1.,2.,3.,4.),
        (1.,2.,3.,4.),
        (1.,2.,3.,4.),
        (1.,2.,3.,4.),
        (1.,2.,3.,4.),
        )
    bottomData = (
        (1.,2.,3.,4.),
        (1.,2.,3.,4.),
        (1.,2.,3.,4.),
        (1.,2.,3.,4.),
        (1.,2.,3.,4.),
        (1.,2.,3.,4.),
        (1.,2.,3.,4.),
        (1.,2.,3.,4.),
        )

    transform = (
        (1.,0.,0.),
        (0.,1.,0.),
        (0.,0.,1.)
        )

    sField = frame1.FieldOutput(name='S',
        description='Stress', type=TENSOR_3D_PLANAR,
        componentLabels=('S11', 'S22', 'S33','S12'),
        validInvariants=(MISES,))
    sField.addData(position=INTEGRATION_POINT,
    sectionPoint=spTop, instance=instance1,
    labels=elementLabelData, data=topData,
    localCoordSystem=transform)
    sField.addData(position=INTEGRATION_POINT,
        sectionPoint=spBot, instance=instance1,
        labels=elementLabelData, data=bottomData,
        localCoordSystem=transform)

    #  For this step, make this the default field
    #  for visualization.

    step1.setDefaultField(sField)

    #  History data:

    #  Create a HistoryRegion for a specific point.

    hRegionStep1 = step1.HistoryRegion(name='historyNode0',
        description='Displacement and reaction force',
        point=instance1.nodes[0])

    #  Create variables for this history output in step1.

    hOutputStep1U1 = hRegionStep1.HistoryOutput(name='U1',
        description='Displacement', type=SCALAR)
    hOutputStep1Rf1 = hRegionStep1.HistoryOutput(name='RF1',
        description='Reaction Force', type=SCALAR)

    #  Add history data for step1.

    timeData1 = (0.0, 0.1, 0.3, 1.0)
    u1Data = (0.0, 0.1, 0.3, 0.5)
    rf1Data = (0.0, 0.1, 0.3, 0.5)

    hOutputStep1U1.addData(frameValue=timeData1,
        value=u1Data)
    hOutputStep1Rf1.addData(frameValue=timeData1,
        value=rf1Data)

    #  Create another step for history data.
    step2 = odb.Step(name='step-2',  description='',
        domain=TIME, timePeriod=1.0)
    hRegionStep2 = step2.HistoryRegion(
        name='historyNode0',
        description='Displacement and reaction force',
        point=instance1.nodes[0])
    hOutputStep2U1 = hRegionStep2.HistoryOutput(
        name='U1',
        description='Displacement',
        type=SCALAR)
    hOutputStep2Rf1 = hRegionStep2.HistoryOutput(
        name='RF1',
        description='Reaction Force',
        type=SCALAR)

    #  Add history data for the second step.
    timeData2 = (1.2, 1.9, 3.0, 4.0)
    u1Data = (0.8, 0.9, 1.3, 1.5)
    rf1Data = (0.9, 1.1, 1.3, 1.5)

    hOutputStep2U1.addData(frameValue=timeData2,
        value=u1Data)
    hOutputStep2Rf1.addData(frameValue=timeData2,
        value=rf1Data)

    # Get XY Data from the two steps.
    u1FromStep1 = hRegionStep1.getSubset(variableName='U1')
    u1FromStep2 = hRegionStep2.getSubset(variableName='U1')

    # Square the history data.
    u1SquaredFromStep1 = \
        power(u1FromStep1.historyOutputs['U1'], 2.0)
    u1SquaredFromStep2 = \
        power(u1FromStep2.historyOutputs['U1'], 2.0)

    # Add the squared displacement to the two steps.
    hOutputStep1sumU1 = hRegionStep1.HistoryOutput(
        name='squareU1',
        description='Square of displacements',
        type=SCALAR)
    hOutputStep1sumU1.addData(data=u1SquaredFromStep1.data)

    hOutputStep2sumU1 = hRegionStep2.HistoryOutput(
        name='squareU1',
        description='Square of displacements',
        type=SCALAR)
    hOutputStep2sumU1.addData(data=u1SquaredFromStep2.data)

    # Save the results in the output database.
    # Use the Visualization module of Abaqus/CAE to
    # view the contents of the output database.

    odb.save()
    odb.close()

if __name__ == "__main__":
    createODB()
```

## An Abaqus Scripting Interface version of FPERT

A Fortran program that reads the Abaqus results file and creates a deformed mesh from the original coordinate data and eigenvectors is described in [Creation of a perturbed mesh from original coordinate data and eigenvectors: FPERT](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEEXARefMap/simaexa-c-fpert.htm?contextscope=all). This example illustrates an Abaqus Scripting Interface script that reads an output database and performs similar calculations.

The command line arguments provide the following:

- **odbName**: The output database file name.
- **modeList**: A list of eigenmodes to use in the perturbation.
- **weightList**: The perturbation weighting factors.
- **outNameUser**: The output file name (optional).

Use the following command to retrieve the example script:

```python2
# abaqus fetch job=odbPert

# Abaqus Scripting Interface version of FPERT, a Fortran
# program to create a perturbed mesh from original coordinate
# data and eigenvectors. FPERT is described in the Abaqus Example
# Problems Manual.

import sys
from odbAccess import *
from types import IntType

# Get input from the user

odbName = raw_input('Enter odb name (w/o .odb): ')
modes = eval(raw_input('Enter mode shape(s): '))
if type(modes) is IntType:
    modes = (modes,)

odb = openOdb(odbName + '.odb')

# Get the undeformed coordinates from the first
# step and frame

step = odb.steps.values()[0]

try:
coords = step.frames[0].fieldOutputs['COORD']
except:
err = "The analysis must include a field output request \
    for variable COORD."
print err
sys.exit(1)

# Perturb the nodal coordinates

factors = []
for mode in modes:
    try:
    frame = step.frames[mode]
    except IndexError:
    print 'Input error: mode %s does not exist' % mode
    sys.exit(1)
    factors.append(float(raw_input(
        'Enter imperfection factor for mode %s: '% mode)))
    coords = coords + factors[-1] * frame.fieldOutputs['U']

# Write new nodal coordinates to a file

outFile = open(odbName + '_perturbed.inp', 'w')
header = \
"""
*******************************************************
** Node data for perturbed mesh.
** Input mesh from: %s
** Mode shapes used: %s
** Imperfection factors used: %s
*******************************************************
"""
outFile.write(header % (odbName, modes, factors))
format = '%6i, %14.7e, %14.7e, %14.7e\n'
for value in coords.values:
    outFile.write(
        format % ((value.nodeLabel,) + tuple(value.data)))
outFile.write('** End of perturbed mesh node input file.')
outFile.close()
```

(computations-with-fieldoutput-objects)=

## Computations with FieldOutput objects

This example illustrates how you can operate on FieldOutput objects and save the computed field to the output database. The example script does the following:

Retrieves two specified fields from the output database.

- Computes a new field by subtracting the fields that were retrieved.
- Creates a new Step object in the output database.
- Creates a new Frame object in the new step.
- Creates a new FieldOutput object in the new frame.
- Uses the `addData` method to add the computed field to the new FieldOutput object.
- Use the following command to retrieve the example script:

```python2
abaqus fetch job=fieldOperation
```

The fetch command also retrieves an input file that you can use to generate the output database that is read by the example script.

```python2
# FieldOutput operators example problem
#
# Script that does computations with fields and
# saves the results computed to the output database
#

from odbAccess import *
odb = openOdb(path='fieldOperation.odb')

# Get fields from output database.

field1 = odb.steps['LC1'].frames[1].fieldOutputs['U']
field2 = odb.steps['LC2'].frames[1].fieldOutputs['U']

# Compute difference between fields.

deltaDisp = field2 - field1

# Save new field.

newStep = odb.Step(name='user',
    description='user defined results', domain= TIME, timePeriod=0)
newFrame = newStep.Frame(incrementNumber=0, frameValue=0.0)
newField = newFrame.FieldOutput(name='U',
    description='delta displacements', type=VECTOR)
newField.addData(field=deltaDisp)

odb.save()
```

## Computations with FieldValue objects

This example illustrates how you can use the fieldValue operators to sum and average fieldValues in a region. The example script does the following:

- Retrieves the stress field for a specified region during the last step and frame of the output database.
- Sums all the stress fieldValues and computes the average value.
- For each component of stress, print the sum and the average stress.

Use the following command to retrieve the example script:

```sh
abaqus fetch job=sumRegionFieldValue
```

The fetch command also retrieves an input file that you can use to generate the output database that is read by the example script.

```python2
#
# fieldValue operators example problem:
#
# sum and average stress field values in a region
#

from odbAccess import *

#
# get field
#

odb = openOdb(path='sumRegionFieldValue.odb')
endSet = odb.rootAssembly.elementSets['END1']
field = odb.steps.values()[-1].frames[-1].fieldOutputs['S']
subField = field.getSubset(region=endSet)

#
# sum values
#

sum = 0
for val in subField.values:
sum = sum + val
ave = sum / len(subField.values)

#
# print results
#

print 'Component    Sum            Average'
labels = field.componentLabels
for i in range( len(labels) ):
    print '%s          %5.3e      %5.3e'% \
            (labels[i], sum.data[i], ave.data[i])
```

## Computations with HistoryOutput objects

This example illustrates how you can use the historyOutput operators to compute the displacement magnitude from the components. The example script does the following:

- Retrieves the node of interest using a nodeSet.
- Uses the node of interest to construct a HistoryPoint object.
- Uses the HistoryPoint to retrieve the historyRegion.
- Computes the displacement magnitude history from the displacement component HistoryOutput objects in the historyRegion.
- Scales the displacement magnitude history using a predefined value.
- Prints the displacement magnitude history.

Use the following command to retrieve the example script:

```sh
abaqus fetch job=compDispMagHist
```

The fetch command also retrieves an input file that you can use to generate the output database that is read by the example script.

```python2
# HistoryOutput operators example problem.
#
# Compute magnitude of node displacement history from
# displacement components and scale relative to given
# allowable displacement.
#

from odbAccess import *

#
# get historyRegion for the node in nodeSet TIP
#

odb = openOdb(path='compDispMagHist.odb')
endSet = odb.rootAssembly.instances['BEAM-1-1'].nodeSets['TIP']
histPoint = HistoryPoint(node=endSet.nodes[0])
tipHistories = odb.steps['Step-2'].getHistoryRegion(
    point=histPoint)

#
# Compute and scale magnitude.
#

maxAllowableDisp = 5.0
sum = 0
componentLabels = ('U1', 'U2', 'U3')
for name in componentLabels:
   sum = sum + power(tipHistories.historyOutputs[name], 2.0)
sum = sqrt(sum) / maxAllowableDisp

#
# Print magnitude.
#

print 'History:', sum.name
print 'Time       Magnitude'
for dataPair in sum.data:
    print "%5.4f  %5.2f"%(dataPair[0], dataPair[1])
```

## Creating a new load combination from different load cases

This example illustrates how you can use the frame operators to create a new load combination from existing load cases. The example script does the following:

- Retrieves the information describing the new load combination from the command line.
- Retrieves the frames for each load case.
- Computes the new stresses and displacements.
- Saves data computed to the output database as a new load combination.

The command line arguments provide the following:

- **odbName**: The output database file name.
- **stepName**: The name of the step containing the load cases.
- **loadCaseNames**: The load case names.
- **scaling**: The scale factors to apply to each load case.

Use the following command to retrieve the example script:

```sh
abaqus fetch job=createLoadComb
```

The fetch command also retrieves an input file that you can use to generate an output database that can be read by the example script.

```python2
import types
from odbAccess import *

# retrieve request from user
odbName = raw_input('Enter odb name')
stepName = raw_input('Enter step name')

loadCaseNames = eval(raw_input(
    'Enter new load case as:
    ['loadCase1Name', ..., 'loadCaseNName']'))
if type(loadCaseNames) == types.TupleType:
    loadCaseNames = list(loadCaseNames)
lcName = raw_input('Enter new load case name')
scaling = eval(raw_input(
    'Enter new load case as:(scaleFactor1, .., scaleFactorN)'))

odb = openOdb(odbName)
step = odb.steps[stepName]

# compute new load case
newStress = 0
newDisp = 0

for loadCaseName in loadCaseNames:
    frame = step.getFrame(loadCase=step.loadCases[loadCaseName])
    scaleFac = scaling[loadCaseNames.index(frame.loadCase.name)]
    newStress = newStress + scaleFac*frame.fieldOutputs['S']
    newDisp = newDisp + scaleFac*frame.fieldOutputs['U']

# save new load case to odb
lcNew = step.LoadCase(name=lcName)
newFrame = step.Frame(loadCase=lcNew)
newFrame.FieldOutput(field=newStress, name='S')
newFrame.FieldOutput(name='U', field=newDisp)

odb.save()
odb.close()
```

## Stress range for multiple load cases

This example illustrates how you can use the envelope operations to compute the stress range over a number of load cases. The example script does the following:

- For each load case during a specified step, the script collects the S11 components of the stress tensor fields into a list of scalar fields.
- Computes the maximum and minimum of the S11 stress component using the envelope calculations.
- Computes the stress range using the maximum and minimum values of the stress component.
- Creates a new frame in the step.
- Writes the computed stress range into a new FieldOutput object in the new frame.

Use the following command to retrieve the example script:

```sh
abaqus fetch job=stressRange
```

The fetch command also retrieves an input file that you can use to generate an output database that can be read by the example script.

```python2
from odbAccess import *

# retrieve request from user
odbName = raw_input('Enter odb name')
stepName = raw_input('Enter step name')

# retrieve steps from the odb
odb=openOdb(odbName)
step = odb.steps[stepName]
sFields = []

for loadCase in step.loadCases.values():
    stressField = step.getFrame(loadCase=loadCase).fieldOutputs['S']
    sFields.append(stressField.getScalarField(componentLabel='S11'))

# compute stress range
maxStress, maxLoc = maxEnvelope(sFields)
minStress, minLoc = minEnvelope(sFields)

stressRange = maxStress - minStress

# save to same step
newFrame = step.Frame(incrementNumber=0, frameValue=0.0,
    description='Stress Range')
newFrame.FieldOutput(field=stressRange, name='S11 Range')

odb.save()
odb.close()
```

(transformation-of-field-results)=

## Transformation of field results

This example illustrates how field results can be transformed to a different coordinate system. The example computes deviation of the nodal displacements with respect to a perfectly cylindrical displacement (cylinder bore distortion). The example does the following:

- Creates a cylindrical coordinate system.
- Transforms the results to the new coordinate system.
- Computes the average radial displacement.
- Computes the distortion as the difference between radial displacement and the average radial displacement.
- Saves the distortion field to the output database for viewing.

Use the following commands to retrieve the example script and an input file to create a sample output database:

```python2
# abaqus fetch job=transformExa
# abaqus fetch job=esf4sxdg
from odbAccess import *

# Retrieve request from user.

odbName = raw_input('Enter odb name')
stepName = raw_input('Enter step name')
frameNo = int( raw_input('Enter frame number') )


odb = openOdb(odbName)

# Retrieve the displacements from last frame of the last step.

step = odb.steps[stepName]
frame = step.frames[frameNo]
displacement = frame.fieldOutputs['U']

# Create cylindrical coordinate system and compute
# associated results

coordSys = odb.rootAssembly.DatumCsysByThreePoints(name='cylC',
    coordSysType=CYLINDRICAL, origin=(0,0,0),
    point1=(1.0, 0.0, 0), point2=(0.0, 0.0, 1.0) )

cylindricalDisp = displacement.getTransformedField(
    datumCsys=coordSys)
radialDisp = cylindricalDisp.getScalarField(componentLabel='U1')

# Compute average radius.

sum = 0.0
for val in radialDisp.values:
    sum = sum + val.data
aveDisp = sum / len(radialDisp.values)

# Compute distortion.

distortion = radialDisp - aveDisp

# Save computed results to the database.

frame.FieldOutput(field=radialDisp)
fieldDescription = 'Distortion ( \
    average radial displacement = ' + str(aveDisp) + ')'
frame.FieldOutput(name='Distortion',
    description=fieldDescription, field=distortion)

odb.save()
odb.close()
```

## Viewing the analysis of a meshed beam cross-section

This example illustrates how you can view the results of a meshed beam cross-section analysis that was generated using Timoshenko beams, as described in [Meshed beam cross-sections](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEANLRefMap/simaanl-c-meshedsection.htm?contextscope=all). Before you execute the example script, you must run two analyses that create the following output database files:

- An output database generated by the two-dimensional cross-section analysis. The script reads cross-section data, including the out-of-plane warping function, from this output database.
- An output database generated by the beam analysis. The script reads generalized section strains (SE) from this output database.

Use the following command to retrieve the example script:

```sh
abaqus fetch job=compositeBeam
```

You must run the script from Abaqus/CAE by selecting **File -> Run Script** from the main menu. The script uses `getInputs` to display a dialog box that prompts you for the name of the output databases generated by the two-dimensional cross-section analysis and by the beam analysis. The names are case-insensitive, and you can omit the `.odb` file suffix. The files must be in the local directory. The dialog box also prompts you for the following:

- The name of the step
- The increment or mode number (for a frequency analysis)
- The name of the load case (if any)
- The name of the part instance
- The element number
- The integration point number

If you do not enter a value in a field, the script looks in the beam analysis output database for possible values. The script then enters a default value in the dialog box and displays information about the range of possible values in the Abaqus/CAE message area. You can leave the load case field blank if the analysis did not include load cases. The script does not continue until all the values in the dialog box are acceptable. The same values are written to a file called `compositeBeam_values.dat` in the local directory, and these values appear as defaults in the dialog box the next time you run the example script.

After the `getInputs` method returns acceptable values, the script reads the two output databases and writes the generated data back to the output database created by the two-dimensional cross-section analysis. If the beam cross-section mesh consists of 1-DOF warping elements, the script then displays an undeformed contour plot of S11 and uses the getInputs method again to display a dialog box with a list of the available stress and strain components (S11, S22, S33, E11, E22, and E33). If the beam cross-section mesh consists of 3-DOF warping elements, the deformed contour plot is displayed, and the full three-dimensional stress and strain components (S11, S22, S33, S12, S13, S23, E11, E22, E33, E12, E13, and E23) are available. The deformation represents the in-plane and out-of-plane warping. Click **OK** in this dialog box to cycle through the available components. Click Cancel to end the script. You can also select the component to display by starting the Visualization module and selecting `Result -> Field Output` from the main menu.

The example script writes new stress and strain fields. The script must provide a unique name for the generated field output because each of these fields is generated for a specific beam analysis output database and for a specific part instance, step, frame, element, and integration point. The script constructs this unique name as follows:

- All contour stress and strain fields for a specific beam analysis output database are written to a new frame, where the description of the frame is the name of the output database. For example, for a beam analysis output database called `beam_run17.odb`, the frame description is **Beam ODB: beam_run17**.
- The field name is assembled from a concatenation of the **step name**, **frame index**, **instance name**, **element**, and **integration point**, followed by E or S. For example, `Step-1_4_LINEARMESHED_12_1_E`. Any spaces in a step or instance name are replaced by underscores.

You can run the script many times; for example, to create contour data for a particular step, increment, and integration point along each element of the beam. In this case you would also use **Result -> Field Output** to select which element to display.

The contour data generated by the example script are written back to the output database that was originally created by the two-dimensional, cross-section analysis. If you want to preserve this database in its original form, you must save a copy before you run the example script.

## Using infinite elements to compute and view the results of an acoustic far-field analysis

This example illustrates how you can use the Abaqus Scripting Interface to compute acoustic far-field pressure values from infinite element sets and project the results onto a spherical surface for visualization purposes. This script is designed primarily to compute the acoustic far-field pressure using a layer of infinite acoustic elements that forms a full or partial spherical surface. The script extends the acoustic analysis functionality within Abaqus/Standard, as described in [Acoustic, shock, and coupled acoustic-structural analysis](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEANLRefMap/simaanl-c-acoustic.htm?contextscope=all) and [Infinite elements](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEELMRefMap/simaelm-c-infinite.htm?contextscope=all). The script writes the acoustic far-field pressure values to an output database, and you can use Abaqus/CAE to view the far-field results.

The far-field pressure is defined as

$$
\lim _{r \rightarrow \infty} p(r)=\lim _{r \rightarrow \infty}\left(\frac{1}{k r} e^{-i k r} p_{F A R}\right)
$$

where $p(r)$ is the acoustic pressure at a distance $r$ from the reference point, $k$ is the wave number, and $p_{F A R}$ is the acoustic far-field pressure. The acoustic pressure decibel value is defined as

$$
&\mathrm{PORdB}=20 \log _{10}\left(\frac{p_{R M S}}{d B R e f}\right) \\
&p_{R M S}=\left(\frac{|\mathrm{POR}|}{\sqrt{2}}\right)
$$

where $|\mathrm{POR}|$ is the magnitude of the acoustic pressure at a point, $p_{R M S}$ is the root mean square acoustic pressure, and $d B R e f$ is the decibel reference value given as user input. The far-field pressure decibel value is defined in the same manner as $\operatorname{POR} d B$, using the same reference value $d B R e f)$

```{note}
If $d B R e f=20 \mu P a$ (in SI units), POR $d B$ corresponds to $d B S P L$
```

The script also calculates the far-field acoustic intensity, which is defined as

$$
\mathrm{INTEN}_{\mathrm{FAR}}=\left(\frac{p_{R M S F A R}^{2}}{\rho\times c}\right)
$$

where $p_{R M S F A R}$ is the far-field rms pressure, $\rho$ is the fluid density, and $c$ is the speed of sound in the medium.

Before you execute the script, you must run a direct-solution, steady-state dynamics acoustics analysis that includes three-dimensional acoustic infinite elements (ACIN3D3, ACIN3D4, ACIN3D6, and ACIN3D8). In addition, the output database must contain results for the following output variables:

- INFN, the acoustic infinite element normal vector.
- INFR, the acoustic infinite element “radius,” used in the coordinate map for these elements.
- PINF, the acoustic infinite element pressure coefficients.

Use the following command to retrieve the script:

```sh
abaqus fetch job=acousticVisualization
```

Enter the Visualization module, and display the output database in the current viewport. Run the script by selecting **File -> Run Script** from the main menu bar.

The script uses getInputs to display a dialog box that prompts you for the following information:

- The name of the element set containing the infinite elements (the name is case sensitive). By default, the script locates all the infinite elements in the model and uses them to create the spherical surface. If the script cannot find the specified element set in the output database, it displays a list of the available element sets in the message area.

- The radius of the sphere (required). The script asks you to enter a new value if the sphere with this radius does not intersect any of the selected infinite elements.

- The coordinates of the center of the sphere. By default, the script uses (0,0,0).

- The analysis steps. You can enter one of the following:

  - An Int
  - A comma-separated list of Ints
  - A range; for example, 1:20

  You can also enter a combination of Ints and ranges; for example, 4,5,10:20,30. By default, the script reads data from all the steps. The script ignores any steps that do not perform a direct-solution, steady-state dynamics acoustics analysis or that have no results.

- The frequencies for which output should be generated (Hz). You can enter a Float, a list of Floats, or a range. By default, the script generates output for all the frequencies in the original output database.

- A decibel reference value (required).

- The name of the part instance to create (required). The script appends this name to the name of the instance containing the infinite elements being used.

- The speed of sound (required).

- The fluid density (required)

- Whether to write data to the original output database. By default, the script writes to an output database called `current-odb-name_acvis.odb`.

After the `getInputs` method returns acceptable values, the script processes the elements in the specified element sets. The visualization sphere is then determined using the specified radius and center. For each element in the infinite element sets, the script creates a corresponding membrane element such that the new element is a projection of the old element onto the surface of the sphere. The projection uses the infinite element reference point and the internally calculated infinite direction normal (INFN) at each node of the element.

Once the new display elements have been created, the script writes results at the nodes in the set. The following output results are written back to the output database:

- POR, the acoustic pressure.
- PORdB, the acoustic pressure decibel value. If the reference value used is $2\times10^{-5}$ Pa, the PFARdB corresponds to dB SPL.
- PFAR, the acoustic far-field pressure.
- PFARdB, the far-field pressure decibel value.
- INTEN_FAR, the far-field acoustic intensity.

To create the output at each node, the script first determines the point at which the node ray intersects the sphere. Using the distance from the reference point to the intersection point and the element shape functions, the required output variables are calculated at the intersection point.

After the script has finished writing data, it opens the output database containing the new data. For comparison, the original instance is displayed along with the new instance, but results are available only for the new instance. However, if you chose to write the results back to the original output database, the original instance and the new instance along with the original results and the new results can be displayed side-by-side. The script displays any error, warning, or information messages in the message area.

You can run the script more than once and continue writing data to the same output database. For example, you can run the script several times to look at the far-field pressures at various points in space, and results on several spheres will be written to the output database.

To see how the script operates on a single triangular-element model, use the following command to retrieve the input file:

```sh
abaqus fetch job=singleTriangularElementModel
```

Use the following command to create the corresponding output database:

```sh
abaqus job=singleTriangularElementModel
```

The results from running the script twice using the single triangular-element model, changing the radius of the sphere, and writing the data back to the original output database are shown in {numref}`cmd-odb-api-acousticviz`

(cmd-odb-api-acousticviz)=

```{figure} /images/cmd-odb-api-acousticviz.png
:align: center
:width: 50%

Displaying the acoustic pressure on several spheres.
```

This model simulates the response of a sphere in "breathing" mode (a uniform radial expansion/compression mode). The model consists of one triangular ACIN3D3 element. Each node of the element is placed on a coordinate axis at a distance of $1.0$ from the origin that serves as the reference point for the infinite element. The acoustic material properties do not have physical significance; the values used are for convenience only. The loading consists of applying an in-phase pressure boundary condition to all the nodes. Under this loading and geometry, the model behaves as a spherical source (an acoustic monopole) radiating in the radial direction only. The acoustic pressure, $p$, and the acoustic far-field pressure, $p_{F A R}$, at a distance $r$ from the center of the sphere are

$$
p(r)=p_{0}\left(\frac{r_{0}}{r}\right) e^{-i k\left(r-r_{0}\right)}
$$

and

$$
p_{F A R}(r)=p_{0} r_{0} k e^{i k r_{0}}
$$

where $p_{0}$ is the known acoustic pressure at some reference distance $r_{0}$ and $k$ is the wave number.

For this single-element example, you should enter a value of $1.0$ for the speed of sound; thus, $k=2 \pi f$, where $f$ is the frequency in $\mathrm{Hz}$. $r_{0}$ in this model is 1 , and $p_{0}$ is $0.001$. The equations for the acoustic pressure, $p$, and the acoustic far-field pressure, $p_{F A R}$, reduce to

$$
p(r)=\frac{0.001}{r} e^{-i k(r-1)}
$$

and

$$
p_{F A R}(r)=0.001 k e^{i k}.
$$

## An Abaqus Scripting Interface version of FELBOW

This example illustrates the use of an Abaqus Scripting Interface script to read selected element integration point records from an output database and to postprocess the elbow element results. The script creates X–Y data that can be plotted with the X–Y plotting capability in Abaqus/CAE. The script performs the same function as the Fortran program described in [Creation of a data file to facilitate the postprocessing of elbow element results: FELBOW](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEEXARefMap/simaexa-c-felbow.htm?contextscope=all).

The script reads integration point data for elbow elements from an output database to visualize one of the following:

1. Variation of an output variable around the circumference of a given elbow element, or
2. Ovalization of a given elbow element.

The script creates either an ASCII file containing **X - Y** data or a new output database file that can be viewed using Abaqus/CAE.

To use option 2, you must ensure that the integration point coordinates (COORD) are written to the output database. For option 1 the **X** - data are data for the distance around the circumference of the elbow element, measured along the middle surface, and the **Y** - data are data for the output variable. For option 2 the **X - Y** data are the current coordinates of the middle-surface integration points around the circumference of the elbow element, projected to a local coordinate system in the plane of the deformed cross-section. The origin of the local system coincides with the center of the cross-section; the plane of the deformed cross-section is defined as the plane that contains the center of the cross-section.

You should specify the name of the output database during program execution. The script prompts for more information, depending on the option that was chosen; this information includes the following:

- Your choice for storing results (ASCII file or a new output database)
- File name based on the above choice
- The postprocessing option (1 or 2)
- The part name
- The step name
- The frame number
- The element output variable (option 1 only)
- The component of the variable (option 1 only)
- The section point number (option 1 only)
- The element number or element set name

Before executing the script, run an analysis that creates an output database file containing the appropriate output. This analysis includes, for example, output for the elements and the integration point coordinates of the elements. Execute the script using the following command:

```python2
abaqus python felbow.py <filename.odb>
```

The script prompts for other information, such as the desired postprocessing option, part name, etc. The script processes the data and produces a text file or a new output database that contains the information required to visualize the elbow element results.

[Elastic-plastic collapse of a thin-walled elbow under in-plane bending and internal pressure](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEEXARefMap/simaexa-c-elbowcollapse.htm?contextscope=all) contains several figures that can be created with the aid of this program.
