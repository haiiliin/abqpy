# Copying, deleting, and renaming Abaqus Scripting Interface objects

The following section describes how you copy and delete Abaqus Scripting Interface objects.

## Creating a copy of an object

Most Abaqus objects have a method that creates a copy of the object. The same command provides the name of the new object. Methods that create a copy of an object are called copy constructors. Although copy constructors exist for most objects, in most cases they are not documented in the Abaqus Scripting Reference Guide. The format of a copy constructor is

```python2
ObjectName(name='name', objectToCopy=objectToBeCopied)
```

A copy constructor returns an object of the type of objectToBeCopied with the given name. For example, the following statements show you can create a Part object and then use a copy constructor to create a second Part object that is a copy of the first:

```python2
firstBolt = mdb.models['Metric'].Part(
    name='boltPattern', dimensionality=THREE_D,
    type=DEFORMABLE_BODY)
secondBolt = mdb.models['Metric'].Part(
    name='newBoltPattern', objectToCopy=firstBolt)
```

You can also use the copy constructor to create a new object in a different model.

```python2
firstBolt = mdb.models['Metric'].Part(
    name='boltPattern', dimensionality=THREE_D,
    type=DEFORMABLE_BODY)
secondBolt = mdb.models['SAE'].Part(
    name='boltPattern', objectToCopy=firstBolt)
```

## More on copying objects

To create a copy of an object, some objects use the base type described in Abstract base type. For example, to copy a HomogeneousSolidSection object, you use the abstract base type Section constructor.

```python2
import material
import section
impactModel = mdb.Model(name='Model A')
mySteel = impactModel.Material(name='Steel')

# Create a section

firstSection = impactModel.HomogeneousSolidSection(
    name='steelSection 1', material='Steel',
    thickness=1.0)

# Copy the section

secondSection = impactModel.Section(
    name='steelSection 2', objectToCopy=firstSection)
```

## Deleting objects

In general, if you can create an object, you can delete the object. For example, the following statements create a Material object in the material repository:

```python2
myMaterial = mdb.models['Model-1'].Material(name='aluminum')
```

You can use the Python del statement to delete an object, but you must provide the full path to the object.

```python2
del mdb.models['Model-1'].materials['aluminum']
```

The variable myMaterial that referred to the object still exists; however, the variable no longer refers to the object. You can use the del statement to delete the variable.

```python2
del myMaterial
```

Conversely, if you create the object as before but delete the variable that referred to the object, only the variable is deleted; the object still exists. You can assign a new variable to the object.

```python2
myMaterial = mdb.models['Model-1'].Material(name='aluminum')
del myMaterial
myNewMaterial = mdb.models['Model-1'].materials['aluminum']
```

The previous explanation does not apply to the few Abaqus/CAE objects that are not members of either an Mdb object or a Session object; for example, XYData and Leaf objects. These objects are sometimes referred to as temporary, and the delete semantics for these objects are the same as for standard Python objects. The object exists as long as there is a reference to it. If you delete the reference, the object is also deleted.

## Renaming objects

When you rename an object, variables that refer to that object may become stale, depending on the implementation detail of that object interface. It is always best to create new variables after you rename an object.
