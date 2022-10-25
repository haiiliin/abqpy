"""
Compression Output Script
=========================

A script to get the output of the compression model.
"""

from abaqus import *
from abaqusConstants import *
from driverUtils import *
import visualization
import numpy as np

executeOnCaeStartup()

# Open output database
odb = session.openOdb('Job-1.odb')

# Show the output database in viewport
session.viewports['Viewport: 1'].setValues(displayedObject=odb)

# Extract output data
dataList = session.xyDataListFromField(odb=odb, outputPosition=NODAL, 
                                       variable=(('U', NODAL, ((COMPONENT, 'U3'),)),),
                                       nodeSets=('INSTANCE.SET-TOP', ))

data = np.array(dataList[0])
np.savetxt('data.csv', data, header='time,U3', delimiter=',', comments='')
