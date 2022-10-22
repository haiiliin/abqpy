from typing_extensions import Literal
from typing import Optional

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from ..Job.JobMdb import JobMdb
from ..Model.Model import Model
from ..Part.AcisMdb import AcisMdb
from ..UtilityAndView.abaqusConstants import abaqusConstants as C
from ..UtilityAndView.abaqusConstants import (Boolean, NOT_SET, ON, STANDARD_EXPLICIT,
                                              SymbolicConstant)


@abaqus_class_doc
class Mdb(AcisMdb, JobMdb):
    """The Mdb object is the high-level Abaqus model database. A model database stores models
    and analysis controls.

    .. note:: 
        This object can be accessed by::

            mdb
    """

    @abaqus_method_doc
    def Model(
        self,
        name: str,
        description: str = "",
        stefanBoltzmann: Optional[float] = None,
        absoluteZero: Optional[float] = None,
        waveFormulation: Literal[C.SCATTERED, C.NOT_SET, C.TOTAL] = NOT_SET,
        modelType: Literal[C.STANDARD_EXPLICIT, C.ELECTROMAGNETIC] = STANDARD_EXPLICIT,
        universalGas: Optional[float] = None,
        copyConstraints: Boolean = ON,
        copyConnectors: Boolean = ON,
        copyInteractions: Boolean = ON,
    ) -> Model:
        """This method creates a Model object.

        .. note:: 
            This function can be accessed by::

                mdb.Model

        Parameters
        ----------
        name
            A String specifying the repository key.
        description
            A String specifying the purpose and contents of the Model object. The default value is
            an empty string.
        stefanBoltzmann
            None or a Float specifying the Stefan-Boltzmann constant. The default value is None.
        absoluteZero
            None or a Float specifying the absolute zero constant. The default value is None.
        waveFormulation
            A SymbolicConstant specifying the type of incident wave formulation to be used in
            acoustic problems. Possible values are NOT_SET, SCATTERED, and TOTAL. The default value
            is NOT_SET.
        modelType
            A SymbolicConstant specifying the analysis model type. Possible values are
            STANDARD_EXPLICIT and ELECTROMAGNETIC. The default is STANDARD_EXPLICIT.
        universalGas
            None or a Float specifying the universal gas constant. The default value is None.
        copyConstraints
            A boolean specifying whether to copy the constraints created in the model to the model
            that instances this model. The default value is ON.
        copyConnectors
            A boolean specifying whether to copy the connectors created in the model to the model
            that instances this model. The default value is ON.
        copyInteractions
            A boolean specifying whether to copy the interactions created in the model to the model
            that instances this model. The default value is ON.

        Returns
        -------
        model: Model
            A :py:class:`~abaqus.Model.Model.Model` object
        """
        self.models[name] = model = Model(
            name,
            description,
            stefanBoltzmann,
            absoluteZero,
            waveFormulation,
            modelType,
            universalGas,
            copyConstraints,
            copyConnectors,
            copyInteractions,
        )
        return model
