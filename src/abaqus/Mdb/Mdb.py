from abaqusConstants import *
from ..Job.JobMdb import JobMdb
from ..Model.Model import Model
from ..Part.AcisMdb import AcisMdb


class Mdb(AcisMdb, JobMdb):
    """The Mdb object is the high-level Abaqus model database. A model database stores models
    and analysis controls.

    Attributes
    ----------
    version: int
        An Int specifying the release number of the :py:class:`~abaqus.Mdb.Mdb.Mdb` object in memory.
    lastChangedCount: float
        A Float specifying the value of a counter associated with the :py:class:`~abaqus.abaqus.Mdb` object. The counter
        indicates when the :py:class:`~abaqus.Mdb.Mdb.Mdb` object was last changed.
    jobs: dict[str, Job]
        A repository of :py:class:`~abaqus.Job.Job.Job` objects.
    adaptivityProcesses: dict[str, AdaptivityProcess]
        A repository of :py:class:`~abaqus.Adaptivity.AdaptivityProcess.AdaptivityProcess` objects.
    coexecutions: dict[str, Coexecution]
        A repository of :py:class:`~abaqus.Job.Coexecution.Coexecution` objects.
    optimizationProcesses: dict[str, OptimizationProcess]
        A repository of :py:class:`~abaqus.Job.OptimizationProcess.OptimizationProcess` objects.
    meshEditOptions: MeshEditOptions
        A :py:class:`~abaqus.EditMesh.MeshEditOptions.MeshEditOptions` object specifying the undo/redo behavior when editing meshes on parts
        or part instances.
    models: dict[str, Model]
        A repository of :py:class:`~abaqus.Model.Model.Model` objects.
    customData: RepositorySupport
        A :py:class:`~abaqus.CustomKernel.RepositorySupport.RepositorySupport` object.
    annotations: dict[str, Annotation]
        A repository of :py:class:`~abaqus.Annotation.Annotation.Annotation` objects.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        mdb
    """

    def Model(
        self,
        name: str,
        description: str = "",
        stefanBoltzmann: float = None,
        absoluteZero: float = None,
        waveFormulation: SymbolicConstant = NOT_SET,
        modelType: SymbolicConstant = STANDARD_EXPLICIT,
        universalGas: float = None,
        copyConstraints: Boolean = ON,
        copyConnectors: Boolean = ON,
        copyInteractions: Boolean = ON,
    ) -> Model:
        """This method creates a Model object.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

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
            A Model object
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
