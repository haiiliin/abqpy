============================
Prompting the user for input
============================

You may want to request input from a user while an Abaqus Scripting Interface script is executing. There are many reasons for requesting input; for example, to specify design parameters, to enable a macro to take action based on the input received, or to force parts of the script to be repeated. The Abaqus Scripting Interface provides three functions that request input from the user and return the data entered by the user:

- The `getInput` function requests a single input from the user from a text field in a dialog box.

- The `getInputs` function requests multiple inputs from the user from text fields in a dialog box.

- The `getWarningReply` function requests a reply to a warning message from the user from a warning dialog box.

.. note::

    Note: You cannot use a script that contains getInput, getInputs or getWarningReply if you are running the script from the command line and passing the script name to the command line options -start,-replay or -noGUI.

