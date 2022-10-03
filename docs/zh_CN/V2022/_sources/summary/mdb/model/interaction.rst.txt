===========
Interaction
===========

A specific type of interaction object and a specific type of interaction state object are designed for each type of interaction. An interaction object stores the non-propagating data of an interaction as well as a number of instances of the corresponding interaction state object, each of which stores the propagating data of the interaction in a single step. Instances of the interaction state object are created and deleted internally by its corresponding interaction object.

Create interactions
-------------------

.. autoclass:: abaqus.Interaction.InteractionModel.InteractionModel
    :noindex:

    .. autoclasstoc::

.. This is a comment ro supress the warning "(ERROR/3) Document may not end with a transition."
