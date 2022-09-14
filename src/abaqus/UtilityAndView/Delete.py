from abqpy.decorators import abaqus_function_doc
from ..UtilityAndView.abaqusConstants import *

"""The deleteObjectCallback module provides methods that allow you to register a callback 
that will be invoked when specified Abaqus Scripting Interface objects are about to be 
deleted. This callback allows you to examine an object before it is deleted. 
For example, in the following script the myCallback function is executed when any Job 
object is about to be deleted::

    import deleteObjectCallback
    
    def myCallback(path, userData): 
        print 'About to delete', path 
    deleteObjectCallback.addCallback(path='mdb.jobs[*]') 

.. note:: 
    This object can be accessed by::

        import deleteObjectCallback

"""


@abaqus_function_doc
def deleteObjectCallback(
    callback: str, path: str, userData: str = None, includeChildren: Boolean = False
):
    """This method adds a callback function that will be invoked when the specified Abaqus
    Scripting Interface objects are about to be deleted. The callback is invoked only when
    the object is deleted using the Python statement del object. The callback is not invoked
    when the object is deleted using an Abaqus Scripting Interface command such as
    mdb.models[name].parts[name].deleteFeature().

    .. note:: 
        This function can be accessed by::

            deleteObjectCallback.addCallback

    Parameters
    ----------
    callback
        A Python function to be called when an object matching the specified path is about to be
        deleted. The interface definition of the callback function is `def
        functionName(objectPath, userData)` where **objectPath** is the path to the object about to
        be deleted. **userData** is the object passed as the **userData** argument to the addCallback
        method.
    path
        A String specifying the path to an object or the SymbolicConstant ANY. You can include
        wildcards in the path to specify a pattern to be matched. Examples of valid paths
        are  `path='mdb.models[*]' path="mdb.models['Axle*'].parts[*]"`, and
        `path='mdb.models[*].materials[*]'`
    userData
        Any type of data. This data will be passed to the callback function. The default value
        is None.
    includeChildren
        A Boolean specifying that the callback should be called if an object owned by the object
        specified by the **path** argument is about to be deleted. The default value is False.
    """
    ...
