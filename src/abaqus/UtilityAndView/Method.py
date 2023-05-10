from typing import Optional

from abqpy.decorators import abaqus_function_doc

from ..UtilityAndView.abaqusConstants import OFF, Boolean

"""The methodCallback module provides functions that allow you to register a callback that 
will be invoked when certain Abaqus Scripting Interface commands are about to be 
executed. This callback allows you to augment the standard behavior of Abaqus Scripting 
Interface commands. 
For example, in the following script the myCallback function is executed when the 
writeInput method of an object whose type is JobType (in other words, any Job object) is 
about to be called::

    import methodCallback 
    from job import JobType 
    
    def myCallback(callingObject, arguments, keywordArguments, userData): 
        print 'An input file  is about to be written.' 
    methodCallback.addCallback(JobType, 'writeInput', myCallback) 

.. note:: 
    This object can be accessed by::

        import methodCallback

"""


@abaqus_function_doc
def addCallback(
    caller: str,
    methodName: str,
    callback: str,
    userData: Optional[str] = None,
    callAfter: Boolean = OFF,
):
    """This method adds a callback function that will be invoked when certain Abaqus/CAE commands are about to
    be executed.

    .. note::
        This function can be accessed by::

            methodCallback.addCallback

    Parameters
    ----------
    caller
        An object or type object specifying which object will trigger the callback function to
        be invoked or the Symbolic Constant ALL_TYPES.
    methodName
        A String specifying the name of the method on the caller that will trigger the callback
        function to be invoked or the Symbolic Constant ALL_METHODS.
    callback
        A Python function to be called when a command matching the specified caller and method
        name is about to be executed. The interface definition of the callback function is `def
        functionName(callingMethod, args, keywordArgs, userData)` where **callingMethod** is the
        method that called this function. **args** is the sequence of non-keyword arguments that
        was passed to the calling method. **keywordArgs** is the dictionary of keyword arguments
        that was passed to the calling method. **userData** is the object passed as the **userData**
        argument to the addCallback method.
    userData
        Any type of data. This data will be passed to the callback function. The default value
        is None.
    callAfter
        A Boolean specifying that the callback should be called after the method has executed
        (instead of before the method is called). The default value is False, which indicates
        that the callback should be called before the method has executed. If **callAfter** = True,
        you can also access the return value of the command from within the callback by
        including the following statement `returnValue = getMethodReturnValue()` The
        getMethodReturnValue function is in the global namespace of the callback function.
    """
    ...


@abaqus_function_doc
def removeCallback(caller: str, methodName: str, callback: str, userData: Optional[str] = None):
    """This method removes a callback added by the addCallback method. To successfully remove a callback, all
    arguments must exactly match those used when the callback was added.

    .. note::
        This function can be accessed by::

            methodCallback.removeCallback

    Parameters
    ----------
    caller
        An object or type object specifying which object will trigger the callback function to
        be invoked or the Symbolic Constant ALL_TYPES.
    methodName
        A String specifying the name of the method on the caller that will trigger the callback
        function to be invoked or the Symbolic Constant ALL_METHODS.
    callback
        A Python function to be called when a command matching the specified caller and method
        name is about to be executed. The interface definition of the callback function is `def
        functionName(callingMethod, args, keywordArgs, userData)` where **callingMethod** is the
        method that called this function. **args** is the sequence of nonkeyword arguments that was
        passed to the calling method. **keywordArgs** is the dictionary of keyword arguments that
        was passed to the calling method. **userData** is the object passed as the **userData**
        argument to the removeCallback method.
    userData
        Any type of data. This data will be passed to the callback function. The default value
        is None.
    """
    ...
