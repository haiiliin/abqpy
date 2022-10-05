===
CLI
===

The default execution procedure invoked by `abqpy` inside the Python interpreter
environment where it is installed is to run one of the two following command lines:

1. When there is a ``import abaqus`` or ``from abaqus import ...`` statement:

.. code-block:: sh

    abaqus cae noGUI=script.py -- [args ...]
        
2. When there is a ``import odbAccess`` or ``from odbAccess import ...`` statement:

.. code-block:: sh

    abaqus python script.py [args ...]

These commands lines are invoked when you run your script containing the above
statements in your installed Python interpreter, with a simple command line launch:

.. code-block:: sh
    
    python script.py [args ...]

However, there are other execution procedures that can be run with the `abaqus`
command and also another options that could be passed to these commands. To supply
that procedures and options, `abqpy` provides a separate **command line interface**.

.. code-block::

    usage: abqpy [-h] [-g [options ...] | -n [options ...] | -p [options ...]] [--] [script] [args ...]

    The abqpy command line interface

    positional arguments:
    script                the python script to run
    args                  arguments that will be passed to the python script

    optional arguments:
    -h, --help            show this help message and exit
    -g [options ...], --cae-gui [options ...]
                            command line options used to run Abaqus/CAE command with the graphical user interface (GUI mode)
    -n [options ...], --cae-nogui [options ...]
                            command line options used to run Abaqus/CAE command without the graphical user interface (noGUI mode)
    -p [options ...], --python [options ...]
                            command line options used to run Abaqus Python command
    --                    argument to pass the script after abaqus command line options

Currently, `abqpy` command line interface provides 3 execution modes: **Abaqus/CAE**
Execution in 2 modes: GUI and noGUI modes; and **Abaqus Python** Execution mode.

Examples:

1. If you want to run you python script in Abaqus/CAE GUI mode, you could run:

.. code-block:: sh

    abqpy script.py [args ...] -g

2. If you want to run you python script in Abaqus/CAE GUI or noGUI mode, providing
   the `database` file option, you could run:

.. code-block:: sh

    abqpy script.py [args ...] -g database=file.odb # GUI mode
    
    abqpy script.py [args ...] -n database=file.odb # noGUI mode

3. If you want to pass your python script file name after the abaqus command line
   options, you will need to use the ``--`` argument before the script filename, to
   prevent `abqpy` from attempting to parse it to abaqus:
   
.. code-block:: sh

    abqpy -g database=file.odb -- script.py [args ...]

Some moderns Python IDEs allow you to customize the default python launch parameters
that will be passed to the interpreter. This feature permits to run `abqpy` command line
interface as a module script and customize your default abaqus execution procedure.

Example: In 
`VS Code Python Extension
<https://marketplace.visualstudio.com/items?itemName=ms-python.python>`_,
you can specify the following setting:

.. code-block:: json
    
    "python.terminal.launchArgs": [ "-m", "abqpy", "-g", "--" ]

That setting will make VS Code Python Extension run by default all python script
files in the integrated terminal with the following command line:

.. code-block:: sh
    
    python -m abqpy -g -- script.py [args ...]

Which provides a way to change the default abaqus execution procedure to GUI mode.
