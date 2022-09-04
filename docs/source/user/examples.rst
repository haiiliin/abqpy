============================================================
Putting it all Together: Abaqus Scripting Interface Examples
============================================================

The section provides examples that illustrate how you can combine Abaqus Scripting Interface commands and Python statements to create your own scripts. You can use the scripts to create Abaqus/CAE models, submit jobs for analysis, and view the results. For examples of scripts that read and write from an output database, see `Example scripts that access data from an output database <https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAECMDRefMap/simacmd-m-OdbIntroExamplesPyc-sb.htm?contextscope=all>`_.

The Abaqus/CAE example scripts in this section illustrate:

- How you can use commands from the Abaqus Scripting Interface to create a simple model, submit it for analysis, and view the results. :doc:`examples/cantilever` uses Abaqus Scripting Interface commands to reproduce the cantilever beam tutorial described in `Understanding Abaqus/CAE modules <https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEGSARefMap/simagsa-c-caebeammodel.htm?contextscope=all#simagsa-c-caebeammodel>`_.
- How you can use the Abaqus Scripting Interface to control the output from the Visualization module in Abaqus/CAE (Abaqus/Viewer).
  
  - :ref:`opening-the-tutorial-output-database` explains how to use **abaqus fetch** to retrieve the Abaqus/CAE tutorial output database.
  - :ref:`opening-an-output-database-and-displaying-a-contour-plot` explains how to open the tutorial output database, display a contour plot, and print the resulting viewport to a file.
  - :ref:`printing-a-contour-plot-at-the-end-of-each-step` explains how to open the tutorial output database, customize the legend, display a contour plot at the end of each step, and print the resulting viewports to a file.
- How you can introduce more complex programming techniques into your Abaqus Scripting Interface scripts. :doc:`examples/sensitivity` reproduces the problem found in :doc:`examples/sensitivity`. You use Abaqus/CAE to create the model, and you use Abaqus Scripting Interface commands to parameterize an evaluation of the model by changing its geometry and element type. The example investigates the sensitivity of the shell elements in Abaqus to skew distortion when they are used as thin plates.
- How you can use functions available in the caePrefsAccess module to edit the display preferences and GUI settings in the abaqus_2021.gpr file. :doc:`examples/settings` describes how to query for and set several default display and GUI behaviors in Abaqus/CAE.

The example scripts from this guide can be copied to the user's working directory by using the Abaqus **fetch** utility:

.. code-block:: sh

    abaqus fetch job=scriptName

where **scriptName.py** is the name of the script (see `Fetching sample input files <https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEEXCRefMap/simaexc-c-fetchproc.htm?contextscope=all>`_).

.. toctree::
    :maxdepth: 1
    :caption: Contents

    examples/cantilever
    examples/plot
    examples/sensitivity
    examples/settings