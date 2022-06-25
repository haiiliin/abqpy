=========================================================
Example programs that access data from an output database
=========================================================

The following examples illustrate how you use the output database commands to access data from an output database.

Finding the maximum value of von Mises stress
---------------------------------------------

This example illustrates how you can iterate through an output database and search for the maximum value of von Mises stress. The program opens the output database specified by the first argument on the command line and iterates through the following:

- Each step.
- Each frame in each step.
- Each value of von Mises stress in each frame.

In addition, you can supply an optional assembly element set argument from the command line, in which case the program searches only the element set for the maximum value of von Mises stress.

The following illustrates how you can run the example program from the system prompt. The program will search the element set ALL ELEMENTS in the viewer tutorial output database for the maximum value of von Mises stress:

.. code-block:: sh

    abaqus odbMaxMises.exe -odb viewer_tutorial.odb 
        -elset "ALL ELEMENTS"

.. note::
    If a command line argument is a String that contains spaces, some systems will interpret the String correctly only if it is enclosed in double quotation marks. For example, "ALL ELEMENTS".

You can also run the example with only the **-help** parameter for a summary of the usage.

Use the following commands to retrieve the example program and the viewer tutorial output database:

.. code-block:: cpp
    
    // abaqus fetch job=odbMaxMises.C
    // abaqus fetch job=viewer_tutorial

    /***************************************************************
    odbMaxMises.C
    Code to determine the location and value of the maximum 
    von-mises stress in an output database.
    Usage: abaqus odbMaxMises -odb odbName -elset(optional)
        elsetName
    Requirements:
    1. -odb   : Name of the output database.
    2. -elset : Name of the assembly level element set. 
                Search will be done only for element belonging 
                to this set. If this parameter is not provided, 
                search will be performed over the entire model.
    3. -help  : Print usage
    ****************************************************************/
    #if (defined(HP) && (! defined(HKS_HPUXI)))
    #include <iostream.h>
    #else
    #include <iostream>
    using namespace std;
    #endif

    #include <odb_API.h>
    #include <sys/stat.h>
    /*
    *************** 
    utility functions
    ***************
    */
    bool fileExists(const odb_String  &string);
    void rightTrim(odb_String  &string,const char* char_set);
    void printExecutionSummary();
    /***************************************************************/


    int ABQmain(int argc, char **argv)
    {
    odb_String odbPath;  
    bool ifOdbName = false;
    odb_String elsetName;
    bool ifElset = false;
    odb_Set myElset;
    odb_String region = "over the entire model";
    char msg[256];
    char *abaCmd = argv[0];
    
    for (int arg = 0; arg<argc; arg++)
        {
        if (strncmp(argv[arg],"-o**",2) == 0)
        {
        arg++;
        odbPath = argv[arg];
        rightTrim(odbPath,".odb");
        if (!fileExists(odbPath))
            {
            cerr << "**ERROR** output database  " << odbPath.CStr() 
            << " does not exist\n" << endl;
            exit(1);
            }
        ifOdbName = true;
        }	  
        else if (strncmp(argv[arg],"-e**",2)== 0)
        {
        arg++;
        elsetName = argv[arg];
        ifElset = true;
        }
        else if (strncmp(argv[arg],"-h**",2)== 0)
        {
        printExecutionSummary(); 
        exit(0);
        }
        }
    if (!ifOdbName)
        {
        cerr << "**ERROR** output database name is not provided\n";
        printExecutionSummary();
        exit(1);
        }
    // Open the output database
    odb_Odb& myOdb = openOdb(odbPath);
    odb_Assembly& myAssembly = myOdb.rootAssembly();
    if (ifElset) 
        {
        if (myAssembly.elementSets().isMember(elsetName))
        {       
        myElset = myAssembly.elementSets()[elsetName]; 
        region = " in the element set : " + elsetName;
        }
        else
            {
            cerr<<"An assembly level elset " << elsetName.CStr()
                << " does not exist in the output database :"
                << myOdb.name().CStr() << endl;
        myOdb.close();
        exit(0);
        }
        }
    // Initialize maximum values.
    float maxMises = -0.1;
    int numFV = 0;
    int maxElem = 0;
    odb_String maxStep = "__None__";  
    int maxFrame = -1;
    static const odb_String Stress = "S";    
    bool isStressPresent = false;
    int numBD = 0,numElems = 0, numIP = 0, numComp = 0, position = 0;
    // Iterate over all available steps
    odb_StepRepository& sRep1 = myOdb.steps();        
    odb_StepRepositoryIT sIter1 (sRep1);
    for (sIter1.first(); !sIter1.isDone(); sIter1.next())
        {
        odb_Step& step = sRep1[sIter1.currentKey()];
        cout<<"Processing Step: "<<step.name().CStr()<<endl;
        odb_SequenceFrame& frameSequence = step.frames();
        int numFrames = frameSequence.size();      
        for (int f = 0; f<numFrames; f++) 
        {
        odb_Frame& frame = frameSequence[f]; 
        odb_FieldOutputRepository& fieldRep = frame.fieldOutputs();
        if (fieldRep.isMember(Stress))
        {
            isStressPresent = true;
            odb_FieldOutput field = fieldRep.get(Stress);
            if (ifElset) 
            field = field.getSubset(myElset);
            const odb_SequenceFieldBulkData& seqVal = 
                    field.bulkDataBlocks(); 
            int numBlocks = seqVal.size();
            for ( int iblock=0; iblock<numBlocks; iblock++) 
            {
            const odb_FieldBulkData& bulkData = seqVal[iblock];	      
            numBD = bulkData.length();
            numElems = bulkData.numberOfElements();
            numIP = numBD/numElems;
            numComp = bulkData.width();
            float* mises = bulkData.mises();
            int* elementLabels = bulkData.elementLabels();
            int* integrationPoints = bulkData.integrationPoints();	
            for (int elem=0; elem<numElems; elem++) 
            {				    	  		     
                for (int ip=0; ip<numIP; ip++)
                {
                position = elem*numIP+ip;
                float misesData = mises[position];		
                if (misesData > maxMises)
                {
                    maxMises = misesData;
                    maxElem = elementLabels[elem];
                    maxStep = step.name();
                    maxFrame = frame.incrementNumber();
                }
                }
            }
            }

        }	
        }    
        }
    if (isStressPresent)
        {
        cout << "Maximum von Mises stress " << region.CStr() 
        << " is " << maxMises << "  in element " 
            << maxElem << endl;
        cout << "Location: frame # " << maxFrame << " step:  " 
            << maxStep.CStr() << endl;
        }
    else
        {
        cout << " Stress output is not available in  the "
        << "output database : " << myOdb.name().CStr() << endl;
        }        
    // close the output database before exiting the program
    myOdb.close();
    return(0);
    }

    bool fileExists(const odb_String  &string)
    {
    bool exists = false;
    struct  stat  buf;  
    if (stat(string.CStr(),&buf)==0)
        exists = true;
    return exists;
    }

    void rightTrim(odb_String  &string,const char* char_set)
    {
    int length = string.Length();
    if (string.Find(char_set)==length)
        string.append(odb_String(char_set));
    }

    void printExecutionSummary()
    {
    cout << " Code to determine the location and value of the\n"
    << " maximum von-mises stress in an output database.\n"
    << " Usage: abaqus odbMaxMises -odb odbName \n"
    << " -elset(optional), -elsetName\n"
    << " Requirements:\n"
    << " 1. -odb   : Name of the output database.\n"
    << " 2. -elset : Name of the assembly level element set.\n"
    << "             Search will be done only for element \n"
    << "             belonging to this set.\n"
    << "             If this parameter is not provided, search \n"
    << "             will be performed over the entire model.\n"
    << " 3. -help  : Print usage\n";
    }

