import typing
from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from ..UtilityAndView.abaqusConstants import *


@abaqus_class_doc
class KeywordBlock:
    """The KeywordBlock object contains a representation of its model in the Abaqus input file
    format. You may edit the contents of the KeywordBlock to add solver functionality that
    is not supported by Abaqus/CAE. As a general rule, edits to the KeywordBlock object
    should be made as the last step prior to writing the actual Abaqus input file, thus
    avoiding possible conflicts with changes made using other MDB commands. The KeywordBlock
    object has no constructor. A :py:class:`~abaqus.Model.KeywordBlock.KeywordBlock` object is created when you create a model
    object. A model object contains only one KeywordBlock object.

    .. note::
        This object can be accessed by::
        
            mdb.models[name].keywordBlock
    """

    #: A Boolean specifying whether the Keywords Editor has been used to change the model.
    edited: Boolean = OFF

    #: A Float specifying the value of the counter associated with the Mdb object at the most
    #: recent synchronization.
    lastSynchCount: typing.Optional[float] = None

    #: A tuple of Strings specifying a sequence of Strings that is identical to the information
    #: written to the Abaqus input file. Each String in the sequence represents an Abaqus input
    #: file keyword along with the parameters and data lines associated with the keyword. A
    #: String can also be a comment in the input file. You initialize this data member by
    #: calling synchVersions. After you initialize the data member, you use calls to replace
    #: and insert to record your edits in the correct location. If the last call to
    #: synchVersions used the argument **storeNodesAndElements** = False, the entry for the
    #: keywords NODE and ELEMENT will contain only the keyword and its parameters, not the data
    #: lines.
    sieBlocks: tuple = ()

    @abaqus_method_doc
    def setValues(self, edited: Boolean = OFF):
        """This method modifies the KeywordBlock object.

        Parameters
        ----------
        edited
            A Boolean specifying whether this objects **sieBlocks** member has been edited. Setting
            edited=False will set the **sieBlocks** member to an empty tuple, thereby discarding all
            previous edits.
        """
        ...

    @abaqus_method_doc
    def insert(self, position: int, text: str):
        """This method inserts a String at a specified position in the **sieBlocks** member.

        Parameters
        ----------
        position
            An Int specifying the position in the **sieBlocks** member after which the new string will
            be inserted.
        text
            A String specifying the text to be inserted. The text represents an Abaqus input file
            keyword and its associated data

        Raises
        ------
        IndexError
        """
        ...

    @abaqus_method_doc
    def replace(self, position: int, text: str):
        """This method replaces a String at a specified position in the **sieBlocks** member.

        Parameters
        ----------
        position
            An Int specifying the position of the String to be replaced in the **sieBlocks** member.
        text
            A String specifying the text to be replaced. The text represents an Abaqus input file
            keyword and its associated data.

        Raises
        ------
        IndexError
        """
        ...

    @abaqus_method_doc
    def synchVersions(self, storeNodesAndElements: Boolean):
        """This method synchronizes, or merges, the edits made in this object with those made in
        the model using other scripting commands or the user interface. The synchVersions method
        updates the **sieBlocks** member. The **sieBlocks** member is empty prior to the first call
        to synchVersions. As a side effect, synchVersions sets **lastSynchCount** to the current
        value of the counter associated with the Mdb object, which is used to determine if
        synchronization is necessary.

        Parameters
        ----------
        storeNodesAndElements
            A Boolean specifying whether the nodal coordinates and element connectivities (i.e. the
            data lines for the *NODE and *ELEMENT keyword blocks) are to be stored in the
            **sieBlocks** member. All other keywords and their data lines are always stored. The
            default value is True. If **storeNodesAndElements** is True, the size of the keywordBlock
            data will be similar to that of the input file. Since the KeywordBlock is stored in the
            Abaqus/CAE database, this will result in a larger database. It will also result in a
            slower execution of the synchVersions command. If **storeNodesAndElements** is False, the
            data lines are not stored in **sieBlocks**. Consequently, only set
            **storeNodesAndElements** = True if you wish to make changes to the **NODE** or **ELEMENT** data
            lines themselves. If your task is limited to reading nodal coordinates and element
            connectivities (i.e. not editing this information) then it is generally better to access
            this information from other parts of the Mdb.

        Raises
        ------
        IndexError
        """
        ...
