from typing import Dict, Optional

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from .AdaptivityIteration import AdaptivityIteration
from ..Job.ModelJob import ModelJob
from ..UtilityAndView.abaqusConstants import Boolean, OFF, SymbolicConstant


@abaqus_class_doc
class AdaptivityProcess:
    """The AdaptivityProcess object defines a series of jobs that will be submitted for
    analysis. Abaqus performs adaptive remeshing between each job.

    .. note:: 
        This object can be accessed by::

            import job
            mdb.adaptivityProcesses[name]
    """

    #: A SymbolicConstant specifying the status of the adaptivity process. Possible values are
    #: SUBMITTED, RUNNING, ABORTED, TERMINATED, and COMPLETED.
    status: Optional[SymbolicConstant] = None

    #: A repository of AdaptivityIteration objects specifying the AdaptivityIteration objects
    #: received during running the adaptivity process.
    iterations: Dict[int, AdaptivityIteration] = {}

    #: A String specifying the name of the Adaptivity Process.
    name: str

    #: A :py:class:`~abaqus.Job.ModelJob.ModelJob` object specifying a job to be used as the prototype for all analysis jobs run
    #: by the adaptivity process.
    job: ModelJob

    #: An Int specifying the maximum number of analysis jobs that will be run by the Adaptivity
    #: Process. Abaqus performs adaptive remeshing between each analysis. The default value is
    #: 3.
    maxIterations: int = 3

    #: A String specifying the prefix to use for jobs created by the adaptivity process. An
    #: empty string indicates that the name of the adaptivity process should be used. The
    #: default value is an empty string.
    jobPrefix: str = ""

    @abaqus_method_doc
    def __init__(
        self, name: str, job: ModelJob, maxIterations: int = 3, jobPrefix: str = ""
    ):
        """This method creates an AdaptivityProcess object.

        .. note:: 
            This function can be accessed by::

                mdb.AdaptivityProcess

        Parameters
        ----------
        name
            A String specifying the name of the Adaptivity Process.
        job
            A :py:class:`~abaqus.Job.ModelJob.ModelJob` object specifying a job to be used as the prototype for all analysis jobs run
            by the adaptivity process.
        maxIterations
            An Int specifying the maximum number of analysis jobs that will be run by the Adaptivity
            Process. Abaqus performs adaptive remeshing between each analysis. The default value is
            3.
        jobPrefix
            A String specifying the prefix to use for jobs created by the adaptivity process. An
            empty string indicates that the name of the adaptivity process should be used. The
            default value is an empty string.

        Returns
        -------
        AdaptivityProcess
            An :py:class:`~abaqus.Adaptivity.AdaptivityProcess.AdaptivityProcess` object.

        Raises
        ------
        AbaqusException
        """
        ...

    @abaqus_method_doc
    def submit(
        self,
        waitForCompletion: Boolean = OFF,
        datacheckJob: Boolean = False,
        continueJob: Boolean = False,
    ):
        """This method begins the process of analysis and adaptive remeshing.

        Parameters
        ----------
        waitForCompletion
            A Boolean specifying whether to interrupt the execution of a script until the end of the
            adaptive remeshing process is reached.
        datacheckJob
            A Boolean specifying whether to run the adaptivity as a datacheck analysis. The default
            value is False. The datacheckJob and continueJob arguments cannot both be True.
        continueJob
            A Boolean specifying whether to run the adaptivity as a continuation analysis. The
            default value is False. The datacheckJob and continueJob arguments cannot both be True.
        """
        ...

    @abaqus_method_doc
    def setValues(self, maxIterations: int = 3, jobPrefix: str = ""):
        """This method modifies the AdaptivityProcess object.

        Parameters
        ----------
        maxIterations
            An Int specifying the maximum number of analysis jobs that will be run by the Adaptivity
            Process. Abaqus performs adaptive remeshing between each analysis. The default value is
            3.
        jobPrefix
            A String specifying the prefix to use for jobs created by the adaptivity process. An
            empty string indicates that the name of the adaptivity process should be used. The
            default value is an empty string.
        """
        ...

    @abaqus_method_doc
    def AdaptivityIteration(
        self,
        iteration: int,
        jobName: str,
        modelName: str,
        odbPath: str,
        remeshingErrors: int,
    ) -> AdaptivityIteration:
        """This method creates an AdaptivityIteration object.

        .. note:: 
            This function can be accessed by::

                mdb.AdaptivityProcess

        Parameters
        ----------
        iteration
            An Int specifying the sequence number for this iteration in the adaptivity process.
        jobName
            A String specifying the name of the job that was run for this iteration.
        modelName
            A String specifying the name of the model that was analyzed and remeshed in this
            iteration.
        odbPath
            A String specifying the path to the ODB file that was created for this iteration.
        remeshingErrors
            An Int specifying the number of part instances which generated errors while remeshing
            the model in this iteration of the adaptivity process.

        Returns
        -------
        AdaptivityIteration
            An :py:class:`~abaqus.Adaptivity.AdaptivityIteration.AdaptivityIteration` object.
        """
        self.iterations[iteration] = iteration = AdaptivityIteration(
            iteration, jobName, modelName, odbPath, remeshingErrors
        )
        return iteration
