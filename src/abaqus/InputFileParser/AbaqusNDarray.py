from abqpy.decorators import abaqus_class_doc


@abaqus_class_doc
class AbaqusNDarray:
    """The AbaqusNDarray object is a sequence object derived from numpy.ndarray and is used to store numeric
    keyword data from an Abaqus input file. This object is similar to the numpy.ndarray object, but the numeric
    elements are returned as standard Python objects, not numpy numeric types. The numeric elements can be:

    - All ints.
    - All floats.
    - First column int, all other columns floats.

    In the last of these cases, the member **colZeroIsInt** will be True; in the other two
    cases, it will be False.
    """

    ...