Creating an output database
---------------------------

The following example illustrates how you can use the Abaqus C++ API commands to do the following:

1. Create a new output database.
2. Add model data.
3. Add field data.
4. Add history data.
5. Read history data.
6. Save the output database.

Use the following command to retrieve the example program:

.. code-block:: cpp

    // abaqus fetch job=odbWrite

    ////////////////////////////////////////////////////
    // Code to create an output database and add model,
    // field, and history data. The code also reads
    // history data, performs an operation on the data, and writes
    // the result back to the output database.
    //
    // SECTION: System includes
    //
    #include <math.h>
    //
    // Begin local includes
    //
    #include <odb_API.h>
    #include <odb_MaterialTypes.h>
    #include <odb_SectionTypes.h>
    //
    // End local includes
    //

    int ABQmain(int argc, char **argv)
    {
        // Create an ODB (which also creates the rootAssembly).
        int n;
        odb_String name("simpleModel");
        odb_String analysisTitle("ODB created with C++ ODB API");
        odb_String description("example illustrating C++ ODB API");
        odb_String path("odbWriteC.odb");
        odb_Odb& odb = Odb(name,
                        analysisTitle,
                        description,
                        path);

        // Model data:
        // Set up the section categories.
        odb_String sectionCategoryName("S5");
        odb_String sectionCategoryDescription("Five-Layered Shell");
        odb_SectionCategory& sCat =
            odb.SectionCategory(sectionCategoryName,
                                sectionCategoryDescription);
        int sectionPointNumber = 1;
        odb_String sectionPointDescription("Bottom");
        odb_SectionPoint spBot =
            sCat.SectionPoint(sectionPointNumber,
                            sectionPointDescription);
        sectionPointNumber = 3;
        sectionPointDescription = "Middle";
        odb_SectionPoint spMid =
            sCat.SectionPoint(sectionPointNumber,
                            sectionPointDescription);
        sectionPointNumber = 5;
        sectionPointDescription = "Top";
        odb_SectionPoint spTop =
            sCat.SectionPoint(sectionPointNumber,
                            sectionPointDescription);

        // Create few materials
        odb_MaterialApi materialApi;
        odb.extendApi(odb_Enum::odb_MATERIAL,materialApi);
        odb_String materialName("Elastic Material");
        odb_Material& material_1 =
            materialApi.Material(materialName);
        odb_SequenceSequenceDouble myTable;
        odb_SequenceDouble myData;
        myData.append(12000.00);//youngs modulus
        myData.append(0.3);//poissons ratio
        myTable.append(myData);
        odb_String type("ISOTROPIC");
        bool noCompression = false;
        bool noTension = false;
        bool temperatureDependency = false;
        int dependencies = 0;
        odb_String moduli("LONG_TERM");
        material_1.Elastic(myTable,
                        type,
                        noCompression,
                        noTension,
                        temperatureDependency,
                        dependencies,
                        moduli);

        //create few sections
        odb_SectionApi sectionApi;
        odb.extendApi(odb_Enum::odb_SECTION,
                    sectionApi);
        odb_String sectionName("Homogeneous Shell Section");
        double thickness = 2.0;
        odb_HomogeneousShellSection& section_1 =
            sectionApi.HomogeneousShellSection(sectionName,thickness,materialName);

        // Create a 2-element shell model,
        //4 integration points, 5 section points.

        odb_Part& part1 = odb.Part("part-1",
                                odb_Enum::THREE_D,
                    odb_Enum::DEFORMABLE_BODY);

        odb_SequenceInt nodeLabels;
        for(n=1; n<7; n++)
        nodeLabels.append(n);

        double c[6][3] = { {1,  0,  0.0},
                    {2,  0,  0.0},
                {2,  1,  0.1},
                {1,  1,  0.1},
                {2, -1, -0.1},
                {1, -1, -0.1} };
        odb_SequenceSequenceFloat nodeCoor;
        for(n=0; n<nodeLabels.size(); n++) {
        odb_SequenceFloat loc;
        for(int i=0; i<3; i++)
            loc.append(c[n][i]);
        nodeCoor.append(loc);
        }
        odb_String nodeSetName("nset-1");
        part1.addNodes(nodeLabels,
                    nodeCoor,
                    nodeSetName);

        odb_SequenceInt elLabels;
        elLabels.append(1);
        elLabels.append(2);
        odb_SequenceSequenceInt connect;
        const int numNodePerEl = 4;
        int conn[2][numNodePerEl] = { {1, 2, 3, 4},
                                {6, 5, 2, 1} };
        for(int e=0; e<elLabels.size(); e++) {
        odb_SequenceInt l;
        for(int i=0; i<numNodePerEl; i++)
            l.append(conn[e][i]);
        connect.append(l);
        }
        odb_String elType("S4");
        odb_String elsetName("eset-1");
        part1.addElements(elLabels,
                        connect,
                        elType,
                        elsetName,
                        sCat);

        // Instance the part.
        odb_String partInstanceName("part-1-1");
        odb_Instance& instance1 =
            odb.rootAssembly().Instance(partInstanceName, part1);
        // create instance level sets for section assignment
        elsetName = "Material 1";
        odb_Set& elset_1 = instance1.ElementSet(elsetName,
                                                elLabels);
        // section assignment on instance
        instance1.assignSection(elset_1,section_1);
        // Field data:
        // Create a step and a frame.
        odb_String stepName("step-1");
        odb_String stepDescription("first analysis step");
        odb_Step& step1 = odb.Step(stepName,
                                stepDescription,
                                odb_Enum::TIME,
                    1.0);
        int incrementNumber = 1;
        float analysisTime = 0.1;
        odb_String frameDescription("results frame for time");
        frameDescription.append(analysisTime);
        odb_Frame frame1 = step1.Frame(incrementNumber,
                                    analysisTime,
                                    frameDescription);

        // Write nodal displacements.
        odb_String fieldName("U");
        odb_String fieldDescription("Displacements");
        odb_FieldOutput& uField =
            frame1.FieldOutput(fieldName,
                            fieldDescription,
                odb_Enum::VECTOR);

        odb_SequenceSequenceFloat dispData;
        odb_SequenceFloat dispData1[6];
        // create some displacement values
        for(n=0; n<6; n++) {
        for(int m=1; m<4; m++)
            dispData1[n].append(n*3+m);
        dispData.append(dispData1[n]);
        }
        uField.addData(odb_Enum::NODAL,
                    instance1,
                    nodeLabels,
                    dispData);

        // Make this the default deformed field for visualization.

        step1.setDefaultDeformedField(uField);

        // Write stress tensors (output only available at
        // top/bottom section points)
        // The element defined above (S4) has 4 integration points.
        // Hence, there are 4 stress tensors per element.
        // Each Field constructor refers to only one layer of
        // section points.

        odb_SequenceSequenceFloat topData;
        odb_SequenceFloat topData1;
        for(n=1; n<5; n++)
        topData1.append(n);

        for(n=0; n<8; n++)
        topData.append(topData1);

        odb_SequenceSequenceFloat bottomData;
        odb_SequenceFloat bottomData1;
        for(n=1; n<5; n++)
        bottomData1.append(n);

        for(n=0; n<8; n++)
        bottomData.append(bottomData1);

        odb_SequenceSequenceFloat transform;

        //transform = ((1.,0.,0.), (0.,1.,0.), (0.,0.,1.))

        for(n=1; n<4; n++){
        odb_SequenceFloat transform1;
        for(int m=1; m<4; m++) {
            if(m==n)transform1.append(1);
            else transform1.append(0);
        }
        transform.append(transform1);
        }

        odb_SequenceString componentLabels;
        componentLabels.append("S11");
        componentLabels.append("S22");
        componentLabels.append("S33");
        componentLabels.append("S12");

        odb_SequenceInvariant validInvariants;
        validInvariants.append(odb_Enum::MISES);
        fieldName = "S";
        fieldDescription = "Stress";
        odb_FieldOutput& sField =
            frame1.FieldOutput(fieldName,
                            fieldDescription,
                            odb_Enum::TENSOR_3D_PLANAR,
                            componentLabels,
                            validInvariants);

        sField.addData(odb_Enum::INTEGRATION_POINT,
                    instance1,
            elLabels,
                    topData,
                    spTop,
                    transform);

        sField.addData(odb_Enum::INTEGRATION_POINT,
                    instance1,
            elLabels,
                    bottomData,
                    spBot,
                    transform);

        // For this step, make this the default
        // field for visualization.

        step1.setDefaultField(sField);

        // History data:
        // Create a HistoryRegion for a specific point.
        odb_HistoryPoint hPoint1(instance1.getNodeFromLabel(1));
        odb_String historyRegionName("historyNode0");
        odb_String historyRegionDescription(
            "Displacement and reaction force");
        odb_HistoryRegion& hRegionStep1 =
            step1.HistoryRegion(historyRegionName,
                                historyRegionDescription,
                                hPoint1);

        // Create variables for this history output in step1.

        odb_String historyOutputName("U1");
        odb_String historyOutputDescription("Displacement");
        odb_HistoryOutput& hOutputStep1U1 =
            hRegionStep1.HistoryOutput(historyOutputName,
                                    historyOutputDescription,
                                    odb_Enum::SCALAR);
        historyOutputName = "RF1";
        historyOutputDescription = "Reaction Force";
        odb_HistoryOutput& hOutputStep1Rf1 =
            hRegionStep1.HistoryOutput(historyOutputName,
                                    historyOutputDescription,
                                    odb_Enum::SCALAR);
        // Add history data for step1.

        hOutputStep1U1.addData(0.0, 0.0);
        hOutputStep1Rf1.addData(0.0,0.0);
        hOutputStep1U1.addData(0.1, 0.1);
        hOutputStep1Rf1.addData(0.1,0.1);
        hOutputStep1U1.addData(0.3, 0.3);
        hOutputStep1Rf1.addData(0.3,0.3);
        hOutputStep1U1.addData(1.0, 0.5);
        hOutputStep1Rf1.addData(1.0,0.5);

        // Create another step for history data.
        stepName = "step-2";
        stepDescription = "second analysis step";
        odb_Step& step2 = odb.Step(stepName,
                                stepDescription,
                                odb_Enum::TIME,
                    1.0);


        // Create new history region

        odb_HistoryPoint hPoint2(instance1.getNodeFromLabel(1));

        odb_HistoryRegion& hRegionStep2 =
            step2.HistoryRegion(historyRegionName,
                                historyRegionDescription,
                                hPoint2);

        //Create new history output
        historyOutputName = "U1";
        historyOutputDescription = "Displacement";
        odb_HistoryOutput& hOutputStep2U1 =
            hRegionStep2.HistoryOutput(historyOutputName,
                                    historyOutputDescription,
                                    odb_Enum::SCALAR);

        historyOutputName = "RF1";
        historyOutputDescription = "Reaction Force";
        odb_HistoryOutput& hOutputStep2Rf1 =
            hRegionStep2.HistoryOutput(historyOutputName,
                                    historyOutputDescription,
                                    odb_Enum::SCALAR);


        // Add history data for the second step.

        hOutputStep2U1.addData(1.2, 0.8);
        hOutputStep2Rf1.addData(1.2,0.9);
        hOutputStep2U1.addData(1.9, 0.9);
        hOutputStep2Rf1.addData(1.9,1.1);
        hOutputStep2U1.addData(3.0, 1.3);
        hOutputStep2Rf1.addData(3.0,1.3);
        hOutputStep2U1.addData(4.0, 1.5);
        hOutputStep2Rf1.addData(4.0,1.5);

        // Square the history data U, and store as new history output
        historyOutputName = "squareU1";
        historyOutputDescription = "Square of displacements";
        odb_HistoryOutput&  hOutputStep1sumU1 =
            hRegionStep1.HistoryOutput(historyOutputName,
                                    historyOutputDescription,
                                    odb_Enum::SCALAR);
        historyOutputName = "squareU2";
        odb_HistoryOutput&  hOutputStep2sumU1 =
            hRegionStep2.HistoryOutput(historyOutputName,
                                    historyOutputDescription,
                                    odb_Enum::SCALAR);

        // Get XY Data from the two steps.

        odb_HistoryOutputRepository& historyOutputs1 =
            hRegionStep1.historyOutputs();
        historyOutputName = "U1";
        odb_HistoryOutput& u1FromStep1 =
            historyOutputs1[historyOutputName];

        odb_HistoryOutputRepository& historyOutputs2 =
        hRegionStep2.historyOutputs();
        odb_HistoryOutput& u1FromStep2 =
            historyOutputs2[historyOutputName];

        odb_SequenceSequenceFloat hdata1 = u1FromStep1.data();
        odb_SequenceSequenceFloat hdata2 = u1FromStep2.data();

        // Add the squared displacement to the two steps.

        for(n=0; n<hdata1.size(); n++){
        odb_SequenceFloat hdata11=hdata1.get(n);
        hOutputStep1sumU1.addData(hdata11.get(0),
            pow((double)hdata11.get(1),(int)2));
        }

        for(n=0; n<hdata2.size(); n++){
        odb_SequenceFloat hdata22=hdata2.get(n);
        hOutputStep2sumU1.addData(hdata22.get(0),
            pow((double)hdata22.get(1),(int)2));
        }


        // Save the results in the output database.
        // Use the Visualization module of Abaqus/CAE to
        // view the contents of the output database.

        odb.save();
        odb.close();
        return 0;
    }

