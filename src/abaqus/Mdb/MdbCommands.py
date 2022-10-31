"""
Mdb commands
============
The following command upgrades a model database (.cae) to the current release and
writes the upgraded model database to a new file.

This page discusses:

* upgradeMdb
* CombineOptResults

"""
from typing import Union, Sequence

from abqpy.decorators import abaqus_function_doc
from typing_extensions import Literal

from .Mdb import Mdb
from ..UtilityAndView.abaqusConstants import INITIAL_AND_LAST, ALL, FIRST
from ..UtilityAndView.abaqusConstants import abaqusConstants as C


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
    optIter: Literal[C.INITIAL_AND_LAST, C.NONE, C.ALL, C.LAST, C.EVERY_NCYCLES, C.SPECIFY] = INITIAL_AND_LAST,
    nValues: Union[int, Sequence[int], Literal[C.ALL]] = ALL,
    models: Union[Sequence[str], Literal[C.ALL]] = ALL,
    steps: Union[Sequence[str], Literal[C.ALL]] = ALL,
    analysisFieldVariables: Union[Sequence[str], Literal[C.ALL]] = ALL,
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


@abaqus_function_doc
def openMdb(pathName: str) -> Mdb:
    """This method opens an existing model database file.

    .. note::
        This function can be accessed by::

            Mdb

    Parameters
    ----------
    pathName: str
        A String specifying the path to the model database file to open. If you do not provide a
        file extension, Abaqus/CAE attempts to open the file with .cae appended to the path.

    Returns
    -------
    Mdb
        A Mdb object

    Raises
    ------
    MdbError
        invalid model database;
        If the file is an invalid model database
    MdbError
        incompatible release number, expected *<Abaqus release>*, got *<earlier or later Abaqus release>*;
        If the file contains a model database from an Abaqus release other than the Abaqus
        release you are currently running
    MdbError
        cannot open file; may be in use by another CAE session;
        If the model database file is already opened in write mode
    MdbError
        cannot open file;
        If the command fails to open the model database file for reasons not mentioned above
    """
    return Mdb(pathName)
