from abaqus import *
from abaqusConstants import *
from driverUtils import *
import numpy as np

executeOnCaeStartup()

# Open output database
odb = session.openOdb('Job-1.odb')

# Extract output data
dataList = session.xyDataListFromField(odb=odb, outputPosition=NODAL, 
                                       variable=(('U', NODAL, ((COMPONENT, 'U3'),)),),
                                       nodeSets=('INSTANCE.SET-TOP', ))

data = np.array(dataList[0])
np.savetxt('data.csv', data, header='time,U3', delimiter=',', comments='')
