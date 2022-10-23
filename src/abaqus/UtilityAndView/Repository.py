from abqpy.decorators import abaqus_class_doc, abaqus_method_doc


@abaqus_class_doc
class Repository(dict):
    """Repositories are containers that store a particular type of object; for example, the
    steps repository contains all the steps defined in the model. An Abaqus Scripting
    Interface Repository maps a key to a value. The key is usually a String, and the value
    is any Python object, usually an Abaqus object. A repository is similar to a Python
    dictionary; however, only a constructor can add an object to a repository. In addition,
    all of the objects in a repository are of the same base type. For more information, see
    Repositories. A Repository has no constructor. Abaqus creates empty repositories when
    you import a module. For example, Abaqus creates an empty parts repository when you
    import the part module.
    The following methods of the Repository object are standard Python dictionary methods
    and are not described here:
    The Repository object is derived from the dict object.
    - has_key
    - items
    - keys
    - values
    -
    [changeKey(...)](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-utlrepositorypyc.htm?ContextScope=all#simaker-utlrepositorychangekeypyc)
    """

    @abaqus_method_doc
    def changeKey(self, fromName: str, toName: str):
        """This method changes the name of a key in a repository and the **name** member of the value
        object.

        Parameters
        ----------
        fromName
            A String specifying the old name of the repository key.
        toName
            A String specifying the new name of the repository key.
        """
        ...
