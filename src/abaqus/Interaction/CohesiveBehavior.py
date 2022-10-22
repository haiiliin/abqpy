from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from ..UtilityAndView.abaqusConstants import (ALL_NODES, Boolean, OFF, ON, SymbolicConstant,
                                              UNCOUPLED)


@abaqus_class_doc
class CohesiveBehavior:
    """The CohesiveBehaviour

    .. note:: 
        This object can be accessed by::

            import interaction
            mdb.models[name].interactionProperties[name].cohesiveBehavior

        The table data for this object are:

        - If **coupling** = UNCOUPLED, the table data specify the following:
        
            - Stiffness coefficient in the normal direction, Knn.
            - Stiffness coefficient in the first shear direction, Kss.
            - Stiffness coefficient in the second shear direction, Ktt.
            - Temperature, if the data depend on temperature.
            - Value of the first field variable, if the data depend on field variables.
            - Value of the second field variable.
            - Etc.
        - If **coupling** = COUPLED, the table data specify the following:
        
            - Stiffness coefficient in the normal direction, Knn.
            - Stiffness coefficient in the first shear direction, Kss.
            - Stiffness coefficient in the second shear direction, Ktt.
            - Coupled stiffness coefficient, Kns.
            - Coupled stiffness coefficient, Knt.
            - Coupled stiffness coefficient, Kst.
            - Temperature, if the data depend on temperature.
            - Value of the first field variable, if the data depend on field variables.
            - Value of the second field variable.
            - Etc.

        The corresponding analysis keywords are:
        
        - COHESIVE BEHAVIOR
    """

    #: A Boolean specifying whether to enforce cohesive behavior for recurrent contacts at
    #: nodes on the slave surface subsequent to ultimate failure. The default value is OFF.
    repeatedContacts: Boolean = OFF

    #: A SymbolicConstant specifying the eligible slave nodes. Possible values are
    #: ALL_NODES, INITIAL_NODES, and SPECIFIED. The default value is ALL_NODES.
    eligibility: SymbolicConstant = ALL_NODES

    #: A Boolean specifying whether to use the default contact penalties. The default value is
    #: ON.
    defaultPenalties: Boolean = ON

    #: A SymbolicConstant specifying whether the traction-separation coefficients are coupled
    #: or uncoupled. This argument is valid only for **defaultPenalties** = OFF. Possible values
    #: are UNCOUPLED and COUPLED. The default value is UNCOUPLED.
    coupling: SymbolicConstant = UNCOUPLED

    #: A Boolean specifying whether the coefficient data depend on temperature. This argument
    #: is valid only for **defaultPenalties** = OFF. The default value is OFF.
    temperatureDependency: Boolean = OFF

    #: An Int specifying the number of field variables. This argument is valid only for
    #: **defaultPenalties** = OFF. The default value is 0.
    dependencies: int = 0

    #: A sequence of sequences of Floats specifying the traction-separation coefficients. The
    #: items in the table data are described below. This argument is valid only for
    #: **defaultPenalties** = OFF.
    table: tuple = ()

    @abaqus_method_doc
    def __init__(
        self,
        repeatedContacts: Boolean = OFF,
        eligibility: SymbolicConstant = ALL_NODES,
        defaultPenalties: Boolean = ON,
        coupling: SymbolicConstant = UNCOUPLED,
        temperatureDependency: Boolean = OFF,
        dependencies: int = 0,
        table: tuple = (),
    ):
        """This method creates a CohesiveBehavior object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].interactionProperties[name].CohesiveBehavior

        Parameters
        ----------
        repeatedContacts
            A Boolean specifying whether to enforce cohesive behavior for recurrent contacts at
            nodes on the slave surface subsequent to ultimate failure. The default value is OFF.
        eligibility
            A SymbolicConstant specifying the eligible slave nodes. Possible values are
            ALL_NODES, INITIAL_NODES, and SPECIFIED. The default value is ALL_NODES.
        defaultPenalties
            A Boolean specifying whether to use the default contact penalties. The default value is
            ON.
        coupling
            A SymbolicConstant specifying whether the traction-separation coefficients are coupled
            or uncoupled. This argument is valid only for **defaultPenalties** = OFF. Possible values
            are UNCOUPLED and COUPLED. The default value is UNCOUPLED.
        temperatureDependency
            A Boolean specifying whether the coefficient data depend on temperature. This argument
            is valid only for **defaultPenalties** = OFF. The default value is OFF.
        dependencies
            An Int specifying the number of field variables. This argument is valid only for
            **defaultPenalties** = OFF. The default value is 0.
        table
            A sequence of sequences of Floats specifying the traction-separation coefficients. The
            items in the table data are described below. This argument is valid only for
            **defaultPenalties** = OFF.

        Returns
        -------
        CohesiveBehavior
            A :py:class:`~abaqus.Interaction.CohesiveBehavior.CohesiveBehavior` object.
        """
        ...

    @abaqus_method_doc
    def setValues(self, *args, **kwargs):
        """This method modifies the CohesiveBehavior object."""
        ...
