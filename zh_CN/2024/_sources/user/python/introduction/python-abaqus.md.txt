# Python and Abaqus

Python is the standard programming language for Abaqus products and is used in several ways.

- The Abaqus environment file uses Python statements.

- The parameter definitions on the data lines of the [PARAMETER](https://help.3ds.com/2021/english/dssimulia_established/SIMACAEKEYRefMap/simakey-r-parameter.htm?contextscope=all#simakey-r-parameter) ("Define parameters for input parametrization") option in the Abaqus input file are Python statements.

- The parametric study capability of Abaqus requires the user to write and to execute a Python scripting (.psf) file.

- Abaqus/CAE records its commands as a Python script in the replay (.rpy) file.

- You can execute Abaqus/CAE tasks directly using a Python script. You can execute a script from Abaqus/CAE using the following:

  > - From the main menu bar.
  > - The Macro Manager.
  > - The command line interface (CLI).

- You can access the output database (.odb) using a Python script.
