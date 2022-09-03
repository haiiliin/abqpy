=======
Summary
=======

The examples illustrate how a script can operate on a model in a model database or on the data stored in an output database. The details of the commands in the examples are described in later sections; however, you should note the following:

- You can run a script from the Abaqus/CAE startup screen when you start a session. After a session has started, you can run a script from the FileRun Script menu or from the command line interface.

- A script is a sequence of commands stored in ASCII format and can be edited with a standard text editor.

- A set of example scripts are provided with Abaqus. Use the abaqus fetch command to retrieve a script and any associated files.

- You must use the import statement to make the required set of Abaqus Scripting Interface commands available. For example, the statement import part provides the commands that create and operate on parts.

- A command that creates something (an "object" in object-oriented programming terms) is called a constructor and starts with an uppercase character. For example, the following statement uses the Model constructor to create a model object.

  .. code-block:: python2

      myModel = mdb.Model(name='Model A')

  The model object created is

  .. code-block:: python2

      mdb.models['Model A']

- You can use a variable to refer to an object. Variables make your scripts easier to read and understand. myModel refers to a model object in the previous example.

- A Python script can include a loop. The start and end of a loop is controlled by indentation in the script.

- Python includes a set of built-in functions. For example, the len() function returns the length of a sequence.

- You can use commands to replicate any operation that can be performed interactively when you are working with Abaqus/CAE; for example, creating a viewport, displaying a contour plot, and setting the step and the frame to display.