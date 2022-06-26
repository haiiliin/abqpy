====
Part
====

Features in Abaqus/CAE include Parts, Datums, Partitions, and Assembly operations. Part commands create Feature objects on only the Part object. The commands that create Feature objects on only the rootAssembly object are described in Assembly commands. The commands that create Feature objects on both the Part and the rootAssembly objects are described in Feature commands.


Create parts
------------

.. autoclass:: abaqus.Part.PartModel.PartModel
    :members:

.. autoclass:: abaqus.Part.PartBase.PartBase
    :members:

Object features
---------------

Part
~~~~

.. autoclass:: abaqus.Part.Part.Part
    :members:
    :inherited-members:

    .. autoclassdoc::

AcisFile
~~~~~~~~

.. autoclass:: abaqus.Part.AcisFile.AcisFile
    :members:

    .. autoclassdoc::

AcisMdb
~~~~~~~

.. autoclass:: abaqus.Part.AcisMdb.AcisMdb
    :members:

    .. autoclassdoc::

Feature
~~~~~~~

.. autoclass:: abaqus.Part.Feature.Feature
    :members:

    .. autoclassdoc::