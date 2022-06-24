===============================
Continuation lines and comments
===============================

You can continue a statement on the following line if you break the statement between a set of (), {}, or [] delimiters. For example, look at the tuple that was used in :doc:`user/about/examples/creat-part`_ to assign the coordinates of the vertices to a variable:

.. code-block:: python

    xyCoordsOuter = ((-10, 30), (10, 30), (40, -30), 
        (30, -30), (20, -10), (-20, -10), 
        (-30, -30), (-40, -30), (-10, 30))

If a statement breaks at any other place, you must include a \\ character at the end of the line to indicate that it is continued on the next line. For example,

.. code-block:: python

    distance = mdb.models['Model-1'].parts['housing'].\
        getDistance(entity1=node1, entity2=node2)

When you are running Python from a local Linux or Windows window, the prompt changes to the . . . characters to indicate that you are on a continuation line.
Comments in a Python script begin with the # character and continue to the end of the line.

.. code-block:: python

    >>> # Define material constants
    >>> modulus = 1e6 # Define Young's modulus