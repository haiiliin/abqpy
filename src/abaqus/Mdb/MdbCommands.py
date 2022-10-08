"""
Mdb commands
============
The following command upgrades a model database (.cae) to the current release and
writes the upgraded model database to a new file.

This page discusses:

* upgradeMdb
* CombineOptResults

"""
from typing import Union, Tuple
from typing_extensions import Literal
from ..UtilityAndView.abaqusConstants import abaqusConstants as C
from ..UtilityAndView.abaqusConstants import INITIAL_AND_LAST, ALL, FIRST


def upgradeMdb(existingMdbPath: str, upgradedMdbPath: str) -> None:
    """
    This method upgrades an existing Mdb object to the current release and writes the
    upgraded version of the Mdb object to a file. In addition, Abaqus/CAE writes
    information about the status of the upgrade to the log file ( upgradedMdbPath.log
    ).
    
    Parameters
    ----------
    existingMdbPath : str
        A String specifying the path to the file containing the model database to be
        upgraded.
    upgradedMdbPath : str
        A String specifying the path to the file that will contain the upgraded model
        database.
    
    Raises
    ------
    MdbError
        Cannot convert file
    """
    ...


def CombineOptResults(
    optResultLocation: str,
    optIter: Literal[
        C.INITIAL_AND_LAST, C.NONE, C.ALL, C.LAST, C.EVERY_NCYCLES, C.SPECIFY
    ] = INITIAL_AND_LAST,
    nValues: Union[int, Tuple[int, ...], Literal[C.ALL]] = ALL,
    models: Union[Tuple[str, ...], Literal[C.ALL]] = ALL,
    steps: Union[Tuple[str, ...], Literal[C.ALL]] = ALL,
    analysisFieldVariables: Union[Tuple[str, ...], Literal[C.ALL]] = ALL,
    includeResultsFrom: Literal[C.ORIGINAL_MODEL, C.FIRST, C.LAST] = FIRST,
    originalModel: str = ...,
) -> None:
    """   
    This method combines the results from existing ODB files for each optimization
    cycle and writes a merged ODB file.
    
    Parameters
    ----------
    optResultLocation : str
        A String specifying the path to the folder in which optimization results are present.
    optIter
        A Symbolic Constant to specify the optimization cycles from which the results
        should be merged. The possible values are INITIAL_AND_LAST, NONE, ALL, LAST,
        EVERY_NCYCLES, SPECIFY. The default value is INITIAL_AND_LAST.
    nValues
        An Int or a tuple of Ints specifying the optimization cycles from which the
        results should be merged. This argument is used only when EVERY_NCYCLES or
        SPECIFY is selected for optIter. The default value is ALL.
    models
        A tuple of strings specifying the list of models for which the merging of
        results is performed. The default value is ALL.
    steps
        A tuple of strings specifying the list of steps from the selected models to
        be included in the odb merge. The default value is ALL.
    analysisFieldVariables
        A tuple of strings specifying the list of analysisFieldVariables to be
        included in the odb merge. The default value is ALL.
    includeResultsFrom
       A Symbolic Constant to specify the target odb to which the results will be
       merged. The possible values are ORIGINAL_MODEL, FIRST or LAST. The default
       value is FIRST.
    originalModel
        A String to specify the path of target odb if includeResultsFrom is set to
        ORIGINAL_MODEL.
    """
    ...
