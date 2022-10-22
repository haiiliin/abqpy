from typing import List

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from ..UtilityAndView.abaqusConstants import Boolean, ON


@abaqus_class_doc
class BackwardCompatibility:
    """The BackwardCompatibility object enables the user to control access to deprecated
    commands in the Abaqus Scripting Interface and to collect data on which deprecated
    commands have been used. This enables the user to check that no deprecated methods,
    members, or arguments have been used. Data are recorded on any deprecated members,
    methods, or arguments that are used.
    The BackwardCompatibility object has no constructor. The abaqus module and the odbAccess
    module each have a member named backwardCompatibility.
    By default, the value of the **includeDeprecated** member is ON, and Abaqus will execute a
    script containing deprecated commands with no indication that you should update the
    script. You can do either of the following to change the value of the
    **includeDeprecated** member and to determine which commands have been deprecated:
    
    - From the command line interface in Abaqus/CAE or from an Abaqus Scripting Interface
      script that is run from within Abaqus/CAE, use the following command::

          backwardCompatibility.setValues(includeDeprecated=OFF)

    - From an Abaqus Scripting Interface script that is run using `abaqus python` at the
      system prompt, use the following two commands::

          from odbAccess import *
          backwardCompatibility.setValues(includeDeprecated=OFF)

    In addition, the BackwardCompatibility object provides tools to assist you in
    determining the deprecated commands that have been used. For example, to determine the
    deprecated commands used in the script createLug.py, use the following commands::

        backwardCompatibility.resetDeprecatedMethodsUsed()
        backwardCompatibility.resetDeprecatedMembersUsed()
        backwardCompatibility.resetDeprecatedArgsUsed()
        execfile('createLug.py')
        print backwardCompatibility.getDeprecatedMethodsUsed()
        print backwardCompatibility.getDeprecatedMembersUsed()
        print backwardCompatibility.getDeprecatedArgsUsed()

    .. note:: 
        This object can be accessed by::

            backwardCompatibility
    """

    #: A Boolean specifying whether deprecated members, methods, and arguments can be seen and
    #: used. Possible values are ON and OFF. The default value is ON.
    includeDeprecated: Boolean = ON

    #: A Boolean specifying whether a warning is displayed after running a script that contains
    #: deprecated commands. The default value is True.
    reportDeprecated: Boolean = True

    #: A Boolean specifying whether the keys and indices are included in the report that is
    #: displayed when **reportDeprecated** is True. The default value is False.
    showKeysInReport: Boolean = False

    @abaqus_method_doc
    def getDeprecatedMethodsUsed(self):
        """This method returns a list of deprecated methods used since the last call to
        resetDeprecatedMethodsUsed.

        Returns
        -------
        List[str]
            A list of Strings.
        """
        ...

    @abaqus_method_doc
    def getDeprecatedArgsUsed(self):
        """This method returns a list of deprecated arguments used since the last call to
        resetDeprecatedArgsUsed.

        Returns
        -------
        List[str]
            A list of Strings.
        """
        ...

    @abaqus_method_doc
    def resetDeprecatedMethodsUsed(self):
        """This method clears the list of deprecated methods used."""
        ...

    @abaqus_method_doc
    def resetDeprecatedArgsUsed(self):
        """This method clears the list of deprecated arguments used."""
        ...

    @abaqus_method_doc
    def setValues(
        self,
        includeDeprecated: Boolean = ON,
        reportDeprecated: Boolean = True,
        showKeysInReport: Boolean = False,
    ):
        """This method modifies the BackwardCompatibility object.

        Parameters
        ----------
        includeDeprecated
            A Boolean specifying whether deprecated members, methods, and arguments can be seen and
            used. The default value is ON.
        reportDeprecated
            A Boolean specifying whether a warning is displayed after running a script that contains
            deprecated commands. The default value is True.
        showKeysInReport
            A Boolean specifying whether the keys and indices are included in the report that is
            displayed when **reportDeprecated** is True. The default value is False.
        """
        ...
