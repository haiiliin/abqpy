"""The following commands are used to request data entry from a user."""
from typing import overload

from abqpy.decorators import abaqus_function_doc


@abaqus_function_doc
@overload
def getInput(prompt: str, default: str = ""):
    r"""This method is used to obtain a single input from a user from a dialog box. The method displays a modal
    dialog box with a text field prefaced by the specified label. The user enters data in the text field or
    accepts the optional default value that is displayed in the text field. When the user clicks the OK button,
    the getInput method reads the data from the dialog box and closes the dialog box. You can use a \t separator
    in the label argument to provide a tooltip from the dialog box; for example::

        getInput('Enter a number:\tEnter the number of nodes to delete')

    .. note::
        You cannot use a script that contains getInput if you are running the script from
        the command line and passing the script name to the command line options **-start**,
        **-script**, **-replay**, or **-noGUI**.

    .. note::
        This function can be accessed by::

            getInput

    Parameters
    ----------
    prompt
        A String specifying the text field in the dialog box.
    default
        A String specifying a default value to be displayed in the text field in the dialog box.

    Returns
    -------
    str
        A String or None if the user clicks Cancel.
    """
    ...


@abaqus_function_doc
@overload
def getInput(fields: tuple, label: str = "", dialogTitle: str = ""):
    """This method is used to obtain multiple inputs from a user from a dialog box. The method
    displays a modal dialog box with a column of text fields prefaced by the specified
    labels. The user enters data in the text fields or accepts the optional default values
    that are displayed in the text field. When the user clicks the OK button, the getInputs
    method reads the data from the dialog box and closes the dialog box.
    Note:You cannot use a script that contains getInputs if you are running the script from
    the command line and passing the script name to the command line options **-start**,
    **-script**, **-replay**, or **-noGUI**.

    .. note::
        This function can be accessed by::

            getInputs

    Parameters
    ----------
    fields
        A sequence of sequence of Strings specifying the text fields in the dialog box. Each
        inner sequence is a pair of Strings specifying a label that describes a text field along
        with a default value that appears in the text field. If the field has no default value,
        you should enter an empty string in the second string in the pair.
    label
        A String specifying a label to be placed at the top of the dialog box. The default is an
        empty string, indicating that no label will be shown.
    dialogTitle
        A String specifying the text to be shown in the title bar of the dialog box. The default
        is Get Inputs.

    Returns
    -------
    Sequence[str]
        A sequence of Strings representing the data in each of the text fields in the dialog
        box. If the user clicks the Cancel button, the method returns a sequence of None
        objects.
    """
    ...


@abaqus_function_doc
def getInput(*args, **kwargs):
    ...


@abaqus_function_doc
def getWarningReply(message: str, buttons: str):
    r"""This method is used to obtain a reply from a user from a warning dialog box. The method displays a modal
    warning dialog box with a message and standard buttons. The user clicks the one of the standard buttons, the
    getWarningReply returns the corresponding button value and closes the dialog box. You can use a separator in
    the message argument to provide a multi-line message in the warning dialog box; for example::

        from abaqus import *
        getWarningReply('Out of disk space!\nOkay to continue', (YES, NO))

    .. note::
        You cannot use a script that contains getWarningReply if you are running the script
        from the command line and passing the script name to the command line options
        **-start**, **-script**, **-replay**, or **-noGUI**.

    .. note::
        This function can be accessed by::

            getWarningReply

    Parameters
    ----------
    message
        A String specifying the message in the warning dialog box.
    buttons
        A Sequence of standard buttons to be displayed in the warning dialog box. Permissible
        values are YES, NO, YES_TO_ALL and CANCEL.

    Returns
    -------
    The button that the user clicks.
    """
    ...
