import sys, os
# Execute only if in Python 3.x interpreter
if sys.version_info[0] > 2:
    # Check which folder the test are running from and then
    # add the `src` folder to PATH for testing. Also change
    # the work directory to `temp` to run Abaqus command in it.
    folder = os.path.basename(os.getcwd())
    if folder == 'temp':
        sys.path.insert(0,os.path.abspath('../../src'))
    elif folder == 'tests':
        sys.path.insert(0,os.path.abspath('../src'))
        os.chdir('temp')
    else:
        sys.path.insert(0,os.path.abspath('./src'))
        os.chdir('tests/temp')
    
    #This check is needed to run from `pytest` framework
    if sys.argv[0] != __file__:
        sys.argv.insert(0,__file__)

from abaqus import *
from abaqusConstants import *
from driverUtils import *
import numpy as np
try:
    import pytest # type: ignore
except ImportError:
    # define `pytest` to use in Abaqus interpreter
    # because it doesn't have a `pytest` module
    class pytest:
        @staticmethod
        def raises(error):
            class EnterExit:
                def __enter__(self):
                    pass
                def __exit__(self,typ,val,tb):
                    pass
            return EnterExit()


def test_odb():
    executeOnCaeStartup()

    # Open output database
    with pytest.raises(SystemExit):
        odb = session.openOdb('Job-1.odb')
    
        # Extract output data
        dataList = session.xyDataListFromField(odb=odb, outputPosition=NODAL,
                                               variable=(('U', NODAL, ((COMPONENT, 'U3'),)),),
                                               nodeSets=('INSTANCE.SET-TOP', ))
    
        data = np.array(dataList[0])
        if data.size > 0:
            np.savetxt('data.csv', data, header='time,U3', delimiter=',', comments='')

if sys.version_info[0] < 3: # run the test in Abaqus
    test_odb()