Reading data from an output database
------------------------------------

This example illustrates how you can print the content of an output database. The example opens the output database specified on the command line and calls functions that print the following:

- Parts
- Part instances
- The root assembly
- Connectors
- Connector properties
- Datum coordinate systems
- Nodes
- Elements
- Sets
- Faces
- Sections
- Steps
- Frames
- Fields
- Field values
- Field bulk data
- Field locations
- History regions
- History output
- History points

Use the following command to retrieve the example program:

.. code-block:: sh

    abaqus fetch job=odbDump

Decreasing the amount of data in an output database by retaining data at specific frames
----------------------------------------------------------------------------------------

This example illustrates how you can decrease the size of an output database. In most cases a large output database results from excessive field output being generated over a large number of frames. The Abaqus C++ API does not support the deletion of data from an output database; however, you can use this example program to copy data from select frames into a second output database created by a **datacheck** analysis that has identical model data. The original analysis and the **datacheck** analysis must be run using the same number of processors because the internal organization of data may differ based on the number of processors. The program uses addData to copy data at specified frames from the large output database into the new output database. The addData method works only when the model data in the two output databases are identical. For more information, see :py:meth:`~abaqus.Odb.FieldOutput.FieldOutput.addData`.

When you run the program, the following command line parameters are required:

- **-smallOdb odbName**

  The name of the output database created with a **datacheck** analysis of the original problem. For more information, see `Abaqus/Standard and Abaqus/Explicit execution <https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEEXCRefMap/simaexc-c-analysisproc.htm?contextscope=all>`_.

