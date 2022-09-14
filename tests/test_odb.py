from abaqus import *
from abaqusConstants import *
from driverUtils import *
import visualization
import numpy as np
import pytest


def test_odb():
    executeOnCaeStartup()

    with pytest.raises(SystemExit):
        # Open output database
        odb = session.openOdb('Job-1.odb')
        
        # Show the output database in viewport
        session.viewports['Viewport: 1'].setValues(displayedObject=odb)
    
        # Extract output data
        dataList = session.xyDataListFromField(odb=odb, outputPosition=NODAL,
                                               variable=(('U', NODAL, ((COMPONENT, 'U3'),)),),
                                               nodeSets=('INSTANCE.SET-TOP', ))
    
        data = np.array(dataList[0])
        if data.size > 0:
            np.savetxt('data.csv', data, header='time,U3', delimiter=',', comments='')
