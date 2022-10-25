# Compiling and linking your C++ source code

Sample postprocessing programs to perform commonly exercised tasks are presented in separate sections in this chapter. These and other C++ postprocessing programs must be compiled and linked using the make parameter when running the Abaqus execution procedure (see [Making user-defined executables and subroutines](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEEXCRefMap/simaexc-c-makeproc.htm?contextscope=all)). To link properly, the programs cannot contain a C++ main routine. Instead, the programs must begin with a C++ function called ABQmain.

```python2
#include <odb_API.h>

int ABQmain(int argc, char **argv)
{
    //Insert user code here
    return 0
}
```

The arguments passed into the program upon execution will be passed into `ABQmain` as though it were the standard C++ main function. The compile and link commands used by the **abaqus make** utility are determined by the settings of the **compile_cpp** and **link** parameters in the Abaqus environment file.
