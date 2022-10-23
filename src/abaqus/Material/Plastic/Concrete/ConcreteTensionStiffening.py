from typing_extensions import Literal
from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from ....UtilityAndView.abaqusConstants import abaqusConstants as C
from ....UtilityAndView.abaqusConstants import Boolean, OFF, STRAIN


@abaqus_class_doc
class ConcreteTensionStiffening:
    r"""The ConcreteTensionStiffening object specifies hardening for the concrete damaged
    plasticity model.

    .. note:: 
        This object can be accessed by::

            import material
            mdb.models[name].materials[name].concreteDamagedPlasticity.concreteTensionStiffening
            import odbMaterial
            session.odbs[name].materials[name].concreteDamagedPlasticity.concreteTensionStiffening

        The table data for this object are:

        - If **type** = STRAIN, the table data specify the following:
        
            - Remaining direct stress after cracking, :math:`\sigma_{t}`.
            - Direct cracking strain, :math:`\epsilon_{t}^{c k}`.
            - Direct cracking strain rate, :math:`\dot{\epsilon}_{t}^{c k}`.
            - Temperature, if the data depend on temperature.
            - Value of the first field variable, if the data depend on field variables.
            - Value of the second field variable.
            - Etc.
        - If **type** = DISPLACEMENT, the table data specify the following:
        
            - Remaining direct stress after cracking, :math:`\sigma_{t}`.
            - Direct cracking displacement, :math:`u_{t}^{c k}`.
            - Direct cracking displacement rate, :math:`\dot{u}_{t}^{c k}`.
            - Temperature, if the data depend on temperature.
            - Value of the first field variable, if the data depend on field variables.
            - Value of the second field variable.
            - Etc.
        - If **type** = GFI, the table data specify the following:
        
            - Failure stress, :math:`\sigma_{t 0}`
            - Fracture energy, :math:`G_{f}`.
            - Direct cracking displacement rate, :math:`\dot{u}_{t}^{c k}`.
            - Temperature, if the data depend on temperature.
            - Value of the first field variable, if the data depend on field variables.
            - Value of the second field variable.
            - Etc.

        The corresponding analysis keywords are:

        - CONCRETE TENSION STIFFENING
    """

    @abaqus_method_doc
    def __init__(
        self,
        table: tuple,
        rate: Boolean = OFF,
        type: Literal[C.STRAIN, C.GFI, C.DISPLACEMENT] = STRAIN,
        temperatureDependency: Boolean = OFF,
        dependencies: int = 0,
    ):
        """This method creates a ConcreteTensionStiffening object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].materials[name].concreteDamagedPlasticity.ConcreteTensionStiffening.ConcreteTensionStiffeningials[name].concreteDamagedPlasticity.ConcreteTensionStiffening
            
        Parameters
        ----------
        table
            A sequence of sequences of Floats specifying the items described below. 
        rate
            A Boolean specifying whether the data depend on rate. The default value is OFF. 
        type
            A SymbolicConstant specifying the type of postcracking behavior data. Possible values 
            are: 
            
            - STRAIN, specifying postfailure stress as a function of cracking strain. 
            - DISPLACEMENT, specifying postfailure stress as a function of cracking displacement. 
            - GFI, specifying failure stress as a function of the fracture energy. 
            
            The default value is STRAIN. 
        temperatureDependency
            A Boolean specifying whether the data depend on temperature. The default value is OFF. 
        dependencies
            An Int specifying the number of field variable dependencies. The default value is 0. 

        Returns
        -------
        ConcreteTensionStiffening
            A :py:class:`~abaqus.Material.Plastic.Concrete.ConcreteTensionStiffening.ConcreteTensionStiffening` object. 

        Raises
        ------
        RangeError
        """
        ...

    @abaqus_method_doc
    def setValues(self, *args, **kwargs):
        """This method modifies the ConcreteTensionStiffening object.

        Raises
        ------
        RangeError
        """
        ...
