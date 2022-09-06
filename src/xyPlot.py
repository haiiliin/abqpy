from typing import List
from abaqus.XY.AreaStyle import AreaStyle
from abaqus.XY.LineStyle import LineStyle
from abaqus.XY.QuantityType import QuantityType
from abaqus.XY.SymbolStyle import SymbolStyle
from abaqus.XY.TextStyle import TextStyle
from abaqus.XY.XYData import XYData
from abaqus.XY.XYSession import XYSession

# TODO: signature for these functions, see if it is really necessary

def XYDataFromFile() -> XYData:
    ...
def XYDataFromFreeBody() -> List[XYData]:
    ...
def XYDataFromHistory() -> XYData:
    ...
def XYDataFromPath() -> XYData:
    ...
def XYDataFromShellThickness() -> List[XYData]:
    ...
def xyDataListFromField() -> List[XYData]:
    ...