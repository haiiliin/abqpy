# Generating a customized plot

The following section provides examples of Abaqus Scripting Interface scripts that open an output database and generate a customized plot. In effect, these scripts reproduce the functionality of the Visualization module in Abaqus/CAE.

(opening-the-tutorial-output-database)=

## Opening the tutorial output database

Each of the following example scripts opens the output database used by the Visualization module tutorial in Getting Started with Abaqus/CAE. Use the following command to retrieve the output database that is read by the scripts:

```sh
abaqus fetch job=viewer_tutorial
```

(opening-an-output-database-and-displaying-a-contour-plot)=

## Opening an output database and displaying a contour plot

The following example of a script containing Abaqus Scripting Interface commands uses the output database used by [Viewing the Output from Your Analysis](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEGSARefMap/simagsa-m-Caevismod-sb.htm?contextscope=all#simagsa-m-Caevismod-sb).

Use the following command to retrieve the example script:

```sh
abaqus fetch job=viewerOpenOdbAndContour
```

The script does the following:

- Creates a viewport, and makes it the current viewport.
- Opens an output database.
- Displays a contour plot.
- Displays the model in the first frame of the third step.
- Sets the number of contour intervals and the contour limits.
- Prints a color image of the viewport to a .png file.

```python2
"""
viewerOpenOdbAndContour.py

Print a contour plot to a local PNG-format file.
"""

from abaqus import *
from abaqusConstants import *
import visualization

# Create a new Viewport for this example.

myViewport=session.Viewport(name='Print a contour plot',
    origin=(10, 10), width=200, height=100)

# Open the output database and associate it
# with the new viewport.

odbPath = "viewer_tutorial.odb"
myOdb = visualization.openOdb(path=odbPath)

myViewport.setValues(displayedObject=myOdb)


# Display a contour plot of the output database.

myViewport.odbDisplay.display.setValues(plotState=(CONTOURS_ON_DEF,))

# Change to the first frame of the third step.
# Remember that indices in Python begin with zero:
#   The index of the first frame is 0.
#   The index of the third step is 2.

myViewport.odbDisplay.setFrame(step=2, frame=0)

# Change the number of contour intervals to 10
# starting at 0.0 and ending at 0.10.

myViewport.odbDisplay.contourOptions.setValues(numIntervals=10,
    maxAutoCompute=OFF, maxValue=0.10,
    minAutoCompute=OFF, minValue=0.0,)

# Generate color output.
# Do not print the viewport decorations or the black background.

session.printOptions.setValues(rendition=COLOR,
    vpDecorations=OFF, vpBackground=OFF)

# Print the viewport to a local PNG-format file.

session.printToFile(fileName='contourPlot', format=PNG,
    canvasObjects=(myViewport,))
```

(printing-a-contour-plot-at-the-end-of-each-step)=

## Printing a contour plot at the end of each step

The following example script demonstrates how to produce and print a contour plot at the last frame of every step within an output database file. The example sets the appropriate contour limits so that all plots can be viewed within a fixed range.

Use the following command to retrieve the example script:

```sh
abaqus fetch job=viewerPrintContours
```

The script does the following:

- Defines the contour limits function.
- Determines the final frame of every step within an output database file.
- Produces a contour plot at the final frame of every step.
- Prints the contour plot to a file.

```python2
"""
viewerPrintContours.py

Print a set of contour plots to .png files.
"""

from abaqus import *
from abaqusConstants import *
import visualization

# Create a viewport for this example.

myViewport=session.Viewport(name=
    'Print contour plot after each step', origin=(10, 10),
    width=150, height=100)

# Open the output database and associate it with the viewport.
# Then set the plot state to CONTOURS_ON_DEF

try:
    myOdb = visualization.openOdb(path='viewer_tutorial.odb')

except (AbaqusException), value:
    print 'Error:', value

myViewport.setValues(displayedObject=myOdb)


myViewport.odbDisplay.display.setValues(plotState=(CONTOURS_ON_DEF,))

# Determine the number of steps in the output database.

mySteps = myOdb.steps
numSteps = len(mySteps)

# Set the maximum and minimum limits of the contour legend.

myViewport.odbDisplay.contourOptions.setValues(numIntervals=10,
    maxAutoCompute=OFF, maxValue=0.1,
    minAutoCompute=OFF, minValue=0.0)

# Establish print preferences.

session.printOptions.setValues(vpBackground=OFF)
session.psOptions.setValues(orientation=LANDSCAPE)
myViewport.viewportAnnotationOptions.setValues(
    triad=OFF,title=OFF,state=OFF)
myViewport.odbDisplay.basicOptions.setValues(
    coordSystemDisplay=OFF, )

# For each step, obtain the following:
#     1) The step key.
#     2) The number of frames in the step.
#     3) The increment number of the last frame in the step.
#

for i in range(numSteps):
    stepKey = mySteps.keys()[i]
    step = mySteps[stepKey]
    numFrames = len(step.frames)

#   Go to the last frame.
#   Display a contour plot.
#   Display the step description and the increment number.

    myViewport.odbDisplay.setFrame(step=i, frame=numFrames-1)
    myViewport.odbDisplay.display.setValues(plotState=(CONTOURS_ON_DEF,))

# Remove white space from the step key and use the result
# to name the file.

    fileName=stepKey.replace(' ','')

# Print the viewport to a file.

    session.printToFile(fileName, PNG, (myViewport,))
```
