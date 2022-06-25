========================================
Exception handling in an output database
========================================

Support for C++ exception handling is provided in the API to the output database.

For example, in your C++ program you may wish to customize the error message when an output database was not opened successfully as follows:

.. code-block:: cpp
    
    odb_String invalidOdbName = "invalid.odb";
    try {
        odb_Odb& odb = openOdb(invalidOdbName);
    }
    catch(odb_BaseException& exc) {
        cerr << "odbBaseException caught\n";
        cerr << "Abaqus error message: " << exc.UserReport().CStr() 
        << endl;
        cerr << "Customized error message here\n";
    }
    catch(...) {
        cerr << "Unknown Exception.\n";
    }

For more information, see BaseException object.