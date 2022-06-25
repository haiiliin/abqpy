"""The Highlight commands are used to highlight objects in the current viewport and to
remove the highlighting. 

"""


def highlight(object: str):
    """This method highlights an object in the current viewport.

    .. note:: 
            This function can be accessed by:

            .. code-block:: python

                highlight

    Parameters
    ----------
    object
        An object specifying the object in the current viewport to be highlighted. You can
        specify only a single object. Abaqus/CAE highlights only the edges of a face when
        highlighting a surface and a face together. The following objects are supported:
        **For the MDB**
            - ConstrainedSketchVertex
            - Edge
            - Face
            - Surface
            - Cell
            - Node
            - Element
            - Element face
            - Element edge
            - Feature
            - Datum
            - Instance
            - Set
            - Load
            - Boundary condition
            - Predefined field
            - Display group
        **For the ODB**
            - Node
            - Element
            - Display group

    Returns
    -------
    """
    pass


def unhighlight(object: str):
    """This method removes highlighting from an object in the current viewport.

    .. note:: 
            This function can be accessed by:

            .. code-block:: python

                unhighlight

    Parameters
    ----------
    object
        An object specifying the object in the current viewport from which the highlighting will
        be removed. You can specify only a single object. See highlight for a list of supported
        objects.

    Returns
    -------
    """
    pass
