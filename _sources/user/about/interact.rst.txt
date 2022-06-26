=================================================================
How does the Abaqus Scripting Interface interact with Abaqus/CAE?
=================================================================

:numref:`acl-all-schematic-nls-1` illustrates how Abaqus Scripting Interface commands interact with the Abaqus/CAE kernel.

.. _acl-all-schematic-nls-1:
.. figure:: /images/acl-all-schematic-nls.png
    :width: 50%
    :align: center
    
    Abaqus Scripting Interface commands and Abaqus/CAE.

The Abaqus Scripting Interface allows you to bypass the Abaqus/CAE GUI and communicate directly with the kernel. A file containing Abaqus Scripting Interface commands is called a script. You can use scripts to do the following:

- To automate repetitive tasks. For example, you can create a script that executes when a user starts an Abaqus/CAE session. Such a script might be used to generate a library of standard materials. As a result, when the user enters the Property module, these materials will be available. Similarly, the script might be used to create remote queues for running analysis jobs, and these queues will be available in the Job module.
    
- To perform a parametric study. For example, you can create a script that incrementally modifies the geometry of a part and analyzes the resulting model. The same script can read the resulting output databases, display the results, and generate annotated hard copies from each analysis.
    
- Create and modify the model databases and models that are created interactively when you work with Abaqus/CAE. The Abaqus Scripting Interface is an application programming interface (API) to your model databases and models. For a discussion of model databases and models, see `What is an Abaqus/CAE model database? <https://help.3ds.com/2021/english/dssimulia_established/SIMACAECAERefMap/simacae-c-dbsconcepts.htm?contextscope=all>`_ and `What is an Abaqus/CAE model? <https://help.3ds.com/2021/english/dssimulia_established/SIMACAECAERefMap/simacae-m-DbsConcWhatismodel-sb.htm?contextscope=all>`_ "This section describes an Abaqus/CAE model".
    
- Access the data in an output database. For example, you may wish to do your own postprocessing of analysis results. You can write your own data to an output database and use the Visualization module of Abaqus/CAE to view its contents.
    

The Abaqus Scripting Interface is an extension of the popular object-oriented language called Python. Any discussion of the Abaqus Scripting Interface applies equally to Python in general, and the Abaqus Scripting Interface uses the syntax and operators required by Python.