"""The Highlight commands are used to highlight objects in the current viewport and to remove the
highlighting."""
from abqpy.decorators import abaqus_function_doc


@abaqus_function_doc
def highlight(object):
    """This method highlights an object in the current viewport.

    .. note::
        This function can be accessed by::

            highlight

    Parameters
    ----------
    object
        An object specifying the object in the current viewport to be highlighted. You can
        specify only a single object. Abaqus/CAE highlights only the edges of a face when
        highlighting a surface and a face together. The following objects are supported:

        - **For the MDB**

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
        - **For the ODB**

            - Node
            - Element
            - Display group

    Returns
    -------
    """
    # TODO: Implement this method.
    ...


@abaqus_function_doc
def unhighlight(object):
    """This method removes highlighting from an object in the current viewport.

    .. note::
        This function can be accessed by::

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
    # TODO: Implement this method.
    ...
