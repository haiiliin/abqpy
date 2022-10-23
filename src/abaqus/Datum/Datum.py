from abqpy.decorators import abaqus_class_doc


@abaqus_class_doc
class Datum:
    """The Datum object is the abstract base type for other Datum objects. The Datum object has
    no explicit constructor. The methods and members of the Datum object are common to all
    objects derived from the Datum.

    .. note::
        This object can be accessed by::

            import part
            mdb.models[name].parts[name].datums[i]
            import assembly
            mdb.models[name].rootAssembly.allInstances[name].datums[i]
            mdb.models[name].rootAssembly.datums[i]
            mdb.models[name].rootAssembly.instances[name].datums[i]
            mdb.models[name].rootAssembly.modelInstances[i].datums[i]
    """

    ...
