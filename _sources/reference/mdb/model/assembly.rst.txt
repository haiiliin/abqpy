========
Assembly
========

Features in Abaqus/CAE include Parts, Datums, Partitions, and Assembly operations. Assembly commands create Feature objects on only the rootAssembly object. The commands that create Feature objects on only the Part object are described in Part commands. The commands that create Feature objects on both the Part and the rootAssembly objects are described in Feature commands.


Create instances
----------------

.. autoclass:: abaqus.Assembly.AssemblyModel.AssemblyModel
    :members:


Object features
---------------

Assembly
~~~~~~~~

.. autoclass:: abaqus.Assembly.Assembly.Assembly
    :members:

    .. autoclassdoc::

    .. autoclasstoc::

ConnectorOrientation
~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Assembly.ConnectorOrientation.ConnectorOrientation
    :members:

    .. autoclassdoc::

ConnectorOrientationArray
~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Assembly.ConnectorOrientationArray.ConnectorOrientationArray
    :members:

    .. autoclassdoc::

Feature
~~~~~~~

.. autoclass:: abaqus.Assembly.Feature.Feature
    :members:

    .. autoclassdoc::

ModelInstance
~~~~~~~~~~~~~

.. autoclass:: abaqus.Model.Model.ModelInstance
    :members:

    .. autoclassdoc::

PartInstance
~~~~~~~~~~~~

.. autoclass:: abaqus.Assembly.PartInstance.PartInstance
    :members:

    .. autoclassdoc::

PartInstanceArray
~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Assembly.PartInstanceArray.PartInstanceArray
    :members:

    .. autoclassdoc::

