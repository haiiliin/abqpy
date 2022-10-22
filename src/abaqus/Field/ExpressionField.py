from typing import Optional

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from .AnalyticalField import AnalyticalField


@abaqus_class_doc
class ExpressionField(AnalyticalField):
    """The ExpressionField object defines a spatially varying field whose value is calculated
    from a user-supplied mathematical expression.
    The ExpressionField object is derived from the AnalyticalField object.

    .. note:: 
        This object can be accessed by::

            import fields
            mdb.models[name].analyticalFields[name]
    """

    #: A String specifying the repository key.
    name: str

    #: A String specifying the Python expression to evaluate in space. Variables are X, Y, and
    #: Z; R, Th, and Z; or R, Th, and P based on the selected coordinate system.
    expression: str

    #: None or a DatumCsys object specifying the local coordinate system of the field. If
    #: **localCsys** = None, the field is defined in the global coordinate system. The default
    #: value is None.
    localCsys: Optional[str] = None

    #: A String specifying the description of the field. The default value is an empty string.
    description: str = ""

    @abaqus_method_doc
    def __init__(
        self, name: str, expression: str, localCsys: Optional[str] = None, description: str = ""
    ):
        """This method creates an ExpressionField object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].ExpressionField

        Parameters
        ----------
        name
            A String specifying the repository key.
        expression
            A String specifying the Python expression to evaluate in space. Variables are X, Y, and
            Z; R, Th, and Z; or R, Th, and P based on the selected coordinate system.
        localCsys
            None or a DatumCsys object specifying the local coordinate system of the field. If
            **localCsys** = None, the field is defined in the global coordinate system. The default
            value is None.
        description
            A String specifying the description of the field. The default value is an empty string.

        Returns
        -------
        ExpressionField
            An :py:class:`~abaqus.Field.ExpressionField.ExpressionField` object.

        Raises
        ------
        TextException
        """
        super().__init__()

    @abaqus_method_doc
    def setValues(self, localCsys: Optional[str] = None, description: str = ""):
        """This method modifies the ExpressionField object.

        Parameters
        ----------
        localCsys
            None or a DatumCsys object specifying the local coordinate system of the field. If
            **localCsys** = None, the field is defined in the global coordinate system. The default
            value is None.
        description
            A String specifying the description of the field. The default value is an empty string.
        """
        ...
