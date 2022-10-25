# Exception handling in an output database

Python exception handling in the output database is identical to that in the model database. Python exception handling is described in {ref}`exception-handling`.

The exceptions thrown are of type OdbError; for example, the following script catches exceptions thrown when the python interface in not successful in opening an output database:

```python2
invalidOdbName = "invalid.odb"
try:
    myOdb = openOdb(invalidOdbName)
except OdbError,e:
    print 'Abaqus error message: %s' % str(e)
    print 'customized error message here'
except:
    print 'Unknown Exception. '
```
