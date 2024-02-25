"""The following command is used to record a user-defined command in the Abaqus journal file."""
from abqpy.decorators import abaqus_function_doc


@abaqus_function_doc
def journalMethodCall(objectPath: str, methodName: str, args: tuple, kargs: str):
    """This function may be used by a user-defined command to record itself in the Abaqus journal file. For
    example::

        def setValues(self, **kargs):
            for arg,value in kargs.items():
                setattr(arg, value)
            from abaqus import journalMethodCall
            objPath = '%s[%r]' % (self.reposPath, self.name)
            journalMethodCall(objPath, 'setValues', (), kargs)

    .. note::
        Your command should not call journalMethodCall if the command changes the mdb using
        built-in Abaqus Scripting Interface commands, because built-in commands are journaled by
        default. A command that changes the mdb customData is one example of a command that
        should call journalMethodCall.

    .. note::
        This function can be accessed by::

            journalMethodCall

    Parameters
    ----------
    objectPath
        A String specifying the path to the object.
    methodName
        A String specifying the name of the method.
    args
        A sequence specifying the positional arguments to be written to the journal file.
    kargs
        A Python dict object specifying the keyword arguments to be written to the journal file.
    """
    ...