- **-largeOdb odbName**

  The name of the large output database generated by the original problem. The program copies selected frames from this output database.

The following parameters are optional:

- **-history**

  Copy all history output from all available steps in the large output database. By default, history output is not copied.
  
  .. warning:: 
      Copying large amounts of history data can result in the program creating a very large output database.

- **-debug**

  Print a detailed report of all the operations performed during the running of the program. By default, no debug information is generated.
  
  .. warning:: 
      If you are extracting data from a large output database, the debug option can generate large amounts of information.

You can also run the example with only the **-help** parameter for a summary of the usage.

The following is an example of how you can use this program in conjunction with the output database generated by the problem described in `Free ring under initial velocity: comparison of rate-independent and rate-dependent plasticity <https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEBMKRefMap/simabmk-c-freering.htm?contextscope=all>`_. Use the following commands to retrieve the example program and the benchmark input file:

.. code-block:: sh

    abaqus fetch job=odbFilter.C
    abaqus fetch job=ringshell.inp

1. Run an analysis using the benchmark input file:

  .. code-block:: sh

      abaqus job=ringshell

  This creates an output database called `ringshell.odb` that contains 100 frames of data.

1. Run a **datacheck** analysis to obtain a new output database called `ringshell_datacheck.odb` that contains the same model data as `ringshell.odb`:

  .. code-block:: sh

      abaqus job=ringshell_datacheck -input ringshell datacheck

