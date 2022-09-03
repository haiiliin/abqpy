=================
Executing scripts
=================

You have seen how to execute Python statements from the stand-alone Python interpreter. If your script does not access the functionality of Abaqus/CAE, you can run the script by typing `abaqus python scriptname.py` at the system prompt. Abaqus will run the script through the Python interpreter and return you to the system prompt.

If your script accesses the functionality of any of the Abaqus/CAE modules, the statements must be interpreted by the Abaqus/CAE kernel; you cannot run the script from the Python interpreter invoked from the system prompt. You must execute the script in Abaqus/CAE by selecting **File -> Run Script** from the main menu bar and selecting the file to execute. In addition, the script must contain the following statements:

.. code-block:: python2

    from abaqus import * 
    from abaqusConstants import *

If your script accesses and manipulates data in an output database, you can execute the script using either of the methods already described:

Type `abaqus python scriptname.py` at the system prompt. The script must contain the following statement:

.. code-block:: python2

    from odbAccess import *

Select FileRun Script from the Abaqus/CAE main menu bar, and select the file to execute. The script must contain the following statement:

.. code-block:: python2

    from visualization import *

When you run a script in Abaqus/CAE from the CLI, as part of a macro, or from the **File -> Run Script** menu option, Abaqus/CAE displays a stop button that you can use to stop a script that has been running for a predefined duration. If you want to display this button for scripts run using other methods, execute the `showStopButtonInGui` command from the `abaqus` module before you run the script. The command is not issued automatically when a script is run from the user interface; for example, as part of a plug-in.