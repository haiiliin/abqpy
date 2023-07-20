# Improving the efficiency of your scripts

If you are accessing large amounts of data from an output database, you should be aware of potential inefficiencies in your script and techniques that will help to speed up your scripts.

To improve the efficiency of scripts that access an output database, you should create objects that will be used to hold temporary variables that are accessed multiple times while the script is executing. For example, if the script accesses the temporary variable while inside a loop that is executed many times, creating an object to hold the variable will speed up your script significantly.

The following example examines the von Mises stress in each element during a particular frame of field output. If the stress is greater than a certain maximum value, the script prints the strain components for the element.

```python2
stressField = frame.fieldOutputs['MISES']
strainField = frame.fieldOutputs['LE']
count = 0
for v in stressField.values:
    if v.mises > stressCap:
        if v.integrationPoint:
            print 'Element label = ', v.elementLabel, \
                'Integration Point = ', v.integrationPoint
        else:
            print 'Element label = ', v.elementLabel
        for component in strainField.values[count].data:
            print '%-10.5f' % component,
        print
    count = count + 1
```

In this example every time the script accesses a strain component from **strainField.value**, Abaqus must reconstruct the sequence of FieldValue objects. This reconstruction could result in a significant performance degradation, particularly for a large model.

A slight change in the script greatly improves its performance, as shown in the following example:

```python2
stressField = frame.fieldOutputs['MISES']
strainFieldValues = frame.fieldOutputs['LE'].values
count = 0
for v in stressField.values:
    if v.mises > stressCap:
        if v.integrationPoint:
            print 'Element label = ', v.elementLabel, \
                'Integration Point = ', v.integrationPoint
        else:
            print 'Element label = ', v.elementLabel
        for component in strainFieldValues[count].data:
            print '%-10.5f' % component,
        print
    count = count + 1
```

The second script replaces the statement strainField = frame.fieldOutputs\['LE'\] with the statement strainFieldValues = frame.fieldOutputs\['LE'\].values. As a result, Abaqus does not need to reconstruct the sequence of FieldValue objects each time the script accesses a strain component.

Similarly, if you expect to retrieve more than one frame from an output database, you should create a temporary variable that holds the entire frame repository. You can then provide the logic to retrieve the desired frames from the repository and avoid recreating the repository each time. For example, executing the following statements could be very slow:

```python2
for i in range(len(odb.steps[name].frames)-1):
    frame[i] = odb.steps[name].frames[i]
```

Creating a temporary variable to hold the frame repository provides the same functionality and speeds up the process:

```python2
frameRepository = odb.steps[name].frames
for i in range(len(frameRepository)-1):
    frame[i] = frameRepository[i]
```

Such a potential loss of performance will not be a problem when accessing a load case frame. Accessing a load case frame does not result in the creation of a frame repository and, thus, does not suffer from a corresponding loss of performance.