1. Create the executable program:

  .. code-block:: sh

      abaqus make job=odbFilter.C

The program displays the number of frames available in each step. For each step you must specify the number of increments between frames, which is the frequency at which the data will be copied to the new output database. Data for the first and last increment in each step are always copied. For example, if a step has 100 frames, and you enter a frame interval of 37, the program will copy data for frames 0, 37, 74, and 100.

The following statement will run the executable program and read data from the small output database containing only model data and the large output database created by the benchmark example:

.. code-block:: sh

    abaqus odbFilter -smallOdb ringshell_datacheck -largeOdb ringshell 

The program prompts you for the increment between frames:

.. code-block:: sh

    Results from ODB : ringshell.odb will be filtered & written 
    to ODB: ringshell_datacheck
    By default only the first & last increment of a step will 
    be saved
    For each step enter the increment between frames
    for example : 3 => frames 0,3,6,..,lastframe will be saved
    STEP Step-1 has 101 Frames
    Enter Increment between frames

Enter 37 to define the increment between frames. The program then reads the data and displays the frames being processed:

.. code-block:: sh

    Processing frame # : 0
    Processing frame # : 37
    Processing frame # : 74
    Processing frame # : 100
    Filtering successfully completed

Stress range for multiple load cases
------------------------------------

This example illustrates how you can use the envelope operations to compute the stress range over a number of load cases. The example program does the following:

