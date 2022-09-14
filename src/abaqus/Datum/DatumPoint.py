from abqpy.decorators import abaqus_class_doc
from .Datum import Datum


@abaqus_class_doc
class DatumPoint(Datum):
    """The DatumPoint object has no direct constructor; it is created when a Feature object is
    created. For example, the DatumPointByCoordinate method creates a Feature object that
    creates a DatumPoint object.
    The DatumPoint object is derived from the Datum object.

    .. note:: 
        This object can be accessed by::

            import part
            mdb.models[name].parts[name].datums[i]
            import assembly
            mdb.models[name].rootAssembly.allInstances[name].datums[i]
            mdb.models[name].rootAssembly.datums[i]
            mdb.models[name].rootAssembly.instances[name].datums[i]
    """

    #: A tuple of Floats specifying the **X**-, **Y**-, and **Z**-coordinates of a point located on
    #: the datum.
    pointOn: float = None
