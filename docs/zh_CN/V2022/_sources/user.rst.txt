============
User's Guide
============

The Abaqus Scripting User's Guide takes you through the process of understanding the Python programming language and the Abaqus Scripting Interface so that you can write your own programs. It also describes how you use the Abaqus Scripting Interface and the C++ application programming interface (API) to access an Abaqus output database.

This guide is a part of the Abaqus® documentation collection, which describes all the capabilities of the Abaqus finite element analysis technology used in SIMULIA® applications.

The guide consists of the following sections:

- :doc:`user/about`

  - :doc:`user/about/interface`

    This section provides an overview of the Abaqus Scripting Interface and describes how Abaqus/CAE executes scripts.

  - :doc:`user/about/examples`

    Two simple examples are provided to introduce you to programming with the Abaqus Scripting Interface.

    - :doc:`user/about/examples/create-part` 
    - :doc:`user/about/examples/read-output`
    
- :doc:`user/python`

  - :doc:`user/python/introduction`

    This section is intended as a basic introduction to the Python programming language and is not an exhaustive description of the language. There are several books on the market that describe Python, and these books are listed as references. Additional resources, such as Python-related sites, are also listed.

  - :doc:`user/python/python-abaqus`

    This section describes the Abaqus Scripting Interface in more detail. The documentation style used in the command reference is explained, and important Abaqus Scripting Interface concepts such as data types and error handling are introduced.

  - :doc:`user/python/use-scripts`

    This section describes how you use the Abaqus Scripting Interface to control Abaqus/CAE models and analysis jobs. The Abaqus object model is introduced, along with techniques for specifying a region and reading messages from an analysis product (Abaqus/Standard or Abaqus/Explicit). You can skip this section of the guide if you are not working with Abaqus/CAE.

- :doc:`user/environment`

- :doc:`user/examples`

  This section provides a set of example scripts that lead you through the cantilever beam tutorial found in `Creating and Analyzing a Simple Model in Abaqus/CAE <https://help.3ds.com/2021/english/dssimulia_established/SIMACAEGSARefMap/simagsa-m-Caebeam-sb.htm?contextscope=all#simagsa-m-Caebeam-sb>`_. The following section is a basic tutorial for the experienced Abaqus user. It leads you through the Abaqus/CAE modeling process by visiting each of the modules and showing you the basic steps to create and analyze a simple model."). Additional examples are provided that read from an output database, display a contour plot, and print a contour plot from each step of the analysis. The final example illustrates how you can read from a model database created by Abaqus/CAE, parameterize the model, submit a set of analysis jobs, and generate results from the resulting output databases.

- :doc:`user/output`
  
  - :doc:`user/output/python`

    When you execute an analysis job, Abaqus/Standard and Abaqus/Explicit store the results of the analysis in an output database (.odb file) that can be viewed in the Visualization module of Abaqus/CAE or in Abaqus/Viewer. This section describes how you use the Abaqus Scripting Interface to access the data stored in an output database.

    You can do the following with the Abaqus Scripting Interface:

    - Read model data describing the geometry of the parts and the assembly; for example, nodal coordinates, element connectivity, and element type and shape.
    - Read model data describing the sections and materials and where they are used in an assembly.
    - Read field output data from selected steps, frames, and regions.
    - Read history output data.
    - Operate on field output and history output data.
    - Write model data, field output data, and history data to an existing output database or to a new output database.

  - :doc:`user/output/cpp`

    This section describes how you use the C++ language to access an application programming interface (API) to the data stored in an output database. The functionality of the C++ API is identical to the Abaqus Scripting Interface API; however, the interactive nature of the Abaqus Scripting Interface and its integration with Abaqus/CAE makes it easier to use and program. The C++ interface is aimed at experienced C++ programmers who want to bypass the Abaqus Scripting Interface for performance considerations. The C++ API offers faster access to the output database, although this is a consideration only if you need to access large amounts of data.

.. toctree::
   :maxdepth: 1
   :caption: Contents
   
   user/about
   user/python
   user/environment
   user/examples
   user/output
