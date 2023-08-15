import visualization
from abaqus import *
from abaqusConstants import *
from driverUtils import *


def test_odb():
    executeOnCaeStartup()

    # Open output database
    odb = session.openOdb("Job-1.odb")

    # Show the output database in viewport
    session.viewports["Viewport: 1"].setValues(displayedObject=odb)

    # Extract output data
    dataList = session.xyDataListFromField(
        odb=odb, outputPosition=NODAL, variable=(("U", NODAL, ((COMPONENT, "U3"),)),), nodeSets=("INSTANCE.SET-TOP",)
    )
