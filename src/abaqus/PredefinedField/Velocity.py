from abaqusConstants import *
from .PredefinedField import PredefinedField
from ..Region.Region import Region


class Velocity(PredefinedField):
    """The Velocity object stores the data for an initial velocity predefined field.
    The Velocity object is derived from the PredefinedField object.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import load
        mdb.models[name].predefinedFields[name]

    The corresponding analysis keywords are:

    - INITIAL CONDITIONS

    """

    def __init__(
        self,
        name: str,
        region: Region,
        velocity1: float,
        velocity2: float,
        velocity3: float,
        omega: float,
        axisBegin: tuple,
        axisEnd: tuple,
        field: str = "",
        distributionType: SymbolicConstant = MAGNITUDE,
    ):
        """This method creates a Velocity predefined field object.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            mdb.models[name].Velocity

        Parameters
        ----------
        name
            A String specifying the repository key.
        region
            A Region object specifying the region to which the predefined field is applied.
        velocity1
            A Float specifying the first component of the velocity.
        velocity2
            A Float specifying the second component of the velocity.
        velocity3
            A Float specifying the third component of the velocity.
        omega
            A Float specifying the angular velocity.
        axisBegin
            A sequence of Floats specifying the *X-*, *Y-*, and **Z**- coordinates of the starting
            point of the axis about which **omega** is defined.
        axisEnd
            A sequence of Floats specifying the *X-*, *Y-*, and **Z**- coordinates of the end point of
            the axis about which **omega** is defined.
        field
            A String specifying the name of the AnalyticalField object associated with this
            predefined field. The **field** argument applies only when
            **distributionType**=FIELD_ANALYTICAL. The default value is an empty string.
        distributionType
            A SymbolicConstant specifying whether the load is uniform. Possible values are MAGNITUDE
            and FIELD_ANALYTICAL. The default value is MAGNITUDE.

        Returns
        -------
            A Velocity object.
        """
        super().__init__()
        pass

    def setValues(
        self, field: str = "", distributionType: SymbolicConstant = MAGNITUDE
    ):
        """This method modifies the Velocity object.

        Parameters
        ----------
        field
            A String specifying the name of the AnalyticalField object associated with this
            predefined field. The **field** argument applies only when
            **distributionType**=FIELD_ANALYTICAL. The default value is an empty string.
        distributionType
            A SymbolicConstant specifying whether the load is uniform. Possible values are MAGNITUDE
            and FIELD_ANALYTICAL. The default value is MAGNITUDE.
        """
        pass