- For each load case during a specified step, the program collects the S11 components of the stress tensor fields into a list of scalar fields.
- Computes the maximum and minimum of the S11 stress component using the envelope calculations.
- Computes the stress range using the maximum and minimum values of the stress component.
- Creates a new frame in the step.
- Writes the computed stress range into a new FieldOutput object in the new frame.

Use the following command to retrieve the example program:

.. code-block:: sh

    abaqus fetch job=stressRange

The fetch command also retrieves an input file that you can use to generate an output database that can be read by the example program.

.. code-block:: cpp
    
    ////////////////////////////////////////////////////
    // Code to compute a stress range from 
    // all the load cases in a step.
    //
    // The stress range is saved to a frame with the
    // description "Stress Range"

    // System includes
    #if (defined(HP) && (! defined(HKS_HPUXI)))
    #include <iostream.h>
    #else
    #include <iostream>
    using namespace std;
    #endif

    // Begin Local Includes
    #include <odb_API.h>
    // End Local Includes

    odb_FieldOutput computeStressRange( odb_Step& step );

    int ABQmain(int argc, char **argv)
    {
        if( argc < 3 ) {
            cerr << "Usage: abaqus stressRange.x odb_name"
                <<         "step_name" 
                <<         endl;
            return 1;
        }

        odb_String odbName(argv[1]);
        odb_String stepName(argv[2]);
        cout << "Computing for odb \"" << odbName.CStr() << "\"";
        cout << " and step \"" << stepName.CStr() << "\"." << endl;

        // compute stress range and save to odb
        odb_Odb& odb = openOdb(odbName);
        odb_Step& step = odb.steps()[stepName];
        odb_FieldOutput range = computeStressRange(step);

        // Save the results in the output database. 
        odb_Frame rangeFrame = step.Frame(0, 0, "Stress Range");
        rangeFrame.FieldOutput(range, "S11 Range");
        odb.save();
        odb.close();

        return 0;
    }

    odb_FieldOutput
    computeStressRange(odb_Step& step)
    {
        // collect stress fields for all load cases
        odb_SequenceFieldOutput sFields;
        odb_LoadCaseRepositoryIT iter(step.loadCases());
        for( iter.first(); !iter.isDone(); iter.next() ) {
            odb_Frame frame = step.getFrame( iter.currentValue() );
            odb_FieldOutput& stressField = frame.fieldOutputs()["S"];
            sFields.append(stressField.getScalarField("S11"));
        };

        // compute maximum and minimum envelopes
        odb_SequenceFieldOutput maxFields = maxEnvelope(sFields);
        odb_SequenceFieldOutput minFields = minEnvelope(sFields);

        // compute and return range
        return (maxFields.get(0) - minFields.get(0));
    }

