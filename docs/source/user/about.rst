====================================
About the Abaqus Scripting Interface
====================================

The Abaqus Scripting Interface is an application programming interface (API) to the models and data used by Abaqus. The Abaqus Scripting Interface is an extension of the Python object-oriented programming language; Abaqus Scripting Interface scripts are Python scripts. You can use the Abaqus Scripting Interface to do the following:

- Create and modify the components of an Abaqus model, such as parts, materials, loads, and steps. 
- Create, modify, and submit Abaqus analysis jobs.
- Read from and write to an Abaqus output database.
- View the results of an analysis.
    

You use the Abaqus Scripting Interface to access the functionality of Abaqus/CAE from scripts (or programs). (The Visualization module of Abaqus/CAE is also licensed separately as Abaqus/Viewer; therefore, the Abaqus Scripting Interface can also be used to access the functionality of Abaqus/Viewer.) Because the Abaqus Scripting Interface is a customized extension of standard Python, further extension of Abaqus base types to create user-defined classes is not allowed.

This section provides an introduction to the Abaqus Scripting Interface.

.. toctree::
   :maxdepth: 1
   :caption: Contents
   
   about/interface
   about/interact
   about/examples