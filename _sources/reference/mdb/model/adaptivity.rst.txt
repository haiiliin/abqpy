==========
Adaptivity
==========

The Adaptivity commands are used to define objects, perform analyses, and calculate new meshes for Arbitrary Lagrangian Eularian (ALE) adaptive smoothing (adaptive meshing) and varying topology adaptivity (adaptive remeshing).


Create adaptivity mesh control features
---------------------------------------

.. autoclass:: abaqus.Adaptivity.AdaptivityModel.AdaptivityModel
    :members:


Create adaptivity mesh state features
-------------------------------------

.. autoclass:: abaqus.Adaptivity.AdaptivityStep.AdaptivityStep
    :members:


Create features for AdaptivityIteration
---------------------------------------

.. autoclass:: abaqus.Adaptivity.RuleResult.RuleResult
    :members:


Object Features
---------------

AdaptiveMeshConstraint
~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Adaptivity.AdaptiveMeshConstraint.AdaptiveMeshConstraint
    :members:
    
AdaptiveMeshConstraintState
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Adaptivity.AdaptiveMeshConstraintState.AdaptiveMeshConstraintState
    :members:
    

AdaptiveMeshControl
~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Adaptivity.AdaptiveMeshControl.AdaptiveMeshControl
    :members:

AdaptiveMeshDomain
~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Adaptivity.AdaptiveMeshDomain.AdaptiveMeshDomain
    :members:

AdaptivityIteration
~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Adaptivity.AdaptivityIteration.AdaptivityIteration
    :members:

AdaptivityProcess
~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Adaptivity.AdaptivityProcess.AdaptivityProcess
    :members:

DisplacementAdaptiveMeshConstraint
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Adaptivity.DisplacementAdaptiveMeshConstraint.DisplacementAdaptiveMeshConstraint
    :members:

DisplacementAdaptiveMeshConstraintState
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Adaptivity.DisplacementAdaptiveMeshConstraintState.DisplacementAdaptiveMeshConstraintState
    :members:

ErrorIndicatorResult
~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Adaptivity.ErrorIndicatorResult.ErrorIndicatorResult
    :members:

RemeshingRule
~~~~~~~~~~~~~

.. autoclass:: abaqus.Adaptivity.RemeshingRule.RemeshingRule
    :members:

RuleResult
~~~~~~~~~~
    
.. autoclass:: abaqus.Adaptivity.RuleResult.RuleResult
    :members:

VelocityAdaptiveMeshConstraint
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Adaptivity.VelocityAdaptiveMeshConstraint.VelocityAdaptiveMeshConstraint
    :members:

VelocityAdaptiveMeshConstraintState
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Adaptivity.VelocityAdaptiveMeshConstraintState.VelocityAdaptiveMeshConstraintState
    :members:
