from typing import 

from abqpy.decorators import abaqus_function_doc

"""These functions display status information. 

"""


@abaqus_function_doc
@overload
def milestone(message: str):
    """This function displays a string in the prompt area.

    .. note:: 
        This function can be accessed by::

            milestone

    Parameters
    ----------
    message
        A String specifying the text to display.
    """
    ...


@abaqus_function_doc
@overload
def milestone(message: str, percent: int):
    """This function displays a percentage complete message in the prompt area.

    .. note:: 
        This function can be accessed by::

            milestone

    Parameters
    ----------
    message
        A String specifying the text to display.
    percent
        An Int specifying the percentage complete.
    """
    ...


@abaqus_function_doc
@overload
def milestone(message: str, object: str, done: int, total: int):
    """This function displays a message in the prompt area indicating the number done out of a
    total. The form of the message is `operation: object nn out of nn`

    .. note:: 
        This function can be accessed by::

            milestone

    Parameters
    ----------
    message
        A String specifying the operation.
    object
        A String specifying the object.
    done
        An Int specifying the number being processed.
    total
        An Int specifying the total number.
    """
    ...


@abaqus_function_doc
def milestone(*args, **kwargs):
    ...
