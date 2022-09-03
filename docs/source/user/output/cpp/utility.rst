=================
Utility interface
=================

The Abaqus C++ API provides a set of utilities that allow a user to access certain commonly used functionality (such as strings, sequences (lists), and repositories) quickly and easily using a set of supported and maintained interfaces.

The following interface classes are provided:

- **Strings**

  The odb_String object provides a convenient means of storing and passing strings. The odb_String object also provides a simple interface to append and modify the data stored in the string.

- **Sequences**

  An odb_Sequence class is a container used to hold an ordered list of objects of a specific type. Data can be appended and retrieved from the sequence.The following odb_Sequence objects are provided to store integer, float, and enumeration data:odb_SequenceIntodb_SequenceFloatodb_SequenceStringodb_SequenceInvariantodb_SequenceElementFaceSequences of sequences are also available in the following forms:odb_SequenceSequenceFloatodb_SequenceSequenceSequenceFloatodb_SequenceSequenceIntodb_SequenceSequenceElementFaceThe following Abaqus objects are also stored as sequences:odb_SequenceNodeodb_SequenceElementodb_SequenceFieldValueodb_SequenceFrameodb_SequenceSectionPointodb_SequenceLoadCaseThe following Abaqus object can be collected in a sequence for utility operations:odb_SequenceFieldOutput

- **Repositories**

  Repositories are provided to store objects retrieved by name. Both the repositories and the content of the repositories are created by the API; the user can only retrieve objects from repositories. Iterators are provided to navigate the repositories.The following Abaqus repositories are provided:odb_PartRepositoryodb_FieldOutputRepositoryodb_SectionCategoryRepositoryodb_HistoryRegionRepositoryodb_SetRepositoryodb_HistoryOutputRepositoryodb_StepRepositoryodb_InstanceRepository

More detail on these interface utility objects can be found in :doc:`/reference/odb`.

Utility interface examples
--------------------------

The following examples demonstrate the utility interface for each of the utility interface classes discussed:

- **Strings**
  
  .. code-block:: cpp
    
      odb_String type = stressField.baseElementTypes()[0];
      odb_String elementType = 
        odb_String("Element type is ") + type;
      cout << elementType.CStr() << endl; 
 
- **Sequences**
  
  .. code-block:: cpp
    
      odb_Set& mySurface = rootAssy.surfaces()["TARGET"]; 
      const odb_String instanceName = "PART-1-1";
      const odb_SequenceElementFace allFaces = 
          mySurface.faces(instanceName);
      odb_SequenceSequenceElementFace newFaces;
      int allFaces_size = allFaces.size();
      for (int i=0; i<allFaces_size; i++) {
          const odb_SequenceElementFace fList = allFaces[i];
          odb_SequenceElementFace newList;
          int fList_size = fList.size();
          for (int j=0; j<fList_size; j++) {
              const odb_Enum::odb_ElementFaceEnum face = fList[j];
              newList.append(face);
          }
          newFaces.append(newList);
      }
 
- **Repositories**
  
  .. code-block:: cpp
    
      odb_StepRepository stepCon = odb.steps();
      odb_StepRepositoryIT iter (stepCon);
      for (iter.first(); !iter.isDone(); iter.next()) {
          cout << "step name : " << iter.currentKey().CStr() << endl;
          const odb_Step& step = iter.currentValue();
          cout << "step description : " << step.description().CStr();
          cout << endl;
      }
