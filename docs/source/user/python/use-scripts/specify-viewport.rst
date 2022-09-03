============================================
Specifying what is displayed in the viewport
============================================

While a script is running and moving between models, modules, parts, and assemblies, you can control the contents of specified viewports. The contents can be one of the following:

- A part
- The assembly
- A sketch
- Data from an output database
- An X–Y plot
- Empty

n some cases you will want to update the contents of the viewport as the model changes; for example, to illustrate how the assembly was partitioned prior to meshing. However, frequent updates to a viewport will slow down your script, and you may want to leave the viewport empty until the script has completed. Alternatively, you can display an object that the script is not operating on; for example, you can display a part while the script operates on the assembly.

You use the following command to change the contents of a specified viewport:

.. code-block:: python2

    session.viewports[name].setValues(displayedObject=object)

The displayedObject argument can be a Part, Assembly, Sketch, Odb, or XYPlot object or `None`. If displayedObject=None, Abaqus/CAE displays an empty viewport. For more information, see `setValues(...)`.
