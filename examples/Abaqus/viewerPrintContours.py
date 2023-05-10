"""
Print Contour Plots
===================

`viewerPrintContours.py` from `Printing a contour plot at the end of each step <https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAECMDRefMap/simacmd-c-intexaprintcontour.htm?contextscope=all&id=01196185741b4c25ae212a9cc00dc138>`_.

Print a set of contour plots to .png files.

Run the following command before running this script:

.. code-block:: sh

    abaqus fetch job=viewer_tutorial

The following example script demonstrates how to produce and print a contour plot at the last frame of every step within an output database file. The example sets the appropriate contour limits so that all plots can be viewed within a fixed range.

Use the following command to retrieve the example script:

.. code-block:: sh

    abaqus fetch job=viewerPrintContours

The script does the following:

- Defines the contour limits function.
- Determines the final frame of every step within an output database file.
- Produces a contour plot at the final frame of every step.
- Prints the contour plot to a file.
"""

import visualization
from abaqus import *
from abaqusConstants import *

# Create a viewport for this example.

myViewport = session.Viewport(name="Print contour plot after each step", origin=(10, 10), width=150, height=100)

# Open the output database and associate it with the viewport.
# Then set the plot state to CONTOURS_ON_DEF

try:
    myOdb = visualization.openOdb(path="viewer_tutorial.odb")

except Exception as e:
    print("Error:", e)

myViewport.setValues(displayedObject=myOdb)


myViewport.odbDisplay.display.setValues(plotState=(CONTOURS_ON_DEF,))

# Determine the number of steps in the output database.

mySteps = myOdb.steps
numSteps = len(mySteps)

# Set the maximum and minimum limits of the contour legend.

myViewport.odbDisplay.contourOptions.setValues(
    numIntervals=10, maxAutoCompute=OFF, maxValue=0.1, minAutoCompute=OFF, minValue=0.0
)

# Establish print preferences.

session.printOptions.setValues(vpBackground=OFF)
session.psOptions.setValues(orientation=LANDSCAPE)
myViewport.viewportAnnotationOptions.setValues(triad=OFF, title=OFF, state=OFF)
myViewport.odbDisplay.basicOptions.setValues(
    coordSystemDisplay=OFF,
)

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

    myViewport.odbDisplay.setFrame(step=i, frame=numFrames - 1)
    myViewport.odbDisplay.display.setValues(plotState=(CONTOURS_ON_DEF,))

    # Remove white space from the step key and use the result
    # to name the file.

    fileName = stepKey.replace(" ", "")

    # Print the viewport to a file.

    session.printToFile(fileName, PNG, (myViewport,))
