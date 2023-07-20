# Accessing the C++ interface from an existing application

This section provides information that may be helpful to users who need to access results in an output database from an existing application. Most users should find that the **abaqus make** utility is sufficient for their postprocessing needs. Since linking and executing with dynamically linked runtime libraries is highly system dependent, the information in this section is intended for users who have an advanced working knowledge of compilation and linking with runtime libraries.

It is important to ensure that the compiler used to compile and link the existing application is consistent with the compilers used to generate the Abaqus release. The “System Requirements” document lists the name and version of the compiler used for the Abaqus release on each supported platform. You can access this document through the **System Information** section of the **Support** page at <https:www.3ds.com/simulia>. You can also find information on compiling and linking with the C++ interface to an output database in the Dassault Systèmes Knowledge Base at <https://support.3ds.com/knowledge-base/>.

## Initializing the C++ interface

Before any calls are made to the C++ interface, the following call must be made to initialize the interface:

```cpp
odb_initializeAPI();
```

This call is generated automatically when the **abaqus make** utility is run but must be included in any application that is not compiled and linked using the **abaqus make** utility. After all calls to the C++ interface have been completed, the interface may be deactivated by including a call to

```cpp
odb_finalizeAPI();
```

If the finalization call is not made explicitly, the finalize routine will be called automatically when the application exits.

## Link library location

The libraries necessary to link applications that access the C++ interface are located in the following directories:

- **Linux**

  _abaqus_dir/code/lib_

- **Windows**

  _abaqus_dircodelib_

where **abaqus_dir** is the name of the directory in which Abaqus is installed. To determine the location of **abaqus_dir** at your site, type `abaqus whereami` at an operating system prompt.

During linking, the `ABQodb` library and several other libraries shipped with the Abaqus release are used to resolve all the functions available in the interface to the output database. The command used by Abaqus to link runtime libraries (for example, for user subroutines) is available through the Abaqus environment variable **link_sl**. Additional information about linking with the Abaqus libraries, including the names of all libraries which must be specified as part of the link command, may be obtained by running the **abaqus make** utility in verbose mode with a verbosity level of 3.

## Runtime library location

The runtime libraries required to execute a program that accesses the C++ interface are located in the following directories:

- **Linux**

  _abaqus_dir/code/bin_

- **Windows**

  _abaqus_dircodebin_

where **abaqus_dir** is the name of the directory in which Abaqus is installed. To determine the location of **abaqus_dir** at your site, type `abaqus whereami` at an operating system prompt.

The correct path to the Abaqus runtime libraries must be specified prior to starting the user application. The runtime library path is typically set using the system environment variable `LD_LIBRARY_PATH`, but the method used to set the path may vary depending on your operating system configuration. The `ABQodb` library and several utility libraries resolve all the functions available in the interface to the output database, as described in [Link library location](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAECMDRefMap/simacmd-c-odbintrocpplinklibrary.htm?contextscope=all). At runtime these libraries depend on many of the underlying Abaqus libraries. As a result, if you do not define the correct runtime library path, your application will not run.

## Header file location

he header files required to compile a program that accesses the C++ interface are located in the following directories:

- **Linux**

  _abaqus_dir/code/include_

- **Windows**

  _abaqus_dircodeinclude_

where **abaqus_dir** is the name of the directory in which Abaqus is installed. To determine the location of **abaqus_dir** at your site, type `abaqus whereami` at an operating system prompt.

Only `odb_API.h` must be included to access the C++ interface, but the path to the header files must be provided during compilation.