A C++ version of FELBOW
-----------------------

This example illustrates the use of a C++ program to read selected element integration point records from an output database and to postprocess the elbow element results. The program creates **X - Y** data that can be plotted with the *X–Y* plotting capability in Abaqus/CAE. The program performs the same function as the Fortran program described in `Creation of a data file to facilitate the postprocessing of elbow element results: FELBOW <https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEEXARefMap/simaexa-c-felbow.htm?contextscope=all>`_.

The program reads integration point data for elbow elements from an output database to visualize one of the following:

1. Variation of an output variable around the circumference of a given elbow element, or
2. Ovalization of a given elbow element.

The program creates either an ASCII file containing *X–Y* data or a new output database file that can be viewed using Abaqus/CAE.

To use option 2, you must ensure that the integration point coordinates (COORD) are written to the output database. For option 1 the *X*-data are data for the distance around the circumference of the elbow element, measured along the middle surface, and the *Y*-data are data for the output variable. For option 2 the *X–Y* data are the current coordinates of the middle-surface integration points around the circumference of the elbow element, projected to a local coordinate system in the plane of the deformed cross-section. The origin of the local system coincides with the center of the cross-section; the plane of the deformed cross-section is defined as the plane that contains the center of the cross-section.

You should specify the name of the output database during program execution. The program prompts for more information, depending on the option that was chosen; this information includes the following:

