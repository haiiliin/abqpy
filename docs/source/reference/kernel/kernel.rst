=============
Custom Kernel
=============


The customKernel module augments the mdb, odb, and session objects with an object called customData. The customData object can contain custom data that you created using standard Python objects; for example, dictionaries, strings, numbers, and classes. In addition, the customData object can contain objects that you created using the classes described in this section.

All objects that you create under the mdb.customData and odb[odbName].customData object will be stored in the Abaqus/CAE model and output database, respectively, when you save the database; all objects that you create under the session.customData object will be lost when you exit Abaqus/CAE.

The customData object is an instance of the RepositorySupport class; for more information, see RepositorySupport. The classes described in this section register with the GUI infrastructure when you create the class. As a result, if you write a custom GUI script, you can query these objects from the GUI, and you can also be notified when the contents of these objects change so you can update the GUI accordingly. For more information, see Extending the Abaqus Scripting Interface and Accessing kernel data from the GUI.


Object features
---------------

CommandRegister
~~~~~~~~~~~~~~~

.. autoclass:: abaqus.CustomKernel.CommandRegister.CommandRegister
    :members:
    :special-members: __init__

    .. autoclasstoc::

RegisteredDictionary
~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.CustomKernel.RegisteredDictionary.RegisteredDictionary
    :members:
    :special-members: __init__

    .. autoclasstoc::

RegisteredList
~~~~~~~~~~~~~~

.. autoclass:: abaqus.CustomKernel.RegisteredList.RegisteredList
    :members:
    :special-members: __init__

    .. autoclasstoc::

RegisteredTuple
~~~~~~~~~~~~~~~

.. autoclass:: abaqus.CustomKernel.RegisteredTuple.RegisteredTuple
    :members:
    :special-members: __init__

    .. autoclasstoc::

RepositorySupport
~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.CustomKernel.RepositorySupport.RepositorySupport
    :members:
    :special-members: __init__