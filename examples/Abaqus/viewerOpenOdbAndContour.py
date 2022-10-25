"""
Open Odb and Display a Contour Plot
===================================

`viewerOpenOdbAndContour.py` from `Opening an output database and displaying a contour plot <https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAECMDRefMap/simacmd-c-intexaopenodb.htm?contextscope=all&id=0d282d5c2d004c5d9f115b9e7853cacf>`_.

Print a contour plot to a local PNG-format file.

Run the following command before running this script:

.. code-block:: sh

    abaqus fetch job=viewer_tutorial

The following example of a script containing Abaqus Scripting Interface commands uses the output database used by `Viewing the Output from Your Analysis <https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEGSARefMap/simagsa-m-Caevismod-sb.htm?contextscope=all#simagsa-m-Caevismod-sb>`_.

Use the following command to retrieve the example script:

.. code-block:: sh

    abaqus fetch job=viewerOpenOdbAndContour

The script does the following:

- Creates a viewport, and makes it the current viewport.
- Opens an output database.
- Displays a contour plot.
- Displays the model in the first frame of the third step.
- Sets the number of contour intervals and the contour limits.
- Prints a color image of the viewport to a .png file.
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