- Your choice for storing results (ASCII file or a new output database)
- File name based on the above choice
- The postprocessing option (1 or 2)
- The part name
- The step name
- The frame number
- The element output variable (option 1 only)
- The component of the variable (option 1 only)
- The section point number (option 1 only)
- The element number or element set name

Before program execution, compile and link the C++ program using the **abaqus make** utility:

.. code-block:: sh
    
    abaqus make job=felbow.C

After successful compilation, the program's object code is linked automatically with the Abaqus object codes stored in the shared program library and interface library to build the executable program. Refer to `Customizing the Abaqus environment <https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEILGRefMap/simailg-m-Environment-sb.htm?contextscope=all>`_ to see which compile and link commands are used for a particular computer.

Before executing the program, run an analysis that creates an output database file containing the appropriate output. This analysis includes, for example, output for the elements and the integration point coordinates of the elements. Execute the program using the following command:

.. code-block:: sh
    
    abaqus felbow <filename.odb>

The program prompts for other information, such as the desired postprocessing option, part name, etc. The program processes the data and produces a text file or a new output database file that contains the information required to visualize the elbow element results.

`Elastic-plastic collapse of a thin-walled elbow under in-plane bending and internal pressure <https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEEXARefMap/simaexa-c-elbowcollapse.htm?contextscope=all>`_ contains several figures that can be created with the aid of this program.
